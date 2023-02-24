# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imgsearch20200320 import models as imgsearch_20200320_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('imgsearch', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        request: imgsearch_20200320_models.AddImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imgsearch_20200320_models.AddImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.extra_data):
            body['ExtraData'] = request.extra_data
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddImage',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imgsearch_20200320_models.AddImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_image_with_options_async(
        self,
        request: imgsearch_20200320_models.AddImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imgsearch_20200320_models.AddImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.extra_data):
            body['ExtraData'] = request.extra_data
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddImage',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imgsearch_20200320_models.AddImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_image(
        self,
        request: imgsearch_20200320_models.AddImageRequest,
    ) -> imgsearch_20200320_models.AddImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_image_with_options(request, runtime)

    async def add_image_async(
        self,
        request: imgsearch_20200320_models.AddImageRequest,
    ) -> imgsearch_20200320_models.AddImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_image_with_options_async(request, runtime)

    def add_image_advance(
        self,
        request: imgsearch_20200320_models.AddImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imgsearch_20200320_models.AddImageResponse:
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
            product='imgsearch',
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
        add_image_req = imgsearch_20200320_models.AddImageRequest()
        OpenApiUtilClient.convert(request, add_image_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
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
            add_image_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        add_image_resp = self.add_image_with_options(add_image_req, runtime)
        return add_image_resp

    async def add_image_advance_async(
        self,
        request: imgsearch_20200320_models.AddImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imgsearch_20200320_models.AddImageResponse:
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
            product='imgsearch',
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
        add_image_req = imgsearch_20200320_models.AddImageRequest()
        OpenApiUtilClient.convert(request, add_image_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
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
            add_image_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        add_image_resp = await self.add_image_with_options_async(add_image_req, runtime)
        return add_image_resp

    def create_image_db_with_options(
        self,
        request: imgsearch_20200320_models.CreateImageDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imgsearch_20200320_models.CreateImageDbResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateImageDb',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imgsearch_20200320_models.CreateImageDbResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_db_with_options_async(
        self,
        request: imgsearch_20200320_models.CreateImageDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imgsearch_20200320_models.CreateImageDbResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateImageDb',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imgsearch_20200320_models.CreateImageDbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_db(
        self,
        request: imgsearch_20200320_models.CreateImageDbRequest,
    ) -> imgsearch_20200320_models.CreateImageDbResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_image_db_with_options(request, runtime)

    async def create_image_db_async(
        self,
        request: imgsearch_20200320_models.CreateImageDbRequest,
    ) -> imgsearch_20200320_models.CreateImageDbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_image_db_with_options_async(request, runtime)

    def delete_image_with_options(
        self,
        request: imgsearch_20200320_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imgsearch_20200320_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteImage',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imgsearch_20200320_models.DeleteImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_image_with_options_async(
        self,
        request: imgsearch_20200320_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imgsearch_20200320_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteImage',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imgsearch_20200320_models.DeleteImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_image(
        self,
        request: imgsearch_20200320_models.DeleteImageRequest,
    ) -> imgsearch_20200320_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    async def delete_image_async(
        self,
        request: imgsearch_20200320_models.DeleteImageRequest,
    ) -> imgsearch_20200320_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_with_options_async(request, runtime)

    def delete_image_db_with_options(
        self,
        request: imgsearch_20200320_models.DeleteImageDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imgsearch_20200320_models.DeleteImageDbResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteImageDb',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imgsearch_20200320_models.DeleteImageDbResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_image_db_with_options_async(
        self,
        request: imgsearch_20200320_models.DeleteImageDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imgsearch_20200320_models.DeleteImageDbResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteImageDb',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imgsearch_20200320_models.DeleteImageDbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_image_db(
        self,
        request: imgsearch_20200320_models.DeleteImageDbRequest,
    ) -> imgsearch_20200320_models.DeleteImageDbResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_image_db_with_options(request, runtime)

    async def delete_image_db_async(
        self,
        request: imgsearch_20200320_models.DeleteImageDbRequest,
    ) -> imgsearch_20200320_models.DeleteImageDbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_db_with_options_async(request, runtime)

    def list_image_dbs_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> imgsearch_20200320_models.ListImageDbsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListImageDbs',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imgsearch_20200320_models.ListImageDbsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_image_dbs_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> imgsearch_20200320_models.ListImageDbsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListImageDbs',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imgsearch_20200320_models.ListImageDbsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_image_dbs(self) -> imgsearch_20200320_models.ListImageDbsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_image_dbs_with_options(runtime)

    async def list_image_dbs_async(self) -> imgsearch_20200320_models.ListImageDbsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_image_dbs_with_options_async(runtime)

    def list_images_with_options(
        self,
        request: imgsearch_20200320_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imgsearch_20200320_models.ListImagesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id_prefix):
            body['EntityIdPrefix'] = request.entity_id_prefix
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imgsearch_20200320_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_images_with_options_async(
        self,
        request: imgsearch_20200320_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imgsearch_20200320_models.ListImagesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id_prefix):
            body['EntityIdPrefix'] = request.entity_id_prefix
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imgsearch_20200320_models.ListImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_images(
        self,
        request: imgsearch_20200320_models.ListImagesRequest,
    ) -> imgsearch_20200320_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_images_with_options(request, runtime)

    async def list_images_async(
        self,
        request: imgsearch_20200320_models.ListImagesRequest,
    ) -> imgsearch_20200320_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_images_with_options_async(request, runtime)

    def search_image_with_options(
        self,
        request: imgsearch_20200320_models.SearchImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imgsearch_20200320_models.SearchImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchImage',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imgsearch_20200320_models.SearchImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_image_with_options_async(
        self,
        request: imgsearch_20200320_models.SearchImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imgsearch_20200320_models.SearchImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchImage',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imgsearch_20200320_models.SearchImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_image(
        self,
        request: imgsearch_20200320_models.SearchImageRequest,
    ) -> imgsearch_20200320_models.SearchImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_image_with_options(request, runtime)

    async def search_image_async(
        self,
        request: imgsearch_20200320_models.SearchImageRequest,
    ) -> imgsearch_20200320_models.SearchImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_image_with_options_async(request, runtime)

    def search_image_advance(
        self,
        request: imgsearch_20200320_models.SearchImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imgsearch_20200320_models.SearchImageResponse:
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
            product='imgsearch',
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
        search_image_req = imgsearch_20200320_models.SearchImageRequest()
        OpenApiUtilClient.convert(request, search_image_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
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
            search_image_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        search_image_resp = self.search_image_with_options(search_image_req, runtime)
        return search_image_resp

    async def search_image_advance_async(
        self,
        request: imgsearch_20200320_models.SearchImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imgsearch_20200320_models.SearchImageResponse:
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
            product='imgsearch',
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
        search_image_req = imgsearch_20200320_models.SearchImageRequest()
        OpenApiUtilClient.convert(request, search_image_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
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
            search_image_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        search_image_resp = await self.search_image_with_options_async(search_image_req, runtime)
        return search_image_resp
