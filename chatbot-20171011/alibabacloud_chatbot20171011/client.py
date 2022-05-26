# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_chatbot20171011 import models as chatbot_20171011_models
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.perspective_id):
            query['PerspectiveId'] = request.perspective_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivatePerspective',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ActivatePerspectiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_perspective_with_options_async(
        self,
        request: chatbot_20171011_models.ActivatePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ActivatePerspectiveResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.perspective_id):
            query['PerspectiveId'] = request.perspective_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivatePerspective',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ActivatePerspectiveResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        if not UtilClient.is_unset(request.synonym):
            query['Synonym'] = request.synonym
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSynonym',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.AddSynonymResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_synonym_with_options_async(
        self,
        request: chatbot_20171011_models.AddSynonymRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.AddSynonymResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        if not UtilClient.is_unset(request.synonym):
            query['Synonym'] = request.synonym
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSynonym',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.AddSynonymResponse(),
            await self.call_api_async(params, req, runtime)
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
        tmp_req: chatbot_20171011_models.AppendEntityMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.AppendEntityMemberResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.AppendEntityMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.member):
            request.member_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.member), 'Member', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.apply_type):
            query['ApplyType'] = request.apply_type
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.member_shrink):
            query['Member'] = request.member_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AppendEntityMember',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.AppendEntityMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def append_entity_member_with_options_async(
        self,
        tmp_req: chatbot_20171011_models.AppendEntityMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.AppendEntityMemberResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.AppendEntityMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.member):
            request.member_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.member), 'Member', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.apply_type):
            query['ApplyType'] = request.apply_type
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.member_shrink):
            query['Member'] = request.member_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AppendEntityMember',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.AppendEntityMemberResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.perspective):
            query['Perspective'] = request.perspective
        if not UtilClient.is_unset(request.recommend_num):
            query['RecommendNum'] = request.recommend_num
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Associate',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.AssociateResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_with_options_async(
        self,
        request: chatbot_20171011_models.AssociateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.AssociateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.perspective):
            query['Perspective'] = request.perspective
        if not UtilClient.is_unset(request.recommend_num):
            query['RecommendNum'] = request.recommend_num
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Associate',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.AssociateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_name):
            query['IntentName'] = request.intent_name
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        if not UtilClient.is_unset(request.perspective):
            query['Perspective'] = request.perspective
        if not UtilClient.is_unset(request.sender_id):
            query['SenderId'] = request.sender_id
        if not UtilClient.is_unset(request.sender_nick):
            query['SenderNick'] = request.sender_nick
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.utterance):
            query['Utterance'] = request.utterance
        if not UtilClient.is_unset(request.vendor_param):
            query['VendorParam'] = request.vendor_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Chat',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_with_options_async(
        self,
        request: chatbot_20171011_models.ChatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ChatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_name):
            query['IntentName'] = request.intent_name
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        if not UtilClient.is_unset(request.perspective):
            query['Perspective'] = request.perspective
        if not UtilClient.is_unset(request.sender_id):
            query['SenderId'] = request.sender_id
        if not UtilClient.is_unset(request.sender_nick):
            query['SenderNick'] = request.sender_nick
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.utterance):
            query['Utterance'] = request.utterance
        if not UtilClient.is_unset(request.vendor_param):
            query['VendorParam'] = request.vendor_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Chat',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ChatResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.avatar):
            query['Avatar'] = request.avatar
        if not UtilClient.is_unset(request.introduction):
            query['Introduction'] = request.introduction
        if not UtilClient.is_unset(request.language_code):
            query['LanguageCode'] = request.language_code
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.robot_type):
            query['RobotType'] = request.robot_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBot',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateBotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_bot_with_options_async(
        self,
        request: chatbot_20171011_models.CreateBotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateBotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.avatar):
            query['Avatar'] = request.avatar
        if not UtilClient.is_unset(request.introduction):
            query['Introduction'] = request.introduction
        if not UtilClient.is_unset(request.language_code):
            query['LanguageCode'] = request.language_code
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.robot_type):
            query['RobotType'] = request.robot_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBot',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateBotResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.knowledge_type):
            query['KnowledgeType'] = request.knowledge_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parent_category_id):
            query['ParentCategoryId'] = request.parent_category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCategory',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_category_with_options_async(
        self,
        request: chatbot_20171011_models.CreateCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.knowledge_type):
            query['KnowledgeType'] = request.knowledge_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parent_category_id):
            query['ParentCategoryId'] = request.parent_category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCategory',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateCategoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCoreWord',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateCoreWordResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_core_word_with_options_async(
        self,
        request: chatbot_20171011_models.CreateCoreWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateCoreWordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCoreWord',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateCoreWordResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dialog_name):
            query['DialogName'] = request.dialog_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDialog',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateDialogResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dialog_with_options_async(
        self,
        request: chatbot_20171011_models.CreateDialogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateDialogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dialog_name):
            query['DialogName'] = request.dialog_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDialog',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateDialogResponse(),
            await self.call_api_async(params, req, runtime)
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
        tmp_req: chatbot_20171011_models.CreateEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateEntityResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.CreateEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not UtilClient.is_unset(request.entity_name):
            query['EntityName'] = request.entity_name
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.members_shrink):
            query['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.regex):
            query['Regex'] = request.regex
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEntity',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_entity_with_options_async(
        self,
        tmp_req: chatbot_20171011_models.CreateEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateEntityResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.CreateEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not UtilClient.is_unset(request.entity_name):
            query['EntityName'] = request.entity_name
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.members_shrink):
            query['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.regex):
            query['Regex'] = request.regex
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEntity',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateEntityResponse(),
            await self.call_api_async(params, req, runtime)
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
        tmp_req: chatbot_20171011_models.CreateIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateIntentResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.CreateIntentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_definition):
            request.intent_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.intent_definition), 'IntentDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not UtilClient.is_unset(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIntent',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_intent_with_options_async(
        self,
        tmp_req: chatbot_20171011_models.CreateIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateIntentResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.CreateIntentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_definition):
            request.intent_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.intent_definition), 'IntentDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not UtilClient.is_unset(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIntent',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateIntentResponse(),
            await self.call_api_async(params, req, runtime)
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
        tmp_req: chatbot_20171011_models.CreateKnowledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateKnowledgeResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.CreateKnowledgeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.knowledge):
            request.knowledge_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.knowledge), 'Knowledge', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.knowledge_shrink):
            body['Knowledge'] = request.knowledge_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateKnowledge',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateKnowledgeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_knowledge_with_options_async(
        self,
        tmp_req: chatbot_20171011_models.CreateKnowledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreateKnowledgeResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.CreateKnowledgeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.knowledge):
            request.knowledge_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.knowledge), 'Knowledge', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.knowledge_shrink):
            body['Knowledge'] = request.knowledge_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateKnowledge',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateKnowledgeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_perspective_with_options(
        self,
        request: chatbot_20171011_models.CreatePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreatePerspectiveResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePerspective',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreatePerspectiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_perspective_with_options_async(
        self,
        request: chatbot_20171011_models.CreatePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.CreatePerspectiveResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePerspective',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreatePerspectiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_perspective(
        self,
        request: chatbot_20171011_models.CreatePerspectiveRequest,
    ) -> chatbot_20171011_models.CreatePerspectiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_perspective_with_options(request, runtime)

    async def create_perspective_async(
        self,
        request: chatbot_20171011_models.CreatePerspectiveRequest,
    ) -> chatbot_20171011_models.CreatePerspectiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_perspective_with_options_async(request, runtime)

    def delete_bot_with_options(
        self,
        request: chatbot_20171011_models.DeleteBotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteBotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBot',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteBotResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_bot_with_options_async(
        self,
        request: chatbot_20171011_models.DeleteBotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteBotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBot',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteBotResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCategory',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_category_with_options_async(
        self,
        request: chatbot_20171011_models.DeleteCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCategory',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteCategoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCoreWord',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteCoreWordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_core_word_with_options_async(
        self,
        request: chatbot_20171011_models.DeleteCoreWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteCoreWordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCoreWord',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteCoreWordResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDialog',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteDialogResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dialog_with_options_async(
        self,
        request: chatbot_20171011_models.DeleteDialogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteDialogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDialog',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteDialogResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEntity',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_entity_with_options_async(
        self,
        request: chatbot_20171011_models.DeleteEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteEntityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEntity',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteEntityResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIntent',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_intent_with_options_async(
        self,
        request: chatbot_20171011_models.DeleteIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteIntentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIntent',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteIntentResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKnowledge',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteKnowledgeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_knowledge_with_options_async(
        self,
        request: chatbot_20171011_models.DeleteKnowledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeleteKnowledgeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKnowledge',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteKnowledgeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_perspective_with_options(
        self,
        request: chatbot_20171011_models.DeletePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeletePerspectiveResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.perspective_id):
            query['PerspectiveId'] = request.perspective_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePerspective',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeletePerspectiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_perspective_with_options_async(
        self,
        request: chatbot_20171011_models.DeletePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DeletePerspectiveResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.perspective_id):
            query['PerspectiveId'] = request.perspective_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePerspective',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeletePerspectiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_perspective(
        self,
        request: chatbot_20171011_models.DeletePerspectiveRequest,
    ) -> chatbot_20171011_models.DeletePerspectiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_perspective_with_options(request, runtime)

    async def delete_perspective_async(
        self,
        request: chatbot_20171011_models.DeletePerspectiveRequest,
    ) -> chatbot_20171011_models.DeletePerspectiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_perspective_with_options_async(request, runtime)

    def describe_bot_with_options(
        self,
        request: chatbot_20171011_models.DescribeBotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeBotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBot',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeBotResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_bot_with_options_async(
        self,
        request: chatbot_20171011_models.DescribeBotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeBotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBot',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeBotResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCategory',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_category_with_options_async(
        self,
        request: chatbot_20171011_models.DescribeCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCategory',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeCategoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCoreWord',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeCoreWordResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_core_word_with_options_async(
        self,
        request: chatbot_20171011_models.DescribeCoreWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeCoreWordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCoreWord',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeCoreWordResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDialog',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeDialogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dialog_with_options_async(
        self,
        request: chatbot_20171011_models.DescribeDialogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeDialogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDialog',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeDialogResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_dialog_flow_with_options(
        self,
        request: chatbot_20171011_models.DescribeDialogFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeDialogFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDialogFlow',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeDialogFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dialog_flow_with_options_async(
        self,
        request: chatbot_20171011_models.DescribeDialogFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeDialogFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDialogFlow',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeDialogFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dialog_flow(
        self,
        request: chatbot_20171011_models.DescribeDialogFlowRequest,
    ) -> chatbot_20171011_models.DescribeDialogFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dialog_flow_with_options(request, runtime)

    async def describe_dialog_flow_async(
        self,
        request: chatbot_20171011_models.DescribeDialogFlowRequest,
    ) -> chatbot_20171011_models.DescribeDialogFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dialog_flow_with_options_async(request, runtime)

    def describe_entities_with_options(
        self,
        request: chatbot_20171011_models.DescribeEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeEntitiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEntities',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_entities_with_options_async(
        self,
        request: chatbot_20171011_models.DescribeEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeEntitiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEntities',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_entities(
        self,
        request: chatbot_20171011_models.DescribeEntitiesRequest,
    ) -> chatbot_20171011_models.DescribeEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_entities_with_options(request, runtime)

    async def describe_entities_async(
        self,
        request: chatbot_20171011_models.DescribeEntitiesRequest,
    ) -> chatbot_20171011_models.DescribeEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_entities_with_options_async(request, runtime)

    def describe_intent_with_options(
        self,
        request: chatbot_20171011_models.DescribeIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeIntentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIntent',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_intent_with_options_async(
        self,
        request: chatbot_20171011_models.DescribeIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeIntentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIntent',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_intent(
        self,
        request: chatbot_20171011_models.DescribeIntentRequest,
    ) -> chatbot_20171011_models.DescribeIntentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_intent_with_options(request, runtime)

    async def describe_intent_async(
        self,
        request: chatbot_20171011_models.DescribeIntentRequest,
    ) -> chatbot_20171011_models.DescribeIntentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_intent_with_options_async(request, runtime)

    def describe_knowledge_with_options(
        self,
        request: chatbot_20171011_models.DescribeKnowledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeKnowledgeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKnowledge',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeKnowledgeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_knowledge_with_options_async(
        self,
        request: chatbot_20171011_models.DescribeKnowledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribeKnowledgeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKnowledge',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeKnowledgeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_knowledge(
        self,
        request: chatbot_20171011_models.DescribeKnowledgeRequest,
    ) -> chatbot_20171011_models.DescribeKnowledgeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_knowledge_with_options(request, runtime)

    async def describe_knowledge_async(
        self,
        request: chatbot_20171011_models.DescribeKnowledgeRequest,
    ) -> chatbot_20171011_models.DescribeKnowledgeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_knowledge_with_options_async(request, runtime)

    def describe_perspective_with_options(
        self,
        request: chatbot_20171011_models.DescribePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribePerspectiveResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.perspective_id):
            query['PerspectiveId'] = request.perspective_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePerspective',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribePerspectiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_perspective_with_options_async(
        self,
        request: chatbot_20171011_models.DescribePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DescribePerspectiveResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.perspective_id):
            query['PerspectiveId'] = request.perspective_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePerspective',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribePerspectiveResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDialogFlow',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DisableDialogFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_dialog_flow_with_options_async(
        self,
        request: chatbot_20171011_models.DisableDialogFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DisableDialogFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDialogFlow',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DisableDialogFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableKnowledge',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DisableKnowledgeResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_knowledge_with_options_async(
        self,
        request: chatbot_20171011_models.DisableKnowledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.DisableKnowledgeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableKnowledge',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DisableKnowledgeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Feedback',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.FeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def feedback_with_options_async(
        self,
        request: chatbot_20171011_models.FeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.FeedbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Feedback',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.FeedbackResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_async_result_with_options(
        self,
        request: chatbot_20171011_models.GetAsyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.GetAsyncResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncResult',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetAsyncResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_result_with_options_async(
        self,
        request: chatbot_20171011_models.GetAsyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.GetAsyncResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncResult',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetAsyncResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_result(
        self,
        request: chatbot_20171011_models.GetAsyncResultRequest,
    ) -> chatbot_20171011_models.GetAsyncResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_async_result_with_options(request, runtime)

    async def get_async_result_async(
        self,
        request: chatbot_20171011_models.GetAsyncResultRequest,
    ) -> chatbot_20171011_models.GetAsyncResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_async_result_with_options_async(request, runtime)

    def get_bot_chat_data_with_options(
        self,
        request: chatbot_20171011_models.GetBotChatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.GetBotChatDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBotChatData',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetBotChatDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bot_chat_data_with_options_async(
        self,
        request: chatbot_20171011_models.GetBotChatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.GetBotChatDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBotChatData',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetBotChatDataResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBotDsStatData',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetBotDsStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bot_ds_stat_data_with_options_async(
        self,
        request: chatbot_20171011_models.GetBotDsStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.GetBotDsStatDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBotDsStatData',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetBotDsStatDataResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBotKnowledgeStatData',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetBotKnowledgeStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bot_knowledge_stat_data_with_options_async(
        self,
        request: chatbot_20171011_models.GetBotKnowledgeStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.GetBotKnowledgeStatDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBotKnowledgeStatData',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetBotKnowledgeStatDataResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBotSessionData',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetBotSessionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bot_session_data_with_options_async(
        self,
        request: chatbot_20171011_models.GetBotSessionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.GetBotSessionDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBotSessionData',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetBotSessionDataResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sender_id):
            query['SenderId'] = request.sender_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConversationList',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetConversationListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_conversation_list_with_options_async(
        self,
        request: chatbot_20171011_models.GetConversationListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.GetConversationListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sender_id):
            query['SenderId'] = request.sender_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConversationList',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetConversationListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotChatHistorys',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotChatHistorysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bot_chat_historys_with_options_async(
        self,
        request: chatbot_20171011_models.ListBotChatHistorysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotChatHistorysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotChatHistorys',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotChatHistorysResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotColdDsDatas',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotColdDsDatasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bot_cold_ds_datas_with_options_async(
        self,
        request: chatbot_20171011_models.ListBotColdDsDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotColdDsDatasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotColdDsDatas',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotColdDsDatasResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotColdKnowledges',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotColdKnowledgesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bot_cold_knowledges_with_options_async(
        self,
        request: chatbot_20171011_models.ListBotColdKnowledgesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotColdKnowledgesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotColdKnowledges',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotColdKnowledgesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotDsDetails',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotDsDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bot_ds_details_with_options_async(
        self,
        request: chatbot_20171011_models.ListBotDsDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotDsDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotDsDetails',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotDsDetailsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotHotDsDatas',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotHotDsDatasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bot_hot_ds_datas_with_options_async(
        self,
        request: chatbot_20171011_models.ListBotHotDsDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotHotDsDatasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotHotDsDatas',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotHotDsDatasResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotHotKnowledges',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotHotKnowledgesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bot_hot_knowledges_with_options_async(
        self,
        request: chatbot_20171011_models.ListBotHotKnowledgesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotHotKnowledgesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotHotKnowledges',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotHotKnowledgesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotKnowledgeDetails',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotKnowledgeDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bot_knowledge_details_with_options_async(
        self,
        request: chatbot_20171011_models.ListBotKnowledgeDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotKnowledgeDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotKnowledgeDetails',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotKnowledgeDetailsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotReceptionDetailDatas',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotReceptionDetailDatasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bot_reception_detail_datas_with_options_async(
        self,
        request: chatbot_20171011_models.ListBotReceptionDetailDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListBotReceptionDetailDatasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotReceptionDetailDatas',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotReceptionDetailDatasResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConversationLogs',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListConversationLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_conversation_logs_with_options_async(
        self,
        request: chatbot_20171011_models.ListConversationLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.ListConversationLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConversationLogs',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListConversationLogsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveKnowledgeCategory',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.MoveKnowledgeCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_knowledge_category_with_options_async(
        self,
        request: chatbot_20171011_models.MoveKnowledgeCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.MoveKnowledgeCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveKnowledgeCategory',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.MoveKnowledgeCategoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishDialogFlow',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.PublishDialogFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_dialog_flow_with_options_async(
        self,
        request: chatbot_20171011_models.PublishDialogFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.PublishDialogFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishDialogFlow',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.PublishDialogFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishKnowledge',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.PublishKnowledgeResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_knowledge_with_options_async(
        self,
        request: chatbot_20171011_models.PublishKnowledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.PublishKnowledgeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishKnowledge',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.PublishKnowledgeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBots',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryBotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_bots_with_options_async(
        self,
        request: chatbot_20171011_models.QueryBotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryBotsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBots',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryBotsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_categories_with_options(
        self,
        request: chatbot_20171011_models.QueryCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryCategoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.knowledge_type):
            query['KnowledgeType'] = request.knowledge_type
        if not UtilClient.is_unset(request.parent_category_id):
            query['ParentCategoryId'] = request.parent_category_id
        if not UtilClient.is_unset(request.show_childrens):
            query['ShowChildrens'] = request.show_childrens
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCategories',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_categories_with_options_async(
        self,
        request: chatbot_20171011_models.QueryCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryCategoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.knowledge_type):
            query['KnowledgeType'] = request.knowledge_type
        if not UtilClient.is_unset(request.parent_category_id):
            query['ParentCategoryId'] = request.parent_category_id
        if not UtilClient.is_unset(request.show_childrens):
            query['ShowChildrens'] = request.show_childrens
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCategories',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_categories(
        self,
        request: chatbot_20171011_models.QueryCategoriesRequest,
    ) -> chatbot_20171011_models.QueryCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_categories_with_options(request, runtime)

    async def query_categories_async(
        self,
        request: chatbot_20171011_models.QueryCategoriesRequest,
    ) -> chatbot_20171011_models.QueryCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_categories_with_options_async(request, runtime)

    def query_core_words_with_options(
        self,
        request: chatbot_20171011_models.QueryCoreWordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryCoreWordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.synonym):
            query['Synonym'] = request.synonym
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCoreWords',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryCoreWordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_core_words_with_options_async(
        self,
        request: chatbot_20171011_models.QueryCoreWordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryCoreWordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.synonym):
            query['Synonym'] = request.synonym
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCoreWords',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryCoreWordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_core_words(
        self,
        request: chatbot_20171011_models.QueryCoreWordsRequest,
    ) -> chatbot_20171011_models.QueryCoreWordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_core_words_with_options(request, runtime)

    async def query_core_words_async(
        self,
        request: chatbot_20171011_models.QueryCoreWordsRequest,
    ) -> chatbot_20171011_models.QueryCoreWordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_core_words_with_options_async(request, runtime)

    def query_dialogs_with_options(
        self,
        request: chatbot_20171011_models.QueryDialogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryDialogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_name):
            query['DialogName'] = request.dialog_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDialogs',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryDialogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dialogs_with_options_async(
        self,
        request: chatbot_20171011_models.QueryDialogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryDialogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_name):
            query['DialogName'] = request.dialog_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDialogs',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryDialogsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_entities_with_options(
        self,
        request: chatbot_20171011_models.QueryEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryEntitiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not UtilClient.is_unset(request.entity_name):
            query['EntityName'] = request.entity_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEntities',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_entities_with_options_async(
        self,
        request: chatbot_20171011_models.QueryEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryEntitiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not UtilClient.is_unset(request.entity_name):
            query['EntityName'] = request.entity_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEntities',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_entities(
        self,
        request: chatbot_20171011_models.QueryEntitiesRequest,
    ) -> chatbot_20171011_models.QueryEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_entities_with_options(request, runtime)

    async def query_entities_async(
        self,
        request: chatbot_20171011_models.QueryEntitiesRequest,
    ) -> chatbot_20171011_models.QueryEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_entities_with_options_async(request, runtime)

    def query_intents_with_options(
        self,
        request: chatbot_20171011_models.QueryIntentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryIntentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_name):
            query['IntentName'] = request.intent_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryIntents',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryIntentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_intents_with_options_async(
        self,
        request: chatbot_20171011_models.QueryIntentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryIntentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_name):
            query['IntentName'] = request.intent_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryIntents',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryIntentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_intents(
        self,
        request: chatbot_20171011_models.QueryIntentsRequest,
    ) -> chatbot_20171011_models.QueryIntentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_intents_with_options(request, runtime)

    async def query_intents_async(
        self,
        request: chatbot_20171011_models.QueryIntentsRequest,
    ) -> chatbot_20171011_models.QueryIntentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_intents_with_options_async(request, runtime)

    def query_knowledges_with_options(
        self,
        request: chatbot_20171011_models.QueryKnowledgesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryKnowledgesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        if not UtilClient.is_unset(request.knowledge_title):
            query['KnowledgeTitle'] = request.knowledge_title
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryKnowledges',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryKnowledgesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_knowledges_with_options_async(
        self,
        request: chatbot_20171011_models.QueryKnowledgesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryKnowledgesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        if not UtilClient.is_unset(request.knowledge_title):
            query['KnowledgeTitle'] = request.knowledge_title
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryKnowledges',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryKnowledgesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_knowledges(
        self,
        request: chatbot_20171011_models.QueryKnowledgesRequest,
    ) -> chatbot_20171011_models.QueryKnowledgesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_knowledges_with_options(request, runtime)

    async def query_knowledges_async(
        self,
        request: chatbot_20171011_models.QueryKnowledgesRequest,
    ) -> chatbot_20171011_models.QueryKnowledgesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_knowledges_with_options_async(request, runtime)

    def query_perspectives_with_options(
        self,
        request: chatbot_20171011_models.QueryPerspectivesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryPerspectivesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPerspectives',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryPerspectivesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_perspectives_with_options_async(
        self,
        request: chatbot_20171011_models.QueryPerspectivesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QueryPerspectivesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPerspectives',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryPerspectivesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_perspectives(
        self,
        request: chatbot_20171011_models.QueryPerspectivesRequest,
    ) -> chatbot_20171011_models.QueryPerspectivesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_perspectives_with_options(request, runtime)

    async def query_perspectives_async(
        self,
        request: chatbot_20171011_models.QueryPerspectivesRequest,
    ) -> chatbot_20171011_models.QueryPerspectivesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_perspectives_with_options_async(request, runtime)

    def query_system_entities_with_options(
        self,
        request: chatbot_20171011_models.QuerySystemEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QuerySystemEntitiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_name):
            query['EntityName'] = request.entity_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySystemEntities',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QuerySystemEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_system_entities_with_options_async(
        self,
        request: chatbot_20171011_models.QuerySystemEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.QuerySystemEntitiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_name):
            query['EntityName'] = request.entity_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySystemEntities',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QuerySystemEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
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
        tmp_req: chatbot_20171011_models.RemoveEntityMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.RemoveEntityMemberResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.RemoveEntityMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.member):
            request.member_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.member), 'Member', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.member_shrink):
            query['Member'] = request.member_shrink
        if not UtilClient.is_unset(request.remove_type):
            query['RemoveType'] = request.remove_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveEntityMember',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.RemoveEntityMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_entity_member_with_options_async(
        self,
        tmp_req: chatbot_20171011_models.RemoveEntityMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.RemoveEntityMemberResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.RemoveEntityMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.member):
            request.member_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.member), 'Member', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.member_shrink):
            query['Member'] = request.member_shrink
        if not UtilClient.is_unset(request.remove_type):
            query['RemoveType'] = request.remove_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveEntityMember',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.RemoveEntityMemberResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        if not UtilClient.is_unset(request.synonym):
            query['Synonym'] = request.synonym
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveSynonym',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.RemoveSynonymResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_synonym_with_options_async(
        self,
        request: chatbot_20171011_models.RemoveSynonymRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.RemoveSynonymResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        if not UtilClient.is_unset(request.synonym):
            query['Synonym'] = request.synonym
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveSynonym',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.RemoveSynonymResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TestDialogFlow',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.TestDialogFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def test_dialog_flow_with_options_async(
        self,
        request: chatbot_20171011_models.TestDialogFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.TestDialogFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TestDialogFlow',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.TestDialogFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCategory',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_category_with_options_async(
        self,
        request: chatbot_20171011_models.UpdateCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCategory',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateCategoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_code):
            query['CoreWordCode'] = request.core_word_code
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCoreWord',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateCoreWordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_core_word_with_options_async(
        self,
        request: chatbot_20171011_models.UpdateCoreWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateCoreWordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_code):
            query['CoreWordCode'] = request.core_word_code
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCoreWord',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateCoreWordResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not UtilClient.is_unset(request.dialog_name):
            query['DialogName'] = request.dialog_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDialog',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateDialogResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dialog_with_options_async(
        self,
        request: chatbot_20171011_models.UpdateDialogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateDialogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not UtilClient.is_unset(request.dialog_name):
            query['DialogName'] = request.dialog_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDialog',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateDialogResponse(),
            await self.call_api_async(params, req, runtime)
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
        tmp_req: chatbot_20171011_models.UpdateDialogFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateDialogFlowResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.UpdateDialogFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.module_definition):
            request.module_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.module_definition), 'ModuleDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        body = {}
        if not UtilClient.is_unset(request.module_definition_shrink):
            body['ModuleDefinition'] = request.module_definition_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDialogFlow',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateDialogFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dialog_flow_with_options_async(
        self,
        tmp_req: chatbot_20171011_models.UpdateDialogFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateDialogFlowResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.UpdateDialogFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.module_definition):
            request.module_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.module_definition), 'ModuleDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        body = {}
        if not UtilClient.is_unset(request.module_definition_shrink):
            body['ModuleDefinition'] = request.module_definition_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDialogFlow',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateDialogFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
        tmp_req: chatbot_20171011_models.UpdateEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateEntityResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.UpdateEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.entity_name):
            query['EntityName'] = request.entity_name
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.regex):
            query['Regex'] = request.regex
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEntity',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_entity_with_options_async(
        self,
        tmp_req: chatbot_20171011_models.UpdateEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateEntityResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.UpdateEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.entity_name):
            query['EntityName'] = request.entity_name
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.regex):
            query['Regex'] = request.regex
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEntity',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateEntityResponse(),
            await self.call_api_async(params, req, runtime)
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
        tmp_req: chatbot_20171011_models.UpdateIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateIntentResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.UpdateIntentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_definition):
            request.intent_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.intent_definition), 'IntentDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIntent',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_intent_with_options_async(
        self,
        tmp_req: chatbot_20171011_models.UpdateIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateIntentResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.UpdateIntentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_definition):
            request.intent_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.intent_definition), 'IntentDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIntent',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateIntentResponse(),
            await self.call_api_async(params, req, runtime)
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
        tmp_req: chatbot_20171011_models.UpdateKnowledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateKnowledgeResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.UpdateKnowledgeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.knowledge):
            request.knowledge_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.knowledge), 'Knowledge', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.knowledge_shrink):
            body['Knowledge'] = request.knowledge_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateKnowledge',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateKnowledgeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_knowledge_with_options_async(
        self,
        tmp_req: chatbot_20171011_models.UpdateKnowledgeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdateKnowledgeResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.UpdateKnowledgeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.knowledge):
            request.knowledge_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.knowledge), 'Knowledge', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.knowledge_shrink):
            body['Knowledge'] = request.knowledge_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateKnowledge',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateKnowledgeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.perspective_id):
            query['PerspectiveId'] = request.perspective_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePerspective',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdatePerspectiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_perspective_with_options_async(
        self,
        request: chatbot_20171011_models.UpdatePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20171011_models.UpdatePerspectiveResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.perspective_id):
            query['PerspectiveId'] = request.perspective_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePerspective',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdatePerspectiveResponse(),
            await self.call_api_async(params, req, runtime)
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
