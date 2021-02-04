# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imagerecog20190930 import models as imagerecog_20190930_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('imagerecog', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        request: imagerecog_20190930_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.GetAsyncJobResultResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return imagerecog_20190930_models.GetAsyncJobResultResponse().from_map(
            self.do_rpcrequest('GetAsyncJobResult', '2019-09-30', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_async_job_result_with_options_async(
        self,
        request: imagerecog_20190930_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.GetAsyncJobResultResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return imagerecog_20190930_models.GetAsyncJobResultResponse().from_map(
            await self.do_rpcrequest_async('GetAsyncJobResult', '2019-09-30', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_async_job_result(
        self,
        request: imagerecog_20190930_models.GetAsyncJobResultRequest,
    ) -> imagerecog_20190930_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_async_job_result_with_options(request, runtime)

    async def get_async_job_result_async(
        self,
        request: imagerecog_20190930_models.GetAsyncJobResultRequest,
    ) -> imagerecog_20190930_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_async_job_result_with_options_async(request, runtime)

    def detect_image_elements_with_options(
        self,
        request: imagerecog_20190930_models.DetectImageElementsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.DetectImageElementsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.DetectImageElementsResponse().from_map(
            self.do_rpcrequest('DetectImageElements', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_image_elements_with_options_async(
        self,
        request: imagerecog_20190930_models.DetectImageElementsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.DetectImageElementsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.DetectImageElementsResponse().from_map(
            await self.do_rpcrequest_async('DetectImageElements', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_image_elements(
        self,
        request: imagerecog_20190930_models.DetectImageElementsRequest,
    ) -> imagerecog_20190930_models.DetectImageElementsResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_image_elements_with_options(request, runtime)

    async def detect_image_elements_async(
        self,
        request: imagerecog_20190930_models.DetectImageElementsRequest,
    ) -> imagerecog_20190930_models.DetectImageElementsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_elements_with_options_async(request, runtime)

    def detect_image_elements_advance(
        self,
        request: imagerecog_20190930_models.DetectImageElementsAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.DetectImageElementsResponse:
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
            product='imagerecog',
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
        detect_image_elements_req = imagerecog_20190930_models.DetectImageElementsRequest()
        OpenApiUtilClient.convert(request, detect_image_elements_req)
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
        detect_image_elements_req.url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_image_elements_resp = self.detect_image_elements_with_options(detect_image_elements_req, runtime)
        return detect_image_elements_resp

    async def detect_image_elements_advance_async(
        self,
        request: imagerecog_20190930_models.DetectImageElementsAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.DetectImageElementsResponse:
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
            product='imagerecog',
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
        detect_image_elements_req = imagerecog_20190930_models.DetectImageElementsRequest()
        OpenApiUtilClient.convert(request, detect_image_elements_req)
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
        detect_image_elements_req.url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_image_elements_resp = await self.detect_image_elements_with_options_async(detect_image_elements_req, runtime)
        return detect_image_elements_resp

    def recognize_vehicle_type_with_options(
        self,
        request: imagerecog_20190930_models.RecognizeVehicleTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeVehicleTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.RecognizeVehicleTypeResponse().from_map(
            self.do_rpcrequest('RecognizeVehicleType', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_vehicle_type_with_options_async(
        self,
        request: imagerecog_20190930_models.RecognizeVehicleTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeVehicleTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.RecognizeVehicleTypeResponse().from_map(
            await self.do_rpcrequest_async('RecognizeVehicleType', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_vehicle_type(
        self,
        request: imagerecog_20190930_models.RecognizeVehicleTypeRequest,
    ) -> imagerecog_20190930_models.RecognizeVehicleTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_vehicle_type_with_options(request, runtime)

    async def recognize_vehicle_type_async(
        self,
        request: imagerecog_20190930_models.RecognizeVehicleTypeRequest,
    ) -> imagerecog_20190930_models.RecognizeVehicleTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_vehicle_type_with_options_async(request, runtime)

    def recognize_vehicle_type_advance(
        self,
        request: imagerecog_20190930_models.RecognizeVehicleTypeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeVehicleTypeResponse:
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
            product='imagerecog',
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
        recognize_vehicle_type_req = imagerecog_20190930_models.RecognizeVehicleTypeRequest()
        OpenApiUtilClient.convert(request, recognize_vehicle_type_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
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
        recognize_vehicle_type_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_vehicle_type_resp = self.recognize_vehicle_type_with_options(recognize_vehicle_type_req, runtime)
        return recognize_vehicle_type_resp

    async def recognize_vehicle_type_advance_async(
        self,
        request: imagerecog_20190930_models.RecognizeVehicleTypeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeVehicleTypeResponse:
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
            product='imagerecog',
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
        recognize_vehicle_type_req = imagerecog_20190930_models.RecognizeVehicleTypeRequest()
        OpenApiUtilClient.convert(request, recognize_vehicle_type_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
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
        recognize_vehicle_type_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_vehicle_type_resp = await self.recognize_vehicle_type_with_options_async(recognize_vehicle_type_req, runtime)
        return recognize_vehicle_type_resp

    def recognize_food_with_options(
        self,
        request: imagerecog_20190930_models.RecognizeFoodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeFoodResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.RecognizeFoodResponse().from_map(
            self.do_rpcrequest('RecognizeFood', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_food_with_options_async(
        self,
        request: imagerecog_20190930_models.RecognizeFoodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeFoodResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.RecognizeFoodResponse().from_map(
            await self.do_rpcrequest_async('RecognizeFood', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_food(
        self,
        request: imagerecog_20190930_models.RecognizeFoodRequest,
    ) -> imagerecog_20190930_models.RecognizeFoodResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_food_with_options(request, runtime)

    async def recognize_food_async(
        self,
        request: imagerecog_20190930_models.RecognizeFoodRequest,
    ) -> imagerecog_20190930_models.RecognizeFoodResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_food_with_options_async(request, runtime)

    def recognize_food_advance(
        self,
        request: imagerecog_20190930_models.RecognizeFoodAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeFoodResponse:
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
            product='imagerecog',
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
        recognize_food_req = imagerecog_20190930_models.RecognizeFoodRequest()
        OpenApiUtilClient.convert(request, recognize_food_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
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
        recognize_food_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_food_resp = self.recognize_food_with_options(recognize_food_req, runtime)
        return recognize_food_resp

    async def recognize_food_advance_async(
        self,
        request: imagerecog_20190930_models.RecognizeFoodAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeFoodResponse:
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
            product='imagerecog',
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
        recognize_food_req = imagerecog_20190930_models.RecognizeFoodRequest()
        OpenApiUtilClient.convert(request, recognize_food_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
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
        recognize_food_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_food_resp = await self.recognize_food_with_options_async(recognize_food_req, runtime)
        return recognize_food_resp

    def recognize_image_style_with_options(
        self,
        request: imagerecog_20190930_models.RecognizeImageStyleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeImageStyleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.RecognizeImageStyleResponse().from_map(
            self.do_rpcrequest('RecognizeImageStyle', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_image_style_with_options_async(
        self,
        request: imagerecog_20190930_models.RecognizeImageStyleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeImageStyleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.RecognizeImageStyleResponse().from_map(
            await self.do_rpcrequest_async('RecognizeImageStyle', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_image_style(
        self,
        request: imagerecog_20190930_models.RecognizeImageStyleRequest,
    ) -> imagerecog_20190930_models.RecognizeImageStyleResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_image_style_with_options(request, runtime)

    async def recognize_image_style_async(
        self,
        request: imagerecog_20190930_models.RecognizeImageStyleRequest,
    ) -> imagerecog_20190930_models.RecognizeImageStyleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_image_style_with_options_async(request, runtime)

    def recognize_image_style_advance(
        self,
        request: imagerecog_20190930_models.RecognizeImageStyleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeImageStyleResponse:
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
            product='imagerecog',
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
        recognize_image_style_req = imagerecog_20190930_models.RecognizeImageStyleRequest()
        OpenApiUtilClient.convert(request, recognize_image_style_req)
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
        recognize_image_style_req.url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_image_style_resp = self.recognize_image_style_with_options(recognize_image_style_req, runtime)
        return recognize_image_style_resp

    async def recognize_image_style_advance_async(
        self,
        request: imagerecog_20190930_models.RecognizeImageStyleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeImageStyleResponse:
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
            product='imagerecog',
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
        recognize_image_style_req = imagerecog_20190930_models.RecognizeImageStyleRequest()
        OpenApiUtilClient.convert(request, recognize_image_style_req)
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
        recognize_image_style_req.url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_image_style_resp = await self.recognize_image_style_with_options_async(recognize_image_style_req, runtime)
        return recognize_image_style_resp

    def recognize_scene_with_options(
        self,
        request: imagerecog_20190930_models.RecognizeSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.RecognizeSceneResponse().from_map(
            self.do_rpcrequest('RecognizeScene', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_scene_with_options_async(
        self,
        request: imagerecog_20190930_models.RecognizeSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.RecognizeSceneResponse().from_map(
            await self.do_rpcrequest_async('RecognizeScene', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_scene(
        self,
        request: imagerecog_20190930_models.RecognizeSceneRequest,
    ) -> imagerecog_20190930_models.RecognizeSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_scene_with_options(request, runtime)

    async def recognize_scene_async(
        self,
        request: imagerecog_20190930_models.RecognizeSceneRequest,
    ) -> imagerecog_20190930_models.RecognizeSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_scene_with_options_async(request, runtime)

    def recognize_scene_advance(
        self,
        request: imagerecog_20190930_models.RecognizeSceneAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeSceneResponse:
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
            product='imagerecog',
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
        recognize_scene_req = imagerecog_20190930_models.RecognizeSceneRequest()
        OpenApiUtilClient.convert(request, recognize_scene_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
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
        recognize_scene_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_scene_resp = self.recognize_scene_with_options(recognize_scene_req, runtime)
        return recognize_scene_resp

    async def recognize_scene_advance_async(
        self,
        request: imagerecog_20190930_models.RecognizeSceneAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeSceneResponse:
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
            product='imagerecog',
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
        recognize_scene_req = imagerecog_20190930_models.RecognizeSceneRequest()
        OpenApiUtilClient.convert(request, recognize_scene_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
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
        recognize_scene_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_scene_resp = await self.recognize_scene_with_options_async(recognize_scene_req, runtime)
        return recognize_scene_resp

    def classifying_rubbish_with_options(
        self,
        request: imagerecog_20190930_models.ClassifyingRubbishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.ClassifyingRubbishResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.ClassifyingRubbishResponse().from_map(
            self.do_rpcrequest('ClassifyingRubbish', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def classifying_rubbish_with_options_async(
        self,
        request: imagerecog_20190930_models.ClassifyingRubbishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.ClassifyingRubbishResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.ClassifyingRubbishResponse().from_map(
            await self.do_rpcrequest_async('ClassifyingRubbish', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def classifying_rubbish(
        self,
        request: imagerecog_20190930_models.ClassifyingRubbishRequest,
    ) -> imagerecog_20190930_models.ClassifyingRubbishResponse:
        runtime = util_models.RuntimeOptions()
        return self.classifying_rubbish_with_options(request, runtime)

    async def classifying_rubbish_async(
        self,
        request: imagerecog_20190930_models.ClassifyingRubbishRequest,
    ) -> imagerecog_20190930_models.ClassifyingRubbishResponse:
        runtime = util_models.RuntimeOptions()
        return await self.classifying_rubbish_with_options_async(request, runtime)

    def classifying_rubbish_advance(
        self,
        request: imagerecog_20190930_models.ClassifyingRubbishAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.ClassifyingRubbishResponse:
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
            product='imagerecog',
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
        classifying_rubbish_req = imagerecog_20190930_models.ClassifyingRubbishRequest()
        OpenApiUtilClient.convert(request, classifying_rubbish_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
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
        classifying_rubbish_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        classifying_rubbish_resp = self.classifying_rubbish_with_options(classifying_rubbish_req, runtime)
        return classifying_rubbish_resp

    async def classifying_rubbish_advance_async(
        self,
        request: imagerecog_20190930_models.ClassifyingRubbishAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.ClassifyingRubbishResponse:
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
            product='imagerecog',
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
        classifying_rubbish_req = imagerecog_20190930_models.ClassifyingRubbishRequest()
        OpenApiUtilClient.convert(request, classifying_rubbish_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
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
        classifying_rubbish_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        classifying_rubbish_resp = await self.classifying_rubbish_with_options_async(classifying_rubbish_req, runtime)
        return classifying_rubbish_resp

    def detect_fruits_with_options(
        self,
        request: imagerecog_20190930_models.DetectFruitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.DetectFruitsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.DetectFruitsResponse().from_map(
            self.do_rpcrequest('DetectFruits', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_fruits_with_options_async(
        self,
        request: imagerecog_20190930_models.DetectFruitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.DetectFruitsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.DetectFruitsResponse().from_map(
            await self.do_rpcrequest_async('DetectFruits', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_fruits(
        self,
        request: imagerecog_20190930_models.DetectFruitsRequest,
    ) -> imagerecog_20190930_models.DetectFruitsResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_fruits_with_options(request, runtime)

    async def detect_fruits_async(
        self,
        request: imagerecog_20190930_models.DetectFruitsRequest,
    ) -> imagerecog_20190930_models.DetectFruitsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_fruits_with_options_async(request, runtime)

    def detect_fruits_advance(
        self,
        request: imagerecog_20190930_models.DetectFruitsAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.DetectFruitsResponse:
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
            product='imagerecog',
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
        detect_fruits_req = imagerecog_20190930_models.DetectFruitsRequest()
        OpenApiUtilClient.convert(request, detect_fruits_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
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
        detect_fruits_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_fruits_resp = self.detect_fruits_with_options(detect_fruits_req, runtime)
        return detect_fruits_resp

    async def detect_fruits_advance_async(
        self,
        request: imagerecog_20190930_models.DetectFruitsAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.DetectFruitsResponse:
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
            product='imagerecog',
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
        detect_fruits_req = imagerecog_20190930_models.DetectFruitsRequest()
        OpenApiUtilClient.convert(request, detect_fruits_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
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
        detect_fruits_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_fruits_resp = await self.detect_fruits_with_options_async(detect_fruits_req, runtime)
        return detect_fruits_resp

    def recognize_image_color_with_options(
        self,
        request: imagerecog_20190930_models.RecognizeImageColorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeImageColorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.RecognizeImageColorResponse().from_map(
            self.do_rpcrequest('RecognizeImageColor', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_image_color_with_options_async(
        self,
        request: imagerecog_20190930_models.RecognizeImageColorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeImageColorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.RecognizeImageColorResponse().from_map(
            await self.do_rpcrequest_async('RecognizeImageColor', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_image_color(
        self,
        request: imagerecog_20190930_models.RecognizeImageColorRequest,
    ) -> imagerecog_20190930_models.RecognizeImageColorResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_image_color_with_options(request, runtime)

    async def recognize_image_color_async(
        self,
        request: imagerecog_20190930_models.RecognizeImageColorRequest,
    ) -> imagerecog_20190930_models.RecognizeImageColorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_image_color_with_options_async(request, runtime)

    def recognize_image_color_advance(
        self,
        request: imagerecog_20190930_models.RecognizeImageColorAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeImageColorResponse:
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
            product='imagerecog',
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
        recognize_image_color_req = imagerecog_20190930_models.RecognizeImageColorRequest()
        OpenApiUtilClient.convert(request, recognize_image_color_req)
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
        recognize_image_color_req.url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_image_color_resp = self.recognize_image_color_with_options(recognize_image_color_req, runtime)
        return recognize_image_color_resp

    async def recognize_image_color_advance_async(
        self,
        request: imagerecog_20190930_models.RecognizeImageColorAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeImageColorResponse:
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
            product='imagerecog',
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
        recognize_image_color_req = imagerecog_20190930_models.RecognizeImageColorRequest()
        OpenApiUtilClient.convert(request, recognize_image_color_req)
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
        recognize_image_color_req.url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_image_color_resp = await self.recognize_image_color_with_options_async(recognize_image_color_req, runtime)
        return recognize_image_color_resp

    def recognize_logo_with_options(
        self,
        request: imagerecog_20190930_models.RecognizeLogoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeLogoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.RecognizeLogoResponse().from_map(
            self.do_rpcrequest('RecognizeLogo', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_logo_with_options_async(
        self,
        request: imagerecog_20190930_models.RecognizeLogoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.RecognizeLogoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.RecognizeLogoResponse().from_map(
            await self.do_rpcrequest_async('RecognizeLogo', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_logo(
        self,
        request: imagerecog_20190930_models.RecognizeLogoRequest,
    ) -> imagerecog_20190930_models.RecognizeLogoResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_logo_with_options(request, runtime)

    async def recognize_logo_async(
        self,
        request: imagerecog_20190930_models.RecognizeLogoRequest,
    ) -> imagerecog_20190930_models.RecognizeLogoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_logo_with_options_async(request, runtime)

    def tagging_image_with_options(
        self,
        request: imagerecog_20190930_models.TaggingImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.TaggingImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.TaggingImageResponse().from_map(
            self.do_rpcrequest('TaggingImage', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tagging_image_with_options_async(
        self,
        request: imagerecog_20190930_models.TaggingImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.TaggingImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.TaggingImageResponse().from_map(
            await self.do_rpcrequest_async('TaggingImage', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tagging_image(
        self,
        request: imagerecog_20190930_models.TaggingImageRequest,
    ) -> imagerecog_20190930_models.TaggingImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.tagging_image_with_options(request, runtime)

    async def tagging_image_async(
        self,
        request: imagerecog_20190930_models.TaggingImageRequest,
    ) -> imagerecog_20190930_models.TaggingImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tagging_image_with_options_async(request, runtime)

    def tagging_image_advance(
        self,
        request: imagerecog_20190930_models.TaggingImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.TaggingImageResponse:
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
            product='imagerecog',
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
        tagging_image_req = imagerecog_20190930_models.TaggingImageRequest()
        OpenApiUtilClient.convert(request, tagging_image_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
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
        tagging_image_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        tagging_image_resp = self.tagging_image_with_options(tagging_image_req, runtime)
        return tagging_image_resp

    async def tagging_image_advance_async(
        self,
        request: imagerecog_20190930_models.TaggingImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.TaggingImageResponse:
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
            product='imagerecog',
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
        tagging_image_req = imagerecog_20190930_models.TaggingImageRequest()
        OpenApiUtilClient.convert(request, tagging_image_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
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
        tagging_image_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        tagging_image_resp = await self.tagging_image_with_options_async(tagging_image_req, runtime)
        return tagging_image_resp

    def evaluate_certificate_quality_with_options(
        self,
        request: imagerecog_20190930_models.EvaluateCertificateQualityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.EvaluateCertificateQualityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.EvaluateCertificateQualityResponse().from_map(
            self.do_rpcrequest('EvaluateCertificateQuality', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def evaluate_certificate_quality_with_options_async(
        self,
        request: imagerecog_20190930_models.EvaluateCertificateQualityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.EvaluateCertificateQualityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imagerecog_20190930_models.EvaluateCertificateQualityResponse().from_map(
            await self.do_rpcrequest_async('EvaluateCertificateQuality', '2019-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def evaluate_certificate_quality(
        self,
        request: imagerecog_20190930_models.EvaluateCertificateQualityRequest,
    ) -> imagerecog_20190930_models.EvaluateCertificateQualityResponse:
        runtime = util_models.RuntimeOptions()
        return self.evaluate_certificate_quality_with_options(request, runtime)

    async def evaluate_certificate_quality_async(
        self,
        request: imagerecog_20190930_models.EvaluateCertificateQualityRequest,
    ) -> imagerecog_20190930_models.EvaluateCertificateQualityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.evaluate_certificate_quality_with_options_async(request, runtime)

    def evaluate_certificate_quality_advance(
        self,
        request: imagerecog_20190930_models.EvaluateCertificateQualityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.EvaluateCertificateQualityResponse:
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
            product='imagerecog',
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
        evaluate_certificate_quality_req = imagerecog_20190930_models.EvaluateCertificateQualityRequest()
        OpenApiUtilClient.convert(request, evaluate_certificate_quality_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
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
        evaluate_certificate_quality_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        evaluate_certificate_quality_resp = self.evaluate_certificate_quality_with_options(evaluate_certificate_quality_req, runtime)
        return evaluate_certificate_quality_resp

    async def evaluate_certificate_quality_advance_async(
        self,
        request: imagerecog_20190930_models.EvaluateCertificateQualityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imagerecog_20190930_models.EvaluateCertificateQualityResponse:
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
            product='imagerecog',
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
        evaluate_certificate_quality_req = imagerecog_20190930_models.EvaluateCertificateQualityRequest()
        OpenApiUtilClient.convert(request, evaluate_certificate_quality_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
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
        evaluate_certificate_quality_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        evaluate_certificate_quality_resp = await self.evaluate_certificate_quality_with_options_async(evaluate_certificate_quality_req, runtime)
        return evaluate_certificate_quality_resp
