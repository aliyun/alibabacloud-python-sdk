# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tdsr20200101 import models as tdsr_20200101_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_mosaics_with_options(
        self,
        request: tdsr_20200101_models.AddMosaicsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.AddMosaicsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mark_position):
            query['MarkPosition'] = request.mark_position
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMosaics',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddMosaicsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_mosaics_with_options_async(
        self,
        request: tdsr_20200101_models.AddMosaicsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.AddMosaicsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mark_position):
            query['MarkPosition'] = request.mark_position
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMosaics',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddMosaicsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_mosaics(
        self,
        request: tdsr_20200101_models.AddMosaicsRequest,
    ) -> tdsr_20200101_models.AddMosaicsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_mosaics_with_options(request, runtime)

    async def add_mosaics_async(
        self,
        request: tdsr_20200101_models.AddMosaicsRequest,
    ) -> tdsr_20200101_models.AddMosaicsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_mosaics_with_options_async(request, runtime)

    def add_project_with_options(
        self,
        request: tdsr_20200101_models.AddProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.AddProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_id):
            query['BusinessId'] = request.business_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddProject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_project_with_options_async(
        self,
        request: tdsr_20200101_models.AddProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.AddProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_id):
            query['BusinessId'] = request.business_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddProject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_project(
        self,
        request: tdsr_20200101_models.AddProjectRequest,
    ) -> tdsr_20200101_models.AddProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_project_with_options(request, runtime)

    async def add_project_async(
        self,
        request: tdsr_20200101_models.AddProjectRequest,
    ) -> tdsr_20200101_models.AddProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_project_with_options_async(request, runtime)

    def add_relative_position_with_options(
        self,
        request: tdsr_20200101_models.AddRelativePositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.AddRelativePositionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.relative_position):
            query['RelativePosition'] = request.relative_position
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRelativePosition',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddRelativePositionResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_relative_position_with_options_async(
        self,
        request: tdsr_20200101_models.AddRelativePositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.AddRelativePositionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.relative_position):
            query['RelativePosition'] = request.relative_position
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRelativePosition',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddRelativePositionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_relative_position(
        self,
        request: tdsr_20200101_models.AddRelativePositionRequest,
    ) -> tdsr_20200101_models.AddRelativePositionResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_relative_position_with_options(request, runtime)

    async def add_relative_position_async(
        self,
        request: tdsr_20200101_models.AddRelativePositionRequest,
    ) -> tdsr_20200101_models.AddRelativePositionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_relative_position_with_options_async(request, runtime)

    def add_room_plan_with_options(
        self,
        request: tdsr_20200101_models.AddRoomPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.AddRoomPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRoomPlan',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddRoomPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_room_plan_with_options_async(
        self,
        request: tdsr_20200101_models.AddRoomPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.AddRoomPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRoomPlan',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddRoomPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_room_plan(
        self,
        request: tdsr_20200101_models.AddRoomPlanRequest,
    ) -> tdsr_20200101_models.AddRoomPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_room_plan_with_options(request, runtime)

    async def add_room_plan_async(
        self,
        request: tdsr_20200101_models.AddRoomPlanRequest,
    ) -> tdsr_20200101_models.AddRoomPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_room_plan_with_options_async(request, runtime)

    def add_scene_with_options(
        self,
        request: tdsr_20200101_models.AddSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.AddSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.customer_uid):
            query['CustomerUid'] = request.customer_uid
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_scene_with_options_async(
        self,
        request: tdsr_20200101_models.AddSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.AddSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.customer_uid):
            query['CustomerUid'] = request.customer_uid
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_scene(
        self,
        request: tdsr_20200101_models.AddSceneRequest,
    ) -> tdsr_20200101_models.AddSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_scene_with_options(request, runtime)

    async def add_scene_async(
        self,
        request: tdsr_20200101_models.AddSceneRequest,
    ) -> tdsr_20200101_models.AddSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_scene_with_options_async(request, runtime)

    def add_sub_scene_with_options(
        self,
        request: tdsr_20200101_models.AddSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.AddSubSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSubScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddSubSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_sub_scene_with_options_async(
        self,
        request: tdsr_20200101_models.AddSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.AddSubSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSubScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddSubSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_sub_scene(
        self,
        request: tdsr_20200101_models.AddSubSceneRequest,
    ) -> tdsr_20200101_models.AddSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_sub_scene_with_options(request, runtime)

    async def add_sub_scene_async(
        self,
        request: tdsr_20200101_models.AddSubSceneRequest,
    ) -> tdsr_20200101_models.AddSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_sub_scene_with_options_async(request, runtime)

    def check_user_property_with_options(
        self,
        request: tdsr_20200101_models.CheckUserPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.CheckUserPropertyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckUserProperty',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.CheckUserPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_user_property_with_options_async(
        self,
        request: tdsr_20200101_models.CheckUserPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.CheckUserPropertyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckUserProperty',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.CheckUserPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_user_property(
        self,
        request: tdsr_20200101_models.CheckUserPropertyRequest,
    ) -> tdsr_20200101_models.CheckUserPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_user_property_with_options(request, runtime)

    async def check_user_property_async(
        self,
        request: tdsr_20200101_models.CheckUserPropertyRequest,
    ) -> tdsr_20200101_models.CheckUserPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_user_property_with_options_async(request, runtime)

    def copy_scene_with_options(
        self,
        request: tdsr_20200101_models.CopySceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.CopySceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.CopySceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_scene_with_options_async(
        self,
        request: tdsr_20200101_models.CopySceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.CopySceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.CopySceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_scene(
        self,
        request: tdsr_20200101_models.CopySceneRequest,
    ) -> tdsr_20200101_models.CopySceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.copy_scene_with_options(request, runtime)

    async def copy_scene_async(
        self,
        request: tdsr_20200101_models.CopySceneRequest,
    ) -> tdsr_20200101_models.CopySceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.copy_scene_with_options_async(request, runtime)

    def detail_project_with_options(
        self,
        request: tdsr_20200101_models.DetailProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DetailProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetailProject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DetailProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def detail_project_with_options_async(
        self,
        request: tdsr_20200101_models.DetailProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DetailProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetailProject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DetailProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detail_project(
        self,
        request: tdsr_20200101_models.DetailProjectRequest,
    ) -> tdsr_20200101_models.DetailProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.detail_project_with_options(request, runtime)

    async def detail_project_async(
        self,
        request: tdsr_20200101_models.DetailProjectRequest,
    ) -> tdsr_20200101_models.DetailProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detail_project_with_options_async(request, runtime)

    def detail_scene_with_options(
        self,
        request: tdsr_20200101_models.DetailSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DetailSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetailScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DetailSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def detail_scene_with_options_async(
        self,
        request: tdsr_20200101_models.DetailSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DetailSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetailScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DetailSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detail_scene(
        self,
        request: tdsr_20200101_models.DetailSceneRequest,
    ) -> tdsr_20200101_models.DetailSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.detail_scene_with_options(request, runtime)

    async def detail_scene_async(
        self,
        request: tdsr_20200101_models.DetailSceneRequest,
    ) -> tdsr_20200101_models.DetailSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detail_scene_with_options_async(request, runtime)

    def detail_sub_scene_with_options(
        self,
        request: tdsr_20200101_models.DetailSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DetailSubSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetailSubScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DetailSubSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def detail_sub_scene_with_options_async(
        self,
        request: tdsr_20200101_models.DetailSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DetailSubSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetailSubScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DetailSubSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detail_sub_scene(
        self,
        request: tdsr_20200101_models.DetailSubSceneRequest,
    ) -> tdsr_20200101_models.DetailSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.detail_sub_scene_with_options(request, runtime)

    async def detail_sub_scene_async(
        self,
        request: tdsr_20200101_models.DetailSubSceneRequest,
    ) -> tdsr_20200101_models.DetailSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detail_sub_scene_with_options_async(request, runtime)

    def drop_project_with_options(
        self,
        request: tdsr_20200101_models.DropProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DropProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DropProject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DropProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def drop_project_with_options_async(
        self,
        request: tdsr_20200101_models.DropProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DropProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DropProject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DropProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def drop_project(
        self,
        request: tdsr_20200101_models.DropProjectRequest,
    ) -> tdsr_20200101_models.DropProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.drop_project_with_options(request, runtime)

    async def drop_project_async(
        self,
        request: tdsr_20200101_models.DropProjectRequest,
    ) -> tdsr_20200101_models.DropProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.drop_project_with_options_async(request, runtime)

    def drop_scene_with_options(
        self,
        request: tdsr_20200101_models.DropSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DropSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DropScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DropSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def drop_scene_with_options_async(
        self,
        request: tdsr_20200101_models.DropSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DropSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DropScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DropSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def drop_scene(
        self,
        request: tdsr_20200101_models.DropSceneRequest,
    ) -> tdsr_20200101_models.DropSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.drop_scene_with_options(request, runtime)

    async def drop_scene_async(
        self,
        request: tdsr_20200101_models.DropSceneRequest,
    ) -> tdsr_20200101_models.DropSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.drop_scene_with_options_async(request, runtime)

    def drop_sub_scene_with_options(
        self,
        request: tdsr_20200101_models.DropSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DropSubSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DropSubScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DropSubSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def drop_sub_scene_with_options_async(
        self,
        request: tdsr_20200101_models.DropSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.DropSubSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DropSubScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DropSubSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def drop_sub_scene(
        self,
        request: tdsr_20200101_models.DropSubSceneRequest,
    ) -> tdsr_20200101_models.DropSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.drop_sub_scene_with_options(request, runtime)

    async def drop_sub_scene_async(
        self,
        request: tdsr_20200101_models.DropSubSceneRequest,
    ) -> tdsr_20200101_models.DropSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.drop_sub_scene_with_options_async(request, runtime)

    def get_conn_data_with_options(
        self,
        request: tdsr_20200101_models.GetConnDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetConnDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConnData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetConnDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_conn_data_with_options_async(
        self,
        request: tdsr_20200101_models.GetConnDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetConnDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConnData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetConnDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_conn_data(
        self,
        request: tdsr_20200101_models.GetConnDataRequest,
    ) -> tdsr_20200101_models.GetConnDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_conn_data_with_options(request, runtime)

    async def get_conn_data_async(
        self,
        request: tdsr_20200101_models.GetConnDataRequest,
    ) -> tdsr_20200101_models.GetConnDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_conn_data_with_options_async(request, runtime)

    def get_copy_scene_task_status_with_options(
        self,
        request: tdsr_20200101_models.GetCopySceneTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetCopySceneTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCopySceneTaskStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetCopySceneTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_copy_scene_task_status_with_options_async(
        self,
        request: tdsr_20200101_models.GetCopySceneTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetCopySceneTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCopySceneTaskStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetCopySceneTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_copy_scene_task_status(
        self,
        request: tdsr_20200101_models.GetCopySceneTaskStatusRequest,
    ) -> tdsr_20200101_models.GetCopySceneTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_copy_scene_task_status_with_options(request, runtime)

    async def get_copy_scene_task_status_async(
        self,
        request: tdsr_20200101_models.GetCopySceneTaskStatusRequest,
    ) -> tdsr_20200101_models.GetCopySceneTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_copy_scene_task_status_with_options_async(request, runtime)

    def get_hotspot_config_with_options(
        self,
        request: tdsr_20200101_models.GetHotspotConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetHotspotConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotspotConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetHotspotConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotspot_config_with_options_async(
        self,
        request: tdsr_20200101_models.GetHotspotConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetHotspotConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotspotConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetHotspotConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotspot_config(
        self,
        request: tdsr_20200101_models.GetHotspotConfigRequest,
    ) -> tdsr_20200101_models.GetHotspotConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotspot_config_with_options(request, runtime)

    async def get_hotspot_config_async(
        self,
        request: tdsr_20200101_models.GetHotspotConfigRequest,
    ) -> tdsr_20200101_models.GetHotspotConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotspot_config_with_options_async(request, runtime)

    def get_hotspot_scene_data_with_options(
        self,
        request: tdsr_20200101_models.GetHotspotSceneDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetHotspotSceneDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotspotSceneData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetHotspotSceneDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotspot_scene_data_with_options_async(
        self,
        request: tdsr_20200101_models.GetHotspotSceneDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetHotspotSceneDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotspotSceneData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetHotspotSceneDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotspot_scene_data(
        self,
        request: tdsr_20200101_models.GetHotspotSceneDataRequest,
    ) -> tdsr_20200101_models.GetHotspotSceneDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotspot_scene_data_with_options(request, runtime)

    async def get_hotspot_scene_data_async(
        self,
        request: tdsr_20200101_models.GetHotspotSceneDataRequest,
    ) -> tdsr_20200101_models.GetHotspotSceneDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotspot_scene_data_with_options_async(request, runtime)

    def get_hotspot_tag_with_options(
        self,
        request: tdsr_20200101_models.GetHotspotTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetHotspotTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        if not UtilClient.is_unset(request.sub_scene_uuid):
            query['SubSceneUuid'] = request.sub_scene_uuid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotspotTag',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetHotspotTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotspot_tag_with_options_async(
        self,
        request: tdsr_20200101_models.GetHotspotTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetHotspotTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        if not UtilClient.is_unset(request.sub_scene_uuid):
            query['SubSceneUuid'] = request.sub_scene_uuid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotspotTag',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetHotspotTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotspot_tag(
        self,
        request: tdsr_20200101_models.GetHotspotTagRequest,
    ) -> tdsr_20200101_models.GetHotspotTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hotspot_tag_with_options(request, runtime)

    async def get_hotspot_tag_async(
        self,
        request: tdsr_20200101_models.GetHotspotTagRequest,
    ) -> tdsr_20200101_models.GetHotspotTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hotspot_tag_with_options_async(request, runtime)

    def get_layout_data_with_options(
        self,
        request: tdsr_20200101_models.GetLayoutDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetLayoutDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLayoutData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetLayoutDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_layout_data_with_options_async(
        self,
        request: tdsr_20200101_models.GetLayoutDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetLayoutDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLayoutData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetLayoutDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_layout_data(
        self,
        request: tdsr_20200101_models.GetLayoutDataRequest,
    ) -> tdsr_20200101_models.GetLayoutDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_layout_data_with_options(request, runtime)

    async def get_layout_data_async(
        self,
        request: tdsr_20200101_models.GetLayoutDataRequest,
    ) -> tdsr_20200101_models.GetLayoutDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_layout_data_with_options_async(request, runtime)

    def get_origin_layout_data_with_options(
        self,
        request: tdsr_20200101_models.GetOriginLayoutDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetOriginLayoutDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOriginLayoutData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetOriginLayoutDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_origin_layout_data_with_options_async(
        self,
        request: tdsr_20200101_models.GetOriginLayoutDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetOriginLayoutDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOriginLayoutData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetOriginLayoutDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_origin_layout_data(
        self,
        request: tdsr_20200101_models.GetOriginLayoutDataRequest,
    ) -> tdsr_20200101_models.GetOriginLayoutDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_origin_layout_data_with_options(request, runtime)

    async def get_origin_layout_data_async(
        self,
        request: tdsr_20200101_models.GetOriginLayoutDataRequest,
    ) -> tdsr_20200101_models.GetOriginLayoutDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_origin_layout_data_with_options_async(request, runtime)

    def get_oss_policy_with_options(
        self,
        request: tdsr_20200101_models.GetOssPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetOssPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssPolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetOssPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_policy_with_options_async(
        self,
        request: tdsr_20200101_models.GetOssPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetOssPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssPolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetOssPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_policy(
        self,
        request: tdsr_20200101_models.GetOssPolicyRequest,
    ) -> tdsr_20200101_models.GetOssPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oss_policy_with_options(request, runtime)

    async def get_oss_policy_async(
        self,
        request: tdsr_20200101_models.GetOssPolicyRequest,
    ) -> tdsr_20200101_models.GetOssPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oss_policy_with_options_async(request, runtime)

    def get_pack_scene_task_status_with_options(
        self,
        request: tdsr_20200101_models.GetPackSceneTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetPackSceneTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPackSceneTaskStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetPackSceneTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pack_scene_task_status_with_options_async(
        self,
        request: tdsr_20200101_models.GetPackSceneTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetPackSceneTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPackSceneTaskStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetPackSceneTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pack_scene_task_status(
        self,
        request: tdsr_20200101_models.GetPackSceneTaskStatusRequest,
    ) -> tdsr_20200101_models.GetPackSceneTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pack_scene_task_status_with_options(request, runtime)

    async def get_pack_scene_task_status_async(
        self,
        request: tdsr_20200101_models.GetPackSceneTaskStatusRequest,
    ) -> tdsr_20200101_models.GetPackSceneTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pack_scene_task_status_with_options_async(request, runtime)

    def get_rectify_image_with_options(
        self,
        request: tdsr_20200101_models.GetRectifyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetRectifyImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRectifyImage',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetRectifyImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rectify_image_with_options_async(
        self,
        request: tdsr_20200101_models.GetRectifyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetRectifyImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRectifyImage',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetRectifyImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rectify_image(
        self,
        request: tdsr_20200101_models.GetRectifyImageRequest,
    ) -> tdsr_20200101_models.GetRectifyImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_rectify_image_with_options(request, runtime)

    async def get_rectify_image_async(
        self,
        request: tdsr_20200101_models.GetRectifyImageRequest,
    ) -> tdsr_20200101_models.GetRectifyImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_rectify_image_with_options_async(request, runtime)

    def get_scene_build_task_status_with_options(
        self,
        request: tdsr_20200101_models.GetSceneBuildTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetSceneBuildTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSceneBuildTaskStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSceneBuildTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scene_build_task_status_with_options_async(
        self,
        request: tdsr_20200101_models.GetSceneBuildTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetSceneBuildTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSceneBuildTaskStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSceneBuildTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scene_build_task_status(
        self,
        request: tdsr_20200101_models.GetSceneBuildTaskStatusRequest,
    ) -> tdsr_20200101_models.GetSceneBuildTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_scene_build_task_status_with_options(request, runtime)

    async def get_scene_build_task_status_async(
        self,
        request: tdsr_20200101_models.GetSceneBuildTaskStatusRequest,
    ) -> tdsr_20200101_models.GetSceneBuildTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_scene_build_task_status_with_options_async(request, runtime)

    def get_scene_pack_url_with_options(
        self,
        request: tdsr_20200101_models.GetScenePackUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetScenePackUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenePackUrl',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetScenePackUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scene_pack_url_with_options_async(
        self,
        request: tdsr_20200101_models.GetScenePackUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetScenePackUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenePackUrl',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetScenePackUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scene_pack_url(
        self,
        request: tdsr_20200101_models.GetScenePackUrlRequest,
    ) -> tdsr_20200101_models.GetScenePackUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_scene_pack_url_with_options(request, runtime)

    async def get_scene_pack_url_async(
        self,
        request: tdsr_20200101_models.GetScenePackUrlRequest,
    ) -> tdsr_20200101_models.GetScenePackUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_scene_pack_url_with_options_async(request, runtime)

    def get_scene_preview_data_with_options(
        self,
        request: tdsr_20200101_models.GetScenePreviewDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetScenePreviewDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        if not UtilClient.is_unset(request.show_tag):
            query['ShowTag'] = request.show_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenePreviewData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetScenePreviewDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scene_preview_data_with_options_async(
        self,
        request: tdsr_20200101_models.GetScenePreviewDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetScenePreviewDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        if not UtilClient.is_unset(request.show_tag):
            query['ShowTag'] = request.show_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenePreviewData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetScenePreviewDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scene_preview_data(
        self,
        request: tdsr_20200101_models.GetScenePreviewDataRequest,
    ) -> tdsr_20200101_models.GetScenePreviewDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_scene_preview_data_with_options(request, runtime)

    async def get_scene_preview_data_async(
        self,
        request: tdsr_20200101_models.GetScenePreviewDataRequest,
    ) -> tdsr_20200101_models.GetScenePreviewDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_scene_preview_data_with_options_async(request, runtime)

    def get_scene_preview_info_with_options(
        self,
        request: tdsr_20200101_models.GetScenePreviewInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetScenePreviewInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.model_token):
            query['ModelToken'] = request.model_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenePreviewInfo',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetScenePreviewInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scene_preview_info_with_options_async(
        self,
        request: tdsr_20200101_models.GetScenePreviewInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetScenePreviewInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.model_token):
            query['ModelToken'] = request.model_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenePreviewInfo',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetScenePreviewInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scene_preview_info(
        self,
        request: tdsr_20200101_models.GetScenePreviewInfoRequest,
    ) -> tdsr_20200101_models.GetScenePreviewInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_scene_preview_info_with_options(request, runtime)

    async def get_scene_preview_info_async(
        self,
        request: tdsr_20200101_models.GetScenePreviewInfoRequest,
    ) -> tdsr_20200101_models.GetScenePreviewInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_scene_preview_info_with_options_async(request, runtime)

    def get_scene_preview_resource_with_options(
        self,
        request: tdsr_20200101_models.GetScenePreviewResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetScenePreviewResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenePreviewResource',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetScenePreviewResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scene_preview_resource_with_options_async(
        self,
        request: tdsr_20200101_models.GetScenePreviewResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetScenePreviewResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenePreviewResource',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetScenePreviewResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scene_preview_resource(
        self,
        request: tdsr_20200101_models.GetScenePreviewResourceRequest,
    ) -> tdsr_20200101_models.GetScenePreviewResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_scene_preview_resource_with_options(request, runtime)

    async def get_scene_preview_resource_async(
        self,
        request: tdsr_20200101_models.GetScenePreviewResourceRequest,
    ) -> tdsr_20200101_models.GetScenePreviewResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_scene_preview_resource_with_options_async(request, runtime)

    def get_single_conn_data_with_options(
        self,
        request: tdsr_20200101_models.GetSingleConnDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetSingleConnDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSingleConnData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSingleConnDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_single_conn_data_with_options_async(
        self,
        request: tdsr_20200101_models.GetSingleConnDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetSingleConnDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSingleConnData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSingleConnDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_single_conn_data(
        self,
        request: tdsr_20200101_models.GetSingleConnDataRequest,
    ) -> tdsr_20200101_models.GetSingleConnDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_single_conn_data_with_options(request, runtime)

    async def get_single_conn_data_async(
        self,
        request: tdsr_20200101_models.GetSingleConnDataRequest,
    ) -> tdsr_20200101_models.GetSingleConnDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_single_conn_data_with_options_async(request, runtime)

    def get_source_pack_status_with_options(
        self,
        request: tdsr_20200101_models.GetSourcePackStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetSourcePackStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSourcePackStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSourcePackStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_source_pack_status_with_options_async(
        self,
        request: tdsr_20200101_models.GetSourcePackStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetSourcePackStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSourcePackStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSourcePackStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_source_pack_status(
        self,
        request: tdsr_20200101_models.GetSourcePackStatusRequest,
    ) -> tdsr_20200101_models.GetSourcePackStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_source_pack_status_with_options(request, runtime)

    async def get_source_pack_status_async(
        self,
        request: tdsr_20200101_models.GetSourcePackStatusRequest,
    ) -> tdsr_20200101_models.GetSourcePackStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_source_pack_status_with_options_async(request, runtime)

    def get_sub_scene_task_status_with_options(
        self,
        request: tdsr_20200101_models.GetSubSceneTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetSubSceneTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubSceneTaskStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSubSceneTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sub_scene_task_status_with_options_async(
        self,
        request: tdsr_20200101_models.GetSubSceneTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetSubSceneTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubSceneTaskStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSubSceneTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sub_scene_task_status(
        self,
        request: tdsr_20200101_models.GetSubSceneTaskStatusRequest,
    ) -> tdsr_20200101_models.GetSubSceneTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sub_scene_task_status_with_options(request, runtime)

    async def get_sub_scene_task_status_async(
        self,
        request: tdsr_20200101_models.GetSubSceneTaskStatusRequest,
    ) -> tdsr_20200101_models.GetSubSceneTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sub_scene_task_status_with_options_async(request, runtime)

    def get_task_status_with_options(
        self,
        request: tdsr_20200101_models.GetTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_status_with_options_async(
        self,
        request: tdsr_20200101_models.GetTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_status(
        self,
        request: tdsr_20200101_models.GetTaskStatusRequest,
    ) -> tdsr_20200101_models.GetTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_status_with_options(request, runtime)

    async def get_task_status_async(
        self,
        request: tdsr_20200101_models.GetTaskStatusRequest,
    ) -> tdsr_20200101_models.GetTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_status_with_options_async(request, runtime)

    def get_window_config_with_options(
        self,
        request: tdsr_20200101_models.GetWindowConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetWindowConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWindowConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetWindowConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_window_config_with_options_async(
        self,
        request: tdsr_20200101_models.GetWindowConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.GetWindowConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWindowConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetWindowConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_window_config(
        self,
        request: tdsr_20200101_models.GetWindowConfigRequest,
    ) -> tdsr_20200101_models.GetWindowConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_window_config_with_options(request, runtime)

    async def get_window_config_async(
        self,
        request: tdsr_20200101_models.GetWindowConfigRequest,
    ) -> tdsr_20200101_models.GetWindowConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_window_config_with_options_async(request, runtime)

    def label_build_with_options(
        self,
        request: tdsr_20200101_models.LabelBuildRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.LabelBuildResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.model_style):
            query['ModelStyle'] = request.model_style
        if not UtilClient.is_unset(request.optimize_wall_width):
            query['OptimizeWallWidth'] = request.optimize_wall_width
        if not UtilClient.is_unset(request.plan_style):
            query['PlanStyle'] = request.plan_style
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.wall_height):
            query['WallHeight'] = request.wall_height
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LabelBuild',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.LabelBuildResponse(),
            self.call_api(params, req, runtime)
        )

    async def label_build_with_options_async(
        self,
        request: tdsr_20200101_models.LabelBuildRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.LabelBuildResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.model_style):
            query['ModelStyle'] = request.model_style
        if not UtilClient.is_unset(request.optimize_wall_width):
            query['OptimizeWallWidth'] = request.optimize_wall_width
        if not UtilClient.is_unset(request.plan_style):
            query['PlanStyle'] = request.plan_style
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.wall_height):
            query['WallHeight'] = request.wall_height
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LabelBuild',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.LabelBuildResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def label_build(
        self,
        request: tdsr_20200101_models.LabelBuildRequest,
    ) -> tdsr_20200101_models.LabelBuildResponse:
        runtime = util_models.RuntimeOptions()
        return self.label_build_with_options(request, runtime)

    async def label_build_async(
        self,
        request: tdsr_20200101_models.LabelBuildRequest,
    ) -> tdsr_20200101_models.LabelBuildResponse:
        runtime = util_models.RuntimeOptions()
        return await self.label_build_with_options_async(request, runtime)

    def link_image_with_options(
        self,
        request: tdsr_20200101_models.LinkImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.LinkImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.camera_height):
            query['CameraHeight'] = request.camera_height
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LinkImage',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.LinkImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def link_image_with_options_async(
        self,
        request: tdsr_20200101_models.LinkImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.LinkImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.camera_height):
            query['CameraHeight'] = request.camera_height
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LinkImage',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.LinkImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def link_image(
        self,
        request: tdsr_20200101_models.LinkImageRequest,
    ) -> tdsr_20200101_models.LinkImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.link_image_with_options(request, runtime)

    async def link_image_async(
        self,
        request: tdsr_20200101_models.LinkImageRequest,
    ) -> tdsr_20200101_models.LinkImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.link_image_with_options_async(request, runtime)

    def list_project_with_options(
        self,
        request: tdsr_20200101_models.ListProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.ListProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_with_options_async(
        self,
        request: tdsr_20200101_models.ListProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.ListProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project(
        self,
        request: tdsr_20200101_models.ListProjectRequest,
    ) -> tdsr_20200101_models.ListProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_project_with_options(request, runtime)

    async def list_project_async(
        self,
        request: tdsr_20200101_models.ListProjectRequest,
    ) -> tdsr_20200101_models.ListProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_project_with_options_async(request, runtime)

    def list_scene_with_options(
        self,
        request: tdsr_20200101_models.ListSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.ListSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scene_with_options_async(
        self,
        request: tdsr_20200101_models.ListSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.ListSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scene(
        self,
        request: tdsr_20200101_models.ListSceneRequest,
    ) -> tdsr_20200101_models.ListSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_scene_with_options(request, runtime)

    async def list_scene_async(
        self,
        request: tdsr_20200101_models.ListSceneRequest,
    ) -> tdsr_20200101_models.ListSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_scene_with_options_async(request, runtime)

    def list_sub_scene_with_options(
        self,
        request: tdsr_20200101_models.ListSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.ListSubSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.show_layout_data):
            query['ShowLayoutData'] = request.show_layout_data
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListSubSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sub_scene_with_options_async(
        self,
        request: tdsr_20200101_models.ListSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.ListSubSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.show_layout_data):
            query['ShowLayoutData'] = request.show_layout_data
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListSubSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sub_scene(
        self,
        request: tdsr_20200101_models.ListSubSceneRequest,
    ) -> tdsr_20200101_models.ListSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sub_scene_with_options(request, runtime)

    async def list_sub_scene_async(
        self,
        request: tdsr_20200101_models.ListSubSceneRequest,
    ) -> tdsr_20200101_models.ListSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sub_scene_with_options_async(request, runtime)

    def optimize_right_angle_with_options(
        self,
        request: tdsr_20200101_models.OptimizeRightAngleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.OptimizeRightAngleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OptimizeRightAngle',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.OptimizeRightAngleResponse(),
            self.call_api(params, req, runtime)
        )

    async def optimize_right_angle_with_options_async(
        self,
        request: tdsr_20200101_models.OptimizeRightAngleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.OptimizeRightAngleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OptimizeRightAngle',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.OptimizeRightAngleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def optimize_right_angle(
        self,
        request: tdsr_20200101_models.OptimizeRightAngleRequest,
    ) -> tdsr_20200101_models.OptimizeRightAngleResponse:
        runtime = util_models.RuntimeOptions()
        return self.optimize_right_angle_with_options(request, runtime)

    async def optimize_right_angle_async(
        self,
        request: tdsr_20200101_models.OptimizeRightAngleRequest,
    ) -> tdsr_20200101_models.OptimizeRightAngleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.optimize_right_angle_with_options_async(request, runtime)

    def pack_scene_with_options(
        self,
        request: tdsr_20200101_models.PackSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.PackSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PackScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PackSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def pack_scene_with_options_async(
        self,
        request: tdsr_20200101_models.PackSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.PackSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PackScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PackSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pack_scene(
        self,
        request: tdsr_20200101_models.PackSceneRequest,
    ) -> tdsr_20200101_models.PackSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.pack_scene_with_options(request, runtime)

    async def pack_scene_async(
        self,
        request: tdsr_20200101_models.PackSceneRequest,
    ) -> tdsr_20200101_models.PackSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pack_scene_with_options_async(request, runtime)

    def pack_source_with_options(
        self,
        request: tdsr_20200101_models.PackSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.PackSourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PackSource',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PackSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def pack_source_with_options_async(
        self,
        request: tdsr_20200101_models.PackSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.PackSourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PackSource',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PackSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pack_source(
        self,
        request: tdsr_20200101_models.PackSourceRequest,
    ) -> tdsr_20200101_models.PackSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.pack_source_with_options(request, runtime)

    async def pack_source_async(
        self,
        request: tdsr_20200101_models.PackSourceRequest,
    ) -> tdsr_20200101_models.PackSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pack_source_with_options_async(request, runtime)

    def pred_image_with_options(
        self,
        request: tdsr_20200101_models.PredImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.PredImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.correct_vertical):
            query['CorrectVertical'] = request.correct_vertical
        if not UtilClient.is_unset(request.count_detect_door):
            query['CountDetectDoor'] = request.count_detect_door
        if not UtilClient.is_unset(request.detect_door):
            query['DetectDoor'] = request.detect_door
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PredImage',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PredImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def pred_image_with_options_async(
        self,
        request: tdsr_20200101_models.PredImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.PredImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.correct_vertical):
            query['CorrectVertical'] = request.correct_vertical
        if not UtilClient.is_unset(request.count_detect_door):
            query['CountDetectDoor'] = request.count_detect_door
        if not UtilClient.is_unset(request.detect_door):
            query['DetectDoor'] = request.detect_door
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PredImage',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PredImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pred_image(
        self,
        request: tdsr_20200101_models.PredImageRequest,
    ) -> tdsr_20200101_models.PredImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.pred_image_with_options(request, runtime)

    async def pred_image_async(
        self,
        request: tdsr_20200101_models.PredImageRequest,
    ) -> tdsr_20200101_models.PredImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pred_image_with_options_async(request, runtime)

    def prediction_wall_line_with_options(
        self,
        request: tdsr_20200101_models.PredictionWallLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.PredictionWallLineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.camera_height):
            query['CameraHeight'] = request.camera_height
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PredictionWallLine',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PredictionWallLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def prediction_wall_line_with_options_async(
        self,
        request: tdsr_20200101_models.PredictionWallLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.PredictionWallLineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.camera_height):
            query['CameraHeight'] = request.camera_height
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PredictionWallLine',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PredictionWallLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def prediction_wall_line(
        self,
        request: tdsr_20200101_models.PredictionWallLineRequest,
    ) -> tdsr_20200101_models.PredictionWallLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.prediction_wall_line_with_options(request, runtime)

    async def prediction_wall_line_async(
        self,
        request: tdsr_20200101_models.PredictionWallLineRequest,
    ) -> tdsr_20200101_models.PredictionWallLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.prediction_wall_line_with_options_async(request, runtime)

    def publish_hotspot_with_options(
        self,
        request: tdsr_20200101_models.PublishHotspotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.PublishHotspotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_tag):
            query['ParamTag'] = request.param_tag
        if not UtilClient.is_unset(request.sub_scene_uuid):
            query['SubSceneUuid'] = request.sub_scene_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishHotspot',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PublishHotspotResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_hotspot_with_options_async(
        self,
        request: tdsr_20200101_models.PublishHotspotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.PublishHotspotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_tag):
            query['ParamTag'] = request.param_tag
        if not UtilClient.is_unset(request.sub_scene_uuid):
            query['SubSceneUuid'] = request.sub_scene_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishHotspot',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PublishHotspotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_hotspot(
        self,
        request: tdsr_20200101_models.PublishHotspotRequest,
    ) -> tdsr_20200101_models.PublishHotspotResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_hotspot_with_options(request, runtime)

    async def publish_hotspot_async(
        self,
        request: tdsr_20200101_models.PublishHotspotRequest,
    ) -> tdsr_20200101_models.PublishHotspotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_hotspot_with_options_async(request, runtime)

    def publish_scene_with_options(
        self,
        request: tdsr_20200101_models.PublishSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.PublishSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PublishSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_scene_with_options_async(
        self,
        request: tdsr_20200101_models.PublishSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.PublishSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PublishSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_scene(
        self,
        request: tdsr_20200101_models.PublishSceneRequest,
    ) -> tdsr_20200101_models.PublishSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_scene_with_options(request, runtime)

    async def publish_scene_async(
        self,
        request: tdsr_20200101_models.PublishSceneRequest,
    ) -> tdsr_20200101_models.PublishSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_scene_with_options_async(request, runtime)

    def publish_status_with_options(
        self,
        request: tdsr_20200101_models.PublishStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.PublishStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PublishStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_status_with_options_async(
        self,
        request: tdsr_20200101_models.PublishStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.PublishStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PublishStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_status(
        self,
        request: tdsr_20200101_models.PublishStatusRequest,
    ) -> tdsr_20200101_models.PublishStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_status_with_options(request, runtime)

    async def publish_status_async(
        self,
        request: tdsr_20200101_models.PublishStatusRequest,
    ) -> tdsr_20200101_models.PublishStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_status_with_options_async(request, runtime)

    def recovery_origin_image_with_options(
        self,
        request: tdsr_20200101_models.RecoveryOriginImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.RecoveryOriginImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoveryOriginImage',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.RecoveryOriginImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def recovery_origin_image_with_options_async(
        self,
        request: tdsr_20200101_models.RecoveryOriginImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.RecoveryOriginImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoveryOriginImage',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.RecoveryOriginImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recovery_origin_image(
        self,
        request: tdsr_20200101_models.RecoveryOriginImageRequest,
    ) -> tdsr_20200101_models.RecoveryOriginImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.recovery_origin_image_with_options(request, runtime)

    async def recovery_origin_image_async(
        self,
        request: tdsr_20200101_models.RecoveryOriginImageRequest,
    ) -> tdsr_20200101_models.RecoveryOriginImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recovery_origin_image_with_options_async(request, runtime)

    def rect_vertical_with_options(
        self,
        request: tdsr_20200101_models.RectVerticalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.RectVerticalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.count_detect_door):
            query['CountDetectDoor'] = request.count_detect_door
        if not UtilClient.is_unset(request.detect_door):
            query['DetectDoor'] = request.detect_door
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        if not UtilClient.is_unset(request.vertical_rect):
            query['VerticalRect'] = request.vertical_rect
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RectVertical',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.RectVerticalResponse(),
            self.call_api(params, req, runtime)
        )

    async def rect_vertical_with_options_async(
        self,
        request: tdsr_20200101_models.RectVerticalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.RectVerticalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.count_detect_door):
            query['CountDetectDoor'] = request.count_detect_door
        if not UtilClient.is_unset(request.detect_door):
            query['DetectDoor'] = request.detect_door
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        if not UtilClient.is_unset(request.vertical_rect):
            query['VerticalRect'] = request.vertical_rect
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RectVertical',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.RectVerticalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rect_vertical(
        self,
        request: tdsr_20200101_models.RectVerticalRequest,
    ) -> tdsr_20200101_models.RectVerticalResponse:
        runtime = util_models.RuntimeOptions()
        return self.rect_vertical_with_options(request, runtime)

    async def rect_vertical_async(
        self,
        request: tdsr_20200101_models.RectVerticalRequest,
    ) -> tdsr_20200101_models.RectVerticalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rect_vertical_with_options_async(request, runtime)

    def rectify_image_with_options(
        self,
        request: tdsr_20200101_models.RectifyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.RectifyImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.camera_height):
            query['CameraHeight'] = request.camera_height
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RectifyImage',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.RectifyImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def rectify_image_with_options_async(
        self,
        request: tdsr_20200101_models.RectifyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.RectifyImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.camera_height):
            query['CameraHeight'] = request.camera_height
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RectifyImage',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.RectifyImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rectify_image(
        self,
        request: tdsr_20200101_models.RectifyImageRequest,
    ) -> tdsr_20200101_models.RectifyImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.rectify_image_with_options(request, runtime)

    async def rectify_image_async(
        self,
        request: tdsr_20200101_models.RectifyImageRequest,
    ) -> tdsr_20200101_models.RectifyImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rectify_image_with_options_async(request, runtime)

    def rollback_sub_scene_with_options(
        self,
        request: tdsr_20200101_models.RollbackSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.RollbackSubSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackSubScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.RollbackSubSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_sub_scene_with_options_async(
        self,
        request: tdsr_20200101_models.RollbackSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.RollbackSubSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackSubScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.RollbackSubSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_sub_scene(
        self,
        request: tdsr_20200101_models.RollbackSubSceneRequest,
    ) -> tdsr_20200101_models.RollbackSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.rollback_sub_scene_with_options(request, runtime)

    async def rollback_sub_scene_async(
        self,
        request: tdsr_20200101_models.RollbackSubSceneRequest,
    ) -> tdsr_20200101_models.RollbackSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rollback_sub_scene_with_options_async(request, runtime)

    def save_hotspot_config_with_options(
        self,
        request: tdsr_20200101_models.SaveHotspotConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.SaveHotspotConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_tag):
            query['ParamTag'] = request.param_tag
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveHotspotConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.SaveHotspotConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_hotspot_config_with_options_async(
        self,
        request: tdsr_20200101_models.SaveHotspotConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.SaveHotspotConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_tag):
            query['ParamTag'] = request.param_tag
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveHotspotConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.SaveHotspotConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_hotspot_config(
        self,
        request: tdsr_20200101_models.SaveHotspotConfigRequest,
    ) -> tdsr_20200101_models.SaveHotspotConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_hotspot_config_with_options(request, runtime)

    async def save_hotspot_config_async(
        self,
        request: tdsr_20200101_models.SaveHotspotConfigRequest,
    ) -> tdsr_20200101_models.SaveHotspotConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_hotspot_config_with_options_async(request, runtime)

    def save_hotspot_tag_with_options(
        self,
        request: tdsr_20200101_models.SaveHotspotTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.SaveHotspotTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_tag):
            query['ParamTag'] = request.param_tag
        if not UtilClient.is_unset(request.sub_scene_uuid):
            query['SubSceneUuid'] = request.sub_scene_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveHotspotTag',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.SaveHotspotTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_hotspot_tag_with_options_async(
        self,
        request: tdsr_20200101_models.SaveHotspotTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.SaveHotspotTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_tag):
            query['ParamTag'] = request.param_tag
        if not UtilClient.is_unset(request.sub_scene_uuid):
            query['SubSceneUuid'] = request.sub_scene_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveHotspotTag',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.SaveHotspotTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_hotspot_tag(
        self,
        request: tdsr_20200101_models.SaveHotspotTagRequest,
    ) -> tdsr_20200101_models.SaveHotspotTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_hotspot_tag_with_options(request, runtime)

    async def save_hotspot_tag_async(
        self,
        request: tdsr_20200101_models.SaveHotspotTagRequest,
    ) -> tdsr_20200101_models.SaveHotspotTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_hotspot_tag_with_options_async(request, runtime)

    def scene_publish_with_options(
        self,
        request: tdsr_20200101_models.ScenePublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.ScenePublishResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScenePublish',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ScenePublishResponse(),
            self.call_api(params, req, runtime)
        )

    async def scene_publish_with_options_async(
        self,
        request: tdsr_20200101_models.ScenePublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.ScenePublishResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScenePublish',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ScenePublishResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scene_publish(
        self,
        request: tdsr_20200101_models.ScenePublishRequest,
    ) -> tdsr_20200101_models.ScenePublishResponse:
        runtime = util_models.RuntimeOptions()
        return self.scene_publish_with_options(request, runtime)

    async def scene_publish_async(
        self,
        request: tdsr_20200101_models.ScenePublishRequest,
    ) -> tdsr_20200101_models.ScenePublishResponse:
        runtime = util_models.RuntimeOptions()
        return await self.scene_publish_with_options_async(request, runtime)

    def temp_preview_with_options(
        self,
        request: tdsr_20200101_models.TempPreviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.TempPreviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TempPreview',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.TempPreviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def temp_preview_with_options_async(
        self,
        request: tdsr_20200101_models.TempPreviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.TempPreviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TempPreview',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.TempPreviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def temp_preview(
        self,
        request: tdsr_20200101_models.TempPreviewRequest,
    ) -> tdsr_20200101_models.TempPreviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.temp_preview_with_options(request, runtime)

    async def temp_preview_async(
        self,
        request: tdsr_20200101_models.TempPreviewRequest,
    ) -> tdsr_20200101_models.TempPreviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.temp_preview_with_options_async(request, runtime)

    def temp_preview_status_with_options(
        self,
        request: tdsr_20200101_models.TempPreviewStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.TempPreviewStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TempPreviewStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.TempPreviewStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def temp_preview_status_with_options_async(
        self,
        request: tdsr_20200101_models.TempPreviewStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.TempPreviewStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TempPreviewStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.TempPreviewStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def temp_preview_status(
        self,
        request: tdsr_20200101_models.TempPreviewStatusRequest,
    ) -> tdsr_20200101_models.TempPreviewStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.temp_preview_status_with_options(request, runtime)

    async def temp_preview_status_async(
        self,
        request: tdsr_20200101_models.TempPreviewStatusRequest,
    ) -> tdsr_20200101_models.TempPreviewStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.temp_preview_status_with_options_async(request, runtime)

    def update_conn_data_with_options(
        self,
        request: tdsr_20200101_models.UpdateConnDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateConnDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conn_data):
            query['ConnData'] = request.conn_data
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConnData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateConnDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_conn_data_with_options_async(
        self,
        request: tdsr_20200101_models.UpdateConnDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateConnDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conn_data):
            query['ConnData'] = request.conn_data
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConnData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateConnDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_conn_data(
        self,
        request: tdsr_20200101_models.UpdateConnDataRequest,
    ) -> tdsr_20200101_models.UpdateConnDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_conn_data_with_options(request, runtime)

    async def update_conn_data_async(
        self,
        request: tdsr_20200101_models.UpdateConnDataRequest,
    ) -> tdsr_20200101_models.UpdateConnDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_conn_data_with_options_async(request, runtime)

    def update_layout_data_with_options(
        self,
        request: tdsr_20200101_models.UpdateLayoutDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateLayoutDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.layout_data):
            query['LayoutData'] = request.layout_data
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLayoutData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateLayoutDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_layout_data_with_options_async(
        self,
        request: tdsr_20200101_models.UpdateLayoutDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateLayoutDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.layout_data):
            query['LayoutData'] = request.layout_data
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLayoutData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateLayoutDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_layout_data(
        self,
        request: tdsr_20200101_models.UpdateLayoutDataRequest,
    ) -> tdsr_20200101_models.UpdateLayoutDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_layout_data_with_options(request, runtime)

    async def update_layout_data_async(
        self,
        request: tdsr_20200101_models.UpdateLayoutDataRequest,
    ) -> tdsr_20200101_models.UpdateLayoutDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_layout_data_with_options_async(request, runtime)

    def update_project_with_options(
        self,
        request: tdsr_20200101_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_id):
            query['BusinessId'] = request.business_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        request: tdsr_20200101_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_id):
            query['BusinessId'] = request.business_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project(
        self,
        request: tdsr_20200101_models.UpdateProjectRequest,
    ) -> tdsr_20200101_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    async def update_project_async(
        self,
        request: tdsr_20200101_models.UpdateProjectRequest,
    ) -> tdsr_20200101_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_project_with_options_async(request, runtime)

    def update_scene_with_options(
        self,
        request: tdsr_20200101_models.UpdateSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scene_with_options_async(
        self,
        request: tdsr_20200101_models.UpdateSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scene(
        self,
        request: tdsr_20200101_models.UpdateSceneRequest,
    ) -> tdsr_20200101_models.UpdateSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_scene_with_options(request, runtime)

    async def update_scene_async(
        self,
        request: tdsr_20200101_models.UpdateSceneRequest,
    ) -> tdsr_20200101_models.UpdateSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_scene_with_options_async(request, runtime)

    def update_sub_scene_with_options(
        self,
        tmp_req: tdsr_20200101_models.UpdateSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateSubSceneResponse:
        UtilClient.validate_model(tmp_req)
        request = tdsr_20200101_models.UpdateSubSceneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.view_point):
            request.view_point_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.view_point, 'ViewPoint', 'json')
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.view_point_shrink):
            query['ViewPoint'] = request.view_point_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSubScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateSubSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sub_scene_with_options_async(
        self,
        tmp_req: tdsr_20200101_models.UpdateSubSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateSubSceneResponse:
        UtilClient.validate_model(tmp_req)
        request = tdsr_20200101_models.UpdateSubSceneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.view_point):
            request.view_point_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.view_point, 'ViewPoint', 'json')
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.view_point_shrink):
            query['ViewPoint'] = request.view_point_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSubScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateSubSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sub_scene(
        self,
        request: tdsr_20200101_models.UpdateSubSceneRequest,
    ) -> tdsr_20200101_models.UpdateSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_sub_scene_with_options(request, runtime)

    async def update_sub_scene_async(
        self,
        request: tdsr_20200101_models.UpdateSubSceneRequest,
    ) -> tdsr_20200101_models.UpdateSubSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_sub_scene_with_options_async(request, runtime)

    def update_sub_scene_seq_with_options(
        self,
        tmp_req: tdsr_20200101_models.UpdateSubSceneSeqRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateSubSceneSeqResponse:
        UtilClient.validate_model(tmp_req)
        request = tdsr_20200101_models.UpdateSubSceneSeqShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort_sub_scene_ids):
            request.sort_sub_scene_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort_sub_scene_ids, 'SortSubSceneIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.sort_sub_scene_ids_shrink):
            query['SortSubSceneIds'] = request.sort_sub_scene_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSubSceneSeq',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateSubSceneSeqResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sub_scene_seq_with_options_async(
        self,
        tmp_req: tdsr_20200101_models.UpdateSubSceneSeqRequest,
        runtime: util_models.RuntimeOptions,
    ) -> tdsr_20200101_models.UpdateSubSceneSeqResponse:
        UtilClient.validate_model(tmp_req)
        request = tdsr_20200101_models.UpdateSubSceneSeqShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort_sub_scene_ids):
            request.sort_sub_scene_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort_sub_scene_ids, 'SortSubSceneIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.sort_sub_scene_ids_shrink):
            query['SortSubSceneIds'] = request.sort_sub_scene_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSubSceneSeq',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateSubSceneSeqResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sub_scene_seq(
        self,
        request: tdsr_20200101_models.UpdateSubSceneSeqRequest,
    ) -> tdsr_20200101_models.UpdateSubSceneSeqResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_sub_scene_seq_with_options(request, runtime)

    async def update_sub_scene_seq_async(
        self,
        request: tdsr_20200101_models.UpdateSubSceneSeqRequest,
    ) -> tdsr_20200101_models.UpdateSubSceneSeqResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_sub_scene_seq_with_options_async(request, runtime)
