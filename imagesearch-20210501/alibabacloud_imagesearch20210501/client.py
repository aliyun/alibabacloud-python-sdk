# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imagesearch20210501 import models as image_search_20210501_models
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

    def search_by_pic_with_options(
        self,
        request: image_search_20210501_models.SearchByPicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20210501_models.SearchByPicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            image_search_20210501_models.SearchByPicResponse(),
            self.do_rpcrequest('SearchByPic', '2021-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_by_pic_with_options_async(
        self,
        request: image_search_20210501_models.SearchByPicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20210501_models.SearchByPicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            image_search_20210501_models.SearchByPicResponse(),
            await self.do_rpcrequest_async('SearchByPic', '2021-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_by_pic(
        self,
        request: image_search_20210501_models.SearchByPicRequest,
    ) -> image_search_20210501_models.SearchByPicResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_by_pic_with_options(request, runtime)

    async def search_by_pic_async(
        self,
        request: image_search_20210501_models.SearchByPicRequest,
    ) -> image_search_20210501_models.SearchByPicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_by_pic_with_options_async(request, runtime)

    def search_by_pic_advance(
        self,
        request: image_search_20210501_models.SearchByPicAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20210501_models.SearchByPicResponse:
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
        search_by_pic_req = image_search_20210501_models.SearchByPicRequest()
        OpenApiUtilClient.convert(request, search_by_pic_req)
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
            search_by_pic_req.pic_content = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        search_by_pic_resp = self.search_by_pic_with_options(search_by_pic_req, runtime)
        return search_by_pic_resp

    async def search_by_pic_advance_async(
        self,
        request: image_search_20210501_models.SearchByPicAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20210501_models.SearchByPicResponse:
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
        search_by_pic_req = image_search_20210501_models.SearchByPicRequest()
        OpenApiUtilClient.convert(request, search_by_pic_req)
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
            search_by_pic_req.pic_content = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        search_by_pic_resp = await self.search_by_pic_with_options_async(search_by_pic_req, runtime)
        return search_by_pic_resp

    def search_by_url_with_options(
        self,
        request: image_search_20210501_models.SearchByUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20210501_models.SearchByUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            image_search_20210501_models.SearchByUrlResponse(),
            self.do_rpcrequest('SearchByUrl', '2021-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_by_url_with_options_async(
        self,
        request: image_search_20210501_models.SearchByUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> image_search_20210501_models.SearchByUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            image_search_20210501_models.SearchByUrlResponse(),
            await self.do_rpcrequest_async('SearchByUrl', '2021-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_by_url(
        self,
        request: image_search_20210501_models.SearchByUrlRequest,
    ) -> image_search_20210501_models.SearchByUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_by_url_with_options(request, runtime)

    async def search_by_url_async(
        self,
        request: image_search_20210501_models.SearchByUrlRequest,
    ) -> image_search_20210501_models.SearchByUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_by_url_with_options_async(request, runtime)
