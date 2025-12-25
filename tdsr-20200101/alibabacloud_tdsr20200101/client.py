# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tdsr20200101 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
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
            'cn-hangzhou': 'lyj.cn-hangzhou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('tdsr', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_hotspot_file_with_options(
        self,
        request: main_models.AddHotspotFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddHotspotFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddHotspotFile',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddHotspotFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_hotspot_file_with_options_async(
        self,
        request: main_models.AddHotspotFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddHotspotFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddHotspotFile',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddHotspotFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_hotspot_file(
        self,
        request: main_models.AddHotspotFileRequest,
    ) -> main_models.AddHotspotFileResponse:
        runtime = RuntimeOptions()
        return self.add_hotspot_file_with_options(request, runtime)

    async def add_hotspot_file_async(
        self,
        request: main_models.AddHotspotFileRequest,
    ) -> main_models.AddHotspotFileResponse:
        runtime = RuntimeOptions()
        return await self.add_hotspot_file_with_options_async(request, runtime)

    def add_mosaics_with_options(
        self,
        request: main_models.AddMosaicsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddMosaicsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mark_position):
            query['MarkPosition'] = request.mark_position
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddMosaics',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMosaicsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_mosaics_with_options_async(
        self,
        request: main_models.AddMosaicsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddMosaicsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mark_position):
            query['MarkPosition'] = request.mark_position
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddMosaics',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMosaicsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_mosaics(
        self,
        request: main_models.AddMosaicsRequest,
    ) -> main_models.AddMosaicsResponse:
        runtime = RuntimeOptions()
        return self.add_mosaics_with_options(request, runtime)

    async def add_mosaics_async(
        self,
        request: main_models.AddMosaicsRequest,
    ) -> main_models.AddMosaicsResponse:
        runtime = RuntimeOptions()
        return await self.add_mosaics_with_options_async(request, runtime)

    def add_project_with_options(
        self,
        request: main_models.AddProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_id):
            query['BusinessId'] = request.business_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddProject',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_project_with_options_async(
        self,
        request: main_models.AddProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_id):
            query['BusinessId'] = request.business_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddProject',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_project(
        self,
        request: main_models.AddProjectRequest,
    ) -> main_models.AddProjectResponse:
        runtime = RuntimeOptions()
        return self.add_project_with_options(request, runtime)

    async def add_project_async(
        self,
        request: main_models.AddProjectRequest,
    ) -> main_models.AddProjectResponse:
        runtime = RuntimeOptions()
        return await self.add_project_with_options_async(request, runtime)

    def add_relative_position_with_options(
        self,
        request: main_models.AddRelativePositionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRelativePositionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.relative_position):
            query['RelativePosition'] = request.relative_position
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddRelativePosition',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRelativePositionResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_relative_position_with_options_async(
        self,
        request: main_models.AddRelativePositionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRelativePositionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.relative_position):
            query['RelativePosition'] = request.relative_position
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddRelativePosition',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRelativePositionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_relative_position(
        self,
        request: main_models.AddRelativePositionRequest,
    ) -> main_models.AddRelativePositionResponse:
        runtime = RuntimeOptions()
        return self.add_relative_position_with_options(request, runtime)

    async def add_relative_position_async(
        self,
        request: main_models.AddRelativePositionRequest,
    ) -> main_models.AddRelativePositionResponse:
        runtime = RuntimeOptions()
        return await self.add_relative_position_with_options_async(request, runtime)

    def add_room_plan_with_options(
        self,
        request: main_models.AddRoomPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRoomPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddRoomPlan',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRoomPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_room_plan_with_options_async(
        self,
        request: main_models.AddRoomPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRoomPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddRoomPlan',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRoomPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_room_plan(
        self,
        request: main_models.AddRoomPlanRequest,
    ) -> main_models.AddRoomPlanResponse:
        runtime = RuntimeOptions()
        return self.add_room_plan_with_options(request, runtime)

    async def add_room_plan_async(
        self,
        request: main_models.AddRoomPlanRequest,
    ) -> main_models.AddRoomPlanResponse:
        runtime = RuntimeOptions()
        return await self.add_room_plan_with_options_async(request, runtime)

    def add_scene_with_options(
        self,
        request: main_models.AddSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_uid):
            query['CustomerUid'] = request.customer_uid
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_scene_with_options_async(
        self,
        request: main_models.AddSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_uid):
            query['CustomerUid'] = request.customer_uid
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_scene(
        self,
        request: main_models.AddSceneRequest,
    ) -> main_models.AddSceneResponse:
        runtime = RuntimeOptions()
        return self.add_scene_with_options(request, runtime)

    async def add_scene_async(
        self,
        request: main_models.AddSceneRequest,
    ) -> main_models.AddSceneResponse:
        runtime = RuntimeOptions()
        return await self.add_scene_with_options_async(request, runtime)

    def add_sub_scene_with_options(
        self,
        request: main_models.AddSubSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSubSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSubScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSubSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_sub_scene_with_options_async(
        self,
        request: main_models.AddSubSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSubSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSubScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSubSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_sub_scene(
        self,
        request: main_models.AddSubSceneRequest,
    ) -> main_models.AddSubSceneResponse:
        runtime = RuntimeOptions()
        return self.add_sub_scene_with_options(request, runtime)

    async def add_sub_scene_async(
        self,
        request: main_models.AddSubSceneRequest,
    ) -> main_models.AddSubSceneResponse:
        runtime = RuntimeOptions()
        return await self.add_sub_scene_with_options_async(request, runtime)

    def check_user_property_with_options(
        self,
        request: main_models.CheckUserPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckUserPropertyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckUserProperty',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckUserPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_user_property_with_options_async(
        self,
        request: main_models.CheckUserPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckUserPropertyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckUserProperty',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckUserPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_user_property(
        self,
        request: main_models.CheckUserPropertyRequest,
    ) -> main_models.CheckUserPropertyResponse:
        runtime = RuntimeOptions()
        return self.check_user_property_with_options(request, runtime)

    async def check_user_property_async(
        self,
        request: main_models.CheckUserPropertyRequest,
    ) -> main_models.CheckUserPropertyResponse:
        runtime = RuntimeOptions()
        return await self.check_user_property_with_options_async(request, runtime)

    def copy_scene_with_options(
        self,
        request: main_models.CopySceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopySceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.scene_name):
            query['SceneName'] = request.scene_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CopyScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopySceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_scene_with_options_async(
        self,
        request: main_models.CopySceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopySceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.scene_name):
            query['SceneName'] = request.scene_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CopyScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopySceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_scene(
        self,
        request: main_models.CopySceneRequest,
    ) -> main_models.CopySceneResponse:
        runtime = RuntimeOptions()
        return self.copy_scene_with_options(request, runtime)

    async def copy_scene_async(
        self,
        request: main_models.CopySceneRequest,
    ) -> main_models.CopySceneResponse:
        runtime = RuntimeOptions()
        return await self.copy_scene_with_options_async(request, runtime)

    def create_upload_policy_with_options(
        self,
        request: main_models.CreateUploadPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUploadPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUploadPolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUploadPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_upload_policy_with_options_async(
        self,
        request: main_models.CreateUploadPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUploadPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUploadPolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUploadPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_upload_policy(
        self,
        request: main_models.CreateUploadPolicyRequest,
    ) -> main_models.CreateUploadPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_upload_policy_with_options(request, runtime)

    async def create_upload_policy_async(
        self,
        request: main_models.CreateUploadPolicyRequest,
    ) -> main_models.CreateUploadPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_upload_policy_with_options_async(request, runtime)

    def detail_project_with_options(
        self,
        request: main_models.DetailProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetailProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetailProject',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetailProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def detail_project_with_options_async(
        self,
        request: main_models.DetailProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetailProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetailProject',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetailProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detail_project(
        self,
        request: main_models.DetailProjectRequest,
    ) -> main_models.DetailProjectResponse:
        runtime = RuntimeOptions()
        return self.detail_project_with_options(request, runtime)

    async def detail_project_async(
        self,
        request: main_models.DetailProjectRequest,
    ) -> main_models.DetailProjectResponse:
        runtime = RuntimeOptions()
        return await self.detail_project_with_options_async(request, runtime)

    def detail_scene_with_options(
        self,
        request: main_models.DetailSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetailSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetailScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetailSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def detail_scene_with_options_async(
        self,
        request: main_models.DetailSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetailSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetailScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetailSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detail_scene(
        self,
        request: main_models.DetailSceneRequest,
    ) -> main_models.DetailSceneResponse:
        runtime = RuntimeOptions()
        return self.detail_scene_with_options(request, runtime)

    async def detail_scene_async(
        self,
        request: main_models.DetailSceneRequest,
    ) -> main_models.DetailSceneResponse:
        runtime = RuntimeOptions()
        return await self.detail_scene_with_options_async(request, runtime)

    def detail_sub_scene_with_options(
        self,
        request: main_models.DetailSubSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetailSubSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetailSubScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetailSubSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def detail_sub_scene_with_options_async(
        self,
        request: main_models.DetailSubSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetailSubSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetailSubScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetailSubSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detail_sub_scene(
        self,
        request: main_models.DetailSubSceneRequest,
    ) -> main_models.DetailSubSceneResponse:
        runtime = RuntimeOptions()
        return self.detail_sub_scene_with_options(request, runtime)

    async def detail_sub_scene_async(
        self,
        request: main_models.DetailSubSceneRequest,
    ) -> main_models.DetailSubSceneResponse:
        runtime = RuntimeOptions()
        return await self.detail_sub_scene_with_options_async(request, runtime)

    def drop_project_with_options(
        self,
        request: main_models.DropProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DropProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DropProject',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DropProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def drop_project_with_options_async(
        self,
        request: main_models.DropProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DropProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DropProject',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DropProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def drop_project(
        self,
        request: main_models.DropProjectRequest,
    ) -> main_models.DropProjectResponse:
        runtime = RuntimeOptions()
        return self.drop_project_with_options(request, runtime)

    async def drop_project_async(
        self,
        request: main_models.DropProjectRequest,
    ) -> main_models.DropProjectResponse:
        runtime = RuntimeOptions()
        return await self.drop_project_with_options_async(request, runtime)

    def drop_scene_with_options(
        self,
        request: main_models.DropSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DropSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DropScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DropSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def drop_scene_with_options_async(
        self,
        request: main_models.DropSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DropSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DropScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DropSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def drop_scene(
        self,
        request: main_models.DropSceneRequest,
    ) -> main_models.DropSceneResponse:
        runtime = RuntimeOptions()
        return self.drop_scene_with_options(request, runtime)

    async def drop_scene_async(
        self,
        request: main_models.DropSceneRequest,
    ) -> main_models.DropSceneResponse:
        runtime = RuntimeOptions()
        return await self.drop_scene_with_options_async(request, runtime)

    def drop_sub_scene_with_options(
        self,
        request: main_models.DropSubSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DropSubSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DropSubScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DropSubSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def drop_sub_scene_with_options_async(
        self,
        request: main_models.DropSubSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DropSubSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DropSubScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DropSubSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def drop_sub_scene(
        self,
        request: main_models.DropSubSceneRequest,
    ) -> main_models.DropSubSceneResponse:
        runtime = RuntimeOptions()
        return self.drop_sub_scene_with_options(request, runtime)

    async def drop_sub_scene_async(
        self,
        request: main_models.DropSubSceneRequest,
    ) -> main_models.DropSubSceneResponse:
        runtime = RuntimeOptions()
        return await self.drop_sub_scene_with_options_async(request, runtime)

    def get_conn_data_with_options(
        self,
        request: main_models.GetConnDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConnDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConnData',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConnDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_conn_data_with_options_async(
        self,
        request: main_models.GetConnDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConnDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConnData',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConnDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_conn_data(
        self,
        request: main_models.GetConnDataRequest,
    ) -> main_models.GetConnDataResponse:
        runtime = RuntimeOptions()
        return self.get_conn_data_with_options(request, runtime)

    async def get_conn_data_async(
        self,
        request: main_models.GetConnDataRequest,
    ) -> main_models.GetConnDataResponse:
        runtime = RuntimeOptions()
        return await self.get_conn_data_with_options_async(request, runtime)

    def get_copy_scene_task_status_with_options(
        self,
        request: main_models.GetCopySceneTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCopySceneTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCopySceneTaskStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCopySceneTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_copy_scene_task_status_with_options_async(
        self,
        request: main_models.GetCopySceneTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCopySceneTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCopySceneTaskStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCopySceneTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_copy_scene_task_status(
        self,
        request: main_models.GetCopySceneTaskStatusRequest,
    ) -> main_models.GetCopySceneTaskStatusResponse:
        runtime = RuntimeOptions()
        return self.get_copy_scene_task_status_with_options(request, runtime)

    async def get_copy_scene_task_status_async(
        self,
        request: main_models.GetCopySceneTaskStatusRequest,
    ) -> main_models.GetCopySceneTaskStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_copy_scene_task_status_with_options_async(request, runtime)

    def get_hotspot_config_with_options(
        self,
        request: main_models.GetHotspotConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotspotConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.preview_token):
            query['PreviewToken'] = request.preview_token
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotspotConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotspotConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotspot_config_with_options_async(
        self,
        request: main_models.GetHotspotConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotspotConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.preview_token):
            query['PreviewToken'] = request.preview_token
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotspotConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotspotConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotspot_config(
        self,
        request: main_models.GetHotspotConfigRequest,
    ) -> main_models.GetHotspotConfigResponse:
        runtime = RuntimeOptions()
        return self.get_hotspot_config_with_options(request, runtime)

    async def get_hotspot_config_async(
        self,
        request: main_models.GetHotspotConfigRequest,
    ) -> main_models.GetHotspotConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_hotspot_config_with_options_async(request, runtime)

    def get_hotspot_scene_data_with_options(
        self,
        request: main_models.GetHotspotSceneDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotspotSceneDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.preview_token):
            query['PreviewToken'] = request.preview_token
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotspotSceneData',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotspotSceneDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotspot_scene_data_with_options_async(
        self,
        request: main_models.GetHotspotSceneDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotspotSceneDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.preview_token):
            query['PreviewToken'] = request.preview_token
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotspotSceneData',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotspotSceneDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotspot_scene_data(
        self,
        request: main_models.GetHotspotSceneDataRequest,
    ) -> main_models.GetHotspotSceneDataResponse:
        runtime = RuntimeOptions()
        return self.get_hotspot_scene_data_with_options(request, runtime)

    async def get_hotspot_scene_data_async(
        self,
        request: main_models.GetHotspotSceneDataRequest,
    ) -> main_models.GetHotspotSceneDataResponse:
        runtime = RuntimeOptions()
        return await self.get_hotspot_scene_data_with_options_async(request, runtime)

    def get_hotspot_tag_with_options(
        self,
        request: main_models.GetHotspotTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotspotTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.preview_token):
            query['PreviewToken'] = request.preview_token
        if not DaraCore.is_null(request.sub_scene_uuid):
            query['SubSceneUuid'] = request.sub_scene_uuid
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotspotTag',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotspotTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotspot_tag_with_options_async(
        self,
        request: main_models.GetHotspotTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotspotTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.preview_token):
            query['PreviewToken'] = request.preview_token
        if not DaraCore.is_null(request.sub_scene_uuid):
            query['SubSceneUuid'] = request.sub_scene_uuid
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotspotTag',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotspotTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotspot_tag(
        self,
        request: main_models.GetHotspotTagRequest,
    ) -> main_models.GetHotspotTagResponse:
        runtime = RuntimeOptions()
        return self.get_hotspot_tag_with_options(request, runtime)

    async def get_hotspot_tag_async(
        self,
        request: main_models.GetHotspotTagRequest,
    ) -> main_models.GetHotspotTagResponse:
        runtime = RuntimeOptions()
        return await self.get_hotspot_tag_with_options_async(request, runtime)

    def get_layout_data_with_options(
        self,
        request: main_models.GetLayoutDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLayoutDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLayoutData',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLayoutDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_layout_data_with_options_async(
        self,
        request: main_models.GetLayoutDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLayoutDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLayoutData',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLayoutDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_layout_data(
        self,
        request: main_models.GetLayoutDataRequest,
    ) -> main_models.GetLayoutDataResponse:
        runtime = RuntimeOptions()
        return self.get_layout_data_with_options(request, runtime)

    async def get_layout_data_async(
        self,
        request: main_models.GetLayoutDataRequest,
    ) -> main_models.GetLayoutDataResponse:
        runtime = RuntimeOptions()
        return await self.get_layout_data_with_options_async(request, runtime)

    def get_origin_layout_data_with_options(
        self,
        request: main_models.GetOriginLayoutDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOriginLayoutDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOriginLayoutData',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOriginLayoutDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_origin_layout_data_with_options_async(
        self,
        request: main_models.GetOriginLayoutDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOriginLayoutDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOriginLayoutData',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOriginLayoutDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_origin_layout_data(
        self,
        request: main_models.GetOriginLayoutDataRequest,
    ) -> main_models.GetOriginLayoutDataResponse:
        runtime = RuntimeOptions()
        return self.get_origin_layout_data_with_options(request, runtime)

    async def get_origin_layout_data_async(
        self,
        request: main_models.GetOriginLayoutDataRequest,
    ) -> main_models.GetOriginLayoutDataResponse:
        runtime = RuntimeOptions()
        return await self.get_origin_layout_data_with_options_async(request, runtime)

    def get_oss_policy_with_options(
        self,
        request: main_models.GetOssPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOssPolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_policy_with_options_async(
        self,
        request: main_models.GetOssPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOssPolicy',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_policy(
        self,
        request: main_models.GetOssPolicyRequest,
    ) -> main_models.GetOssPolicyResponse:
        runtime = RuntimeOptions()
        return self.get_oss_policy_with_options(request, runtime)

    async def get_oss_policy_async(
        self,
        request: main_models.GetOssPolicyRequest,
    ) -> main_models.GetOssPolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_oss_policy_with_options_async(request, runtime)

    def get_pack_scene_task_status_with_options(
        self,
        request: main_models.GetPackSceneTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPackSceneTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPackSceneTaskStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPackSceneTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pack_scene_task_status_with_options_async(
        self,
        request: main_models.GetPackSceneTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPackSceneTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPackSceneTaskStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPackSceneTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pack_scene_task_status(
        self,
        request: main_models.GetPackSceneTaskStatusRequest,
    ) -> main_models.GetPackSceneTaskStatusResponse:
        runtime = RuntimeOptions()
        return self.get_pack_scene_task_status_with_options(request, runtime)

    async def get_pack_scene_task_status_async(
        self,
        request: main_models.GetPackSceneTaskStatusRequest,
    ) -> main_models.GetPackSceneTaskStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_pack_scene_task_status_with_options_async(request, runtime)

    def get_rectify_image_with_options(
        self,
        request: main_models.GetRectifyImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRectifyImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRectifyImage',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRectifyImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rectify_image_with_options_async(
        self,
        request: main_models.GetRectifyImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRectifyImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRectifyImage',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRectifyImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rectify_image(
        self,
        request: main_models.GetRectifyImageRequest,
    ) -> main_models.GetRectifyImageResponse:
        runtime = RuntimeOptions()
        return self.get_rectify_image_with_options(request, runtime)

    async def get_rectify_image_async(
        self,
        request: main_models.GetRectifyImageRequest,
    ) -> main_models.GetRectifyImageResponse:
        runtime = RuntimeOptions()
        return await self.get_rectify_image_with_options_async(request, runtime)

    def get_scene_build_task_status_with_options(
        self,
        request: main_models.GetSceneBuildTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSceneBuildTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSceneBuildTaskStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSceneBuildTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scene_build_task_status_with_options_async(
        self,
        request: main_models.GetSceneBuildTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSceneBuildTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSceneBuildTaskStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSceneBuildTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scene_build_task_status(
        self,
        request: main_models.GetSceneBuildTaskStatusRequest,
    ) -> main_models.GetSceneBuildTaskStatusResponse:
        runtime = RuntimeOptions()
        return self.get_scene_build_task_status_with_options(request, runtime)

    async def get_scene_build_task_status_async(
        self,
        request: main_models.GetSceneBuildTaskStatusRequest,
    ) -> main_models.GetSceneBuildTaskStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_scene_build_task_status_with_options_async(request, runtime)

    def get_scene_pack_url_with_options(
        self,
        request: main_models.GetScenePackUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScenePackUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScenePackUrl',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScenePackUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scene_pack_url_with_options_async(
        self,
        request: main_models.GetScenePackUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScenePackUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScenePackUrl',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScenePackUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scene_pack_url(
        self,
        request: main_models.GetScenePackUrlRequest,
    ) -> main_models.GetScenePackUrlResponse:
        runtime = RuntimeOptions()
        return self.get_scene_pack_url_with_options(request, runtime)

    async def get_scene_pack_url_async(
        self,
        request: main_models.GetScenePackUrlRequest,
    ) -> main_models.GetScenePackUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_scene_pack_url_with_options_async(request, runtime)

    def get_scene_preview_data_with_options(
        self,
        request: main_models.GetScenePreviewDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScenePreviewDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.preview_token):
            query['PreviewToken'] = request.preview_token
        if not DaraCore.is_null(request.show_tag):
            query['ShowTag'] = request.show_tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScenePreviewData',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScenePreviewDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scene_preview_data_with_options_async(
        self,
        request: main_models.GetScenePreviewDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScenePreviewDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.preview_token):
            query['PreviewToken'] = request.preview_token
        if not DaraCore.is_null(request.show_tag):
            query['ShowTag'] = request.show_tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScenePreviewData',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScenePreviewDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scene_preview_data(
        self,
        request: main_models.GetScenePreviewDataRequest,
    ) -> main_models.GetScenePreviewDataResponse:
        runtime = RuntimeOptions()
        return self.get_scene_preview_data_with_options(request, runtime)

    async def get_scene_preview_data_async(
        self,
        request: main_models.GetScenePreviewDataRequest,
    ) -> main_models.GetScenePreviewDataResponse:
        runtime = RuntimeOptions()
        return await self.get_scene_preview_data_with_options_async(request, runtime)

    def get_scene_preview_info_with_options(
        self,
        request: main_models.GetScenePreviewInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScenePreviewInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.model_token):
            query['ModelToken'] = request.model_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScenePreviewInfo',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScenePreviewInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scene_preview_info_with_options_async(
        self,
        request: main_models.GetScenePreviewInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScenePreviewInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.model_token):
            query['ModelToken'] = request.model_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScenePreviewInfo',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScenePreviewInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scene_preview_info(
        self,
        request: main_models.GetScenePreviewInfoRequest,
    ) -> main_models.GetScenePreviewInfoResponse:
        runtime = RuntimeOptions()
        return self.get_scene_preview_info_with_options(request, runtime)

    async def get_scene_preview_info_async(
        self,
        request: main_models.GetScenePreviewInfoRequest,
    ) -> main_models.GetScenePreviewInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_scene_preview_info_with_options_async(request, runtime)

    def get_scene_preview_resource_with_options(
        self,
        request: main_models.GetScenePreviewResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScenePreviewResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.draft):
            query['Draft'] = request.draft
        if not DaraCore.is_null(request.preview_token):
            query['PreviewToken'] = request.preview_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScenePreviewResource',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScenePreviewResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scene_preview_resource_with_options_async(
        self,
        request: main_models.GetScenePreviewResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScenePreviewResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.draft):
            query['Draft'] = request.draft
        if not DaraCore.is_null(request.preview_token):
            query['PreviewToken'] = request.preview_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScenePreviewResource',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScenePreviewResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scene_preview_resource(
        self,
        request: main_models.GetScenePreviewResourceRequest,
    ) -> main_models.GetScenePreviewResourceResponse:
        runtime = RuntimeOptions()
        return self.get_scene_preview_resource_with_options(request, runtime)

    async def get_scene_preview_resource_async(
        self,
        request: main_models.GetScenePreviewResourceRequest,
    ) -> main_models.GetScenePreviewResourceResponse:
        runtime = RuntimeOptions()
        return await self.get_scene_preview_resource_with_options_async(request, runtime)

    def get_single_conn_data_with_options(
        self,
        request: main_models.GetSingleConnDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSingleConnDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSingleConnData',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSingleConnDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_single_conn_data_with_options_async(
        self,
        request: main_models.GetSingleConnDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSingleConnDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSingleConnData',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSingleConnDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_single_conn_data(
        self,
        request: main_models.GetSingleConnDataRequest,
    ) -> main_models.GetSingleConnDataResponse:
        runtime = RuntimeOptions()
        return self.get_single_conn_data_with_options(request, runtime)

    async def get_single_conn_data_async(
        self,
        request: main_models.GetSingleConnDataRequest,
    ) -> main_models.GetSingleConnDataResponse:
        runtime = RuntimeOptions()
        return await self.get_single_conn_data_with_options_async(request, runtime)

    def get_source_pack_status_with_options(
        self,
        request: main_models.GetSourcePackStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSourcePackStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSourcePackStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSourcePackStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_source_pack_status_with_options_async(
        self,
        request: main_models.GetSourcePackStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSourcePackStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSourcePackStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSourcePackStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_source_pack_status(
        self,
        request: main_models.GetSourcePackStatusRequest,
    ) -> main_models.GetSourcePackStatusResponse:
        runtime = RuntimeOptions()
        return self.get_source_pack_status_with_options(request, runtime)

    async def get_source_pack_status_async(
        self,
        request: main_models.GetSourcePackStatusRequest,
    ) -> main_models.GetSourcePackStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_source_pack_status_with_options_async(request, runtime)

    def get_sub_scene_task_status_with_options(
        self,
        request: main_models.GetSubSceneTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSubSceneTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSubSceneTaskStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubSceneTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sub_scene_task_status_with_options_async(
        self,
        request: main_models.GetSubSceneTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSubSceneTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSubSceneTaskStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubSceneTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sub_scene_task_status(
        self,
        request: main_models.GetSubSceneTaskStatusRequest,
    ) -> main_models.GetSubSceneTaskStatusResponse:
        runtime = RuntimeOptions()
        return self.get_sub_scene_task_status_with_options(request, runtime)

    async def get_sub_scene_task_status_async(
        self,
        request: main_models.GetSubSceneTaskStatusRequest,
    ) -> main_models.GetSubSceneTaskStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_sub_scene_task_status_with_options_async(request, runtime)

    def get_task_status_with_options(
        self,
        request: main_models.GetTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_status_with_options_async(
        self,
        request: main_models.GetTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_status(
        self,
        request: main_models.GetTaskStatusRequest,
    ) -> main_models.GetTaskStatusResponse:
        runtime = RuntimeOptions()
        return self.get_task_status_with_options(request, runtime)

    async def get_task_status_async(
        self,
        request: main_models.GetTaskStatusRequest,
    ) -> main_models.GetTaskStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_task_status_with_options_async(request, runtime)

    def get_window_config_with_options(
        self,
        request: main_models.GetWindowConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWindowConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.preview_token):
            query['PreviewToken'] = request.preview_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWindowConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWindowConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_window_config_with_options_async(
        self,
        request: main_models.GetWindowConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWindowConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.preview_token):
            query['PreviewToken'] = request.preview_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWindowConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWindowConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_window_config(
        self,
        request: main_models.GetWindowConfigRequest,
    ) -> main_models.GetWindowConfigResponse:
        runtime = RuntimeOptions()
        return self.get_window_config_with_options(request, runtime)

    async def get_window_config_async(
        self,
        request: main_models.GetWindowConfigRequest,
    ) -> main_models.GetWindowConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_window_config_with_options_async(request, runtime)

    def label_build_with_options(
        self,
        request: main_models.LabelBuildRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LabelBuildResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.model_style):
            query['ModelStyle'] = request.model_style
        if not DaraCore.is_null(request.optimize_wall_width):
            query['OptimizeWallWidth'] = request.optimize_wall_width
        if not DaraCore.is_null(request.plan_style):
            query['PlanStyle'] = request.plan_style
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.wall_height):
            query['WallHeight'] = request.wall_height
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LabelBuild',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LabelBuildResponse(),
            self.call_api(params, req, runtime)
        )

    async def label_build_with_options_async(
        self,
        request: main_models.LabelBuildRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LabelBuildResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.model_style):
            query['ModelStyle'] = request.model_style
        if not DaraCore.is_null(request.optimize_wall_width):
            query['OptimizeWallWidth'] = request.optimize_wall_width
        if not DaraCore.is_null(request.plan_style):
            query['PlanStyle'] = request.plan_style
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.wall_height):
            query['WallHeight'] = request.wall_height
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LabelBuild',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LabelBuildResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def label_build(
        self,
        request: main_models.LabelBuildRequest,
    ) -> main_models.LabelBuildResponse:
        runtime = RuntimeOptions()
        return self.label_build_with_options(request, runtime)

    async def label_build_async(
        self,
        request: main_models.LabelBuildRequest,
    ) -> main_models.LabelBuildResponse:
        runtime = RuntimeOptions()
        return await self.label_build_with_options_async(request, runtime)

    def link_image_with_options(
        self,
        request: main_models.LinkImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LinkImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.camera_height):
            query['CameraHeight'] = request.camera_height
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LinkImage',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LinkImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def link_image_with_options_async(
        self,
        request: main_models.LinkImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LinkImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.camera_height):
            query['CameraHeight'] = request.camera_height
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LinkImage',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LinkImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def link_image(
        self,
        request: main_models.LinkImageRequest,
    ) -> main_models.LinkImageResponse:
        runtime = RuntimeOptions()
        return self.link_image_with_options(request, runtime)

    async def link_image_async(
        self,
        request: main_models.LinkImageRequest,
    ) -> main_models.LinkImageResponse:
        runtime = RuntimeOptions()
        return await self.link_image_with_options_async(request, runtime)

    def list_project_with_options(
        self,
        request: main_models.ListProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProject',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_with_options_async(
        self,
        request: main_models.ListProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProject',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project(
        self,
        request: main_models.ListProjectRequest,
    ) -> main_models.ListProjectResponse:
        runtime = RuntimeOptions()
        return self.list_project_with_options(request, runtime)

    async def list_project_async(
        self,
        request: main_models.ListProjectRequest,
    ) -> main_models.ListProjectResponse:
        runtime = RuntimeOptions()
        return await self.list_project_with_options_async(request, runtime)

    def list_scene_with_options(
        self,
        request: main_models.ListSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scene_with_options_async(
        self,
        request: main_models.ListSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scene(
        self,
        request: main_models.ListSceneRequest,
    ) -> main_models.ListSceneResponse:
        runtime = RuntimeOptions()
        return self.list_scene_with_options(request, runtime)

    async def list_scene_async(
        self,
        request: main_models.ListSceneRequest,
    ) -> main_models.ListSceneResponse:
        runtime = RuntimeOptions()
        return await self.list_scene_with_options_async(request, runtime)

    def list_sub_scene_with_options(
        self,
        request: main_models.ListSubSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSubSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.show_layout_data):
            query['ShowLayoutData'] = request.show_layout_data
        if not DaraCore.is_null(request.sort_field):
            query['SortField'] = request.sort_field
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSubScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sub_scene_with_options_async(
        self,
        request: main_models.ListSubSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSubSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.show_layout_data):
            query['ShowLayoutData'] = request.show_layout_data
        if not DaraCore.is_null(request.sort_field):
            query['SortField'] = request.sort_field
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSubScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sub_scene(
        self,
        request: main_models.ListSubSceneRequest,
    ) -> main_models.ListSubSceneResponse:
        runtime = RuntimeOptions()
        return self.list_sub_scene_with_options(request, runtime)

    async def list_sub_scene_async(
        self,
        request: main_models.ListSubSceneRequest,
    ) -> main_models.ListSubSceneResponse:
        runtime = RuntimeOptions()
        return await self.list_sub_scene_with_options_async(request, runtime)

    def optimize_right_angle_with_options(
        self,
        request: main_models.OptimizeRightAngleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OptimizeRightAngleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OptimizeRightAngle',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OptimizeRightAngleResponse(),
            self.call_api(params, req, runtime)
        )

    async def optimize_right_angle_with_options_async(
        self,
        request: main_models.OptimizeRightAngleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OptimizeRightAngleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OptimizeRightAngle',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OptimizeRightAngleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def optimize_right_angle(
        self,
        request: main_models.OptimizeRightAngleRequest,
    ) -> main_models.OptimizeRightAngleResponse:
        runtime = RuntimeOptions()
        return self.optimize_right_angle_with_options(request, runtime)

    async def optimize_right_angle_async(
        self,
        request: main_models.OptimizeRightAngleRequest,
    ) -> main_models.OptimizeRightAngleResponse:
        runtime = RuntimeOptions()
        return await self.optimize_right_angle_with_options_async(request, runtime)

    def pack_scene_with_options(
        self,
        request: main_models.PackSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PackSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PackScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PackSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def pack_scene_with_options_async(
        self,
        request: main_models.PackSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PackSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PackScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PackSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pack_scene(
        self,
        request: main_models.PackSceneRequest,
    ) -> main_models.PackSceneResponse:
        runtime = RuntimeOptions()
        return self.pack_scene_with_options(request, runtime)

    async def pack_scene_async(
        self,
        request: main_models.PackSceneRequest,
    ) -> main_models.PackSceneResponse:
        runtime = RuntimeOptions()
        return await self.pack_scene_with_options_async(request, runtime)

    def pack_source_with_options(
        self,
        request: main_models.PackSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PackSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PackSource',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PackSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def pack_source_with_options_async(
        self,
        request: main_models.PackSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PackSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PackSource',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PackSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pack_source(
        self,
        request: main_models.PackSourceRequest,
    ) -> main_models.PackSourceResponse:
        runtime = RuntimeOptions()
        return self.pack_source_with_options(request, runtime)

    async def pack_source_async(
        self,
        request: main_models.PackSourceRequest,
    ) -> main_models.PackSourceResponse:
        runtime = RuntimeOptions()
        return await self.pack_source_with_options_async(request, runtime)

    def pred_image_with_options(
        self,
        request: main_models.PredImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PredImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.correct_vertical):
            query['CorrectVertical'] = request.correct_vertical
        if not DaraCore.is_null(request.count_detect_door):
            query['CountDetectDoor'] = request.count_detect_door
        if not DaraCore.is_null(request.detect_door):
            query['DetectDoor'] = request.detect_door
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PredImage',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PredImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def pred_image_with_options_async(
        self,
        request: main_models.PredImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PredImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.correct_vertical):
            query['CorrectVertical'] = request.correct_vertical
        if not DaraCore.is_null(request.count_detect_door):
            query['CountDetectDoor'] = request.count_detect_door
        if not DaraCore.is_null(request.detect_door):
            query['DetectDoor'] = request.detect_door
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PredImage',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PredImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pred_image(
        self,
        request: main_models.PredImageRequest,
    ) -> main_models.PredImageResponse:
        runtime = RuntimeOptions()
        return self.pred_image_with_options(request, runtime)

    async def pred_image_async(
        self,
        request: main_models.PredImageRequest,
    ) -> main_models.PredImageResponse:
        runtime = RuntimeOptions()
        return await self.pred_image_with_options_async(request, runtime)

    def prediction_wall_line_with_options(
        self,
        request: main_models.PredictionWallLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PredictionWallLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.camera_height):
            query['CameraHeight'] = request.camera_height
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PredictionWallLine',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PredictionWallLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def prediction_wall_line_with_options_async(
        self,
        request: main_models.PredictionWallLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PredictionWallLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.camera_height):
            query['CameraHeight'] = request.camera_height
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PredictionWallLine',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PredictionWallLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def prediction_wall_line(
        self,
        request: main_models.PredictionWallLineRequest,
    ) -> main_models.PredictionWallLineResponse:
        runtime = RuntimeOptions()
        return self.prediction_wall_line_with_options(request, runtime)

    async def prediction_wall_line_async(
        self,
        request: main_models.PredictionWallLineRequest,
    ) -> main_models.PredictionWallLineResponse:
        runtime = RuntimeOptions()
        return await self.prediction_wall_line_with_options_async(request, runtime)

    def publish_hotspot_with_options(
        self,
        request: main_models.PublishHotspotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishHotspotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.param_tag):
            query['ParamTag'] = request.param_tag
        if not DaraCore.is_null(request.sub_scene_uuid):
            query['SubSceneUuid'] = request.sub_scene_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishHotspot',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishHotspotResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_hotspot_with_options_async(
        self,
        request: main_models.PublishHotspotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishHotspotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.param_tag):
            query['ParamTag'] = request.param_tag
        if not DaraCore.is_null(request.sub_scene_uuid):
            query['SubSceneUuid'] = request.sub_scene_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishHotspot',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishHotspotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_hotspot(
        self,
        request: main_models.PublishHotspotRequest,
    ) -> main_models.PublishHotspotResponse:
        runtime = RuntimeOptions()
        return self.publish_hotspot_with_options(request, runtime)

    async def publish_hotspot_async(
        self,
        request: main_models.PublishHotspotRequest,
    ) -> main_models.PublishHotspotResponse:
        runtime = RuntimeOptions()
        return await self.publish_hotspot_with_options_async(request, runtime)

    def publish_hotspot_config_with_options(
        self,
        request: main_models.PublishHotspotConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishHotspotConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishHotspotConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishHotspotConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_hotspot_config_with_options_async(
        self,
        request: main_models.PublishHotspotConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishHotspotConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishHotspotConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishHotspotConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_hotspot_config(
        self,
        request: main_models.PublishHotspotConfigRequest,
    ) -> main_models.PublishHotspotConfigResponse:
        runtime = RuntimeOptions()
        return self.publish_hotspot_config_with_options(request, runtime)

    async def publish_hotspot_config_async(
        self,
        request: main_models.PublishHotspotConfigRequest,
    ) -> main_models.PublishHotspotConfigResponse:
        runtime = RuntimeOptions()
        return await self.publish_hotspot_config_with_options_async(request, runtime)

    def publish_scene_with_options(
        self,
        request: main_models.PublishSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_scene_with_options_async(
        self,
        request: main_models.PublishSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_scene(
        self,
        request: main_models.PublishSceneRequest,
    ) -> main_models.PublishSceneResponse:
        runtime = RuntimeOptions()
        return self.publish_scene_with_options(request, runtime)

    async def publish_scene_async(
        self,
        request: main_models.PublishSceneRequest,
    ) -> main_models.PublishSceneResponse:
        runtime = RuntimeOptions()
        return await self.publish_scene_with_options_async(request, runtime)

    def publish_status_with_options(
        self,
        request: main_models.PublishStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_status_with_options_async(
        self,
        request: main_models.PublishStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_status(
        self,
        request: main_models.PublishStatusRequest,
    ) -> main_models.PublishStatusResponse:
        runtime = RuntimeOptions()
        return self.publish_status_with_options(request, runtime)

    async def publish_status_async(
        self,
        request: main_models.PublishStatusRequest,
    ) -> main_models.PublishStatusResponse:
        runtime = RuntimeOptions()
        return await self.publish_status_with_options_async(request, runtime)

    def recovery_origin_image_with_options(
        self,
        request: main_models.RecoveryOriginImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecoveryOriginImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecoveryOriginImage',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecoveryOriginImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def recovery_origin_image_with_options_async(
        self,
        request: main_models.RecoveryOriginImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecoveryOriginImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecoveryOriginImage',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecoveryOriginImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recovery_origin_image(
        self,
        request: main_models.RecoveryOriginImageRequest,
    ) -> main_models.RecoveryOriginImageResponse:
        runtime = RuntimeOptions()
        return self.recovery_origin_image_with_options(request, runtime)

    async def recovery_origin_image_async(
        self,
        request: main_models.RecoveryOriginImageRequest,
    ) -> main_models.RecoveryOriginImageResponse:
        runtime = RuntimeOptions()
        return await self.recovery_origin_image_with_options_async(request, runtime)

    def rect_vertical_with_options(
        self,
        request: main_models.RectVerticalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RectVerticalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.count_detect_door):
            query['CountDetectDoor'] = request.count_detect_door
        if not DaraCore.is_null(request.detect_door):
            query['DetectDoor'] = request.detect_door
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        if not DaraCore.is_null(request.vertical_rect):
            query['VerticalRect'] = request.vertical_rect
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RectVertical',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RectVerticalResponse(),
            self.call_api(params, req, runtime)
        )

    async def rect_vertical_with_options_async(
        self,
        request: main_models.RectVerticalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RectVerticalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.count_detect_door):
            query['CountDetectDoor'] = request.count_detect_door
        if not DaraCore.is_null(request.detect_door):
            query['DetectDoor'] = request.detect_door
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        if not DaraCore.is_null(request.vertical_rect):
            query['VerticalRect'] = request.vertical_rect
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RectVertical',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RectVerticalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rect_vertical(
        self,
        request: main_models.RectVerticalRequest,
    ) -> main_models.RectVerticalResponse:
        runtime = RuntimeOptions()
        return self.rect_vertical_with_options(request, runtime)

    async def rect_vertical_async(
        self,
        request: main_models.RectVerticalRequest,
    ) -> main_models.RectVerticalResponse:
        runtime = RuntimeOptions()
        return await self.rect_vertical_with_options_async(request, runtime)

    def rectify_image_with_options(
        self,
        request: main_models.RectifyImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RectifyImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.camera_height):
            query['CameraHeight'] = request.camera_height
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RectifyImage',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RectifyImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def rectify_image_with_options_async(
        self,
        request: main_models.RectifyImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RectifyImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.camera_height):
            query['CameraHeight'] = request.camera_height
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RectifyImage',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RectifyImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rectify_image(
        self,
        request: main_models.RectifyImageRequest,
    ) -> main_models.RectifyImageResponse:
        runtime = RuntimeOptions()
        return self.rectify_image_with_options(request, runtime)

    async def rectify_image_async(
        self,
        request: main_models.RectifyImageRequest,
    ) -> main_models.RectifyImageResponse:
        runtime = RuntimeOptions()
        return await self.rectify_image_with_options_async(request, runtime)

    def rollback_sub_scene_with_options(
        self,
        request: main_models.RollbackSubSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackSubSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackSubScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackSubSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_sub_scene_with_options_async(
        self,
        request: main_models.RollbackSubSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackSubSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackSubScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackSubSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_sub_scene(
        self,
        request: main_models.RollbackSubSceneRequest,
    ) -> main_models.RollbackSubSceneResponse:
        runtime = RuntimeOptions()
        return self.rollback_sub_scene_with_options(request, runtime)

    async def rollback_sub_scene_async(
        self,
        request: main_models.RollbackSubSceneRequest,
    ) -> main_models.RollbackSubSceneResponse:
        runtime = RuntimeOptions()
        return await self.rollback_sub_scene_with_options_async(request, runtime)

    def save_hotspot_config_with_options(
        self,
        request: main_models.SaveHotspotConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveHotspotConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.param_tag):
            query['ParamTag'] = request.param_tag
        if not DaraCore.is_null(request.preview_token):
            query['PreviewToken'] = request.preview_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveHotspotConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveHotspotConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_hotspot_config_with_options_async(
        self,
        request: main_models.SaveHotspotConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveHotspotConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.param_tag):
            query['ParamTag'] = request.param_tag
        if not DaraCore.is_null(request.preview_token):
            query['PreviewToken'] = request.preview_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveHotspotConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveHotspotConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_hotspot_config(
        self,
        request: main_models.SaveHotspotConfigRequest,
    ) -> main_models.SaveHotspotConfigResponse:
        runtime = RuntimeOptions()
        return self.save_hotspot_config_with_options(request, runtime)

    async def save_hotspot_config_async(
        self,
        request: main_models.SaveHotspotConfigRequest,
    ) -> main_models.SaveHotspotConfigResponse:
        runtime = RuntimeOptions()
        return await self.save_hotspot_config_with_options_async(request, runtime)

    def save_hotspot_tag_with_options(
        self,
        request: main_models.SaveHotspotTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveHotspotTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.param_tag):
            query['ParamTag'] = request.param_tag
        if not DaraCore.is_null(request.sub_scene_uuid):
            query['SubSceneUuid'] = request.sub_scene_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveHotspotTag',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveHotspotTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_hotspot_tag_with_options_async(
        self,
        request: main_models.SaveHotspotTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveHotspotTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.param_tag):
            query['ParamTag'] = request.param_tag
        if not DaraCore.is_null(request.sub_scene_uuid):
            query['SubSceneUuid'] = request.sub_scene_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveHotspotTag',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveHotspotTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_hotspot_tag(
        self,
        request: main_models.SaveHotspotTagRequest,
    ) -> main_models.SaveHotspotTagResponse:
        runtime = RuntimeOptions()
        return self.save_hotspot_tag_with_options(request, runtime)

    async def save_hotspot_tag_async(
        self,
        request: main_models.SaveHotspotTagRequest,
    ) -> main_models.SaveHotspotTagResponse:
        runtime = RuntimeOptions()
        return await self.save_hotspot_tag_with_options_async(request, runtime)

    def save_hotspot_tag_list_with_options(
        self,
        request: main_models.SaveHotspotTagListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveHotspotTagListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hotspot_list_json):
            query['HotspotListJson'] = request.hotspot_list_json
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveHotspotTagList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveHotspotTagListResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_hotspot_tag_list_with_options_async(
        self,
        request: main_models.SaveHotspotTagListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveHotspotTagListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hotspot_list_json):
            query['HotspotListJson'] = request.hotspot_list_json
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveHotspotTagList',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveHotspotTagListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_hotspot_tag_list(
        self,
        request: main_models.SaveHotspotTagListRequest,
    ) -> main_models.SaveHotspotTagListResponse:
        runtime = RuntimeOptions()
        return self.save_hotspot_tag_list_with_options(request, runtime)

    async def save_hotspot_tag_list_async(
        self,
        request: main_models.SaveHotspotTagListRequest,
    ) -> main_models.SaveHotspotTagListResponse:
        runtime = RuntimeOptions()
        return await self.save_hotspot_tag_list_with_options_async(request, runtime)

    def save_minimap_with_options(
        self,
        request: main_models.SaveMinimapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveMinimapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveMinimap',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveMinimapResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_minimap_with_options_async(
        self,
        request: main_models.SaveMinimapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveMinimapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveMinimap',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveMinimapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_minimap(
        self,
        request: main_models.SaveMinimapRequest,
    ) -> main_models.SaveMinimapResponse:
        runtime = RuntimeOptions()
        return self.save_minimap_with_options(request, runtime)

    async def save_minimap_async(
        self,
        request: main_models.SaveMinimapRequest,
    ) -> main_models.SaveMinimapResponse:
        runtime = RuntimeOptions()
        return await self.save_minimap_with_options_async(request, runtime)

    def save_model_config_with_options(
        self,
        request: main_models.SaveModelConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveModelConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveModelConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveModelConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_model_config_with_options_async(
        self,
        request: main_models.SaveModelConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveModelConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveModelConfig',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveModelConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_model_config(
        self,
        request: main_models.SaveModelConfigRequest,
    ) -> main_models.SaveModelConfigResponse:
        runtime = RuntimeOptions()
        return self.save_model_config_with_options(request, runtime)

    async def save_model_config_async(
        self,
        request: main_models.SaveModelConfigRequest,
    ) -> main_models.SaveModelConfigResponse:
        runtime = RuntimeOptions()
        return await self.save_model_config_with_options_async(request, runtime)

    def scene_publish_with_options(
        self,
        request: main_models.ScenePublishRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ScenePublishResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ScenePublish',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScenePublishResponse(),
            self.call_api(params, req, runtime)
        )

    async def scene_publish_with_options_async(
        self,
        request: main_models.ScenePublishRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ScenePublishResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ScenePublish',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScenePublishResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scene_publish(
        self,
        request: main_models.ScenePublishRequest,
    ) -> main_models.ScenePublishResponse:
        runtime = RuntimeOptions()
        return self.scene_publish_with_options(request, runtime)

    async def scene_publish_async(
        self,
        request: main_models.ScenePublishRequest,
    ) -> main_models.ScenePublishResponse:
        runtime = RuntimeOptions()
        return await self.scene_publish_with_options_async(request, runtime)

    def temp_preview_with_options(
        self,
        request: main_models.TempPreviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TempPreviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TempPreview',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TempPreviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def temp_preview_with_options_async(
        self,
        request: main_models.TempPreviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TempPreviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TempPreview',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TempPreviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def temp_preview(
        self,
        request: main_models.TempPreviewRequest,
    ) -> main_models.TempPreviewResponse:
        runtime = RuntimeOptions()
        return self.temp_preview_with_options(request, runtime)

    async def temp_preview_async(
        self,
        request: main_models.TempPreviewRequest,
    ) -> main_models.TempPreviewResponse:
        runtime = RuntimeOptions()
        return await self.temp_preview_with_options_async(request, runtime)

    def temp_preview_status_with_options(
        self,
        request: main_models.TempPreviewStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TempPreviewStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TempPreviewStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TempPreviewStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def temp_preview_status_with_options_async(
        self,
        request: main_models.TempPreviewStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TempPreviewStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TempPreviewStatus',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TempPreviewStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def temp_preview_status(
        self,
        request: main_models.TempPreviewStatusRequest,
    ) -> main_models.TempPreviewStatusResponse:
        runtime = RuntimeOptions()
        return self.temp_preview_status_with_options(request, runtime)

    async def temp_preview_status_async(
        self,
        request: main_models.TempPreviewStatusRequest,
    ) -> main_models.TempPreviewStatusResponse:
        runtime = RuntimeOptions()
        return await self.temp_preview_status_with_options_async(request, runtime)

    def update_conn_data_with_options(
        self,
        request: main_models.UpdateConnDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConnDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conn_data):
            query['ConnData'] = request.conn_data
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConnData',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConnDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_conn_data_with_options_async(
        self,
        request: main_models.UpdateConnDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConnDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conn_data):
            query['ConnData'] = request.conn_data
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConnData',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConnDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_conn_data(
        self,
        request: main_models.UpdateConnDataRequest,
    ) -> main_models.UpdateConnDataResponse:
        runtime = RuntimeOptions()
        return self.update_conn_data_with_options(request, runtime)

    async def update_conn_data_async(
        self,
        request: main_models.UpdateConnDataRequest,
    ) -> main_models.UpdateConnDataResponse:
        runtime = RuntimeOptions()
        return await self.update_conn_data_with_options_async(request, runtime)

    def update_layout_data_with_options(
        self,
        request: main_models.UpdateLayoutDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLayoutDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.layout_data):
            query['LayoutData'] = request.layout_data
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLayoutData',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLayoutDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_layout_data_with_options_async(
        self,
        request: main_models.UpdateLayoutDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLayoutDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.layout_data):
            query['LayoutData'] = request.layout_data
        if not DaraCore.is_null(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLayoutData',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLayoutDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_layout_data(
        self,
        request: main_models.UpdateLayoutDataRequest,
    ) -> main_models.UpdateLayoutDataResponse:
        runtime = RuntimeOptions()
        return self.update_layout_data_with_options(request, runtime)

    async def update_layout_data_async(
        self,
        request: main_models.UpdateLayoutDataRequest,
    ) -> main_models.UpdateLayoutDataResponse:
        runtime = RuntimeOptions()
        return await self.update_layout_data_with_options_async(request, runtime)

    def update_project_with_options(
        self,
        request: main_models.UpdateProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_id):
            query['BusinessId'] = request.business_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProject',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        request: main_models.UpdateProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_id):
            query['BusinessId'] = request.business_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProject',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project(
        self,
        request: main_models.UpdateProjectRequest,
    ) -> main_models.UpdateProjectResponse:
        runtime = RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    async def update_project_async(
        self,
        request: main_models.UpdateProjectRequest,
    ) -> main_models.UpdateProjectResponse:
        runtime = RuntimeOptions()
        return await self.update_project_with_options_async(request, runtime)

    def update_scene_with_options(
        self,
        request: main_models.UpdateSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scene_with_options_async(
        self,
        request: main_models.UpdateSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scene(
        self,
        request: main_models.UpdateSceneRequest,
    ) -> main_models.UpdateSceneResponse:
        runtime = RuntimeOptions()
        return self.update_scene_with_options(request, runtime)

    async def update_scene_async(
        self,
        request: main_models.UpdateSceneRequest,
    ) -> main_models.UpdateSceneResponse:
        runtime = RuntimeOptions()
        return await self.update_scene_with_options_async(request, runtime)

    def update_sub_scene_with_options(
        self,
        tmp_req: main_models.UpdateSubSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSubSceneResponse:
        tmp_req.validate()
        request = main_models.UpdateSubSceneShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.view_point):
            request.view_point_shrink = Utils.array_to_string_with_specified_style(tmp_req.view_point, 'ViewPoint', 'json')
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.view_point_shrink):
            query['ViewPoint'] = request.view_point_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSubScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSubSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sub_scene_with_options_async(
        self,
        tmp_req: main_models.UpdateSubSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSubSceneResponse:
        tmp_req.validate()
        request = main_models.UpdateSubSceneShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.view_point):
            request.view_point_shrink = Utils.array_to_string_with_specified_style(tmp_req.view_point, 'ViewPoint', 'json')
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.view_point_shrink):
            query['ViewPoint'] = request.view_point_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSubScene',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSubSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sub_scene(
        self,
        request: main_models.UpdateSubSceneRequest,
    ) -> main_models.UpdateSubSceneResponse:
        runtime = RuntimeOptions()
        return self.update_sub_scene_with_options(request, runtime)

    async def update_sub_scene_async(
        self,
        request: main_models.UpdateSubSceneRequest,
    ) -> main_models.UpdateSubSceneResponse:
        runtime = RuntimeOptions()
        return await self.update_sub_scene_with_options_async(request, runtime)

    def update_sub_scene_seq_with_options(
        self,
        tmp_req: main_models.UpdateSubSceneSeqRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSubSceneSeqResponse:
        tmp_req.validate()
        request = main_models.UpdateSubSceneSeqShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sort_sub_scene_ids):
            request.sort_sub_scene_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort_sub_scene_ids, 'SortSubSceneIds', 'json')
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.sort_sub_scene_ids_shrink):
            query['SortSubSceneIds'] = request.sort_sub_scene_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSubSceneSeq',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSubSceneSeqResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sub_scene_seq_with_options_async(
        self,
        tmp_req: main_models.UpdateSubSceneSeqRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSubSceneSeqResponse:
        tmp_req.validate()
        request = main_models.UpdateSubSceneSeqShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sort_sub_scene_ids):
            request.sort_sub_scene_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort_sub_scene_ids, 'SortSubSceneIds', 'json')
        query = {}
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.sort_sub_scene_ids_shrink):
            query['SortSubSceneIds'] = request.sort_sub_scene_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSubSceneSeq',
            version = '2020-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSubSceneSeqResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sub_scene_seq(
        self,
        request: main_models.UpdateSubSceneSeqRequest,
    ) -> main_models.UpdateSubSceneSeqResponse:
        runtime = RuntimeOptions()
        return self.update_sub_scene_seq_with_options(request, runtime)

    async def update_sub_scene_seq_async(
        self,
        request: main_models.UpdateSubSceneSeqRequest,
    ) -> main_models.UpdateSubSceneSeqResponse:
        runtime = RuntimeOptions()
        return await self.update_sub_scene_seq_with_options_async(request, runtime)
