# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_lingmou20250527 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def close_chat_instance_sessions_with_options(
        self,
        instance_id: str,
        tmp_req: main_models.CloseChatInstanceSessionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloseChatInstanceSessionsResponse:
        tmp_req.validate()
        request = main_models.CloseChatInstanceSessionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.session_ids):
            request.session_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.session_ids, 'sessionIds', 'json')
        body = {}
        if not DaraCore.is_null(request.session_ids_shrink):
            body['sessionIds'] = request.session_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloseChatInstanceSessions',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/chat/instances/{DaraURL.percent_encode(instance_id)}/sessions/close',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseChatInstanceSessionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_chat_instance_sessions_with_options_async(
        self,
        instance_id: str,
        tmp_req: main_models.CloseChatInstanceSessionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloseChatInstanceSessionsResponse:
        tmp_req.validate()
        request = main_models.CloseChatInstanceSessionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.session_ids):
            request.session_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.session_ids, 'sessionIds', 'json')
        body = {}
        if not DaraCore.is_null(request.session_ids_shrink):
            body['sessionIds'] = request.session_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloseChatInstanceSessions',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/chat/instances/{DaraURL.percent_encode(instance_id)}/sessions/close',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseChatInstanceSessionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_chat_instance_sessions(
        self,
        instance_id: str,
        request: main_models.CloseChatInstanceSessionsRequest,
    ) -> main_models.CloseChatInstanceSessionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.close_chat_instance_sessions_with_options(instance_id, request, headers, runtime)

    async def close_chat_instance_sessions_async(
        self,
        instance_id: str,
        request: main_models.CloseChatInstanceSessionsRequest,
    ) -> main_models.CloseChatInstanceSessionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.close_chat_instance_sessions_with_options_async(instance_id, request, headers, runtime)

    def confirm_train_pic_avatar_with_options(
        self,
        request: main_models.ConfirmTrainPicAvatarRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ConfirmTrainPicAvatarResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.avatar_id):
            query['avatarId'] = request.avatar_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfirmTrainPicAvatar',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/train/confirmTrainPicAvatar',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfirmTrainPicAvatarResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_train_pic_avatar_with_options_async(
        self,
        request: main_models.ConfirmTrainPicAvatarRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ConfirmTrainPicAvatarResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.avatar_id):
            query['avatarId'] = request.avatar_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfirmTrainPicAvatar',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/train/confirmTrainPicAvatar',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfirmTrainPicAvatarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_train_pic_avatar(
        self,
        request: main_models.ConfirmTrainPicAvatarRequest,
    ) -> main_models.ConfirmTrainPicAvatarResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.confirm_train_pic_avatar_with_options(request, headers, runtime)

    async def confirm_train_pic_avatar_async(
        self,
        request: main_models.ConfirmTrainPicAvatarRequest,
    ) -> main_models.ConfirmTrainPicAvatarResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.confirm_train_pic_avatar_with_options_async(request, headers, runtime)

    def create_background_pic_with_options(
        self,
        request: main_models.CreateBackgroundPicRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackgroundPicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filename):
            query['filename'] = request.filename
        if not DaraCore.is_null(request.oss_key):
            query['ossKey'] = request.oss_key
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackgroundPic',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/chat/createBackgroundPic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackgroundPicResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_background_pic_with_options_async(
        self,
        request: main_models.CreateBackgroundPicRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackgroundPicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filename):
            query['filename'] = request.filename
        if not DaraCore.is_null(request.oss_key):
            query['ossKey'] = request.oss_key
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackgroundPic',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/chat/createBackgroundPic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackgroundPicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_background_pic(
        self,
        request: main_models.CreateBackgroundPicRequest,
    ) -> main_models.CreateBackgroundPicResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_background_pic_with_options(request, headers, runtime)

    async def create_background_pic_async(
        self,
        request: main_models.CreateBackgroundPicRequest,
    ) -> main_models.CreateBackgroundPicResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_background_pic_with_options_async(request, headers, runtime)

    def create_broadcast_sticker_with_options(
        self,
        request: main_models.CreateBroadcastStickerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateBroadcastStickerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_name):
            body['fileName'] = request.file_name
        if not DaraCore.is_null(request.oss_key):
            body['ossKey'] = request.oss_key
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBroadcastSticker',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/customer/broadcast/material/sticker/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBroadcastStickerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_broadcast_sticker_with_options_async(
        self,
        request: main_models.CreateBroadcastStickerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateBroadcastStickerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_name):
            body['fileName'] = request.file_name
        if not DaraCore.is_null(request.oss_key):
            body['ossKey'] = request.oss_key
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBroadcastSticker',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/customer/broadcast/material/sticker/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBroadcastStickerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_broadcast_sticker(
        self,
        request: main_models.CreateBroadcastStickerRequest,
    ) -> main_models.CreateBroadcastStickerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_broadcast_sticker_with_options(request, headers, runtime)

    async def create_broadcast_sticker_async(
        self,
        request: main_models.CreateBroadcastStickerRequest,
    ) -> main_models.CreateBroadcastStickerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_broadcast_sticker_with_options_async(request, headers, runtime)

    def create_broadcast_video_from_template_with_options(
        self,
        request: main_models.CreateBroadcastVideoFromTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateBroadcastVideoFromTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.template_id):
            body['templateId'] = request.template_id
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        if not DaraCore.is_null(request.video_options):
            body['videoOptions'] = request.video_options
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBroadcastVideoFromTemplate',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/api/v1/amp/customer/broadcast/video/createFromTemplate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBroadcastVideoFromTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_broadcast_video_from_template_with_options_async(
        self,
        request: main_models.CreateBroadcastVideoFromTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateBroadcastVideoFromTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.template_id):
            body['templateId'] = request.template_id
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        if not DaraCore.is_null(request.video_options):
            body['videoOptions'] = request.video_options
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBroadcastVideoFromTemplate',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/api/v1/amp/customer/broadcast/video/createFromTemplate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBroadcastVideoFromTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_broadcast_video_from_template(
        self,
        request: main_models.CreateBroadcastVideoFromTemplateRequest,
    ) -> main_models.CreateBroadcastVideoFromTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_broadcast_video_from_template_with_options(request, headers, runtime)

    async def create_broadcast_video_from_template_async(
        self,
        request: main_models.CreateBroadcastVideoFromTemplateRequest,
    ) -> main_models.CreateBroadcastVideoFromTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_broadcast_video_from_template_with_options_async(request, headers, runtime)

    def create_chat_config_with_options(
        self,
        request: main_models.CreateChatConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.avatar_id):
            query['avatarId'] = request.avatar_id
        if not DaraCore.is_null(request.background_id):
            query['backgroundId'] = request.background_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateChatConfig',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/chat/createChatConfig',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chat_config_with_options_async(
        self,
        request: main_models.CreateChatConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.avatar_id):
            query['avatarId'] = request.avatar_id
        if not DaraCore.is_null(request.background_id):
            query['backgroundId'] = request.background_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateChatConfig',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/chat/createChatConfig',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chat_config(
        self,
        request: main_models.CreateChatConfigRequest,
    ) -> main_models.CreateChatConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_chat_config_with_options(request, headers, runtime)

    async def create_chat_config_async(
        self,
        request: main_models.CreateChatConfigRequest,
    ) -> main_models.CreateChatConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_chat_config_with_options_async(request, headers, runtime)

    def create_chat_session_with_options(
        self,
        id: str,
        request: main_models.CreateChatSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.license):
            query['license'] = request.license
        if not DaraCore.is_null(request.platform):
            query['platform'] = request.platform
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateChatSession',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/chat/init/{DaraURL.percent_encode(id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chat_session_with_options_async(
        self,
        id: str,
        request: main_models.CreateChatSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.license):
            query['license'] = request.license
        if not DaraCore.is_null(request.platform):
            query['platform'] = request.platform
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateChatSession',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/chat/init/{DaraURL.percent_encode(id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chat_session(
        self,
        id: str,
        request: main_models.CreateChatSessionRequest,
    ) -> main_models.CreateChatSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_chat_session_with_options(id, request, headers, runtime)

    async def create_chat_session_async(
        self,
        id: str,
        request: main_models.CreateChatSessionRequest,
    ) -> main_models.CreateChatSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_chat_session_with_options_async(id, request, headers, runtime)

    def create_no_train_pic_avatar_with_options(
        self,
        request: main_models.CreateNoTrainPicAvatarRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateNoTrainPicAvatarResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expressiveness):
            query['expressiveness'] = request.expressiveness
        if not DaraCore.is_null(request.gender):
            query['gender'] = request.gender
        if not DaraCore.is_null(request.generate_assets):
            query['generateAssets'] = request.generate_assets
        if not DaraCore.is_null(request.image_oss_path):
            query['imageOssPath'] = request.image_oss_path
        if not DaraCore.is_null(request.jwt_token):
            query['jwtToken'] = request.jwt_token
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.transparent):
            query['transparent'] = request.transparent
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNoTrainPicAvatar',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/chat/createNoTrainPicAvatar',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNoTrainPicAvatarResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_no_train_pic_avatar_with_options_async(
        self,
        request: main_models.CreateNoTrainPicAvatarRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateNoTrainPicAvatarResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expressiveness):
            query['expressiveness'] = request.expressiveness
        if not DaraCore.is_null(request.gender):
            query['gender'] = request.gender
        if not DaraCore.is_null(request.generate_assets):
            query['generateAssets'] = request.generate_assets
        if not DaraCore.is_null(request.image_oss_path):
            query['imageOssPath'] = request.image_oss_path
        if not DaraCore.is_null(request.jwt_token):
            query['jwtToken'] = request.jwt_token
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.transparent):
            query['transparent'] = request.transparent
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNoTrainPicAvatar',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/chat/createNoTrainPicAvatar',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNoTrainPicAvatarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_no_train_pic_avatar(
        self,
        request: main_models.CreateNoTrainPicAvatarRequest,
    ) -> main_models.CreateNoTrainPicAvatarResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_no_train_pic_avatar_with_options(request, headers, runtime)

    async def create_no_train_pic_avatar_async(
        self,
        request: main_models.CreateNoTrainPicAvatarRequest,
    ) -> main_models.CreateNoTrainPicAvatarResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_no_train_pic_avatar_with_options_async(request, headers, runtime)

    def create_ttsvoice_custom_with_options(
        self,
        request: main_models.CreateTTSVoiceCustomRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTTSVoiceCustomResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['fileName'] = request.file_name
        if not DaraCore.is_null(request.gender):
            query['gender'] = request.gender
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.oss_key):
            query['ossKey'] = request.oss_key
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTTSVoiceCustom',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/voice/createTTSVoiceCustom',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTTSVoiceCustomResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ttsvoice_custom_with_options_async(
        self,
        request: main_models.CreateTTSVoiceCustomRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTTSVoiceCustomResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['fileName'] = request.file_name
        if not DaraCore.is_null(request.gender):
            query['gender'] = request.gender
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.oss_key):
            query['ossKey'] = request.oss_key
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTTSVoiceCustom',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/voice/createTTSVoiceCustom',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTTSVoiceCustomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ttsvoice_custom(
        self,
        request: main_models.CreateTTSVoiceCustomRequest,
    ) -> main_models.CreateTTSVoiceCustomResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_ttsvoice_custom_with_options(request, headers, runtime)

    async def create_ttsvoice_custom_async(
        self,
        request: main_models.CreateTTSVoiceCustomRequest,
    ) -> main_models.CreateTTSVoiceCustomResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_ttsvoice_custom_with_options_async(request, headers, runtime)

    def create_train_pic_avatar_with_options(
        self,
        request: main_models.CreateTrainPicAvatarRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTrainPicAvatarResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gender):
            query['gender'] = request.gender
        if not DaraCore.is_null(request.generate_assets):
            query['generateAssets'] = request.generate_assets
        if not DaraCore.is_null(request.image_oss_path):
            query['imageOssPath'] = request.image_oss_path
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.template_id):
            query['templateId'] = request.template_id
        if not DaraCore.is_null(request.transparent):
            query['transparent'] = request.transparent
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrainPicAvatar',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/train/createTrainPicAvatar',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTrainPicAvatarResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_train_pic_avatar_with_options_async(
        self,
        request: main_models.CreateTrainPicAvatarRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTrainPicAvatarResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gender):
            query['gender'] = request.gender
        if not DaraCore.is_null(request.generate_assets):
            query['generateAssets'] = request.generate_assets
        if not DaraCore.is_null(request.image_oss_path):
            query['imageOssPath'] = request.image_oss_path
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.template_id):
            query['templateId'] = request.template_id
        if not DaraCore.is_null(request.transparent):
            query['transparent'] = request.transparent
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrainPicAvatar',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/train/createTrainPicAvatar',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTrainPicAvatarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_train_pic_avatar(
        self,
        request: main_models.CreateTrainPicAvatarRequest,
    ) -> main_models.CreateTrainPicAvatarResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_train_pic_avatar_with_options(request, headers, runtime)

    async def create_train_pic_avatar_async(
        self,
        request: main_models.CreateTrainPicAvatarRequest,
    ) -> main_models.CreateTrainPicAvatarResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_train_pic_avatar_with_options_async(request, headers, runtime)

    def get_broadcast_template_with_options(
        self,
        request: main_models.GetBroadcastTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBroadcastTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBroadcastTemplate',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/customer/broadcast/template/detail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBroadcastTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_broadcast_template_with_options_async(
        self,
        request: main_models.GetBroadcastTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBroadcastTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBroadcastTemplate',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/customer/broadcast/template/detail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBroadcastTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_broadcast_template(
        self,
        request: main_models.GetBroadcastTemplateRequest,
    ) -> main_models.GetBroadcastTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_broadcast_template_with_options(request, headers, runtime)

    async def get_broadcast_template_async(
        self,
        request: main_models.GetBroadcastTemplateRequest,
    ) -> main_models.GetBroadcastTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_broadcast_template_with_options_async(request, headers, runtime)

    def get_ttsvoice_by_id_custom_with_options(
        self,
        request: main_models.GetTTSVoiceByIdCustomRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTTSVoiceByIdCustomResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.voice_id):
            query['voiceId'] = request.voice_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTTSVoiceByIdCustom',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/voice/getTTSVoiceById',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTTSVoiceByIdCustomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ttsvoice_by_id_custom_with_options_async(
        self,
        request: main_models.GetTTSVoiceByIdCustomRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTTSVoiceByIdCustomResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.voice_id):
            query['voiceId'] = request.voice_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTTSVoiceByIdCustom',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/voice/getTTSVoiceById',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTTSVoiceByIdCustomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ttsvoice_by_id_custom(
        self,
        request: main_models.GetTTSVoiceByIdCustomRequest,
    ) -> main_models.GetTTSVoiceByIdCustomResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_ttsvoice_by_id_custom_with_options(request, headers, runtime)

    async def get_ttsvoice_by_id_custom_async(
        self,
        request: main_models.GetTTSVoiceByIdCustomRequest,
    ) -> main_models.GetTTSVoiceByIdCustomResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_ttsvoice_by_id_custom_with_options_async(request, headers, runtime)

    def get_train_pic_avatar_status_with_options(
        self,
        request: main_models.GetTrainPicAvatarStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTrainPicAvatarStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.avatar_id):
            query['avatarId'] = request.avatar_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrainPicAvatarStatus',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/train/getTrainPicAvatarStatus',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrainPicAvatarStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_train_pic_avatar_status_with_options_async(
        self,
        request: main_models.GetTrainPicAvatarStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTrainPicAvatarStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.avatar_id):
            query['avatarId'] = request.avatar_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrainPicAvatarStatus',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/train/getTrainPicAvatarStatus',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrainPicAvatarStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_train_pic_avatar_status(
        self,
        request: main_models.GetTrainPicAvatarStatusRequest,
    ) -> main_models.GetTrainPicAvatarStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_train_pic_avatar_status_with_options(request, headers, runtime)

    async def get_train_pic_avatar_status_async(
        self,
        request: main_models.GetTrainPicAvatarStatusRequest,
    ) -> main_models.GetTrainPicAvatarStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_train_pic_avatar_status_with_options_async(request, headers, runtime)

    def get_upload_policy_with_options(
        self,
        request: main_models.GetUploadPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUploadPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.jwt_token):
            query['jwtToken'] = request.jwt_token
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUploadPolicy',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/chat/getUploadPolicy',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUploadPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_upload_policy_with_options_async(
        self,
        request: main_models.GetUploadPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUploadPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.jwt_token):
            query['jwtToken'] = request.jwt_token
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUploadPolicy',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/chat/getUploadPolicy',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUploadPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_upload_policy(
        self,
        request: main_models.GetUploadPolicyRequest,
    ) -> main_models.GetUploadPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_upload_policy_with_options(request, headers, runtime)

    async def get_upload_policy_async(
        self,
        request: main_models.GetUploadPolicyRequest,
    ) -> main_models.GetUploadPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_upload_policy_with_options_async(request, headers, runtime)

    def list_broadcast_templates_with_options(
        self,
        request: main_models.ListBroadcastTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListBroadcastTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBroadcastTemplates',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/customer/broadcast/template/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBroadcastTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_broadcast_templates_with_options_async(
        self,
        request: main_models.ListBroadcastTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListBroadcastTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBroadcastTemplates',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/customer/broadcast/template/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBroadcastTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_broadcast_templates(
        self,
        request: main_models.ListBroadcastTemplatesRequest,
    ) -> main_models.ListBroadcastTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_broadcast_templates_with_options(request, headers, runtime)

    async def list_broadcast_templates_async(
        self,
        request: main_models.ListBroadcastTemplatesRequest,
    ) -> main_models.ListBroadcastTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_broadcast_templates_with_options_async(request, headers, runtime)

    def list_broadcast_videos_by_id_with_options(
        self,
        tmp_req: main_models.ListBroadcastVideosByIdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListBroadcastVideosByIdResponse:
        tmp_req.validate()
        request = main_models.ListBroadcastVideosByIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.video_ids):
            request.video_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_ids, 'videoIds', 'json')
        query = {}
        if not DaraCore.is_null(request.video_ids_shrink):
            query['videoIds'] = request.video_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBroadcastVideosById',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/api/v1/amp/customer/broadcast/video/batchQuery',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBroadcastVideosByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_broadcast_videos_by_id_with_options_async(
        self,
        tmp_req: main_models.ListBroadcastVideosByIdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListBroadcastVideosByIdResponse:
        tmp_req.validate()
        request = main_models.ListBroadcastVideosByIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.video_ids):
            request.video_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_ids, 'videoIds', 'json')
        query = {}
        if not DaraCore.is_null(request.video_ids_shrink):
            query['videoIds'] = request.video_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBroadcastVideosById',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/api/v1/amp/customer/broadcast/video/batchQuery',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBroadcastVideosByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_broadcast_videos_by_id(
        self,
        request: main_models.ListBroadcastVideosByIdRequest,
    ) -> main_models.ListBroadcastVideosByIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_broadcast_videos_by_id_with_options(request, headers, runtime)

    async def list_broadcast_videos_by_id_async(
        self,
        request: main_models.ListBroadcastVideosByIdRequest,
    ) -> main_models.ListBroadcastVideosByIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_broadcast_videos_by_id_with_options_async(request, headers, runtime)

    def list_private_ttsvoices_custom_with_options(
        self,
        request: main_models.ListPrivateTTSVoicesCustomRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPrivateTTSVoicesCustomResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrivateTTSVoicesCustom',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/voice/listPrivateTTSVoicesCustom',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrivateTTSVoicesCustomResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_private_ttsvoices_custom_with_options_async(
        self,
        request: main_models.ListPrivateTTSVoicesCustomRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPrivateTTSVoicesCustomResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrivateTTSVoicesCustom',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/voice/listPrivateTTSVoicesCustom',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrivateTTSVoicesCustomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_private_ttsvoices_custom(
        self,
        request: main_models.ListPrivateTTSVoicesCustomRequest,
    ) -> main_models.ListPrivateTTSVoicesCustomResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_private_ttsvoices_custom_with_options(request, headers, runtime)

    async def list_private_ttsvoices_custom_async(
        self,
        request: main_models.ListPrivateTTSVoicesCustomRequest,
    ) -> main_models.ListPrivateTTSVoicesCustomResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_private_ttsvoices_custom_with_options_async(request, headers, runtime)

    def list_template_material_with_options(
        self,
        request: main_models.ListTemplateMaterialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplateMaterialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.template_ids):
            query['templateIds'] = request.template_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplateMaterial',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/train/listTemplateMaterial',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplateMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_template_material_with_options_async(
        self,
        request: main_models.ListTemplateMaterialRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplateMaterialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.template_ids):
            query['templateIds'] = request.template_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplateMaterial',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/train/listTemplateMaterial',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplateMaterialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_template_material(
        self,
        request: main_models.ListTemplateMaterialRequest,
    ) -> main_models.ListTemplateMaterialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_template_material_with_options(request, headers, runtime)

    async def list_template_material_async(
        self,
        request: main_models.ListTemplateMaterialRequest,
    ) -> main_models.ListTemplateMaterialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_template_material_with_options_async(request, headers, runtime)

    def query_chat_instance_sessions_with_options(
        self,
        instance_id: str,
        tmp_req: main_models.QueryChatInstanceSessionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryChatInstanceSessionsResponse:
        tmp_req.validate()
        request = main_models.QueryChatInstanceSessionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.session_ids):
            request.session_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.session_ids, 'sessionIds', 'json')
        query = {}
        if not DaraCore.is_null(request.session_ids_shrink):
            query['sessionIds'] = request.session_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryChatInstanceSessions',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/chat/instances/{DaraURL.percent_encode(instance_id)}/sessions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryChatInstanceSessionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_chat_instance_sessions_with_options_async(
        self,
        instance_id: str,
        tmp_req: main_models.QueryChatInstanceSessionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryChatInstanceSessionsResponse:
        tmp_req.validate()
        request = main_models.QueryChatInstanceSessionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.session_ids):
            request.session_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.session_ids, 'sessionIds', 'json')
        query = {}
        if not DaraCore.is_null(request.session_ids_shrink):
            query['sessionIds'] = request.session_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryChatInstanceSessions',
            version = '2025-05-27',
            protocol = 'HTTPS',
            pathname = f'/openapi/chat/instances/{DaraURL.percent_encode(instance_id)}/sessions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryChatInstanceSessionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_chat_instance_sessions(
        self,
        instance_id: str,
        request: main_models.QueryChatInstanceSessionsRequest,
    ) -> main_models.QueryChatInstanceSessionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_chat_instance_sessions_with_options(instance_id, request, headers, runtime)

    async def query_chat_instance_sessions_async(
        self,
        instance_id: str,
        request: main_models.QueryChatInstanceSessionsRequest,
    ) -> main_models.QueryChatInstanceSessionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_chat_instance_sessions_with_options_async(instance_id, request, headers, runtime)
