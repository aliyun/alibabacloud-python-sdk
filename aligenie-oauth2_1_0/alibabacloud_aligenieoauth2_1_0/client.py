# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aligenieoauth2_1_0 import models as ali_genieoauth_2__1__0_models
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
        self._endpoint = self.get_endpoint('aligenie', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_playing_list_with_options(
        self,
        tmp_req: ali_genieoauth_2__1__0_models.CreatePlayingListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.CreatePlayingListResponse:
        """
        @summary 创建播放列表
        
        @param tmp_req: CreatePlayingListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePlayingListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieoauth_2__1__0_models.CreatePlayingListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_create_playing_list_request):
            request.open_create_playing_list_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.open_create_playing_list_request, 'OpenCreatePlayingListRequest', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_create_playing_list_request_shrink):
            body['OpenCreatePlayingListRequest'] = request.open_create_playing_list_request_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePlayingList',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/content/playing/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.CreatePlayingListResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_playing_list_with_options_async(
        self,
        tmp_req: ali_genieoauth_2__1__0_models.CreatePlayingListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.CreatePlayingListResponse:
        """
        @summary 创建播放列表
        
        @param tmp_req: CreatePlayingListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePlayingListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieoauth_2__1__0_models.CreatePlayingListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_info):
            request.device_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_info, 'DeviceInfo', 'json')
        if not UtilClient.is_unset(tmp_req.open_create_playing_list_request):
            request.open_create_playing_list_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.open_create_playing_list_request, 'OpenCreatePlayingListRequest', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_info_shrink):
            query['DeviceInfo'] = request.device_info_shrink
        body = {}
        if not UtilClient.is_unset(request.open_create_playing_list_request_shrink):
            body['OpenCreatePlayingListRequest'] = request.open_create_playing_list_request_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePlayingList',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/content/playing/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.CreatePlayingListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_playing_list(
        self,
        request: ali_genieoauth_2__1__0_models.CreatePlayingListRequest,
    ) -> ali_genieoauth_2__1__0_models.CreatePlayingListResponse:
        """
        @summary 创建播放列表
        
        @param request: CreatePlayingListRequest
        @return: CreatePlayingListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_playing_list_with_options(request, headers, runtime)

    async def create_playing_list_async(
        self,
        request: ali_genieoauth_2__1__0_models.CreatePlayingListRequest,
    ) -> ali_genieoauth_2__1__0_models.CreatePlayingListResponse:
        """
        @summary 创建播放列表
        
        @param request: CreatePlayingListRequest
        @return: CreatePlayingListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_playing_list_with_options_async(request, headers, runtime)

    def execute_scene_with_options(
        self,
        request: ali_genieoauth_2__1__0_models.ExecuteSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.ExecuteSceneResponse:
        """
        @summary 执行场景
        
        @param request: ExecuteSceneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteSceneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteScene',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/iot/scene/execute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.ExecuteSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_scene_with_options_async(
        self,
        request: ali_genieoauth_2__1__0_models.ExecuteSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.ExecuteSceneResponse:
        """
        @summary 执行场景
        
        @param request: ExecuteSceneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteSceneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteScene',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/iot/scene/execute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.ExecuteSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_scene(
        self,
        request: ali_genieoauth_2__1__0_models.ExecuteSceneRequest,
    ) -> ali_genieoauth_2__1__0_models.ExecuteSceneResponse:
        """
        @summary 执行场景
        
        @param request: ExecuteSceneRequest
        @return: ExecuteSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_scene_with_options(request, headers, runtime)

    async def execute_scene_async(
        self,
        request: ali_genieoauth_2__1__0_models.ExecuteSceneRequest,
    ) -> ali_genieoauth_2__1__0_models.ExecuteSceneResponse:
        """
        @summary 执行场景
        
        @param request: ExecuteSceneRequest
        @return: ExecuteSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_scene_with_options_async(request, headers, runtime)

    def execute_smart_home_scene_with_options(
        self,
        request: ali_genieoauth_2__1__0_models.ExecuteSmartHomeSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.ExecuteSmartHomeSceneResponse:
        """
        @summary 执行场景（全屋）
        
        @param request: ExecuteSmartHomeSceneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteSmartHomeSceneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.family_id):
            body['FamilyId'] = request.family_id
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteSmartHomeScene',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/iot/smart_home/scene/execute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.ExecuteSmartHomeSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_smart_home_scene_with_options_async(
        self,
        request: ali_genieoauth_2__1__0_models.ExecuteSmartHomeSceneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.ExecuteSmartHomeSceneResponse:
        """
        @summary 执行场景（全屋）
        
        @param request: ExecuteSmartHomeSceneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteSmartHomeSceneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.family_id):
            body['FamilyId'] = request.family_id
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteSmartHomeScene',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/iot/smart_home/scene/execute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.ExecuteSmartHomeSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_smart_home_scene(
        self,
        request: ali_genieoauth_2__1__0_models.ExecuteSmartHomeSceneRequest,
    ) -> ali_genieoauth_2__1__0_models.ExecuteSmartHomeSceneResponse:
        """
        @summary 执行场景（全屋）
        
        @param request: ExecuteSmartHomeSceneRequest
        @return: ExecuteSmartHomeSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_smart_home_scene_with_options(request, headers, runtime)

    async def execute_smart_home_scene_async(
        self,
        request: ali_genieoauth_2__1__0_models.ExecuteSmartHomeSceneRequest,
    ) -> ali_genieoauth_2__1__0_models.ExecuteSmartHomeSceneResponse:
        """
        @summary 执行场景（全屋）
        
        @param request: ExecuteSmartHomeSceneRequest
        @return: ExecuteSmartHomeSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_smart_home_scene_with_options_async(request, headers, runtime)

    def get_scene_list_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.GetSceneListResponse:
        """
        @summary 获取场景列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSceneListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSceneList',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/iot/scene/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.GetSceneListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scene_list_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.GetSceneListResponse:
        """
        @summary 获取场景列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSceneListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSceneList',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/iot/scene/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.GetSceneListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scene_list(self) -> ali_genieoauth_2__1__0_models.GetSceneListResponse:
        """
        @summary 获取场景列表
        
        @return: GetSceneListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_scene_list_with_options(headers, runtime)

    async def get_scene_list_async(self) -> ali_genieoauth_2__1__0_models.GetSceneListResponse:
        """
        @summary 获取场景列表
        
        @return: GetSceneListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_scene_list_with_options_async(headers, runtime)

    def get_smart_home_scene_list_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.GetSmartHomeSceneListResponse:
        """
        @summary 获取场景列表（全屋）
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSmartHomeSceneListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSmartHomeSceneList',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/iot/smart_home/scene/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.GetSmartHomeSceneListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_smart_home_scene_list_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.GetSmartHomeSceneListResponse:
        """
        @summary 获取场景列表（全屋）
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSmartHomeSceneListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSmartHomeSceneList',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/iot/smart_home/scene/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.GetSmartHomeSceneListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_smart_home_scene_list(self) -> ali_genieoauth_2__1__0_models.GetSmartHomeSceneListResponse:
        """
        @summary 获取场景列表（全屋）
        
        @return: GetSmartHomeSceneListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_smart_home_scene_list_with_options(headers, runtime)

    async def get_smart_home_scene_list_async(self) -> ali_genieoauth_2__1__0_models.GetSmartHomeSceneListResponse:
        """
        @summary 获取场景列表（全屋）
        
        @return: GetSmartHomeSceneListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_smart_home_scene_list_with_options_async(headers, runtime)

    def get_user_basic_info_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.GetUserBasicInfoResponse:
        """
        @summary 获取
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserBasicInfoResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUserBasicInfo',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/users/basic',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.GetUserBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_basic_info_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.GetUserBasicInfoResponse:
        """
        @summary 获取
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserBasicInfoResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUserBasicInfo',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/users/basic',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.GetUserBasicInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_basic_info(self) -> ali_genieoauth_2__1__0_models.GetUserBasicInfoResponse:
        """
        @summary 获取
        
        @return: GetUserBasicInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_basic_info_with_options(headers, runtime)

    async def get_user_basic_info_async(self) -> ali_genieoauth_2__1__0_models.GetUserBasicInfoResponse:
        """
        @summary 获取
        
        @return: GetUserBasicInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_basic_info_with_options_async(headers, runtime)

    def get_user_phone_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.GetUserPhoneResponse:
        """
        @summary 获取天猫精灵用户绑定的手机号
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserPhoneResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUserPhone',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/user/profile/phone',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.GetUserPhoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_phone_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.GetUserPhoneResponse:
        """
        @summary 获取天猫精灵用户绑定的手机号
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserPhoneResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUserPhone',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/user/profile/phone',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.GetUserPhoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_phone(self) -> ali_genieoauth_2__1__0_models.GetUserPhoneResponse:
        """
        @summary 获取天猫精灵用户绑定的手机号
        
        @return: GetUserPhoneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_phone_with_options(headers, runtime)

    async def get_user_phone_async(self) -> ali_genieoauth_2__1__0_models.GetUserPhoneResponse:
        """
        @summary 获取天猫精灵用户绑定的手机号
        
        @return: GetUserPhoneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_phone_with_options_async(headers, runtime)

    def o_auth_2revocation_endpoint_with_options(
        self,
        request: ali_genieoauth_2__1__0_models.OAuth2RevocationEndpointRequest,
        headers: ali_genieoauth_2__1__0_models.OAuth2RevocationEndpointHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.OAuth2RevocationEndpointResponse:
        """
        @summary OAuth2令牌撤销端点
        
        @param request: OAuth2RevocationEndpointRequest
        @param headers: OAuth2RevocationEndpointHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: OAuth2RevocationEndpointResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.token_type_hint):
            body['TokenTypeHint'] = request.token_type_hint
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OAuth2RevocationEndpoint',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/revoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.OAuth2RevocationEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def o_auth_2revocation_endpoint_with_options_async(
        self,
        request: ali_genieoauth_2__1__0_models.OAuth2RevocationEndpointRequest,
        headers: ali_genieoauth_2__1__0_models.OAuth2RevocationEndpointHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.OAuth2RevocationEndpointResponse:
        """
        @summary OAuth2令牌撤销端点
        
        @param request: OAuth2RevocationEndpointRequest
        @param headers: OAuth2RevocationEndpointHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: OAuth2RevocationEndpointResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.token_type_hint):
            body['TokenTypeHint'] = request.token_type_hint
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OAuth2RevocationEndpoint',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/revoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.OAuth2RevocationEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def o_auth_2revocation_endpoint(
        self,
        request: ali_genieoauth_2__1__0_models.OAuth2RevocationEndpointRequest,
    ) -> ali_genieoauth_2__1__0_models.OAuth2RevocationEndpointResponse:
        """
        @summary OAuth2令牌撤销端点
        
        @param request: OAuth2RevocationEndpointRequest
        @return: OAuth2RevocationEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieoauth_2__1__0_models.OAuth2RevocationEndpointHeaders()
        return self.o_auth_2revocation_endpoint_with_options(request, headers, runtime)

    async def o_auth_2revocation_endpoint_async(
        self,
        request: ali_genieoauth_2__1__0_models.OAuth2RevocationEndpointRequest,
    ) -> ali_genieoauth_2__1__0_models.OAuth2RevocationEndpointResponse:
        """
        @summary OAuth2令牌撤销端点
        
        @param request: OAuth2RevocationEndpointRequest
        @return: OAuth2RevocationEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieoauth_2__1__0_models.OAuth2RevocationEndpointHeaders()
        return await self.o_auth_2revocation_endpoint_with_options_async(request, headers, runtime)

    def o_auth_2token_endpoint_with_options(
        self,
        request: ali_genieoauth_2__1__0_models.OAuth2TokenEndpointRequest,
        headers: ali_genieoauth_2__1__0_models.OAuth2TokenEndpointHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.OAuth2TokenEndpointResponse:
        """
        @summary OAuth2令牌端点
        
        @param request: OAuth2TokenEndpointRequest
        @param headers: OAuth2TokenEndpointHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: OAuth2TokenEndpointResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.grant_type):
            body['GrantType'] = request.grant_type
        if not UtilClient.is_unset(request.redirect_uri):
            body['RedirectUri'] = request.redirect_uri
        if not UtilClient.is_unset(request.refresh_token):
            body['RefreshToken'] = request.refresh_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OAuth2TokenEndpoint',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/token',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.OAuth2TokenEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def o_auth_2token_endpoint_with_options_async(
        self,
        request: ali_genieoauth_2__1__0_models.OAuth2TokenEndpointRequest,
        headers: ali_genieoauth_2__1__0_models.OAuth2TokenEndpointHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.OAuth2TokenEndpointResponse:
        """
        @summary OAuth2令牌端点
        
        @param request: OAuth2TokenEndpointRequest
        @param headers: OAuth2TokenEndpointHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: OAuth2TokenEndpointResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.grant_type):
            body['GrantType'] = request.grant_type
        if not UtilClient.is_unset(request.redirect_uri):
            body['RedirectUri'] = request.redirect_uri
        if not UtilClient.is_unset(request.refresh_token):
            body['RefreshToken'] = request.refresh_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_aligenie_access_token):
            real_headers['x-acs-aligenie-access-token'] = UtilClient.to_jsonstring(headers.x_acs_aligenie_access_token)
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OAuth2TokenEndpoint',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/token',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.OAuth2TokenEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def o_auth_2token_endpoint(
        self,
        request: ali_genieoauth_2__1__0_models.OAuth2TokenEndpointRequest,
    ) -> ali_genieoauth_2__1__0_models.OAuth2TokenEndpointResponse:
        """
        @summary OAuth2令牌端点
        
        @param request: OAuth2TokenEndpointRequest
        @return: OAuth2TokenEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieoauth_2__1__0_models.OAuth2TokenEndpointHeaders()
        return self.o_auth_2token_endpoint_with_options(request, headers, runtime)

    async def o_auth_2token_endpoint_async(
        self,
        request: ali_genieoauth_2__1__0_models.OAuth2TokenEndpointRequest,
    ) -> ali_genieoauth_2__1__0_models.OAuth2TokenEndpointResponse:
        """
        @summary OAuth2令牌端点
        
        @param request: OAuth2TokenEndpointRequest
        @return: OAuth2TokenEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = ali_genieoauth_2__1__0_models.OAuth2TokenEndpointHeaders()
        return await self.o_auth_2token_endpoint_with_options_async(request, headers, runtime)

    def push_device_notification_with_options(
        self,
        tmp_req: ali_genieoauth_2__1__0_models.PushDeviceNotificationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.PushDeviceNotificationResponse:
        """
        @summary 推送设备通知
        
        @param tmp_req: PushDeviceNotificationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushDeviceNotificationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieoauth_2__1__0_models.PushDeviceNotificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tenant_info):
            request.tenant_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_info, 'TenantInfo', 'json')
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_info_shrink):
            body['TenantInfo'] = request.tenant_info_shrink
        if not UtilClient.is_unset(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushDeviceNotification',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/device/notification/push',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.PushDeviceNotificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_device_notification_with_options_async(
        self,
        tmp_req: ali_genieoauth_2__1__0_models.PushDeviceNotificationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.PushDeviceNotificationResponse:
        """
        @summary 推送设备通知
        
        @param tmp_req: PushDeviceNotificationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushDeviceNotificationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ali_genieoauth_2__1__0_models.PushDeviceNotificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tenant_info):
            request.tenant_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_info, 'TenantInfo', 'json')
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_info_shrink):
            body['TenantInfo'] = request.tenant_info_shrink
        if not UtilClient.is_unset(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushDeviceNotification',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/device/notification/push',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.PushDeviceNotificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_device_notification(
        self,
        request: ali_genieoauth_2__1__0_models.PushDeviceNotificationRequest,
    ) -> ali_genieoauth_2__1__0_models.PushDeviceNotificationResponse:
        """
        @summary 推送设备通知
        
        @param request: PushDeviceNotificationRequest
        @return: PushDeviceNotificationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_device_notification_with_options(request, headers, runtime)

    async def push_device_notification_async(
        self,
        request: ali_genieoauth_2__1__0_models.PushDeviceNotificationRequest,
    ) -> ali_genieoauth_2__1__0_models.PushDeviceNotificationResponse:
        """
        @summary 推送设备通知
        
        @param request: PushDeviceNotificationRequest
        @return: PushDeviceNotificationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_device_notification_with_options_async(request, headers, runtime)

    def query_device_list_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.QueryDeviceListResponse:
        """
        @summary 查询设备列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDeviceListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='QueryDeviceList',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/device/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.QueryDeviceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_list_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ali_genieoauth_2__1__0_models.QueryDeviceListResponse:
        """
        @summary 查询设备列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDeviceListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='QueryDeviceList',
            version='oauth2_1.0',
            protocol='HTTPS',
            pathname=f'/v1.0/oauth2/device/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ali_genieoauth_2__1__0_models.QueryDeviceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_device_list(self) -> ali_genieoauth_2__1__0_models.QueryDeviceListResponse:
        """
        @summary 查询设备列表
        
        @return: QueryDeviceListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_device_list_with_options(headers, runtime)

    async def query_device_list_async(self) -> ali_genieoauth_2__1__0_models.QueryDeviceListResponse:
        """
        @summary 查询设备列表
        
        @return: QueryDeviceListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_device_list_with_options_async(headers, runtime)
