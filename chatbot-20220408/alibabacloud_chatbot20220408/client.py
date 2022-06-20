# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_chatbot20220408 import models as chatbot_20220408_models
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

    def associate_with_options(
        self,
        tmp_req: chatbot_20220408_models.AssociateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.AssociateResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.AssociateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.perspective):
            request.perspective_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.perspective, 'Perspective', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.perspective_shrink):
            query['Perspective'] = request.perspective_shrink
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
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.AssociateResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_with_options_async(
        self,
        tmp_req: chatbot_20220408_models.AssociateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.AssociateResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.AssociateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.perspective):
            request.perspective_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.perspective, 'Perspective', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.perspective_shrink):
            query['Perspective'] = request.perspective_shrink
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
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.AssociateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate(
        self,
        request: chatbot_20220408_models.AssociateRequest,
    ) -> chatbot_20220408_models.AssociateResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_with_options(request, runtime)

    async def associate_async(
        self,
        request: chatbot_20220408_models.AssociateRequest,
    ) -> chatbot_20220408_models.AssociateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_with_options_async(request, runtime)

    def begin_session_with_options(
        self,
        request: chatbot_20220408_models.BeginSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.BeginSessionResponse:
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
            action='BeginSession',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.BeginSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def begin_session_with_options_async(
        self,
        request: chatbot_20220408_models.BeginSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.BeginSessionResponse:
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
            action='BeginSession',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.BeginSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def begin_session(
        self,
        request: chatbot_20220408_models.BeginSessionRequest,
    ) -> chatbot_20220408_models.BeginSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.begin_session_with_options(request, runtime)

    async def begin_session_async(
        self,
        request: chatbot_20220408_models.BeginSessionRequest,
    ) -> chatbot_20220408_models.BeginSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.begin_session_with_options_async(request, runtime)

    def cancel_instance_publish_task_with_options(
        self,
        request: chatbot_20220408_models.CancelInstancePublishTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CancelInstancePublishTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelInstancePublishTask',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CancelInstancePublishTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_instance_publish_task_with_options_async(
        self,
        request: chatbot_20220408_models.CancelInstancePublishTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CancelInstancePublishTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelInstancePublishTask',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CancelInstancePublishTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_instance_publish_task(
        self,
        request: chatbot_20220408_models.CancelInstancePublishTaskRequest,
    ) -> chatbot_20220408_models.CancelInstancePublishTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_instance_publish_task_with_options(request, runtime)

    async def cancel_instance_publish_task_async(
        self,
        request: chatbot_20220408_models.CancelInstancePublishTaskRequest,
    ) -> chatbot_20220408_models.CancelInstancePublishTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_instance_publish_task_with_options_async(request, runtime)

    def cancel_publish_task_with_options(
        self,
        request: chatbot_20220408_models.CancelPublishTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CancelPublishTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelPublishTask',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CancelPublishTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_publish_task_with_options_async(
        self,
        request: chatbot_20220408_models.CancelPublishTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CancelPublishTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelPublishTask',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CancelPublishTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_publish_task(
        self,
        request: chatbot_20220408_models.CancelPublishTaskRequest,
    ) -> chatbot_20220408_models.CancelPublishTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_publish_task_with_options(request, runtime)

    async def cancel_publish_task_async(
        self,
        request: chatbot_20220408_models.CancelPublishTaskRequest,
    ) -> chatbot_20220408_models.CancelPublishTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_publish_task_with_options_async(request, runtime)

    def chat_with_options(
        self,
        tmp_req: chatbot_20220408_models.ChatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ChatResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.ChatShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.perspective):
            request.perspective_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.perspective, 'Perspective', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_name):
            query['IntentName'] = request.intent_name
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        if not UtilClient.is_unset(request.perspective_shrink):
            query['Perspective'] = request.perspective_shrink
        if not UtilClient.is_unset(request.sender_id):
            query['SenderId'] = request.sender_id
        if not UtilClient.is_unset(request.sender_nick):
            query['SenderNick'] = request.sender_nick
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.utterance):
            query['Utterance'] = request.utterance
        if not UtilClient.is_unset(request.vendor_param):
            query['VendorParam'] = request.vendor_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Chat',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_with_options_async(
        self,
        tmp_req: chatbot_20220408_models.ChatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ChatResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.ChatShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.perspective):
            request.perspective_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.perspective, 'Perspective', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_name):
            query['IntentName'] = request.intent_name
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        if not UtilClient.is_unset(request.perspective_shrink):
            query['Perspective'] = request.perspective_shrink
        if not UtilClient.is_unset(request.sender_id):
            query['SenderId'] = request.sender_id
        if not UtilClient.is_unset(request.sender_nick):
            query['SenderNick'] = request.sender_nick
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.utterance):
            query['Utterance'] = request.utterance
        if not UtilClient.is_unset(request.vendor_param):
            query['VendorParam'] = request.vendor_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Chat',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat(
        self,
        request: chatbot_20220408_models.ChatRequest,
    ) -> chatbot_20220408_models.ChatResponse:
        runtime = util_models.RuntimeOptions()
        return self.chat_with_options(request, runtime)

    async def chat_async(
        self,
        request: chatbot_20220408_models.ChatRequest,
    ) -> chatbot_20220408_models.ChatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.chat_with_options_async(request, runtime)

    def continue_instance_publish_task_with_options(
        self,
        request: chatbot_20220408_models.ContinueInstancePublishTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ContinueInstancePublishTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ContinueInstancePublishTask',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ContinueInstancePublishTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def continue_instance_publish_task_with_options_async(
        self,
        request: chatbot_20220408_models.ContinueInstancePublishTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ContinueInstancePublishTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ContinueInstancePublishTask',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ContinueInstancePublishTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def continue_instance_publish_task(
        self,
        request: chatbot_20220408_models.ContinueInstancePublishTaskRequest,
    ) -> chatbot_20220408_models.ContinueInstancePublishTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.continue_instance_publish_task_with_options(request, runtime)

    async def continue_instance_publish_task_async(
        self,
        request: chatbot_20220408_models.ContinueInstancePublishTaskRequest,
    ) -> chatbot_20220408_models.ContinueInstancePublishTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.continue_instance_publish_task_with_options_async(request, runtime)

    def create_category_with_options(
        self,
        request: chatbot_20220408_models.CreateCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.parent_category_id):
            body['ParentCategoryId'] = request.parent_category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCategory',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_category_with_options_async(
        self,
        request: chatbot_20220408_models.CreateCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.parent_category_id):
            body['ParentCategoryId'] = request.parent_category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCategory',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_category(
        self,
        request: chatbot_20220408_models.CreateCategoryRequest,
    ) -> chatbot_20220408_models.CreateCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_category_with_options(request, runtime)

    async def create_category_async(
        self,
        request: chatbot_20220408_models.CreateCategoryRequest,
    ) -> chatbot_20220408_models.CreateCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_category_with_options_async(request, runtime)

    def create_conn_question_with_options(
        self,
        request: chatbot_20220408_models.CreateConnQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateConnQuestionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.conn_question_id):
            body['ConnQuestionId'] = request.conn_question_id
        if not UtilClient.is_unset(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConnQuestion',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateConnQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_conn_question_with_options_async(
        self,
        request: chatbot_20220408_models.CreateConnQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateConnQuestionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.conn_question_id):
            body['ConnQuestionId'] = request.conn_question_id
        if not UtilClient.is_unset(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConnQuestion',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateConnQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_conn_question(
        self,
        request: chatbot_20220408_models.CreateConnQuestionRequest,
    ) -> chatbot_20220408_models.CreateConnQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_conn_question_with_options(request, runtime)

    async def create_conn_question_async(
        self,
        request: chatbot_20220408_models.CreateConnQuestionRequest,
    ) -> chatbot_20220408_models.CreateConnQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_conn_question_with_options_async(request, runtime)

    def create_dsentity_with_options(
        self,
        request: chatbot_20220408_models.CreateDSEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateDSEntityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_name):
            query['EntityName'] = request.entity_name
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDSEntity',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateDSEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dsentity_with_options_async(
        self,
        request: chatbot_20220408_models.CreateDSEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateDSEntityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_name):
            query['EntityName'] = request.entity_name
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDSEntity',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateDSEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dsentity(
        self,
        request: chatbot_20220408_models.CreateDSEntityRequest,
    ) -> chatbot_20220408_models.CreateDSEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dsentity_with_options(request, runtime)

    async def create_dsentity_async(
        self,
        request: chatbot_20220408_models.CreateDSEntityRequest,
    ) -> chatbot_20220408_models.CreateDSEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dsentity_with_options_async(request, runtime)

    def create_dsentity_value_with_options(
        self,
        tmp_req: chatbot_20220408_models.CreateDSEntityValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateDSEntityValueResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreateDSEntityValueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.synonyms):
            request.synonyms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.synonyms, 'Synonyms', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.synonyms_shrink):
            body['Synonyms'] = request.synonyms_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDSEntityValue',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateDSEntityValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dsentity_value_with_options_async(
        self,
        tmp_req: chatbot_20220408_models.CreateDSEntityValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateDSEntityValueResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreateDSEntityValueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.synonyms):
            request.synonyms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.synonyms, 'Synonyms', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.synonyms_shrink):
            body['Synonyms'] = request.synonyms_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDSEntityValue',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateDSEntityValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dsentity_value(
        self,
        request: chatbot_20220408_models.CreateDSEntityValueRequest,
    ) -> chatbot_20220408_models.CreateDSEntityValueResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dsentity_value_with_options(request, runtime)

    async def create_dsentity_value_async(
        self,
        request: chatbot_20220408_models.CreateDSEntityValueRequest,
    ) -> chatbot_20220408_models.CreateDSEntityValueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dsentity_value_with_options_async(request, runtime)

    def create_faq_with_options(
        self,
        request: chatbot_20220408_models.CreateFaqRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateFaqResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.solution_content):
            body['SolutionContent'] = request.solution_content
        if not UtilClient.is_unset(request.solution_type):
            body['SolutionType'] = request.solution_type
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFaq',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateFaqResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_faq_with_options_async(
        self,
        request: chatbot_20220408_models.CreateFaqRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateFaqResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.solution_content):
            body['SolutionContent'] = request.solution_content
        if not UtilClient.is_unset(request.solution_type):
            body['SolutionType'] = request.solution_type
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFaq',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateFaqResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_faq(
        self,
        request: chatbot_20220408_models.CreateFaqRequest,
    ) -> chatbot_20220408_models.CreateFaqResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_faq_with_options(request, runtime)

    async def create_faq_async(
        self,
        request: chatbot_20220408_models.CreateFaqRequest,
    ) -> chatbot_20220408_models.CreateFaqResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_faq_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: chatbot_20220408_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
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
            action='CreateInstance',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: chatbot_20220408_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
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
            action='CreateInstance',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: chatbot_20220408_models.CreateInstanceRequest,
    ) -> chatbot_20220408_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: chatbot_20220408_models.CreateInstanceRequest,
    ) -> chatbot_20220408_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_instance_publish_task_with_options(
        self,
        request: chatbot_20220408_models.CreateInstancePublishTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateInstancePublishTaskResponse:
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
            action='CreateInstancePublishTask',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateInstancePublishTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_publish_task_with_options_async(
        self,
        request: chatbot_20220408_models.CreateInstancePublishTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateInstancePublishTaskResponse:
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
            action='CreateInstancePublishTask',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateInstancePublishTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_publish_task(
        self,
        request: chatbot_20220408_models.CreateInstancePublishTaskRequest,
    ) -> chatbot_20220408_models.CreateInstancePublishTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_publish_task_with_options(request, runtime)

    async def create_instance_publish_task_async(
        self,
        request: chatbot_20220408_models.CreateInstancePublishTaskRequest,
    ) -> chatbot_20220408_models.CreateInstancePublishTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_publish_task_with_options_async(request, runtime)

    def create_intent_with_options(
        self,
        tmp_req: chatbot_20220408_models.CreateIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateIntentResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreateIntentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_definition):
            request.intent_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.intent_definition), 'IntentDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIntent',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_intent_with_options_async(
        self,
        tmp_req: chatbot_20220408_models.CreateIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateIntentResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreateIntentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_definition):
            request.intent_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.intent_definition), 'IntentDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIntent',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_intent(
        self,
        request: chatbot_20220408_models.CreateIntentRequest,
    ) -> chatbot_20220408_models.CreateIntentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_intent_with_options(request, runtime)

    async def create_intent_async(
        self,
        request: chatbot_20220408_models.CreateIntentRequest,
    ) -> chatbot_20220408_models.CreateIntentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_intent_with_options_async(request, runtime)

    def create_lgf_with_options(
        self,
        tmp_req: chatbot_20220408_models.CreateLgfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateLgfResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreateLgfShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lgf_definition):
            request.lgf_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.lgf_definition), 'LgfDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lgf_definition_shrink):
            query['LgfDefinition'] = request.lgf_definition_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLgf',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateLgfResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_lgf_with_options_async(
        self,
        tmp_req: chatbot_20220408_models.CreateLgfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateLgfResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreateLgfShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lgf_definition):
            request.lgf_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.lgf_definition), 'LgfDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lgf_definition_shrink):
            query['LgfDefinition'] = request.lgf_definition_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLgf',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateLgfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_lgf(
        self,
        request: chatbot_20220408_models.CreateLgfRequest,
    ) -> chatbot_20220408_models.CreateLgfResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_lgf_with_options(request, runtime)

    async def create_lgf_async(
        self,
        request: chatbot_20220408_models.CreateLgfRequest,
    ) -> chatbot_20220408_models.CreateLgfResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_lgf_with_options_async(request, runtime)

    def create_perspective_with_options(
        self,
        request: chatbot_20220408_models.CreatePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreatePerspectiveResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePerspective',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreatePerspectiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_perspective_with_options_async(
        self,
        request: chatbot_20220408_models.CreatePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreatePerspectiveResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePerspective',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreatePerspectiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_perspective(
        self,
        request: chatbot_20220408_models.CreatePerspectiveRequest,
    ) -> chatbot_20220408_models.CreatePerspectiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_perspective_with_options(request, runtime)

    async def create_perspective_async(
        self,
        request: chatbot_20220408_models.CreatePerspectiveRequest,
    ) -> chatbot_20220408_models.CreatePerspectiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_perspective_with_options_async(request, runtime)

    def create_publish_task_with_options(
        self,
        tmp_req: chatbot_20220408_models.CreatePublishTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreatePublishTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreatePublishTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_id_list):
            request.data_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_id_list, 'DataIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.data_id_list_shrink):
            query['DataIdList'] = request.data_id_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePublishTask',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreatePublishTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_publish_task_with_options_async(
        self,
        tmp_req: chatbot_20220408_models.CreatePublishTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreatePublishTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreatePublishTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_id_list):
            request.data_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_id_list, 'DataIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.data_id_list_shrink):
            query['DataIdList'] = request.data_id_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePublishTask',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreatePublishTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_publish_task(
        self,
        request: chatbot_20220408_models.CreatePublishTaskRequest,
    ) -> chatbot_20220408_models.CreatePublishTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_publish_task_with_options(request, runtime)

    async def create_publish_task_async(
        self,
        request: chatbot_20220408_models.CreatePublishTaskRequest,
    ) -> chatbot_20220408_models.CreatePublishTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_publish_task_with_options_async(request, runtime)

    def create_sim_question_with_options(
        self,
        request: chatbot_20220408_models.CreateSimQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateSimQuestionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSimQuestion',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateSimQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sim_question_with_options_async(
        self,
        request: chatbot_20220408_models.CreateSimQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateSimQuestionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSimQuestion',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateSimQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sim_question(
        self,
        request: chatbot_20220408_models.CreateSimQuestionRequest,
    ) -> chatbot_20220408_models.CreateSimQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sim_question_with_options(request, runtime)

    async def create_sim_question_async(
        self,
        request: chatbot_20220408_models.CreateSimQuestionRequest,
    ) -> chatbot_20220408_models.CreateSimQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sim_question_with_options_async(request, runtime)

    def create_solution_with_options(
        self,
        request: chatbot_20220408_models.CreateSolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateSolutionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.content_type):
            query['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        if not UtilClient.is_unset(request.perspective_codes):
            query['PerspectiveCodes'] = request.perspective_codes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSolution',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateSolutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_solution_with_options_async(
        self,
        request: chatbot_20220408_models.CreateSolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateSolutionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.content_type):
            query['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        if not UtilClient.is_unset(request.perspective_codes):
            query['PerspectiveCodes'] = request.perspective_codes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSolution',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateSolutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_solution(
        self,
        request: chatbot_20220408_models.CreateSolutionRequest,
    ) -> chatbot_20220408_models.CreateSolutionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_solution_with_options(request, runtime)

    async def create_solution_async(
        self,
        request: chatbot_20220408_models.CreateSolutionRequest,
    ) -> chatbot_20220408_models.CreateSolutionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_solution_with_options_async(request, runtime)

    def create_user_say_with_options(
        self,
        tmp_req: chatbot_20220408_models.CreateUserSayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateUserSayResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreateUserSayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_say_definition):
            request.user_say_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_say_definition), 'UserSayDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_say_definition_shrink):
            query['UserSayDefinition'] = request.user_say_definition_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserSay',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateUserSayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_say_with_options_async(
        self,
        tmp_req: chatbot_20220408_models.CreateUserSayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateUserSayResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreateUserSayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_say_definition):
            request.user_say_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_say_definition), 'UserSayDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_say_definition_shrink):
            query['UserSayDefinition'] = request.user_say_definition_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserSay',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.CreateUserSayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_say(
        self,
        request: chatbot_20220408_models.CreateUserSayRequest,
    ) -> chatbot_20220408_models.CreateUserSayResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_say_with_options(request, runtime)

    async def create_user_say_async(
        self,
        request: chatbot_20220408_models.CreateUserSayRequest,
    ) -> chatbot_20220408_models.CreateUserSayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_say_with_options_async(request, runtime)

    def delete_category_with_options(
        self,
        request: chatbot_20220408_models.DeleteCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCategory',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_category_with_options_async(
        self,
        request: chatbot_20220408_models.DeleteCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCategory',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_category(
        self,
        request: chatbot_20220408_models.DeleteCategoryRequest,
    ) -> chatbot_20220408_models.DeleteCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_category_with_options(request, runtime)

    async def delete_category_async(
        self,
        request: chatbot_20220408_models.DeleteCategoryRequest,
    ) -> chatbot_20220408_models.DeleteCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_category_with_options_async(request, runtime)

    def delete_conn_question_with_options(
        self,
        request: chatbot_20220408_models.DeleteConnQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteConnQuestionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.outline_id):
            body['OutlineId'] = request.outline_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteConnQuestion',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteConnQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_conn_question_with_options_async(
        self,
        request: chatbot_20220408_models.DeleteConnQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteConnQuestionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.outline_id):
            body['OutlineId'] = request.outline_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteConnQuestion',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteConnQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_conn_question(
        self,
        request: chatbot_20220408_models.DeleteConnQuestionRequest,
    ) -> chatbot_20220408_models.DeleteConnQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_conn_question_with_options(request, runtime)

    async def delete_conn_question_async(
        self,
        request: chatbot_20220408_models.DeleteConnQuestionRequest,
    ) -> chatbot_20220408_models.DeleteConnQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_conn_question_with_options_async(request, runtime)

    def delete_dsentity_with_options(
        self,
        request: chatbot_20220408_models.DeleteDSEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteDSEntityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDSEntity',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteDSEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dsentity_with_options_async(
        self,
        request: chatbot_20220408_models.DeleteDSEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteDSEntityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDSEntity',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteDSEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dsentity(
        self,
        request: chatbot_20220408_models.DeleteDSEntityRequest,
    ) -> chatbot_20220408_models.DeleteDSEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dsentity_with_options(request, runtime)

    async def delete_dsentity_async(
        self,
        request: chatbot_20220408_models.DeleteDSEntityRequest,
    ) -> chatbot_20220408_models.DeleteDSEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dsentity_with_options_async(request, runtime)

    def delete_dsentity_value_with_options(
        self,
        request: chatbot_20220408_models.DeleteDSEntityValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteDSEntityValueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.entity_value_id):
            query['EntityValueId'] = request.entity_value_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDSEntityValue',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteDSEntityValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dsentity_value_with_options_async(
        self,
        request: chatbot_20220408_models.DeleteDSEntityValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteDSEntityValueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.entity_value_id):
            query['EntityValueId'] = request.entity_value_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDSEntityValue',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteDSEntityValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dsentity_value(
        self,
        request: chatbot_20220408_models.DeleteDSEntityValueRequest,
    ) -> chatbot_20220408_models.DeleteDSEntityValueResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dsentity_value_with_options(request, runtime)

    async def delete_dsentity_value_async(
        self,
        request: chatbot_20220408_models.DeleteDSEntityValueRequest,
    ) -> chatbot_20220408_models.DeleteDSEntityValueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dsentity_value_with_options_async(request, runtime)

    def delete_faq_with_options(
        self,
        request: chatbot_20220408_models.DeleteFaqRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteFaqResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFaq',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteFaqResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_faq_with_options_async(
        self,
        request: chatbot_20220408_models.DeleteFaqRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteFaqResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFaq',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteFaqResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_faq(
        self,
        request: chatbot_20220408_models.DeleteFaqRequest,
    ) -> chatbot_20220408_models.DeleteFaqResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_faq_with_options(request, runtime)

    async def delete_faq_async(
        self,
        request: chatbot_20220408_models.DeleteFaqRequest,
    ) -> chatbot_20220408_models.DeleteFaqResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_faq_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: chatbot_20220408_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteInstanceResponse:
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
            action='DeleteInstance',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: chatbot_20220408_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteInstanceResponse:
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
            action='DeleteInstance',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: chatbot_20220408_models.DeleteInstanceRequest,
    ) -> chatbot_20220408_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: chatbot_20220408_models.DeleteInstanceRequest,
    ) -> chatbot_20220408_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_intent_with_options(
        self,
        request: chatbot_20220408_models.DeleteIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteIntentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIntent',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_intent_with_options_async(
        self,
        request: chatbot_20220408_models.DeleteIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteIntentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIntent',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_intent(
        self,
        request: chatbot_20220408_models.DeleteIntentRequest,
    ) -> chatbot_20220408_models.DeleteIntentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_intent_with_options(request, runtime)

    async def delete_intent_async(
        self,
        request: chatbot_20220408_models.DeleteIntentRequest,
    ) -> chatbot_20220408_models.DeleteIntentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_intent_with_options_async(request, runtime)

    def delete_lgf_with_options(
        self,
        request: chatbot_20220408_models.DeleteLgfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteLgfResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.lgf_id):
            query['LgfId'] = request.lgf_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLgf',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteLgfResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_lgf_with_options_async(
        self,
        request: chatbot_20220408_models.DeleteLgfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteLgfResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.lgf_id):
            query['LgfId'] = request.lgf_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLgf',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteLgfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_lgf(
        self,
        request: chatbot_20220408_models.DeleteLgfRequest,
    ) -> chatbot_20220408_models.DeleteLgfResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_lgf_with_options(request, runtime)

    async def delete_lgf_async(
        self,
        request: chatbot_20220408_models.DeleteLgfRequest,
    ) -> chatbot_20220408_models.DeleteLgfResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_lgf_with_options_async(request, runtime)

    def delete_perspective_with_options(
        self,
        request: chatbot_20220408_models.DeletePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeletePerspectiveResponse:
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
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeletePerspectiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_perspective_with_options_async(
        self,
        request: chatbot_20220408_models.DeletePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeletePerspectiveResponse:
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
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeletePerspectiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_perspective(
        self,
        request: chatbot_20220408_models.DeletePerspectiveRequest,
    ) -> chatbot_20220408_models.DeletePerspectiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_perspective_with_options(request, runtime)

    async def delete_perspective_async(
        self,
        request: chatbot_20220408_models.DeletePerspectiveRequest,
    ) -> chatbot_20220408_models.DeletePerspectiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_perspective_with_options_async(request, runtime)

    def delete_sim_question_with_options(
        self,
        request: chatbot_20220408_models.DeleteSimQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteSimQuestionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.sim_question_id):
            body['SimQuestionId'] = request.sim_question_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSimQuestion',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteSimQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sim_question_with_options_async(
        self,
        request: chatbot_20220408_models.DeleteSimQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteSimQuestionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.sim_question_id):
            body['SimQuestionId'] = request.sim_question_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSimQuestion',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteSimQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sim_question(
        self,
        request: chatbot_20220408_models.DeleteSimQuestionRequest,
    ) -> chatbot_20220408_models.DeleteSimQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sim_question_with_options(request, runtime)

    async def delete_sim_question_async(
        self,
        request: chatbot_20220408_models.DeleteSimQuestionRequest,
    ) -> chatbot_20220408_models.DeleteSimQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sim_question_with_options_async(request, runtime)

    def delete_solution_with_options(
        self,
        request: chatbot_20220408_models.DeleteSolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteSolutionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.solution_id):
            body['SolutionId'] = request.solution_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSolution',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteSolutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_solution_with_options_async(
        self,
        request: chatbot_20220408_models.DeleteSolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteSolutionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.solution_id):
            body['SolutionId'] = request.solution_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSolution',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteSolutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_solution(
        self,
        request: chatbot_20220408_models.DeleteSolutionRequest,
    ) -> chatbot_20220408_models.DeleteSolutionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_solution_with_options(request, runtime)

    async def delete_solution_async(
        self,
        request: chatbot_20220408_models.DeleteSolutionRequest,
    ) -> chatbot_20220408_models.DeleteSolutionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_solution_with_options_async(request, runtime)

    def delete_user_say_with_options(
        self,
        request: chatbot_20220408_models.DeleteUserSayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteUserSayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.user_say_id):
            query['UserSayId'] = request.user_say_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserSay',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteUserSayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_say_with_options_async(
        self,
        request: chatbot_20220408_models.DeleteUserSayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteUserSayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.user_say_id):
            query['UserSayId'] = request.user_say_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserSay',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DeleteUserSayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_say(
        self,
        request: chatbot_20220408_models.DeleteUserSayRequest,
    ) -> chatbot_20220408_models.DeleteUserSayResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_say_with_options(request, runtime)

    async def delete_user_say_async(
        self,
        request: chatbot_20220408_models.DeleteUserSayRequest,
    ) -> chatbot_20220408_models.DeleteUserSayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_say_with_options_async(request, runtime)

    def describe_category_with_options(
        self,
        request: chatbot_20220408_models.DescribeCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCategory',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DescribeCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_category_with_options_async(
        self,
        request: chatbot_20220408_models.DescribeCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCategory',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DescribeCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_category(
        self,
        request: chatbot_20220408_models.DescribeCategoryRequest,
    ) -> chatbot_20220408_models.DescribeCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_category_with_options(request, runtime)

    async def describe_category_async(
        self,
        request: chatbot_20220408_models.DescribeCategoryRequest,
    ) -> chatbot_20220408_models.DescribeCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_category_with_options_async(request, runtime)

    def describe_dsentity_with_options(
        self,
        request: chatbot_20220408_models.DescribeDSEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeDSEntityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDSEntity',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DescribeDSEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dsentity_with_options_async(
        self,
        request: chatbot_20220408_models.DescribeDSEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeDSEntityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDSEntity',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DescribeDSEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dsentity(
        self,
        request: chatbot_20220408_models.DescribeDSEntityRequest,
    ) -> chatbot_20220408_models.DescribeDSEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dsentity_with_options(request, runtime)

    async def describe_dsentity_async(
        self,
        request: chatbot_20220408_models.DescribeDSEntityRequest,
    ) -> chatbot_20220408_models.DescribeDSEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dsentity_with_options_async(request, runtime)

    def describe_faq_with_options(
        self,
        request: chatbot_20220408_models.DescribeFaqRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeFaqResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFaq',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DescribeFaqResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_faq_with_options_async(
        self,
        request: chatbot_20220408_models.DescribeFaqRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeFaqResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFaq',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DescribeFaqResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_faq(
        self,
        request: chatbot_20220408_models.DescribeFaqRequest,
    ) -> chatbot_20220408_models.DescribeFaqResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_faq_with_options(request, runtime)

    async def describe_faq_async(
        self,
        request: chatbot_20220408_models.DescribeFaqRequest,
    ) -> chatbot_20220408_models.DescribeFaqResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_faq_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: chatbot_20220408_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeInstanceResponse:
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
            action='DescribeInstance',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: chatbot_20220408_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeInstanceResponse:
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
            action='DescribeInstance',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        request: chatbot_20220408_models.DescribeInstanceRequest,
    ) -> chatbot_20220408_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: chatbot_20220408_models.DescribeInstanceRequest,
    ) -> chatbot_20220408_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_intent_with_options(
        self,
        request: chatbot_20220408_models.DescribeIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeIntentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.intent_id):
            body['IntentId'] = request.intent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeIntent',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DescribeIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_intent_with_options_async(
        self,
        request: chatbot_20220408_models.DescribeIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeIntentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.intent_id):
            body['IntentId'] = request.intent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeIntent',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DescribeIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_intent(
        self,
        request: chatbot_20220408_models.DescribeIntentRequest,
    ) -> chatbot_20220408_models.DescribeIntentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_intent_with_options(request, runtime)

    async def describe_intent_async(
        self,
        request: chatbot_20220408_models.DescribeIntentRequest,
    ) -> chatbot_20220408_models.DescribeIntentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_intent_with_options_async(request, runtime)

    def describe_perspective_with_options(
        self,
        request: chatbot_20220408_models.DescribePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribePerspectiveResponse:
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
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DescribePerspectiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_perspective_with_options_async(
        self,
        request: chatbot_20220408_models.DescribePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribePerspectiveResponse:
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
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.DescribePerspectiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_perspective(
        self,
        request: chatbot_20220408_models.DescribePerspectiveRequest,
    ) -> chatbot_20220408_models.DescribePerspectiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_perspective_with_options(request, runtime)

    async def describe_perspective_async(
        self,
        request: chatbot_20220408_models.DescribePerspectiveRequest,
    ) -> chatbot_20220408_models.DescribePerspectiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_perspective_with_options_async(request, runtime)

    def feedback_with_options(
        self,
        request: chatbot_20220408_models.FeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.FeedbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.feedback_content):
            query['FeedbackContent'] = request.feedback_content
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
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.FeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def feedback_with_options_async(
        self,
        request: chatbot_20220408_models.FeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.FeedbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.feedback_content):
            query['FeedbackContent'] = request.feedback_content
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
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.FeedbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def feedback(
        self,
        request: chatbot_20220408_models.FeedbackRequest,
    ) -> chatbot_20220408_models.FeedbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.feedback_with_options(request, runtime)

    async def feedback_async(
        self,
        request: chatbot_20220408_models.FeedbackRequest,
    ) -> chatbot_20220408_models.FeedbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.feedback_with_options_async(request, runtime)

    def get_async_result_with_options(
        self,
        request: chatbot_20220408_models.GetAsyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.GetAsyncResultResponse:
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
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.GetAsyncResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_result_with_options_async(
        self,
        request: chatbot_20220408_models.GetAsyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.GetAsyncResultResponse:
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
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.GetAsyncResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_result(
        self,
        request: chatbot_20220408_models.GetAsyncResultRequest,
    ) -> chatbot_20220408_models.GetAsyncResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_async_result_with_options(request, runtime)

    async def get_async_result_async(
        self,
        request: chatbot_20220408_models.GetAsyncResultRequest,
    ) -> chatbot_20220408_models.GetAsyncResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_async_result_with_options_async(request, runtime)

    def get_instance_publish_task_state_with_options(
        self,
        request: chatbot_20220408_models.GetInstancePublishTaskStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.GetInstancePublishTaskStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstancePublishTaskState',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.GetInstancePublishTaskStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_publish_task_state_with_options_async(
        self,
        request: chatbot_20220408_models.GetInstancePublishTaskStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.GetInstancePublishTaskStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstancePublishTaskState',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.GetInstancePublishTaskStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_publish_task_state(
        self,
        request: chatbot_20220408_models.GetInstancePublishTaskStateRequest,
    ) -> chatbot_20220408_models.GetInstancePublishTaskStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_publish_task_state_with_options(request, runtime)

    async def get_instance_publish_task_state_async(
        self,
        request: chatbot_20220408_models.GetInstancePublishTaskStateRequest,
    ) -> chatbot_20220408_models.GetInstancePublishTaskStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_publish_task_state_with_options_async(request, runtime)

    def get_publish_task_state_with_options(
        self,
        request: chatbot_20220408_models.GetPublishTaskStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.GetPublishTaskStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublishTaskState',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.GetPublishTaskStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_publish_task_state_with_options_async(
        self,
        request: chatbot_20220408_models.GetPublishTaskStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.GetPublishTaskStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublishTaskState',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.GetPublishTaskStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_publish_task_state(
        self,
        request: chatbot_20220408_models.GetPublishTaskStateRequest,
    ) -> chatbot_20220408_models.GetPublishTaskStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_publish_task_state_with_options(request, runtime)

    async def get_publish_task_state_async(
        self,
        request: chatbot_20220408_models.GetPublishTaskStateRequest,
    ) -> chatbot_20220408_models.GetPublishTaskStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_publish_task_state_with_options_async(request, runtime)

    def link_instance_category_with_options(
        self,
        request: chatbot_20220408_models.LinkInstanceCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.LinkInstanceCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.category_ids):
            body['CategoryIds'] = request.category_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LinkInstanceCategory',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.LinkInstanceCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def link_instance_category_with_options_async(
        self,
        request: chatbot_20220408_models.LinkInstanceCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.LinkInstanceCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.category_ids):
            body['CategoryIds'] = request.category_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LinkInstanceCategory',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.LinkInstanceCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def link_instance_category(
        self,
        request: chatbot_20220408_models.LinkInstanceCategoryRequest,
    ) -> chatbot_20220408_models.LinkInstanceCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.link_instance_category_with_options(request, runtime)

    async def link_instance_category_async(
        self,
        request: chatbot_20220408_models.LinkInstanceCategoryRequest,
    ) -> chatbot_20220408_models.LinkInstanceCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.link_instance_category_with_options_async(request, runtime)

    def list_agent_with_options(
        self,
        request: chatbot_20220408_models.ListAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListAgentResponse:
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
            action='ListAgent',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agent_with_options_async(
        self,
        request: chatbot_20220408_models.ListAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListAgentResponse:
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
            action='ListAgent',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agent(
        self,
        request: chatbot_20220408_models.ListAgentRequest,
    ) -> chatbot_20220408_models.ListAgentResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_agent_with_options(request, runtime)

    async def list_agent_async(
        self,
        request: chatbot_20220408_models.ListAgentRequest,
    ) -> chatbot_20220408_models.ListAgentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_agent_with_options_async(request, runtime)

    def list_category_with_options(
        self,
        request: chatbot_20220408_models.ListCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.parent_category_id):
            body['ParentCategoryId'] = request.parent_category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCategory',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_category_with_options_async(
        self,
        request: chatbot_20220408_models.ListCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.parent_category_id):
            body['ParentCategoryId'] = request.parent_category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCategory',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_category(
        self,
        request: chatbot_20220408_models.ListCategoryRequest,
    ) -> chatbot_20220408_models.ListCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_category_with_options(request, runtime)

    async def list_category_async(
        self,
        request: chatbot_20220408_models.ListCategoryRequest,
    ) -> chatbot_20220408_models.ListCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_category_with_options_async(request, runtime)

    def list_conn_question_with_options(
        self,
        request: chatbot_20220408_models.ListConnQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListConnQuestionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConnQuestion',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListConnQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_conn_question_with_options_async(
        self,
        request: chatbot_20220408_models.ListConnQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListConnQuestionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConnQuestion',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListConnQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_conn_question(
        self,
        request: chatbot_20220408_models.ListConnQuestionRequest,
    ) -> chatbot_20220408_models.ListConnQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_conn_question_with_options(request, runtime)

    async def list_conn_question_async(
        self,
        request: chatbot_20220408_models.ListConnQuestionRequest,
    ) -> chatbot_20220408_models.ListConnQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_conn_question_with_options_async(request, runtime)

    def list_dsentity_with_options(
        self,
        request: chatbot_20220408_models.ListDSEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListDSEntityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDSEntity',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListDSEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dsentity_with_options_async(
        self,
        request: chatbot_20220408_models.ListDSEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListDSEntityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDSEntity',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListDSEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dsentity(
        self,
        request: chatbot_20220408_models.ListDSEntityRequest,
    ) -> chatbot_20220408_models.ListDSEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dsentity_with_options(request, runtime)

    async def list_dsentity_async(
        self,
        request: chatbot_20220408_models.ListDSEntityRequest,
    ) -> chatbot_20220408_models.ListDSEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dsentity_with_options_async(request, runtime)

    def list_dsentity_value_with_options(
        self,
        request: chatbot_20220408_models.ListDSEntityValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListDSEntityValueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.entity_value_id):
            body['EntityValueId'] = request.entity_value_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDSEntityValue',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListDSEntityValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dsentity_value_with_options_async(
        self,
        request: chatbot_20220408_models.ListDSEntityValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListDSEntityValueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.entity_value_id):
            body['EntityValueId'] = request.entity_value_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDSEntityValue',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListDSEntityValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dsentity_value(
        self,
        request: chatbot_20220408_models.ListDSEntityValueRequest,
    ) -> chatbot_20220408_models.ListDSEntityValueResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dsentity_value_with_options(request, runtime)

    async def list_dsentity_value_async(
        self,
        request: chatbot_20220408_models.ListDSEntityValueRequest,
    ) -> chatbot_20220408_models.ListDSEntityValueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dsentity_value_with_options_async(request, runtime)

    def list_instance_with_options(
        self,
        request: chatbot_20220408_models.ListInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.robot_type):
            query['RobotType'] = request.robot_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstance',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_with_options_async(
        self,
        request: chatbot_20220408_models.ListInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.robot_type):
            query['RobotType'] = request.robot_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstance',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance(
        self,
        request: chatbot_20220408_models.ListInstanceRequest,
    ) -> chatbot_20220408_models.ListInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instance_with_options(request, runtime)

    async def list_instance_async(
        self,
        request: chatbot_20220408_models.ListInstanceRequest,
    ) -> chatbot_20220408_models.ListInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_with_options_async(request, runtime)

    def list_intent_with_options(
        self,
        request: chatbot_20220408_models.ListIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListIntentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
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
            action='ListIntent',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intent_with_options_async(
        self,
        request: chatbot_20220408_models.ListIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListIntentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
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
            action='ListIntent',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intent(
        self,
        request: chatbot_20220408_models.ListIntentRequest,
    ) -> chatbot_20220408_models.ListIntentResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_intent_with_options(request, runtime)

    async def list_intent_async(
        self,
        request: chatbot_20220408_models.ListIntentRequest,
    ) -> chatbot_20220408_models.ListIntentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_intent_with_options_async(request, runtime)

    def list_lgf_with_options(
        self,
        request: chatbot_20220408_models.ListLgfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListLgfResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.lgf_text):
            query['LgfText'] = request.lgf_text
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLgf',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListLgfResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_lgf_with_options_async(
        self,
        request: chatbot_20220408_models.ListLgfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListLgfResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.lgf_text):
            query['LgfText'] = request.lgf_text
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLgf',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListLgfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_lgf(
        self,
        request: chatbot_20220408_models.ListLgfRequest,
    ) -> chatbot_20220408_models.ListLgfResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_lgf_with_options(request, runtime)

    async def list_lgf_async(
        self,
        request: chatbot_20220408_models.ListLgfRequest,
    ) -> chatbot_20220408_models.ListLgfResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_lgf_with_options_async(request, runtime)

    def list_sim_question_with_options(
        self,
        request: chatbot_20220408_models.ListSimQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListSimQuestionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSimQuestion',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListSimQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sim_question_with_options_async(
        self,
        request: chatbot_20220408_models.ListSimQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListSimQuestionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSimQuestion',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListSimQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sim_question(
        self,
        request: chatbot_20220408_models.ListSimQuestionRequest,
    ) -> chatbot_20220408_models.ListSimQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sim_question_with_options(request, runtime)

    async def list_sim_question_async(
        self,
        request: chatbot_20220408_models.ListSimQuestionRequest,
    ) -> chatbot_20220408_models.ListSimQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sim_question_with_options_async(request, runtime)

    def list_solution_with_options(
        self,
        request: chatbot_20220408_models.ListSolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListSolutionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSolution',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListSolutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_solution_with_options_async(
        self,
        request: chatbot_20220408_models.ListSolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListSolutionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSolution',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListSolutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_solution(
        self,
        request: chatbot_20220408_models.ListSolutionRequest,
    ) -> chatbot_20220408_models.ListSolutionResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_solution_with_options(request, runtime)

    async def list_solution_async(
        self,
        request: chatbot_20220408_models.ListSolutionRequest,
    ) -> chatbot_20220408_models.ListSolutionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_solution_with_options_async(request, runtime)

    def list_user_say_with_options(
        self,
        request: chatbot_20220408_models.ListUserSayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListUserSayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserSay',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListUserSayResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_say_with_options_async(
        self,
        request: chatbot_20220408_models.ListUserSayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListUserSayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserSay',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.ListUserSayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_say(
        self,
        request: chatbot_20220408_models.ListUserSayRequest,
    ) -> chatbot_20220408_models.ListUserSayResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_say_with_options(request, runtime)

    async def list_user_say_async(
        self,
        request: chatbot_20220408_models.ListUserSayRequest,
    ) -> chatbot_20220408_models.ListUserSayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_say_with_options_async(request, runtime)

    def nlu_with_options(
        self,
        request: chatbot_20220408_models.NluRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.NluResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Nlu',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.NluResponse(),
            self.call_api(params, req, runtime)
        )

    async def nlu_with_options_async(
        self,
        request: chatbot_20220408_models.NluRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.NluResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Nlu',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.NluResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def nlu(
        self,
        request: chatbot_20220408_models.NluRequest,
    ) -> chatbot_20220408_models.NluResponse:
        runtime = util_models.RuntimeOptions()
        return self.nlu_with_options(request, runtime)

    async def nlu_async(
        self,
        request: chatbot_20220408_models.NluRequest,
    ) -> chatbot_20220408_models.NluResponse:
        runtime = util_models.RuntimeOptions()
        return await self.nlu_with_options_async(request, runtime)

    def query_perspectives_with_options(
        self,
        request: chatbot_20220408_models.QueryPerspectivesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.QueryPerspectivesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPerspectives',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.QueryPerspectivesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_perspectives_with_options_async(
        self,
        request: chatbot_20220408_models.QueryPerspectivesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.QueryPerspectivesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPerspectives',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.QueryPerspectivesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_perspectives(
        self,
        request: chatbot_20220408_models.QueryPerspectivesRequest,
    ) -> chatbot_20220408_models.QueryPerspectivesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_perspectives_with_options(request, runtime)

    async def query_perspectives_async(
        self,
        request: chatbot_20220408_models.QueryPerspectivesRequest,
    ) -> chatbot_20220408_models.QueryPerspectivesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_perspectives_with_options_async(request, runtime)

    def search_faq_with_options(
        self,
        tmp_req: chatbot_20220408_models.SearchFaqRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.SearchFaqResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.SearchFaqShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.category_ids):
            request.category_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.category_ids_shrink):
            body['CategoryIds'] = request.category_ids_shrink
        if not UtilClient.is_unset(request.create_time_begin):
            body['CreateTimeBegin'] = request.create_time_begin
        if not UtilClient.is_unset(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_user_name):
            body['CreateUserName'] = request.create_user_name
        if not UtilClient.is_unset(request.end_time_begin):
            body['EndTimeBegin'] = request.end_time_begin
        if not UtilClient.is_unset(request.end_time_end):
            body['EndTimeEnd'] = request.end_time_end
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.modify_time_begin):
            body['ModifyTimeBegin'] = request.modify_time_begin
        if not UtilClient.is_unset(request.modify_time_end):
            body['ModifyTimeEnd'] = request.modify_time_end
        if not UtilClient.is_unset(request.modify_user_name):
            body['ModifyUserName'] = request.modify_user_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_scope):
            body['SearchScope'] = request.search_scope
        if not UtilClient.is_unset(request.start_time_begin):
            body['StartTimeBegin'] = request.start_time_begin
        if not UtilClient.is_unset(request.start_time_end):
            body['StartTimeEnd'] = request.start_time_end
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchFaq',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.SearchFaqResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_faq_with_options_async(
        self,
        tmp_req: chatbot_20220408_models.SearchFaqRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.SearchFaqResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.SearchFaqShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.category_ids):
            request.category_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.category_ids_shrink):
            body['CategoryIds'] = request.category_ids_shrink
        if not UtilClient.is_unset(request.create_time_begin):
            body['CreateTimeBegin'] = request.create_time_begin
        if not UtilClient.is_unset(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_user_name):
            body['CreateUserName'] = request.create_user_name
        if not UtilClient.is_unset(request.end_time_begin):
            body['EndTimeBegin'] = request.end_time_begin
        if not UtilClient.is_unset(request.end_time_end):
            body['EndTimeEnd'] = request.end_time_end
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.modify_time_begin):
            body['ModifyTimeBegin'] = request.modify_time_begin
        if not UtilClient.is_unset(request.modify_time_end):
            body['ModifyTimeEnd'] = request.modify_time_end
        if not UtilClient.is_unset(request.modify_user_name):
            body['ModifyUserName'] = request.modify_user_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_scope):
            body['SearchScope'] = request.search_scope
        if not UtilClient.is_unset(request.start_time_begin):
            body['StartTimeBegin'] = request.start_time_begin
        if not UtilClient.is_unset(request.start_time_end):
            body['StartTimeEnd'] = request.start_time_end
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchFaq',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.SearchFaqResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_faq(
        self,
        request: chatbot_20220408_models.SearchFaqRequest,
    ) -> chatbot_20220408_models.SearchFaqResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_faq_with_options(request, runtime)

    async def search_faq_async(
        self,
        request: chatbot_20220408_models.SearchFaqRequest,
    ) -> chatbot_20220408_models.SearchFaqResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_faq_with_options_async(request, runtime)

    def update_category_with_options(
        self,
        request: chatbot_20220408_models.UpdateCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCategory',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_category_with_options_async(
        self,
        request: chatbot_20220408_models.UpdateCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCategory',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_category(
        self,
        request: chatbot_20220408_models.UpdateCategoryRequest,
    ) -> chatbot_20220408_models.UpdateCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_category_with_options(request, runtime)

    async def update_category_async(
        self,
        request: chatbot_20220408_models.UpdateCategoryRequest,
    ) -> chatbot_20220408_models.UpdateCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_category_with_options_async(request, runtime)

    def update_conn_question_with_options(
        self,
        request: chatbot_20220408_models.UpdateConnQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateConnQuestionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.conn_question_id):
            body['ConnQuestionId'] = request.conn_question_id
        if not UtilClient.is_unset(request.outline_id):
            body['OutlineId'] = request.outline_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConnQuestion',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateConnQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_conn_question_with_options_async(
        self,
        request: chatbot_20220408_models.UpdateConnQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateConnQuestionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.conn_question_id):
            body['ConnQuestionId'] = request.conn_question_id
        if not UtilClient.is_unset(request.outline_id):
            body['OutlineId'] = request.outline_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConnQuestion',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateConnQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_conn_question(
        self,
        request: chatbot_20220408_models.UpdateConnQuestionRequest,
    ) -> chatbot_20220408_models.UpdateConnQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_conn_question_with_options(request, runtime)

    async def update_conn_question_async(
        self,
        request: chatbot_20220408_models.UpdateConnQuestionRequest,
    ) -> chatbot_20220408_models.UpdateConnQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_conn_question_with_options_async(request, runtime)

    def update_dsentity_with_options(
        self,
        request: chatbot_20220408_models.UpdateDSEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateDSEntityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.entity_name):
            query['EntityName'] = request.entity_name
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDSEntity',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateDSEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dsentity_with_options_async(
        self,
        request: chatbot_20220408_models.UpdateDSEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateDSEntityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.entity_name):
            query['EntityName'] = request.entity_name
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDSEntity',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateDSEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dsentity(
        self,
        request: chatbot_20220408_models.UpdateDSEntityRequest,
    ) -> chatbot_20220408_models.UpdateDSEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_dsentity_with_options(request, runtime)

    async def update_dsentity_async(
        self,
        request: chatbot_20220408_models.UpdateDSEntityRequest,
    ) -> chatbot_20220408_models.UpdateDSEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dsentity_with_options_async(request, runtime)

    def update_dsentity_value_with_options(
        self,
        tmp_req: chatbot_20220408_models.UpdateDSEntityValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateDSEntityValueResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.UpdateDSEntityValueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.synonyms):
            request.synonyms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.synonyms, 'Synonyms', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.entity_value_id):
            query['EntityValueId'] = request.entity_value_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.synonyms_shrink):
            body['Synonyms'] = request.synonyms_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDSEntityValue',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateDSEntityValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dsentity_value_with_options_async(
        self,
        tmp_req: chatbot_20220408_models.UpdateDSEntityValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateDSEntityValueResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.UpdateDSEntityValueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.synonyms):
            request.synonyms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.synonyms, 'Synonyms', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.entity_value_id):
            query['EntityValueId'] = request.entity_value_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.synonyms_shrink):
            body['Synonyms'] = request.synonyms_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDSEntityValue',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateDSEntityValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dsentity_value(
        self,
        request: chatbot_20220408_models.UpdateDSEntityValueRequest,
    ) -> chatbot_20220408_models.UpdateDSEntityValueResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_dsentity_value_with_options(request, runtime)

    async def update_dsentity_value_async(
        self,
        request: chatbot_20220408_models.UpdateDSEntityValueRequest,
    ) -> chatbot_20220408_models.UpdateDSEntityValueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dsentity_value_with_options_async(request, runtime)

    def update_faq_with_options(
        self,
        request: chatbot_20220408_models.UpdateFaqRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateFaqResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFaq',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateFaqResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_faq_with_options_async(
        self,
        request: chatbot_20220408_models.UpdateFaqRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateFaqResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFaq',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateFaqResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_faq(
        self,
        request: chatbot_20220408_models.UpdateFaqRequest,
    ) -> chatbot_20220408_models.UpdateFaqResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_faq_with_options(request, runtime)

    async def update_faq_async(
        self,
        request: chatbot_20220408_models.UpdateFaqRequest,
    ) -> chatbot_20220408_models.UpdateFaqResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_faq_with_options_async(request, runtime)

    def update_instance_with_options(
        self,
        request: chatbot_20220408_models.UpdateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.introduction):
            query['Introduction'] = request.introduction
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        request: chatbot_20220408_models.UpdateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.introduction):
            query['Introduction'] = request.introduction
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        request: chatbot_20220408_models.UpdateInstanceRequest,
    ) -> chatbot_20220408_models.UpdateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_instance_with_options(request, runtime)

    async def update_instance_async(
        self,
        request: chatbot_20220408_models.UpdateInstanceRequest,
    ) -> chatbot_20220408_models.UpdateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_with_options_async(request, runtime)

    def update_intent_with_options(
        self,
        tmp_req: chatbot_20220408_models.UpdateIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateIntentResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.UpdateIntentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_definition):
            request.intent_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.intent_definition), 'IntentDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIntent',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateIntentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_intent_with_options_async(
        self,
        tmp_req: chatbot_20220408_models.UpdateIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateIntentResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.UpdateIntentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_definition):
            request.intent_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.intent_definition), 'IntentDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIntent',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateIntentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_intent(
        self,
        request: chatbot_20220408_models.UpdateIntentRequest,
    ) -> chatbot_20220408_models.UpdateIntentResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_intent_with_options(request, runtime)

    async def update_intent_async(
        self,
        request: chatbot_20220408_models.UpdateIntentRequest,
    ) -> chatbot_20220408_models.UpdateIntentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_intent_with_options_async(request, runtime)

    def update_lgf_with_options(
        self,
        tmp_req: chatbot_20220408_models.UpdateLgfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateLgfResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.UpdateLgfShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lgf_definition):
            request.lgf_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.lgf_definition), 'LgfDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lgf_definition_shrink):
            query['LgfDefinition'] = request.lgf_definition_shrink
        if not UtilClient.is_unset(request.lgf_id):
            query['LgfId'] = request.lgf_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLgf',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateLgfResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_lgf_with_options_async(
        self,
        tmp_req: chatbot_20220408_models.UpdateLgfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateLgfResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.UpdateLgfShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lgf_definition):
            request.lgf_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.lgf_definition), 'LgfDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lgf_definition_shrink):
            query['LgfDefinition'] = request.lgf_definition_shrink
        if not UtilClient.is_unset(request.lgf_id):
            query['LgfId'] = request.lgf_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLgf',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateLgfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_lgf(
        self,
        request: chatbot_20220408_models.UpdateLgfRequest,
    ) -> chatbot_20220408_models.UpdateLgfResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_lgf_with_options(request, runtime)

    async def update_lgf_async(
        self,
        request: chatbot_20220408_models.UpdateLgfRequest,
    ) -> chatbot_20220408_models.UpdateLgfResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_lgf_with_options_async(request, runtime)

    def update_perspective_with_options(
        self,
        request: chatbot_20220408_models.UpdatePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdatePerspectiveResponse:
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
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdatePerspectiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_perspective_with_options_async(
        self,
        request: chatbot_20220408_models.UpdatePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdatePerspectiveResponse:
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
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdatePerspectiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_perspective(
        self,
        request: chatbot_20220408_models.UpdatePerspectiveRequest,
    ) -> chatbot_20220408_models.UpdatePerspectiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_perspective_with_options(request, runtime)

    async def update_perspective_async(
        self,
        request: chatbot_20220408_models.UpdatePerspectiveRequest,
    ) -> chatbot_20220408_models.UpdatePerspectiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_perspective_with_options_async(request, runtime)

    def update_sim_question_with_options(
        self,
        request: chatbot_20220408_models.UpdateSimQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateSimQuestionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.sim_question_id):
            body['SimQuestionId'] = request.sim_question_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSimQuestion',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateSimQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sim_question_with_options_async(
        self,
        request: chatbot_20220408_models.UpdateSimQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateSimQuestionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.sim_question_id):
            body['SimQuestionId'] = request.sim_question_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSimQuestion',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateSimQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sim_question(
        self,
        request: chatbot_20220408_models.UpdateSimQuestionRequest,
    ) -> chatbot_20220408_models.UpdateSimQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_sim_question_with_options(request, runtime)

    async def update_sim_question_async(
        self,
        request: chatbot_20220408_models.UpdateSimQuestionRequest,
    ) -> chatbot_20220408_models.UpdateSimQuestionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_sim_question_with_options_async(request, runtime)

    def update_solution_with_options(
        self,
        request: chatbot_20220408_models.UpdateSolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateSolutionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_type):
            body['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.perspective_codes):
            body['PerspectiveCodes'] = request.perspective_codes
        if not UtilClient.is_unset(request.solution_id):
            body['SolutionId'] = request.solution_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSolution',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateSolutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_solution_with_options_async(
        self,
        request: chatbot_20220408_models.UpdateSolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateSolutionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_type):
            body['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.perspective_codes):
            body['PerspectiveCodes'] = request.perspective_codes
        if not UtilClient.is_unset(request.solution_id):
            body['SolutionId'] = request.solution_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSolution',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateSolutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_solution(
        self,
        request: chatbot_20220408_models.UpdateSolutionRequest,
    ) -> chatbot_20220408_models.UpdateSolutionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_solution_with_options(request, runtime)

    async def update_solution_async(
        self,
        request: chatbot_20220408_models.UpdateSolutionRequest,
    ) -> chatbot_20220408_models.UpdateSolutionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_solution_with_options_async(request, runtime)

    def update_user_say_with_options(
        self,
        tmp_req: chatbot_20220408_models.UpdateUserSayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateUserSayResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.UpdateUserSayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_say_definition):
            request.user_say_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_say_definition), 'UserSayDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_say_definition_shrink):
            query['UserSayDefinition'] = request.user_say_definition_shrink
        if not UtilClient.is_unset(request.user_say_id):
            query['UserSayId'] = request.user_say_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserSay',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateUserSayResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_say_with_options_async(
        self,
        tmp_req: chatbot_20220408_models.UpdateUserSayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateUserSayResponse:
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.UpdateUserSayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_say_definition):
            request.user_say_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user_say_definition), 'UserSayDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_say_definition_shrink):
            query['UserSayDefinition'] = request.user_say_definition_shrink
        if not UtilClient.is_unset(request.user_say_id):
            query['UserSayId'] = request.user_say_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserSay',
            version='2022-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20220408_models.UpdateUserSayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_say(
        self,
        request: chatbot_20220408_models.UpdateUserSayRequest,
    ) -> chatbot_20220408_models.UpdateUserSayResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_say_with_options(request, runtime)

    async def update_user_say_async(
        self,
        request: chatbot_20220408_models.UpdateUserSayRequest,
    ) -> chatbot_20220408_models.UpdateUserSayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_say_with_options_async(request, runtime)
