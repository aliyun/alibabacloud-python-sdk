# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_bailianmodelonchip20240816 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('bailianmodelonchip', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def active_interaction_create_with_options(
        self,
        request: main_models.ActiveInteractionCreateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ActiveInteractionCreateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image):
            body['image'] = request.image
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ActiveInteractionCreate',
            version = '2024-08-16',
            protocol = 'HTTPS',
            pathname = f'/open/api/v1/active/interaction/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActiveInteractionCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def active_interaction_create_with_options_async(
        self,
        request: main_models.ActiveInteractionCreateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ActiveInteractionCreateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image):
            body['image'] = request.image
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ActiveInteractionCreate',
            version = '2024-08-16',
            protocol = 'HTTPS',
            pathname = f'/open/api/v1/active/interaction/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActiveInteractionCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def active_interaction_create(
        self,
        request: main_models.ActiveInteractionCreateRequest,
    ) -> main_models.ActiveInteractionCreateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.active_interaction_create_with_options(request, headers, runtime)

    async def active_interaction_create_async(
        self,
        request: main_models.ActiveInteractionCreateRequest,
    ) -> main_models.ActiveInteractionCreateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.active_interaction_create_with_options_async(request, headers, runtime)

    def active_interaction_eu_create_with_options(
        self,
        request: main_models.ActiveInteractionEuCreateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ActiveInteractionEuCreateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image):
            body['image'] = request.image
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ActiveInteractionEuCreate',
            version = '2024-08-16',
            protocol = 'HTTPS',
            pathname = f'/open/api/eu/active/interaction/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActiveInteractionEuCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def active_interaction_eu_create_with_options_async(
        self,
        request: main_models.ActiveInteractionEuCreateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ActiveInteractionEuCreateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image):
            body['image'] = request.image
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ActiveInteractionEuCreate',
            version = '2024-08-16',
            protocol = 'HTTPS',
            pathname = f'/open/api/eu/active/interaction/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActiveInteractionEuCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def active_interaction_eu_create(
        self,
        request: main_models.ActiveInteractionEuCreateRequest,
    ) -> main_models.ActiveInteractionEuCreateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.active_interaction_eu_create_with_options(request, headers, runtime)

    async def active_interaction_eu_create_async(
        self,
        request: main_models.ActiveInteractionEuCreateRequest,
    ) -> main_models.ActiveInteractionEuCreateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.active_interaction_eu_create_with_options_async(request, headers, runtime)

    def device_register_with_options(
        self,
        request: main_models.DeviceRegisterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeviceRegisterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.nonce):
            body['nonce'] = request.nonce
        if not DaraCore.is_null(request.request_time):
            body['requestTime'] = request.request_time
        if not DaraCore.is_null(request.signature):
            body['signature'] = request.signature
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeviceRegister',
            version = '2024-08-16',
            protocol = 'HTTPS',
            pathname = f'/open/api/device/v1/register',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeviceRegisterResponse(),
            self.call_api(params, req, runtime)
        )

    async def device_register_with_options_async(
        self,
        request: main_models.DeviceRegisterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeviceRegisterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.nonce):
            body['nonce'] = request.nonce
        if not DaraCore.is_null(request.request_time):
            body['requestTime'] = request.request_time
        if not DaraCore.is_null(request.signature):
            body['signature'] = request.signature
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeviceRegister',
            version = '2024-08-16',
            protocol = 'HTTPS',
            pathname = f'/open/api/device/v1/register',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeviceRegisterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def device_register(
        self,
        request: main_models.DeviceRegisterRequest,
    ) -> main_models.DeviceRegisterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.device_register_with_options(request, headers, runtime)

    async def device_register_async(
        self,
        request: main_models.DeviceRegisterRequest,
    ) -> main_models.DeviceRegisterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.device_register_with_options_async(request, headers, runtime)

    def get_pass_through_auth_info_with_options(
        self,
        request: main_models.GetPassThroughAuthInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPassThroughAuthInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.device_name):
            body['deviceName'] = request.device_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPassThroughAuthInfo',
            version = '2024-08-16',
            protocol = 'HTTPS',
            pathname = f'/open/api/auth/v1/token/getPassThroughAuthInfo',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPassThroughAuthInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pass_through_auth_info_with_options_async(
        self,
        request: main_models.GetPassThroughAuthInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPassThroughAuthInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.device_name):
            body['deviceName'] = request.device_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPassThroughAuthInfo',
            version = '2024-08-16',
            protocol = 'HTTPS',
            pathname = f'/open/api/auth/v1/token/getPassThroughAuthInfo',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPassThroughAuthInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pass_through_auth_info(
        self,
        request: main_models.GetPassThroughAuthInfoRequest,
    ) -> main_models.GetPassThroughAuthInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pass_through_auth_info_with_options(request, headers, runtime)

    async def get_pass_through_auth_info_async(
        self,
        request: main_models.GetPassThroughAuthInfoRequest,
    ) -> main_models.GetPassThroughAuthInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pass_through_auth_info_with_options_async(request, headers, runtime)

    def get_token_with_options(
        self,
        request: main_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.device_name):
            body['deviceName'] = request.device_name
        if not DaraCore.is_null(request.nonce):
            body['nonce'] = request.nonce
        if not DaraCore.is_null(request.request_time):
            body['requestTime'] = request.request_time
        if not DaraCore.is_null(request.signature):
            body['signature'] = request.signature
        if not DaraCore.is_null(request.token_key):
            body['tokenKey'] = request.token_key
        if not DaraCore.is_null(request.token_type):
            body['tokenType'] = request.token_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetToken',
            version = '2024-08-16',
            protocol = 'HTTPS',
            pathname = f'/open/api/auth/v1/token/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_with_options_async(
        self,
        request: main_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.device_name):
            body['deviceName'] = request.device_name
        if not DaraCore.is_null(request.nonce):
            body['nonce'] = request.nonce
        if not DaraCore.is_null(request.request_time):
            body['requestTime'] = request.request_time
        if not DaraCore.is_null(request.signature):
            body['signature'] = request.signature
        if not DaraCore.is_null(request.token_key):
            body['tokenKey'] = request.token_key
        if not DaraCore.is_null(request.token_type):
            body['tokenType'] = request.token_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetToken',
            version = '2024-08-16',
            protocol = 'HTTPS',
            pathname = f'/open/api/auth/v1/token/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token(
        self,
        request: main_models.GetTokenRequest,
    ) -> main_models.GetTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_token_with_options(request, headers, runtime)

    async def get_token_async(
        self,
        request: main_models.GetTokenRequest,
    ) -> main_models.GetTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_token_with_options_async(request, headers, runtime)

    def model_type_determine_with_options(
        self,
        tmp_req: main_models.ModelTypeDetermineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelTypeDetermineResponse:
        tmp_req.validate()
        request = main_models.ModelTypeDetermineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.history):
            request.history_shrink = Utils.array_to_string_with_specified_style(tmp_req.history, 'history', 'json')
        body = {}
        if not DaraCore.is_null(request.history_shrink):
            body['history'] = request.history_shrink
        if not DaraCore.is_null(request.input_text):
            body['inputText'] = request.input_text
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModelTypeDetermine',
            version = '2024-08-16',
            protocol = 'HTTPS',
            pathname = f'/open/api/v1/model/type/determine',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelTypeDetermineResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_type_determine_with_options_async(
        self,
        tmp_req: main_models.ModelTypeDetermineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelTypeDetermineResponse:
        tmp_req.validate()
        request = main_models.ModelTypeDetermineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.history):
            request.history_shrink = Utils.array_to_string_with_specified_style(tmp_req.history, 'history', 'json')
        body = {}
        if not DaraCore.is_null(request.history_shrink):
            body['history'] = request.history_shrink
        if not DaraCore.is_null(request.input_text):
            body['inputText'] = request.input_text
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModelTypeDetermine',
            version = '2024-08-16',
            protocol = 'HTTPS',
            pathname = f'/open/api/v1/model/type/determine',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelTypeDetermineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_type_determine(
        self,
        request: main_models.ModelTypeDetermineRequest,
    ) -> main_models.ModelTypeDetermineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_type_determine_with_options(request, headers, runtime)

    async def model_type_determine_async(
        self,
        request: main_models.ModelTypeDetermineRequest,
    ) -> main_models.ModelTypeDetermineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_type_determine_with_options_async(request, headers, runtime)

    def omni_realtime_conversation_euwith_options(
        self,
        request: main_models.OmniRealtimeConversationEURequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OmniRealtimeConversationEUResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.input_audio):
            body['inputAudio'] = request.input_audio
        if not DaraCore.is_null(request.user_prompt):
            body['userPrompt'] = request.user_prompt
        if not DaraCore.is_null(request.voice):
            body['voice'] = request.voice
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OmniRealtimeConversationEU',
            version = '2024-08-16',
            protocol = 'HTTPS',
            pathname = f'/open/api/eu/active/interaction/audio',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OmniRealtimeConversationEUResponse(),
            self.call_api(params, req, runtime)
        )

    async def omni_realtime_conversation_euwith_options_async(
        self,
        request: main_models.OmniRealtimeConversationEURequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OmniRealtimeConversationEUResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.input_audio):
            body['inputAudio'] = request.input_audio
        if not DaraCore.is_null(request.user_prompt):
            body['userPrompt'] = request.user_prompt
        if not DaraCore.is_null(request.voice):
            body['voice'] = request.voice
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OmniRealtimeConversationEU',
            version = '2024-08-16',
            protocol = 'HTTPS',
            pathname = f'/open/api/eu/active/interaction/audio',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OmniRealtimeConversationEUResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def omni_realtime_conversation_eu(
        self,
        request: main_models.OmniRealtimeConversationEURequest,
    ) -> main_models.OmniRealtimeConversationEUResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.omni_realtime_conversation_euwith_options(request, headers, runtime)

    async def omni_realtime_conversation_eu_async(
        self,
        request: main_models.OmniRealtimeConversationEURequest,
    ) -> main_models.OmniRealtimeConversationEUResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.omni_realtime_conversation_euwith_options_async(request, headers, runtime)
