# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_grace20220606 import models as grace_20220606_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


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
        self._endpoint = self.get_endpoint('grace', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def analyze_file_with_options(
        self,
        request: grace_20220606_models.AnalyzeFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> grace_20220606_models.AnalyzeFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keep_unreachable_objects):
            query['keepUnreachableObjects'] = request.keep_unreachable_objects
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AnalyzeFile',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/AnalyzeFile',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            grace_20220606_models.AnalyzeFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def analyze_file_with_options_async(
        self,
        request: grace_20220606_models.AnalyzeFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> grace_20220606_models.AnalyzeFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keep_unreachable_objects):
            query['keepUnreachableObjects'] = request.keep_unreachable_objects
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AnalyzeFile',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/AnalyzeFile',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            grace_20220606_models.AnalyzeFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def analyze_file(
        self,
        request: grace_20220606_models.AnalyzeFileRequest,
    ) -> grace_20220606_models.AnalyzeFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.analyze_file_with_options(request, headers, runtime)

    async def analyze_file_async(
        self,
        request: grace_20220606_models.AnalyzeFileRequest,
    ) -> grace_20220606_models.AnalyzeFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.analyze_file_with_options_async(request, headers, runtime)

    def get_file_with_options(
        self,
        request: grace_20220606_models.GetFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> grace_20220606_models.GetFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFile',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/GetFile',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            grace_20220606_models.GetFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_with_options_async(
        self,
        request: grace_20220606_models.GetFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> grace_20220606_models.GetFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFile',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/GetFile',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            grace_20220606_models.GetFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file(
        self,
        request: grace_20220606_models.GetFileRequest,
    ) -> grace_20220606_models.GetFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_file_with_options(request, headers, runtime)

    async def get_file_async(
        self,
        request: grace_20220606_models.GetFileRequest,
    ) -> grace_20220606_models.GetFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_file_with_options_async(request, headers, runtime)

    def upload_file_by_osswith_options(
        self,
        request: grace_20220606_models.UploadFileByOSSRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> grace_20220606_models.UploadFileByOSSResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['bucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.display_name):
            query['displayName'] = request.display_name
        if not UtilClient.is_unset(request.endpoint):
            query['endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.object_name):
            query['objectName'] = request.object_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadFileByOSS',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/UploadFileByOSS',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            grace_20220606_models.UploadFileByOSSResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_file_by_osswith_options_async(
        self,
        request: grace_20220606_models.UploadFileByOSSRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> grace_20220606_models.UploadFileByOSSResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['bucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.display_name):
            query['displayName'] = request.display_name
        if not UtilClient.is_unset(request.endpoint):
            query['endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.object_name):
            query['objectName'] = request.object_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadFileByOSS',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/UploadFileByOSS',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            grace_20220606_models.UploadFileByOSSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_file_by_oss(
        self,
        request: grace_20220606_models.UploadFileByOSSRequest,
    ) -> grace_20220606_models.UploadFileByOSSResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upload_file_by_osswith_options(request, headers, runtime)

    async def upload_file_by_oss_async(
        self,
        request: grace_20220606_models.UploadFileByOSSRequest,
    ) -> grace_20220606_models.UploadFileByOSSResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upload_file_by_osswith_options_async(request, headers, runtime)

    def upload_file_by_urlwith_options(
        self,
        request: grace_20220606_models.UploadFileByURLRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> grace_20220606_models.UploadFileByURLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['displayName'] = request.display_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.url):
            query['url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadFileByURL',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/UploadFileByURL',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            grace_20220606_models.UploadFileByURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_file_by_urlwith_options_async(
        self,
        request: grace_20220606_models.UploadFileByURLRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> grace_20220606_models.UploadFileByURLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['displayName'] = request.display_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.url):
            query['url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadFileByURL',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/UploadFileByURL',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            grace_20220606_models.UploadFileByURLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_file_by_url(
        self,
        request: grace_20220606_models.UploadFileByURLRequest,
    ) -> grace_20220606_models.UploadFileByURLResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upload_file_by_urlwith_options(request, headers, runtime)

    async def upload_file_by_url_async(
        self,
        request: grace_20220606_models.UploadFileByURLRequest,
    ) -> grace_20220606_models.UploadFileByURLResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upload_file_by_urlwith_options_async(request, headers, runtime)
