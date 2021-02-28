# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_chatbot20171011 import models as chatbot_20171011_models
from alibabacloud_tea_util import models as util_models


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
        self._endpoint = self.get_endpoint('chatbot', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def activate_perspective_with_options(
        self,
        request: chatbot_20171011_models.ActivatePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ActivatePerspectiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ActivatePerspectiveResponse().from_map(
            self.do_rpcrequest('ActivatePerspective', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def activate_perspective_with_options_async(
        self,
        request: chatbot_20171011_models.ActivatePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ActivatePerspectiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ActivatePerspectiveResponse().from_map(
            await self.do_rpcrequest_async('ActivatePerspective', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def activate_perspective(
        self,
        request: chatbot_20171011_models.ActivatePerspectiveRequest,
    ) -> chatbot_20171011_models.ActivatePerspectiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.activate_perspective_with_options(request, runtime)

    async def activate_perspective_async(
        self,
        request: chatbot_20171011_models.ActivatePerspectiveRequest,
    ) -> chatbot_20171011_models.ActivatePerspectiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.activate_perspective_with_options_async(request, runtime)

    def add_synonym_with_options(
        self,
        request: chatbot_20171011_models.AddSynonymRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.AddSynonymResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.AddSynonymResponse().from_map(
            self.do_rpcrequest('AddSynonym', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_synonym_with_options_async(
        self,
        request: chatbot_20171011_models.AddSynonymRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.AddSynonymResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.AddSynonymResponse().from_map(
            await self.do_rpcrequest_async('AddSynonym', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_synonym(
        self,
        request: chatbot_20171011_models.AddSynonymRequest,
    ) -> chatbot_20171011_models.AddSynonymResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_synonym_with_options(request, runtime)

    async def add_synonym_async(
        self,
        request: chatbot_20171011_models.AddSynonymRequest,
    ) -> chatbot_20171011_models.AddSynonymResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_synonym_with_options_async(request, runtime)

    def append_entity_member_with_options(
        self,
        request: chatbot_20171011_models.AppendEntityMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.AppendEntityMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.AppendEntityMemberResponse().from_map(
            self.do_rpcrequest('AppendEntityMember', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def append_entity_member_with_options_async(
        self,
        request: chatbot_20171011_models.AppendEntityMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.AppendEntityMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.AppendEntityMemberResponse().from_map(
            await self.do_rpcrequest_async('AppendEntityMember', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def append_entity_member(
        self,
        request: chatbot_20171011_models.AppendEntityMemberRequest,
    ) -> chatbot_20171011_models.AppendEntityMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.append_entity_member_with_options(request, runtime)

    async def append_entity_member_async(
        self,
        request: chatbot_20171011_models.AppendEntityMemberRequest,
    ) -> chatbot_20171011_models.AppendEntityMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.append_entity_member_with_options_async(request, runtime)

    def associate_with_options(
        self,
        request: chatbot_20171011_models.AssociateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.AssociateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.AssociateResponse().from_map(
            self.do_rpcrequest('Associate', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_with_options_async(
        self,
        request: chatbot_20171011_models.AssociateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.AssociateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.AssociateResponse().from_map(
            await self.do_rpcrequest_async('Associate', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate(
        self,
        request: chatbot_20171011_models.AssociateRequest,
    ) -> chatbot_20171011_models.AssociateResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_with_options(request, runtime)

    async def associate_async(
        self,
        request: chatbot_20171011_models.AssociateRequest,
    ) -> chatbot_20171011_models.AssociateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_with_options_async(request, runtime)

    def chat_with_options(
        self,
        request: chatbot_20171011_models.ChatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ChatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ChatResponse().from_map(
            self.do_rpcrequest('Chat', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def chat_with_options_async(
        self,
        request: chatbot_20171011_models.ChatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ChatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ChatResponse().from_map(
            await self.do_rpcrequest_async('Chat', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def chat(
        self,
        request: chatbot_20171011_models.ChatRequest,
    ) -> chatbot_20171011_models.ChatResponse:
        runtime = util_models.RuntimeOptions()
        return self.chat_with_options(request, runtime)

    async def chat_async(
        self,
        request: chatbot_20171011_models.ChatRequest,
    ) -> chatbot_20171011_models.ChatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.chat_with_options_async(request, runtime)

    def create_bot_with_options(
        self,
        request: chatbot_20171011_models.CreateBotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateBotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.CreateBotResponse().from_map(
            self.do_rpcrequest('CreateBot', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_bot_with_options_async(
        self,
        request: chatbot_20171011_models.CreateBotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateBotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.CreateBotResponse().from_map(
            await self.do_rpcrequest_async('CreateBot', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_bot(
        self,
        request: chatbot_20171011_models.CreateBotRequest,
    ) -> chatbot_20171011_models.CreateBotResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_bot_with_options(request, runtime)

    async def create_bot_async(
        self,
        request: chatbot_20171011_models.CreateBotRequest,
    ) -> chatbot_20171011_models.CreateBotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_bot_with_options_async(request, runtime)

    def create_category_with_options(
        self,
        request: chatbot_20171011_models.CreateCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.CreateCategoryResponse().from_map(
            self.do_rpcrequest('CreateCategory', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_category_with_options_async(
        self,
        request: chatbot_20171011_models.CreateCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.CreateCategoryResponse().from_map(
            await self.do_rpcrequest_async('CreateCategory', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_category(
        self,
        request: chatbot_20171011_models.CreateCategoryRequest,
    ) -> chatbot_20171011_models.CreateCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_category_with_options(request, runtime)

    async def create_category_async(
        self,
        request: chatbot_20171011_models.CreateCategoryRequest,
    ) -> chatbot_20171011_models.CreateCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_category_with_options_async(request, runtime)

    def create_core_word_with_options(
        self,
        request: chatbot_20171011_models.CreateCoreWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateCoreWordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.CreateCoreWordResponse().from_map(
            self.do_rpcrequest('CreateCoreWord', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_core_word_with_options_async(
        self,
        request: chatbot_20171011_models.CreateCoreWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateCoreWordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.CreateCoreWordResponse().from_map(
            await self.do_rpcrequest_async('CreateCoreWord', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_core_word(
        self,
        request: chatbot_20171011_models.CreateCoreWordRequest,
    ) -> chatbot_20171011_models.CreateCoreWordResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_core_word_with_options(request, runtime)

    async def create_core_word_async(
        self,
        request: chatbot_20171011_models.CreateCoreWordRequest,
    ) -> chatbot_20171011_models.CreateCoreWordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_core_word_with_options_async(request, runtime)

    def create_dialog_with_options(
        self,
        request: chatbot_20171011_models.CreateDialogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateDialogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.CreateDialogResponse().from_map(
            self.do_rpcrequest('CreateDialog', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dialog_with_options_async(
        self,
        request: chatbot_20171011_models.CreateDialogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateDialogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.CreateDialogResponse().from_map(
            await self.do_rpcrequest_async('CreateDialog', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dialog(
        self,
        request: chatbot_20171011_models.CreateDialogRequest,
    ) -> chatbot_20171011_models.CreateDialogResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dialog_with_options(request, runtime)

    async def create_dialog_async(
        self,
        request: chatbot_20171011_models.CreateDialogRequest,
    ) -> chatbot_20171011_models.CreateDialogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dialog_with_options_async(request, runtime)

    def create_entity_with_options(
        self,
        request: chatbot_20171011_models.CreateEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.CreateEntityResponse().from_map(
            self.do_rpcrequest('CreateEntity', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_entity_with_options_async(
        self,
        request: chatbot_20171011_models.CreateEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.CreateEntityResponse().from_map(
            await self.do_rpcrequest_async('CreateEntity', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_entity(
        self,
        request: chatbot_20171011_models.CreateEntityRequest,
    ) -> chatbot_20171011_models.CreateEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_entity_with_options(request, runtime)

    async def create_entity_async(
        self,
        request: chatbot_20171011_models.CreateEntityRequest,
    ) -> chatbot_20171011_models.CreateEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_entity_with_options_async(request, runtime)

    def create_intent_with_options(
        self,
        request: chatbot_20171011_models.CreateIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateIntentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.CreateIntentResponse().from_map(
            self.do_rpcrequest('CreateIntent', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_intent_with_options_async(
        self,
        request: chatbot_20171011_models.CreateIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateIntentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.CreateIntentResponse().from_map(
            await self.do_rpcrequest_async('CreateIntent', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_intent(
        self,
        request: chatbot_20171011_models.CreateIntentRequest,
    ) -> chatbot_20171011_models.CreateIntentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_intent_with_options(request, runtime)

    async def create_intent_async(
        self,
        request: chatbot_20171011_models.CreateIntentRequest,
    ) -> chatbot_20171011_models.CreateIntentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_intent_with_options_async(request, runtime)

    def create_knowledge_with_options(
        self,
        request: chatbot_20171011_models.CreateKnowledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateKnowledgeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.CreateKnowledgeResponse().from_map(
            self.do_rpcrequest('CreateKnowledge', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_knowledge_with_options_async(
        self,
        request: chatbot_20171011_models.CreateKnowledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateKnowledgeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.CreateKnowledgeResponse().from_map(
            await self.do_rpcrequest_async('CreateKnowledge', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_knowledge(
        self,
        request: chatbot_20171011_models.CreateKnowledgeRequest,
    ) -> chatbot_20171011_models.CreateKnowledgeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_knowledge_with_options(request, runtime)

    async def create_knowledge_async(
        self,
        request: chatbot_20171011_models.CreateKnowledgeRequest,
    ) -> chatbot_20171011_models.CreateKnowledgeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_knowledge_with_options_async(request, runtime)

    def delete_bot_with_options(
        self,
        request: chatbot_20171011_models.DeleteBotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteBotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DeleteBotResponse().from_map(
            self.do_rpcrequest('DeleteBot', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_bot_with_options_async(
        self,
        request: chatbot_20171011_models.DeleteBotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteBotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DeleteBotResponse().from_map(
            await self.do_rpcrequest_async('DeleteBot', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_bot(
        self,
        request: chatbot_20171011_models.DeleteBotRequest,
    ) -> chatbot_20171011_models.DeleteBotResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_bot_with_options(request, runtime)

    async def delete_bot_async(
        self,
        request: chatbot_20171011_models.DeleteBotRequest,
    ) -> chatbot_20171011_models.DeleteBotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_bot_with_options_async(request, runtime)

    def delete_category_with_options(
        self,
        request: chatbot_20171011_models.DeleteCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DeleteCategoryResponse().from_map(
            self.do_rpcrequest('DeleteCategory', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_category_with_options_async(
        self,
        request: chatbot_20171011_models.DeleteCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DeleteCategoryResponse().from_map(
            await self.do_rpcrequest_async('DeleteCategory', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_category(
        self,
        request: chatbot_20171011_models.DeleteCategoryRequest,
    ) -> chatbot_20171011_models.DeleteCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_category_with_options(request, runtime)

    async def delete_category_async(
        self,
        request: chatbot_20171011_models.DeleteCategoryRequest,
    ) -> chatbot_20171011_models.DeleteCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_category_with_options_async(request, runtime)

    def delete_core_word_with_options(
        self,
        request: chatbot_20171011_models.DeleteCoreWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteCoreWordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DeleteCoreWordResponse().from_map(
            self.do_rpcrequest('DeleteCoreWord', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_core_word_with_options_async(
        self,
        request: chatbot_20171011_models.DeleteCoreWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteCoreWordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DeleteCoreWordResponse().from_map(
            await self.do_rpcrequest_async('DeleteCoreWord', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_core_word(
        self,
        request: chatbot_20171011_models.DeleteCoreWordRequest,
    ) -> chatbot_20171011_models.DeleteCoreWordResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_core_word_with_options(request, runtime)

    async def delete_core_word_async(
        self,
        request: chatbot_20171011_models.DeleteCoreWordRequest,
    ) -> chatbot_20171011_models.DeleteCoreWordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_core_word_with_options_async(request, runtime)

    def delete_dialog_with_options(
        self,
        request: chatbot_20171011_models.DeleteDialogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteDialogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DeleteDialogResponse().from_map(
            self.do_rpcrequest('DeleteDialog', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dialog_with_options_async(
        self,
        request: chatbot_20171011_models.DeleteDialogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteDialogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DeleteDialogResponse().from_map(
            await self.do_rpcrequest_async('DeleteDialog', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dialog(
        self,
        request: chatbot_20171011_models.DeleteDialogRequest,
    ) -> chatbot_20171011_models.DeleteDialogResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dialog_with_options(request, runtime)

    async def delete_dialog_async(
        self,
        request: chatbot_20171011_models.DeleteDialogRequest,
    ) -> chatbot_20171011_models.DeleteDialogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dialog_with_options_async(request, runtime)

    def delete_entity_with_options(
        self,
        request: chatbot_20171011_models.DeleteEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DeleteEntityResponse().from_map(
            self.do_rpcrequest('DeleteEntity', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_entity_with_options_async(
        self,
        request: chatbot_20171011_models.DeleteEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DeleteEntityResponse().from_map(
            await self.do_rpcrequest_async('DeleteEntity', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_entity(
        self,
        request: chatbot_20171011_models.DeleteEntityRequest,
    ) -> chatbot_20171011_models.DeleteEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_entity_with_options(request, runtime)

    async def delete_entity_async(
        self,
        request: chatbot_20171011_models.DeleteEntityRequest,
    ) -> chatbot_20171011_models.DeleteEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_entity_with_options_async(request, runtime)

    def delete_intent_with_options(
        self,
        request: chatbot_20171011_models.DeleteIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteIntentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DeleteIntentResponse().from_map(
            self.do_rpcrequest('DeleteIntent', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_intent_with_options_async(
        self,
        request: chatbot_20171011_models.DeleteIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteIntentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DeleteIntentResponse().from_map(
            await self.do_rpcrequest_async('DeleteIntent', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_intent(
        self,
        request: chatbot_20171011_models.DeleteIntentRequest,
    ) -> chatbot_20171011_models.DeleteIntentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_intent_with_options(request, runtime)

    async def delete_intent_async(
        self,
        request: chatbot_20171011_models.DeleteIntentRequest,
    ) -> chatbot_20171011_models.DeleteIntentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_intent_with_options_async(request, runtime)

    def delete_knowledge_with_options(
        self,
        request: chatbot_20171011_models.DeleteKnowledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteKnowledgeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DeleteKnowledgeResponse().from_map(
            self.do_rpcrequest('DeleteKnowledge', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_knowledge_with_options_async(
        self,
        request: chatbot_20171011_models.DeleteKnowledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteKnowledgeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DeleteKnowledgeResponse().from_map(
            await self.do_rpcrequest_async('DeleteKnowledge', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_knowledge(
        self,
        request: chatbot_20171011_models.DeleteKnowledgeRequest,
    ) -> chatbot_20171011_models.DeleteKnowledgeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_knowledge_with_options(request, runtime)

    async def delete_knowledge_async(
        self,
        request: chatbot_20171011_models.DeleteKnowledgeRequest,
    ) -> chatbot_20171011_models.DeleteKnowledgeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_knowledge_with_options_async(request, runtime)

    def describe_bot_with_options(
        self,
        request: chatbot_20171011_models.DescribeBotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeBotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DescribeBotResponse().from_map(
            self.do_rpcrequest('DescribeBot', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_bot_with_options_async(
        self,
        request: chatbot_20171011_models.DescribeBotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeBotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DescribeBotResponse().from_map(
            await self.do_rpcrequest_async('DescribeBot', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_bot(
        self,
        request: chatbot_20171011_models.DescribeBotRequest,
    ) -> chatbot_20171011_models.DescribeBotResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_bot_with_options(request, runtime)

    async def describe_bot_async(
        self,
        request: chatbot_20171011_models.DescribeBotRequest,
    ) -> chatbot_20171011_models.DescribeBotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_bot_with_options_async(request, runtime)

    def describe_category_with_options(
        self,
        request: chatbot_20171011_models.DescribeCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DescribeCategoryResponse().from_map(
            self.do_rpcrequest('DescribeCategory', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_category_with_options_async(
        self,
        request: chatbot_20171011_models.DescribeCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DescribeCategoryResponse().from_map(
            await self.do_rpcrequest_async('DescribeCategory', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_category(
        self,
        request: chatbot_20171011_models.DescribeCategoryRequest,
    ) -> chatbot_20171011_models.DescribeCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_category_with_options(request, runtime)

    async def describe_category_async(
        self,
        request: chatbot_20171011_models.DescribeCategoryRequest,
    ) -> chatbot_20171011_models.DescribeCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_category_with_options_async(request, runtime)

    def describe_core_word_with_options(
        self,
        request: chatbot_20171011_models.DescribeCoreWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeCoreWordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DescribeCoreWordResponse().from_map(
            self.do_rpcrequest('DescribeCoreWord', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_core_word_with_options_async(
        self,
        request: chatbot_20171011_models.DescribeCoreWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeCoreWordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DescribeCoreWordResponse().from_map(
            await self.do_rpcrequest_async('DescribeCoreWord', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_core_word(
        self,
        request: chatbot_20171011_models.DescribeCoreWordRequest,
    ) -> chatbot_20171011_models.DescribeCoreWordResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_core_word_with_options(request, runtime)

    async def describe_core_word_async(
        self,
        request: chatbot_20171011_models.DescribeCoreWordRequest,
    ) -> chatbot_20171011_models.DescribeCoreWordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_core_word_with_options_async(request, runtime)

    def describe_dialog_with_options(
        self,
        request: chatbot_20171011_models.DescribeDialogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeDialogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DescribeDialogResponse().from_map(
            self.do_rpcrequest('DescribeDialog', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dialog_with_options_async(
        self,
        request: chatbot_20171011_models.DescribeDialogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeDialogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DescribeDialogResponse().from_map(
            await self.do_rpcrequest_async('DescribeDialog', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dialog(
        self,
        request: chatbot_20171011_models.DescribeDialogRequest,
    ) -> chatbot_20171011_models.DescribeDialogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dialog_with_options(request, runtime)

    async def describe_dialog_async(
        self,
        request: chatbot_20171011_models.DescribeDialogRequest,
    ) -> chatbot_20171011_models.DescribeDialogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dialog_with_options_async(request, runtime)

    def describe_perspective_with_options(
        self,
        request: chatbot_20171011_models.DescribePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribePerspectiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DescribePerspectiveResponse().from_map(
            self.do_rpcrequest('DescribePerspective', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_perspective_with_options_async(
        self,
        request: chatbot_20171011_models.DescribePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribePerspectiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DescribePerspectiveResponse().from_map(
            await self.do_rpcrequest_async('DescribePerspective', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_perspective(
        self,
        request: chatbot_20171011_models.DescribePerspectiveRequest,
    ) -> chatbot_20171011_models.DescribePerspectiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_perspective_with_options(request, runtime)

    async def describe_perspective_async(
        self,
        request: chatbot_20171011_models.DescribePerspectiveRequest,
    ) -> chatbot_20171011_models.DescribePerspectiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_perspective_with_options_async(request, runtime)

    def disable_dialog_flow_with_options(
        self,
        request: chatbot_20171011_models.DisableDialogFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DisableDialogFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DisableDialogFlowResponse().from_map(
            self.do_rpcrequest('DisableDialogFlow', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_dialog_flow_with_options_async(
        self,
        request: chatbot_20171011_models.DisableDialogFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DisableDialogFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DisableDialogFlowResponse().from_map(
            await self.do_rpcrequest_async('DisableDialogFlow', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_dialog_flow(
        self,
        request: chatbot_20171011_models.DisableDialogFlowRequest,
    ) -> chatbot_20171011_models.DisableDialogFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_dialog_flow_with_options(request, runtime)

    async def disable_dialog_flow_async(
        self,
        request: chatbot_20171011_models.DisableDialogFlowRequest,
    ) -> chatbot_20171011_models.DisableDialogFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_dialog_flow_with_options_async(request, runtime)

    def disable_knowledge_with_options(
        self,
        request: chatbot_20171011_models.DisableKnowledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DisableKnowledgeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DisableKnowledgeResponse().from_map(
            self.do_rpcrequest('DisableKnowledge', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_knowledge_with_options_async(
        self,
        request: chatbot_20171011_models.DisableKnowledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DisableKnowledgeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.DisableKnowledgeResponse().from_map(
            await self.do_rpcrequest_async('DisableKnowledge', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_knowledge(
        self,
        request: chatbot_20171011_models.DisableKnowledgeRequest,
    ) -> chatbot_20171011_models.DisableKnowledgeResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_knowledge_with_options(request, runtime)

    async def disable_knowledge_async(
        self,
        request: chatbot_20171011_models.DisableKnowledgeRequest,
    ) -> chatbot_20171011_models.DisableKnowledgeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_knowledge_with_options_async(request, runtime)

    def feedback_with_options(
        self,
        request: chatbot_20171011_models.FeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.FeedbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.FeedbackResponse().from_map(
            self.do_rpcrequest('Feedback', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def feedback_with_options_async(
        self,
        request: chatbot_20171011_models.FeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.FeedbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.FeedbackResponse().from_map(
            await self.do_rpcrequest_async('Feedback', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def feedback(
        self,
        request: chatbot_20171011_models.FeedbackRequest,
    ) -> chatbot_20171011_models.FeedbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.feedback_with_options(request, runtime)

    async def feedback_async(
        self,
        request: chatbot_20171011_models.FeedbackRequest,
    ) -> chatbot_20171011_models.FeedbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.feedback_with_options_async(request, runtime)

    def get_bot_chat_data_with_options(
        self,
        request: chatbot_20171011_models.GetBotChatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.GetBotChatDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.GetBotChatDataResponse().from_map(
            self.do_rpcrequest('GetBotChatData', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_bot_chat_data_with_options_async(
        self,
        request: chatbot_20171011_models.GetBotChatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.GetBotChatDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.GetBotChatDataResponse().from_map(
            await self.do_rpcrequest_async('GetBotChatData', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_bot_chat_data(
        self,
        request: chatbot_20171011_models.GetBotChatDataRequest,
    ) -> chatbot_20171011_models.GetBotChatDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bot_chat_data_with_options(request, runtime)

    async def get_bot_chat_data_async(
        self,
        request: chatbot_20171011_models.GetBotChatDataRequest,
    ) -> chatbot_20171011_models.GetBotChatDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bot_chat_data_with_options_async(request, runtime)

    def get_bot_ds_stat_data_with_options(
        self,
        request: chatbot_20171011_models.GetBotDsStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.GetBotDsStatDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.GetBotDsStatDataResponse().from_map(
            self.do_rpcrequest('GetBotDsStatData', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_bot_ds_stat_data_with_options_async(
        self,
        request: chatbot_20171011_models.GetBotDsStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.GetBotDsStatDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.GetBotDsStatDataResponse().from_map(
            await self.do_rpcrequest_async('GetBotDsStatData', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_bot_ds_stat_data(
        self,
        request: chatbot_20171011_models.GetBotDsStatDataRequest,
    ) -> chatbot_20171011_models.GetBotDsStatDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bot_ds_stat_data_with_options(request, runtime)

    async def get_bot_ds_stat_data_async(
        self,
        request: chatbot_20171011_models.GetBotDsStatDataRequest,
    ) -> chatbot_20171011_models.GetBotDsStatDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bot_ds_stat_data_with_options_async(request, runtime)

    def get_bot_knowledge_stat_data_with_options(
        self,
        request: chatbot_20171011_models.GetBotKnowledgeStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.GetBotKnowledgeStatDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.GetBotKnowledgeStatDataResponse().from_map(
            self.do_rpcrequest('GetBotKnowledgeStatData', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_bot_knowledge_stat_data_with_options_async(
        self,
        request: chatbot_20171011_models.GetBotKnowledgeStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.GetBotKnowledgeStatDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.GetBotKnowledgeStatDataResponse().from_map(
            await self.do_rpcrequest_async('GetBotKnowledgeStatData', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_bot_knowledge_stat_data(
        self,
        request: chatbot_20171011_models.GetBotKnowledgeStatDataRequest,
    ) -> chatbot_20171011_models.GetBotKnowledgeStatDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bot_knowledge_stat_data_with_options(request, runtime)

    async def get_bot_knowledge_stat_data_async(
        self,
        request: chatbot_20171011_models.GetBotKnowledgeStatDataRequest,
    ) -> chatbot_20171011_models.GetBotKnowledgeStatDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bot_knowledge_stat_data_with_options_async(request, runtime)

    def get_bot_session_data_with_options(
        self,
        request: chatbot_20171011_models.GetBotSessionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.GetBotSessionDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.GetBotSessionDataResponse().from_map(
            self.do_rpcrequest('GetBotSessionData', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_bot_session_data_with_options_async(
        self,
        request: chatbot_20171011_models.GetBotSessionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.GetBotSessionDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.GetBotSessionDataResponse().from_map(
            await self.do_rpcrequest_async('GetBotSessionData', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_bot_session_data(
        self,
        request: chatbot_20171011_models.GetBotSessionDataRequest,
    ) -> chatbot_20171011_models.GetBotSessionDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bot_session_data_with_options(request, runtime)

    async def get_bot_session_data_async(
        self,
        request: chatbot_20171011_models.GetBotSessionDataRequest,
    ) -> chatbot_20171011_models.GetBotSessionDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bot_session_data_with_options_async(request, runtime)

    def get_conversation_list_with_options(
        self,
        request: chatbot_20171011_models.GetConversationListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.GetConversationListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.GetConversationListResponse().from_map(
            self.do_rpcrequest('GetConversationList', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_conversation_list_with_options_async(
        self,
        request: chatbot_20171011_models.GetConversationListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.GetConversationListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.GetConversationListResponse().from_map(
            await self.do_rpcrequest_async('GetConversationList', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_conversation_list(
        self,
        request: chatbot_20171011_models.GetConversationListRequest,
    ) -> chatbot_20171011_models.GetConversationListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_conversation_list_with_options(request, runtime)

    async def get_conversation_list_async(
        self,
        request: chatbot_20171011_models.GetConversationListRequest,
    ) -> chatbot_20171011_models.GetConversationListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_conversation_list_with_options_async(request, runtime)

    def list_bot_chat_historys_with_options(
        self,
        request: chatbot_20171011_models.ListBotChatHistorysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotChatHistorysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ListBotChatHistorysResponse().from_map(
            self.do_rpcrequest('ListBotChatHistorys', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_bot_chat_historys_with_options_async(
        self,
        request: chatbot_20171011_models.ListBotChatHistorysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotChatHistorysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ListBotChatHistorysResponse().from_map(
            await self.do_rpcrequest_async('ListBotChatHistorys', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bot_chat_historys(
        self,
        request: chatbot_20171011_models.ListBotChatHistorysRequest,
    ) -> chatbot_20171011_models.ListBotChatHistorysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_bot_chat_historys_with_options(request, runtime)

    async def list_bot_chat_historys_async(
        self,
        request: chatbot_20171011_models.ListBotChatHistorysRequest,
    ) -> chatbot_20171011_models.ListBotChatHistorysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_bot_chat_historys_with_options_async(request, runtime)

    def list_bot_cold_ds_datas_with_options(
        self,
        request: chatbot_20171011_models.ListBotColdDsDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotColdDsDatasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ListBotColdDsDatasResponse().from_map(
            self.do_rpcrequest('ListBotColdDsDatas', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_bot_cold_ds_datas_with_options_async(
        self,
        request: chatbot_20171011_models.ListBotColdDsDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotColdDsDatasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ListBotColdDsDatasResponse().from_map(
            await self.do_rpcrequest_async('ListBotColdDsDatas', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bot_cold_ds_datas(
        self,
        request: chatbot_20171011_models.ListBotColdDsDatasRequest,
    ) -> chatbot_20171011_models.ListBotColdDsDatasResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_bot_cold_ds_datas_with_options(request, runtime)

    async def list_bot_cold_ds_datas_async(
        self,
        request: chatbot_20171011_models.ListBotColdDsDatasRequest,
    ) -> chatbot_20171011_models.ListBotColdDsDatasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_bot_cold_ds_datas_with_options_async(request, runtime)

    def list_bot_cold_knowledges_with_options(
        self,
        request: chatbot_20171011_models.ListBotColdKnowledgesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotColdKnowledgesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ListBotColdKnowledgesResponse().from_map(
            self.do_rpcrequest('ListBotColdKnowledges', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_bot_cold_knowledges_with_options_async(
        self,
        request: chatbot_20171011_models.ListBotColdKnowledgesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotColdKnowledgesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ListBotColdKnowledgesResponse().from_map(
            await self.do_rpcrequest_async('ListBotColdKnowledges', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bot_cold_knowledges(
        self,
        request: chatbot_20171011_models.ListBotColdKnowledgesRequest,
    ) -> chatbot_20171011_models.ListBotColdKnowledgesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_bot_cold_knowledges_with_options(request, runtime)

    async def list_bot_cold_knowledges_async(
        self,
        request: chatbot_20171011_models.ListBotColdKnowledgesRequest,
    ) -> chatbot_20171011_models.ListBotColdKnowledgesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_bot_cold_knowledges_with_options_async(request, runtime)

    def list_bot_ds_details_with_options(
        self,
        request: chatbot_20171011_models.ListBotDsDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotDsDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ListBotDsDetailsResponse().from_map(
            self.do_rpcrequest('ListBotDsDetails', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_bot_ds_details_with_options_async(
        self,
        request: chatbot_20171011_models.ListBotDsDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotDsDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ListBotDsDetailsResponse().from_map(
            await self.do_rpcrequest_async('ListBotDsDetails', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bot_ds_details(
        self,
        request: chatbot_20171011_models.ListBotDsDetailsRequest,
    ) -> chatbot_20171011_models.ListBotDsDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_bot_ds_details_with_options(request, runtime)

    async def list_bot_ds_details_async(
        self,
        request: chatbot_20171011_models.ListBotDsDetailsRequest,
    ) -> chatbot_20171011_models.ListBotDsDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_bot_ds_details_with_options_async(request, runtime)

    def list_bot_hot_ds_datas_with_options(
        self,
        request: chatbot_20171011_models.ListBotHotDsDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotHotDsDatasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ListBotHotDsDatasResponse().from_map(
            self.do_rpcrequest('ListBotHotDsDatas', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_bot_hot_ds_datas_with_options_async(
        self,
        request: chatbot_20171011_models.ListBotHotDsDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotHotDsDatasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ListBotHotDsDatasResponse().from_map(
            await self.do_rpcrequest_async('ListBotHotDsDatas', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bot_hot_ds_datas(
        self,
        request: chatbot_20171011_models.ListBotHotDsDatasRequest,
    ) -> chatbot_20171011_models.ListBotHotDsDatasResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_bot_hot_ds_datas_with_options(request, runtime)

    async def list_bot_hot_ds_datas_async(
        self,
        request: chatbot_20171011_models.ListBotHotDsDatasRequest,
    ) -> chatbot_20171011_models.ListBotHotDsDatasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_bot_hot_ds_datas_with_options_async(request, runtime)

    def list_bot_hot_knowledges_with_options(
        self,
        request: chatbot_20171011_models.ListBotHotKnowledgesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotHotKnowledgesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ListBotHotKnowledgesResponse().from_map(
            self.do_rpcrequest('ListBotHotKnowledges', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_bot_hot_knowledges_with_options_async(
        self,
        request: chatbot_20171011_models.ListBotHotKnowledgesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotHotKnowledgesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ListBotHotKnowledgesResponse().from_map(
            await self.do_rpcrequest_async('ListBotHotKnowledges', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bot_hot_knowledges(
        self,
        request: chatbot_20171011_models.ListBotHotKnowledgesRequest,
    ) -> chatbot_20171011_models.ListBotHotKnowledgesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_bot_hot_knowledges_with_options(request, runtime)

    async def list_bot_hot_knowledges_async(
        self,
        request: chatbot_20171011_models.ListBotHotKnowledgesRequest,
    ) -> chatbot_20171011_models.ListBotHotKnowledgesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_bot_hot_knowledges_with_options_async(request, runtime)

    def list_bot_knowledge_details_with_options(
        self,
        request: chatbot_20171011_models.ListBotKnowledgeDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotKnowledgeDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ListBotKnowledgeDetailsResponse().from_map(
            self.do_rpcrequest('ListBotKnowledgeDetails', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_bot_knowledge_details_with_options_async(
        self,
        request: chatbot_20171011_models.ListBotKnowledgeDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotKnowledgeDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ListBotKnowledgeDetailsResponse().from_map(
            await self.do_rpcrequest_async('ListBotKnowledgeDetails', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bot_knowledge_details(
        self,
        request: chatbot_20171011_models.ListBotKnowledgeDetailsRequest,
    ) -> chatbot_20171011_models.ListBotKnowledgeDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_bot_knowledge_details_with_options(request, runtime)

    async def list_bot_knowledge_details_async(
        self,
        request: chatbot_20171011_models.ListBotKnowledgeDetailsRequest,
    ) -> chatbot_20171011_models.ListBotKnowledgeDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_bot_knowledge_details_with_options_async(request, runtime)

    def list_bot_reception_detail_datas_with_options(
        self,
        request: chatbot_20171011_models.ListBotReceptionDetailDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotReceptionDetailDatasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ListBotReceptionDetailDatasResponse().from_map(
            self.do_rpcrequest('ListBotReceptionDetailDatas', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_bot_reception_detail_datas_with_options_async(
        self,
        request: chatbot_20171011_models.ListBotReceptionDetailDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotReceptionDetailDatasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ListBotReceptionDetailDatasResponse().from_map(
            await self.do_rpcrequest_async('ListBotReceptionDetailDatas', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bot_reception_detail_datas(
        self,
        request: chatbot_20171011_models.ListBotReceptionDetailDatasRequest,
    ) -> chatbot_20171011_models.ListBotReceptionDetailDatasResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_bot_reception_detail_datas_with_options(request, runtime)

    async def list_bot_reception_detail_datas_async(
        self,
        request: chatbot_20171011_models.ListBotReceptionDetailDatasRequest,
    ) -> chatbot_20171011_models.ListBotReceptionDetailDatasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_bot_reception_detail_datas_with_options_async(request, runtime)

    def list_conversation_logs_with_options(
        self,
        request: chatbot_20171011_models.ListConversationLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListConversationLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ListConversationLogsResponse().from_map(
            self.do_rpcrequest('ListConversationLogs', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_conversation_logs_with_options_async(
        self,
        request: chatbot_20171011_models.ListConversationLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListConversationLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.ListConversationLogsResponse().from_map(
            await self.do_rpcrequest_async('ListConversationLogs', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_conversation_logs(
        self,
        request: chatbot_20171011_models.ListConversationLogsRequest,
    ) -> chatbot_20171011_models.ListConversationLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_conversation_logs_with_options(request, runtime)

    async def list_conversation_logs_async(
        self,
        request: chatbot_20171011_models.ListConversationLogsRequest,
    ) -> chatbot_20171011_models.ListConversationLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_conversation_logs_with_options_async(request, runtime)

    def move_knowledge_category_with_options(
        self,
        request: chatbot_20171011_models.MoveKnowledgeCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.MoveKnowledgeCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.MoveKnowledgeCategoryResponse().from_map(
            self.do_rpcrequest('MoveKnowledgeCategory', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def move_knowledge_category_with_options_async(
        self,
        request: chatbot_20171011_models.MoveKnowledgeCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.MoveKnowledgeCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.MoveKnowledgeCategoryResponse().from_map(
            await self.do_rpcrequest_async('MoveKnowledgeCategory', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_knowledge_category(
        self,
        request: chatbot_20171011_models.MoveKnowledgeCategoryRequest,
    ) -> chatbot_20171011_models.MoveKnowledgeCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_knowledge_category_with_options(request, runtime)

    async def move_knowledge_category_async(
        self,
        request: chatbot_20171011_models.MoveKnowledgeCategoryRequest,
    ) -> chatbot_20171011_models.MoveKnowledgeCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_knowledge_category_with_options_async(request, runtime)

    def publish_dialog_flow_with_options(
        self,
        request: chatbot_20171011_models.PublishDialogFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.PublishDialogFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.PublishDialogFlowResponse().from_map(
            self.do_rpcrequest('PublishDialogFlow', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_dialog_flow_with_options_async(
        self,
        request: chatbot_20171011_models.PublishDialogFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.PublishDialogFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.PublishDialogFlowResponse().from_map(
            await self.do_rpcrequest_async('PublishDialogFlow', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_dialog_flow(
        self,
        request: chatbot_20171011_models.PublishDialogFlowRequest,
    ) -> chatbot_20171011_models.PublishDialogFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_dialog_flow_with_options(request, runtime)

    async def publish_dialog_flow_async(
        self,
        request: chatbot_20171011_models.PublishDialogFlowRequest,
    ) -> chatbot_20171011_models.PublishDialogFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_dialog_flow_with_options_async(request, runtime)

    def publish_knowledge_with_options(
        self,
        request: chatbot_20171011_models.PublishKnowledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.PublishKnowledgeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.PublishKnowledgeResponse().from_map(
            self.do_rpcrequest('PublishKnowledge', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_knowledge_with_options_async(
        self,
        request: chatbot_20171011_models.PublishKnowledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.PublishKnowledgeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.PublishKnowledgeResponse().from_map(
            await self.do_rpcrequest_async('PublishKnowledge', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_knowledge(
        self,
        request: chatbot_20171011_models.PublishKnowledgeRequest,
    ) -> chatbot_20171011_models.PublishKnowledgeResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_knowledge_with_options(request, runtime)

    async def publish_knowledge_async(
        self,
        request: chatbot_20171011_models.PublishKnowledgeRequest,
    ) -> chatbot_20171011_models.PublishKnowledgeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_knowledge_with_options_async(request, runtime)

    def query_bots_with_options(
        self,
        request: chatbot_20171011_models.QueryBotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryBotsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.QueryBotsResponse().from_map(
            self.do_rpcrequest('QueryBots', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_bots_with_options_async(
        self,
        request: chatbot_20171011_models.QueryBotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryBotsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.QueryBotsResponse().from_map(
            await self.do_rpcrequest_async('QueryBots', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_bots(
        self,
        request: chatbot_20171011_models.QueryBotsRequest,
    ) -> chatbot_20171011_models.QueryBotsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_bots_with_options(request, runtime)

    async def query_bots_async(
        self,
        request: chatbot_20171011_models.QueryBotsRequest,
    ) -> chatbot_20171011_models.QueryBotsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_bots_with_options_async(request, runtime)

    def query_dialogs_with_options(
        self,
        request: chatbot_20171011_models.QueryDialogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryDialogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.QueryDialogsResponse().from_map(
            self.do_rpcrequest('QueryDialogs', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_dialogs_with_options_async(
        self,
        request: chatbot_20171011_models.QueryDialogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryDialogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.QueryDialogsResponse().from_map(
            await self.do_rpcrequest_async('QueryDialogs', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_dialogs(
        self,
        request: chatbot_20171011_models.QueryDialogsRequest,
    ) -> chatbot_20171011_models.QueryDialogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_dialogs_with_options(request, runtime)

    async def query_dialogs_async(
        self,
        request: chatbot_20171011_models.QueryDialogsRequest,
    ) -> chatbot_20171011_models.QueryDialogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_dialogs_with_options_async(request, runtime)

    def query_perspectives_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryPerspectivesResponse:
        req = open_api_models.OpenApiRequest()
        return chatbot_20171011_models.QueryPerspectivesResponse().from_map(
            self.do_rpcrequest('QueryPerspectives', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_perspectives_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryPerspectivesResponse:
        req = open_api_models.OpenApiRequest()
        return chatbot_20171011_models.QueryPerspectivesResponse().from_map(
            await self.do_rpcrequest_async('QueryPerspectives', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_perspectives(self) -> chatbot_20171011_models.QueryPerspectivesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_perspectives_with_options(runtime)

    async def query_perspectives_async(self) -> chatbot_20171011_models.QueryPerspectivesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_perspectives_with_options_async(runtime)

    def query_system_entities_with_options(
        self,
        request: chatbot_20171011_models.QuerySystemEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QuerySystemEntitiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.QuerySystemEntitiesResponse().from_map(
            self.do_rpcrequest('QuerySystemEntities', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_system_entities_with_options_async(
        self,
        request: chatbot_20171011_models.QuerySystemEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QuerySystemEntitiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.QuerySystemEntitiesResponse().from_map(
            await self.do_rpcrequest_async('QuerySystemEntities', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_system_entities(
        self,
        request: chatbot_20171011_models.QuerySystemEntitiesRequest,
    ) -> chatbot_20171011_models.QuerySystemEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_system_entities_with_options(request, runtime)

    async def query_system_entities_async(
        self,
        request: chatbot_20171011_models.QuerySystemEntitiesRequest,
    ) -> chatbot_20171011_models.QuerySystemEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_system_entities_with_options_async(request, runtime)

    def remove_entity_member_with_options(
        self,
        request: chatbot_20171011_models.RemoveEntityMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.RemoveEntityMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.RemoveEntityMemberResponse().from_map(
            self.do_rpcrequest('RemoveEntityMember', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_entity_member_with_options_async(
        self,
        request: chatbot_20171011_models.RemoveEntityMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.RemoveEntityMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.RemoveEntityMemberResponse().from_map(
            await self.do_rpcrequest_async('RemoveEntityMember', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_entity_member(
        self,
        request: chatbot_20171011_models.RemoveEntityMemberRequest,
    ) -> chatbot_20171011_models.RemoveEntityMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_entity_member_with_options(request, runtime)

    async def remove_entity_member_async(
        self,
        request: chatbot_20171011_models.RemoveEntityMemberRequest,
    ) -> chatbot_20171011_models.RemoveEntityMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_entity_member_with_options_async(request, runtime)

    def remove_synonym_with_options(
        self,
        request: chatbot_20171011_models.RemoveSynonymRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.RemoveSynonymResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.RemoveSynonymResponse().from_map(
            self.do_rpcrequest('RemoveSynonym', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_synonym_with_options_async(
        self,
        request: chatbot_20171011_models.RemoveSynonymRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.RemoveSynonymResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.RemoveSynonymResponse().from_map(
            await self.do_rpcrequest_async('RemoveSynonym', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_synonym(
        self,
        request: chatbot_20171011_models.RemoveSynonymRequest,
    ) -> chatbot_20171011_models.RemoveSynonymResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_synonym_with_options(request, runtime)

    async def remove_synonym_async(
        self,
        request: chatbot_20171011_models.RemoveSynonymRequest,
    ) -> chatbot_20171011_models.RemoveSynonymResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_synonym_with_options_async(request, runtime)

    def test_dialog_flow_with_options(
        self,
        request: chatbot_20171011_models.TestDialogFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.TestDialogFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.TestDialogFlowResponse().from_map(
            self.do_rpcrequest('TestDialogFlow', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def test_dialog_flow_with_options_async(
        self,
        request: chatbot_20171011_models.TestDialogFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.TestDialogFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.TestDialogFlowResponse().from_map(
            await self.do_rpcrequest_async('TestDialogFlow', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def test_dialog_flow(
        self,
        request: chatbot_20171011_models.TestDialogFlowRequest,
    ) -> chatbot_20171011_models.TestDialogFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.test_dialog_flow_with_options(request, runtime)

    async def test_dialog_flow_async(
        self,
        request: chatbot_20171011_models.TestDialogFlowRequest,
    ) -> chatbot_20171011_models.TestDialogFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.test_dialog_flow_with_options_async(request, runtime)

    def update_category_with_options(
        self,
        request: chatbot_20171011_models.UpdateCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.UpdateCategoryResponse().from_map(
            self.do_rpcrequest('UpdateCategory', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_category_with_options_async(
        self,
        request: chatbot_20171011_models.UpdateCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.UpdateCategoryResponse().from_map(
            await self.do_rpcrequest_async('UpdateCategory', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_category(
        self,
        request: chatbot_20171011_models.UpdateCategoryRequest,
    ) -> chatbot_20171011_models.UpdateCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_category_with_options(request, runtime)

    async def update_category_async(
        self,
        request: chatbot_20171011_models.UpdateCategoryRequest,
    ) -> chatbot_20171011_models.UpdateCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_category_with_options_async(request, runtime)

    def update_core_word_with_options(
        self,
        request: chatbot_20171011_models.UpdateCoreWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateCoreWordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.UpdateCoreWordResponse().from_map(
            self.do_rpcrequest('UpdateCoreWord', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_core_word_with_options_async(
        self,
        request: chatbot_20171011_models.UpdateCoreWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateCoreWordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.UpdateCoreWordResponse().from_map(
            await self.do_rpcrequest_async('UpdateCoreWord', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_core_word(
        self,
        request: chatbot_20171011_models.UpdateCoreWordRequest,
    ) -> chatbot_20171011_models.UpdateCoreWordResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_core_word_with_options(request, runtime)

    async def update_core_word_async(
        self,
        request: chatbot_20171011_models.UpdateCoreWordRequest,
    ) -> chatbot_20171011_models.UpdateCoreWordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_core_word_with_options_async(request, runtime)

    def update_dialog_with_options(
        self,
        request: chatbot_20171011_models.UpdateDialogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateDialogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.UpdateDialogResponse().from_map(
            self.do_rpcrequest('UpdateDialog', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_dialog_with_options_async(
        self,
        request: chatbot_20171011_models.UpdateDialogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateDialogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.UpdateDialogResponse().from_map(
            await self.do_rpcrequest_async('UpdateDialog', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_dialog(
        self,
        request: chatbot_20171011_models.UpdateDialogRequest,
    ) -> chatbot_20171011_models.UpdateDialogResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_dialog_with_options(request, runtime)

    async def update_dialog_async(
        self,
        request: chatbot_20171011_models.UpdateDialogRequest,
    ) -> chatbot_20171011_models.UpdateDialogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dialog_with_options_async(request, runtime)

    def update_dialog_flow_with_options(
        self,
        request: chatbot_20171011_models.UpdateDialogFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateDialogFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.UpdateDialogFlowResponse().from_map(
            self.do_rpcrequest('UpdateDialogFlow', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_dialog_flow_with_options_async(
        self,
        request: chatbot_20171011_models.UpdateDialogFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateDialogFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.UpdateDialogFlowResponse().from_map(
            await self.do_rpcrequest_async('UpdateDialogFlow', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_dialog_flow(
        self,
        request: chatbot_20171011_models.UpdateDialogFlowRequest,
    ) -> chatbot_20171011_models.UpdateDialogFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_dialog_flow_with_options(request, runtime)

    async def update_dialog_flow_async(
        self,
        request: chatbot_20171011_models.UpdateDialogFlowRequest,
    ) -> chatbot_20171011_models.UpdateDialogFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dialog_flow_with_options_async(request, runtime)

    def update_entity_with_options(
        self,
        request: chatbot_20171011_models.UpdateEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.UpdateEntityResponse().from_map(
            self.do_rpcrequest('UpdateEntity', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_entity_with_options_async(
        self,
        request: chatbot_20171011_models.UpdateEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.UpdateEntityResponse().from_map(
            await self.do_rpcrequest_async('UpdateEntity', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_entity(
        self,
        request: chatbot_20171011_models.UpdateEntityRequest,
    ) -> chatbot_20171011_models.UpdateEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_entity_with_options(request, runtime)

    async def update_entity_async(
        self,
        request: chatbot_20171011_models.UpdateEntityRequest,
    ) -> chatbot_20171011_models.UpdateEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_entity_with_options_async(request, runtime)

    def update_intent_with_options(
        self,
        request: chatbot_20171011_models.UpdateIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateIntentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.UpdateIntentResponse().from_map(
            self.do_rpcrequest('UpdateIntent', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_intent_with_options_async(
        self,
        request: chatbot_20171011_models.UpdateIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateIntentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.UpdateIntentResponse().from_map(
            await self.do_rpcrequest_async('UpdateIntent', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_intent(
        self,
        request: chatbot_20171011_models.UpdateIntentRequest,
    ) -> chatbot_20171011_models.UpdateIntentResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_intent_with_options(request, runtime)

    async def update_intent_async(
        self,
        request: chatbot_20171011_models.UpdateIntentRequest,
    ) -> chatbot_20171011_models.UpdateIntentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_intent_with_options_async(request, runtime)

    def update_knowledge_with_options(
        self,
        request: chatbot_20171011_models.UpdateKnowledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateKnowledgeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.UpdateKnowledgeResponse().from_map(
            self.do_rpcrequest('UpdateKnowledge', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_knowledge_with_options_async(
        self,
        request: chatbot_20171011_models.UpdateKnowledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateKnowledgeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.UpdateKnowledgeResponse().from_map(
            await self.do_rpcrequest_async('UpdateKnowledge', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_knowledge(
        self,
        request: chatbot_20171011_models.UpdateKnowledgeRequest,
    ) -> chatbot_20171011_models.UpdateKnowledgeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_knowledge_with_options(request, runtime)

    async def update_knowledge_async(
        self,
        request: chatbot_20171011_models.UpdateKnowledgeRequest,
    ) -> chatbot_20171011_models.UpdateKnowledgeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_knowledge_with_options_async(request, runtime)

    def update_perspective_with_options(
        self,
        request: chatbot_20171011_models.UpdatePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdatePerspectiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.UpdatePerspectiveResponse().from_map(
            self.do_rpcrequest('UpdatePerspective', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_perspective_with_options_async(
        self,
        request: chatbot_20171011_models.UpdatePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdatePerspectiveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return chatbot_20171011_models.UpdatePerspectiveResponse().from_map(
            await self.do_rpcrequest_async('UpdatePerspective', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_perspective(
        self,
        request: chatbot_20171011_models.UpdatePerspectiveRequest,
    ) -> chatbot_20171011_models.UpdatePerspectiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_perspective_with_options(request, runtime)

    async def update_perspective_async(
        self,
        request: chatbot_20171011_models.UpdatePerspectiveRequest,
    ) -> chatbot_20171011_models.UpdatePerspectiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_perspective_with_options_async(request, runtime)
