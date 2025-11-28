# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_lingmou20250527 import models as ling_mou_20250527_models
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
        self._endpoint = self.get_endpoint('lingmou', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def close_chat_instance_sessions_with_options(
        self,
        instance_id: str,
        tmp_req: ling_mou_20250527_models.CloseChatInstanceSessionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.CloseChatInstanceSessionsResponse:
        """
        @summary 关闭会话实例session
        
        @param tmp_req: CloseChatInstanceSessionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseChatInstanceSessionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ling_mou_20250527_models.CloseChatInstanceSessionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.session_ids):
            request.session_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.session_ids, 'sessionIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.session_ids_shrink):
            body['sessionIds'] = request.session_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloseChatInstanceSessions',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/chat/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sessions/close',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.CloseChatInstanceSessionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_chat_instance_sessions_with_options_async(
        self,
        instance_id: str,
        tmp_req: ling_mou_20250527_models.CloseChatInstanceSessionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.CloseChatInstanceSessionsResponse:
        """
        @summary 关闭会话实例session
        
        @param tmp_req: CloseChatInstanceSessionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseChatInstanceSessionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ling_mou_20250527_models.CloseChatInstanceSessionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.session_ids):
            request.session_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.session_ids, 'sessionIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.session_ids_shrink):
            body['sessionIds'] = request.session_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloseChatInstanceSessions',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/chat/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sessions/close',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.CloseChatInstanceSessionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_chat_instance_sessions(
        self,
        instance_id: str,
        request: ling_mou_20250527_models.CloseChatInstanceSessionsRequest,
    ) -> ling_mou_20250527_models.CloseChatInstanceSessionsResponse:
        """
        @summary 关闭会话实例session
        
        @param request: CloseChatInstanceSessionsRequest
        @return: CloseChatInstanceSessionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.close_chat_instance_sessions_with_options(instance_id, request, headers, runtime)

    async def close_chat_instance_sessions_async(
        self,
        instance_id: str,
        request: ling_mou_20250527_models.CloseChatInstanceSessionsRequest,
    ) -> ling_mou_20250527_models.CloseChatInstanceSessionsResponse:
        """
        @summary 关闭会话实例session
        
        @param request: CloseChatInstanceSessionsRequest
        @return: CloseChatInstanceSessionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.close_chat_instance_sessions_with_options_async(instance_id, request, headers, runtime)

    def confirm_train_pic_avatar_with_options(
        self,
        request: ling_mou_20250527_models.ConfirmTrainPicAvatarRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.ConfirmTrainPicAvatarResponse:
        """
        @summary 用户确认
        
        @param request: ConfirmTrainPicAvatarRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfirmTrainPicAvatarResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.avatar_id):
            query['avatarId'] = request.avatar_id
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmTrainPicAvatar',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/train/confirmTrainPicAvatar',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.ConfirmTrainPicAvatarResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_train_pic_avatar_with_options_async(
        self,
        request: ling_mou_20250527_models.ConfirmTrainPicAvatarRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.ConfirmTrainPicAvatarResponse:
        """
        @summary 用户确认
        
        @param request: ConfirmTrainPicAvatarRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfirmTrainPicAvatarResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.avatar_id):
            query['avatarId'] = request.avatar_id
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmTrainPicAvatar',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/train/confirmTrainPicAvatar',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.ConfirmTrainPicAvatarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_train_pic_avatar(
        self,
        request: ling_mou_20250527_models.ConfirmTrainPicAvatarRequest,
    ) -> ling_mou_20250527_models.ConfirmTrainPicAvatarResponse:
        """
        @summary 用户确认
        
        @param request: ConfirmTrainPicAvatarRequest
        @return: ConfirmTrainPicAvatarResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.confirm_train_pic_avatar_with_options(request, headers, runtime)

    async def confirm_train_pic_avatar_async(
        self,
        request: ling_mou_20250527_models.ConfirmTrainPicAvatarRequest,
    ) -> ling_mou_20250527_models.ConfirmTrainPicAvatarResponse:
        """
        @summary 用户确认
        
        @param request: ConfirmTrainPicAvatarRequest
        @return: ConfirmTrainPicAvatarResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.confirm_train_pic_avatar_with_options_async(request, headers, runtime)

    def create_background_pic_with_options(
        self,
        request: ling_mou_20250527_models.CreateBackgroundPicRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.CreateBackgroundPicResponse:
        """
        @summary 创建背景素材
        
        @param request: CreateBackgroundPicRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackgroundPicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filename):
            query['filename'] = request.filename
        if not UtilClient.is_unset(request.oss_key):
            query['ossKey'] = request.oss_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackgroundPic',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/chat/createBackgroundPic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.CreateBackgroundPicResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_background_pic_with_options_async(
        self,
        request: ling_mou_20250527_models.CreateBackgroundPicRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.CreateBackgroundPicResponse:
        """
        @summary 创建背景素材
        
        @param request: CreateBackgroundPicRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackgroundPicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filename):
            query['filename'] = request.filename
        if not UtilClient.is_unset(request.oss_key):
            query['ossKey'] = request.oss_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackgroundPic',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/chat/createBackgroundPic',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.CreateBackgroundPicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_background_pic(
        self,
        request: ling_mou_20250527_models.CreateBackgroundPicRequest,
    ) -> ling_mou_20250527_models.CreateBackgroundPicResponse:
        """
        @summary 创建背景素材
        
        @param request: CreateBackgroundPicRequest
        @return: CreateBackgroundPicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_background_pic_with_options(request, headers, runtime)

    async def create_background_pic_async(
        self,
        request: ling_mou_20250527_models.CreateBackgroundPicRequest,
    ) -> ling_mou_20250527_models.CreateBackgroundPicResponse:
        """
        @summary 创建背景素材
        
        @param request: CreateBackgroundPicRequest
        @return: CreateBackgroundPicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_background_pic_with_options_async(request, headers, runtime)

    def create_chat_config_with_options(
        self,
        request: ling_mou_20250527_models.CreateChatConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.CreateChatConfigResponse:
        """
        @summary 背景配置
        
        @param request: CreateChatConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChatConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.avatar_id):
            query['avatarId'] = request.avatar_id
        if not UtilClient.is_unset(request.background_id):
            query['backgroundId'] = request.background_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChatConfig',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/chat/createChatConfig',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.CreateChatConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chat_config_with_options_async(
        self,
        request: ling_mou_20250527_models.CreateChatConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.CreateChatConfigResponse:
        """
        @summary 背景配置
        
        @param request: CreateChatConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChatConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.avatar_id):
            query['avatarId'] = request.avatar_id
        if not UtilClient.is_unset(request.background_id):
            query['backgroundId'] = request.background_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChatConfig',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/chat/createChatConfig',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.CreateChatConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chat_config(
        self,
        request: ling_mou_20250527_models.CreateChatConfigRequest,
    ) -> ling_mou_20250527_models.CreateChatConfigResponse:
        """
        @summary 背景配置
        
        @param request: CreateChatConfigRequest
        @return: CreateChatConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_chat_config_with_options(request, headers, runtime)

    async def create_chat_config_async(
        self,
        request: ling_mou_20250527_models.CreateChatConfigRequest,
    ) -> ling_mou_20250527_models.CreateChatConfigResponse:
        """
        @summary 背景配置
        
        @param request: CreateChatConfigRequest
        @return: CreateChatConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_chat_config_with_options_async(request, headers, runtime)

    def create_chat_session_with_options(
        self,
        id: str,
        request: ling_mou_20250527_models.CreateChatSessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.CreateChatSessionResponse:
        """
        @summary 创建数字人会话
        
        @param request: CreateChatSessionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChatSessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.license):
            query['license'] = request.license
        if not UtilClient.is_unset(request.platform):
            query['platform'] = request.platform
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChatSession',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/chat/init/{OpenApiUtilClient.get_encode_param(id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.CreateChatSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chat_session_with_options_async(
        self,
        id: str,
        request: ling_mou_20250527_models.CreateChatSessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.CreateChatSessionResponse:
        """
        @summary 创建数字人会话
        
        @param request: CreateChatSessionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChatSessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.license):
            query['license'] = request.license
        if not UtilClient.is_unset(request.platform):
            query['platform'] = request.platform
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChatSession',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/chat/init/{OpenApiUtilClient.get_encode_param(id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.CreateChatSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chat_session(
        self,
        id: str,
        request: ling_mou_20250527_models.CreateChatSessionRequest,
    ) -> ling_mou_20250527_models.CreateChatSessionResponse:
        """
        @summary 创建数字人会话
        
        @param request: CreateChatSessionRequest
        @return: CreateChatSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_chat_session_with_options(id, request, headers, runtime)

    async def create_chat_session_async(
        self,
        id: str,
        request: ling_mou_20250527_models.CreateChatSessionRequest,
    ) -> ling_mou_20250527_models.CreateChatSessionResponse:
        """
        @summary 创建数字人会话
        
        @param request: CreateChatSessionRequest
        @return: CreateChatSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_chat_session_with_options_async(id, request, headers, runtime)

    def create_no_train_pic_avatar_with_options(
        self,
        request: ling_mou_20250527_models.CreateNoTrainPicAvatarRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.CreateNoTrainPicAvatarResponse:
        """
        @summary 创建对话免训照片数字人
        
        @param request: CreateNoTrainPicAvatarRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNoTrainPicAvatarResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expressiveness):
            query['expressiveness'] = request.expressiveness
        if not UtilClient.is_unset(request.gender):
            query['gender'] = request.gender
        if not UtilClient.is_unset(request.generate_assets):
            query['generateAssets'] = request.generate_assets
        if not UtilClient.is_unset(request.image_oss_path):
            query['imageOssPath'] = request.image_oss_path
        if not UtilClient.is_unset(request.jwt_token):
            query['jwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.transparent):
            query['transparent'] = request.transparent
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNoTrainPicAvatar',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/chat/createNoTrainPicAvatar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.CreateNoTrainPicAvatarResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_no_train_pic_avatar_with_options_async(
        self,
        request: ling_mou_20250527_models.CreateNoTrainPicAvatarRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.CreateNoTrainPicAvatarResponse:
        """
        @summary 创建对话免训照片数字人
        
        @param request: CreateNoTrainPicAvatarRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNoTrainPicAvatarResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expressiveness):
            query['expressiveness'] = request.expressiveness
        if not UtilClient.is_unset(request.gender):
            query['gender'] = request.gender
        if not UtilClient.is_unset(request.generate_assets):
            query['generateAssets'] = request.generate_assets
        if not UtilClient.is_unset(request.image_oss_path):
            query['imageOssPath'] = request.image_oss_path
        if not UtilClient.is_unset(request.jwt_token):
            query['jwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.transparent):
            query['transparent'] = request.transparent
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNoTrainPicAvatar',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/chat/createNoTrainPicAvatar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.CreateNoTrainPicAvatarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_no_train_pic_avatar(
        self,
        request: ling_mou_20250527_models.CreateNoTrainPicAvatarRequest,
    ) -> ling_mou_20250527_models.CreateNoTrainPicAvatarResponse:
        """
        @summary 创建对话免训照片数字人
        
        @param request: CreateNoTrainPicAvatarRequest
        @return: CreateNoTrainPicAvatarResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_no_train_pic_avatar_with_options(request, headers, runtime)

    async def create_no_train_pic_avatar_async(
        self,
        request: ling_mou_20250527_models.CreateNoTrainPicAvatarRequest,
    ) -> ling_mou_20250527_models.CreateNoTrainPicAvatarResponse:
        """
        @summary 创建对话免训照片数字人
        
        @param request: CreateNoTrainPicAvatarRequest
        @return: CreateNoTrainPicAvatarResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_no_train_pic_avatar_with_options_async(request, headers, runtime)

    def create_ttsvoice_custom_with_options(
        self,
        request: ling_mou_20250527_models.CreateTTSVoiceCustomRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.CreateTTSVoiceCustomResponse:
        """
        @summary 创建TTS音色
        
        @param request: CreateTTSVoiceCustomRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTTSVoiceCustomResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.gender):
            query['gender'] = request.gender
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.oss_key):
            query['ossKey'] = request.oss_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTTSVoiceCustom',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/voice/createTTSVoiceCustom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.CreateTTSVoiceCustomResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ttsvoice_custom_with_options_async(
        self,
        request: ling_mou_20250527_models.CreateTTSVoiceCustomRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.CreateTTSVoiceCustomResponse:
        """
        @summary 创建TTS音色
        
        @param request: CreateTTSVoiceCustomRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTTSVoiceCustomResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.gender):
            query['gender'] = request.gender
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.oss_key):
            query['ossKey'] = request.oss_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTTSVoiceCustom',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/voice/createTTSVoiceCustom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.CreateTTSVoiceCustomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ttsvoice_custom(
        self,
        request: ling_mou_20250527_models.CreateTTSVoiceCustomRequest,
    ) -> ling_mou_20250527_models.CreateTTSVoiceCustomResponse:
        """
        @summary 创建TTS音色
        
        @param request: CreateTTSVoiceCustomRequest
        @return: CreateTTSVoiceCustomResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ttsvoice_custom_with_options(request, headers, runtime)

    async def create_ttsvoice_custom_async(
        self,
        request: ling_mou_20250527_models.CreateTTSVoiceCustomRequest,
    ) -> ling_mou_20250527_models.CreateTTSVoiceCustomResponse:
        """
        @summary 创建TTS音色
        
        @param request: CreateTTSVoiceCustomRequest
        @return: CreateTTSVoiceCustomResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_ttsvoice_custom_with_options_async(request, headers, runtime)

    def create_train_pic_avatar_with_options(
        self,
        request: ling_mou_20250527_models.CreateTrainPicAvatarRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.CreateTrainPicAvatarResponse:
        """
        @summary 创建图片训练数字人
        
        @param request: CreateTrainPicAvatarRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTrainPicAvatarResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gender):
            query['gender'] = request.gender
        if not UtilClient.is_unset(request.generate_assets):
            query['generateAssets'] = request.generate_assets
        if not UtilClient.is_unset(request.image_oss_path):
            query['imageOssPath'] = request.image_oss_path
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.template_id):
            query['templateId'] = request.template_id
        if not UtilClient.is_unset(request.transparent):
            query['transparent'] = request.transparent
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTrainPicAvatar',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/train/createTrainPicAvatar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.CreateTrainPicAvatarResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_train_pic_avatar_with_options_async(
        self,
        request: ling_mou_20250527_models.CreateTrainPicAvatarRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.CreateTrainPicAvatarResponse:
        """
        @summary 创建图片训练数字人
        
        @param request: CreateTrainPicAvatarRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTrainPicAvatarResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gender):
            query['gender'] = request.gender
        if not UtilClient.is_unset(request.generate_assets):
            query['generateAssets'] = request.generate_assets
        if not UtilClient.is_unset(request.image_oss_path):
            query['imageOssPath'] = request.image_oss_path
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.template_id):
            query['templateId'] = request.template_id
        if not UtilClient.is_unset(request.transparent):
            query['transparent'] = request.transparent
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTrainPicAvatar',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/train/createTrainPicAvatar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.CreateTrainPicAvatarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_train_pic_avatar(
        self,
        request: ling_mou_20250527_models.CreateTrainPicAvatarRequest,
    ) -> ling_mou_20250527_models.CreateTrainPicAvatarResponse:
        """
        @summary 创建图片训练数字人
        
        @param request: CreateTrainPicAvatarRequest
        @return: CreateTrainPicAvatarResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_train_pic_avatar_with_options(request, headers, runtime)

    async def create_train_pic_avatar_async(
        self,
        request: ling_mou_20250527_models.CreateTrainPicAvatarRequest,
    ) -> ling_mou_20250527_models.CreateTrainPicAvatarResponse:
        """
        @summary 创建图片训练数字人
        
        @param request: CreateTrainPicAvatarRequest
        @return: CreateTrainPicAvatarResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_train_pic_avatar_with_options_async(request, headers, runtime)

    def get_train_pic_avatar_status_with_options(
        self,
        request: ling_mou_20250527_models.GetTrainPicAvatarStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.GetTrainPicAvatarStatusResponse:
        """
        @summary 查询图片训练数字人的状态
        
        @param request: GetTrainPicAvatarStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTrainPicAvatarStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.avatar_id):
            query['avatarId'] = request.avatar_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrainPicAvatarStatus',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/train/getTrainPicAvatarStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.GetTrainPicAvatarStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_train_pic_avatar_status_with_options_async(
        self,
        request: ling_mou_20250527_models.GetTrainPicAvatarStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.GetTrainPicAvatarStatusResponse:
        """
        @summary 查询图片训练数字人的状态
        
        @param request: GetTrainPicAvatarStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTrainPicAvatarStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.avatar_id):
            query['avatarId'] = request.avatar_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrainPicAvatarStatus',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/train/getTrainPicAvatarStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.GetTrainPicAvatarStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_train_pic_avatar_status(
        self,
        request: ling_mou_20250527_models.GetTrainPicAvatarStatusRequest,
    ) -> ling_mou_20250527_models.GetTrainPicAvatarStatusResponse:
        """
        @summary 查询图片训练数字人的状态
        
        @param request: GetTrainPicAvatarStatusRequest
        @return: GetTrainPicAvatarStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_train_pic_avatar_status_with_options(request, headers, runtime)

    async def get_train_pic_avatar_status_async(
        self,
        request: ling_mou_20250527_models.GetTrainPicAvatarStatusRequest,
    ) -> ling_mou_20250527_models.GetTrainPicAvatarStatusResponse:
        """
        @summary 查询图片训练数字人的状态
        
        @param request: GetTrainPicAvatarStatusRequest
        @return: GetTrainPicAvatarStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_train_pic_avatar_status_with_options_async(request, headers, runtime)

    def get_upload_policy_with_options(
        self,
        request: ling_mou_20250527_models.GetUploadPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.GetUploadPolicyResponse:
        """
        @summary 获取对话免训图片素材上传凭证
        
        @param request: GetUploadPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUploadPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['jwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUploadPolicy',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/chat/getUploadPolicy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.GetUploadPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_upload_policy_with_options_async(
        self,
        request: ling_mou_20250527_models.GetUploadPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.GetUploadPolicyResponse:
        """
        @summary 获取对话免训图片素材上传凭证
        
        @param request: GetUploadPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUploadPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['jwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUploadPolicy',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/chat/getUploadPolicy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.GetUploadPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_upload_policy(
        self,
        request: ling_mou_20250527_models.GetUploadPolicyRequest,
    ) -> ling_mou_20250527_models.GetUploadPolicyResponse:
        """
        @summary 获取对话免训图片素材上传凭证
        
        @param request: GetUploadPolicyRequest
        @return: GetUploadPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_upload_policy_with_options(request, headers, runtime)

    async def get_upload_policy_async(
        self,
        request: ling_mou_20250527_models.GetUploadPolicyRequest,
    ) -> ling_mou_20250527_models.GetUploadPolicyResponse:
        """
        @summary 获取对话免训图片素材上传凭证
        
        @param request: GetUploadPolicyRequest
        @return: GetUploadPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_upload_policy_with_options_async(request, headers, runtime)

    def list_private_ttsvoices_custom_with_options(
        self,
        request: ling_mou_20250527_models.ListPrivateTTSVoicesCustomRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.ListPrivateTTSVoicesCustomResponse:
        """
        @summary 列举私有TTS音色
        
        @param request: ListPrivateTTSVoicesCustomRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrivateTTSVoicesCustomResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateTTSVoicesCustom',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/voice/listPrivateTTSVoicesCustom',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.ListPrivateTTSVoicesCustomResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_private_ttsvoices_custom_with_options_async(
        self,
        request: ling_mou_20250527_models.ListPrivateTTSVoicesCustomRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.ListPrivateTTSVoicesCustomResponse:
        """
        @summary 列举私有TTS音色
        
        @param request: ListPrivateTTSVoicesCustomRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrivateTTSVoicesCustomResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateTTSVoicesCustom',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/voice/listPrivateTTSVoicesCustom',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.ListPrivateTTSVoicesCustomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_private_ttsvoices_custom(
        self,
        request: ling_mou_20250527_models.ListPrivateTTSVoicesCustomRequest,
    ) -> ling_mou_20250527_models.ListPrivateTTSVoicesCustomResponse:
        """
        @summary 列举私有TTS音色
        
        @param request: ListPrivateTTSVoicesCustomRequest
        @return: ListPrivateTTSVoicesCustomResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_private_ttsvoices_custom_with_options(request, headers, runtime)

    async def list_private_ttsvoices_custom_async(
        self,
        request: ling_mou_20250527_models.ListPrivateTTSVoicesCustomRequest,
    ) -> ling_mou_20250527_models.ListPrivateTTSVoicesCustomResponse:
        """
        @summary 列举私有TTS音色
        
        @param request: ListPrivateTTSVoicesCustomRequest
        @return: ListPrivateTTSVoicesCustomResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_private_ttsvoices_custom_with_options_async(request, headers, runtime)

    def list_template_material_with_options(
        self,
        request: ling_mou_20250527_models.ListTemplateMaterialRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.ListTemplateMaterialResponse:
        """
        @summary 查询底板素材
        
        @param request: ListTemplateMaterialRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTemplateMaterialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.template_ids):
            query['templateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplateMaterial',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/train/listTemplateMaterial',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.ListTemplateMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_template_material_with_options_async(
        self,
        request: ling_mou_20250527_models.ListTemplateMaterialRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.ListTemplateMaterialResponse:
        """
        @summary 查询底板素材
        
        @param request: ListTemplateMaterialRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTemplateMaterialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.template_ids):
            query['templateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplateMaterial',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/train/listTemplateMaterial',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.ListTemplateMaterialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_template_material(
        self,
        request: ling_mou_20250527_models.ListTemplateMaterialRequest,
    ) -> ling_mou_20250527_models.ListTemplateMaterialResponse:
        """
        @summary 查询底板素材
        
        @param request: ListTemplateMaterialRequest
        @return: ListTemplateMaterialResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_template_material_with_options(request, headers, runtime)

    async def list_template_material_async(
        self,
        request: ling_mou_20250527_models.ListTemplateMaterialRequest,
    ) -> ling_mou_20250527_models.ListTemplateMaterialResponse:
        """
        @summary 查询底板素材
        
        @param request: ListTemplateMaterialRequest
        @return: ListTemplateMaterialResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_template_material_with_options_async(request, headers, runtime)

    def query_chat_instance_sessions_with_options(
        self,
        instance_id: str,
        tmp_req: ling_mou_20250527_models.QueryChatInstanceSessionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.QueryChatInstanceSessionsResponse:
        """
        @summary 查询会话实例session
        
        @param tmp_req: QueryChatInstanceSessionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryChatInstanceSessionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ling_mou_20250527_models.QueryChatInstanceSessionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.session_ids):
            request.session_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.session_ids, 'sessionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.session_ids_shrink):
            query['sessionIds'] = request.session_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryChatInstanceSessions',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/chat/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sessions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.QueryChatInstanceSessionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_chat_instance_sessions_with_options_async(
        self,
        instance_id: str,
        tmp_req: ling_mou_20250527_models.QueryChatInstanceSessionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ling_mou_20250527_models.QueryChatInstanceSessionsResponse:
        """
        @summary 查询会话实例session
        
        @param tmp_req: QueryChatInstanceSessionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryChatInstanceSessionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ling_mou_20250527_models.QueryChatInstanceSessionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.session_ids):
            request.session_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.session_ids, 'sessionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.session_ids_shrink):
            query['sessionIds'] = request.session_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryChatInstanceSessions',
            version='2025-05-27',
            protocol='HTTPS',
            pathname=f'/openapi/chat/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sessions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ling_mou_20250527_models.QueryChatInstanceSessionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_chat_instance_sessions(
        self,
        instance_id: str,
        request: ling_mou_20250527_models.QueryChatInstanceSessionsRequest,
    ) -> ling_mou_20250527_models.QueryChatInstanceSessionsResponse:
        """
        @summary 查询会话实例session
        
        @param request: QueryChatInstanceSessionsRequest
        @return: QueryChatInstanceSessionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_chat_instance_sessions_with_options(instance_id, request, headers, runtime)

    async def query_chat_instance_sessions_async(
        self,
        instance_id: str,
        request: ling_mou_20250527_models.QueryChatInstanceSessionsRequest,
    ) -> ling_mou_20250527_models.QueryChatInstanceSessionsResponse:
        """
        @summary 查询会话实例session
        
        @param request: QueryChatInstanceSessionsRequest
        @return: QueryChatInstanceSessionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_chat_instance_sessions_with_options_async(instance_id, request, headers, runtime)
