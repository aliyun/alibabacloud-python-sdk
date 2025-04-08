# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imagesearch20201214 import models as image_search_20201214_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_oss_sdk.client import Client as OSSClient
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models


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

    def add_image_with_options(
        self,
        request: image_search_20201214_models.AddImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.AddImageResponse:
        """
        @summary Adds an image to an Image Search instance.
        
        @description You can call this operation to add an image to an Image Search instance.
        > If you want to obtain more information about the service and technical support, click [Online Consulting](https://www.aliyun.com/core/online-consult?from=aZgW6LJHr2) or join the DingTalk group (ID 35035130).
        ## QPS limits
        By default, the concurrency limit for adding an image to instances whose image capacity specifications are 0.1 million images is 1. This means that the system can process up to one request of adding an image every second. By default, the concurrency limit for adding an image to instances of other image capacity specifications is 5. This means that the system can process up to five requests of adding an image every second.
        
        @param request: AddImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.custom_content):
            body['CustomContent'] = request.custom_content
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.int_attr):
            body['IntAttr'] = request.int_attr
        if not UtilClient.is_unset(request.int_attr_2):
            body['IntAttr2'] = request.int_attr_2
        if not UtilClient.is_unset(request.int_attr_3):
            body['IntAttr3'] = request.int_attr_3
        if not UtilClient.is_unset(request.int_attr_4):
            body['IntAttr4'] = request.int_attr_4
        if not UtilClient.is_unset(request.pic_content):
            body['PicContent'] = request.pic_content
        if not UtilClient.is_unset(request.pic_name):
            body['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.str_attr):
            body['StrAttr'] = request.str_attr
        if not UtilClient.is_unset(request.str_attr_2):
            body['StrAttr2'] = request.str_attr_2
        if not UtilClient.is_unset(request.str_attr_3):
            body['StrAttr3'] = request.str_attr_3
        if not UtilClient.is_unset(request.str_attr_4):
            body['StrAttr4'] = request.str_attr_4
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddImage',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.AddImageResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.AddImageResponse(),
                self.execute(params, req, runtime)
            )

    async def add_image_with_options_async(
        self,
        request: image_search_20201214_models.AddImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.AddImageResponse:
        """
        @summary Adds an image to an Image Search instance.
        
        @description You can call this operation to add an image to an Image Search instance.
        > If you want to obtain more information about the service and technical support, click [Online Consulting](https://www.aliyun.com/core/online-consult?from=aZgW6LJHr2) or join the DingTalk group (ID 35035130).
        ## QPS limits
        By default, the concurrency limit for adding an image to instances whose image capacity specifications are 0.1 million images is 1. This means that the system can process up to one request of adding an image every second. By default, the concurrency limit for adding an image to instances of other image capacity specifications is 5. This means that the system can process up to five requests of adding an image every second.
        
        @param request: AddImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.custom_content):
            body['CustomContent'] = request.custom_content
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.int_attr):
            body['IntAttr'] = request.int_attr
        if not UtilClient.is_unset(request.int_attr_2):
            body['IntAttr2'] = request.int_attr_2
        if not UtilClient.is_unset(request.int_attr_3):
            body['IntAttr3'] = request.int_attr_3
        if not UtilClient.is_unset(request.int_attr_4):
            body['IntAttr4'] = request.int_attr_4
        if not UtilClient.is_unset(request.pic_content):
            body['PicContent'] = request.pic_content
        if not UtilClient.is_unset(request.pic_name):
            body['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.str_attr):
            body['StrAttr'] = request.str_attr
        if not UtilClient.is_unset(request.str_attr_2):
            body['StrAttr2'] = request.str_attr_2
        if not UtilClient.is_unset(request.str_attr_3):
            body['StrAttr3'] = request.str_attr_3
        if not UtilClient.is_unset(request.str_attr_4):
            body['StrAttr4'] = request.str_attr_4
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddImage',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.AddImageResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.AddImageResponse(),
                await self.execute_async(params, req, runtime)
            )

    def add_image(
        self,
        request: image_search_20201214_models.AddImageRequest,
    ) -> image_search_20201214_models.AddImageResponse:
        """
        @summary Adds an image to an Image Search instance.
        
        @description You can call this operation to add an image to an Image Search instance.
        > If you want to obtain more information about the service and technical support, click [Online Consulting](https://www.aliyun.com/core/online-consult?from=aZgW6LJHr2) or join the DingTalk group (ID 35035130).
        ## QPS limits
        By default, the concurrency limit for adding an image to instances whose image capacity specifications are 0.1 million images is 1. This means that the system can process up to one request of adding an image every second. By default, the concurrency limit for adding an image to instances of other image capacity specifications is 5. This means that the system can process up to five requests of adding an image every second.
        
        @param request: AddImageRequest
        @return: AddImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_image_with_options(request, runtime)

    async def add_image_async(
        self,
        request: image_search_20201214_models.AddImageRequest,
    ) -> image_search_20201214_models.AddImageResponse:
        """
        @summary Adds an image to an Image Search instance.
        
        @description You can call this operation to add an image to an Image Search instance.
        > If you want to obtain more information about the service and technical support, click [Online Consulting](https://www.aliyun.com/core/online-consult?from=aZgW6LJHr2) or join the DingTalk group (ID 35035130).
        ## QPS limits
        By default, the concurrency limit for adding an image to instances whose image capacity specifications are 0.1 million images is 1. This means that the system can process up to one request of adding an image every second. By default, the concurrency limit for adding an image to instances of other image capacity specifications is 5. This means that the system can process up to five requests of adding an image every second.
        
        @param request: AddImageRequest
        @return: AddImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_image_with_options_async(request, runtime)

    def add_image_advance(
        self,
        request: image_search_20201214_models.AddImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.AddImageResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        add_image_req = image_search_20201214_models.AddImageRequest()
        OpenApiUtilClient.convert(request, add_image_req)
        if not UtilClient.is_unset(request.pic_content_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.pic_content_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            add_image_req.pic_content = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        add_image_resp = self.add_image_with_options(add_image_req, runtime)
        return add_image_resp

    async def add_image_advance_async(
        self,
        request: image_search_20201214_models.AddImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.AddImageResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        add_image_req = image_search_20201214_models.AddImageRequest()
        OpenApiUtilClient.convert(request, add_image_req)
        if not UtilClient.is_unset(request.pic_content_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.pic_content_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            add_image_req.pic_content = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        add_image_resp = await self.add_image_with_options_async(add_image_req, runtime)
        return add_image_resp

    def compare_similar_by_image_with_options(
        self,
        request: image_search_20201214_models.CompareSimilarByImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.CompareSimilarByImageResponse:
        """
        @summary 对比图片相似值
        
        @param request: CompareSimilarByImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompareSimilarByImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.primary_pic_content):
            body['PrimaryPicContent'] = request.primary_pic_content
        if not UtilClient.is_unset(request.secondary_pic_content):
            body['SecondaryPicContent'] = request.secondary_pic_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompareSimilarByImage',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.CompareSimilarByImageResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.CompareSimilarByImageResponse(),
                self.execute(params, req, runtime)
            )

    async def compare_similar_by_image_with_options_async(
        self,
        request: image_search_20201214_models.CompareSimilarByImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.CompareSimilarByImageResponse:
        """
        @summary 对比图片相似值
        
        @param request: CompareSimilarByImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompareSimilarByImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.primary_pic_content):
            body['PrimaryPicContent'] = request.primary_pic_content
        if not UtilClient.is_unset(request.secondary_pic_content):
            body['SecondaryPicContent'] = request.secondary_pic_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompareSimilarByImage',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.CompareSimilarByImageResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.CompareSimilarByImageResponse(),
                await self.execute_async(params, req, runtime)
            )

    def compare_similar_by_image(
        self,
        request: image_search_20201214_models.CompareSimilarByImageRequest,
    ) -> image_search_20201214_models.CompareSimilarByImageResponse:
        """
        @summary 对比图片相似值
        
        @param request: CompareSimilarByImageRequest
        @return: CompareSimilarByImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.compare_similar_by_image_with_options(request, runtime)

    async def compare_similar_by_image_async(
        self,
        request: image_search_20201214_models.CompareSimilarByImageRequest,
    ) -> image_search_20201214_models.CompareSimilarByImageResponse:
        """
        @summary 对比图片相似值
        
        @param request: CompareSimilarByImageRequest
        @return: CompareSimilarByImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.compare_similar_by_image_with_options_async(request, runtime)

    def compare_similar_by_image_advance(
        self,
        request: image_search_20201214_models.CompareSimilarByImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.CompareSimilarByImageResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        compare_similar_by_image_req = image_search_20201214_models.CompareSimilarByImageRequest()
        OpenApiUtilClient.convert(request, compare_similar_by_image_req)
        if not UtilClient.is_unset(request.primary_pic_content_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.primary_pic_content_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            compare_similar_by_image_req.primary_pic_content = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        if not UtilClient.is_unset(request.secondary_pic_content_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.secondary_pic_content_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            compare_similar_by_image_req.secondary_pic_content = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        compare_similar_by_image_resp = self.compare_similar_by_image_with_options(compare_similar_by_image_req, runtime)
        return compare_similar_by_image_resp

    async def compare_similar_by_image_advance_async(
        self,
        request: image_search_20201214_models.CompareSimilarByImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.CompareSimilarByImageResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        compare_similar_by_image_req = image_search_20201214_models.CompareSimilarByImageRequest()
        OpenApiUtilClient.convert(request, compare_similar_by_image_req)
        if not UtilClient.is_unset(request.primary_pic_content_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.primary_pic_content_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            compare_similar_by_image_req.primary_pic_content = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        if not UtilClient.is_unset(request.secondary_pic_content_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.secondary_pic_content_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            compare_similar_by_image_req.secondary_pic_content = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        compare_similar_by_image_resp = await self.compare_similar_by_image_with_options_async(compare_similar_by_image_req, runtime)
        return compare_similar_by_image_resp

    def delete_image_with_options(
        self,
        request: image_search_20201214_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.DeleteImageResponse:
        """
        @summary This topic describes the syntax of the DeleteImage operation and provides examples of this operation. You can call this operation to delete images from an Image Search instance.
        
        @description This operation deletes images from an Image Search instance.
        >  A success response is returned even if the specified image does not exist on the instance. Therefore, you cannot determine whether the image exists on the instance based on the response.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 20. In this case, the system can process at most 20 requests every second.
        
        @param request: DeleteImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.is_delete_by_filter):
            body['IsDeleteByFilter'] = request.is_delete_by_filter
        if not UtilClient.is_unset(request.pic_name):
            body['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteImage',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.DeleteImageResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.DeleteImageResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_image_with_options_async(
        self,
        request: image_search_20201214_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.DeleteImageResponse:
        """
        @summary This topic describes the syntax of the DeleteImage operation and provides examples of this operation. You can call this operation to delete images from an Image Search instance.
        
        @description This operation deletes images from an Image Search instance.
        >  A success response is returned even if the specified image does not exist on the instance. Therefore, you cannot determine whether the image exists on the instance based on the response.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 20. In this case, the system can process at most 20 requests every second.
        
        @param request: DeleteImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.is_delete_by_filter):
            body['IsDeleteByFilter'] = request.is_delete_by_filter
        if not UtilClient.is_unset(request.pic_name):
            body['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteImage',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.DeleteImageResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.DeleteImageResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_image(
        self,
        request: image_search_20201214_models.DeleteImageRequest,
    ) -> image_search_20201214_models.DeleteImageResponse:
        """
        @summary This topic describes the syntax of the DeleteImage operation and provides examples of this operation. You can call this operation to delete images from an Image Search instance.
        
        @description This operation deletes images from an Image Search instance.
        >  A success response is returned even if the specified image does not exist on the instance. Therefore, you cannot determine whether the image exists on the instance based on the response.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 20. In this case, the system can process at most 20 requests every second.
        
        @param request: DeleteImageRequest
        @return: DeleteImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    async def delete_image_async(
        self,
        request: image_search_20201214_models.DeleteImageRequest,
    ) -> image_search_20201214_models.DeleteImageResponse:
        """
        @summary This topic describes the syntax of the DeleteImage operation and provides examples of this operation. You can call this operation to delete images from an Image Search instance.
        
        @description This operation deletes images from an Image Search instance.
        >  A success response is returned even if the specified image does not exist on the instance. Therefore, you cannot determine whether the image exists on the instance based on the response.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 20. In this case, the system can process at most 20 requests every second.
        
        @param request: DeleteImageRequest
        @return: DeleteImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_with_options_async(request, runtime)

    def detail_with_options(
        self,
        request: image_search_20201214_models.DetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.DetailResponse:
        """
        @summary This topic describes the syntax of the Detail operation and provides examples of this operation. You can call this operation to query instance details.
        
        @description This operation queries instance details.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 1. In this case, the system can process only 1 request every second.
        
        @param request: DetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Detail',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.DetailResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.DetailResponse(),
                self.execute(params, req, runtime)
            )

    async def detail_with_options_async(
        self,
        request: image_search_20201214_models.DetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.DetailResponse:
        """
        @summary This topic describes the syntax of the Detail operation and provides examples of this operation. You can call this operation to query instance details.
        
        @description This operation queries instance details.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 1. In this case, the system can process only 1 request every second.
        
        @param request: DetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Detail',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.DetailResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.DetailResponse(),
                await self.execute_async(params, req, runtime)
            )

    def detail(
        self,
        request: image_search_20201214_models.DetailRequest,
    ) -> image_search_20201214_models.DetailResponse:
        """
        @summary This topic describes the syntax of the Detail operation and provides examples of this operation. You can call this operation to query instance details.
        
        @description This operation queries instance details.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 1. In this case, the system can process only 1 request every second.
        
        @param request: DetailRequest
        @return: DetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detail_with_options(request, runtime)

    async def detail_async(
        self,
        request: image_search_20201214_models.DetailRequest,
    ) -> image_search_20201214_models.DetailResponse:
        """
        @summary This topic describes the syntax of the Detail operation and provides examples of this operation. You can call this operation to query instance details.
        
        @description This operation queries instance details.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 1. In this case, the system can process only 1 request every second.
        
        @param request: DetailRequest
        @return: DetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detail_with_options_async(request, runtime)

    def dump_meta_with_options(
        self,
        request: image_search_20201214_models.DumpMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.DumpMetaResponse:
        """
        @summary This topic describes the syntax of the DumpMeta operation and provides examples of this operation. You can call this operation to create a task for exporting metadata from an Image Search instance.
        
        @description This operation creates a task for exporting metadata from an Image Search instance.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 1. In this case, the system can process at most 1 request every second.
        
        @param request: DumpMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DumpMetaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DumpMeta',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.DumpMetaResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.DumpMetaResponse(),
                self.execute(params, req, runtime)
            )

    async def dump_meta_with_options_async(
        self,
        request: image_search_20201214_models.DumpMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.DumpMetaResponse:
        """
        @summary This topic describes the syntax of the DumpMeta operation and provides examples of this operation. You can call this operation to create a task for exporting metadata from an Image Search instance.
        
        @description This operation creates a task for exporting metadata from an Image Search instance.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 1. In this case, the system can process at most 1 request every second.
        
        @param request: DumpMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DumpMetaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DumpMeta',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.DumpMetaResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.DumpMetaResponse(),
                await self.execute_async(params, req, runtime)
            )

    def dump_meta(
        self,
        request: image_search_20201214_models.DumpMetaRequest,
    ) -> image_search_20201214_models.DumpMetaResponse:
        """
        @summary This topic describes the syntax of the DumpMeta operation and provides examples of this operation. You can call this operation to create a task for exporting metadata from an Image Search instance.
        
        @description This operation creates a task for exporting metadata from an Image Search instance.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 1. In this case, the system can process at most 1 request every second.
        
        @param request: DumpMetaRequest
        @return: DumpMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dump_meta_with_options(request, runtime)

    async def dump_meta_async(
        self,
        request: image_search_20201214_models.DumpMetaRequest,
    ) -> image_search_20201214_models.DumpMetaResponse:
        """
        @summary This topic describes the syntax of the DumpMeta operation and provides examples of this operation. You can call this operation to create a task for exporting metadata from an Image Search instance.
        
        @description This operation creates a task for exporting metadata from an Image Search instance.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 1. In this case, the system can process at most 1 request every second.
        
        @param request: DumpMetaRequest
        @return: DumpMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dump_meta_with_options_async(request, runtime)

    def dump_meta_list_with_options(
        self,
        request: image_search_20201214_models.DumpMetaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.DumpMetaListResponse:
        """
        @summary This topic describes the syntax of the DumpMetaList operation and provides examples of this operation. You can call this operation to query tasks that are used for exporting metadata from an Image Search instance.
        
        @description This operation queries tasks that are used for exporting metadata from an Image Search instance.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 1. In this case, the system can process at most 1 request every second.
        
        @param request: DumpMetaListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DumpMetaListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DumpMetaList',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.DumpMetaListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.DumpMetaListResponse(),
                self.execute(params, req, runtime)
            )

    async def dump_meta_list_with_options_async(
        self,
        request: image_search_20201214_models.DumpMetaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.DumpMetaListResponse:
        """
        @summary This topic describes the syntax of the DumpMetaList operation and provides examples of this operation. You can call this operation to query tasks that are used for exporting metadata from an Image Search instance.
        
        @description This operation queries tasks that are used for exporting metadata from an Image Search instance.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 1. In this case, the system can process at most 1 request every second.
        
        @param request: DumpMetaListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DumpMetaListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DumpMetaList',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.DumpMetaListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.DumpMetaListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def dump_meta_list(
        self,
        request: image_search_20201214_models.DumpMetaListRequest,
    ) -> image_search_20201214_models.DumpMetaListResponse:
        """
        @summary This topic describes the syntax of the DumpMetaList operation and provides examples of this operation. You can call this operation to query tasks that are used for exporting metadata from an Image Search instance.
        
        @description This operation queries tasks that are used for exporting metadata from an Image Search instance.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 1. In this case, the system can process at most 1 request every second.
        
        @param request: DumpMetaListRequest
        @return: DumpMetaListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dump_meta_list_with_options(request, runtime)

    async def dump_meta_list_async(
        self,
        request: image_search_20201214_models.DumpMetaListRequest,
    ) -> image_search_20201214_models.DumpMetaListResponse:
        """
        @summary This topic describes the syntax of the DumpMetaList operation and provides examples of this operation. You can call this operation to query tasks that are used for exporting metadata from an Image Search instance.
        
        @description This operation queries tasks that are used for exporting metadata from an Image Search instance.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 1. In this case, the system can process at most 1 request every second.
        
        @param request: DumpMetaListRequest
        @return: DumpMetaListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dump_meta_list_with_options_async(request, runtime)

    def increase_instance_with_options(
        self,
        request: image_search_20201214_models.IncreaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.IncreaseInstanceResponse:
        """
        @summary This topic describes the syntax of the IncreaseInstance operation and provides examples of this operation. You can call this operation to create a batch task on an Image Search instance.
        
        @description This operation creates a batch task on an Image Search instance.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 1. In this case, the system can process at most 1 request every second.
        
        @param request: IncreaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IncreaseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.callback_address):
            query['CallbackAddress'] = request.callback_address
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IncreaseInstance',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.IncreaseInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.IncreaseInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def increase_instance_with_options_async(
        self,
        request: image_search_20201214_models.IncreaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.IncreaseInstanceResponse:
        """
        @summary This topic describes the syntax of the IncreaseInstance operation and provides examples of this operation. You can call this operation to create a batch task on an Image Search instance.
        
        @description This operation creates a batch task on an Image Search instance.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 1. In this case, the system can process at most 1 request every second.
        
        @param request: IncreaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IncreaseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.callback_address):
            query['CallbackAddress'] = request.callback_address
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IncreaseInstance',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.IncreaseInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.IncreaseInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def increase_instance(
        self,
        request: image_search_20201214_models.IncreaseInstanceRequest,
    ) -> image_search_20201214_models.IncreaseInstanceResponse:
        """
        @summary This topic describes the syntax of the IncreaseInstance operation and provides examples of this operation. You can call this operation to create a batch task on an Image Search instance.
        
        @description This operation creates a batch task on an Image Search instance.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 1. In this case, the system can process at most 1 request every second.
        
        @param request: IncreaseInstanceRequest
        @return: IncreaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.increase_instance_with_options(request, runtime)

    async def increase_instance_async(
        self,
        request: image_search_20201214_models.IncreaseInstanceRequest,
    ) -> image_search_20201214_models.IncreaseInstanceResponse:
        """
        @summary This topic describes the syntax of the IncreaseInstance operation and provides examples of this operation. You can call this operation to create a batch task on an Image Search instance.
        
        @description This operation creates a batch task on an Image Search instance.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 1. In this case, the system can process at most 1 request every second.
        
        @param request: IncreaseInstanceRequest
        @return: IncreaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.increase_instance_with_options_async(request, runtime)

    def increase_list_with_options(
        self,
        request: image_search_20201214_models.IncreaseListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.IncreaseListResponse:
        """
        @summary This topic describes the syntax of the IncreaseList operation and provides examples of this operation. You can call this operation to query batch tasks on an Image Search instance.
        
        @description This operation queries batch tasks on an Image Search instance.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 1. In this case, the system can process at most 1 request every second.
        
        @param request: IncreaseListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IncreaseListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IncreaseList',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.IncreaseListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.IncreaseListResponse(),
                self.execute(params, req, runtime)
            )

    async def increase_list_with_options_async(
        self,
        request: image_search_20201214_models.IncreaseListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.IncreaseListResponse:
        """
        @summary This topic describes the syntax of the IncreaseList operation and provides examples of this operation. You can call this operation to query batch tasks on an Image Search instance.
        
        @description This operation queries batch tasks on an Image Search instance.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 1. In this case, the system can process at most 1 request every second.
        
        @param request: IncreaseListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IncreaseListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IncreaseList',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.IncreaseListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.IncreaseListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def increase_list(
        self,
        request: image_search_20201214_models.IncreaseListRequest,
    ) -> image_search_20201214_models.IncreaseListResponse:
        """
        @summary This topic describes the syntax of the IncreaseList operation and provides examples of this operation. You can call this operation to query batch tasks on an Image Search instance.
        
        @description This operation queries batch tasks on an Image Search instance.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 1. In this case, the system can process at most 1 request every second.
        
        @param request: IncreaseListRequest
        @return: IncreaseListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.increase_list_with_options(request, runtime)

    async def increase_list_async(
        self,
        request: image_search_20201214_models.IncreaseListRequest,
    ) -> image_search_20201214_models.IncreaseListResponse:
        """
        @summary This topic describes the syntax of the IncreaseList operation and provides examples of this operation. You can call this operation to query batch tasks on an Image Search instance.
        
        @description This operation queries batch tasks on an Image Search instance.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 1. In this case, the system can process at most 1 request every second.
        
        @param request: IncreaseListRequest
        @return: IncreaseListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.increase_list_with_options_async(request, runtime)

    def search_image_by_name_with_options(
        self,
        request: image_search_20201214_models.SearchImageByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.SearchImageByNameResponse:
        """
        @summary This topic describes the syntax of the SearchByName operation and provides examples of this operation. You can call this operation to search for images by image name on an Image Search instance.
        
        @description This operation searches for images by image name on an Image Search instance.
        ## QPS limits
        The maximum number of queries per second is displayed in the Image Search console. The upper limit is specified when you purchase the instance. You can set the upper limit to 5 QPS or 10 QPS.
        
        @param request: SearchImageByNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchImageByNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.distinct_product_id):
            body['DistinctProductId'] = request.distinct_product_id
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.num):
            body['Num'] = request.num
        if not UtilClient.is_unset(request.pic_name):
            body['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.start):
            body['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchImageByName',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.SearchImageByNameResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.SearchImageByNameResponse(),
                self.execute(params, req, runtime)
            )

    async def search_image_by_name_with_options_async(
        self,
        request: image_search_20201214_models.SearchImageByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.SearchImageByNameResponse:
        """
        @summary This topic describes the syntax of the SearchByName operation and provides examples of this operation. You can call this operation to search for images by image name on an Image Search instance.
        
        @description This operation searches for images by image name on an Image Search instance.
        ## QPS limits
        The maximum number of queries per second is displayed in the Image Search console. The upper limit is specified when you purchase the instance. You can set the upper limit to 5 QPS or 10 QPS.
        
        @param request: SearchImageByNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchImageByNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.distinct_product_id):
            body['DistinctProductId'] = request.distinct_product_id
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.num):
            body['Num'] = request.num
        if not UtilClient.is_unset(request.pic_name):
            body['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.start):
            body['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchImageByName',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.SearchImageByNameResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.SearchImageByNameResponse(),
                await self.execute_async(params, req, runtime)
            )

    def search_image_by_name(
        self,
        request: image_search_20201214_models.SearchImageByNameRequest,
    ) -> image_search_20201214_models.SearchImageByNameResponse:
        """
        @summary This topic describes the syntax of the SearchByName operation and provides examples of this operation. You can call this operation to search for images by image name on an Image Search instance.
        
        @description This operation searches for images by image name on an Image Search instance.
        ## QPS limits
        The maximum number of queries per second is displayed in the Image Search console. The upper limit is specified when you purchase the instance. You can set the upper limit to 5 QPS or 10 QPS.
        
        @param request: SearchImageByNameRequest
        @return: SearchImageByNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_image_by_name_with_options(request, runtime)

    async def search_image_by_name_async(
        self,
        request: image_search_20201214_models.SearchImageByNameRequest,
    ) -> image_search_20201214_models.SearchImageByNameResponse:
        """
        @summary This topic describes the syntax of the SearchByName operation and provides examples of this operation. You can call this operation to search for images by image name on an Image Search instance.
        
        @description This operation searches for images by image name on an Image Search instance.
        ## QPS limits
        The maximum number of queries per second is displayed in the Image Search console. The upper limit is specified when you purchase the instance. You can set the upper limit to 5 QPS or 10 QPS.
        
        @param request: SearchImageByNameRequest
        @return: SearchImageByNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_image_by_name_with_options_async(request, runtime)

    def search_image_by_pic_with_options(
        self,
        request: image_search_20201214_models.SearchImageByPicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.SearchImageByPicResponse:
        """
        @summary This topic describes the syntax of the SearchByPic operation and provides examples of this operation. You can call this operation to search for images by image on an Image Search Instance.
        
        @description This operation searches for images by image name on an Image Search instance.
        ## QPS limits
        The maximum number of queries per second is displayed in the Image Search console. The upper limit is specified when you purchase the instance. You can set the upper limit to 5 QPS or 10 QPS.
        ## SDK release notes
        The Image Search SDK has been upgraded to version 3.1.1, which supports multi-subject recognition and similarity scores. For more information, see [Image Search SDK for Java](/help/en/image-search/latest/version-v3-java-sdk).
        
        @param request: SearchImageByPicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchImageByPicResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.distinct_product_id):
            body['DistinctProductId'] = request.distinct_product_id
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.num):
            body['Num'] = request.num
        if not UtilClient.is_unset(request.pic_content):
            body['PicContent'] = request.pic_content
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.start):
            body['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchImageByPic',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.SearchImageByPicResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.SearchImageByPicResponse(),
                self.execute(params, req, runtime)
            )

    async def search_image_by_pic_with_options_async(
        self,
        request: image_search_20201214_models.SearchImageByPicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.SearchImageByPicResponse:
        """
        @summary This topic describes the syntax of the SearchByPic operation and provides examples of this operation. You can call this operation to search for images by image on an Image Search Instance.
        
        @description This operation searches for images by image name on an Image Search instance.
        ## QPS limits
        The maximum number of queries per second is displayed in the Image Search console. The upper limit is specified when you purchase the instance. You can set the upper limit to 5 QPS or 10 QPS.
        ## SDK release notes
        The Image Search SDK has been upgraded to version 3.1.1, which supports multi-subject recognition and similarity scores. For more information, see [Image Search SDK for Java](/help/en/image-search/latest/version-v3-java-sdk).
        
        @param request: SearchImageByPicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchImageByPicResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.distinct_product_id):
            body['DistinctProductId'] = request.distinct_product_id
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.num):
            body['Num'] = request.num
        if not UtilClient.is_unset(request.pic_content):
            body['PicContent'] = request.pic_content
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.start):
            body['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchImageByPic',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.SearchImageByPicResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.SearchImageByPicResponse(),
                await self.execute_async(params, req, runtime)
            )

    def search_image_by_pic(
        self,
        request: image_search_20201214_models.SearchImageByPicRequest,
    ) -> image_search_20201214_models.SearchImageByPicResponse:
        """
        @summary This topic describes the syntax of the SearchByPic operation and provides examples of this operation. You can call this operation to search for images by image on an Image Search Instance.
        
        @description This operation searches for images by image name on an Image Search instance.
        ## QPS limits
        The maximum number of queries per second is displayed in the Image Search console. The upper limit is specified when you purchase the instance. You can set the upper limit to 5 QPS or 10 QPS.
        ## SDK release notes
        The Image Search SDK has been upgraded to version 3.1.1, which supports multi-subject recognition and similarity scores. For more information, see [Image Search SDK for Java](/help/en/image-search/latest/version-v3-java-sdk).
        
        @param request: SearchImageByPicRequest
        @return: SearchImageByPicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_image_by_pic_with_options(request, runtime)

    async def search_image_by_pic_async(
        self,
        request: image_search_20201214_models.SearchImageByPicRequest,
    ) -> image_search_20201214_models.SearchImageByPicResponse:
        """
        @summary This topic describes the syntax of the SearchByPic operation and provides examples of this operation. You can call this operation to search for images by image on an Image Search Instance.
        
        @description This operation searches for images by image name on an Image Search instance.
        ## QPS limits
        The maximum number of queries per second is displayed in the Image Search console. The upper limit is specified when you purchase the instance. You can set the upper limit to 5 QPS or 10 QPS.
        ## SDK release notes
        The Image Search SDK has been upgraded to version 3.1.1, which supports multi-subject recognition and similarity scores. For more information, see [Image Search SDK for Java](/help/en/image-search/latest/version-v3-java-sdk).
        
        @param request: SearchImageByPicRequest
        @return: SearchImageByPicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_image_by_pic_with_options_async(request, runtime)

    def search_image_by_pic_advance(
        self,
        request: image_search_20201214_models.SearchImageByPicAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.SearchImageByPicResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        search_image_by_pic_req = image_search_20201214_models.SearchImageByPicRequest()
        OpenApiUtilClient.convert(request, search_image_by_pic_req)
        if not UtilClient.is_unset(request.pic_content_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.pic_content_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            search_image_by_pic_req.pic_content = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        search_image_by_pic_resp = self.search_image_by_pic_with_options(search_image_by_pic_req, runtime)
        return search_image_by_pic_resp

    async def search_image_by_pic_advance_async(
        self,
        request: image_search_20201214_models.SearchImageByPicAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.SearchImageByPicResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        search_image_by_pic_req = image_search_20201214_models.SearchImageByPicRequest()
        OpenApiUtilClient.convert(request, search_image_by_pic_req)
        if not UtilClient.is_unset(request.pic_content_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.pic_content_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            search_image_by_pic_req.pic_content = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        search_image_by_pic_resp = await self.search_image_by_pic_with_options_async(search_image_by_pic_req, runtime)
        return search_image_by_pic_resp

    def search_image_by_text_with_options(
        self,
        request: image_search_20201214_models.SearchImageByTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.SearchImageByTextResponse:
        """
        @summary SearchImageByText
        
        @param request: SearchImageByTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchImageByTextResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.distinct_product_id):
            body['DistinctProductId'] = request.distinct_product_id
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.num):
            body['Num'] = request.num
        if not UtilClient.is_unset(request.start):
            body['Start'] = request.start
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchImageByText',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.SearchImageByTextResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.SearchImageByTextResponse(),
                self.execute(params, req, runtime)
            )

    async def search_image_by_text_with_options_async(
        self,
        request: image_search_20201214_models.SearchImageByTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.SearchImageByTextResponse:
        """
        @summary SearchImageByText
        
        @param request: SearchImageByTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchImageByTextResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.distinct_product_id):
            body['DistinctProductId'] = request.distinct_product_id
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.num):
            body['Num'] = request.num
        if not UtilClient.is_unset(request.start):
            body['Start'] = request.start
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchImageByText',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.SearchImageByTextResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.SearchImageByTextResponse(),
                await self.execute_async(params, req, runtime)
            )

    def search_image_by_text(
        self,
        request: image_search_20201214_models.SearchImageByTextRequest,
    ) -> image_search_20201214_models.SearchImageByTextResponse:
        """
        @summary SearchImageByText
        
        @param request: SearchImageByTextRequest
        @return: SearchImageByTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_image_by_text_with_options(request, runtime)

    async def search_image_by_text_async(
        self,
        request: image_search_20201214_models.SearchImageByTextRequest,
    ) -> image_search_20201214_models.SearchImageByTextResponse:
        """
        @summary SearchImageByText
        
        @param request: SearchImageByTextRequest
        @return: SearchImageByTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_image_by_text_with_options_async(request, runtime)

    def update_image_with_options(
        self,
        request: image_search_20201214_models.UpdateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.UpdateImageResponse:
        """
        @summary This topic describes the syntax of the UpdateImage operation and provides examples of this operation. You can call this operation to update image information on an Image Search instance.
        
        @description This operation updates image information on an Image Search instance.
        >    Limits are imposed on the instance creation time.
        >   This operation is supported by instances that are created in the Singapore (Singapore) region after December 2021. This operation is not supported in other regions.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 20. In this case, the system can process at most 20 requests every second.
        
        @param request: UpdateImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.int_attr_3):
            query['IntAttr3'] = request.int_attr_3
        if not UtilClient.is_unset(request.int_attr_4):
            query['IntAttr4'] = request.int_attr_4
        if not UtilClient.is_unset(request.str_attr_3):
            query['StrAttr3'] = request.str_attr_3
        if not UtilClient.is_unset(request.str_attr_4):
            query['StrAttr4'] = request.str_attr_4
        body = {}
        if not UtilClient.is_unset(request.custom_content):
            body['CustomContent'] = request.custom_content
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.int_attr):
            body['IntAttr'] = request.int_attr
        if not UtilClient.is_unset(request.int_attr_2):
            body['IntAttr2'] = request.int_attr_2
        if not UtilClient.is_unset(request.pic_name):
            body['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.str_attr):
            body['StrAttr'] = request.str_attr
        if not UtilClient.is_unset(request.str_attr_2):
            body['StrAttr2'] = request.str_attr_2
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateImage',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.UpdateImageResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.UpdateImageResponse(),
                self.execute(params, req, runtime)
            )

    async def update_image_with_options_async(
        self,
        request: image_search_20201214_models.UpdateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20201214_models.UpdateImageResponse:
        """
        @summary This topic describes the syntax of the UpdateImage operation and provides examples of this operation. You can call this operation to update image information on an Image Search instance.
        
        @description This operation updates image information on an Image Search instance.
        >    Limits are imposed on the instance creation time.
        >   This operation is supported by instances that are created in the Singapore (Singapore) region after December 2021. This operation is not supported in other regions.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 20. In this case, the system can process at most 20 requests every second.
        
        @param request: UpdateImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.int_attr_3):
            query['IntAttr3'] = request.int_attr_3
        if not UtilClient.is_unset(request.int_attr_4):
            query['IntAttr4'] = request.int_attr_4
        if not UtilClient.is_unset(request.str_attr_3):
            query['StrAttr3'] = request.str_attr_3
        if not UtilClient.is_unset(request.str_attr_4):
            query['StrAttr4'] = request.str_attr_4
        body = {}
        if not UtilClient.is_unset(request.custom_content):
            body['CustomContent'] = request.custom_content
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.int_attr):
            body['IntAttr'] = request.int_attr
        if not UtilClient.is_unset(request.int_attr_2):
            body['IntAttr2'] = request.int_attr_2
        if not UtilClient.is_unset(request.pic_name):
            body['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.str_attr):
            body['StrAttr'] = request.str_attr
        if not UtilClient.is_unset(request.str_attr_2):
            body['StrAttr2'] = request.str_attr_2
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateImage',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                image_search_20201214_models.UpdateImageResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                image_search_20201214_models.UpdateImageResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_image(
        self,
        request: image_search_20201214_models.UpdateImageRequest,
    ) -> image_search_20201214_models.UpdateImageResponse:
        """
        @summary This topic describes the syntax of the UpdateImage operation and provides examples of this operation. You can call this operation to update image information on an Image Search instance.
        
        @description This operation updates image information on an Image Search instance.
        >    Limits are imposed on the instance creation time.
        >   This operation is supported by instances that are created in the Singapore (Singapore) region after December 2021. This operation is not supported in other regions.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 20. In this case, the system can process at most 20 requests every second.
        
        @param request: UpdateImageRequest
        @return: UpdateImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_image_with_options(request, runtime)

    async def update_image_async(
        self,
        request: image_search_20201214_models.UpdateImageRequest,
    ) -> image_search_20201214_models.UpdateImageResponse:
        """
        @summary This topic describes the syntax of the UpdateImage operation and provides examples of this operation. You can call this operation to update image information on an Image Search instance.
        
        @description This operation updates image information on an Image Search instance.
        >    Limits are imposed on the instance creation time.
        >   This operation is supported by instances that are created in the Singapore (Singapore) region after December 2021. This operation is not supported in other regions.
        ## QPS limits
        By default, the maximum number of queries supported by this operation is 20. In this case, the system can process at most 20 requests every second.
        
        @param request: UpdateImageRequest
        @return: UpdateImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_image_with_options_async(request, runtime)
