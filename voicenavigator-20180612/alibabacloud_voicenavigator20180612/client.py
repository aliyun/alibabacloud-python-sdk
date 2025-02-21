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
        """
        @param request: AssociateChatbotInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateChatbotInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chatbot_instance_id):
            query['ChatbotInstanceId'] = request.chatbot_instance_id
        if not UtilClient.is_unset(request.chatbot_name):
            query['ChatbotName'] = request.chatbot_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.nlu_service_params_json):
            query['NluServiceParamsJson'] = request.nlu_service_params_json
        if not UtilClient.is_unset(request.nlu_service_type):
            query['NluServiceType'] = request.nlu_service_type
        if not UtilClient.is_unset(request.union_source):
            query['UnionSource'] = request.union_source
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.AssociateChatbotInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.AssociateChatbotInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def associate_chatbot_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.AssociateChatbotInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.AssociateChatbotInstanceResponse:
        """
        @param request: AssociateChatbotInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateChatbotInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chatbot_instance_id):
            query['ChatbotInstanceId'] = request.chatbot_instance_id
        if not UtilClient.is_unset(request.chatbot_name):
            query['ChatbotName'] = request.chatbot_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.nlu_service_params_json):
            query['NluServiceParamsJson'] = request.nlu_service_params_json
        if not UtilClient.is_unset(request.nlu_service_type):
            query['NluServiceType'] = request.nlu_service_type
        if not UtilClient.is_unset(request.union_source):
            query['UnionSource'] = request.union_source
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.AssociateChatbotInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.AssociateChatbotInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def associate_chatbot_instance(
        self,
        request: voice_navigator_20180612_models.AssociateChatbotInstanceRequest,
    ) -> voice_navigator_20180612_models.AssociateChatbotInstanceResponse:
        """
        @param request: AssociateChatbotInstanceRequest
        @return: AssociateChatbotInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_chatbot_instance_with_options(request, runtime)

    async def associate_chatbot_instance_async(
        self,
        request: voice_navigator_20180612_models.AssociateChatbotInstanceRequest,
    ) -> voice_navigator_20180612_models.AssociateChatbotInstanceResponse:
        """
        @param request: AssociateChatbotInstanceRequest
        @return: AssociateChatbotInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.associate_chatbot_instance_with_options_async(request, runtime)

    def audit_ttsvoice_with_options(
        self,
        request: voice_navigator_20180612_models.AuditTTSVoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.AuditTTSVoiceResponse:
        """
        @summary AuditTTSVoice
        
        @param request: AuditTTSVoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuditTTSVoiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pitch_rate):
            query['PitchRate'] = request.pitch_rate
        if not UtilClient.is_unset(request.secret_key):
            query['SecretKey'] = request.secret_key
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.AuditTTSVoiceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.AuditTTSVoiceResponse(),
                self.execute(params, req, runtime)
            )

    async def audit_ttsvoice_with_options_async(
        self,
        request: voice_navigator_20180612_models.AuditTTSVoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.AuditTTSVoiceResponse:
        """
        @summary AuditTTSVoice
        
        @param request: AuditTTSVoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuditTTSVoiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pitch_rate):
            query['PitchRate'] = request.pitch_rate
        if not UtilClient.is_unset(request.secret_key):
            query['SecretKey'] = request.secret_key
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.AuditTTSVoiceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.AuditTTSVoiceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def audit_ttsvoice(
        self,
        request: voice_navigator_20180612_models.AuditTTSVoiceRequest,
    ) -> voice_navigator_20180612_models.AuditTTSVoiceResponse:
        """
        @summary AuditTTSVoice
        
        @param request: AuditTTSVoiceRequest
        @return: AuditTTSVoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.audit_ttsvoice_with_options(request, runtime)

    async def audit_ttsvoice_async(
        self,
        request: voice_navigator_20180612_models.AuditTTSVoiceRequest,
    ) -> voice_navigator_20180612_models.AuditTTSVoiceResponse:
        """
        @summary AuditTTSVoice
        
        @param request: AuditTTSVoiceRequest
        @return: AuditTTSVoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.audit_ttsvoice_with_options_async(request, runtime)

    def begin_dialogue_with_options(
        self,
        request: voice_navigator_20180612_models.BeginDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.BeginDialogueResponse:
        """
        @param request: BeginDialogueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BeginDialogueResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.BeginDialogueResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.BeginDialogueResponse(),
                self.execute(params, req, runtime)
            )

    async def begin_dialogue_with_options_async(
        self,
        request: voice_navigator_20180612_models.BeginDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.BeginDialogueResponse:
        """
        @param request: BeginDialogueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BeginDialogueResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.BeginDialogueResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.BeginDialogueResponse(),
                await self.execute_async(params, req, runtime)
            )

    def begin_dialogue(
        self,
        request: voice_navigator_20180612_models.BeginDialogueRequest,
    ) -> voice_navigator_20180612_models.BeginDialogueResponse:
        """
        @param request: BeginDialogueRequest
        @return: BeginDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.begin_dialogue_with_options(request, runtime)

    async def begin_dialogue_async(
        self,
        request: voice_navigator_20180612_models.BeginDialogueRequest,
    ) -> voice_navigator_20180612_models.BeginDialogueResponse:
        """
        @param request: BeginDialogueRequest
        @return: BeginDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.begin_dialogue_with_options_async(request, runtime)

    def collected_number_with_options(
        self,
        request: voice_navigator_20180612_models.CollectedNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.CollectedNumberResponse:
        """
        @param request: CollectedNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CollectedNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.additional_context):
            query['AdditionalContext'] = request.additional_context
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.CollectedNumberResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.CollectedNumberResponse(),
                self.execute(params, req, runtime)
            )

    async def collected_number_with_options_async(
        self,
        request: voice_navigator_20180612_models.CollectedNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.CollectedNumberResponse:
        """
        @param request: CollectedNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CollectedNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.additional_context):
            query['AdditionalContext'] = request.additional_context
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.CollectedNumberResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.CollectedNumberResponse(),
                await self.execute_async(params, req, runtime)
            )

    def collected_number(
        self,
        request: voice_navigator_20180612_models.CollectedNumberRequest,
    ) -> voice_navigator_20180612_models.CollectedNumberResponse:
        """
        @param request: CollectedNumberRequest
        @return: CollectedNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.collected_number_with_options(request, runtime)

    async def collected_number_async(
        self,
        request: voice_navigator_20180612_models.CollectedNumberRequest,
    ) -> voice_navigator_20180612_models.CollectedNumberResponse:
        """
        @param request: CollectedNumberRequest
        @return: CollectedNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.collected_number_with_options_async(request, runtime)

    def create_download_url_with_options(
        self,
        request: voice_navigator_20180612_models.CreateDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.CreateDownloadUrlResponse:
        """
        @param request: CreateDownloadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDownloadUrlResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.CreateDownloadUrlResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.CreateDownloadUrlResponse(),
                self.execute(params, req, runtime)
            )

    async def create_download_url_with_options_async(
        self,
        request: voice_navigator_20180612_models.CreateDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.CreateDownloadUrlResponse:
        """
        @param request: CreateDownloadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDownloadUrlResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.CreateDownloadUrlResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.CreateDownloadUrlResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_download_url(
        self,
        request: voice_navigator_20180612_models.CreateDownloadUrlRequest,
    ) -> voice_navigator_20180612_models.CreateDownloadUrlResponse:
        """
        @param request: CreateDownloadUrlRequest
        @return: CreateDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_download_url_with_options(request, runtime)

    async def create_download_url_async(
        self,
        request: voice_navigator_20180612_models.CreateDownloadUrlRequest,
    ) -> voice_navigator_20180612_models.CreateDownloadUrlResponse:
        """
        @param request: CreateDownloadUrlRequest
        @return: CreateDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_download_url_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: voice_navigator_20180612_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.CreateInstanceResponse:
        """
        @param request: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.concurrency):
            query['Concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.nlu_service_params_json):
            query['NluServiceParamsJson'] = request.nlu_service_params_json
        if not UtilClient.is_unset(request.union_instance_id):
            query['UnionInstanceId'] = request.union_instance_id
        if not UtilClient.is_unset(request.union_source):
            query['UnionSource'] = request.union_source
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.CreateInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.CreateInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def create_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.CreateInstanceResponse:
        """
        @param request: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.concurrency):
            query['Concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.nlu_service_params_json):
            query['NluServiceParamsJson'] = request.nlu_service_params_json
        if not UtilClient.is_unset(request.union_instance_id):
            query['UnionInstanceId'] = request.union_instance_id
        if not UtilClient.is_unset(request.union_source):
            query['UnionSource'] = request.union_source
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.CreateInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.CreateInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_instance(
        self,
        request: voice_navigator_20180612_models.CreateInstanceRequest,
    ) -> voice_navigator_20180612_models.CreateInstanceResponse:
        """
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: voice_navigator_20180612_models.CreateInstanceRequest,
    ) -> voice_navigator_20180612_models.CreateInstanceResponse:
        """
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def debug_begin_dialogue_with_options(
        self,
        request: voice_navigator_20180612_models.DebugBeginDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DebugBeginDialogueResponse:
        """
        @param request: DebugBeginDialogueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DebugBeginDialogueResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DebugBeginDialogueResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DebugBeginDialogueResponse(),
                self.execute(params, req, runtime)
            )

    async def debug_begin_dialogue_with_options_async(
        self,
        request: voice_navigator_20180612_models.DebugBeginDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DebugBeginDialogueResponse:
        """
        @param request: DebugBeginDialogueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DebugBeginDialogueResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DebugBeginDialogueResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DebugBeginDialogueResponse(),
                await self.execute_async(params, req, runtime)
            )

    def debug_begin_dialogue(
        self,
        request: voice_navigator_20180612_models.DebugBeginDialogueRequest,
    ) -> voice_navigator_20180612_models.DebugBeginDialogueResponse:
        """
        @param request: DebugBeginDialogueRequest
        @return: DebugBeginDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.debug_begin_dialogue_with_options(request, runtime)

    async def debug_begin_dialogue_async(
        self,
        request: voice_navigator_20180612_models.DebugBeginDialogueRequest,
    ) -> voice_navigator_20180612_models.DebugBeginDialogueResponse:
        """
        @param request: DebugBeginDialogueRequest
        @return: DebugBeginDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.debug_begin_dialogue_with_options_async(request, runtime)

    def debug_collected_number_with_options(
        self,
        request: voice_navigator_20180612_models.DebugCollectedNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DebugCollectedNumberResponse:
        """
        @param request: DebugCollectedNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DebugCollectedNumberResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DebugCollectedNumberResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DebugCollectedNumberResponse(),
                self.execute(params, req, runtime)
            )

    async def debug_collected_number_with_options_async(
        self,
        request: voice_navigator_20180612_models.DebugCollectedNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DebugCollectedNumberResponse:
        """
        @param request: DebugCollectedNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DebugCollectedNumberResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DebugCollectedNumberResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DebugCollectedNumberResponse(),
                await self.execute_async(params, req, runtime)
            )

    def debug_collected_number(
        self,
        request: voice_navigator_20180612_models.DebugCollectedNumberRequest,
    ) -> voice_navigator_20180612_models.DebugCollectedNumberResponse:
        """
        @param request: DebugCollectedNumberRequest
        @return: DebugCollectedNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.debug_collected_number_with_options(request, runtime)

    async def debug_collected_number_async(
        self,
        request: voice_navigator_20180612_models.DebugCollectedNumberRequest,
    ) -> voice_navigator_20180612_models.DebugCollectedNumberResponse:
        """
        @param request: DebugCollectedNumberRequest
        @return: DebugCollectedNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.debug_collected_number_with_options_async(request, runtime)

    def debug_dialogue_with_options(
        self,
        request: voice_navigator_20180612_models.DebugDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DebugDialogueResponse:
        """
        @param request: DebugDialogueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DebugDialogueResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DebugDialogueResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DebugDialogueResponse(),
                self.execute(params, req, runtime)
            )

    async def debug_dialogue_with_options_async(
        self,
        request: voice_navigator_20180612_models.DebugDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DebugDialogueResponse:
        """
        @param request: DebugDialogueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DebugDialogueResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DebugDialogueResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DebugDialogueResponse(),
                await self.execute_async(params, req, runtime)
            )

    def debug_dialogue(
        self,
        request: voice_navigator_20180612_models.DebugDialogueRequest,
    ) -> voice_navigator_20180612_models.DebugDialogueResponse:
        """
        @param request: DebugDialogueRequest
        @return: DebugDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.debug_dialogue_with_options(request, runtime)

    async def debug_dialogue_async(
        self,
        request: voice_navigator_20180612_models.DebugDialogueRequest,
    ) -> voice_navigator_20180612_models.DebugDialogueResponse:
        """
        @param request: DebugDialogueRequest
        @return: DebugDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.debug_dialogue_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: voice_navigator_20180612_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DeleteInstanceResponse:
        """
        @param request: DeleteInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DeleteInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DeleteInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DeleteInstanceResponse:
        """
        @param request: DeleteInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DeleteInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DeleteInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_instance(
        self,
        request: voice_navigator_20180612_models.DeleteInstanceRequest,
    ) -> voice_navigator_20180612_models.DeleteInstanceResponse:
        """
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: voice_navigator_20180612_models.DeleteInstanceRequest,
    ) -> voice_navigator_20180612_models.DeleteInstanceResponse:
        """
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def describe_conversation_with_options(
        self,
        request: voice_navigator_20180612_models.DescribeConversationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeConversationResponse:
        """
        @param request: DescribeConversationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConversationResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeConversationResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeConversationResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_conversation_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeConversationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeConversationResponse:
        """
        @param request: DescribeConversationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConversationResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeConversationResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeConversationResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_conversation(
        self,
        request: voice_navigator_20180612_models.DescribeConversationRequest,
    ) -> voice_navigator_20180612_models.DescribeConversationResponse:
        """
        @param request: DescribeConversationRequest
        @return: DescribeConversationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_conversation_with_options(request, runtime)

    async def describe_conversation_async(
        self,
        request: voice_navigator_20180612_models.DescribeConversationRequest,
    ) -> voice_navigator_20180612_models.DescribeConversationResponse:
        """
        @param request: DescribeConversationRequest
        @return: DescribeConversationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_conversation_with_options_async(request, runtime)

    def describe_conversation_context_with_options(
        self,
        request: voice_navigator_20180612_models.DescribeConversationContextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeConversationContextResponse:
        """
        @param request: DescribeConversationContextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConversationContextResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeConversationContextResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeConversationContextResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_conversation_context_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeConversationContextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeConversationContextResponse:
        """
        @param request: DescribeConversationContextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConversationContextResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeConversationContextResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeConversationContextResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_conversation_context(
        self,
        request: voice_navigator_20180612_models.DescribeConversationContextRequest,
    ) -> voice_navigator_20180612_models.DescribeConversationContextResponse:
        """
        @param request: DescribeConversationContextRequest
        @return: DescribeConversationContextResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_conversation_context_with_options(request, runtime)

    async def describe_conversation_context_async(
        self,
        request: voice_navigator_20180612_models.DescribeConversationContextRequest,
    ) -> voice_navigator_20180612_models.DescribeConversationContextResponse:
        """
        @param request: DescribeConversationContextRequest
        @return: DescribeConversationContextResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_conversation_context_with_options_async(request, runtime)

    def describe_export_progress_with_options(
        self,
        request: voice_navigator_20180612_models.DescribeExportProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeExportProgressResponse:
        """
        @param request: DescribeExportProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExportProgressResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeExportProgressResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeExportProgressResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_export_progress_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeExportProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeExportProgressResponse:
        """
        @param request: DescribeExportProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExportProgressResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeExportProgressResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeExportProgressResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_export_progress(
        self,
        request: voice_navigator_20180612_models.DescribeExportProgressRequest,
    ) -> voice_navigator_20180612_models.DescribeExportProgressResponse:
        """
        @param request: DescribeExportProgressRequest
        @return: DescribeExportProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_export_progress_with_options(request, runtime)

    async def describe_export_progress_async(
        self,
        request: voice_navigator_20180612_models.DescribeExportProgressRequest,
    ) -> voice_navigator_20180612_models.DescribeExportProgressResponse:
        """
        @param request: DescribeExportProgressRequest
        @return: DescribeExportProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_export_progress_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: voice_navigator_20180612_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeInstanceResponse:
        """
        @param request: DescribeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeInstanceResponse:
        """
        @param request: DescribeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instance(
        self,
        request: voice_navigator_20180612_models.DescribeInstanceRequest,
    ) -> voice_navigator_20180612_models.DescribeInstanceResponse:
        """
        @param request: DescribeInstanceRequest
        @return: DescribeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: voice_navigator_20180612_models.DescribeInstanceRequest,
    ) -> voice_navigator_20180612_models.DescribeInstanceResponse:
        """
        @param request: DescribeInstanceRequest
        @return: DescribeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_navigation_config_with_options(
        self,
        request: voice_navigator_20180612_models.DescribeNavigationConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeNavigationConfigResponse:
        """
        @param request: DescribeNavigationConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNavigationConfigResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeNavigationConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeNavigationConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_navigation_config_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeNavigationConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeNavigationConfigResponse:
        """
        @param request: DescribeNavigationConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNavigationConfigResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeNavigationConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeNavigationConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_navigation_config(
        self,
        request: voice_navigator_20180612_models.DescribeNavigationConfigRequest,
    ) -> voice_navigator_20180612_models.DescribeNavigationConfigResponse:
        """
        @param request: DescribeNavigationConfigRequest
        @return: DescribeNavigationConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_navigation_config_with_options(request, runtime)

    async def describe_navigation_config_async(
        self,
        request: voice_navigator_20180612_models.DescribeNavigationConfigRequest,
    ) -> voice_navigator_20180612_models.DescribeNavigationConfigResponse:
        """
        @param request: DescribeNavigationConfigRequest
        @return: DescribeNavigationConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_navigation_config_with_options_async(request, runtime)

    def describe_recording_with_options(
        self,
        request: voice_navigator_20180612_models.DescribeRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeRecordingResponse:
        """
        @param request: DescribeRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecordingResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeRecordingResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeRecordingResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_recording_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeRecordingResponse:
        """
        @param request: DescribeRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecordingResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeRecordingResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeRecordingResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_recording(
        self,
        request: voice_navigator_20180612_models.DescribeRecordingRequest,
    ) -> voice_navigator_20180612_models.DescribeRecordingResponse:
        """
        @param request: DescribeRecordingRequest
        @return: DescribeRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_recording_with_options(request, runtime)

    async def describe_recording_async(
        self,
        request: voice_navigator_20180612_models.DescribeRecordingRequest,
    ) -> voice_navigator_20180612_models.DescribeRecordingResponse:
        """
        @param request: DescribeRecordingRequest
        @return: DescribeRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_recording_with_options_async(request, runtime)

    def describe_statistical_data_with_options(
        self,
        request: voice_navigator_20180612_models.DescribeStatisticalDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeStatisticalDataResponse:
        """
        @param request: DescribeStatisticalDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStatisticalDataResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeStatisticalDataResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeStatisticalDataResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_statistical_data_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeStatisticalDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeStatisticalDataResponse:
        """
        @param request: DescribeStatisticalDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStatisticalDataResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeStatisticalDataResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeStatisticalDataResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_statistical_data(
        self,
        request: voice_navigator_20180612_models.DescribeStatisticalDataRequest,
    ) -> voice_navigator_20180612_models.DescribeStatisticalDataResponse:
        """
        @param request: DescribeStatisticalDataRequest
        @return: DescribeStatisticalDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_statistical_data_with_options(request, runtime)

    async def describe_statistical_data_async(
        self,
        request: voice_navigator_20180612_models.DescribeStatisticalDataRequest,
    ) -> voice_navigator_20180612_models.DescribeStatisticalDataResponse:
        """
        @param request: DescribeStatisticalDataRequest
        @return: DescribeStatisticalDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_statistical_data_with_options_async(request, runtime)

    def describe_ttsconfig_with_options(
        self,
        request: voice_navigator_20180612_models.DescribeTTSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeTTSConfigResponse:
        """
        @summary 获取TTS配置
        
        @param request: DescribeTTSConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTTSConfigResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeTTSConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeTTSConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_ttsconfig_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeTTSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeTTSConfigResponse:
        """
        @summary 获取TTS配置
        
        @param request: DescribeTTSConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTTSConfigResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeTTSConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DescribeTTSConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_ttsconfig(
        self,
        request: voice_navigator_20180612_models.DescribeTTSConfigRequest,
    ) -> voice_navigator_20180612_models.DescribeTTSConfigResponse:
        """
        @summary 获取TTS配置
        
        @param request: DescribeTTSConfigRequest
        @return: DescribeTTSConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ttsconfig_with_options(request, runtime)

    async def describe_ttsconfig_async(
        self,
        request: voice_navigator_20180612_models.DescribeTTSConfigRequest,
    ) -> voice_navigator_20180612_models.DescribeTTSConfigResponse:
        """
        @summary 获取TTS配置
        
        @param request: DescribeTTSConfigRequest
        @return: DescribeTTSConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ttsconfig_with_options_async(request, runtime)

    def dialogue_with_options(
        self,
        request: voice_navigator_20180612_models.DialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DialogueResponse:
        """
        @param request: DialogueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DialogueResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DialogueResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DialogueResponse(),
                self.execute(params, req, runtime)
            )

    async def dialogue_with_options_async(
        self,
        request: voice_navigator_20180612_models.DialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DialogueResponse:
        """
        @param request: DialogueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DialogueResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DialogueResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DialogueResponse(),
                await self.execute_async(params, req, runtime)
            )

    def dialogue(
        self,
        request: voice_navigator_20180612_models.DialogueRequest,
    ) -> voice_navigator_20180612_models.DialogueResponse:
        """
        @param request: DialogueRequest
        @return: DialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dialogue_with_options(request, runtime)

    async def dialogue_async(
        self,
        request: voice_navigator_20180612_models.DialogueRequest,
    ) -> voice_navigator_20180612_models.DialogueResponse:
        """
        @param request: DialogueRequest
        @return: DialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dialogue_with_options_async(request, runtime)

    def disable_instance_with_options(
        self,
        request: voice_navigator_20180612_models.DisableInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DisableInstanceResponse:
        """
        @param request: DisableInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DisableInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DisableInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def disable_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.DisableInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DisableInstanceResponse:
        """
        @param request: DisableInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.DisableInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.DisableInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def disable_instance(
        self,
        request: voice_navigator_20180612_models.DisableInstanceRequest,
    ) -> voice_navigator_20180612_models.DisableInstanceResponse:
        """
        @param request: DisableInstanceRequest
        @return: DisableInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_instance_with_options(request, runtime)

    async def disable_instance_async(
        self,
        request: voice_navigator_20180612_models.DisableInstanceRequest,
    ) -> voice_navigator_20180612_models.DisableInstanceResponse:
        """
        @param request: DisableInstanceRequest
        @return: DisableInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_instance_with_options_async(request, runtime)

    def enable_instance_with_options(
        self,
        request: voice_navigator_20180612_models.EnableInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.EnableInstanceResponse:
        """
        @param request: EnableInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.EnableInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.EnableInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def enable_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.EnableInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.EnableInstanceResponse:
        """
        @param request: EnableInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.EnableInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.EnableInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def enable_instance(
        self,
        request: voice_navigator_20180612_models.EnableInstanceRequest,
    ) -> voice_navigator_20180612_models.EnableInstanceResponse:
        """
        @param request: EnableInstanceRequest
        @return: EnableInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_instance_with_options(request, runtime)

    async def enable_instance_async(
        self,
        request: voice_navigator_20180612_models.EnableInstanceRequest,
    ) -> voice_navigator_20180612_models.EnableInstanceResponse:
        """
        @param request: EnableInstanceRequest
        @return: EnableInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_instance_with_options_async(request, runtime)

    def end_dialogue_with_options(
        self,
        request: voice_navigator_20180612_models.EndDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.EndDialogueResponse:
        """
        @param request: EndDialogueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EndDialogueResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.EndDialogueResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.EndDialogueResponse(),
                self.execute(params, req, runtime)
            )

    async def end_dialogue_with_options_async(
        self,
        request: voice_navigator_20180612_models.EndDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.EndDialogueResponse:
        """
        @param request: EndDialogueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EndDialogueResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.EndDialogueResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.EndDialogueResponse(),
                await self.execute_async(params, req, runtime)
            )

    def end_dialogue(
        self,
        request: voice_navigator_20180612_models.EndDialogueRequest,
    ) -> voice_navigator_20180612_models.EndDialogueResponse:
        """
        @param request: EndDialogueRequest
        @return: EndDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.end_dialogue_with_options(request, runtime)

    async def end_dialogue_async(
        self,
        request: voice_navigator_20180612_models.EndDialogueRequest,
    ) -> voice_navigator_20180612_models.EndDialogueResponse:
        """
        @param request: EndDialogueRequest
        @return: EndDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.end_dialogue_with_options_async(request, runtime)

    def export_conversation_details_with_options(
        self,
        request: voice_navigator_20180612_models.ExportConversationDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ExportConversationDetailsResponse:
        """
        @param request: ExportConversationDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportConversationDetailsResponse
        """
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
        if not UtilClient.is_unset(request.result):
            query['Result'] = request.result
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ExportConversationDetailsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ExportConversationDetailsResponse(),
                self.execute(params, req, runtime)
            )

    async def export_conversation_details_with_options_async(
        self,
        request: voice_navigator_20180612_models.ExportConversationDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ExportConversationDetailsResponse:
        """
        @param request: ExportConversationDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportConversationDetailsResponse
        """
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
        if not UtilClient.is_unset(request.result):
            query['Result'] = request.result
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ExportConversationDetailsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ExportConversationDetailsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def export_conversation_details(
        self,
        request: voice_navigator_20180612_models.ExportConversationDetailsRequest,
    ) -> voice_navigator_20180612_models.ExportConversationDetailsResponse:
        """
        @param request: ExportConversationDetailsRequest
        @return: ExportConversationDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_conversation_details_with_options(request, runtime)

    async def export_conversation_details_async(
        self,
        request: voice_navigator_20180612_models.ExportConversationDetailsRequest,
    ) -> voice_navigator_20180612_models.ExportConversationDetailsResponse:
        """
        @param request: ExportConversationDetailsRequest
        @return: ExportConversationDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_conversation_details_with_options_async(request, runtime)

    def export_statistical_data_with_options(
        self,
        request: voice_navigator_20180612_models.ExportStatisticalDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ExportStatisticalDataResponse:
        """
        @param request: ExportStatisticalDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportStatisticalDataResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ExportStatisticalDataResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ExportStatisticalDataResponse(),
                self.execute(params, req, runtime)
            )

    async def export_statistical_data_with_options_async(
        self,
        request: voice_navigator_20180612_models.ExportStatisticalDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ExportStatisticalDataResponse:
        """
        @param request: ExportStatisticalDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportStatisticalDataResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ExportStatisticalDataResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ExportStatisticalDataResponse(),
                await self.execute_async(params, req, runtime)
            )

    def export_statistical_data(
        self,
        request: voice_navigator_20180612_models.ExportStatisticalDataRequest,
    ) -> voice_navigator_20180612_models.ExportStatisticalDataResponse:
        """
        @param request: ExportStatisticalDataRequest
        @return: ExportStatisticalDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_statistical_data_with_options(request, runtime)

    async def export_statistical_data_async(
        self,
        request: voice_navigator_20180612_models.ExportStatisticalDataRequest,
    ) -> voice_navigator_20180612_models.ExportStatisticalDataResponse:
        """
        @param request: ExportStatisticalDataRequest
        @return: ExportStatisticalDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_statistical_data_with_options_async(request, runtime)

    def generate_upload_url_with_options(
        self,
        request: voice_navigator_20180612_models.GenerateUploadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.GenerateUploadUrlResponse:
        """
        @param request: GenerateUploadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateUploadUrlResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.GenerateUploadUrlResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.GenerateUploadUrlResponse(),
                self.execute(params, req, runtime)
            )

    async def generate_upload_url_with_options_async(
        self,
        request: voice_navigator_20180612_models.GenerateUploadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.GenerateUploadUrlResponse:
        """
        @param request: GenerateUploadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateUploadUrlResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.GenerateUploadUrlResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.GenerateUploadUrlResponse(),
                await self.execute_async(params, req, runtime)
            )

    def generate_upload_url(
        self,
        request: voice_navigator_20180612_models.GenerateUploadUrlRequest,
    ) -> voice_navigator_20180612_models.GenerateUploadUrlResponse:
        """
        @param request: GenerateUploadUrlRequest
        @return: GenerateUploadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_upload_url_with_options(request, runtime)

    async def generate_upload_url_async(
        self,
        request: voice_navigator_20180612_models.GenerateUploadUrlRequest,
    ) -> voice_navigator_20180612_models.GenerateUploadUrlResponse:
        """
        @param request: GenerateUploadUrlRequest
        @return: GenerateUploadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_upload_url_with_options_async(request, runtime)

    def get_asr_config_with_options(
        self,
        request: voice_navigator_20180612_models.GetAsrConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.GetAsrConfigResponse:
        """
        @param request: GetAsrConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsrConfigResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.GetAsrConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.GetAsrConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def get_asr_config_with_options_async(
        self,
        request: voice_navigator_20180612_models.GetAsrConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.GetAsrConfigResponse:
        """
        @param request: GetAsrConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsrConfigResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.GetAsrConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.GetAsrConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_asr_config(
        self,
        request: voice_navigator_20180612_models.GetAsrConfigRequest,
    ) -> voice_navigator_20180612_models.GetAsrConfigResponse:
        """
        @param request: GetAsrConfigRequest
        @return: GetAsrConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_asr_config_with_options(request, runtime)

    async def get_asr_config_async(
        self,
        request: voice_navigator_20180612_models.GetAsrConfigRequest,
    ) -> voice_navigator_20180612_models.GetAsrConfigResponse:
        """
        @param request: GetAsrConfigRequest
        @return: GetAsrConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_asr_config_with_options_async(request, runtime)

    def get_real_time_concurrency_with_options(
        self,
        request: voice_navigator_20180612_models.GetRealTimeConcurrencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.GetRealTimeConcurrencyResponse:
        """
        @summary GetRealTimeConcurrency
        
        @param request: GetRealTimeConcurrencyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRealTimeConcurrencyResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.GetRealTimeConcurrencyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.GetRealTimeConcurrencyResponse(),
                self.execute(params, req, runtime)
            )

    async def get_real_time_concurrency_with_options_async(
        self,
        request: voice_navigator_20180612_models.GetRealTimeConcurrencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.GetRealTimeConcurrencyResponse:
        """
        @summary GetRealTimeConcurrency
        
        @param request: GetRealTimeConcurrencyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRealTimeConcurrencyResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.GetRealTimeConcurrencyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.GetRealTimeConcurrencyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_real_time_concurrency(
        self,
        request: voice_navigator_20180612_models.GetRealTimeConcurrencyRequest,
    ) -> voice_navigator_20180612_models.GetRealTimeConcurrencyResponse:
        """
        @summary GetRealTimeConcurrency
        
        @param request: GetRealTimeConcurrencyRequest
        @return: GetRealTimeConcurrencyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_real_time_concurrency_with_options(request, runtime)

    async def get_real_time_concurrency_async(
        self,
        request: voice_navigator_20180612_models.GetRealTimeConcurrencyRequest,
    ) -> voice_navigator_20180612_models.GetRealTimeConcurrencyResponse:
        """
        @summary GetRealTimeConcurrency
        
        @param request: GetRealTimeConcurrencyRequest
        @return: GetRealTimeConcurrencyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_real_time_concurrency_with_options_async(request, runtime)

    def list_chatbot_instances_with_options(
        self,
        request: voice_navigator_20180612_models.ListChatbotInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListChatbotInstancesResponse:
        """
        @param request: ListChatbotInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChatbotInstancesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ListChatbotInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ListChatbotInstancesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_chatbot_instances_with_options_async(
        self,
        request: voice_navigator_20180612_models.ListChatbotInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListChatbotInstancesResponse:
        """
        @param request: ListChatbotInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChatbotInstancesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ListChatbotInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ListChatbotInstancesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_chatbot_instances(
        self,
        request: voice_navigator_20180612_models.ListChatbotInstancesRequest,
    ) -> voice_navigator_20180612_models.ListChatbotInstancesResponse:
        """
        @param request: ListChatbotInstancesRequest
        @return: ListChatbotInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_chatbot_instances_with_options(request, runtime)

    async def list_chatbot_instances_async(
        self,
        request: voice_navigator_20180612_models.ListChatbotInstancesRequest,
    ) -> voice_navigator_20180612_models.ListChatbotInstancesResponse:
        """
        @param request: ListChatbotInstancesRequest
        @return: ListChatbotInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_chatbot_instances_with_options_async(request, runtime)

    def list_conversation_details_with_options(
        self,
        request: voice_navigator_20180612_models.ListConversationDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListConversationDetailsResponse:
        """
        @param request: ListConversationDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConversationDetailsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ListConversationDetailsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ListConversationDetailsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_conversation_details_with_options_async(
        self,
        request: voice_navigator_20180612_models.ListConversationDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListConversationDetailsResponse:
        """
        @param request: ListConversationDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConversationDetailsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ListConversationDetailsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ListConversationDetailsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_conversation_details(
        self,
        request: voice_navigator_20180612_models.ListConversationDetailsRequest,
    ) -> voice_navigator_20180612_models.ListConversationDetailsResponse:
        """
        @param request: ListConversationDetailsRequest
        @return: ListConversationDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_conversation_details_with_options(request, runtime)

    async def list_conversation_details_async(
        self,
        request: voice_navigator_20180612_models.ListConversationDetailsRequest,
    ) -> voice_navigator_20180612_models.ListConversationDetailsResponse:
        """
        @param request: ListConversationDetailsRequest
        @return: ListConversationDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_conversation_details_with_options_async(request, runtime)

    def list_conversations_with_options(
        self,
        request: voice_navigator_20180612_models.ListConversationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListConversationsResponse:
        """
        @param request: ListConversationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConversationsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ListConversationsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ListConversationsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_conversations_with_options_async(
        self,
        request: voice_navigator_20180612_models.ListConversationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListConversationsResponse:
        """
        @param request: ListConversationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConversationsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ListConversationsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ListConversationsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_conversations(
        self,
        request: voice_navigator_20180612_models.ListConversationsRequest,
    ) -> voice_navigator_20180612_models.ListConversationsResponse:
        """
        @param request: ListConversationsRequest
        @return: ListConversationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_conversations_with_options(request, runtime)

    async def list_conversations_async(
        self,
        request: voice_navigator_20180612_models.ListConversationsRequest,
    ) -> voice_navigator_20180612_models.ListConversationsResponse:
        """
        @param request: ListConversationsRequest
        @return: ListConversationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_conversations_with_options_async(request, runtime)

    def list_download_tasks_with_options(
        self,
        request: voice_navigator_20180612_models.ListDownloadTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListDownloadTasksResponse:
        """
        @summary 下载列表
        
        @param request: ListDownloadTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDownloadTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDownloadTasks',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ListDownloadTasksResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ListDownloadTasksResponse(),
                self.execute(params, req, runtime)
            )

    async def list_download_tasks_with_options_async(
        self,
        request: voice_navigator_20180612_models.ListDownloadTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListDownloadTasksResponse:
        """
        @summary 下载列表
        
        @param request: ListDownloadTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDownloadTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDownloadTasks',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ListDownloadTasksResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ListDownloadTasksResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_download_tasks(
        self,
        request: voice_navigator_20180612_models.ListDownloadTasksRequest,
    ) -> voice_navigator_20180612_models.ListDownloadTasksResponse:
        """
        @summary 下载列表
        
        @param request: ListDownloadTasksRequest
        @return: ListDownloadTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_download_tasks_with_options(request, runtime)

    async def list_download_tasks_async(
        self,
        request: voice_navigator_20180612_models.ListDownloadTasksRequest,
    ) -> voice_navigator_20180612_models.ListDownloadTasksResponse:
        """
        @summary 下载列表
        
        @param request: ListDownloadTasksRequest
        @return: ListDownloadTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_download_tasks_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: voice_navigator_20180612_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListInstancesResponse:
        """
        @param request: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ListInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ListInstancesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_instances_with_options_async(
        self,
        request: voice_navigator_20180612_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListInstancesResponse:
        """
        @param request: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ListInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ListInstancesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_instances(
        self,
        request: voice_navigator_20180612_models.ListInstancesRequest,
    ) -> voice_navigator_20180612_models.ListInstancesResponse:
        """
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: voice_navigator_20180612_models.ListInstancesRequest,
    ) -> voice_navigator_20180612_models.ListInstancesResponse:
        """
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def modify_asr_config_with_options(
        self,
        request: voice_navigator_20180612_models.ModifyAsrConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyAsrConfigResponse:
        """
        @param request: ModifyAsrConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAsrConfigResponse
        """
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
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifyAsrConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifyAsrConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_asr_config_with_options_async(
        self,
        request: voice_navigator_20180612_models.ModifyAsrConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyAsrConfigResponse:
        """
        @param request: ModifyAsrConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAsrConfigResponse
        """
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
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifyAsrConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifyAsrConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_asr_config(
        self,
        request: voice_navigator_20180612_models.ModifyAsrConfigRequest,
    ) -> voice_navigator_20180612_models.ModifyAsrConfigResponse:
        """
        @param request: ModifyAsrConfigRequest
        @return: ModifyAsrConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_asr_config_with_options(request, runtime)

    async def modify_asr_config_async(
        self,
        request: voice_navigator_20180612_models.ModifyAsrConfigRequest,
    ) -> voice_navigator_20180612_models.ModifyAsrConfigResponse:
        """
        @param request: ModifyAsrConfigRequest
        @return: ModifyAsrConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_asr_config_with_options_async(request, runtime)

    def modify_greeting_config_with_options(
        self,
        request: voice_navigator_20180612_models.ModifyGreetingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyGreetingConfigResponse:
        """
        @param request: ModifyGreetingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGreetingConfigResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifyGreetingConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifyGreetingConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_greeting_config_with_options_async(
        self,
        request: voice_navigator_20180612_models.ModifyGreetingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyGreetingConfigResponse:
        """
        @param request: ModifyGreetingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGreetingConfigResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifyGreetingConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifyGreetingConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_greeting_config(
        self,
        request: voice_navigator_20180612_models.ModifyGreetingConfigRequest,
    ) -> voice_navigator_20180612_models.ModifyGreetingConfigResponse:
        """
        @param request: ModifyGreetingConfigRequest
        @return: ModifyGreetingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_greeting_config_with_options(request, runtime)

    async def modify_greeting_config_async(
        self,
        request: voice_navigator_20180612_models.ModifyGreetingConfigRequest,
    ) -> voice_navigator_20180612_models.ModifyGreetingConfigResponse:
        """
        @param request: ModifyGreetingConfigRequest
        @return: ModifyGreetingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_greeting_config_with_options_async(request, runtime)

    def modify_instance_with_options(
        self,
        request: voice_navigator_20180612_models.ModifyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyInstanceResponse:
        """
        @param request: ModifyInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifyInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifyInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.ModifyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyInstanceResponse:
        """
        @param request: ModifyInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifyInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifyInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_instance(
        self,
        request: voice_navigator_20180612_models.ModifyInstanceRequest,
    ) -> voice_navigator_20180612_models.ModifyInstanceResponse:
        """
        @param request: ModifyInstanceRequest
        @return: ModifyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_with_options(request, runtime)

    async def modify_instance_async(
        self,
        request: voice_navigator_20180612_models.ModifyInstanceRequest,
    ) -> voice_navigator_20180612_models.ModifyInstanceResponse:
        """
        @param request: ModifyInstanceRequest
        @return: ModifyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_with_options_async(request, runtime)

    def modify_silence_timeout_config_with_options(
        self,
        request: voice_navigator_20180612_models.ModifySilenceTimeoutConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifySilenceTimeoutConfigResponse:
        """
        @param request: ModifySilenceTimeoutConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySilenceTimeoutConfigResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifySilenceTimeoutConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifySilenceTimeoutConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_silence_timeout_config_with_options_async(
        self,
        request: voice_navigator_20180612_models.ModifySilenceTimeoutConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifySilenceTimeoutConfigResponse:
        """
        @param request: ModifySilenceTimeoutConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySilenceTimeoutConfigResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifySilenceTimeoutConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifySilenceTimeoutConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_silence_timeout_config(
        self,
        request: voice_navigator_20180612_models.ModifySilenceTimeoutConfigRequest,
    ) -> voice_navigator_20180612_models.ModifySilenceTimeoutConfigResponse:
        """
        @param request: ModifySilenceTimeoutConfigRequest
        @return: ModifySilenceTimeoutConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_silence_timeout_config_with_options(request, runtime)

    async def modify_silence_timeout_config_async(
        self,
        request: voice_navigator_20180612_models.ModifySilenceTimeoutConfigRequest,
    ) -> voice_navigator_20180612_models.ModifySilenceTimeoutConfigResponse:
        """
        @param request: ModifySilenceTimeoutConfigRequest
        @return: ModifySilenceTimeoutConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_silence_timeout_config_with_options_async(request, runtime)

    def modify_ttsconfig_with_options(
        self,
        request: voice_navigator_20180612_models.ModifyTTSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyTTSConfigResponse:
        """
        @summary 修改TTS配置
        
        @param request: ModifyTTSConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTTSConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_customized_voice):
            query['AliCustomizedVoice'] = request.ali_customized_voice
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_xunfei):
            query['EngineXunfei'] = request.engine_xunfei
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifyTTSConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifyTTSConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_ttsconfig_with_options_async(
        self,
        request: voice_navigator_20180612_models.ModifyTTSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyTTSConfigResponse:
        """
        @summary 修改TTS配置
        
        @param request: ModifyTTSConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTTSConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_customized_voice):
            query['AliCustomizedVoice'] = request.ali_customized_voice
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_xunfei):
            query['EngineXunfei'] = request.engine_xunfei
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifyTTSConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifyTTSConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_ttsconfig(
        self,
        request: voice_navigator_20180612_models.ModifyTTSConfigRequest,
    ) -> voice_navigator_20180612_models.ModifyTTSConfigResponse:
        """
        @summary 修改TTS配置
        
        @param request: ModifyTTSConfigRequest
        @return: ModifyTTSConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_ttsconfig_with_options(request, runtime)

    async def modify_ttsconfig_async(
        self,
        request: voice_navigator_20180612_models.ModifyTTSConfigRequest,
    ) -> voice_navigator_20180612_models.ModifyTTSConfigResponse:
        """
        @summary 修改TTS配置
        
        @param request: ModifyTTSConfigRequest
        @return: ModifyTTSConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_ttsconfig_with_options_async(request, runtime)

    def modify_unrecognizing_config_with_options(
        self,
        request: voice_navigator_20180612_models.ModifyUnrecognizingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyUnrecognizingConfigResponse:
        """
        @param request: ModifyUnrecognizingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUnrecognizingConfigResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifyUnrecognizingConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifyUnrecognizingConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_unrecognizing_config_with_options_async(
        self,
        request: voice_navigator_20180612_models.ModifyUnrecognizingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyUnrecognizingConfigResponse:
        """
        @param request: ModifyUnrecognizingConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUnrecognizingConfigResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifyUnrecognizingConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.ModifyUnrecognizingConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_unrecognizing_config(
        self,
        request: voice_navigator_20180612_models.ModifyUnrecognizingConfigRequest,
    ) -> voice_navigator_20180612_models.ModifyUnrecognizingConfigResponse:
        """
        @param request: ModifyUnrecognizingConfigRequest
        @return: ModifyUnrecognizingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_unrecognizing_config_with_options(request, runtime)

    async def modify_unrecognizing_config_async(
        self,
        request: voice_navigator_20180612_models.ModifyUnrecognizingConfigRequest,
    ) -> voice_navigator_20180612_models.ModifyUnrecognizingConfigResponse:
        """
        @param request: ModifyUnrecognizingConfigRequest
        @return: ModifyUnrecognizingConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_unrecognizing_config_with_options_async(request, runtime)

    def query_conversations_with_options(
        self,
        request: voice_navigator_20180612_models.QueryConversationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.QueryConversationsResponse:
        """
        @param request: QueryConversationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryConversationsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.QueryConversationsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.QueryConversationsResponse(),
                self.execute(params, req, runtime)
            )

    async def query_conversations_with_options_async(
        self,
        request: voice_navigator_20180612_models.QueryConversationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.QueryConversationsResponse:
        """
        @param request: QueryConversationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryConversationsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.QueryConversationsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.QueryConversationsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_conversations(
        self,
        request: voice_navigator_20180612_models.QueryConversationsRequest,
    ) -> voice_navigator_20180612_models.QueryConversationsResponse:
        """
        @param request: QueryConversationsRequest
        @return: QueryConversationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_conversations_with_options(request, runtime)

    async def query_conversations_async(
        self,
        request: voice_navigator_20180612_models.QueryConversationsRequest,
    ) -> voice_navigator_20180612_models.QueryConversationsResponse:
        """
        @param request: QueryConversationsRequest
        @return: QueryConversationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_conversations_with_options_async(request, runtime)

    def save_recording_with_options(
        self,
        request: voice_navigator_20180612_models.SaveRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.SaveRecordingResponse:
        """
        @param request: SaveRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveRecordingResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.SaveRecordingResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.SaveRecordingResponse(),
                self.execute(params, req, runtime)
            )

    async def save_recording_with_options_async(
        self,
        request: voice_navigator_20180612_models.SaveRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.SaveRecordingResponse:
        """
        @param request: SaveRecordingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveRecordingResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.SaveRecordingResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.SaveRecordingResponse(),
                await self.execute_async(params, req, runtime)
            )

    def save_recording(
        self,
        request: voice_navigator_20180612_models.SaveRecordingRequest,
    ) -> voice_navigator_20180612_models.SaveRecordingResponse:
        """
        @param request: SaveRecordingRequest
        @return: SaveRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_recording_with_options(request, runtime)

    async def save_recording_async(
        self,
        request: voice_navigator_20180612_models.SaveRecordingRequest,
    ) -> voice_navigator_20180612_models.SaveRecordingResponse:
        """
        @param request: SaveRecordingRequest
        @return: SaveRecordingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_recording_with_options_async(request, runtime)

    def silence_timeout_with_options(
        self,
        request: voice_navigator_20180612_models.SilenceTimeoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.SilenceTimeoutResponse:
        """
        @param request: SilenceTimeoutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SilenceTimeoutResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.SilenceTimeoutResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.SilenceTimeoutResponse(),
                self.execute(params, req, runtime)
            )

    async def silence_timeout_with_options_async(
        self,
        request: voice_navigator_20180612_models.SilenceTimeoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.SilenceTimeoutResponse:
        """
        @param request: SilenceTimeoutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SilenceTimeoutResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                voice_navigator_20180612_models.SilenceTimeoutResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                voice_navigator_20180612_models.SilenceTimeoutResponse(),
                await self.execute_async(params, req, runtime)
            )

    def silence_timeout(
        self,
        request: voice_navigator_20180612_models.SilenceTimeoutRequest,
    ) -> voice_navigator_20180612_models.SilenceTimeoutResponse:
        """
        @param request: SilenceTimeoutRequest
        @return: SilenceTimeoutResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.silence_timeout_with_options(request, runtime)

    async def silence_timeout_async(
        self,
        request: voice_navigator_20180612_models.SilenceTimeoutRequest,
    ) -> voice_navigator_20180612_models.SilenceTimeoutResponse:
        """
        @param request: SilenceTimeoutRequest
        @return: SilenceTimeoutResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.silence_timeout_with_options_async(request, runtime)
