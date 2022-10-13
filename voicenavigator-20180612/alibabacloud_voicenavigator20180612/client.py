# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_voicenavigator20180612 import models as voice_navigator_20180612_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def associate_chatbot_instance_with_options(
        self,
        request: voice_navigator_20180612_models.AssociateChatbotInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.AssociateChatbotInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chatbot_instance_id):
            query['ChatbotInstanceId'] = request.chatbot_instance_id
        if not UtilClient.is_unset(request.chatbot_name):
            query['ChatbotName'] = request.chatbot_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateChatbotInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.AssociateChatbotInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_chatbot_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.AssociateChatbotInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.AssociateChatbotInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chatbot_instance_id):
            query['ChatbotInstanceId'] = request.chatbot_instance_id
        if not UtilClient.is_unset(request.chatbot_name):
            query['ChatbotName'] = request.chatbot_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateChatbotInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.AssociateChatbotInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_chatbot_instance(
        self,
        request: voice_navigator_20180612_models.AssociateChatbotInstanceRequest,
    ) -> voice_navigator_20180612_models.AssociateChatbotInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_chatbot_instance_with_options(request, runtime)

    async def associate_chatbot_instance_async(
        self,
        request: voice_navigator_20180612_models.AssociateChatbotInstanceRequest,
    ) -> voice_navigator_20180612_models.AssociateChatbotInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_chatbot_instance_with_options_async(request, runtime)

    def audit_ttsvoice_with_options(
        self,
        request: voice_navigator_20180612_models.AuditTTSVoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.AuditTTSVoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.speech_rate):
            query['SpeechRate'] = request.speech_rate
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        if not UtilClient.is_unset(request.voice):
            query['Voice'] = request.voice
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuditTTSVoice',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.AuditTTSVoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def audit_ttsvoice_with_options_async(
        self,
        request: voice_navigator_20180612_models.AuditTTSVoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.AuditTTSVoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.speech_rate):
            query['SpeechRate'] = request.speech_rate
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        if not UtilClient.is_unset(request.voice):
            query['Voice'] = request.voice
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuditTTSVoice',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.AuditTTSVoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def audit_ttsvoice(
        self,
        request: voice_navigator_20180612_models.AuditTTSVoiceRequest,
    ) -> voice_navigator_20180612_models.AuditTTSVoiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.audit_ttsvoice_with_options(request, runtime)

    async def audit_ttsvoice_async(
        self,
        request: voice_navigator_20180612_models.AuditTTSVoiceRequest,
    ) -> voice_navigator_20180612_models.AuditTTSVoiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.audit_ttsvoice_with_options_async(request, runtime)

    def begin_dialogue_with_options(
        self,
        request: voice_navigator_20180612_models.BeginDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.BeginDialogueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.initial_context):
            query['InitialContext'] = request.initial_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BeginDialogue',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.BeginDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def begin_dialogue_with_options_async(
        self,
        request: voice_navigator_20180612_models.BeginDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.BeginDialogueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.initial_context):
            query['InitialContext'] = request.initial_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BeginDialogue',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.BeginDialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def begin_dialogue(
        self,
        request: voice_navigator_20180612_models.BeginDialogueRequest,
    ) -> voice_navigator_20180612_models.BeginDialogueResponse:
        runtime = util_models.RuntimeOptions()
        return self.begin_dialogue_with_options(request, runtime)

    async def begin_dialogue_async(
        self,
        request: voice_navigator_20180612_models.BeginDialogueRequest,
    ) -> voice_navigator_20180612_models.BeginDialogueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.begin_dialogue_with_options_async(request, runtime)

    def collected_number_with_options(
        self,
        request: voice_navigator_20180612_models.CollectedNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.CollectedNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CollectedNumber',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.CollectedNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def collected_number_with_options_async(
        self,
        request: voice_navigator_20180612_models.CollectedNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.CollectedNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CollectedNumber',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.CollectedNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def collected_number(
        self,
        request: voice_navigator_20180612_models.CollectedNumberRequest,
    ) -> voice_navigator_20180612_models.CollectedNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.collected_number_with_options(request, runtime)

    async def collected_number_async(
        self,
        request: voice_navigator_20180612_models.CollectedNumberRequest,
    ) -> voice_navigator_20180612_models.CollectedNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.collected_number_with_options_async(request, runtime)

    def create_download_url_with_options(
        self,
        request: voice_navigator_20180612_models.CreateDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.CreateDownloadUrlResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDownloadUrl',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.CreateDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_download_url_with_options_async(
        self,
        request: voice_navigator_20180612_models.CreateDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.CreateDownloadUrlResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDownloadUrl',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.CreateDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_download_url(
        self,
        request: voice_navigator_20180612_models.CreateDownloadUrlRequest,
    ) -> voice_navigator_20180612_models.CreateDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_download_url_with_options(request, runtime)

    async def create_download_url_async(
        self,
        request: voice_navigator_20180612_models.CreateDownloadUrlRequest,
    ) -> voice_navigator_20180612_models.CreateDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_download_url_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: voice_navigator_20180612_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.concurrency):
            query['Concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.concurrency):
            query['Concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: voice_navigator_20180612_models.CreateInstanceRequest,
    ) -> voice_navigator_20180612_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: voice_navigator_20180612_models.CreateInstanceRequest,
    ) -> voice_navigator_20180612_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def debug_begin_dialogue_with_options(
        self,
        request: voice_navigator_20180612_models.DebugBeginDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DebugBeginDialogueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.initial_context):
            query['InitialContext'] = request.initial_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DebugBeginDialogue',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DebugBeginDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def debug_begin_dialogue_with_options_async(
        self,
        request: voice_navigator_20180612_models.DebugBeginDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DebugBeginDialogueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.initial_context):
            query['InitialContext'] = request.initial_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DebugBeginDialogue',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DebugBeginDialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def debug_begin_dialogue(
        self,
        request: voice_navigator_20180612_models.DebugBeginDialogueRequest,
    ) -> voice_navigator_20180612_models.DebugBeginDialogueResponse:
        runtime = util_models.RuntimeOptions()
        return self.debug_begin_dialogue_with_options(request, runtime)

    async def debug_begin_dialogue_async(
        self,
        request: voice_navigator_20180612_models.DebugBeginDialogueRequest,
    ) -> voice_navigator_20180612_models.DebugBeginDialogueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.debug_begin_dialogue_with_options_async(request, runtime)

    def debug_collected_number_with_options(
        self,
        request: voice_navigator_20180612_models.DebugCollectedNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DebugCollectedNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DebugCollectedNumber',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DebugCollectedNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def debug_collected_number_with_options_async(
        self,
        request: voice_navigator_20180612_models.DebugCollectedNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DebugCollectedNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DebugCollectedNumber',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DebugCollectedNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def debug_collected_number(
        self,
        request: voice_navigator_20180612_models.DebugCollectedNumberRequest,
    ) -> voice_navigator_20180612_models.DebugCollectedNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.debug_collected_number_with_options(request, runtime)

    async def debug_collected_number_async(
        self,
        request: voice_navigator_20180612_models.DebugCollectedNumberRequest,
    ) -> voice_navigator_20180612_models.DebugCollectedNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.debug_collected_number_with_options_async(request, runtime)

    def debug_dialogue_with_options(
        self,
        request: voice_navigator_20180612_models.DebugDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DebugDialogueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.additional_context):
            query['AdditionalContext'] = request.additional_context
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DebugDialogue',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DebugDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def debug_dialogue_with_options_async(
        self,
        request: voice_navigator_20180612_models.DebugDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DebugDialogueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.additional_context):
            query['AdditionalContext'] = request.additional_context
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DebugDialogue',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DebugDialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def debug_dialogue(
        self,
        request: voice_navigator_20180612_models.DebugDialogueRequest,
    ) -> voice_navigator_20180612_models.DebugDialogueResponse:
        runtime = util_models.RuntimeOptions()
        return self.debug_dialogue_with_options(request, runtime)

    async def debug_dialogue_async(
        self,
        request: voice_navigator_20180612_models.DebugDialogueRequest,
    ) -> voice_navigator_20180612_models.DebugDialogueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.debug_dialogue_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: voice_navigator_20180612_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: voice_navigator_20180612_models.DeleteInstanceRequest,
    ) -> voice_navigator_20180612_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: voice_navigator_20180612_models.DeleteInstanceRequest,
    ) -> voice_navigator_20180612_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def describe_conversation_with_options(
        self,
        request: voice_navigator_20180612_models.DescribeConversationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeConversationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConversation',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeConversationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_conversation_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeConversationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeConversationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConversation',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeConversationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_conversation(
        self,
        request: voice_navigator_20180612_models.DescribeConversationRequest,
    ) -> voice_navigator_20180612_models.DescribeConversationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_conversation_with_options(request, runtime)

    async def describe_conversation_async(
        self,
        request: voice_navigator_20180612_models.DescribeConversationRequest,
    ) -> voice_navigator_20180612_models.DescribeConversationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_conversation_with_options_async(request, runtime)

    def describe_conversation_context_with_options(
        self,
        request: voice_navigator_20180612_models.DescribeConversationContextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeConversationContextResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConversationContext',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeConversationContextResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_conversation_context_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeConversationContextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeConversationContextResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConversationContext',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeConversationContextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_conversation_context(
        self,
        request: voice_navigator_20180612_models.DescribeConversationContextRequest,
    ) -> voice_navigator_20180612_models.DescribeConversationContextResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_conversation_context_with_options(request, runtime)

    async def describe_conversation_context_async(
        self,
        request: voice_navigator_20180612_models.DescribeConversationContextRequest,
    ) -> voice_navigator_20180612_models.DescribeConversationContextResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_conversation_context_with_options_async(request, runtime)

    def describe_export_progress_with_options(
        self,
        request: voice_navigator_20180612_models.DescribeExportProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeExportProgressResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExportProgress',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeExportProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_export_progress_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeExportProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeExportProgressResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExportProgress',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeExportProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_export_progress(
        self,
        request: voice_navigator_20180612_models.DescribeExportProgressRequest,
    ) -> voice_navigator_20180612_models.DescribeExportProgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_export_progress_with_options(request, runtime)

    async def describe_export_progress_async(
        self,
        request: voice_navigator_20180612_models.DescribeExportProgressRequest,
    ) -> voice_navigator_20180612_models.DescribeExportProgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_export_progress_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: voice_navigator_20180612_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        request: voice_navigator_20180612_models.DescribeInstanceRequest,
    ) -> voice_navigator_20180612_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: voice_navigator_20180612_models.DescribeInstanceRequest,
    ) -> voice_navigator_20180612_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_navigation_config_with_options(
        self,
        request: voice_navigator_20180612_models.DescribeNavigationConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeNavigationConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNavigationConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeNavigationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_navigation_config_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeNavigationConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeNavigationConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNavigationConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeNavigationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_navigation_config(
        self,
        request: voice_navigator_20180612_models.DescribeNavigationConfigRequest,
    ) -> voice_navigator_20180612_models.DescribeNavigationConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_navigation_config_with_options(request, runtime)

    async def describe_navigation_config_async(
        self,
        request: voice_navigator_20180612_models.DescribeNavigationConfigRequest,
    ) -> voice_navigator_20180612_models.DescribeNavigationConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_navigation_config_with_options_async(request, runtime)

    def describe_recording_with_options(
        self,
        request: voice_navigator_20180612_models.DescribeRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeRecordingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecording',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_recording_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeRecordingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecording',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_recording(
        self,
        request: voice_navigator_20180612_models.DescribeRecordingRequest,
    ) -> voice_navigator_20180612_models.DescribeRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_recording_with_options(request, runtime)

    async def describe_recording_async(
        self,
        request: voice_navigator_20180612_models.DescribeRecordingRequest,
    ) -> voice_navigator_20180612_models.DescribeRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_recording_with_options_async(request, runtime)

    def describe_statistical_data_with_options(
        self,
        request: voice_navigator_20180612_models.DescribeStatisticalDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeStatisticalDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStatisticalData',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeStatisticalDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_statistical_data_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeStatisticalDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeStatisticalDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStatisticalData',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeStatisticalDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_statistical_data(
        self,
        request: voice_navigator_20180612_models.DescribeStatisticalDataRequest,
    ) -> voice_navigator_20180612_models.DescribeStatisticalDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_statistical_data_with_options(request, runtime)

    async def describe_statistical_data_async(
        self,
        request: voice_navigator_20180612_models.DescribeStatisticalDataRequest,
    ) -> voice_navigator_20180612_models.DescribeStatisticalDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_statistical_data_with_options_async(request, runtime)

    def describe_ttsconfig_with_options(
        self,
        request: voice_navigator_20180612_models.DescribeTTSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeTTSConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTTSConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeTTSConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ttsconfig_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeTTSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeTTSConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTTSConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeTTSConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ttsconfig(
        self,
        request: voice_navigator_20180612_models.DescribeTTSConfigRequest,
    ) -> voice_navigator_20180612_models.DescribeTTSConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ttsconfig_with_options(request, runtime)

    async def describe_ttsconfig_async(
        self,
        request: voice_navigator_20180612_models.DescribeTTSConfigRequest,
    ) -> voice_navigator_20180612_models.DescribeTTSConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ttsconfig_with_options_async(request, runtime)

    def dialogue_with_options(
        self,
        request: voice_navigator_20180612_models.DialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DialogueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.additional_context):
            query['AdditionalContext'] = request.additional_context
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.emotion):
            query['Emotion'] = request.emotion
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not UtilClient.is_unset(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Dialogue',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def dialogue_with_options_async(
        self,
        request: voice_navigator_20180612_models.DialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DialogueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.additional_context):
            query['AdditionalContext'] = request.additional_context
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.emotion):
            query['Emotion'] = request.emotion
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not UtilClient.is_unset(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Dialogue',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dialogue(
        self,
        request: voice_navigator_20180612_models.DialogueRequest,
    ) -> voice_navigator_20180612_models.DialogueResponse:
        runtime = util_models.RuntimeOptions()
        return self.dialogue_with_options(request, runtime)

    async def dialogue_async(
        self,
        request: voice_navigator_20180612_models.DialogueRequest,
    ) -> voice_navigator_20180612_models.DialogueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dialogue_with_options_async(request, runtime)

    def disable_instance_with_options(
        self,
        request: voice_navigator_20180612_models.DisableInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DisableInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DisableInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.DisableInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DisableInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DisableInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_instance(
        self,
        request: voice_navigator_20180612_models.DisableInstanceRequest,
    ) -> voice_navigator_20180612_models.DisableInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_instance_with_options(request, runtime)

    async def disable_instance_async(
        self,
        request: voice_navigator_20180612_models.DisableInstanceRequest,
    ) -> voice_navigator_20180612_models.DisableInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_instance_with_options_async(request, runtime)

    def enable_instance_with_options(
        self,
        request: voice_navigator_20180612_models.EnableInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.EnableInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.EnableInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.EnableInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.EnableInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.EnableInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_instance(
        self,
        request: voice_navigator_20180612_models.EnableInstanceRequest,
    ) -> voice_navigator_20180612_models.EnableInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_instance_with_options(request, runtime)

    async def enable_instance_async(
        self,
        request: voice_navigator_20180612_models.EnableInstanceRequest,
    ) -> voice_navigator_20180612_models.EnableInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_instance_with_options_async(request, runtime)

    def end_dialogue_with_options(
        self,
        request: voice_navigator_20180612_models.EndDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.EndDialogueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.hang_up_params):
            query['HangUpParams'] = request.hang_up_params
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EndDialogue',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.EndDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def end_dialogue_with_options_async(
        self,
        request: voice_navigator_20180612_models.EndDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.EndDialogueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.hang_up_params):
            query['HangUpParams'] = request.hang_up_params
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EndDialogue',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.EndDialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def end_dialogue(
        self,
        request: voice_navigator_20180612_models.EndDialogueRequest,
    ) -> voice_navigator_20180612_models.EndDialogueResponse:
        runtime = util_models.RuntimeOptions()
        return self.end_dialogue_with_options(request, runtime)

    async def end_dialogue_async(
        self,
        request: voice_navigator_20180612_models.EndDialogueRequest,
    ) -> voice_navigator_20180612_models.EndDialogueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.end_dialogue_with_options_async(request, runtime)

    def export_conversation_details_with_options(
        self,
        request: voice_navigator_20180612_models.ExportConversationDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ExportConversationDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time_left_range):
            query['BeginTimeLeftRange'] = request.begin_time_left_range
        if not UtilClient.is_unset(request.begin_time_right_range):
            query['BeginTimeRightRange'] = request.begin_time_right_range
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.options):
            query['Options'] = request.options
        if not UtilClient.is_unset(request.rounds_left_range):
            query['RoundsLeftRange'] = request.rounds_left_range
        if not UtilClient.is_unset(request.rounds_right_range):
            query['RoundsRightRange'] = request.rounds_right_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportConversationDetails',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ExportConversationDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_conversation_details_with_options_async(
        self,
        request: voice_navigator_20180612_models.ExportConversationDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ExportConversationDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time_left_range):
            query['BeginTimeLeftRange'] = request.begin_time_left_range
        if not UtilClient.is_unset(request.begin_time_right_range):
            query['BeginTimeRightRange'] = request.begin_time_right_range
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.options):
            query['Options'] = request.options
        if not UtilClient.is_unset(request.rounds_left_range):
            query['RoundsLeftRange'] = request.rounds_left_range
        if not UtilClient.is_unset(request.rounds_right_range):
            query['RoundsRightRange'] = request.rounds_right_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportConversationDetails',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ExportConversationDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_conversation_details(
        self,
        request: voice_navigator_20180612_models.ExportConversationDetailsRequest,
    ) -> voice_navigator_20180612_models.ExportConversationDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_conversation_details_with_options(request, runtime)

    async def export_conversation_details_async(
        self,
        request: voice_navigator_20180612_models.ExportConversationDetailsRequest,
    ) -> voice_navigator_20180612_models.ExportConversationDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_conversation_details_with_options_async(request, runtime)

    def export_statistical_data_with_options(
        self,
        request: voice_navigator_20180612_models.ExportStatisticalDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ExportStatisticalDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time_left_range):
            query['BeginTimeLeftRange'] = request.begin_time_left_range
        if not UtilClient.is_unset(request.begin_time_right_range):
            query['BeginTimeRightRange'] = request.begin_time_right_range
        if not UtilClient.is_unset(request.export_type):
            query['ExportType'] = request.export_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.time_unit):
            query['TimeUnit'] = request.time_unit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportStatisticalData',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ExportStatisticalDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_statistical_data_with_options_async(
        self,
        request: voice_navigator_20180612_models.ExportStatisticalDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ExportStatisticalDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time_left_range):
            query['BeginTimeLeftRange'] = request.begin_time_left_range
        if not UtilClient.is_unset(request.begin_time_right_range):
            query['BeginTimeRightRange'] = request.begin_time_right_range
        if not UtilClient.is_unset(request.export_type):
            query['ExportType'] = request.export_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.time_unit):
            query['TimeUnit'] = request.time_unit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportStatisticalData',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ExportStatisticalDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_statistical_data(
        self,
        request: voice_navigator_20180612_models.ExportStatisticalDataRequest,
    ) -> voice_navigator_20180612_models.ExportStatisticalDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_statistical_data_with_options(request, runtime)

    async def export_statistical_data_async(
        self,
        request: voice_navigator_20180612_models.ExportStatisticalDataRequest,
    ) -> voice_navigator_20180612_models.ExportStatisticalDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_statistical_data_with_options_async(request, runtime)

    def generate_upload_url_with_options(
        self,
        request: voice_navigator_20180612_models.GenerateUploadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.GenerateUploadUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_ip):
            body['CallerIp'] = request.caller_ip
        if not UtilClient.is_unset(request.caller_parent_id):
            body['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            body['InstanceOwnerId'] = request.instance_owner_id
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.proxy_original_security_transport):
            body['ProxyOriginalSecurityTransport'] = request.proxy_original_security_transport
        if not UtilClient.is_unset(request.proxy_original_source_ip):
            body['ProxyOriginalSourceIp'] = request.proxy_original_source_ip
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.security_transport):
            body['SecurityTransport'] = request.security_transport
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.tenant_name):
            body['TenantName'] = request.tenant_name
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.xspace_servicer_id):
            body['XspaceServicerId'] = request.xspace_servicer_id
        if not UtilClient.is_unset(request.xspace_tenant_bu_id):
            body['XspaceTenantBuId'] = request.xspace_tenant_bu_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateUploadUrl',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.GenerateUploadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_upload_url_with_options_async(
        self,
        request: voice_navigator_20180612_models.GenerateUploadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.GenerateUploadUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_ip):
            body['CallerIp'] = request.caller_ip
        if not UtilClient.is_unset(request.caller_parent_id):
            body['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            body['InstanceOwnerId'] = request.instance_owner_id
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.proxy_original_security_transport):
            body['ProxyOriginalSecurityTransport'] = request.proxy_original_security_transport
        if not UtilClient.is_unset(request.proxy_original_source_ip):
            body['ProxyOriginalSourceIp'] = request.proxy_original_source_ip
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.security_transport):
            body['SecurityTransport'] = request.security_transport
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.tenant_name):
            body['TenantName'] = request.tenant_name
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.xspace_servicer_id):
            body['XspaceServicerId'] = request.xspace_servicer_id
        if not UtilClient.is_unset(request.xspace_tenant_bu_id):
            body['XspaceTenantBuId'] = request.xspace_tenant_bu_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateUploadUrl',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.GenerateUploadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_upload_url(
        self,
        request: voice_navigator_20180612_models.GenerateUploadUrlRequest,
    ) -> voice_navigator_20180612_models.GenerateUploadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_upload_url_with_options(request, runtime)

    async def generate_upload_url_async(
        self,
        request: voice_navigator_20180612_models.GenerateUploadUrlRequest,
    ) -> voice_navigator_20180612_models.GenerateUploadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_upload_url_with_options_async(request, runtime)

    def get_asr_config_with_options(
        self,
        request: voice_navigator_20180612_models.GetAsrConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.GetAsrConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_level):
            query['ConfigLevel'] = request.config_level
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsrConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.GetAsrConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_asr_config_with_options_async(
        self,
        request: voice_navigator_20180612_models.GetAsrConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.GetAsrConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_level):
            query['ConfigLevel'] = request.config_level
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsrConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.GetAsrConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_asr_config(
        self,
        request: voice_navigator_20180612_models.GetAsrConfigRequest,
    ) -> voice_navigator_20180612_models.GetAsrConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_asr_config_with_options(request, runtime)

    async def get_asr_config_async(
        self,
        request: voice_navigator_20180612_models.GetAsrConfigRequest,
    ) -> voice_navigator_20180612_models.GetAsrConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_asr_config_with_options_async(request, runtime)

    def get_real_time_concurrency_with_options(
        self,
        request: voice_navigator_20180612_models.GetRealTimeConcurrencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.GetRealTimeConcurrencyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealTimeConcurrency',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.GetRealTimeConcurrencyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_real_time_concurrency_with_options_async(
        self,
        request: voice_navigator_20180612_models.GetRealTimeConcurrencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.GetRealTimeConcurrencyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealTimeConcurrency',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.GetRealTimeConcurrencyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_real_time_concurrency(
        self,
        request: voice_navigator_20180612_models.GetRealTimeConcurrencyRequest,
    ) -> voice_navigator_20180612_models.GetRealTimeConcurrencyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_real_time_concurrency_with_options(request, runtime)

    async def get_real_time_concurrency_async(
        self,
        request: voice_navigator_20180612_models.GetRealTimeConcurrencyRequest,
    ) -> voice_navigator_20180612_models.GetRealTimeConcurrencyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_real_time_concurrency_with_options_async(request, runtime)

    def list_chatbot_instances_with_options(
        self,
        request: voice_navigator_20180612_models.ListChatbotInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListChatbotInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChatbotInstances',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ListChatbotInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chatbot_instances_with_options_async(
        self,
        request: voice_navigator_20180612_models.ListChatbotInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListChatbotInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChatbotInstances',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ListChatbotInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chatbot_instances(
        self,
        request: voice_navigator_20180612_models.ListChatbotInstancesRequest,
    ) -> voice_navigator_20180612_models.ListChatbotInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_chatbot_instances_with_options(request, runtime)

    async def list_chatbot_instances_async(
        self,
        request: voice_navigator_20180612_models.ListChatbotInstancesRequest,
    ) -> voice_navigator_20180612_models.ListChatbotInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_chatbot_instances_with_options_async(request, runtime)

    def list_conversation_details_with_options(
        self,
        request: voice_navigator_20180612_models.ListConversationDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListConversationDetailsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConversationDetails',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ListConversationDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_conversation_details_with_options_async(
        self,
        request: voice_navigator_20180612_models.ListConversationDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListConversationDetailsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConversationDetails',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ListConversationDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_conversation_details(
        self,
        request: voice_navigator_20180612_models.ListConversationDetailsRequest,
    ) -> voice_navigator_20180612_models.ListConversationDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_conversation_details_with_options(request, runtime)

    async def list_conversation_details_async(
        self,
        request: voice_navigator_20180612_models.ListConversationDetailsRequest,
    ) -> voice_navigator_20180612_models.ListConversationDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_conversation_details_with_options_async(request, runtime)

    def list_conversations_with_options(
        self,
        request: voice_navigator_20180612_models.ListConversationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListConversationsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConversations',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ListConversationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_conversations_with_options_async(
        self,
        request: voice_navigator_20180612_models.ListConversationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListConversationsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConversations',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ListConversationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_conversations(
        self,
        request: voice_navigator_20180612_models.ListConversationsRequest,
    ) -> voice_navigator_20180612_models.ListConversationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_conversations_with_options(request, runtime)

    async def list_conversations_async(
        self,
        request: voice_navigator_20180612_models.ListConversationsRequest,
    ) -> voice_navigator_20180612_models.ListConversationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_conversations_with_options_async(request, runtime)

    def list_download_tasks_with_options(
        self,
        request: voice_navigator_20180612_models.ListDownloadTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListDownloadTasksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDownloadTasks',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ListDownloadTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_download_tasks_with_options_async(
        self,
        request: voice_navigator_20180612_models.ListDownloadTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListDownloadTasksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDownloadTasks',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ListDownloadTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_download_tasks(
        self,
        request: voice_navigator_20180612_models.ListDownloadTasksRequest,
    ) -> voice_navigator_20180612_models.ListDownloadTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_download_tasks_with_options(request, runtime)

    async def list_download_tasks_async(
        self,
        request: voice_navigator_20180612_models.ListDownloadTasksRequest,
    ) -> voice_navigator_20180612_models.ListDownloadTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_download_tasks_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: voice_navigator_20180612_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: voice_navigator_20180612_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: voice_navigator_20180612_models.ListInstancesRequest,
    ) -> voice_navigator_20180612_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: voice_navigator_20180612_models.ListInstancesRequest,
    ) -> voice_navigator_20180612_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def modify_asr_config_with_options(
        self,
        request: voice_navigator_20180612_models.ModifyAsrConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyAsrConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asr_acoustic_model_id):
            query['AsrAcousticModelId'] = request.asr_acoustic_model_id
        if not UtilClient.is_unset(request.asr_class_vocabulary_id):
            query['AsrClassVocabularyId'] = request.asr_class_vocabulary_id
        if not UtilClient.is_unset(request.asr_customization_id):
            query['AsrCustomizationId'] = request.asr_customization_id
        if not UtilClient.is_unset(request.asr_vocabulary_id):
            query['AsrVocabularyId'] = request.asr_vocabulary_id
        if not UtilClient.is_unset(request.config_level):
            query['ConfigLevel'] = request.config_level
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAsrConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ModifyAsrConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_asr_config_with_options_async(
        self,
        request: voice_navigator_20180612_models.ModifyAsrConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyAsrConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asr_acoustic_model_id):
            query['AsrAcousticModelId'] = request.asr_acoustic_model_id
        if not UtilClient.is_unset(request.asr_class_vocabulary_id):
            query['AsrClassVocabularyId'] = request.asr_class_vocabulary_id
        if not UtilClient.is_unset(request.asr_customization_id):
            query['AsrCustomizationId'] = request.asr_customization_id
        if not UtilClient.is_unset(request.asr_vocabulary_id):
            query['AsrVocabularyId'] = request.asr_vocabulary_id
        if not UtilClient.is_unset(request.config_level):
            query['ConfigLevel'] = request.config_level
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAsrConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ModifyAsrConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_asr_config(
        self,
        request: voice_navigator_20180612_models.ModifyAsrConfigRequest,
    ) -> voice_navigator_20180612_models.ModifyAsrConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_asr_config_with_options(request, runtime)

    async def modify_asr_config_async(
        self,
        request: voice_navigator_20180612_models.ModifyAsrConfigRequest,
    ) -> voice_navigator_20180612_models.ModifyAsrConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_asr_config_with_options_async(request, runtime)

    def modify_greeting_config_with_options(
        self,
        request: voice_navigator_20180612_models.ModifyGreetingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyGreetingConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.greeting_words):
            query['GreetingWords'] = request.greeting_words
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_trigger):
            query['IntentTrigger'] = request.intent_trigger
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGreetingConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ModifyGreetingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_greeting_config_with_options_async(
        self,
        request: voice_navigator_20180612_models.ModifyGreetingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyGreetingConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.greeting_words):
            query['GreetingWords'] = request.greeting_words
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_trigger):
            query['IntentTrigger'] = request.intent_trigger
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGreetingConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ModifyGreetingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_greeting_config(
        self,
        request: voice_navigator_20180612_models.ModifyGreetingConfigRequest,
    ) -> voice_navigator_20180612_models.ModifyGreetingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_greeting_config_with_options(request, runtime)

    async def modify_greeting_config_async(
        self,
        request: voice_navigator_20180612_models.ModifyGreetingConfigRequest,
    ) -> voice_navigator_20180612_models.ModifyGreetingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_greeting_config_with_options_async(request, runtime)

    def modify_instance_with_options(
        self,
        request: voice_navigator_20180612_models.ModifyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.concurrency):
            query['Concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ModifyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.ModifyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.concurrency):
            query['Concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ModifyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance(
        self,
        request: voice_navigator_20180612_models.ModifyInstanceRequest,
    ) -> voice_navigator_20180612_models.ModifyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_with_options(request, runtime)

    async def modify_instance_async(
        self,
        request: voice_navigator_20180612_models.ModifyInstanceRequest,
    ) -> voice_navigator_20180612_models.ModifyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_with_options_async(request, runtime)

    def modify_silence_timeout_config_with_options(
        self,
        request: voice_navigator_20180612_models.ModifySilenceTimeoutConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifySilenceTimeoutConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.final_action):
            query['FinalAction'] = request.final_action
        if not UtilClient.is_unset(request.final_action_params):
            query['FinalActionParams'] = request.final_action_params
        if not UtilClient.is_unset(request.final_prompt):
            query['FinalPrompt'] = request.final_prompt
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_trigger):
            query['IntentTrigger'] = request.intent_trigger
        if not UtilClient.is_unset(request.prompt):
            query['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySilenceTimeoutConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ModifySilenceTimeoutConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_silence_timeout_config_with_options_async(
        self,
        request: voice_navigator_20180612_models.ModifySilenceTimeoutConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifySilenceTimeoutConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.final_action):
            query['FinalAction'] = request.final_action
        if not UtilClient.is_unset(request.final_action_params):
            query['FinalActionParams'] = request.final_action_params
        if not UtilClient.is_unset(request.final_prompt):
            query['FinalPrompt'] = request.final_prompt
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_trigger):
            query['IntentTrigger'] = request.intent_trigger
        if not UtilClient.is_unset(request.prompt):
            query['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySilenceTimeoutConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ModifySilenceTimeoutConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_silence_timeout_config(
        self,
        request: voice_navigator_20180612_models.ModifySilenceTimeoutConfigRequest,
    ) -> voice_navigator_20180612_models.ModifySilenceTimeoutConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_silence_timeout_config_with_options(request, runtime)

    async def modify_silence_timeout_config_async(
        self,
        request: voice_navigator_20180612_models.ModifySilenceTimeoutConfigRequest,
    ) -> voice_navigator_20180612_models.ModifySilenceTimeoutConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_silence_timeout_config_with_options_async(request, runtime)

    def modify_ttsconfig_with_options(
        self,
        request: voice_navigator_20180612_models.ModifyTTSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyTTSConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.nls_service_type):
            query['NlsServiceType'] = request.nls_service_type
        if not UtilClient.is_unset(request.speech_rate):
            query['SpeechRate'] = request.speech_rate
        if not UtilClient.is_unset(request.voice):
            query['Voice'] = request.voice
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTTSConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ModifyTTSConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ttsconfig_with_options_async(
        self,
        request: voice_navigator_20180612_models.ModifyTTSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyTTSConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.nls_service_type):
            query['NlsServiceType'] = request.nls_service_type
        if not UtilClient.is_unset(request.speech_rate):
            query['SpeechRate'] = request.speech_rate
        if not UtilClient.is_unset(request.voice):
            query['Voice'] = request.voice
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTTSConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ModifyTTSConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ttsconfig(
        self,
        request: voice_navigator_20180612_models.ModifyTTSConfigRequest,
    ) -> voice_navigator_20180612_models.ModifyTTSConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ttsconfig_with_options(request, runtime)

    async def modify_ttsconfig_async(
        self,
        request: voice_navigator_20180612_models.ModifyTTSConfigRequest,
    ) -> voice_navigator_20180612_models.ModifyTTSConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ttsconfig_with_options_async(request, runtime)

    def modify_unrecognizing_config_with_options(
        self,
        request: voice_navigator_20180612_models.ModifyUnrecognizingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyUnrecognizingConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.final_action):
            query['FinalAction'] = request.final_action
        if not UtilClient.is_unset(request.final_action_params):
            query['FinalActionParams'] = request.final_action_params
        if not UtilClient.is_unset(request.final_prompt):
            query['FinalPrompt'] = request.final_prompt
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.prompt):
            query['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUnrecognizingConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ModifyUnrecognizingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_unrecognizing_config_with_options_async(
        self,
        request: voice_navigator_20180612_models.ModifyUnrecognizingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyUnrecognizingConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.final_action):
            query['FinalAction'] = request.final_action
        if not UtilClient.is_unset(request.final_action_params):
            query['FinalActionParams'] = request.final_action_params
        if not UtilClient.is_unset(request.final_prompt):
            query['FinalPrompt'] = request.final_prompt
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.prompt):
            query['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUnrecognizingConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ModifyUnrecognizingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_unrecognizing_config(
        self,
        request: voice_navigator_20180612_models.ModifyUnrecognizingConfigRequest,
    ) -> voice_navigator_20180612_models.ModifyUnrecognizingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_unrecognizing_config_with_options(request, runtime)

    async def modify_unrecognizing_config_async(
        self,
        request: voice_navigator_20180612_models.ModifyUnrecognizingConfigRequest,
    ) -> voice_navigator_20180612_models.ModifyUnrecognizingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_unrecognizing_config_with_options_async(request, runtime)

    def query_conversations_with_options(
        self,
        request: voice_navigator_20180612_models.QueryConversationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.QueryConversationsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryConversations',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.QueryConversationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_conversations_with_options_async(
        self,
        request: voice_navigator_20180612_models.QueryConversationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.QueryConversationsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryConversations',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.QueryConversationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_conversations(
        self,
        request: voice_navigator_20180612_models.QueryConversationsRequest,
    ) -> voice_navigator_20180612_models.QueryConversationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_conversations_with_options(request, runtime)

    async def query_conversations_async(
        self,
        request: voice_navigator_20180612_models.QueryConversationsRequest,
    ) -> voice_navigator_20180612_models.QueryConversationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_conversations_with_options_async(request, runtime)

    def save_recording_with_options(
        self,
        request: voice_navigator_20180612_models.SaveRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.SaveRecordingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.voice_slice_recording_list):
            query['VoiceSliceRecordingList'] = request.voice_slice_recording_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveRecording',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.SaveRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_recording_with_options_async(
        self,
        request: voice_navigator_20180612_models.SaveRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.SaveRecordingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.voice_slice_recording_list):
            query['VoiceSliceRecordingList'] = request.voice_slice_recording_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveRecording',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.SaveRecordingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_recording(
        self,
        request: voice_navigator_20180612_models.SaveRecordingRequest,
    ) -> voice_navigator_20180612_models.SaveRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_recording_with_options(request, runtime)

    async def save_recording_async(
        self,
        request: voice_navigator_20180612_models.SaveRecordingRequest,
    ) -> voice_navigator_20180612_models.SaveRecordingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_recording_with_options_async(request, runtime)

    def silence_timeout_with_options(
        self,
        request: voice_navigator_20180612_models.SilenceTimeoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.SilenceTimeoutResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.initial_context):
            query['InitialContext'] = request.initial_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SilenceTimeout',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.SilenceTimeoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def silence_timeout_with_options_async(
        self,
        request: voice_navigator_20180612_models.SilenceTimeoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.SilenceTimeoutResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.initial_context):
            query['InitialContext'] = request.initial_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SilenceTimeout',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.SilenceTimeoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def silence_timeout(
        self,
        request: voice_navigator_20180612_models.SilenceTimeoutRequest,
    ) -> voice_navigator_20180612_models.SilenceTimeoutResponse:
        runtime = util_models.RuntimeOptions()
        return self.silence_timeout_with_options(request, runtime)

    async def silence_timeout_async(
        self,
        request: voice_navigator_20180612_models.SilenceTimeoutRequest,
    ) -> voice_navigator_20180612_models.SilenceTimeoutResponse:
        runtime = util_models.RuntimeOptions()
        return await self.silence_timeout_with_options_async(request, runtime)
