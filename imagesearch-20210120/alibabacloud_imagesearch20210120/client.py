# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imagesearch20210120 import models as image_search_20210120_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('imagesearch', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def general_recognition_with_options(
        self,
        request: image_search_20210120_models.GeneralRecognitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20210120_models.GeneralRecognitionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            image_search_20210120_models.GeneralRecognitionResponse(),
            self.do_rpcrequest('GeneralRecognition', '2021-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def general_recognition_with_options_async(
        self,
        request: image_search_20210120_models.GeneralRecognitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20210120_models.GeneralRecognitionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            image_search_20210120_models.GeneralRecognitionResponse(),
            await self.do_rpcrequest_async('GeneralRecognition', '2021-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def general_recognition(
        self,
        request: image_search_20210120_models.GeneralRecognitionRequest,
    ) -> image_search_20210120_models.GeneralRecognitionResponse:
        runtime = util_models.RuntimeOptions()
        return self.general_recognition_with_options(request, runtime)

    async def general_recognition_async(
        self,
        request: image_search_20210120_models.GeneralRecognitionRequest,
    ) -> image_search_20210120_models.GeneralRecognitionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.general_recognition_with_options_async(request, runtime)

    def general_recognition_advance(
        self,
        request: image_search_20210120_models.GeneralRecognitionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20210120_models.GeneralRecognitionResponse:
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
            product='ImageSearch',
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
        general_recognition_req = image_search_20210120_models.GeneralRecognitionRequest()
        OpenApiUtilClient.convert(request, general_recognition_req)
        if not UtilClient.is_unset(request.pic_content_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.pic_content_object,
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
            general_recognition_req.pic_content = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        general_recognition_resp = self.general_recognition_with_options(general_recognition_req, runtime)
        return general_recognition_resp

    async def general_recognition_advance_async(
        self,
        request: image_search_20210120_models.GeneralRecognitionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20210120_models.GeneralRecognitionResponse:
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
            product='ImageSearch',
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
        general_recognition_req = image_search_20210120_models.GeneralRecognitionRequest()
        OpenApiUtilClient.convert(request, general_recognition_req)
        if not UtilClient.is_unset(request.pic_content_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.pic_content_object,
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
            general_recognition_req.pic_content = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        general_recognition_resp = await self.general_recognition_with_options_async(general_recognition_req, runtime)
        return general_recognition_resp

    def image_duplication_with_options(
        self,
        request: image_search_20210120_models.ImageDuplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20210120_models.ImageDuplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            image_search_20210120_models.ImageDuplicationResponse(),
            self.do_rpcrequest('ImageDuplication', '2021-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def image_duplication_with_options_async(
        self,
        request: image_search_20210120_models.ImageDuplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20210120_models.ImageDuplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            image_search_20210120_models.ImageDuplicationResponse(),
            await self.do_rpcrequest_async('ImageDuplication', '2021-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def image_duplication(
        self,
        request: image_search_20210120_models.ImageDuplicationRequest,
    ) -> image_search_20210120_models.ImageDuplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.image_duplication_with_options(request, runtime)

    async def image_duplication_async(
        self,
        request: image_search_20210120_models.ImageDuplicationRequest,
    ) -> image_search_20210120_models.ImageDuplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.image_duplication_with_options_async(request, runtime)

    def image_segmentation_with_options(
        self,
        request: image_search_20210120_models.ImageSegmentationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20210120_models.ImageSegmentationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            image_search_20210120_models.ImageSegmentationResponse(),
            self.do_rpcrequest('ImageSegmentation', '2021-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def image_segmentation_with_options_async(
        self,
        request: image_search_20210120_models.ImageSegmentationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20210120_models.ImageSegmentationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            image_search_20210120_models.ImageSegmentationResponse(),
            await self.do_rpcrequest_async('ImageSegmentation', '2021-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def image_segmentation(
        self,
        request: image_search_20210120_models.ImageSegmentationRequest,
    ) -> image_search_20210120_models.ImageSegmentationResponse:
        runtime = util_models.RuntimeOptions()
        return self.image_segmentation_with_options(request, runtime)

    async def image_segmentation_async(
        self,
        request: image_search_20210120_models.ImageSegmentationRequest,
    ) -> image_search_20210120_models.ImageSegmentationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.image_segmentation_with_options_async(request, runtime)

    def image_segmentation_advance(
        self,
        request: image_search_20210120_models.ImageSegmentationAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20210120_models.ImageSegmentationResponse:
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
            product='ImageSearch',
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
        image_segmentation_req = image_search_20210120_models.ImageSegmentationRequest()
        OpenApiUtilClient.convert(request, image_segmentation_req)
        if not UtilClient.is_unset(request.pic_content_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.pic_content_object,
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
            image_segmentation_req.pic_content = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        image_segmentation_resp = self.image_segmentation_with_options(image_segmentation_req, runtime)
        return image_segmentation_resp

    async def image_segmentation_advance_async(
        self,
        request: image_search_20210120_models.ImageSegmentationAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20210120_models.ImageSegmentationResponse:
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
            product='ImageSearch',
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
        image_segmentation_req = image_search_20210120_models.ImageSegmentationRequest()
        OpenApiUtilClient.convert(request, image_segmentation_req)
        if not UtilClient.is_unset(request.pic_content_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.pic_content_object,
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
            image_segmentation_req.pic_content = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        image_segmentation_resp = await self.image_segmentation_with_options_async(image_segmentation_req, runtime)
        return image_segmentation_resp

    def commodity_title_with_options(
        self,
        request: image_search_20210120_models.CommodityTitleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20210120_models.CommodityTitleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            image_search_20210120_models.CommodityTitleResponse(),
            self.do_rpcrequest('CommodityTitle', '2021-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def commodity_title_with_options_async(
        self,
        request: image_search_20210120_models.CommodityTitleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20210120_models.CommodityTitleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            image_search_20210120_models.CommodityTitleResponse(),
            await self.do_rpcrequest_async('CommodityTitle', '2021-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def commodity_title(
        self,
        request: image_search_20210120_models.CommodityTitleRequest,
    ) -> image_search_20210120_models.CommodityTitleResponse:
        runtime = util_models.RuntimeOptions()
        return self.commodity_title_with_options(request, runtime)

    async def commodity_title_async(
        self,
        request: image_search_20210120_models.CommodityTitleRequest,
    ) -> image_search_20210120_models.CommodityTitleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.commodity_title_with_options_async(request, runtime)

    def commodity_title_advance(
        self,
        request: image_search_20210120_models.CommodityTitleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20210120_models.CommodityTitleResponse:
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
            product='ImageSearch',
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
        commodity_title_req = image_search_20210120_models.CommodityTitleRequest()
        OpenApiUtilClient.convert(request, commodity_title_req)
        if not UtilClient.is_unset(request.pic_content_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.pic_content_object,
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
            commodity_title_req.pic_content = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        commodity_title_resp = self.commodity_title_with_options(commodity_title_req, runtime)
        return commodity_title_resp

    async def commodity_title_advance_async(
        self,
        request: image_search_20210120_models.CommodityTitleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20210120_models.CommodityTitleResponse:
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
            product='ImageSearch',
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
        commodity_title_req = image_search_20210120_models.CommodityTitleRequest()
        OpenApiUtilClient.convert(request, commodity_title_req)
        if not UtilClient.is_unset(request.pic_content_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.pic_content_object,
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
            commodity_title_req.pic_content = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        commodity_title_resp = await self.commodity_title_with_options_async(commodity_title_req, runtime)
        return commodity_title_resp
