# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_voicenavigator20180612 import models as main_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('voicenavigator', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def associate_chatbot_instance_with_options(
        self,
        request: main_models.AssociateChatbotInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateChatbotInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chatbot_instance_id):
            query['ChatbotInstanceId'] = request.chatbot_instance_id
        if not DaraCore.is_null(request.chatbot_name):
            query['ChatbotName'] = request.chatbot_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nlu_service_params_json):
            query['NluServiceParamsJson'] = request.nlu_service_params_json
        if not DaraCore.is_null(request.nlu_service_type):
            query['NluServiceType'] = request.nlu_service_type
        if not DaraCore.is_null(request.union_source):
            query['UnionSource'] = request.union_source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateChatbotInstance',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateChatbotInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_chatbot_instance_with_options_async(
        self,
        request: main_models.AssociateChatbotInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateChatbotInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chatbot_instance_id):
            query['ChatbotInstanceId'] = request.chatbot_instance_id
        if not DaraCore.is_null(request.chatbot_name):
            query['ChatbotName'] = request.chatbot_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nlu_service_params_json):
            query['NluServiceParamsJson'] = request.nlu_service_params_json
        if not DaraCore.is_null(request.nlu_service_type):
            query['NluServiceType'] = request.nlu_service_type
        if not DaraCore.is_null(request.union_source):
            query['UnionSource'] = request.union_source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateChatbotInstance',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateChatbotInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_chatbot_instance(
        self,
        request: main_models.AssociateChatbotInstanceRequest,
    ) -> main_models.AssociateChatbotInstanceResponse:
        runtime = RuntimeOptions()
        return self.associate_chatbot_instance_with_options(request, runtime)

    async def associate_chatbot_instance_async(
        self,
        request: main_models.AssociateChatbotInstanceRequest,
    ) -> main_models.AssociateChatbotInstanceResponse:
        runtime = RuntimeOptions()
        return await self.associate_chatbot_instance_with_options_async(request, runtime)

    def audit_ttsvoice_with_options(
        self,
        request: main_models.AuditTTSVoiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuditTTSVoiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_key):
            query['AccessKey'] = request.access_key
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pitch_rate):
            query['PitchRate'] = request.pitch_rate
        if not DaraCore.is_null(request.secret_key):
            query['SecretKey'] = request.secret_key
        if not DaraCore.is_null(request.speech_rate):
            query['SpeechRate'] = request.speech_rate
        if not DaraCore.is_null(request.text):
            query['Text'] = request.text
        if not DaraCore.is_null(request.voice):
            query['Voice'] = request.voice
        if not DaraCore.is_null(request.volume):
            query['Volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuditTTSVoice',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuditTTSVoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def audit_ttsvoice_with_options_async(
        self,
        request: main_models.AuditTTSVoiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuditTTSVoiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_key):
            query['AccessKey'] = request.access_key
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pitch_rate):
            query['PitchRate'] = request.pitch_rate
        if not DaraCore.is_null(request.secret_key):
            query['SecretKey'] = request.secret_key
        if not DaraCore.is_null(request.speech_rate):
            query['SpeechRate'] = request.speech_rate
        if not DaraCore.is_null(request.text):
            query['Text'] = request.text
        if not DaraCore.is_null(request.voice):
            query['Voice'] = request.voice
        if not DaraCore.is_null(request.volume):
            query['Volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuditTTSVoice',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuditTTSVoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def audit_ttsvoice(
        self,
        request: main_models.AuditTTSVoiceRequest,
    ) -> main_models.AuditTTSVoiceResponse:
        runtime = RuntimeOptions()
        return self.audit_ttsvoice_with_options(request, runtime)

    async def audit_ttsvoice_async(
        self,
        request: main_models.AuditTTSVoiceRequest,
    ) -> main_models.AuditTTSVoiceResponse:
        runtime = RuntimeOptions()
        return await self.audit_ttsvoice_with_options_async(request, runtime)

    def begin_dialogue_with_options(
        self,
        request: main_models.BeginDialogueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BeginDialogueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.initial_context):
            query['InitialContext'] = request.initial_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BeginDialogue',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BeginDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def begin_dialogue_with_options_async(
        self,
        request: main_models.BeginDialogueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BeginDialogueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.initial_context):
            query['InitialContext'] = request.initial_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BeginDialogue',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BeginDialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def begin_dialogue(
        self,
        request: main_models.BeginDialogueRequest,
    ) -> main_models.BeginDialogueResponse:
        runtime = RuntimeOptions()
        return self.begin_dialogue_with_options(request, runtime)

    async def begin_dialogue_async(
        self,
        request: main_models.BeginDialogueRequest,
    ) -> main_models.BeginDialogueResponse:
        runtime = RuntimeOptions()
        return await self.begin_dialogue_with_options_async(request, runtime)

    def collected_number_with_options(
        self,
        request: main_models.CollectedNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CollectedNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.additional_context):
            query['AdditionalContext'] = request.additional_context
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CollectedNumber',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CollectedNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def collected_number_with_options_async(
        self,
        request: main_models.CollectedNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CollectedNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.additional_context):
            query['AdditionalContext'] = request.additional_context
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CollectedNumber',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CollectedNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def collected_number(
        self,
        request: main_models.CollectedNumberRequest,
    ) -> main_models.CollectedNumberResponse:
        runtime = RuntimeOptions()
        return self.collected_number_with_options(request, runtime)

    async def collected_number_async(
        self,
        request: main_models.CollectedNumberRequest,
    ) -> main_models.CollectedNumberResponse:
        runtime = RuntimeOptions()
        return await self.collected_number_with_options_async(request, runtime)

    def create_download_url_with_options(
        self,
        request: main_models.CreateDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDownloadUrlResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDownloadUrl',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_download_url_with_options_async(
        self,
        request: main_models.CreateDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDownloadUrlResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDownloadUrl',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_download_url(
        self,
        request: main_models.CreateDownloadUrlRequest,
    ) -> main_models.CreateDownloadUrlResponse:
        runtime = RuntimeOptions()
        return self.create_download_url_with_options(request, runtime)

    async def create_download_url_async(
        self,
        request: main_models.CreateDownloadUrlRequest,
    ) -> main_models.CreateDownloadUrlResponse:
        runtime = RuntimeOptions()
        return await self.create_download_url_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.concurrency):
            query['Concurrency'] = request.concurrency
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.nlu_service_params_json):
            query['NluServiceParamsJson'] = request.nlu_service_params_json
        if not DaraCore.is_null(request.union_instance_id):
            query['UnionInstanceId'] = request.union_instance_id
        if not DaraCore.is_null(request.union_source):
            query['UnionSource'] = request.union_source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.concurrency):
            query['Concurrency'] = request.concurrency
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.nlu_service_params_json):
            query['NluServiceParamsJson'] = request.nlu_service_params_json
        if not DaraCore.is_null(request.union_instance_id):
            query['UnionInstanceId'] = request.union_instance_id
        if not DaraCore.is_null(request.union_source):
            query['UnionSource'] = request.union_source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def debug_begin_dialogue_with_options(
        self,
        request: main_models.DebugBeginDialogueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DebugBeginDialogueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.initial_context):
            query['InitialContext'] = request.initial_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.should_use_sand_box):
            query['ShouldUseSandBox'] = request.should_use_sand_box
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DebugBeginDialogue',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DebugBeginDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def debug_begin_dialogue_with_options_async(
        self,
        request: main_models.DebugBeginDialogueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DebugBeginDialogueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.initial_context):
            query['InitialContext'] = request.initial_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.should_use_sand_box):
            query['ShouldUseSandBox'] = request.should_use_sand_box
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DebugBeginDialogue',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DebugBeginDialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def debug_begin_dialogue(
        self,
        request: main_models.DebugBeginDialogueRequest,
    ) -> main_models.DebugBeginDialogueResponse:
        runtime = RuntimeOptions()
        return self.debug_begin_dialogue_with_options(request, runtime)

    async def debug_begin_dialogue_async(
        self,
        request: main_models.DebugBeginDialogueRequest,
    ) -> main_models.DebugBeginDialogueResponse:
        runtime = RuntimeOptions()
        return await self.debug_begin_dialogue_with_options_async(request, runtime)

    def debug_collected_number_with_options(
        self,
        request: main_models.DebugCollectedNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DebugCollectedNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DebugCollectedNumber',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DebugCollectedNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def debug_collected_number_with_options_async(
        self,
        request: main_models.DebugCollectedNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DebugCollectedNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DebugCollectedNumber',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DebugCollectedNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def debug_collected_number(
        self,
        request: main_models.DebugCollectedNumberRequest,
    ) -> main_models.DebugCollectedNumberResponse:
        runtime = RuntimeOptions()
        return self.debug_collected_number_with_options(request, runtime)

    async def debug_collected_number_async(
        self,
        request: main_models.DebugCollectedNumberRequest,
    ) -> main_models.DebugCollectedNumberResponse:
        runtime = RuntimeOptions()
        return await self.debug_collected_number_with_options_async(request, runtime)

    def debug_dialogue_with_options(
        self,
        request: main_models.DebugDialogueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DebugDialogueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.additional_context):
            query['AdditionalContext'] = request.additional_context
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DebugDialogue',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DebugDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def debug_dialogue_with_options_async(
        self,
        request: main_models.DebugDialogueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DebugDialogueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.additional_context):
            query['AdditionalContext'] = request.additional_context
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DebugDialogue',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DebugDialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def debug_dialogue(
        self,
        request: main_models.DebugDialogueRequest,
    ) -> main_models.DebugDialogueResponse:
        runtime = RuntimeOptions()
        return self.debug_dialogue_with_options(request, runtime)

    async def debug_dialogue_async(
        self,
        request: main_models.DebugDialogueRequest,
    ) -> main_models.DebugDialogueResponse:
        runtime = RuntimeOptions()
        return await self.debug_dialogue_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def describe_conversation_with_options(
        self,
        request: main_models.DescribeConversationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConversationResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConversation',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConversationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_conversation_with_options_async(
        self,
        request: main_models.DescribeConversationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConversationResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConversation',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConversationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_conversation(
        self,
        request: main_models.DescribeConversationRequest,
    ) -> main_models.DescribeConversationResponse:
        runtime = RuntimeOptions()
        return self.describe_conversation_with_options(request, runtime)

    async def describe_conversation_async(
        self,
        request: main_models.DescribeConversationRequest,
    ) -> main_models.DescribeConversationResponse:
        runtime = RuntimeOptions()
        return await self.describe_conversation_with_options_async(request, runtime)

    def describe_conversation_context_with_options(
        self,
        request: main_models.DescribeConversationContextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConversationContextResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConversationContext',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConversationContextResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_conversation_context_with_options_async(
        self,
        request: main_models.DescribeConversationContextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConversationContextResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConversationContext',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConversationContextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_conversation_context(
        self,
        request: main_models.DescribeConversationContextRequest,
    ) -> main_models.DescribeConversationContextResponse:
        runtime = RuntimeOptions()
        return self.describe_conversation_context_with_options(request, runtime)

    async def describe_conversation_context_async(
        self,
        request: main_models.DescribeConversationContextRequest,
    ) -> main_models.DescribeConversationContextResponse:
        runtime = RuntimeOptions()
        return await self.describe_conversation_context_with_options_async(request, runtime)

    def describe_export_progress_with_options(
        self,
        request: main_models.DescribeExportProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExportProgressResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExportProgress',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExportProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_export_progress_with_options_async(
        self,
        request: main_models.DescribeExportProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExportProgressResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExportProgress',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExportProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_export_progress(
        self,
        request: main_models.DescribeExportProgressRequest,
    ) -> main_models.DescribeExportProgressResponse:
        runtime = RuntimeOptions()
        return self.describe_export_progress_with_options(request, runtime)

    async def describe_export_progress_async(
        self,
        request: main_models.DescribeExportProgressRequest,
    ) -> main_models.DescribeExportProgressResponse:
        runtime = RuntimeOptions()
        return await self.describe_export_progress_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: main_models.DescribeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstance',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: main_models.DescribeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstance',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        request: main_models.DescribeInstanceRequest,
    ) -> main_models.DescribeInstanceResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: main_models.DescribeInstanceRequest,
    ) -> main_models.DescribeInstanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_navigation_config_with_options(
        self,
        request: main_models.DescribeNavigationConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNavigationConfigResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNavigationConfig',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNavigationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_navigation_config_with_options_async(
        self,
        request: main_models.DescribeNavigationConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNavigationConfigResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNavigationConfig',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNavigationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_navigation_config(
        self,
        request: main_models.DescribeNavigationConfigRequest,
    ) -> main_models.DescribeNavigationConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_navigation_config_with_options(request, runtime)

    async def describe_navigation_config_async(
        self,
        request: main_models.DescribeNavigationConfigRequest,
    ) -> main_models.DescribeNavigationConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_navigation_config_with_options_async(request, runtime)

    def describe_recording_with_options(
        self,
        request: main_models.DescribeRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecordingResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecording',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_recording_with_options_async(
        self,
        request: main_models.DescribeRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecordingResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecording',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_recording(
        self,
        request: main_models.DescribeRecordingRequest,
    ) -> main_models.DescribeRecordingResponse:
        runtime = RuntimeOptions()
        return self.describe_recording_with_options(request, runtime)

    async def describe_recording_async(
        self,
        request: main_models.DescribeRecordingRequest,
    ) -> main_models.DescribeRecordingResponse:
        runtime = RuntimeOptions()
        return await self.describe_recording_with_options_async(request, runtime)

    def describe_statistical_data_with_options(
        self,
        request: main_models.DescribeStatisticalDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStatisticalDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStatisticalData',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStatisticalDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_statistical_data_with_options_async(
        self,
        request: main_models.DescribeStatisticalDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStatisticalDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStatisticalData',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStatisticalDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_statistical_data(
        self,
        request: main_models.DescribeStatisticalDataRequest,
    ) -> main_models.DescribeStatisticalDataResponse:
        runtime = RuntimeOptions()
        return self.describe_statistical_data_with_options(request, runtime)

    async def describe_statistical_data_async(
        self,
        request: main_models.DescribeStatisticalDataRequest,
    ) -> main_models.DescribeStatisticalDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_statistical_data_with_options_async(request, runtime)

    def describe_ttsconfig_with_options(
        self,
        request: main_models.DescribeTTSConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTTSConfigResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTTSConfig',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTTSConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ttsconfig_with_options_async(
        self,
        request: main_models.DescribeTTSConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTTSConfigResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTTSConfig',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTTSConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ttsconfig(
        self,
        request: main_models.DescribeTTSConfigRequest,
    ) -> main_models.DescribeTTSConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_ttsconfig_with_options(request, runtime)

    async def describe_ttsconfig_async(
        self,
        request: main_models.DescribeTTSConfigRequest,
    ) -> main_models.DescribeTTSConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_ttsconfig_with_options_async(request, runtime)

    def dialogue_with_options(
        self,
        request: main_models.DialogueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DialogueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.additional_context):
            query['AdditionalContext'] = request.additional_context
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.emotion):
            query['Emotion'] = request.emotion
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not DaraCore.is_null(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Dialogue',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def dialogue_with_options_async(
        self,
        request: main_models.DialogueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DialogueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.additional_context):
            query['AdditionalContext'] = request.additional_context
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.emotion):
            query['Emotion'] = request.emotion
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not DaraCore.is_null(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Dialogue',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dialogue(
        self,
        request: main_models.DialogueRequest,
    ) -> main_models.DialogueResponse:
        runtime = RuntimeOptions()
        return self.dialogue_with_options(request, runtime)

    async def dialogue_async(
        self,
        request: main_models.DialogueRequest,
    ) -> main_models.DialogueResponse:
        runtime = RuntimeOptions()
        return await self.dialogue_with_options_async(request, runtime)

    def disable_instance_with_options(
        self,
        request: main_models.DisableInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableInstance',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_instance_with_options_async(
        self,
        request: main_models.DisableInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableInstance',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_instance(
        self,
        request: main_models.DisableInstanceRequest,
    ) -> main_models.DisableInstanceResponse:
        runtime = RuntimeOptions()
        return self.disable_instance_with_options(request, runtime)

    async def disable_instance_async(
        self,
        request: main_models.DisableInstanceRequest,
    ) -> main_models.DisableInstanceResponse:
        runtime = RuntimeOptions()
        return await self.disable_instance_with_options_async(request, runtime)

    def enable_instance_with_options(
        self,
        request: main_models.EnableInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableInstance',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_instance_with_options_async(
        self,
        request: main_models.EnableInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableInstance',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_instance(
        self,
        request: main_models.EnableInstanceRequest,
    ) -> main_models.EnableInstanceResponse:
        runtime = RuntimeOptions()
        return self.enable_instance_with_options(request, runtime)

    async def enable_instance_async(
        self,
        request: main_models.EnableInstanceRequest,
    ) -> main_models.EnableInstanceResponse:
        runtime = RuntimeOptions()
        return await self.enable_instance_with_options_async(request, runtime)

    def end_dialogue_with_options(
        self,
        request: main_models.EndDialogueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EndDialogueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.hang_up_params):
            query['HangUpParams'] = request.hang_up_params
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EndDialogue',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EndDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def end_dialogue_with_options_async(
        self,
        request: main_models.EndDialogueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EndDialogueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.hang_up_params):
            query['HangUpParams'] = request.hang_up_params
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EndDialogue',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EndDialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def end_dialogue(
        self,
        request: main_models.EndDialogueRequest,
    ) -> main_models.EndDialogueResponse:
        runtime = RuntimeOptions()
        return self.end_dialogue_with_options(request, runtime)

    async def end_dialogue_async(
        self,
        request: main_models.EndDialogueRequest,
    ) -> main_models.EndDialogueResponse:
        runtime = RuntimeOptions()
        return await self.end_dialogue_with_options_async(request, runtime)

    def export_conversation_details_with_options(
        self,
        request: main_models.ExportConversationDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportConversationDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time_left_range):
            query['BeginTimeLeftRange'] = request.begin_time_left_range
        if not DaraCore.is_null(request.begin_time_right_range):
            query['BeginTimeRightRange'] = request.begin_time_right_range
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.debug_conversation):
            query['DebugConversation'] = request.debug_conversation
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.options):
            query['Options'] = request.options
        if not DaraCore.is_null(request.result):
            query['Result'] = request.result
        if not DaraCore.is_null(request.rounds_left_range):
            query['RoundsLeftRange'] = request.rounds_left_range
        if not DaraCore.is_null(request.rounds_right_range):
            query['RoundsRightRange'] = request.rounds_right_range
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportConversationDetails',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportConversationDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_conversation_details_with_options_async(
        self,
        request: main_models.ExportConversationDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportConversationDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time_left_range):
            query['BeginTimeLeftRange'] = request.begin_time_left_range
        if not DaraCore.is_null(request.begin_time_right_range):
            query['BeginTimeRightRange'] = request.begin_time_right_range
        if not DaraCore.is_null(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not DaraCore.is_null(request.debug_conversation):
            query['DebugConversation'] = request.debug_conversation
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.options):
            query['Options'] = request.options
        if not DaraCore.is_null(request.result):
            query['Result'] = request.result
        if not DaraCore.is_null(request.rounds_left_range):
            query['RoundsLeftRange'] = request.rounds_left_range
        if not DaraCore.is_null(request.rounds_right_range):
            query['RoundsRightRange'] = request.rounds_right_range
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportConversationDetails',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportConversationDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_conversation_details(
        self,
        request: main_models.ExportConversationDetailsRequest,
    ) -> main_models.ExportConversationDetailsResponse:
        runtime = RuntimeOptions()
        return self.export_conversation_details_with_options(request, runtime)

    async def export_conversation_details_async(
        self,
        request: main_models.ExportConversationDetailsRequest,
    ) -> main_models.ExportConversationDetailsResponse:
        runtime = RuntimeOptions()
        return await self.export_conversation_details_with_options_async(request, runtime)

    def export_statistical_data_with_options(
        self,
        request: main_models.ExportStatisticalDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportStatisticalDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time_left_range):
            query['BeginTimeLeftRange'] = request.begin_time_left_range
        if not DaraCore.is_null(request.begin_time_right_range):
            query['BeginTimeRightRange'] = request.begin_time_right_range
        if not DaraCore.is_null(request.export_type):
            query['ExportType'] = request.export_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.time_unit):
            query['TimeUnit'] = request.time_unit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportStatisticalData',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportStatisticalDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_statistical_data_with_options_async(
        self,
        request: main_models.ExportStatisticalDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportStatisticalDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time_left_range):
            query['BeginTimeLeftRange'] = request.begin_time_left_range
        if not DaraCore.is_null(request.begin_time_right_range):
            query['BeginTimeRightRange'] = request.begin_time_right_range
        if not DaraCore.is_null(request.export_type):
            query['ExportType'] = request.export_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.time_unit):
            query['TimeUnit'] = request.time_unit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportStatisticalData',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportStatisticalDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_statistical_data(
        self,
        request: main_models.ExportStatisticalDataRequest,
    ) -> main_models.ExportStatisticalDataResponse:
        runtime = RuntimeOptions()
        return self.export_statistical_data_with_options(request, runtime)

    async def export_statistical_data_async(
        self,
        request: main_models.ExportStatisticalDataRequest,
    ) -> main_models.ExportStatisticalDataResponse:
        runtime = RuntimeOptions()
        return await self.export_statistical_data_with_options_async(request, runtime)

    def get_asr_config_with_options(
        self,
        request: main_models.GetAsrConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAsrConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_level):
            query['ConfigLevel'] = request.config_level
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsrConfig',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsrConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_asr_config_with_options_async(
        self,
        request: main_models.GetAsrConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAsrConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_level):
            query['ConfigLevel'] = request.config_level
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsrConfig',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsrConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_asr_config(
        self,
        request: main_models.GetAsrConfigRequest,
    ) -> main_models.GetAsrConfigResponse:
        runtime = RuntimeOptions()
        return self.get_asr_config_with_options(request, runtime)

    async def get_asr_config_async(
        self,
        request: main_models.GetAsrConfigRequest,
    ) -> main_models.GetAsrConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_asr_config_with_options_async(request, runtime)

    def get_real_time_concurrency_with_options(
        self,
        request: main_models.GetRealTimeConcurrencyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRealTimeConcurrencyResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRealTimeConcurrency',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRealTimeConcurrencyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_real_time_concurrency_with_options_async(
        self,
        request: main_models.GetRealTimeConcurrencyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRealTimeConcurrencyResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRealTimeConcurrency',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRealTimeConcurrencyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_real_time_concurrency(
        self,
        request: main_models.GetRealTimeConcurrencyRequest,
    ) -> main_models.GetRealTimeConcurrencyResponse:
        runtime = RuntimeOptions()
        return self.get_real_time_concurrency_with_options(request, runtime)

    async def get_real_time_concurrency_async(
        self,
        request: main_models.GetRealTimeConcurrencyRequest,
    ) -> main_models.GetRealTimeConcurrencyResponse:
        runtime = RuntimeOptions()
        return await self.get_real_time_concurrency_with_options_async(request, runtime)

    def list_chatbot_instances_with_options(
        self,
        request: main_models.ListChatbotInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChatbotInstancesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChatbotInstances',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatbotInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chatbot_instances_with_options_async(
        self,
        request: main_models.ListChatbotInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChatbotInstancesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChatbotInstances',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatbotInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chatbot_instances(
        self,
        request: main_models.ListChatbotInstancesRequest,
    ) -> main_models.ListChatbotInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_chatbot_instances_with_options(request, runtime)

    async def list_chatbot_instances_async(
        self,
        request: main_models.ListChatbotInstancesRequest,
    ) -> main_models.ListChatbotInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_chatbot_instances_with_options_async(request, runtime)

    def list_conversation_details_with_options(
        self,
        request: main_models.ListConversationDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConversationDetailsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConversationDetails',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConversationDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_conversation_details_with_options_async(
        self,
        request: main_models.ListConversationDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConversationDetailsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConversationDetails',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConversationDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_conversation_details(
        self,
        request: main_models.ListConversationDetailsRequest,
    ) -> main_models.ListConversationDetailsResponse:
        runtime = RuntimeOptions()
        return self.list_conversation_details_with_options(request, runtime)

    async def list_conversation_details_async(
        self,
        request: main_models.ListConversationDetailsRequest,
    ) -> main_models.ListConversationDetailsResponse:
        runtime = RuntimeOptions()
        return await self.list_conversation_details_with_options_async(request, runtime)

    def list_conversations_with_options(
        self,
        request: main_models.ListConversationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConversationsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConversations',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConversationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_conversations_with_options_async(
        self,
        request: main_models.ListConversationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConversationsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConversations',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConversationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_conversations(
        self,
        request: main_models.ListConversationsRequest,
    ) -> main_models.ListConversationsResponse:
        runtime = RuntimeOptions()
        return self.list_conversations_with_options(request, runtime)

    async def list_conversations_async(
        self,
        request: main_models.ListConversationsRequest,
    ) -> main_models.ListConversationsResponse:
        runtime = RuntimeOptions()
        return await self.list_conversations_with_options_async(request, runtime)

    def list_download_tasks_with_options(
        self,
        request: main_models.ListDownloadTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDownloadTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDownloadTasks',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDownloadTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_download_tasks_with_options_async(
        self,
        request: main_models.ListDownloadTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDownloadTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDownloadTasks',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDownloadTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_download_tasks(
        self,
        request: main_models.ListDownloadTasksRequest,
    ) -> main_models.ListDownloadTasksResponse:
        runtime = RuntimeOptions()
        return self.list_download_tasks_with_options(request, runtime)

    async def list_download_tasks_async(
        self,
        request: main_models.ListDownloadTasksRequest,
    ) -> main_models.ListDownloadTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_download_tasks_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: main_models.ListInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: main_models.ListInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def modify_asr_config_with_options(
        self,
        request: main_models.ModifyAsrConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAsrConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.asr_acoustic_model_id):
            query['AsrAcousticModelId'] = request.asr_acoustic_model_id
        if not DaraCore.is_null(request.asr_class_vocabulary_id):
            query['AsrClassVocabularyId'] = request.asr_class_vocabulary_id
        if not DaraCore.is_null(request.asr_customization_id):
            query['AsrCustomizationId'] = request.asr_customization_id
        if not DaraCore.is_null(request.asr_overrides):
            query['AsrOverrides'] = request.asr_overrides
        if not DaraCore.is_null(request.asr_vocabulary_id):
            query['AsrVocabularyId'] = request.asr_vocabulary_id
        if not DaraCore.is_null(request.config_level):
            query['ConfigLevel'] = request.config_level
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.nls_service_type):
            query['NlsServiceType'] = request.nls_service_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAsrConfig',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAsrConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_asr_config_with_options_async(
        self,
        request: main_models.ModifyAsrConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAsrConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.asr_acoustic_model_id):
            query['AsrAcousticModelId'] = request.asr_acoustic_model_id
        if not DaraCore.is_null(request.asr_class_vocabulary_id):
            query['AsrClassVocabularyId'] = request.asr_class_vocabulary_id
        if not DaraCore.is_null(request.asr_customization_id):
            query['AsrCustomizationId'] = request.asr_customization_id
        if not DaraCore.is_null(request.asr_overrides):
            query['AsrOverrides'] = request.asr_overrides
        if not DaraCore.is_null(request.asr_vocabulary_id):
            query['AsrVocabularyId'] = request.asr_vocabulary_id
        if not DaraCore.is_null(request.config_level):
            query['ConfigLevel'] = request.config_level
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.entry_id):
            query['EntryId'] = request.entry_id
        if not DaraCore.is_null(request.nls_service_type):
            query['NlsServiceType'] = request.nls_service_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAsrConfig',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAsrConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_asr_config(
        self,
        request: main_models.ModifyAsrConfigRequest,
    ) -> main_models.ModifyAsrConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_asr_config_with_options(request, runtime)

    async def modify_asr_config_async(
        self,
        request: main_models.ModifyAsrConfigRequest,
    ) -> main_models.ModifyAsrConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_asr_config_with_options_async(request, runtime)

    def modify_greeting_config_with_options(
        self,
        request: main_models.ModifyGreetingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGreetingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.greeting_words):
            query['GreetingWords'] = request.greeting_words
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_trigger):
            query['IntentTrigger'] = request.intent_trigger
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyGreetingConfig',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGreetingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_greeting_config_with_options_async(
        self,
        request: main_models.ModifyGreetingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGreetingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.greeting_words):
            query['GreetingWords'] = request.greeting_words
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_trigger):
            query['IntentTrigger'] = request.intent_trigger
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyGreetingConfig',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGreetingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_greeting_config(
        self,
        request: main_models.ModifyGreetingConfigRequest,
    ) -> main_models.ModifyGreetingConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_greeting_config_with_options(request, runtime)

    async def modify_greeting_config_async(
        self,
        request: main_models.ModifyGreetingConfigRequest,
    ) -> main_models.ModifyGreetingConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_greeting_config_with_options_async(request, runtime)

    def modify_instance_with_options(
        self,
        request: main_models.ModifyInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.concurrency):
            query['Concurrency'] = request.concurrency
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstance',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_with_options_async(
        self,
        request: main_models.ModifyInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.concurrency):
            query['Concurrency'] = request.concurrency
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstance',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance(
        self,
        request: main_models.ModifyInstanceRequest,
    ) -> main_models.ModifyInstanceResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_with_options(request, runtime)

    async def modify_instance_async(
        self,
        request: main_models.ModifyInstanceRequest,
    ) -> main_models.ModifyInstanceResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_with_options_async(request, runtime)

    def modify_silence_timeout_config_with_options(
        self,
        request: main_models.ModifySilenceTimeoutConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySilenceTimeoutConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.final_action):
            query['FinalAction'] = request.final_action
        if not DaraCore.is_null(request.final_action_params):
            query['FinalActionParams'] = request.final_action_params
        if not DaraCore.is_null(request.final_prompt):
            query['FinalPrompt'] = request.final_prompt
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_trigger):
            query['IntentTrigger'] = request.intent_trigger
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySilenceTimeoutConfig',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySilenceTimeoutConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_silence_timeout_config_with_options_async(
        self,
        request: main_models.ModifySilenceTimeoutConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySilenceTimeoutConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.final_action):
            query['FinalAction'] = request.final_action
        if not DaraCore.is_null(request.final_action_params):
            query['FinalActionParams'] = request.final_action_params
        if not DaraCore.is_null(request.final_prompt):
            query['FinalPrompt'] = request.final_prompt
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.intent_trigger):
            query['IntentTrigger'] = request.intent_trigger
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySilenceTimeoutConfig',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySilenceTimeoutConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_silence_timeout_config(
        self,
        request: main_models.ModifySilenceTimeoutConfigRequest,
    ) -> main_models.ModifySilenceTimeoutConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_silence_timeout_config_with_options(request, runtime)

    async def modify_silence_timeout_config_async(
        self,
        request: main_models.ModifySilenceTimeoutConfigRequest,
    ) -> main_models.ModifySilenceTimeoutConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_silence_timeout_config_with_options_async(request, runtime)

    def modify_ttsconfig_with_options(
        self,
        request: main_models.ModifyTTSConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTTSConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ali_customized_voice):
            query['AliCustomizedVoice'] = request.ali_customized_voice
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_xunfei):
            query['EngineXunfei'] = request.engine_xunfei
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nls_service_type):
            query['NlsServiceType'] = request.nls_service_type
        if not DaraCore.is_null(request.pitch_rate):
            query['PitchRate'] = request.pitch_rate
        if not DaraCore.is_null(request.speech_rate):
            query['SpeechRate'] = request.speech_rate
        if not DaraCore.is_null(request.tts_overrides):
            query['TtsOverrides'] = request.tts_overrides
        if not DaraCore.is_null(request.voice):
            query['Voice'] = request.voice
        if not DaraCore.is_null(request.volume):
            query['Volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTTSConfig',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTTSConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ttsconfig_with_options_async(
        self,
        request: main_models.ModifyTTSConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTTSConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ali_customized_voice):
            query['AliCustomizedVoice'] = request.ali_customized_voice
        if not DaraCore.is_null(request.app_key):
            query['AppKey'] = request.app_key
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_xunfei):
            query['EngineXunfei'] = request.engine_xunfei
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.nls_service_type):
            query['NlsServiceType'] = request.nls_service_type
        if not DaraCore.is_null(request.pitch_rate):
            query['PitchRate'] = request.pitch_rate
        if not DaraCore.is_null(request.speech_rate):
            query['SpeechRate'] = request.speech_rate
        if not DaraCore.is_null(request.tts_overrides):
            query['TtsOverrides'] = request.tts_overrides
        if not DaraCore.is_null(request.voice):
            query['Voice'] = request.voice
        if not DaraCore.is_null(request.volume):
            query['Volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTTSConfig',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTTSConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ttsconfig(
        self,
        request: main_models.ModifyTTSConfigRequest,
    ) -> main_models.ModifyTTSConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_ttsconfig_with_options(request, runtime)

    async def modify_ttsconfig_async(
        self,
        request: main_models.ModifyTTSConfigRequest,
    ) -> main_models.ModifyTTSConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_ttsconfig_with_options_async(request, runtime)

    def modify_unrecognizing_config_with_options(
        self,
        request: main_models.ModifyUnrecognizingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUnrecognizingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.final_action):
            query['FinalAction'] = request.final_action
        if not DaraCore.is_null(request.final_action_params):
            query['FinalActionParams'] = request.final_action_params
        if not DaraCore.is_null(request.final_prompt):
            query['FinalPrompt'] = request.final_prompt
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUnrecognizingConfig',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUnrecognizingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_unrecognizing_config_with_options_async(
        self,
        request: main_models.ModifyUnrecognizingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUnrecognizingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.final_action):
            query['FinalAction'] = request.final_action
        if not DaraCore.is_null(request.final_action_params):
            query['FinalActionParams'] = request.final_action_params
        if not DaraCore.is_null(request.final_prompt):
            query['FinalPrompt'] = request.final_prompt
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUnrecognizingConfig',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUnrecognizingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_unrecognizing_config(
        self,
        request: main_models.ModifyUnrecognizingConfigRequest,
    ) -> main_models.ModifyUnrecognizingConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_unrecognizing_config_with_options(request, runtime)

    async def modify_unrecognizing_config_async(
        self,
        request: main_models.ModifyUnrecognizingConfigRequest,
    ) -> main_models.ModifyUnrecognizingConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_unrecognizing_config_with_options_async(request, runtime)

    def query_conversations_with_options(
        self,
        request: main_models.QueryConversationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryConversationsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryConversations',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryConversationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_conversations_with_options_async(
        self,
        request: main_models.QueryConversationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryConversationsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryConversations',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryConversationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_conversations(
        self,
        request: main_models.QueryConversationsRequest,
    ) -> main_models.QueryConversationsResponse:
        runtime = RuntimeOptions()
        return self.query_conversations_with_options(request, runtime)

    async def query_conversations_async(
        self,
        request: main_models.QueryConversationsRequest,
    ) -> main_models.QueryConversationsResponse:
        runtime = RuntimeOptions()
        return await self.query_conversations_with_options_async(request, runtime)

    def save_recording_with_options(
        self,
        request: main_models.SaveRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.voice_slice_recording_list):
            query['VoiceSliceRecordingList'] = request.voice_slice_recording_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveRecording',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_recording_with_options_async(
        self,
        request: main_models.SaveRecordingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveRecordingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.voice_slice_recording_list):
            query['VoiceSliceRecordingList'] = request.voice_slice_recording_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveRecording',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_recording(
        self,
        request: main_models.SaveRecordingRequest,
    ) -> main_models.SaveRecordingResponse:
        runtime = RuntimeOptions()
        return self.save_recording_with_options(request, runtime)

    async def save_recording_async(
        self,
        request: main_models.SaveRecordingRequest,
    ) -> main_models.SaveRecordingResponse:
        runtime = RuntimeOptions()
        return await self.save_recording_with_options_async(request, runtime)

    def silence_timeout_with_options(
        self,
        request: main_models.SilenceTimeoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SilenceTimeoutResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.initial_context):
            query['InitialContext'] = request.initial_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SilenceTimeout',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SilenceTimeoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def silence_timeout_with_options_async(
        self,
        request: main_models.SilenceTimeoutRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SilenceTimeoutResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not DaraCore.is_null(request.initial_context):
            query['InitialContext'] = request.initial_context
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SilenceTimeout',
            version = '2018-06-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SilenceTimeoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def silence_timeout(
        self,
        request: main_models.SilenceTimeoutRequest,
    ) -> main_models.SilenceTimeoutResponse:
        runtime = RuntimeOptions()
        return self.silence_timeout_with_options(request, runtime)

    async def silence_timeout_async(
        self,
        request: main_models.SilenceTimeoutRequest,
    ) -> main_models.SilenceTimeoutResponse:
        runtime = RuntimeOptions()
        return await self.silence_timeout_with_options_async(request, runtime)
