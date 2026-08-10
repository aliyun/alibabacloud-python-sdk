# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_yike20260707 import models as main_models
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-shanghai': 'yike.cn-shanghai.aliyuncs.com',
            'ap-southeast-1': 'yike.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('yike', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def batch_get_medias_with_options(
        self,
        request: main_models.BatchGetMediasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetMediasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetMedias',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetMediasResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_medias_with_options_async(
        self,
        request: main_models.BatchGetMediasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetMediasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetMedias',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetMediasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_medias(
        self,
        request: main_models.BatchGetMediasRequest,
    ) -> main_models.BatchGetMediasResponse:
        runtime = RuntimeOptions()
        return self.batch_get_medias_with_options(request, runtime)

    async def batch_get_medias_async(
        self,
        request: main_models.BatchGetMediasRequest,
    ) -> main_models.BatchGetMediasResponse:
        runtime = RuntimeOptions()
        return await self.batch_get_medias_with_options_async(request, runtime)

    def create_asset_category_with_options(
        self,
        request: main_models.CreateAssetCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAssetCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_name):
            query['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAssetCategory',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAssetCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_asset_category_with_options_async(
        self,
        request: main_models.CreateAssetCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAssetCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_name):
            query['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAssetCategory',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAssetCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_asset_category(
        self,
        request: main_models.CreateAssetCategoryRequest,
    ) -> main_models.CreateAssetCategoryResponse:
        runtime = RuntimeOptions()
        return self.create_asset_category_with_options(request, runtime)

    async def create_asset_category_async(
        self,
        request: main_models.CreateAssetCategoryRequest,
    ) -> main_models.CreateAssetCategoryResponse:
        runtime = RuntimeOptions()
        return await self.create_asset_category_with_options_async(request, runtime)

    def create_infinite_canvas_with_options(
        self,
        request: main_models.CreateInfiniteCanvasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInfiniteCanvasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cover_url):
            query['CoverUrl'] = request.cover_url
        if not DaraCore.is_null(request.production_id):
            query['ProductionId'] = request.production_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInfiniteCanvas',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInfiniteCanvasResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_infinite_canvas_with_options_async(
        self,
        request: main_models.CreateInfiniteCanvasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInfiniteCanvasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cover_url):
            query['CoverUrl'] = request.cover_url
        if not DaraCore.is_null(request.production_id):
            query['ProductionId'] = request.production_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInfiniteCanvas',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInfiniteCanvasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_infinite_canvas(
        self,
        request: main_models.CreateInfiniteCanvasRequest,
    ) -> main_models.CreateInfiniteCanvasResponse:
        runtime = RuntimeOptions()
        return self.create_infinite_canvas_with_options(request, runtime)

    async def create_infinite_canvas_async(
        self,
        request: main_models.CreateInfiniteCanvasRequest,
    ) -> main_models.CreateInfiniteCanvasResponse:
        runtime = RuntimeOptions()
        return await self.create_infinite_canvas_with_options_async(request, runtime)

    def delete_asset_category_with_options(
        self,
        request: main_models.DeleteAssetCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAssetCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAssetCategory',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAssetCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_asset_category_with_options_async(
        self,
        request: main_models.DeleteAssetCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAssetCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAssetCategory',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAssetCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_asset_category(
        self,
        request: main_models.DeleteAssetCategoryRequest,
    ) -> main_models.DeleteAssetCategoryResponse:
        runtime = RuntimeOptions()
        return self.delete_asset_category_with_options(request, runtime)

    async def delete_asset_category_async(
        self,
        request: main_models.DeleteAssetCategoryRequest,
    ) -> main_models.DeleteAssetCategoryResponse:
        runtime = RuntimeOptions()
        return await self.delete_asset_category_with_options_async(request, runtime)

    def delete_infinite_canvas_with_options(
        self,
        request: main_models.DeleteInfiniteCanvasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInfiniteCanvasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.canvas_id):
            query['CanvasId'] = request.canvas_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInfiniteCanvas',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInfiniteCanvasResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_infinite_canvas_with_options_async(
        self,
        request: main_models.DeleteInfiniteCanvasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInfiniteCanvasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.canvas_id):
            query['CanvasId'] = request.canvas_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInfiniteCanvas',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInfiniteCanvasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_infinite_canvas(
        self,
        request: main_models.DeleteInfiniteCanvasRequest,
    ) -> main_models.DeleteInfiniteCanvasResponse:
        runtime = RuntimeOptions()
        return self.delete_infinite_canvas_with_options(request, runtime)

    async def delete_infinite_canvas_async(
        self,
        request: main_models.DeleteInfiniteCanvasRequest,
    ) -> main_models.DeleteInfiniteCanvasResponse:
        runtime = RuntimeOptions()
        return await self.delete_infinite_canvas_with_options_async(request, runtime)

    def delete_medias_with_options(
        self,
        request: main_models.DeleteMediasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMediasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_physical_files):
            query['DeletePhysicalFiles'] = request.delete_physical_files
        if not DaraCore.is_null(request.input_urls):
            query['InputURLs'] = request.input_urls
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMedias',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMediasResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_medias_with_options_async(
        self,
        request: main_models.DeleteMediasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMediasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_physical_files):
            query['DeletePhysicalFiles'] = request.delete_physical_files
        if not DaraCore.is_null(request.input_urls):
            query['InputURLs'] = request.input_urls
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMedias',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMediasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_medias(
        self,
        request: main_models.DeleteMediasRequest,
    ) -> main_models.DeleteMediasResponse:
        runtime = RuntimeOptions()
        return self.delete_medias_with_options(request, runtime)

    async def delete_medias_async(
        self,
        request: main_models.DeleteMediasRequest,
    ) -> main_models.DeleteMediasResponse:
        runtime = RuntimeOptions()
        return await self.delete_medias_with_options_async(request, runtime)

    def generate_yike_login_token_with_options(
        self,
        request: main_models.GenerateYikeLoginTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateYikeLoginTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_create_production):
            query['AutoCreateProduction'] = request.auto_create_production
        if not DaraCore.is_null(request.expires):
            query['Expires'] = request.expires
        if not DaraCore.is_null(request.nick_name):
            query['NickName'] = request.nick_name
        if not DaraCore.is_null(request.production_auth):
            query['ProductionAuth'] = request.production_auth
        if not DaraCore.is_null(request.sub_user_credit):
            query['SubUserCredit'] = request.sub_user_credit
        if not DaraCore.is_null(request.tenant):
            query['Tenant'] = request.tenant
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateYikeLoginToken',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateYikeLoginTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_yike_login_token_with_options_async(
        self,
        request: main_models.GenerateYikeLoginTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateYikeLoginTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_create_production):
            query['AutoCreateProduction'] = request.auto_create_production
        if not DaraCore.is_null(request.expires):
            query['Expires'] = request.expires
        if not DaraCore.is_null(request.nick_name):
            query['NickName'] = request.nick_name
        if not DaraCore.is_null(request.production_auth):
            query['ProductionAuth'] = request.production_auth
        if not DaraCore.is_null(request.sub_user_credit):
            query['SubUserCredit'] = request.sub_user_credit
        if not DaraCore.is_null(request.tenant):
            query['Tenant'] = request.tenant
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateYikeLoginToken',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateYikeLoginTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_yike_login_token(
        self,
        request: main_models.GenerateYikeLoginTokenRequest,
    ) -> main_models.GenerateYikeLoginTokenResponse:
        runtime = RuntimeOptions()
        return self.generate_yike_login_token_with_options(request, runtime)

    async def generate_yike_login_token_async(
        self,
        request: main_models.GenerateYikeLoginTokenRequest,
    ) -> main_models.GenerateYikeLoginTokenResponse:
        runtime = RuntimeOptions()
        return await self.generate_yike_login_token_with_options_async(request, runtime)

    def get_asset_category_with_options(
        self,
        request: main_models.GetAssetCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAssetCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAssetCategory',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAssetCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_asset_category_with_options_async(
        self,
        request: main_models.GetAssetCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAssetCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAssetCategory',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAssetCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_asset_category(
        self,
        request: main_models.GetAssetCategoryRequest,
    ) -> main_models.GetAssetCategoryResponse:
        runtime = RuntimeOptions()
        return self.get_asset_category_with_options(request, runtime)

    async def get_asset_category_async(
        self,
        request: main_models.GetAssetCategoryRequest,
    ) -> main_models.GetAssetCategoryResponse:
        runtime = RuntimeOptions()
        return await self.get_asset_category_with_options_async(request, runtime)

    def get_image_generation_job_with_options(
        self,
        request: main_models.GetImageGenerationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageGenerationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageGenerationJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageGenerationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_generation_job_with_options_async(
        self,
        request: main_models.GetImageGenerationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageGenerationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageGenerationJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageGenerationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_generation_job(
        self,
        request: main_models.GetImageGenerationJobRequest,
    ) -> main_models.GetImageGenerationJobResponse:
        runtime = RuntimeOptions()
        return self.get_image_generation_job_with_options(request, runtime)

    async def get_image_generation_job_async(
        self,
        request: main_models.GetImageGenerationJobRequest,
    ) -> main_models.GetImageGenerationJobResponse:
        runtime = RuntimeOptions()
        return await self.get_image_generation_job_with_options_async(request, runtime)

    def get_infinite_canvas_with_options(
        self,
        request: main_models.GetInfiniteCanvasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInfiniteCanvasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.canvas_id):
            query['CanvasId'] = request.canvas_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInfiniteCanvas',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInfiniteCanvasResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_infinite_canvas_with_options_async(
        self,
        request: main_models.GetInfiniteCanvasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInfiniteCanvasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.canvas_id):
            query['CanvasId'] = request.canvas_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInfiniteCanvas',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInfiniteCanvasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_infinite_canvas(
        self,
        request: main_models.GetInfiniteCanvasRequest,
    ) -> main_models.GetInfiniteCanvasResponse:
        runtime = RuntimeOptions()
        return self.get_infinite_canvas_with_options(request, runtime)

    async def get_infinite_canvas_async(
        self,
        request: main_models.GetInfiniteCanvasRequest,
    ) -> main_models.GetInfiniteCanvasResponse:
        runtime = RuntimeOptions()
        return await self.get_infinite_canvas_with_options_async(request, runtime)

    def get_media_with_options(
        self,
        request: main_models.GetMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not DaraCore.is_null(request.input_url):
            query['InputURL'] = request.input_url
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMedia',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_media_with_options_async(
        self,
        request: main_models.GetMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not DaraCore.is_null(request.input_url):
            query['InputURL'] = request.input_url
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMedia',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_media(
        self,
        request: main_models.GetMediaRequest,
    ) -> main_models.GetMediaResponse:
        runtime = RuntimeOptions()
        return self.get_media_with_options(request, runtime)

    async def get_media_async(
        self,
        request: main_models.GetMediaRequest,
    ) -> main_models.GetMediaResponse:
        runtime = RuntimeOptions()
        return await self.get_media_with_options_async(request, runtime)

    def get_media_comprehension_job_with_options(
        self,
        request: main_models.GetMediaComprehensionJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaComprehensionJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMediaComprehensionJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMediaComprehensionJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_media_comprehension_job_with_options_async(
        self,
        request: main_models.GetMediaComprehensionJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaComprehensionJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMediaComprehensionJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMediaComprehensionJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_media_comprehension_job(
        self,
        request: main_models.GetMediaComprehensionJobRequest,
    ) -> main_models.GetMediaComprehensionJobResponse:
        runtime = RuntimeOptions()
        return self.get_media_comprehension_job_with_options(request, runtime)

    async def get_media_comprehension_job_async(
        self,
        request: main_models.GetMediaComprehensionJobRequest,
    ) -> main_models.GetMediaComprehensionJobResponse:
        runtime = RuntimeOptions()
        return await self.get_media_comprehension_job_with_options_async(request, runtime)

    def get_remake_script_job_with_options(
        self,
        request: main_models.GetRemakeScriptJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRemakeScriptJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRemakeScriptJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRemakeScriptJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_remake_script_job_with_options_async(
        self,
        request: main_models.GetRemakeScriptJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRemakeScriptJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRemakeScriptJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRemakeScriptJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_remake_script_job(
        self,
        request: main_models.GetRemakeScriptJobRequest,
    ) -> main_models.GetRemakeScriptJobResponse:
        runtime = RuntimeOptions()
        return self.get_remake_script_job_with_options(request, runtime)

    async def get_remake_script_job_async(
        self,
        request: main_models.GetRemakeScriptJobRequest,
    ) -> main_models.GetRemakeScriptJobResponse:
        runtime = RuntimeOptions()
        return await self.get_remake_script_job_with_options_async(request, runtime)

    def get_video_generation_job_with_options(
        self,
        request: main_models.GetVideoGenerationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoGenerationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoGenerationJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoGenerationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_generation_job_with_options_async(
        self,
        request: main_models.GetVideoGenerationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoGenerationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoGenerationJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoGenerationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_generation_job(
        self,
        request: main_models.GetVideoGenerationJobRequest,
    ) -> main_models.GetVideoGenerationJobResponse:
        runtime = RuntimeOptions()
        return self.get_video_generation_job_with_options(request, runtime)

    async def get_video_generation_job_async(
        self,
        request: main_models.GetVideoGenerationJobRequest,
    ) -> main_models.GetVideoGenerationJobResponse:
        runtime = RuntimeOptions()
        return await self.get_video_generation_job_with_options_async(request, runtime)

    def get_video_render_job_with_options(
        self,
        request: main_models.GetVideoRenderJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoRenderJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoRenderJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoRenderJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_render_job_with_options_async(
        self,
        request: main_models.GetVideoRenderJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoRenderJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoRenderJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoRenderJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_render_job(
        self,
        request: main_models.GetVideoRenderJobRequest,
    ) -> main_models.GetVideoRenderJobResponse:
        runtime = RuntimeOptions()
        return self.get_video_render_job_with_options(request, runtime)

    async def get_video_render_job_async(
        self,
        request: main_models.GetVideoRenderJobRequest,
    ) -> main_models.GetVideoRenderJobResponse:
        runtime = RuntimeOptions()
        return await self.get_video_render_job_with_options_async(request, runtime)

    def get_video_translation_job_with_options(
        self,
        request: main_models.GetVideoTranslationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoTranslationJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoTranslationJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoTranslationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_translation_job_with_options_async(
        self,
        request: main_models.GetVideoTranslationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoTranslationJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoTranslationJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoTranslationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_translation_job(
        self,
        request: main_models.GetVideoTranslationJobRequest,
    ) -> main_models.GetVideoTranslationJobResponse:
        runtime = RuntimeOptions()
        return self.get_video_translation_job_with_options(request, runtime)

    async def get_video_translation_job_async(
        self,
        request: main_models.GetVideoTranslationJobRequest,
    ) -> main_models.GetVideoTranslationJobResponse:
        runtime = RuntimeOptions()
        return await self.get_video_translation_job_with_options_async(request, runtime)

    def get_yike_account_credit_with_options(
        self,
        request: main_models.GetYikeAccountCreditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetYikeAccountCreditResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetYikeAccountCredit',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYikeAccountCreditResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_yike_account_credit_with_options_async(
        self,
        request: main_models.GetYikeAccountCreditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetYikeAccountCreditResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetYikeAccountCredit',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYikeAccountCreditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_yike_account_credit(
        self,
        request: main_models.GetYikeAccountCreditRequest,
    ) -> main_models.GetYikeAccountCreditResponse:
        runtime = RuntimeOptions()
        return self.get_yike_account_credit_with_options(request, runtime)

    async def get_yike_account_credit_async(
        self,
        request: main_models.GetYikeAccountCreditRequest,
    ) -> main_models.GetYikeAccountCreditResponse:
        runtime = RuntimeOptions()
        return await self.get_yike_account_credit_with_options_async(request, runtime)

    def get_yike_job_credit_with_options(
        self,
        request: main_models.GetYikeJobCreditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetYikeJobCreditResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetYikeJobCredit',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYikeJobCreditResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_yike_job_credit_with_options_async(
        self,
        request: main_models.GetYikeJobCreditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetYikeJobCreditResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetYikeJobCredit',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYikeJobCreditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_yike_job_credit(
        self,
        request: main_models.GetYikeJobCreditRequest,
    ) -> main_models.GetYikeJobCreditResponse:
        runtime = RuntimeOptions()
        return self.get_yike_job_credit_with_options(request, runtime)

    async def get_yike_job_credit_async(
        self,
        request: main_models.GetYikeJobCreditRequest,
    ) -> main_models.GetYikeJobCreditResponse:
        runtime = RuntimeOptions()
        return await self.get_yike_job_credit_with_options_async(request, runtime)

    def import_media_with_options(
        self,
        request: main_models.ImportMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dynamic_meta_data):
            query['DynamicMetaData'] = request.dynamic_meta_data
        if not DaraCore.is_null(request.entity_id):
            query['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.import_source):
            query['ImportSource'] = request.import_source
        if not DaraCore.is_null(request.input_url):
            query['InputURL'] = request.input_url
        if not DaraCore.is_null(request.media_tags):
            query['MediaTags'] = request.media_tags
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not DaraCore.is_null(request.register_config):
            query['RegisterConfig'] = request.register_config
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportMedia',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_media_with_options_async(
        self,
        request: main_models.ImportMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dynamic_meta_data):
            query['DynamicMetaData'] = request.dynamic_meta_data
        if not DaraCore.is_null(request.entity_id):
            query['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.import_source):
            query['ImportSource'] = request.import_source
        if not DaraCore.is_null(request.input_url):
            query['InputURL'] = request.input_url
        if not DaraCore.is_null(request.media_tags):
            query['MediaTags'] = request.media_tags
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not DaraCore.is_null(request.register_config):
            query['RegisterConfig'] = request.register_config
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportMedia',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_media(
        self,
        request: main_models.ImportMediaRequest,
    ) -> main_models.ImportMediaResponse:
        runtime = RuntimeOptions()
        return self.import_media_with_options(request, runtime)

    async def import_media_async(
        self,
        request: main_models.ImportMediaRequest,
    ) -> main_models.ImportMediaResponse:
        runtime = RuntimeOptions()
        return await self.import_media_with_options_async(request, runtime)

    def list_asset_categories_with_options(
        self,
        request: main_models.ListAssetCategoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAssetCategoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAssetCategories',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAssetCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_asset_categories_with_options_async(
        self,
        request: main_models.ListAssetCategoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAssetCategoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAssetCategories',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAssetCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_asset_categories(
        self,
        request: main_models.ListAssetCategoriesRequest,
    ) -> main_models.ListAssetCategoriesResponse:
        runtime = RuntimeOptions()
        return self.list_asset_categories_with_options(request, runtime)

    async def list_asset_categories_async(
        self,
        request: main_models.ListAssetCategoriesRequest,
    ) -> main_models.ListAssetCategoriesResponse:
        runtime = RuntimeOptions()
        return await self.list_asset_categories_with_options_async(request, runtime)

    def list_infinite_canvases_with_options(
        self,
        request: main_models.ListInfiniteCanvasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInfiniteCanvasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInfiniteCanvases',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInfiniteCanvasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_infinite_canvases_with_options_async(
        self,
        request: main_models.ListInfiniteCanvasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInfiniteCanvasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInfiniteCanvases',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInfiniteCanvasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_infinite_canvases(
        self,
        request: main_models.ListInfiniteCanvasesRequest,
    ) -> main_models.ListInfiniteCanvasesResponse:
        runtime = RuntimeOptions()
        return self.list_infinite_canvases_with_options(request, runtime)

    async def list_infinite_canvases_async(
        self,
        request: main_models.ListInfiniteCanvasesRequest,
    ) -> main_models.ListInfiniteCanvasesResponse:
        runtime = RuntimeOptions()
        return await self.list_infinite_canvases_with_options_async(request, runtime)

    def search_media_with_options(
        self,
        request: main_models.SearchMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.match):
            query['Match'] = request.match
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scroll_token):
            query['ScrollToken'] = request.scroll_token
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchMedia',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_media_with_options_async(
        self,
        request: main_models.SearchMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.match):
            query['Match'] = request.match
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scroll_token):
            query['ScrollToken'] = request.scroll_token
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchMedia',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_media(
        self,
        request: main_models.SearchMediaRequest,
    ) -> main_models.SearchMediaResponse:
        runtime = RuntimeOptions()
        return self.search_media_with_options(request, runtime)

    async def search_media_async(
        self,
        request: main_models.SearchMediaRequest,
    ) -> main_models.SearchMediaResponse:
        runtime = RuntimeOptions()
        return await self.search_media_with_options_async(request, runtime)

    def submit_image_generation_job_with_options(
        self,
        request: main_models.SubmitImageGenerationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitImageGenerationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aspect_ratio):
            query['AspectRatio'] = request.aspect_ratio
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.job_parameters):
            query['JobParameters'] = request.job_parameters
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.n):
            query['N'] = request.n
        if not DaraCore.is_null(request.resolution):
            query['Resolution'] = request.resolution
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitImageGenerationJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitImageGenerationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_image_generation_job_with_options_async(
        self,
        request: main_models.SubmitImageGenerationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitImageGenerationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aspect_ratio):
            query['AspectRatio'] = request.aspect_ratio
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.job_parameters):
            query['JobParameters'] = request.job_parameters
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.n):
            query['N'] = request.n
        if not DaraCore.is_null(request.resolution):
            query['Resolution'] = request.resolution
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitImageGenerationJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitImageGenerationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_image_generation_job(
        self,
        request: main_models.SubmitImageGenerationJobRequest,
    ) -> main_models.SubmitImageGenerationJobResponse:
        runtime = RuntimeOptions()
        return self.submit_image_generation_job_with_options(request, runtime)

    async def submit_image_generation_job_async(
        self,
        request: main_models.SubmitImageGenerationJobRequest,
    ) -> main_models.SubmitImageGenerationJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_image_generation_job_with_options_async(request, runtime)

    def submit_media_comprehension_job_with_options(
        self,
        request: main_models.SubmitMediaComprehensionJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitMediaComprehensionJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.job_params):
            query['JobParams'] = request.job_params
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitMediaComprehensionJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitMediaComprehensionJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_media_comprehension_job_with_options_async(
        self,
        request: main_models.SubmitMediaComprehensionJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitMediaComprehensionJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.job_params):
            query['JobParams'] = request.job_params
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitMediaComprehensionJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitMediaComprehensionJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_media_comprehension_job(
        self,
        request: main_models.SubmitMediaComprehensionJobRequest,
    ) -> main_models.SubmitMediaComprehensionJobResponse:
        runtime = RuntimeOptions()
        return self.submit_media_comprehension_job_with_options(request, runtime)

    async def submit_media_comprehension_job_async(
        self,
        request: main_models.SubmitMediaComprehensionJobRequest,
    ) -> main_models.SubmitMediaComprehensionJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_media_comprehension_job_with_options_async(request, runtime)

    def submit_remake_script_job_with_options(
        self,
        request: main_models.SubmitRemakeScriptJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitRemakeScriptJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.remake_params):
            query['RemakeParams'] = request.remake_params
        if not DaraCore.is_null(request.remake_type):
            query['RemakeType'] = request.remake_type
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitRemakeScriptJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitRemakeScriptJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_remake_script_job_with_options_async(
        self,
        request: main_models.SubmitRemakeScriptJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitRemakeScriptJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.remake_params):
            query['RemakeParams'] = request.remake_params
        if not DaraCore.is_null(request.remake_type):
            query['RemakeType'] = request.remake_type
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitRemakeScriptJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitRemakeScriptJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_remake_script_job(
        self,
        request: main_models.SubmitRemakeScriptJobRequest,
    ) -> main_models.SubmitRemakeScriptJobResponse:
        runtime = RuntimeOptions()
        return self.submit_remake_script_job_with_options(request, runtime)

    async def submit_remake_script_job_async(
        self,
        request: main_models.SubmitRemakeScriptJobRequest,
    ) -> main_models.SubmitRemakeScriptJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_remake_script_job_with_options_async(request, runtime)

    def submit_video_generation_job_with_options(
        self,
        request: main_models.SubmitVideoGenerationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitVideoGenerationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aspect_ratio):
            query['AspectRatio'] = request.aspect_ratio
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.job_parameters):
            query['JobParameters'] = request.job_parameters
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.n):
            query['N'] = request.n
        if not DaraCore.is_null(request.output):
            query['Output'] = request.output
        if not DaraCore.is_null(request.resolution):
            query['Resolution'] = request.resolution
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitVideoGenerationJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitVideoGenerationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_video_generation_job_with_options_async(
        self,
        request: main_models.SubmitVideoGenerationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitVideoGenerationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aspect_ratio):
            query['AspectRatio'] = request.aspect_ratio
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.job_parameters):
            query['JobParameters'] = request.job_parameters
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.n):
            query['N'] = request.n
        if not DaraCore.is_null(request.output):
            query['Output'] = request.output
        if not DaraCore.is_null(request.resolution):
            query['Resolution'] = request.resolution
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitVideoGenerationJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitVideoGenerationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_video_generation_job(
        self,
        request: main_models.SubmitVideoGenerationJobRequest,
    ) -> main_models.SubmitVideoGenerationJobResponse:
        runtime = RuntimeOptions()
        return self.submit_video_generation_job_with_options(request, runtime)

    async def submit_video_generation_job_async(
        self,
        request: main_models.SubmitVideoGenerationJobRequest,
    ) -> main_models.SubmitVideoGenerationJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_video_generation_job_with_options_async(request, runtime)

    def submit_video_render_job_with_options(
        self,
        request: main_models.SubmitVideoRenderJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitVideoRenderJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.script):
            query['Script'] = request.script
        if not DaraCore.is_null(request.settings):
            query['Settings'] = request.settings
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitVideoRenderJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitVideoRenderJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_video_render_job_with_options_async(
        self,
        request: main_models.SubmitVideoRenderJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitVideoRenderJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.script):
            query['Script'] = request.script
        if not DaraCore.is_null(request.settings):
            query['Settings'] = request.settings
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitVideoRenderJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitVideoRenderJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_video_render_job(
        self,
        request: main_models.SubmitVideoRenderJobRequest,
    ) -> main_models.SubmitVideoRenderJobResponse:
        runtime = RuntimeOptions()
        return self.submit_video_render_job_with_options(request, runtime)

    async def submit_video_render_job_async(
        self,
        request: main_models.SubmitVideoRenderJobRequest,
    ) -> main_models.SubmitVideoRenderJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_video_render_job_with_options_async(request, runtime)

    def submit_video_translation_job_with_options(
        self,
        request: main_models.SubmitVideoTranslationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitVideoTranslationJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.input):
            body['Input'] = request.input
        if not DaraCore.is_null(request.job_parameters):
            body['JobParameters'] = request.job_parameters
        if not DaraCore.is_null(request.job_type):
            body['JobType'] = request.job_type
        if not DaraCore.is_null(request.output):
            body['Output'] = request.output
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitVideoTranslationJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitVideoTranslationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_video_translation_job_with_options_async(
        self,
        request: main_models.SubmitVideoTranslationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitVideoTranslationJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.input):
            body['Input'] = request.input
        if not DaraCore.is_null(request.job_parameters):
            body['JobParameters'] = request.job_parameters
        if not DaraCore.is_null(request.job_type):
            body['JobType'] = request.job_type
        if not DaraCore.is_null(request.output):
            body['Output'] = request.output
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitVideoTranslationJob',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitVideoTranslationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_video_translation_job(
        self,
        request: main_models.SubmitVideoTranslationJobRequest,
    ) -> main_models.SubmitVideoTranslationJobResponse:
        runtime = RuntimeOptions()
        return self.submit_video_translation_job_with_options(request, runtime)

    async def submit_video_translation_job_async(
        self,
        request: main_models.SubmitVideoTranslationJobRequest,
    ) -> main_models.SubmitVideoTranslationJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_video_translation_job_with_options_async(request, runtime)

    def update_asset_category_with_options(
        self,
        request: main_models.UpdateAssetCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAssetCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.category_name):
            query['CategoryName'] = request.category_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAssetCategory',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAssetCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_asset_category_with_options_async(
        self,
        request: main_models.UpdateAssetCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAssetCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.category_name):
            query['CategoryName'] = request.category_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAssetCategory',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAssetCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_asset_category(
        self,
        request: main_models.UpdateAssetCategoryRequest,
    ) -> main_models.UpdateAssetCategoryResponse:
        runtime = RuntimeOptions()
        return self.update_asset_category_with_options(request, runtime)

    async def update_asset_category_async(
        self,
        request: main_models.UpdateAssetCategoryRequest,
    ) -> main_models.UpdateAssetCategoryResponse:
        runtime = RuntimeOptions()
        return await self.update_asset_category_with_options_async(request, runtime)

    def update_infinite_canvas_with_options(
        self,
        request: main_models.UpdateInfiniteCanvasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInfiniteCanvasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.canvas_id):
            query['CanvasId'] = request.canvas_id
        if not DaraCore.is_null(request.cover_url):
            query['CoverUrl'] = request.cover_url
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInfiniteCanvas',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInfiniteCanvasResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_infinite_canvas_with_options_async(
        self,
        request: main_models.UpdateInfiniteCanvasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInfiniteCanvasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.canvas_id):
            query['CanvasId'] = request.canvas_id
        if not DaraCore.is_null(request.cover_url):
            query['CoverUrl'] = request.cover_url
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInfiniteCanvas',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInfiniteCanvasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_infinite_canvas(
        self,
        request: main_models.UpdateInfiniteCanvasRequest,
    ) -> main_models.UpdateInfiniteCanvasResponse:
        runtime = RuntimeOptions()
        return self.update_infinite_canvas_with_options(request, runtime)

    async def update_infinite_canvas_async(
        self,
        request: main_models.UpdateInfiniteCanvasRequest,
    ) -> main_models.UpdateInfiniteCanvasResponse:
        runtime = RuntimeOptions()
        return await self.update_infinite_canvas_with_options_async(request, runtime)

    def update_media_with_options(
        self,
        request: main_models.UpdateMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.append_tags):
            query['AppendTags'] = request.append_tags
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dynamic_meta_data):
            query['DynamicMetaData'] = request.dynamic_meta_data
        if not DaraCore.is_null(request.input_url):
            query['InputURL'] = request.input_url
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.media_tags):
            query['MediaTags'] = request.media_tags
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMedia',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_with_options_async(
        self,
        request: main_models.UpdateMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.append_tags):
            query['AppendTags'] = request.append_tags
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dynamic_meta_data):
            query['DynamicMetaData'] = request.dynamic_meta_data
        if not DaraCore.is_null(request.input_url):
            query['InputURL'] = request.input_url
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.media_tags):
            query['MediaTags'] = request.media_tags
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMedia',
            version = '2026-07-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_media(
        self,
        request: main_models.UpdateMediaRequest,
    ) -> main_models.UpdateMediaResponse:
        runtime = RuntimeOptions()
        return self.update_media_with_options(request, runtime)

    async def update_media_async(
        self,
        request: main_models.UpdateMediaRequest,
    ) -> main_models.UpdateMediaResponse:
        runtime = RuntimeOptions()
        return await self.update_media_with_options_async(request, runtime)
