# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_goodstech20191230 import models as goodstech_20191230_models
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
        self._endpoint = self.get_endpoint('goodstech', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def classify_commodity_with_options(
        self,
        request: goodstech_20191230_models.ClassifyCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> goodstech_20191230_models.ClassifyCommodityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return goodstech_20191230_models.ClassifyCommodityResponse().from_map(
            self.do_rpcrequest('ClassifyCommodity', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def classify_commodity_with_options_async(
        self,
        request: goodstech_20191230_models.ClassifyCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> goodstech_20191230_models.ClassifyCommodityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return goodstech_20191230_models.ClassifyCommodityResponse().from_map(
            await self.do_rpcrequest_async('ClassifyCommodity', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def classify_commodity(
        self,
        request: goodstech_20191230_models.ClassifyCommodityRequest,
    ) -> goodstech_20191230_models.ClassifyCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return self.classify_commodity_with_options(request, runtime)

    async def classify_commodity_async(
        self,
        request: goodstech_20191230_models.ClassifyCommodityRequest,
    ) -> goodstech_20191230_models.ClassifyCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.classify_commodity_with_options_async(request, runtime)

    def classify_commodity_advance(
        self,
        request: goodstech_20191230_models.ClassifyCommodityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> goodstech_20191230_models.ClassifyCommodityResponse:
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
            product='goodstech',
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
        classify_commodity_req = goodstech_20191230_models.ClassifyCommodityRequest()
        OpenApiUtilClient.convert(request, classify_commodity_req)
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
        classify_commodity_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        classify_commodity_resp = self.classify_commodity_with_options(classify_commodity_req, runtime)
        return classify_commodity_resp

    async def classify_commodity_advance_async(
        self,
        request: goodstech_20191230_models.ClassifyCommodityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> goodstech_20191230_models.ClassifyCommodityResponse:
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
            product='goodstech',
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
        classify_commodity_req = goodstech_20191230_models.ClassifyCommodityRequest()
        OpenApiUtilClient.convert(request, classify_commodity_req)
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
        classify_commodity_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        classify_commodity_resp = await self.classify_commodity_with_options_async(classify_commodity_req, runtime)
        return classify_commodity_resp

    def recognize_furniture_attribute_with_options(
        self,
        request: goodstech_20191230_models.RecognizeFurnitureAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> goodstech_20191230_models.RecognizeFurnitureAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return goodstech_20191230_models.RecognizeFurnitureAttributeResponse().from_map(
            self.do_rpcrequest('RecognizeFurnitureAttribute', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_furniture_attribute_with_options_async(
        self,
        request: goodstech_20191230_models.RecognizeFurnitureAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> goodstech_20191230_models.RecognizeFurnitureAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return goodstech_20191230_models.RecognizeFurnitureAttributeResponse().from_map(
            await self.do_rpcrequest_async('RecognizeFurnitureAttribute', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_furniture_attribute(
        self,
        request: goodstech_20191230_models.RecognizeFurnitureAttributeRequest,
    ) -> goodstech_20191230_models.RecognizeFurnitureAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_furniture_attribute_with_options(request, runtime)

    async def recognize_furniture_attribute_async(
        self,
        request: goodstech_20191230_models.RecognizeFurnitureAttributeRequest,
    ) -> goodstech_20191230_models.RecognizeFurnitureAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_furniture_attribute_with_options_async(request, runtime)

    def recognize_furniture_attribute_advance(
        self,
        request: goodstech_20191230_models.RecognizeFurnitureAttributeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> goodstech_20191230_models.RecognizeFurnitureAttributeResponse:
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
            product='goodstech',
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
        recognize_furniture_attribute_req = goodstech_20191230_models.RecognizeFurnitureAttributeRequest()
        OpenApiUtilClient.convert(request, recognize_furniture_attribute_req)
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
        recognize_furniture_attribute_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_furniture_attribute_resp = self.recognize_furniture_attribute_with_options(recognize_furniture_attribute_req, runtime)
        return recognize_furniture_attribute_resp

    async def recognize_furniture_attribute_advance_async(
        self,
        request: goodstech_20191230_models.RecognizeFurnitureAttributeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> goodstech_20191230_models.RecognizeFurnitureAttributeResponse:
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
            product='goodstech',
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
        recognize_furniture_attribute_req = goodstech_20191230_models.RecognizeFurnitureAttributeRequest()
        OpenApiUtilClient.convert(request, recognize_furniture_attribute_req)
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
        recognize_furniture_attribute_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_furniture_attribute_resp = await self.recognize_furniture_attribute_with_options_async(recognize_furniture_attribute_req, runtime)
        return recognize_furniture_attribute_resp

    def recognize_furniture_spu_with_options(
        self,
        request: goodstech_20191230_models.RecognizeFurnitureSpuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> goodstech_20191230_models.RecognizeFurnitureSpuResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return goodstech_20191230_models.RecognizeFurnitureSpuResponse().from_map(
            self.do_rpcrequest('RecognizeFurnitureSpu', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_furniture_spu_with_options_async(
        self,
        request: goodstech_20191230_models.RecognizeFurnitureSpuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> goodstech_20191230_models.RecognizeFurnitureSpuResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return goodstech_20191230_models.RecognizeFurnitureSpuResponse().from_map(
            await self.do_rpcrequest_async('RecognizeFurnitureSpu', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_furniture_spu(
        self,
        request: goodstech_20191230_models.RecognizeFurnitureSpuRequest,
    ) -> goodstech_20191230_models.RecognizeFurnitureSpuResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_furniture_spu_with_options(request, runtime)

    async def recognize_furniture_spu_async(
        self,
        request: goodstech_20191230_models.RecognizeFurnitureSpuRequest,
    ) -> goodstech_20191230_models.RecognizeFurnitureSpuResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_furniture_spu_with_options_async(request, runtime)

    def recognize_furniture_spu_advance(
        self,
        request: goodstech_20191230_models.RecognizeFurnitureSpuAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> goodstech_20191230_models.RecognizeFurnitureSpuResponse:
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
            product='goodstech',
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
        recognize_furniture_spu_req = goodstech_20191230_models.RecognizeFurnitureSpuRequest()
        OpenApiUtilClient.convert(request, recognize_furniture_spu_req)
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
        recognize_furniture_spu_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_furniture_spu_resp = self.recognize_furniture_spu_with_options(recognize_furniture_spu_req, runtime)
        return recognize_furniture_spu_resp

    async def recognize_furniture_spu_advance_async(
        self,
        request: goodstech_20191230_models.RecognizeFurnitureSpuAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> goodstech_20191230_models.RecognizeFurnitureSpuResponse:
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
            product='goodstech',
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
        recognize_furniture_spu_req = goodstech_20191230_models.RecognizeFurnitureSpuRequest()
        OpenApiUtilClient.convert(request, recognize_furniture_spu_req)
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
        recognize_furniture_spu_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_furniture_spu_resp = await self.recognize_furniture_spu_with_options_async(recognize_furniture_spu_req, runtime)
        return recognize_furniture_spu_resp
