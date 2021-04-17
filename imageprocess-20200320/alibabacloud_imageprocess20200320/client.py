# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imageprocess20200320 import models as imageprocess_20200320_models
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
        self._endpoint = self.get_endpoint('imageprocess', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def classify_fnfwith_options(
        self,
        request: imageprocess_20200320_models.ClassifyFNFRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ClassifyFNFResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.ClassifyFNFResponse(),
            self.do_rpcrequest('ClassifyFNF', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def classify_fnfwith_options_async(
        self,
        request: imageprocess_20200320_models.ClassifyFNFRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ClassifyFNFResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.ClassifyFNFResponse(),
            await self.do_rpcrequest_async('ClassifyFNF', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def classify_fnf(
        self,
        request: imageprocess_20200320_models.ClassifyFNFRequest,
    ) -> imageprocess_20200320_models.ClassifyFNFResponse:
        runtime = util_models.RuntimeOptions()
        return self.classify_fnfwith_options(request, runtime)

    async def classify_fnf_async(
        self,
        request: imageprocess_20200320_models.ClassifyFNFRequest,
    ) -> imageprocess_20200320_models.ClassifyFNFResponse:
        runtime = util_models.RuntimeOptions()
        return await self.classify_fnfwith_options_async(request, runtime)

    def classify_fnfadvance(
        self,
        request: imageprocess_20200320_models.ClassifyFNFAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ClassifyFNFResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
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
        classify_fnfreq = imageprocess_20200320_models.ClassifyFNFRequest()
        OpenApiUtilClient.convert(request, classify_fnfreq)
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
        classify_fnfreq.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        classify_fnfresp = self.classify_fnfwith_options(classify_fnfreq, runtime)
        return classify_fnfresp

    async def classify_fnfadvance_async(
        self,
        request: imageprocess_20200320_models.ClassifyFNFAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ClassifyFNFResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
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
        classify_fnfreq = imageprocess_20200320_models.ClassifyFNFRequest()
        OpenApiUtilClient.convert(request, classify_fnfreq)
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
        classify_fnfreq.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        classify_fnfresp = await self.classify_fnfwith_options_async(classify_fnfreq, runtime)
        return classify_fnfresp

    def detect_lung_nodule_with_options(
        self,
        request: imageprocess_20200320_models.DetectLungNoduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectLungNoduleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectLungNoduleResponse(),
            self.do_rpcrequest('DetectLungNodule', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_lung_nodule_with_options_async(
        self,
        request: imageprocess_20200320_models.DetectLungNoduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectLungNoduleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectLungNoduleResponse(),
            await self.do_rpcrequest_async('DetectLungNodule', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_lung_nodule(
        self,
        request: imageprocess_20200320_models.DetectLungNoduleRequest,
    ) -> imageprocess_20200320_models.DetectLungNoduleResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_lung_nodule_with_options(request, runtime)

    async def detect_lung_nodule_async(
        self,
        request: imageprocess_20200320_models.DetectLungNoduleRequest,
    ) -> imageprocess_20200320_models.DetectLungNoduleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_lung_nodule_with_options_async(request, runtime)

    def run_ctregistration_with_options(
        self,
        request: imageprocess_20200320_models.RunCTRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.RunCTRegistrationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.RunCTRegistrationResponse(),
            self.do_rpcrequest('RunCTRegistration', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_ctregistration_with_options_async(
        self,
        request: imageprocess_20200320_models.RunCTRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.RunCTRegistrationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.RunCTRegistrationResponse(),
            await self.do_rpcrequest_async('RunCTRegistration', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_ctregistration(
        self,
        request: imageprocess_20200320_models.RunCTRegistrationRequest,
    ) -> imageprocess_20200320_models.RunCTRegistrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_ctregistration_with_options(request, runtime)

    async def run_ctregistration_async(
        self,
        request: imageprocess_20200320_models.RunCTRegistrationRequest,
    ) -> imageprocess_20200320_models.RunCTRegistrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_ctregistration_with_options_async(request, runtime)

    def translate_med_with_options(
        self,
        request: imageprocess_20200320_models.TranslateMedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.TranslateMedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.TranslateMedResponse(),
            self.do_rpcrequest('TranslateMed', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def translate_med_with_options_async(
        self,
        request: imageprocess_20200320_models.TranslateMedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.TranslateMedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.TranslateMedResponse(),
            await self.do_rpcrequest_async('TranslateMed', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def translate_med(
        self,
        request: imageprocess_20200320_models.TranslateMedRequest,
    ) -> imageprocess_20200320_models.TranslateMedResponse:
        runtime = util_models.RuntimeOptions()
        return self.translate_med_with_options(request, runtime)

    async def translate_med_async(
        self,
        request: imageprocess_20200320_models.TranslateMedRequest,
    ) -> imageprocess_20200320_models.TranslateMedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.translate_med_with_options_async(request, runtime)

    def detect_spine_mriwith_options(
        self,
        request: imageprocess_20200320_models.DetectSpineMRIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectSpineMRIResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectSpineMRIResponse(),
            self.do_rpcrequest('DetectSpineMRI', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_spine_mriwith_options_async(
        self,
        request: imageprocess_20200320_models.DetectSpineMRIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectSpineMRIResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectSpineMRIResponse(),
            await self.do_rpcrequest_async('DetectSpineMRI', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_spine_mri(
        self,
        request: imageprocess_20200320_models.DetectSpineMRIRequest,
    ) -> imageprocess_20200320_models.DetectSpineMRIResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_spine_mriwith_options(request, runtime)

    async def detect_spine_mri_async(
        self,
        request: imageprocess_20200320_models.DetectSpineMRIRequest,
    ) -> imageprocess_20200320_models.DetectSpineMRIResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_spine_mriwith_options_async(request, runtime)

    def calc_cacswith_options(
        self,
        request: imageprocess_20200320_models.CalcCACSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.CalcCACSResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.CalcCACSResponse(),
            self.do_rpcrequest('CalcCACS', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def calc_cacswith_options_async(
        self,
        request: imageprocess_20200320_models.CalcCACSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.CalcCACSResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.CalcCACSResponse(),
            await self.do_rpcrequest_async('CalcCACS', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def calc_cacs(
        self,
        request: imageprocess_20200320_models.CalcCACSRequest,
    ) -> imageprocess_20200320_models.CalcCACSResponse:
        runtime = util_models.RuntimeOptions()
        return self.calc_cacswith_options(request, runtime)

    async def calc_cacs_async(
        self,
        request: imageprocess_20200320_models.CalcCACSRequest,
    ) -> imageprocess_20200320_models.CalcCACSResponse:
        runtime = util_models.RuntimeOptions()
        return await self.calc_cacswith_options_async(request, runtime)

    def detect_hip_keypoint_xray_with_options(
        self,
        request: imageprocess_20200320_models.DetectHipKeypointXRayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectHipKeypointXRayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectHipKeypointXRayResponse(),
            self.do_rpcrequest('DetectHipKeypointXRay', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_hip_keypoint_xray_with_options_async(
        self,
        request: imageprocess_20200320_models.DetectHipKeypointXRayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectHipKeypointXRayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectHipKeypointXRayResponse(),
            await self.do_rpcrequest_async('DetectHipKeypointXRay', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_hip_keypoint_xray(
        self,
        request: imageprocess_20200320_models.DetectHipKeypointXRayRequest,
    ) -> imageprocess_20200320_models.DetectHipKeypointXRayResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_hip_keypoint_xray_with_options(request, runtime)

    async def detect_hip_keypoint_xray_async(
        self,
        request: imageprocess_20200320_models.DetectHipKeypointXRayRequest,
    ) -> imageprocess_20200320_models.DetectHipKeypointXRayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_hip_keypoint_xray_with_options_async(request, runtime)

    def detect_hip_keypoint_xray_advance(
        self,
        request: imageprocess_20200320_models.DetectHipKeypointXRayAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectHipKeypointXRayResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
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
        detect_hip_keypoint_xray_req = imageprocess_20200320_models.DetectHipKeypointXRayRequest()
        OpenApiUtilClient.convert(request, detect_hip_keypoint_xray_req)
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
        detect_hip_keypoint_xray_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_hip_keypoint_xray_resp = self.detect_hip_keypoint_xray_with_options(detect_hip_keypoint_xray_req, runtime)
        return detect_hip_keypoint_xray_resp

    async def detect_hip_keypoint_xray_advance_async(
        self,
        request: imageprocess_20200320_models.DetectHipKeypointXRayAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectHipKeypointXRayResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
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
        detect_hip_keypoint_xray_req = imageprocess_20200320_models.DetectHipKeypointXRayRequest()
        OpenApiUtilClient.convert(request, detect_hip_keypoint_xray_req)
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
        detect_hip_keypoint_xray_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_hip_keypoint_xray_resp = await self.detect_hip_keypoint_xray_with_options_async(detect_hip_keypoint_xray_req, runtime)
        return detect_hip_keypoint_xray_resp

    def detect_knee_keypoint_xray_with_options(
        self,
        request: imageprocess_20200320_models.DetectKneeKeypointXRayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectKneeKeypointXRayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectKneeKeypointXRayResponse(),
            self.do_rpcrequest('DetectKneeKeypointXRay', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_knee_keypoint_xray_with_options_async(
        self,
        request: imageprocess_20200320_models.DetectKneeKeypointXRayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectKneeKeypointXRayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectKneeKeypointXRayResponse(),
            await self.do_rpcrequest_async('DetectKneeKeypointXRay', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_knee_keypoint_xray(
        self,
        request: imageprocess_20200320_models.DetectKneeKeypointXRayRequest,
    ) -> imageprocess_20200320_models.DetectKneeKeypointXRayResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_knee_keypoint_xray_with_options(request, runtime)

    async def detect_knee_keypoint_xray_async(
        self,
        request: imageprocess_20200320_models.DetectKneeKeypointXRayRequest,
    ) -> imageprocess_20200320_models.DetectKneeKeypointXRayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_knee_keypoint_xray_with_options_async(request, runtime)

    def detect_knee_keypoint_xray_advance(
        self,
        request: imageprocess_20200320_models.DetectKneeKeypointXRayAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectKneeKeypointXRayResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
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
        detect_knee_keypoint_xray_req = imageprocess_20200320_models.DetectKneeKeypointXRayRequest()
        OpenApiUtilClient.convert(request, detect_knee_keypoint_xray_req)
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
        detect_knee_keypoint_xray_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_knee_keypoint_xray_resp = self.detect_knee_keypoint_xray_with_options(detect_knee_keypoint_xray_req, runtime)
        return detect_knee_keypoint_xray_resp

    async def detect_knee_keypoint_xray_advance_async(
        self,
        request: imageprocess_20200320_models.DetectKneeKeypointXRayAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectKneeKeypointXRayResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
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
        detect_knee_keypoint_xray_req = imageprocess_20200320_models.DetectKneeKeypointXRayRequest()
        OpenApiUtilClient.convert(request, detect_knee_keypoint_xray_req)
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
        detect_knee_keypoint_xray_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_knee_keypoint_xray_resp = await self.detect_knee_keypoint_xray_with_options_async(detect_knee_keypoint_xray_req, runtime)
        return detect_knee_keypoint_xray_resp

    def run_med_qawith_options(
        self,
        request: imageprocess_20200320_models.RunMedQARequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.RunMedQAResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.RunMedQAResponse(),
            self.do_rpcrequest('RunMedQA', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_med_qawith_options_async(
        self,
        request: imageprocess_20200320_models.RunMedQARequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.RunMedQAResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.RunMedQAResponse(),
            await self.do_rpcrequest_async('RunMedQA', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_med_qa(
        self,
        request: imageprocess_20200320_models.RunMedQARequest,
    ) -> imageprocess_20200320_models.RunMedQAResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_med_qawith_options(request, runtime)

    async def run_med_qa_async(
        self,
        request: imageprocess_20200320_models.RunMedQARequest,
    ) -> imageprocess_20200320_models.RunMedQAResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_med_qawith_options_async(request, runtime)

    def detect_knee_xray_with_options(
        self,
        request: imageprocess_20200320_models.DetectKneeXRayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectKneeXRayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectKneeXRayResponse(),
            self.do_rpcrequest('DetectKneeXRay', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_knee_xray_with_options_async(
        self,
        request: imageprocess_20200320_models.DetectKneeXRayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectKneeXRayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectKneeXRayResponse(),
            await self.do_rpcrequest_async('DetectKneeXRay', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_knee_xray(
        self,
        request: imageprocess_20200320_models.DetectKneeXRayRequest,
    ) -> imageprocess_20200320_models.DetectKneeXRayResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_knee_xray_with_options(request, runtime)

    async def detect_knee_xray_async(
        self,
        request: imageprocess_20200320_models.DetectKneeXRayRequest,
    ) -> imageprocess_20200320_models.DetectKneeXRayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_knee_xray_with_options_async(request, runtime)

    def detect_knee_xray_advance(
        self,
        request: imageprocess_20200320_models.DetectKneeXRayAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectKneeXRayResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
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
        detect_knee_xray_req = imageprocess_20200320_models.DetectKneeXRayRequest()
        OpenApiUtilClient.convert(request, detect_knee_xray_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.url_object,
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
        detect_knee_xray_req.url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_knee_xray_resp = self.detect_knee_xray_with_options(detect_knee_xray_req, runtime)
        return detect_knee_xray_resp

    async def detect_knee_xray_advance_async(
        self,
        request: imageprocess_20200320_models.DetectKneeXRayAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectKneeXRayResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
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
        detect_knee_xray_req = imageprocess_20200320_models.DetectKneeXRayRequest()
        OpenApiUtilClient.convert(request, detect_knee_xray_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.url_object,
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
        detect_knee_xray_req.url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_knee_xray_resp = await self.detect_knee_xray_with_options_async(detect_knee_xray_req, runtime)
        return detect_knee_xray_resp

    def get_async_job_result_with_options(
        self,
        request: imageprocess_20200320_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.GetAsyncJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.GetAsyncJobResultResponse(),
            self.do_rpcrequest('GetAsyncJobResult', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_async_job_result_with_options_async(
        self,
        request: imageprocess_20200320_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.GetAsyncJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.GetAsyncJobResultResponse(),
            await self.do_rpcrequest_async('GetAsyncJobResult', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_async_job_result(
        self,
        request: imageprocess_20200320_models.GetAsyncJobResultRequest,
    ) -> imageprocess_20200320_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_async_job_result_with_options(request, runtime)

    async def get_async_job_result_async(
        self,
        request: imageprocess_20200320_models.GetAsyncJobResultRequest,
    ) -> imageprocess_20200320_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_async_job_result_with_options_async(request, runtime)

    def detect_rib_fracture_with_options(
        self,
        request: imageprocess_20200320_models.DetectRibFractureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectRibFractureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectRibFractureResponse(),
            self.do_rpcrequest('DetectRibFracture', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_rib_fracture_with_options_async(
        self,
        request: imageprocess_20200320_models.DetectRibFractureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectRibFractureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectRibFractureResponse(),
            await self.do_rpcrequest_async('DetectRibFracture', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_rib_fracture(
        self,
        request: imageprocess_20200320_models.DetectRibFractureRequest,
    ) -> imageprocess_20200320_models.DetectRibFractureResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_rib_fracture_with_options(request, runtime)

    async def detect_rib_fracture_async(
        self,
        request: imageprocess_20200320_models.DetectRibFractureRequest,
    ) -> imageprocess_20200320_models.DetectRibFractureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_rib_fracture_with_options_async(request, runtime)

    def detect_covid_19cad_with_options(
        self,
        request: imageprocess_20200320_models.DetectCovid19CadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectCovid19CadResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectCovid19CadResponse(),
            self.do_rpcrequest('DetectCovid19Cad', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_covid_19cad_with_options_async(
        self,
        request: imageprocess_20200320_models.DetectCovid19CadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectCovid19CadResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectCovid19CadResponse(),
            await self.do_rpcrequest_async('DetectCovid19Cad', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_covid_19cad(
        self,
        request: imageprocess_20200320_models.DetectCovid19CadRequest,
    ) -> imageprocess_20200320_models.DetectCovid19CadResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_covid_19cad_with_options(request, runtime)

    async def detect_covid_19cad_async(
        self,
        request: imageprocess_20200320_models.DetectCovid19CadRequest,
    ) -> imageprocess_20200320_models.DetectCovid19CadResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_covid_19cad_with_options_async(request, runtime)

    def screen_chest_ctwith_options(
        self,
        request: imageprocess_20200320_models.ScreenChestCTRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenChestCTResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.ScreenChestCTResponse(),
            self.do_rpcrequest('ScreenChestCT', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def screen_chest_ctwith_options_async(
        self,
        request: imageprocess_20200320_models.ScreenChestCTRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.ScreenChestCTResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.ScreenChestCTResponse(),
            await self.do_rpcrequest_async('ScreenChestCT', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def screen_chest_ct(
        self,
        request: imageprocess_20200320_models.ScreenChestCTRequest,
    ) -> imageprocess_20200320_models.ScreenChestCTResponse:
        runtime = util_models.RuntimeOptions()
        return self.screen_chest_ctwith_options(request, runtime)

    async def screen_chest_ct_async(
        self,
        request: imageprocess_20200320_models.ScreenChestCTRequest,
    ) -> imageprocess_20200320_models.ScreenChestCTResponse:
        runtime = util_models.RuntimeOptions()
        return await self.screen_chest_ctwith_options_async(request, runtime)

    def detect_skin_disease_with_options(
        self,
        request: imageprocess_20200320_models.DetectSkinDiseaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectSkinDiseaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectSkinDiseaseResponse(),
            self.do_rpcrequest('DetectSkinDisease', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_skin_disease_with_options_async(
        self,
        request: imageprocess_20200320_models.DetectSkinDiseaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectSkinDiseaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imageprocess_20200320_models.DetectSkinDiseaseResponse(),
            await self.do_rpcrequest_async('DetectSkinDisease', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_skin_disease(
        self,
        request: imageprocess_20200320_models.DetectSkinDiseaseRequest,
    ) -> imageprocess_20200320_models.DetectSkinDiseaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_skin_disease_with_options(request, runtime)

    async def detect_skin_disease_async(
        self,
        request: imageprocess_20200320_models.DetectSkinDiseaseRequest,
    ) -> imageprocess_20200320_models.DetectSkinDiseaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_skin_disease_with_options_async(request, runtime)

    def detect_skin_disease_advance(
        self,
        request: imageprocess_20200320_models.DetectSkinDiseaseAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectSkinDiseaseResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
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
        detect_skin_disease_req = imageprocess_20200320_models.DetectSkinDiseaseRequest()
        OpenApiUtilClient.convert(request, detect_skin_disease_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.url_object,
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
        detect_skin_disease_req.url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_skin_disease_resp = self.detect_skin_disease_with_options(detect_skin_disease_req, runtime)
        return detect_skin_disease_resp

    async def detect_skin_disease_advance_async(
        self,
        request: imageprocess_20200320_models.DetectSkinDiseaseAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageprocess_20200320_models.DetectSkinDiseaseResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageprocess',
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
        detect_skin_disease_req = imageprocess_20200320_models.DetectSkinDiseaseRequest()
        OpenApiUtilClient.convert(request, detect_skin_disease_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.url_object,
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
        detect_skin_disease_req.url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_skin_disease_resp = await self.detect_skin_disease_with_options_async(detect_skin_disease_req, runtime)
        return detect_skin_disease_resp
