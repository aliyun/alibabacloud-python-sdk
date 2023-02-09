# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aisearch20230101 import models as aisearch_20230101_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('aisearch', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        instance_name: str,
        product_id: str,
        tmp_req: aisearch_20230101_models.AddImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.AddImageResponse:
        UtilClient.validate_model(tmp_req)
        request = aisearch_20230101_models.AddImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.boxes):
            request.boxes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.boxes, 'Boxes', 'json')
        query = {}
        if not UtilClient.is_unset(request.custom_content):
            query['CustomContent'] = request.custom_content
        if not UtilClient.is_unset(request.detect_limit):
            query['DetectLimit'] = request.detect_limit
        if not UtilClient.is_unset(request.int_attr):
            query['IntAttr'] = request.int_attr
        if not UtilClient.is_unset(request.pic_content):
            query['PicContent'] = request.pic_content
        if not UtilClient.is_unset(request.pic_name):
            query['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.pic_url):
            query['PicUrl'] = request.pic_url
        if not UtilClient.is_unset(request.str_attr):
            query['StrAttr'] = request.str_attr
        body = {}
        if not UtilClient.is_unset(request.boxes_shrink):
            body['Boxes'] = request.boxes_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddImage',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/entity/{OpenApiUtilClient.get_encode_param(product_id)}/image',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.AddImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_image_with_options_async(
        self,
        instance_name: str,
        product_id: str,
        tmp_req: aisearch_20230101_models.AddImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.AddImageResponse:
        UtilClient.validate_model(tmp_req)
        request = aisearch_20230101_models.AddImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.boxes):
            request.boxes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.boxes, 'Boxes', 'json')
        query = {}
        if not UtilClient.is_unset(request.custom_content):
            query['CustomContent'] = request.custom_content
        if not UtilClient.is_unset(request.detect_limit):
            query['DetectLimit'] = request.detect_limit
        if not UtilClient.is_unset(request.int_attr):
            query['IntAttr'] = request.int_attr
        if not UtilClient.is_unset(request.pic_content):
            query['PicContent'] = request.pic_content
        if not UtilClient.is_unset(request.pic_name):
            query['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.pic_url):
            query['PicUrl'] = request.pic_url
        if not UtilClient.is_unset(request.str_attr):
            query['StrAttr'] = request.str_attr
        body = {}
        if not UtilClient.is_unset(request.boxes_shrink):
            body['Boxes'] = request.boxes_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddImage',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/entity/{OpenApiUtilClient.get_encode_param(product_id)}/image',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.AddImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_image(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.AddImageRequest,
    ) -> aisearch_20230101_models.AddImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_image_with_options(instance_name, product_id, request, headers, runtime)

    async def add_image_async(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.AddImageRequest,
    ) -> aisearch_20230101_models.AddImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_image_with_options_async(instance_name, product_id, request, headers, runtime)

    def add_image_advance(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.AddImageAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.AddImageResponse:
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
            product='aisearch',
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
        add_image_req = aisearch_20230101_models.AddImageRequest()
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
        add_image_resp = self.add_image_with_options(instance_name, product_id, add_image_req, headers, runtime)
        return add_image_resp

    async def add_image_advance_async(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.AddImageAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.AddImageResponse:
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
            product='aisearch',
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
        add_image_req = aisearch_20230101_models.AddImageRequest()
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
        add_image_resp = await self.add_image_with_options_async(instance_name, product_id, add_image_req, headers, runtime)
        return add_image_resp

    def check_oss_increment_meta_exist_with_options(
        self,
        request: aisearch_20230101_models.CheckOssIncrementMetaExistRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.CheckOssIncrementMetaExistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.oss_path):
            query['OssPath'] = request.oss_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckOssIncrementMetaExist',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/oss/check-increment-metafile',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.CheckOssIncrementMetaExistResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_oss_increment_meta_exist_with_options_async(
        self,
        request: aisearch_20230101_models.CheckOssIncrementMetaExistRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.CheckOssIncrementMetaExistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.oss_path):
            query['OssPath'] = request.oss_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckOssIncrementMetaExist',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/oss/check-increment-metafile',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.CheckOssIncrementMetaExistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_oss_increment_meta_exist(
        self,
        request: aisearch_20230101_models.CheckOssIncrementMetaExistRequest,
    ) -> aisearch_20230101_models.CheckOssIncrementMetaExistResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_oss_increment_meta_exist_with_options(request, headers, runtime)

    async def check_oss_increment_meta_exist_async(
        self,
        request: aisearch_20230101_models.CheckOssIncrementMetaExistRequest,
    ) -> aisearch_20230101_models.CheckOssIncrementMetaExistResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_oss_increment_meta_exist_with_options_async(request, headers, runtime)

    def create_batch_tasks_with_options(
        self,
        instance_name: str,
        request: aisearch_20230101_models.CreateBatchTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.CreateBatchTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.callback_address):
            query['CallbackAddress'] = request.callback_address
        if not UtilClient.is_unset(request.oss_path):
            query['OssPath'] = request.oss_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBatchTasks',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/batch-task',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.CreateBatchTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_batch_tasks_with_options_async(
        self,
        instance_name: str,
        request: aisearch_20230101_models.CreateBatchTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.CreateBatchTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.callback_address):
            query['CallbackAddress'] = request.callback_address
        if not UtilClient.is_unset(request.oss_path):
            query['OssPath'] = request.oss_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBatchTasks',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/batch-task',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.CreateBatchTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_batch_tasks(
        self,
        instance_name: str,
        request: aisearch_20230101_models.CreateBatchTasksRequest,
    ) -> aisearch_20230101_models.CreateBatchTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_batch_tasks_with_options(instance_name, request, headers, runtime)

    async def create_batch_tasks_async(
        self,
        instance_name: str,
        request: aisearch_20230101_models.CreateBatchTasksRequest,
    ) -> aisearch_20230101_models.CreateBatchTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_batch_tasks_with_options_async(instance_name, request, headers, runtime)

    def create_dump_meta_with_options(
        self,
        instance_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.CreateDumpMetaResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateDumpMeta',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/dump-meta',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.CreateDumpMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dump_meta_with_options_async(
        self,
        instance_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.CreateDumpMetaResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateDumpMeta',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/dump-meta',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.CreateDumpMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dump_meta(
        self,
        instance_name: str,
    ) -> aisearch_20230101_models.CreateDumpMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_dump_meta_with_options(instance_name, headers, runtime)

    async def create_dump_meta_async(
        self,
        instance_name: str,
    ) -> aisearch_20230101_models.CreateDumpMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_dump_meta_with_options_async(instance_name, headers, runtime)

    def delete_image_with_options(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.DeleteImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pic_name):
            query['PicName'] = request.pic_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImage',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/entity/{OpenApiUtilClient.get_encode_param(product_id)}/image',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.DeleteImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_image_with_options_async(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.DeleteImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pic_name):
            query['PicName'] = request.pic_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImage',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/entity/{OpenApiUtilClient.get_encode_param(product_id)}/image',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.DeleteImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_image(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.DeleteImageRequest,
    ) -> aisearch_20230101_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_image_with_options(instance_name, product_id, request, headers, runtime)

    async def delete_image_async(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.DeleteImageRequest,
    ) -> aisearch_20230101_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_image_with_options_async(instance_name, product_id, request, headers, runtime)

    def get_image_with_options(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.GetImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.GetImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pic_name):
            query['PicName'] = request.pic_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImage',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/entity/{OpenApiUtilClient.get_encode_param(product_id)}/image',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.GetImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_with_options_async(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.GetImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.GetImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pic_name):
            query['PicName'] = request.pic_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImage',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/entity/{OpenApiUtilClient.get_encode_param(product_id)}/image',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.GetImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.GetImageRequest,
    ) -> aisearch_20230101_models.GetImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_image_with_options(instance_name, product_id, request, headers, runtime)

    async def get_image_async(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.GetImageRequest,
    ) -> aisearch_20230101_models.GetImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_image_with_options_async(instance_name, product_id, request, headers, runtime)

    def get_instance_with_options(
        self,
        instance_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.GetInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        instance_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.GetInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        instance_name: str,
    ) -> aisearch_20230101_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_name, headers, runtime)

    async def get_instance_async(
        self,
        instance_name: str,
    ) -> aisearch_20230101_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(instance_name, headers, runtime)

    def list_batch_tasks_with_options(
        self,
        instance_name: str,
        request: aisearch_20230101_models.ListBatchTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.ListBatchTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.oss_path):
            query['OssPath'] = request.oss_path
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBatchTasks',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/batch-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.ListBatchTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_batch_tasks_with_options_async(
        self,
        instance_name: str,
        request: aisearch_20230101_models.ListBatchTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.ListBatchTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.oss_path):
            query['OssPath'] = request.oss_path
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBatchTasks',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/batch-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.ListBatchTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_batch_tasks(
        self,
        instance_name: str,
        request: aisearch_20230101_models.ListBatchTasksRequest,
    ) -> aisearch_20230101_models.ListBatchTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_batch_tasks_with_options(instance_name, request, headers, runtime)

    async def list_batch_tasks_async(
        self,
        instance_name: str,
        request: aisearch_20230101_models.ListBatchTasksRequest,
    ) -> aisearch_20230101_models.ListBatchTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_batch_tasks_with_options_async(instance_name, request, headers, runtime)

    def list_dump_meta_with_options(
        self,
        instance_name: str,
        request: aisearch_20230101_models.ListDumpMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.ListDumpMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDumpMeta',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/dump-metas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.ListDumpMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dump_meta_with_options_async(
        self,
        instance_name: str,
        request: aisearch_20230101_models.ListDumpMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.ListDumpMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDumpMeta',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/dump-metas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.ListDumpMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dump_meta(
        self,
        instance_name: str,
        request: aisearch_20230101_models.ListDumpMetaRequest,
    ) -> aisearch_20230101_models.ListDumpMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dump_meta_with_options(instance_name, request, headers, runtime)

    async def list_dump_meta_async(
        self,
        instance_name: str,
        request: aisearch_20230101_models.ListDumpMetaRequest,
    ) -> aisearch_20230101_models.ListDumpMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dump_meta_with_options_async(instance_name, request, headers, runtime)

    def list_instance_with_options(
        self,
        request: aisearch_20230101_models.ListInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.ListInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstance',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.ListInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_with_options_async(
        self,
        request: aisearch_20230101_models.ListInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.ListInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstance',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.ListInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance(
        self,
        request: aisearch_20230101_models.ListInstanceRequest,
    ) -> aisearch_20230101_models.ListInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_with_options(request, headers, runtime)

    async def list_instance_async(
        self,
        request: aisearch_20230101_models.ListInstanceRequest,
    ) -> aisearch_20230101_models.ListInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_with_options_async(request, headers, runtime)

    def list_oss_bucket_and_path_with_options(
        self,
        request: aisearch_20230101_models.ListOssBucketAndPathRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.ListOssBucketAndPathResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.oss_path):
            query['OssPath'] = request.oss_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOssBucketAndPath',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/oss/buckets-and-path',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.ListOssBucketAndPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_oss_bucket_and_path_with_options_async(
        self,
        request: aisearch_20230101_models.ListOssBucketAndPathRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.ListOssBucketAndPathResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.oss_path):
            query['OssPath'] = request.oss_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOssBucketAndPath',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/oss/buckets-and-path',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.ListOssBucketAndPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_oss_bucket_and_path(
        self,
        request: aisearch_20230101_models.ListOssBucketAndPathRequest,
    ) -> aisearch_20230101_models.ListOssBucketAndPathResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_oss_bucket_and_path_with_options(request, headers, runtime)

    async def list_oss_bucket_and_path_async(
        self,
        request: aisearch_20230101_models.ListOssBucketAndPathRequest,
    ) -> aisearch_20230101_models.ListOssBucketAndPathResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_oss_bucket_and_path_with_options_async(request, headers, runtime)

    def reset_instance_with_options(
        self,
        instance_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.ResetInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResetInstance',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/reset',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.ResetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_instance_with_options_async(
        self,
        instance_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.ResetInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResetInstance',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/reset',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.ResetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_instance(
        self,
        instance_name: str,
    ) -> aisearch_20230101_models.ResetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reset_instance_with_options(instance_name, headers, runtime)

    async def reset_instance_async(
        self,
        instance_name: str,
    ) -> aisearch_20230101_models.ResetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.reset_instance_with_options_async(instance_name, headers, runtime)

    def search_image_by_name_with_options(
        self,
        instance_name: str,
        request: aisearch_20230101_models.SearchImageByNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.SearchImageByNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.pic_name):
            query['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchImageByName',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/search-by-name',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.SearchImageByNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_image_by_name_with_options_async(
        self,
        instance_name: str,
        request: aisearch_20230101_models.SearchImageByNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.SearchImageByNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.pic_name):
            query['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchImageByName',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/search-by-name',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.SearchImageByNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_image_by_name(
        self,
        instance_name: str,
        request: aisearch_20230101_models.SearchImageByNameRequest,
    ) -> aisearch_20230101_models.SearchImageByNameResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_image_by_name_with_options(instance_name, request, headers, runtime)

    async def search_image_by_name_async(
        self,
        instance_name: str,
        request: aisearch_20230101_models.SearchImageByNameRequest,
    ) -> aisearch_20230101_models.SearchImageByNameResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_image_by_name_with_options_async(instance_name, request, headers, runtime)

    def search_image_by_pic_with_options(
        self,
        instance_name: str,
        tmp_req: aisearch_20230101_models.SearchImageByPicRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.SearchImageByPicResponse:
        UtilClient.validate_model(tmp_req)
        request = aisearch_20230101_models.SearchImageByPicShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.box):
            request.box_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.box, 'Box', 'json')
        query = {}
        if not UtilClient.is_unset(request.box_shrink):
            query['Box'] = request.box_shrink
        if not UtilClient.is_unset(request.detect_limit):
            query['DetectLimit'] = request.detect_limit
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.pic_content):
            query['PicContent'] = request.pic_content
        if not UtilClient.is_unset(request.pic_url):
            query['PicUrl'] = request.pic_url
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchImageByPic',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/search-by-pic',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.SearchImageByPicResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_image_by_pic_with_options_async(
        self,
        instance_name: str,
        tmp_req: aisearch_20230101_models.SearchImageByPicRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.SearchImageByPicResponse:
        UtilClient.validate_model(tmp_req)
        request = aisearch_20230101_models.SearchImageByPicShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.box):
            request.box_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.box, 'Box', 'json')
        query = {}
        if not UtilClient.is_unset(request.box_shrink):
            query['Box'] = request.box_shrink
        if not UtilClient.is_unset(request.detect_limit):
            query['DetectLimit'] = request.detect_limit
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.pic_content):
            query['PicContent'] = request.pic_content
        if not UtilClient.is_unset(request.pic_url):
            query['PicUrl'] = request.pic_url
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchImageByPic',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/search-by-pic',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.SearchImageByPicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_image_by_pic(
        self,
        instance_name: str,
        request: aisearch_20230101_models.SearchImageByPicRequest,
    ) -> aisearch_20230101_models.SearchImageByPicResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_image_by_pic_with_options(instance_name, request, headers, runtime)

    async def search_image_by_pic_async(
        self,
        instance_name: str,
        request: aisearch_20230101_models.SearchImageByPicRequest,
    ) -> aisearch_20230101_models.SearchImageByPicResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_image_by_pic_with_options_async(instance_name, request, headers, runtime)

    def search_image_by_pic_advance(
        self,
        instance_name: str,
        request: aisearch_20230101_models.SearchImageByPicAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.SearchImageByPicResponse:
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
            product='aisearch',
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
        search_image_by_pic_req = aisearch_20230101_models.SearchImageByPicRequest()
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
        search_image_by_pic_resp = self.search_image_by_pic_with_options(instance_name, search_image_by_pic_req, headers, runtime)
        return search_image_by_pic_resp

    async def search_image_by_pic_advance_async(
        self,
        instance_name: str,
        request: aisearch_20230101_models.SearchImageByPicAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.SearchImageByPicResponse:
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
            product='aisearch',
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
        search_image_by_pic_req = aisearch_20230101_models.SearchImageByPicRequest()
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
        search_image_by_pic_resp = await self.search_image_by_pic_with_options_async(instance_name, search_image_by_pic_req, headers, runtime)
        return search_image_by_pic_resp

    def stop_batch_tasks_with_options(
        self,
        instance_name: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.StopBatchTasksResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopBatchTasks',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/batch-task/{OpenApiUtilClient.get_encode_param(id)}/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.StopBatchTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_batch_tasks_with_options_async(
        self,
        instance_name: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.StopBatchTasksResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopBatchTasks',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/batch-task/{OpenApiUtilClient.get_encode_param(id)}/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.StopBatchTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_batch_tasks(
        self,
        instance_name: str,
        id: str,
    ) -> aisearch_20230101_models.StopBatchTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_batch_tasks_with_options(instance_name, id, headers, runtime)

    async def stop_batch_tasks_async(
        self,
        instance_name: str,
        id: str,
    ) -> aisearch_20230101_models.StopBatchTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_batch_tasks_with_options_async(instance_name, id, headers, runtime)

    def stop_dump_meta_with_options(
        self,
        instance_name: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.StopDumpMetaResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopDumpMeta',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/dump-meta/{OpenApiUtilClient.get_encode_param(id)}/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.StopDumpMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_dump_meta_with_options_async(
        self,
        instance_name: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.StopDumpMetaResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopDumpMeta',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/dump-meta/{OpenApiUtilClient.get_encode_param(id)}/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.StopDumpMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_dump_meta(
        self,
        instance_name: str,
        id: str,
    ) -> aisearch_20230101_models.StopDumpMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_dump_meta_with_options(instance_name, id, headers, runtime)

    async def stop_dump_meta_async(
        self,
        instance_name: str,
        id: str,
    ) -> aisearch_20230101_models.StopDumpMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_dump_meta_with_options_async(instance_name, id, headers, runtime)

    def update_image_with_options(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.UpdateImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.UpdateImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_content):
            query['CustomContent'] = request.custom_content
        if not UtilClient.is_unset(request.int_attr):
            query['IntAttr'] = request.int_attr
        if not UtilClient.is_unset(request.pic_name):
            query['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.str_attr):
            query['StrAttr'] = request.str_attr
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateImage',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/entity/{OpenApiUtilClient.get_encode_param(product_id)}/image',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.UpdateImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_image_with_options_async(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.UpdateImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aisearch_20230101_models.UpdateImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_content):
            query['CustomContent'] = request.custom_content
        if not UtilClient.is_unset(request.int_attr):
            query['IntAttr'] = request.int_attr
        if not UtilClient.is_unset(request.pic_name):
            query['PicName'] = request.pic_name
        if not UtilClient.is_unset(request.str_attr):
            query['StrAttr'] = request.str_attr
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateImage',
            version='2023-01-01',
            protocol='HTTPS',
            pathname=f'/api/instance/{OpenApiUtilClient.get_encode_param(instance_name)}/entity/{OpenApiUtilClient.get_encode_param(product_id)}/image',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aisearch_20230101_models.UpdateImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_image(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.UpdateImageRequest,
    ) -> aisearch_20230101_models.UpdateImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_image_with_options(instance_name, product_id, request, headers, runtime)

    async def update_image_async(
        self,
        instance_name: str,
        product_id: str,
        request: aisearch_20230101_models.UpdateImageRequest,
    ) -> aisearch_20230101_models.UpdateImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_image_with_options_async(instance_name, product_id, request, headers, runtime)
