# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_contactcenterai20240603 import models as main_models
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
        self._endpoint = self.get_endpoint('contactcenterai', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def analyze_audio_sync_with_sse(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.AnalyzeAudioSyncRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.AnalyzeAudioSyncResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_tags):
            body['categoryTags'] = request.category_tags
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.model_code):
            body['modelCode'] = request.model_code
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        if not DaraCore.is_null(request.result_types):
            body['resultTypes'] = request.result_types
        if not DaraCore.is_null(request.service_inspection):
            body['serviceInspection'] = request.service_inspection
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.template_ids):
            body['templateIds'] = request.template_ids
        if not DaraCore.is_null(request.transcription):
            body['transcription'] = request.transcription
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AnalyzeAudioSync',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/analyzeAudioSync',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.AnalyzeAudioSyncResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def analyze_audio_sync_with_sse_async(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.AnalyzeAudioSyncRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.AnalyzeAudioSyncResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_tags):
            body['categoryTags'] = request.category_tags
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.model_code):
            body['modelCode'] = request.model_code
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        if not DaraCore.is_null(request.result_types):
            body['resultTypes'] = request.result_types
        if not DaraCore.is_null(request.service_inspection):
            body['serviceInspection'] = request.service_inspection
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.template_ids):
            body['templateIds'] = request.template_ids
        if not DaraCore.is_null(request.transcription):
            body['transcription'] = request.transcription
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AnalyzeAudioSync',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/analyzeAudioSync',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.AnalyzeAudioSyncResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def analyze_audio_sync_with_options(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.AnalyzeAudioSyncRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AnalyzeAudioSyncResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_tags):
            body['categoryTags'] = request.category_tags
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.model_code):
            body['modelCode'] = request.model_code
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        if not DaraCore.is_null(request.result_types):
            body['resultTypes'] = request.result_types
        if not DaraCore.is_null(request.service_inspection):
            body['serviceInspection'] = request.service_inspection
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.template_ids):
            body['templateIds'] = request.template_ids
        if not DaraCore.is_null(request.transcription):
            body['transcription'] = request.transcription
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AnalyzeAudioSync',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/analyzeAudioSync',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AnalyzeAudioSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def analyze_audio_sync_with_options_async(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.AnalyzeAudioSyncRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AnalyzeAudioSyncResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_tags):
            body['categoryTags'] = request.category_tags
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.model_code):
            body['modelCode'] = request.model_code
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        if not DaraCore.is_null(request.result_types):
            body['resultTypes'] = request.result_types
        if not DaraCore.is_null(request.service_inspection):
            body['serviceInspection'] = request.service_inspection
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.template_ids):
            body['templateIds'] = request.template_ids
        if not DaraCore.is_null(request.transcription):
            body['transcription'] = request.transcription
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AnalyzeAudioSync',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/analyzeAudioSync',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AnalyzeAudioSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def analyze_audio_sync(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.AnalyzeAudioSyncRequest,
    ) -> main_models.AnalyzeAudioSyncResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.analyze_audio_sync_with_options(workspace_id, app_id, request, headers, runtime)

    async def analyze_audio_sync_async(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.AnalyzeAudioSyncRequest,
    ) -> main_models.AnalyzeAudioSyncResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.analyze_audio_sync_with_options_async(workspace_id, app_id, request, headers, runtime)

    def analyze_conversation_with_sse(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.AnalyzeConversationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.AnalyzeConversationResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_tags):
            body['categoryTags'] = request.category_tags
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.dialogue):
            body['dialogue'] = request.dialogue
        if not DaraCore.is_null(request.examples):
            body['examples'] = request.examples
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.model_code):
            body['modelCode'] = request.model_code
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        if not DaraCore.is_null(request.result_types):
            body['resultTypes'] = request.result_types
        if not DaraCore.is_null(request.scene_name):
            body['sceneName'] = request.scene_name
        if not DaraCore.is_null(request.service_inspection):
            body['serviceInspection'] = request.service_inspection
        if not DaraCore.is_null(request.source_caller_uid):
            body['sourceCallerUid'] = request.source_caller_uid
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.time_constraint_list):
            body['timeConstraintList'] = request.time_constraint_list
        if not DaraCore.is_null(request.user_profiles):
            body['userProfiles'] = request.user_profiles
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AnalyzeConversation',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/analyze_conversation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.AnalyzeConversationResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def analyze_conversation_with_sse_async(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.AnalyzeConversationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.AnalyzeConversationResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_tags):
            body['categoryTags'] = request.category_tags
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.dialogue):
            body['dialogue'] = request.dialogue
        if not DaraCore.is_null(request.examples):
            body['examples'] = request.examples
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.model_code):
            body['modelCode'] = request.model_code
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        if not DaraCore.is_null(request.result_types):
            body['resultTypes'] = request.result_types
        if not DaraCore.is_null(request.scene_name):
            body['sceneName'] = request.scene_name
        if not DaraCore.is_null(request.service_inspection):
            body['serviceInspection'] = request.service_inspection
        if not DaraCore.is_null(request.source_caller_uid):
            body['sourceCallerUid'] = request.source_caller_uid
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.time_constraint_list):
            body['timeConstraintList'] = request.time_constraint_list
        if not DaraCore.is_null(request.user_profiles):
            body['userProfiles'] = request.user_profiles
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AnalyzeConversation',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/analyze_conversation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.AnalyzeConversationResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def analyze_conversation_with_options(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.AnalyzeConversationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AnalyzeConversationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_tags):
            body['categoryTags'] = request.category_tags
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.dialogue):
            body['dialogue'] = request.dialogue
        if not DaraCore.is_null(request.examples):
            body['examples'] = request.examples
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.model_code):
            body['modelCode'] = request.model_code
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        if not DaraCore.is_null(request.result_types):
            body['resultTypes'] = request.result_types
        if not DaraCore.is_null(request.scene_name):
            body['sceneName'] = request.scene_name
        if not DaraCore.is_null(request.service_inspection):
            body['serviceInspection'] = request.service_inspection
        if not DaraCore.is_null(request.source_caller_uid):
            body['sourceCallerUid'] = request.source_caller_uid
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.time_constraint_list):
            body['timeConstraintList'] = request.time_constraint_list
        if not DaraCore.is_null(request.user_profiles):
            body['userProfiles'] = request.user_profiles
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AnalyzeConversation',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/analyze_conversation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AnalyzeConversationResponse(),
            self.call_api(params, req, runtime)
        )

    async def analyze_conversation_with_options_async(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.AnalyzeConversationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AnalyzeConversationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_tags):
            body['categoryTags'] = request.category_tags
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.dialogue):
            body['dialogue'] = request.dialogue
        if not DaraCore.is_null(request.examples):
            body['examples'] = request.examples
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.model_code):
            body['modelCode'] = request.model_code
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        if not DaraCore.is_null(request.result_types):
            body['resultTypes'] = request.result_types
        if not DaraCore.is_null(request.scene_name):
            body['sceneName'] = request.scene_name
        if not DaraCore.is_null(request.service_inspection):
            body['serviceInspection'] = request.service_inspection
        if not DaraCore.is_null(request.source_caller_uid):
            body['sourceCallerUid'] = request.source_caller_uid
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.time_constraint_list):
            body['timeConstraintList'] = request.time_constraint_list
        if not DaraCore.is_null(request.user_profiles):
            body['userProfiles'] = request.user_profiles
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AnalyzeConversation',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/analyze_conversation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AnalyzeConversationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def analyze_conversation(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.AnalyzeConversationRequest,
    ) -> main_models.AnalyzeConversationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.analyze_conversation_with_options(workspace_id, app_id, request, headers, runtime)

    async def analyze_conversation_async(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.AnalyzeConversationRequest,
    ) -> main_models.AnalyzeConversationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.analyze_conversation_with_options_async(workspace_id, app_id, request, headers, runtime)

    def analyze_image_with_sse(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.AnalyzeImageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.AnalyzeImageResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_urls):
            body['imageUrls'] = request.image_urls
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        if not DaraCore.is_null(request.result_types):
            body['resultTypes'] = request.result_types
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AnalyzeImage',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/analyzeImage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.AnalyzeImageResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def analyze_image_with_sse_async(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.AnalyzeImageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.AnalyzeImageResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_urls):
            body['imageUrls'] = request.image_urls
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        if not DaraCore.is_null(request.result_types):
            body['resultTypes'] = request.result_types
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AnalyzeImage',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/analyzeImage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.AnalyzeImageResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def analyze_image_with_options(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.AnalyzeImageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AnalyzeImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_urls):
            body['imageUrls'] = request.image_urls
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        if not DaraCore.is_null(request.result_types):
            body['resultTypes'] = request.result_types
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AnalyzeImage',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/analyzeImage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AnalyzeImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def analyze_image_with_options_async(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.AnalyzeImageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AnalyzeImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_urls):
            body['imageUrls'] = request.image_urls
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        if not DaraCore.is_null(request.result_types):
            body['resultTypes'] = request.result_types
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AnalyzeImage',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/analyzeImage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AnalyzeImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def analyze_image(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.AnalyzeImageRequest,
    ) -> main_models.AnalyzeImageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.analyze_image_with_options(workspace_id, app_id, request, headers, runtime)

    async def analyze_image_async(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.AnalyzeImageRequest,
    ) -> main_models.AnalyzeImageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.analyze_image_with_options_async(workspace_id, app_id, request, headers, runtime)

    def create_task_with_options(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.call_back_url):
            body['callBackUrl'] = request.call_back_url
        if not DaraCore.is_null(request.category_tags):
            body['categoryTags'] = request.category_tags
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.dialogue):
            body['dialogue'] = request.dialogue
        if not DaraCore.is_null(request.examples):
            body['examples'] = request.examples
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.model_code):
            body['modelCode'] = request.model_code
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        if not DaraCore.is_null(request.result_types):
            body['resultTypes'] = request.result_types
        if not DaraCore.is_null(request.service_inspection):
            body['serviceInspection'] = request.service_inspection
        if not DaraCore.is_null(request.task_type):
            body['taskType'] = request.task_type
        if not DaraCore.is_null(request.template_ids):
            body['templateIds'] = request.template_ids
        if not DaraCore.is_null(request.transcription):
            body['transcription'] = request.transcription
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTask',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/createTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_with_options_async(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.call_back_url):
            body['callBackUrl'] = request.call_back_url
        if not DaraCore.is_null(request.category_tags):
            body['categoryTags'] = request.category_tags
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.dialogue):
            body['dialogue'] = request.dialogue
        if not DaraCore.is_null(request.examples):
            body['examples'] = request.examples
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.model_code):
            body['modelCode'] = request.model_code
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        if not DaraCore.is_null(request.result_types):
            body['resultTypes'] = request.result_types
        if not DaraCore.is_null(request.service_inspection):
            body['serviceInspection'] = request.service_inspection
        if not DaraCore.is_null(request.task_type):
            body['taskType'] = request.task_type
        if not DaraCore.is_null(request.template_ids):
            body['templateIds'] = request.template_ids
        if not DaraCore.is_null(request.transcription):
            body['transcription'] = request.transcription
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTask',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/createTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.CreateTaskRequest,
    ) -> main_models.CreateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_task_with_options(workspace_id, app_id, request, headers, runtime)

    async def create_task_async(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.CreateTaskRequest,
    ) -> main_models.CreateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_task_with_options_async(workspace_id, app_id, request, headers, runtime)

    def create_vocab_with_options(
        self,
        request: main_models.CreateVocabRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVocabResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.audio_model_code):
            body['audioModelCode'] = request.audio_model_code
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.word_weight_list):
            body['wordWeightList'] = request.word_weight_list
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVocab',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/vocab/createVocab',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVocabResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vocab_with_options_async(
        self,
        request: main_models.CreateVocabRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVocabResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.audio_model_code):
            body['audioModelCode'] = request.audio_model_code
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.word_weight_list):
            body['wordWeightList'] = request.word_weight_list
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVocab',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/vocab/createVocab',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVocabResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vocab(
        self,
        request: main_models.CreateVocabRequest,
    ) -> main_models.CreateVocabResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_vocab_with_options(request, headers, runtime)

    async def create_vocab_async(
        self,
        request: main_models.CreateVocabRequest,
    ) -> main_models.CreateVocabResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_vocab_with_options_async(request, headers, runtime)

    def delete_vocab_with_options(
        self,
        request: main_models.DeleteVocabRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVocabResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.vocabulary_id):
            body['vocabularyId'] = request.vocabulary_id
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVocab',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/vocab/deleteVocab',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVocabResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vocab_with_options_async(
        self,
        request: main_models.DeleteVocabRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVocabResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.vocabulary_id):
            body['vocabularyId'] = request.vocabulary_id
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVocab',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/vocab/deleteVocab',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVocabResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vocab(
        self,
        request: main_models.DeleteVocabRequest,
    ) -> main_models.DeleteVocabResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_vocab_with_options(request, headers, runtime)

    async def delete_vocab_async(
        self,
        request: main_models.DeleteVocabRequest,
    ) -> main_models.DeleteVocabResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_vocab_with_options_async(request, headers, runtime)

    def general_analyze_image_with_sse(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.GeneralAnalyzeImageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.GeneralAnalyzeImageResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.image_urls):
            body['imageUrls'] = request.image_urls
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.template_ids):
            body['templateIds'] = request.template_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GeneralAnalyzeImage',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/generalanalyzeImage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.GeneralAnalyzeImageResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def general_analyze_image_with_sse_async(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.GeneralAnalyzeImageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.GeneralAnalyzeImageResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.image_urls):
            body['imageUrls'] = request.image_urls
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.template_ids):
            body['templateIds'] = request.template_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GeneralAnalyzeImage',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/generalanalyzeImage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.GeneralAnalyzeImageResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def general_analyze_image_with_options(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.GeneralAnalyzeImageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GeneralAnalyzeImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.image_urls):
            body['imageUrls'] = request.image_urls
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.template_ids):
            body['templateIds'] = request.template_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GeneralAnalyzeImage',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/generalanalyzeImage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GeneralAnalyzeImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def general_analyze_image_with_options_async(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.GeneralAnalyzeImageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GeneralAnalyzeImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.custom_prompt):
            body['customPrompt'] = request.custom_prompt
        if not DaraCore.is_null(request.image_urls):
            body['imageUrls'] = request.image_urls
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        if not DaraCore.is_null(request.template_ids):
            body['templateIds'] = request.template_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GeneralAnalyzeImage',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/generalanalyzeImage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GeneralAnalyzeImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def general_analyze_image(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.GeneralAnalyzeImageRequest,
    ) -> main_models.GeneralAnalyzeImageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.general_analyze_image_with_options(workspace_id, app_id, request, headers, runtime)

    async def general_analyze_image_async(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.GeneralAnalyzeImageRequest,
    ) -> main_models.GeneralAnalyzeImageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.general_analyze_image_with_options_async(workspace_id, app_id, request, headers, runtime)

    def get_task_result_with_options(
        self,
        tmp_req: main_models.GetTaskResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskResultResponse:
        tmp_req.validate()
        request = main_models.GetTaskResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.required_field_list):
            request.required_field_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.required_field_list, 'requiredFieldList', 'simple')
        query = {}
        if not DaraCore.is_null(request.required_field_list_shrink):
            query['requiredFieldList'] = request.required_field_list_shrink
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskResult',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/ccai/app/getTaskResult',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_result_with_options_async(
        self,
        tmp_req: main_models.GetTaskResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskResultResponse:
        tmp_req.validate()
        request = main_models.GetTaskResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.required_field_list):
            request.required_field_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.required_field_list, 'requiredFieldList', 'simple')
        query = {}
        if not DaraCore.is_null(request.required_field_list_shrink):
            query['requiredFieldList'] = request.required_field_list_shrink
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskResult',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/ccai/app/getTaskResult',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_result(
        self,
        request: main_models.GetTaskResultRequest,
    ) -> main_models.GetTaskResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_task_result_with_options(request, headers, runtime)

    async def get_task_result_async(
        self,
        request: main_models.GetTaskResultRequest,
    ) -> main_models.GetTaskResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_task_result_with_options_async(request, headers, runtime)

    def get_vocab_with_options(
        self,
        request: main_models.GetVocabRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVocabResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.vocabulary_id):
            body['vocabularyId'] = request.vocabulary_id
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVocab',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/vocab/getVocab',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVocabResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vocab_with_options_async(
        self,
        request: main_models.GetVocabRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVocabResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.vocabulary_id):
            body['vocabularyId'] = request.vocabulary_id
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVocab',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/vocab/getVocab',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVocabResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vocab(
        self,
        request: main_models.GetVocabRequest,
    ) -> main_models.GetVocabResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_vocab_with_options(request, headers, runtime)

    async def get_vocab_async(
        self,
        request: main_models.GetVocabRequest,
    ) -> main_models.GetVocabResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_vocab_with_options_async(request, headers, runtime)

    def list_vocab_with_options(
        self,
        request: main_models.ListVocabRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVocabResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVocab',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/vocab/listVocab',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVocabResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vocab_with_options_async(
        self,
        request: main_models.ListVocabRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVocabResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVocab',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/vocab/listVocab',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVocabResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vocab(
        self,
        request: main_models.ListVocabRequest,
    ) -> main_models.ListVocabResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_vocab_with_options(request, headers, runtime)

    async def list_vocab_async(
        self,
        request: main_models.ListVocabRequest,
    ) -> main_models.ListVocabResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_vocab_with_options_async(request, headers, runtime)

    def run_completion_with_sse(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.RunCompletionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunCompletionResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dialogue):
            body['Dialogue'] = request.dialogue
        if not DaraCore.is_null(request.fields):
            body['Fields'] = request.fields
        if not DaraCore.is_null(request.model_code):
            body['ModelCode'] = request.model_code
        if not DaraCore.is_null(request.service_inspection):
            body['ServiceInspection'] = request.service_inspection
        if not DaraCore.is_null(request.stream):
            body['Stream'] = request.stream
        if not DaraCore.is_null(request.template_ids):
            body['TemplateIds'] = request.template_ids
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCompletion',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/completion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.RunCompletionResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def run_completion_with_sse_async(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.RunCompletionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunCompletionResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dialogue):
            body['Dialogue'] = request.dialogue
        if not DaraCore.is_null(request.fields):
            body['Fields'] = request.fields
        if not DaraCore.is_null(request.model_code):
            body['ModelCode'] = request.model_code
        if not DaraCore.is_null(request.service_inspection):
            body['ServiceInspection'] = request.service_inspection
        if not DaraCore.is_null(request.stream):
            body['Stream'] = request.stream
        if not DaraCore.is_null(request.template_ids):
            body['TemplateIds'] = request.template_ids
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCompletion',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/completion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.RunCompletionResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def run_completion_with_options(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.RunCompletionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunCompletionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dialogue):
            body['Dialogue'] = request.dialogue
        if not DaraCore.is_null(request.fields):
            body['Fields'] = request.fields
        if not DaraCore.is_null(request.model_code):
            body['ModelCode'] = request.model_code
        if not DaraCore.is_null(request.service_inspection):
            body['ServiceInspection'] = request.service_inspection
        if not DaraCore.is_null(request.stream):
            body['Stream'] = request.stream
        if not DaraCore.is_null(request.template_ids):
            body['TemplateIds'] = request.template_ids
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCompletion',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/completion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunCompletionResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_completion_with_options_async(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.RunCompletionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunCompletionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dialogue):
            body['Dialogue'] = request.dialogue
        if not DaraCore.is_null(request.fields):
            body['Fields'] = request.fields
        if not DaraCore.is_null(request.model_code):
            body['ModelCode'] = request.model_code
        if not DaraCore.is_null(request.service_inspection):
            body['ServiceInspection'] = request.service_inspection
        if not DaraCore.is_null(request.stream):
            body['Stream'] = request.stream
        if not DaraCore.is_null(request.template_ids):
            body['TemplateIds'] = request.template_ids
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCompletion',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/completion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunCompletionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_completion(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.RunCompletionRequest,
    ) -> main_models.RunCompletionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_completion_with_options(workspace_id, app_id, request, headers, runtime)

    async def run_completion_async(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.RunCompletionRequest,
    ) -> main_models.RunCompletionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_completion_with_options_async(workspace_id, app_id, request, headers, runtime)

    def run_completion_message_with_sse(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.RunCompletionMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunCompletionMessageResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.messages):
            body['Messages'] = request.messages
        if not DaraCore.is_null(request.model_code):
            body['ModelCode'] = request.model_code
        if not DaraCore.is_null(request.stream):
            body['Stream'] = request.stream
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCompletionMessage',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/completion_message',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.RunCompletionMessageResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def run_completion_message_with_sse_async(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.RunCompletionMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunCompletionMessageResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.messages):
            body['Messages'] = request.messages
        if not DaraCore.is_null(request.model_code):
            body['ModelCode'] = request.model_code
        if not DaraCore.is_null(request.stream):
            body['Stream'] = request.stream
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCompletionMessage',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/completion_message',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.RunCompletionMessageResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def run_completion_message_with_options(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.RunCompletionMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunCompletionMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.messages):
            body['Messages'] = request.messages
        if not DaraCore.is_null(request.model_code):
            body['ModelCode'] = request.model_code
        if not DaraCore.is_null(request.stream):
            body['Stream'] = request.stream
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCompletionMessage',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/completion_message',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunCompletionMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_completion_message_with_options_async(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.RunCompletionMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunCompletionMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.messages):
            body['Messages'] = request.messages
        if not DaraCore.is_null(request.model_code):
            body['ModelCode'] = request.model_code
        if not DaraCore.is_null(request.stream):
            body['Stream'] = request.stream
        if not DaraCore.is_null(request.response_format_type):
            body['responseFormatType'] = request.response_format_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCompletionMessage',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/ccai/app/{DaraURL.percent_encode(app_id)}/completion_message',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunCompletionMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_completion_message(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.RunCompletionMessageRequest,
    ) -> main_models.RunCompletionMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_completion_message_with_options(workspace_id, app_id, request, headers, runtime)

    async def run_completion_message_async(
        self,
        workspace_id: str,
        app_id: str,
        request: main_models.RunCompletionMessageRequest,
    ) -> main_models.RunCompletionMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_completion_message_with_options_async(workspace_id, app_id, request, headers, runtime)

    def update_vocab_with_options(
        self,
        request: main_models.UpdateVocabRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVocabResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.vocabulary_id):
            body['vocabularyId'] = request.vocabulary_id
        if not DaraCore.is_null(request.word_weight_list):
            body['wordWeightList'] = request.word_weight_list
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVocab',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/vocab/updateVocab',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVocabResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vocab_with_options_async(
        self,
        request: main_models.UpdateVocabRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVocabResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.vocabulary_id):
            body['vocabularyId'] = request.vocabulary_id
        if not DaraCore.is_null(request.word_weight_list):
            body['wordWeightList'] = request.word_weight_list
        if not DaraCore.is_null(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVocab',
            version = '2024-06-03',
            protocol = 'HTTPS',
            pathname = f'/vocab/updateVocab',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVocabResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vocab(
        self,
        request: main_models.UpdateVocabRequest,
    ) -> main_models.UpdateVocabResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_vocab_with_options(request, headers, runtime)

    async def update_vocab_async(
        self,
        request: main_models.UpdateVocabRequest,
    ) -> main_models.UpdateVocabResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_vocab_with_options_async(request, headers, runtime)
