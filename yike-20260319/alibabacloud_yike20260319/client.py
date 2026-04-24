# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_yike20260319 import models as main_models
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
        self._endpoint_rule = ''
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

    def add_yike_user_credit_with_options(
        self,
        request: main_models.AddYikeUserCreditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddYikeUserCreditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.credit):
            query['Credit'] = request.credit
        if not DaraCore.is_null(request.yike_user_id):
            query['YikeUserId'] = request.yike_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddYikeUserCredit',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddYikeUserCreditResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_yike_user_credit_with_options_async(
        self,
        request: main_models.AddYikeUserCreditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddYikeUserCreditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.credit):
            query['Credit'] = request.credit
        if not DaraCore.is_null(request.yike_user_id):
            query['YikeUserId'] = request.yike_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddYikeUserCredit',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddYikeUserCreditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_yike_user_credit(
        self,
        request: main_models.AddYikeUserCreditRequest,
    ) -> main_models.AddYikeUserCreditResponse:
        runtime = RuntimeOptions()
        return self.add_yike_user_credit_with_options(request, runtime)

    async def add_yike_user_credit_async(
        self,
        request: main_models.AddYikeUserCreditRequest,
    ) -> main_models.AddYikeUserCreditResponse:
        runtime = RuntimeOptions()
        return await self.add_yike_user_credit_with_options_async(request, runtime)

    def batch_get_yike_aiapp_job_with_options(
        self,
        request: main_models.BatchGetYikeAIAppJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetYikeAIAppJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetYikeAIAppJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetYikeAIAppJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_yike_aiapp_job_with_options_async(
        self,
        request: main_models.BatchGetYikeAIAppJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetYikeAIAppJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetYikeAIAppJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetYikeAIAppJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_yike_aiapp_job(
        self,
        request: main_models.BatchGetYikeAIAppJobRequest,
    ) -> main_models.BatchGetYikeAIAppJobResponse:
        runtime = RuntimeOptions()
        return self.batch_get_yike_aiapp_job_with_options(request, runtime)

    async def batch_get_yike_aiapp_job_async(
        self,
        request: main_models.BatchGetYikeAIAppJobRequest,
    ) -> main_models.BatchGetYikeAIAppJobResponse:
        runtime = RuntimeOptions()
        return await self.batch_get_yike_aiapp_job_with_options_async(request, runtime)

    def batch_get_yike_asset_media_infos_with_options(
        self,
        request: main_models.BatchGetYikeAssetMediaInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetYikeAssetMediaInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetYikeAssetMediaInfos',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetYikeAssetMediaInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_yike_asset_media_infos_with_options_async(
        self,
        request: main_models.BatchGetYikeAssetMediaInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetYikeAssetMediaInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetYikeAssetMediaInfos',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetYikeAssetMediaInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_yike_asset_media_infos(
        self,
        request: main_models.BatchGetYikeAssetMediaInfosRequest,
    ) -> main_models.BatchGetYikeAssetMediaInfosResponse:
        runtime = RuntimeOptions()
        return self.batch_get_yike_asset_media_infos_with_options(request, runtime)

    async def batch_get_yike_asset_media_infos_async(
        self,
        request: main_models.BatchGetYikeAssetMediaInfosRequest,
    ) -> main_models.BatchGetYikeAssetMediaInfosResponse:
        runtime = RuntimeOptions()
        return await self.batch_get_yike_asset_media_infos_with_options_async(request, runtime)

    def create_yike_asset_upload_with_options(
        self,
        request: main_models.CreateYikeAssetUploadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateYikeAssetUploadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_ext):
            query['FileExt'] = request.file_ext
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateYikeAssetUpload',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateYikeAssetUploadResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_yike_asset_upload_with_options_async(
        self,
        request: main_models.CreateYikeAssetUploadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateYikeAssetUploadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_ext):
            query['FileExt'] = request.file_ext
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateYikeAssetUpload',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateYikeAssetUploadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_yike_asset_upload(
        self,
        request: main_models.CreateYikeAssetUploadRequest,
    ) -> main_models.CreateYikeAssetUploadResponse:
        runtime = RuntimeOptions()
        return self.create_yike_asset_upload_with_options(request, runtime)

    async def create_yike_asset_upload_async(
        self,
        request: main_models.CreateYikeAssetUploadRequest,
    ) -> main_models.CreateYikeAssetUploadResponse:
        runtime = RuntimeOptions()
        return await self.create_yike_asset_upload_with_options_async(request, runtime)

    def create_yike_production_with_options(
        self,
        request: main_models.CreateYikeProductionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateYikeProductionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateYikeProduction',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateYikeProductionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_yike_production_with_options_async(
        self,
        request: main_models.CreateYikeProductionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateYikeProductionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateYikeProduction',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateYikeProductionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_yike_production(
        self,
        request: main_models.CreateYikeProductionRequest,
    ) -> main_models.CreateYikeProductionResponse:
        runtime = RuntimeOptions()
        return self.create_yike_production_with_options(request, runtime)

    async def create_yike_production_async(
        self,
        request: main_models.CreateYikeProductionRequest,
    ) -> main_models.CreateYikeProductionResponse:
        runtime = RuntimeOptions()
        return await self.create_yike_production_with_options_async(request, runtime)

    def create_yike_user_with_options(
        self,
        request: main_models.CreateYikeUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateYikeUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.nickname):
            query['Nickname'] = request.nickname
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.production_ids):
            query['ProductionIds'] = request.production_ids
        if not DaraCore.is_null(request.user_name_prefix):
            query['UserNamePrefix'] = request.user_name_prefix
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateYikeUser',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateYikeUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_yike_user_with_options_async(
        self,
        request: main_models.CreateYikeUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateYikeUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.nickname):
            query['Nickname'] = request.nickname
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.production_ids):
            query['ProductionIds'] = request.production_ids
        if not DaraCore.is_null(request.user_name_prefix):
            query['UserNamePrefix'] = request.user_name_prefix
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateYikeUser',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateYikeUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_yike_user(
        self,
        request: main_models.CreateYikeUserRequest,
    ) -> main_models.CreateYikeUserResponse:
        runtime = RuntimeOptions()
        return self.create_yike_user_with_options(request, runtime)

    async def create_yike_user_async(
        self,
        request: main_models.CreateYikeUserRequest,
    ) -> main_models.CreateYikeUserResponse:
        runtime = RuntimeOptions()
        return await self.create_yike_user_with_options_async(request, runtime)

    def create_yike_workspace_with_options(
        self,
        request: main_models.CreateYikeWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateYikeWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_count_limit):
            query['UserCountLimit'] = request.user_count_limit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateYikeWorkspace',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateYikeWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_yike_workspace_with_options_async(
        self,
        request: main_models.CreateYikeWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateYikeWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_count_limit):
            query['UserCountLimit'] = request.user_count_limit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateYikeWorkspace',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateYikeWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_yike_workspace(
        self,
        request: main_models.CreateYikeWorkspaceRequest,
    ) -> main_models.CreateYikeWorkspaceResponse:
        runtime = RuntimeOptions()
        return self.create_yike_workspace_with_options(request, runtime)

    async def create_yike_workspace_async(
        self,
        request: main_models.CreateYikeWorkspaceRequest,
    ) -> main_models.CreateYikeWorkspaceResponse:
        runtime = RuntimeOptions()
        return await self.create_yike_workspace_with_options_async(request, runtime)

    def delete_yike_asset_media_infos_with_options(
        self,
        request: main_models.DeleteYikeAssetMediaInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteYikeAssetMediaInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.logic_delete):
            query['LogicDelete'] = request.logic_delete
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteYikeAssetMediaInfos',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteYikeAssetMediaInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_yike_asset_media_infos_with_options_async(
        self,
        request: main_models.DeleteYikeAssetMediaInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteYikeAssetMediaInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.logic_delete):
            query['LogicDelete'] = request.logic_delete
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteYikeAssetMediaInfos',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteYikeAssetMediaInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_yike_asset_media_infos(
        self,
        request: main_models.DeleteYikeAssetMediaInfosRequest,
    ) -> main_models.DeleteYikeAssetMediaInfosResponse:
        runtime = RuntimeOptions()
        return self.delete_yike_asset_media_infos_with_options(request, runtime)

    async def delete_yike_asset_media_infos_async(
        self,
        request: main_models.DeleteYikeAssetMediaInfosRequest,
    ) -> main_models.DeleteYikeAssetMediaInfosResponse:
        runtime = RuntimeOptions()
        return await self.delete_yike_asset_media_infos_with_options_async(request, runtime)

    def get_yike_aiapp_job_with_options(
        self,
        request: main_models.GetYikeAIAppJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetYikeAIAppJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetYikeAIAppJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYikeAIAppJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_yike_aiapp_job_with_options_async(
        self,
        request: main_models.GetYikeAIAppJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetYikeAIAppJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetYikeAIAppJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYikeAIAppJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_yike_aiapp_job(
        self,
        request: main_models.GetYikeAIAppJobRequest,
    ) -> main_models.GetYikeAIAppJobResponse:
        runtime = RuntimeOptions()
        return self.get_yike_aiapp_job_with_options(request, runtime)

    async def get_yike_aiapp_job_async(
        self,
        request: main_models.GetYikeAIAppJobRequest,
    ) -> main_models.GetYikeAIAppJobResponse:
        runtime = RuntimeOptions()
        return await self.get_yike_aiapp_job_with_options_async(request, runtime)

    def get_yike_asset_media_info_with_options(
        self,
        request: main_models.GetYikeAssetMediaInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetYikeAssetMediaInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetYikeAssetMediaInfo',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYikeAssetMediaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_yike_asset_media_info_with_options_async(
        self,
        request: main_models.GetYikeAssetMediaInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetYikeAssetMediaInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetYikeAssetMediaInfo',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYikeAssetMediaInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_yike_asset_media_info(
        self,
        request: main_models.GetYikeAssetMediaInfoRequest,
    ) -> main_models.GetYikeAssetMediaInfoResponse:
        runtime = RuntimeOptions()
        return self.get_yike_asset_media_info_with_options(request, runtime)

    async def get_yike_asset_media_info_async(
        self,
        request: main_models.GetYikeAssetMediaInfoRequest,
    ) -> main_models.GetYikeAssetMediaInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_yike_asset_media_info_with_options_async(request, runtime)

    def get_yike_storyboard_job_with_options(
        self,
        request: main_models.GetYikeStoryboardJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetYikeStoryboardJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetYikeStoryboardJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYikeStoryboardJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_yike_storyboard_job_with_options_async(
        self,
        request: main_models.GetYikeStoryboardJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetYikeStoryboardJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetYikeStoryboardJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYikeStoryboardJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_yike_storyboard_job(
        self,
        request: main_models.GetYikeStoryboardJobRequest,
    ) -> main_models.GetYikeStoryboardJobResponse:
        runtime = RuntimeOptions()
        return self.get_yike_storyboard_job_with_options(request, runtime)

    async def get_yike_storyboard_job_async(
        self,
        request: main_models.GetYikeStoryboardJobRequest,
    ) -> main_models.GetYikeStoryboardJobResponse:
        runtime = RuntimeOptions()
        return await self.get_yike_storyboard_job_with_options_async(request, runtime)

    def get_yike_user_with_options(
        self,
        request: main_models.GetYikeUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetYikeUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetYikeUser',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYikeUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_yike_user_with_options_async(
        self,
        request: main_models.GetYikeUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetYikeUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetYikeUser',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYikeUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_yike_user(
        self,
        request: main_models.GetYikeUserRequest,
    ) -> main_models.GetYikeUserResponse:
        runtime = RuntimeOptions()
        return self.get_yike_user_with_options(request, runtime)

    async def get_yike_user_async(
        self,
        request: main_models.GetYikeUserRequest,
    ) -> main_models.GetYikeUserResponse:
        runtime = RuntimeOptions()
        return await self.get_yike_user_with_options_async(request, runtime)

    def get_yike_user_credit_with_options(
        self,
        request: main_models.GetYikeUserCreditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetYikeUserCreditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.yike_user_id):
            query['YikeUserId'] = request.yike_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetYikeUserCredit',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYikeUserCreditResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_yike_user_credit_with_options_async(
        self,
        request: main_models.GetYikeUserCreditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetYikeUserCreditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.yike_user_id):
            query['YikeUserId'] = request.yike_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetYikeUserCredit',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetYikeUserCreditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_yike_user_credit(
        self,
        request: main_models.GetYikeUserCreditRequest,
    ) -> main_models.GetYikeUserCreditResponse:
        runtime = RuntimeOptions()
        return self.get_yike_user_credit_with_options(request, runtime)

    async def get_yike_user_credit_async(
        self,
        request: main_models.GetYikeUserCreditRequest,
    ) -> main_models.GetYikeUserCreditResponse:
        runtime = RuntimeOptions()
        return await self.get_yike_user_credit_with_options_async(request, runtime)

    def list_yike_asset_folders_with_options(
        self,
        request: main_models.ListYikeAssetFoldersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListYikeAssetFoldersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.production_id):
            query['ProductionId'] = request.production_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListYikeAssetFolders',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListYikeAssetFoldersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_yike_asset_folders_with_options_async(
        self,
        request: main_models.ListYikeAssetFoldersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListYikeAssetFoldersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.production_id):
            query['ProductionId'] = request.production_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListYikeAssetFolders',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListYikeAssetFoldersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_yike_asset_folders(
        self,
        request: main_models.ListYikeAssetFoldersRequest,
    ) -> main_models.ListYikeAssetFoldersResponse:
        runtime = RuntimeOptions()
        return self.list_yike_asset_folders_with_options(request, runtime)

    async def list_yike_asset_folders_async(
        self,
        request: main_models.ListYikeAssetFoldersRequest,
    ) -> main_models.ListYikeAssetFoldersResponse:
        runtime = RuntimeOptions()
        return await self.list_yike_asset_folders_with_options_async(request, runtime)

    def list_yike_productions_with_options(
        self,
        request: main_models.ListYikeProductionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListYikeProductionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListYikeProductions',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListYikeProductionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_yike_productions_with_options_async(
        self,
        request: main_models.ListYikeProductionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListYikeProductionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListYikeProductions',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListYikeProductionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_yike_productions(
        self,
        request: main_models.ListYikeProductionsRequest,
    ) -> main_models.ListYikeProductionsResponse:
        runtime = RuntimeOptions()
        return self.list_yike_productions_with_options(request, runtime)

    async def list_yike_productions_async(
        self,
        request: main_models.ListYikeProductionsRequest,
    ) -> main_models.ListYikeProductionsResponse:
        runtime = RuntimeOptions()
        return await self.list_yike_productions_with_options_async(request, runtime)

    def precheck_yike_aiapp_job_with_options(
        self,
        request: main_models.PrecheckYikeAIAppJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PrecheckYikeAIAppJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_params):
            query['AppParams'] = request.app_params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PrecheckYikeAIAppJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PrecheckYikeAIAppJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def precheck_yike_aiapp_job_with_options_async(
        self,
        request: main_models.PrecheckYikeAIAppJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PrecheckYikeAIAppJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_params):
            query['AppParams'] = request.app_params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PrecheckYikeAIAppJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PrecheckYikeAIAppJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def precheck_yike_aiapp_job(
        self,
        request: main_models.PrecheckYikeAIAppJobRequest,
    ) -> main_models.PrecheckYikeAIAppJobResponse:
        runtime = RuntimeOptions()
        return self.precheck_yike_aiapp_job_with_options(request, runtime)

    async def precheck_yike_aiapp_job_async(
        self,
        request: main_models.PrecheckYikeAIAppJobRequest,
    ) -> main_models.PrecheckYikeAIAppJobResponse:
        runtime = RuntimeOptions()
        return await self.precheck_yike_aiapp_job_with_options_async(request, runtime)

    def register_yike_asset_media_info_with_options(
        self,
        request: main_models.RegisterYikeAssetMediaInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterYikeAssetMediaInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.folder_id):
            query['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.input_url):
            query['InputURL'] = request.input_url
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.production_id):
            query['ProductionId'] = request.production_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterYikeAssetMediaInfo',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterYikeAssetMediaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_yike_asset_media_info_with_options_async(
        self,
        request: main_models.RegisterYikeAssetMediaInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterYikeAssetMediaInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.folder_id):
            query['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.input_url):
            query['InputURL'] = request.input_url
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.production_id):
            query['ProductionId'] = request.production_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterYikeAssetMediaInfo',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterYikeAssetMediaInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_yike_asset_media_info(
        self,
        request: main_models.RegisterYikeAssetMediaInfoRequest,
    ) -> main_models.RegisterYikeAssetMediaInfoResponse:
        runtime = RuntimeOptions()
        return self.register_yike_asset_media_info_with_options(request, runtime)

    async def register_yike_asset_media_info_async(
        self,
        request: main_models.RegisterYikeAssetMediaInfoRequest,
    ) -> main_models.RegisterYikeAssetMediaInfoResponse:
        runtime = RuntimeOptions()
        return await self.register_yike_asset_media_info_with_options_async(request, runtime)

    def resume_yike_storyboard_job_with_options(
        self,
        request: main_models.ResumeYikeStoryboardJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeYikeStoryboardJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeYikeStoryboardJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeYikeStoryboardJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_yike_storyboard_job_with_options_async(
        self,
        request: main_models.ResumeYikeStoryboardJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeYikeStoryboardJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeYikeStoryboardJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeYikeStoryboardJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_yike_storyboard_job(
        self,
        request: main_models.ResumeYikeStoryboardJobRequest,
    ) -> main_models.ResumeYikeStoryboardJobResponse:
        runtime = RuntimeOptions()
        return self.resume_yike_storyboard_job_with_options(request, runtime)

    async def resume_yike_storyboard_job_async(
        self,
        request: main_models.ResumeYikeStoryboardJobRequest,
    ) -> main_models.ResumeYikeStoryboardJobResponse:
        runtime = RuntimeOptions()
        return await self.resume_yike_storyboard_job_with_options_async(request, runtime)

    def set_yike_callback_config_with_options(
        self,
        request: main_models.SetYikeCallbackConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetYikeCallbackConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callback_config):
            query['CallbackConfig'] = request.callback_config
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetYikeCallbackConfig',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetYikeCallbackConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_yike_callback_config_with_options_async(
        self,
        request: main_models.SetYikeCallbackConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetYikeCallbackConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callback_config):
            query['CallbackConfig'] = request.callback_config
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetYikeCallbackConfig',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetYikeCallbackConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_yike_callback_config(
        self,
        request: main_models.SetYikeCallbackConfigRequest,
    ) -> main_models.SetYikeCallbackConfigResponse:
        runtime = RuntimeOptions()
        return self.set_yike_callback_config_with_options(request, runtime)

    async def set_yike_callback_config_async(
        self,
        request: main_models.SetYikeCallbackConfigRequest,
    ) -> main_models.SetYikeCallbackConfigResponse:
        runtime = RuntimeOptions()
        return await self.set_yike_callback_config_with_options_async(request, runtime)

    def set_yike_user_role_with_options(
        self,
        request: main_models.SetYikeUserRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetYikeUserRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        if not DaraCore.is_null(request.yike_user_id):
            query['YikeUserId'] = request.yike_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetYikeUserRole',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetYikeUserRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_yike_user_role_with_options_async(
        self,
        request: main_models.SetYikeUserRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetYikeUserRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        if not DaraCore.is_null(request.yike_user_id):
            query['YikeUserId'] = request.yike_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetYikeUserRole',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetYikeUserRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_yike_user_role(
        self,
        request: main_models.SetYikeUserRoleRequest,
    ) -> main_models.SetYikeUserRoleResponse:
        runtime = RuntimeOptions()
        return self.set_yike_user_role_with_options(request, runtime)

    async def set_yike_user_role_async(
        self,
        request: main_models.SetYikeUserRoleRequest,
    ) -> main_models.SetYikeUserRoleResponse:
        runtime = RuntimeOptions()
        return await self.set_yike_user_role_with_options_async(request, runtime)

    def sub_yike_user_credit_with_options(
        self,
        request: main_models.SubYikeUserCreditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubYikeUserCreditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.credit):
            query['Credit'] = request.credit
        if not DaraCore.is_null(request.yike_user_id):
            query['YikeUserId'] = request.yike_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubYikeUserCredit',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubYikeUserCreditResponse(),
            self.call_api(params, req, runtime)
        )

    async def sub_yike_user_credit_with_options_async(
        self,
        request: main_models.SubYikeUserCreditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubYikeUserCreditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.credit):
            query['Credit'] = request.credit
        if not DaraCore.is_null(request.yike_user_id):
            query['YikeUserId'] = request.yike_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubYikeUserCredit',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubYikeUserCreditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sub_yike_user_credit(
        self,
        request: main_models.SubYikeUserCreditRequest,
    ) -> main_models.SubYikeUserCreditResponse:
        runtime = RuntimeOptions()
        return self.sub_yike_user_credit_with_options(request, runtime)

    async def sub_yike_user_credit_async(
        self,
        request: main_models.SubYikeUserCreditRequest,
    ) -> main_models.SubYikeUserCreditResponse:
        runtime = RuntimeOptions()
        return await self.sub_yike_user_credit_with_options_async(request, runtime)

    def submit_yike_aiapp_job_with_options(
        self,
        request: main_models.SubmitYikeAIAppJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitYikeAIAppJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_params):
            body['AppParams'] = request.app_params
        if not DaraCore.is_null(request.folder_id):
            body['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.production_id):
            body['ProductionId'] = request.production_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitYikeAIAppJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitYikeAIAppJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_yike_aiapp_job_with_options_async(
        self,
        request: main_models.SubmitYikeAIAppJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitYikeAIAppJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_params):
            body['AppParams'] = request.app_params
        if not DaraCore.is_null(request.folder_id):
            body['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.production_id):
            body['ProductionId'] = request.production_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitYikeAIAppJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitYikeAIAppJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_yike_aiapp_job(
        self,
        request: main_models.SubmitYikeAIAppJobRequest,
    ) -> main_models.SubmitYikeAIAppJobResponse:
        runtime = RuntimeOptions()
        return self.submit_yike_aiapp_job_with_options(request, runtime)

    async def submit_yike_aiapp_job_async(
        self,
        request: main_models.SubmitYikeAIAppJobRequest,
    ) -> main_models.SubmitYikeAIAppJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_yike_aiapp_job_with_options_async(request, runtime)

    def submit_yike_storyboard_job_with_options(
        self,
        request: main_models.SubmitYikeStoryboardJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitYikeStoryboardJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aspect_ratio):
            query['AspectRatio'] = request.aspect_ratio
        if not DaraCore.is_null(request.exec_mode):
            query['ExecMode'] = request.exec_mode
        if not DaraCore.is_null(request.model_params):
            query['ModelParams'] = request.model_params
        if not DaraCore.is_null(request.narration_voice_id):
            query['NarrationVoiceId'] = request.narration_voice_id
        if not DaraCore.is_null(request.resolution):
            query['Resolution'] = request.resolution
        if not DaraCore.is_null(request.shot_prompt_mode):
            query['ShotPromptMode'] = request.shot_prompt_mode
        if not DaraCore.is_null(request.skip_failure_shot):
            query['SkipFailureShot'] = request.skip_failure_shot
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.video_model):
            query['VideoModel'] = request.video_model
        body = {}
        if not DaraCore.is_null(request.file_url):
            body['FileURL'] = request.file_url
        if not DaraCore.is_null(request.shot_split_mode):
            body['ShotSplitMode'] = request.shot_split_mode
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.style_id):
            body['StyleId'] = request.style_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitYikeStoryboardJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitYikeStoryboardJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_yike_storyboard_job_with_options_async(
        self,
        request: main_models.SubmitYikeStoryboardJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitYikeStoryboardJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aspect_ratio):
            query['AspectRatio'] = request.aspect_ratio
        if not DaraCore.is_null(request.exec_mode):
            query['ExecMode'] = request.exec_mode
        if not DaraCore.is_null(request.model_params):
            query['ModelParams'] = request.model_params
        if not DaraCore.is_null(request.narration_voice_id):
            query['NarrationVoiceId'] = request.narration_voice_id
        if not DaraCore.is_null(request.resolution):
            query['Resolution'] = request.resolution
        if not DaraCore.is_null(request.shot_prompt_mode):
            query['ShotPromptMode'] = request.shot_prompt_mode
        if not DaraCore.is_null(request.skip_failure_shot):
            query['SkipFailureShot'] = request.skip_failure_shot
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.video_model):
            query['VideoModel'] = request.video_model
        body = {}
        if not DaraCore.is_null(request.file_url):
            body['FileURL'] = request.file_url
        if not DaraCore.is_null(request.shot_split_mode):
            body['ShotSplitMode'] = request.shot_split_mode
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.style_id):
            body['StyleId'] = request.style_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitYikeStoryboardJob',
            version = '2026-03-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitYikeStoryboardJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_yike_storyboard_job(
        self,
        request: main_models.SubmitYikeStoryboardJobRequest,
    ) -> main_models.SubmitYikeStoryboardJobResponse:
        runtime = RuntimeOptions()
        return self.submit_yike_storyboard_job_with_options(request, runtime)

    async def submit_yike_storyboard_job_async(
        self,
        request: main_models.SubmitYikeStoryboardJobRequest,
    ) -> main_models.SubmitYikeStoryboardJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_yike_storyboard_job_with_options_async(request, runtime)
