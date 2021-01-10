# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.AssociateChatbotInstanceResponse().from_map(
            self.do_rpcrequest('AssociateChatbotInstance', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_chatbot_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.AssociateChatbotInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.AssociateChatbotInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.AssociateChatbotInstanceResponse().from_map(
            await self.do_rpcrequest_async('AssociateChatbotInstance', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.AuditTTSVoiceResponse().from_map(
            self.do_rpcrequest('AuditTTSVoice', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def audit_ttsvoice_with_options_async(
        self,
        request: voice_navigator_20180612_models.AuditTTSVoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.AuditTTSVoiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.AuditTTSVoiceResponse().from_map(
            await self.do_rpcrequest_async('AuditTTSVoice', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.BeginDialogueResponse().from_map(
            self.do_rpcrequest('BeginDialogue', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def begin_dialogue_with_options_async(
        self,
        request: voice_navigator_20180612_models.BeginDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.BeginDialogueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.BeginDialogueResponse().from_map(
            await self.do_rpcrequest_async('BeginDialogue', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.CollectedNumberResponse().from_map(
            self.do_rpcrequest('CollectedNumber', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def collected_number_with_options_async(
        self,
        request: voice_navigator_20180612_models.CollectedNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.CollectedNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.CollectedNumberResponse().from_map(
            await self.do_rpcrequest_async('CollectedNumber', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_instance_with_options(
        self,
        request: voice_navigator_20180612_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.CreateInstanceResponse().from_map(
            self.do_rpcrequest('CreateInstance', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.CreateInstanceResponse().from_map(
            await self.do_rpcrequest_async('CreateInstance', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.DebugBeginDialogueResponse().from_map(
            self.do_rpcrequest('DebugBeginDialogue', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def debug_begin_dialogue_with_options_async(
        self,
        request: voice_navigator_20180612_models.DebugBeginDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DebugBeginDialogueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.DebugBeginDialogueResponse().from_map(
            await self.do_rpcrequest_async('DebugBeginDialogue', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.DebugCollectedNumberResponse().from_map(
            self.do_rpcrequest('DebugCollectedNumber', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def debug_collected_number_with_options_async(
        self,
        request: voice_navigator_20180612_models.DebugCollectedNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DebugCollectedNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.DebugCollectedNumberResponse().from_map(
            await self.do_rpcrequest_async('DebugCollectedNumber', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.DebugDialogueResponse().from_map(
            self.do_rpcrequest('DebugDialogue', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def debug_dialogue_with_options_async(
        self,
        request: voice_navigator_20180612_models.DebugDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DebugDialogueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.DebugDialogueResponse().from_map(
            await self.do_rpcrequest_async('DebugDialogue', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.DeleteInstanceResponse().from_map(
            self.do_rpcrequest('DeleteInstance', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.DeleteInstanceResponse().from_map(
            await self.do_rpcrequest_async('DeleteInstance', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return voice_navigator_20180612_models.DescribeConversationResponse().from_map(
            self.do_rpcrequest('DescribeConversation', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_conversation_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeConversationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeConversationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return voice_navigator_20180612_models.DescribeConversationResponse().from_map(
            await self.do_rpcrequest_async('DescribeConversation', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return voice_navigator_20180612_models.DescribeConversationContextResponse().from_map(
            self.do_rpcrequest('DescribeConversationContext', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_conversation_context_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeConversationContextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeConversationContextResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return voice_navigator_20180612_models.DescribeConversationContextResponse().from_map(
            await self.do_rpcrequest_async('DescribeConversationContext', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return voice_navigator_20180612_models.DescribeExportProgressResponse().from_map(
            self.do_rpcrequest('DescribeExportProgress', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_export_progress_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeExportProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeExportProgressResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return voice_navigator_20180612_models.DescribeExportProgressResponse().from_map(
            await self.do_rpcrequest_async('DescribeExportProgress', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return voice_navigator_20180612_models.DescribeInstanceResponse().from_map(
            self.do_rpcrequest('DescribeInstance', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return voice_navigator_20180612_models.DescribeInstanceResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstance', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return voice_navigator_20180612_models.DescribeNavigationConfigResponse().from_map(
            self.do_rpcrequest('DescribeNavigationConfig', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_navigation_config_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeNavigationConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeNavigationConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return voice_navigator_20180612_models.DescribeNavigationConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeNavigationConfig', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return voice_navigator_20180612_models.DescribeRecordingResponse().from_map(
            self.do_rpcrequest('DescribeRecording', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_recording_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeRecordingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return voice_navigator_20180612_models.DescribeRecordingResponse().from_map(
            await self.do_rpcrequest_async('DescribeRecording', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return voice_navigator_20180612_models.DescribeStatisticalDataResponse().from_map(
            self.do_rpcrequest('DescribeStatisticalData', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_statistical_data_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeStatisticalDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeStatisticalDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return voice_navigator_20180612_models.DescribeStatisticalDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeStatisticalData', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return voice_navigator_20180612_models.DescribeTTSConfigResponse().from_map(
            self.do_rpcrequest('DescribeTTSConfig', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_ttsconfig_with_options_async(
        self,
        request: voice_navigator_20180612_models.DescribeTTSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DescribeTTSConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return voice_navigator_20180612_models.DescribeTTSConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeTTSConfig', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.DialogueResponse().from_map(
            self.do_rpcrequest('Dialogue', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def dialogue_with_options_async(
        self,
        request: voice_navigator_20180612_models.DialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DialogueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.DialogueResponse().from_map(
            await self.do_rpcrequest_async('Dialogue', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.DisableInstanceResponse().from_map(
            self.do_rpcrequest('DisableInstance', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.DisableInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.DisableInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.DisableInstanceResponse().from_map(
            await self.do_rpcrequest_async('DisableInstance', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.EnableInstanceResponse().from_map(
            self.do_rpcrequest('EnableInstance', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.EnableInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.EnableInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.EnableInstanceResponse().from_map(
            await self.do_rpcrequest_async('EnableInstance', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.EndDialogueResponse().from_map(
            self.do_rpcrequest('EndDialogue', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def end_dialogue_with_options_async(
        self,
        request: voice_navigator_20180612_models.EndDialogueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.EndDialogueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.EndDialogueResponse().from_map(
            await self.do_rpcrequest_async('EndDialogue', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.ExportConversationDetailsResponse().from_map(
            self.do_rpcrequest('ExportConversationDetails', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def export_conversation_details_with_options_async(
        self,
        request: voice_navigator_20180612_models.ExportConversationDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ExportConversationDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.ExportConversationDetailsResponse().from_map(
            await self.do_rpcrequest_async('ExportConversationDetails', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.ExportStatisticalDataResponse().from_map(
            self.do_rpcrequest('ExportStatisticalData', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def export_statistical_data_with_options_async(
        self,
        request: voice_navigator_20180612_models.ExportStatisticalDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ExportStatisticalDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.ExportStatisticalDataResponse().from_map(
            await self.do_rpcrequest_async('ExportStatisticalData', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_chatbot_instances_with_options(
        self,
        request: voice_navigator_20180612_models.ListChatbotInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListChatbotInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return voice_navigator_20180612_models.ListChatbotInstancesResponse().from_map(
            self.do_rpcrequest('ListChatbotInstances', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_chatbot_instances_with_options_async(
        self,
        request: voice_navigator_20180612_models.ListChatbotInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListChatbotInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return voice_navigator_20180612_models.ListChatbotInstancesResponse().from_map(
            await self.do_rpcrequest_async('ListChatbotInstances', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return voice_navigator_20180612_models.ListConversationDetailsResponse().from_map(
            self.do_rpcrequest('ListConversationDetails', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_conversation_details_with_options_async(
        self,
        request: voice_navigator_20180612_models.ListConversationDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListConversationDetailsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return voice_navigator_20180612_models.ListConversationDetailsResponse().from_map(
            await self.do_rpcrequest_async('ListConversationDetails', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return voice_navigator_20180612_models.ListConversationsResponse().from_map(
            self.do_rpcrequest('ListConversations', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_conversations_with_options_async(
        self,
        request: voice_navigator_20180612_models.ListConversationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListConversationsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return voice_navigator_20180612_models.ListConversationsResponse().from_map(
            await self.do_rpcrequest_async('ListConversations', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def list_instances_with_options(
        self,
        request: voice_navigator_20180612_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return voice_navigator_20180612_models.ListInstancesResponse().from_map(
            self.do_rpcrequest('ListInstances', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: voice_navigator_20180612_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return voice_navigator_20180612_models.ListInstancesResponse().from_map(
            await self.do_rpcrequest_async('ListInstances', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def modify_greeting_config_with_options(
        self,
        request: voice_navigator_20180612_models.ModifyGreetingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyGreetingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.ModifyGreetingConfigResponse().from_map(
            self.do_rpcrequest('ModifyGreetingConfig', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_greeting_config_with_options_async(
        self,
        request: voice_navigator_20180612_models.ModifyGreetingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyGreetingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.ModifyGreetingConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyGreetingConfig', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.ModifyInstanceResponse().from_map(
            self.do_rpcrequest('ModifyInstance', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_with_options_async(
        self,
        request: voice_navigator_20180612_models.ModifyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.ModifyInstanceResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstance', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.ModifySilenceTimeoutConfigResponse().from_map(
            self.do_rpcrequest('ModifySilenceTimeoutConfig', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_silence_timeout_config_with_options_async(
        self,
        request: voice_navigator_20180612_models.ModifySilenceTimeoutConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifySilenceTimeoutConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.ModifySilenceTimeoutConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifySilenceTimeoutConfig', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.ModifyTTSConfigResponse().from_map(
            self.do_rpcrequest('ModifyTTSConfig', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ttsconfig_with_options_async(
        self,
        request: voice_navigator_20180612_models.ModifyTTSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyTTSConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.ModifyTTSConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyTTSConfig', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.ModifyUnrecognizingConfigResponse().from_map(
            self.do_rpcrequest('ModifyUnrecognizingConfig', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_unrecognizing_config_with_options_async(
        self,
        request: voice_navigator_20180612_models.ModifyUnrecognizingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.ModifyUnrecognizingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.ModifyUnrecognizingConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyUnrecognizingConfig', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return voice_navigator_20180612_models.QueryConversationsResponse().from_map(
            self.do_rpcrequest('QueryConversations', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def query_conversations_with_options_async(
        self,
        request: voice_navigator_20180612_models.QueryConversationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.QueryConversationsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return voice_navigator_20180612_models.QueryConversationsResponse().from_map(
            await self.do_rpcrequest_async('QueryConversations', '2018-06-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.SaveRecordingResponse().from_map(
            self.do_rpcrequest('SaveRecording', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_recording_with_options_async(
        self,
        request: voice_navigator_20180612_models.SaveRecordingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.SaveRecordingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.SaveRecordingResponse().from_map(
            await self.do_rpcrequest_async('SaveRecording', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.SilenceTimeoutResponse().from_map(
            self.do_rpcrequest('SilenceTimeout', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def silence_timeout_with_options_async(
        self,
        request: voice_navigator_20180612_models.SilenceTimeoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> voice_navigator_20180612_models.SilenceTimeoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return voice_navigator_20180612_models.SilenceTimeoutResponse().from_map(
            await self.do_rpcrequest_async('SilenceTimeout', '2018-06-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
