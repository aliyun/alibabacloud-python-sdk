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

    def apply_for_stream_access_token_with_options(
        self,
        request: chatbot_20220408_models.ApplyForStreamAccessTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ApplyForStreamAccessTokenResponse:
        """
        @summary 申请流式网关AccessToken
        
        @param request: ApplyForStreamAccessTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyForStreamAccessTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyForStreamAccessToken',
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
            chatbot_20220408_models.ApplyForStreamAccessTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_for_stream_access_token_with_options_async(
        self,
        request: chatbot_20220408_models.ApplyForStreamAccessTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ApplyForStreamAccessTokenResponse:
        """
        @summary 申请流式网关AccessToken
        
        @param request: ApplyForStreamAccessTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyForStreamAccessTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyForStreamAccessToken',
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
            chatbot_20220408_models.ApplyForStreamAccessTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_for_stream_access_token(
        self,
        request: chatbot_20220408_models.ApplyForStreamAccessTokenRequest,
    ) -> chatbot_20220408_models.ApplyForStreamAccessTokenResponse:
        """
        @summary 申请流式网关AccessToken
        
        @param request: ApplyForStreamAccessTokenRequest
        @return: ApplyForStreamAccessTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_for_stream_access_token_with_options(request, runtime)

    async def apply_for_stream_access_token_async(
        self,
        request: chatbot_20220408_models.ApplyForStreamAccessTokenRequest,
    ) -> chatbot_20220408_models.ApplyForStreamAccessTokenResponse:
        """
        @summary 申请流式网关AccessToken
        
        @param request: ApplyForStreamAccessTokenRequest
        @return: ApplyForStreamAccessTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.apply_for_stream_access_token_with_options_async(request, runtime)

    def associate_with_options(
        self,
        tmp_req: chatbot_20220408_models.AssociateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.AssociateResponse:
        """
        @summary 会话-联想API
        
        @param tmp_req: AssociateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateResponse
        """
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
        """
        @summary 会话-联想API
        
        @param tmp_req: AssociateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateResponse
        """
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
        """
        @summary 会话-联想API
        
        @param request: AssociateRequest
        @return: AssociateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_with_options(request, runtime)

    async def associate_async(
        self,
        request: chatbot_20220408_models.AssociateRequest,
    ) -> chatbot_20220408_models.AssociateResponse:
        """
        @summary 会话-联想API
        
        @param request: AssociateRequest
        @return: AssociateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.associate_with_options_async(request, runtime)

    def begin_session_with_options(
        self,
        request: chatbot_20220408_models.BeginSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.BeginSessionResponse:
        """
        @summary 获取欢迎语
        
        @param request: BeginSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BeginSessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sand_box):
            body['SandBox'] = request.sand_box
        if not UtilClient.is_unset(request.vendor_param):
            body['VendorParam'] = request.vendor_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        """
        @summary 获取欢迎语
        
        @param request: BeginSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BeginSessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sand_box):
            body['SandBox'] = request.sand_box
        if not UtilClient.is_unset(request.vendor_param):
            body['VendorParam'] = request.vendor_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        """
        @summary 获取欢迎语
        
        @param request: BeginSessionRequest
        @return: BeginSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.begin_session_with_options(request, runtime)

    async def begin_session_async(
        self,
        request: chatbot_20220408_models.BeginSessionRequest,
    ) -> chatbot_20220408_models.BeginSessionResponse:
        """
        @summary 获取欢迎语
        
        @param request: BeginSessionRequest
        @return: BeginSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.begin_session_with_options_async(request, runtime)

    def cancel_instance_publish_task_with_options(
        self,
        request: chatbot_20220408_models.CancelInstancePublishTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CancelInstancePublishTaskResponse:
        """
        @summary 取消机器人发布
        
        @param request: CancelInstancePublishTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelInstancePublishTaskResponse
        """
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
        """
        @summary 取消机器人发布
        
        @param request: CancelInstancePublishTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelInstancePublishTaskResponse
        """
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
        """
        @summary 取消机器人发布
        
        @param request: CancelInstancePublishTaskRequest
        @return: CancelInstancePublishTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_instance_publish_task_with_options(request, runtime)

    async def cancel_instance_publish_task_async(
        self,
        request: chatbot_20220408_models.CancelInstancePublishTaskRequest,
    ) -> chatbot_20220408_models.CancelInstancePublishTaskResponse:
        """
        @summary 取消机器人发布
        
        @param request: CancelInstancePublishTaskRequest
        @return: CancelInstancePublishTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_instance_publish_task_with_options_async(request, runtime)

    def cancel_publish_task_with_options(
        self,
        request: chatbot_20220408_models.CancelPublishTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CancelPublishTaskResponse:
        """
        @summary 取消发布任务
        
        @param request: CancelPublishTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelPublishTaskResponse
        """
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
        """
        @summary 取消发布任务
        
        @param request: CancelPublishTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelPublishTaskResponse
        """
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
        """
        @summary 取消发布任务
        
        @param request: CancelPublishTaskRequest
        @return: CancelPublishTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_publish_task_with_options(request, runtime)

    async def cancel_publish_task_async(
        self,
        request: chatbot_20220408_models.CancelPublishTaskRequest,
    ) -> chatbot_20220408_models.CancelPublishTaskResponse:
        """
        @summary 取消发布任务
        
        @param request: CancelPublishTaskRequest
        @return: CancelPublishTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_publish_task_with_options_async(request, runtime)

    def chat_with_options(
        self,
        tmp_req: chatbot_20220408_models.ChatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ChatResponse:
        """
        @summary 会话API
        
        @param tmp_req: ChatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatResponse
        """
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
        if not UtilClient.is_unset(request.sand_box):
            query['SandBox'] = request.sand_box
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
        """
        @summary 会话API
        
        @param tmp_req: ChatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatResponse
        """
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
        if not UtilClient.is_unset(request.sand_box):
            query['SandBox'] = request.sand_box
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
        """
        @summary 会话API
        
        @param request: ChatRequest
        @return: ChatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.chat_with_options(request, runtime)

    async def chat_async(
        self,
        request: chatbot_20220408_models.ChatRequest,
    ) -> chatbot_20220408_models.ChatResponse:
        """
        @summary 会话API
        
        @param request: ChatRequest
        @return: ChatResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.chat_with_options_async(request, runtime)

    def continue_instance_publish_task_with_options(
        self,
        request: chatbot_20220408_models.ContinueInstancePublishTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ContinueInstancePublishTaskResponse:
        """
        @summary 继续机器人发布
        
        @param request: ContinueInstancePublishTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContinueInstancePublishTaskResponse
        """
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
        """
        @summary 继续机器人发布
        
        @param request: ContinueInstancePublishTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContinueInstancePublishTaskResponse
        """
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
        """
        @summary 继续机器人发布
        
        @param request: ContinueInstancePublishTaskRequest
        @return: ContinueInstancePublishTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.continue_instance_publish_task_with_options(request, runtime)

    async def continue_instance_publish_task_async(
        self,
        request: chatbot_20220408_models.ContinueInstancePublishTaskRequest,
    ) -> chatbot_20220408_models.ContinueInstancePublishTaskResponse:
        """
        @summary 继续机器人发布
        
        @param request: ContinueInstancePublishTaskRequest
        @return: ContinueInstancePublishTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.continue_instance_publish_task_with_options_async(request, runtime)

    def create_category_with_options(
        self,
        request: chatbot_20220408_models.CreateCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateCategoryResponse:
        """
        @summary 新增类目
        
        @param request: CreateCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.biz_code):
            body['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.knowledge_type):
            body['KnowledgeType'] = request.knowledge_type
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
        """
        @summary 新增类目
        
        @param request: CreateCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.biz_code):
            body['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.knowledge_type):
            body['KnowledgeType'] = request.knowledge_type
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
        """
        @summary 新增类目
        
        @param request: CreateCategoryRequest
        @return: CreateCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_category_with_options(request, runtime)

    async def create_category_async(
        self,
        request: chatbot_20220408_models.CreateCategoryRequest,
    ) -> chatbot_20220408_models.CreateCategoryResponse:
        """
        @summary 新增类目
        
        @param request: CreateCategoryRequest
        @return: CreateCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_category_with_options_async(request, runtime)

    def create_conn_question_with_options(
        self,
        request: chatbot_20220408_models.CreateConnQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateConnQuestionResponse:
        """
        @summary 新建FAQ关联问
        
        @param request: CreateConnQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConnQuestionResponse
        """
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
        """
        @summary 新建FAQ关联问
        
        @param request: CreateConnQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConnQuestionResponse
        """
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
        """
        @summary 新建FAQ关联问
        
        @param request: CreateConnQuestionRequest
        @return: CreateConnQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_conn_question_with_options(request, runtime)

    async def create_conn_question_async(
        self,
        request: chatbot_20220408_models.CreateConnQuestionRequest,
    ) -> chatbot_20220408_models.CreateConnQuestionResponse:
        """
        @summary 新建FAQ关联问
        
        @param request: CreateConnQuestionRequest
        @return: CreateConnQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_conn_question_with_options_async(request, runtime)

    def create_dsentity_with_options(
        self,
        request: chatbot_20220408_models.CreateDSEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateDSEntityResponse:
        """
        @summary 实体-创建
        
        @param request: CreateDSEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDSEntityResponse
        """
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
        """
        @summary 实体-创建
        
        @param request: CreateDSEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDSEntityResponse
        """
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
        """
        @summary 实体-创建
        
        @param request: CreateDSEntityRequest
        @return: CreateDSEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dsentity_with_options(request, runtime)

    async def create_dsentity_async(
        self,
        request: chatbot_20220408_models.CreateDSEntityRequest,
    ) -> chatbot_20220408_models.CreateDSEntityResponse:
        """
        @summary 实体-创建
        
        @param request: CreateDSEntityRequest
        @return: CreateDSEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dsentity_with_options_async(request, runtime)

    def create_dsentity_value_with_options(
        self,
        tmp_req: chatbot_20220408_models.CreateDSEntityValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateDSEntityValueResponse:
        """
        @summary 实体成员-创建
        
        @param tmp_req: CreateDSEntityValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDSEntityValueResponse
        """
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
        """
        @summary 实体成员-创建
        
        @param tmp_req: CreateDSEntityValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDSEntityValueResponse
        """
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
        """
        @summary 实体成员-创建
        
        @param request: CreateDSEntityValueRequest
        @return: CreateDSEntityValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dsentity_value_with_options(request, runtime)

    async def create_dsentity_value_async(
        self,
        request: chatbot_20220408_models.CreateDSEntityValueRequest,
    ) -> chatbot_20220408_models.CreateDSEntityValueResponse:
        """
        @summary 实体成员-创建
        
        @param request: CreateDSEntityValueRequest
        @return: CreateDSEntityValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dsentity_value_with_options_async(request, runtime)

    def create_doc_with_options(
        self,
        tmp_req: chatbot_20220408_models.CreateDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateDocResponse:
        """
        @summary 创建文档
        
        @param tmp_req: CreateDocRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDocResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreateDocShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_metadata):
            request.doc_metadata_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_metadata, 'DocMetadata', 'json')
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.doc_metadata_shrink):
            query['DocMetadata'] = request.doc_metadata_shrink
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.meta):
            query['Meta'] = request.meta
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.tag_ids_shrink):
            query['TagIds'] = request.tag_ids_shrink
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDoc',
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
            chatbot_20220408_models.CreateDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_doc_with_options_async(
        self,
        tmp_req: chatbot_20220408_models.CreateDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateDocResponse:
        """
        @summary 创建文档
        
        @param tmp_req: CreateDocRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDocResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreateDocShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_metadata):
            request.doc_metadata_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_metadata, 'DocMetadata', 'json')
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.doc_metadata_shrink):
            query['DocMetadata'] = request.doc_metadata_shrink
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.meta):
            query['Meta'] = request.meta
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.tag_ids_shrink):
            query['TagIds'] = request.tag_ids_shrink
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDoc',
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
            chatbot_20220408_models.CreateDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_doc(
        self,
        request: chatbot_20220408_models.CreateDocRequest,
    ) -> chatbot_20220408_models.CreateDocResponse:
        """
        @summary 创建文档
        
        @param request: CreateDocRequest
        @return: CreateDocResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_doc_with_options(request, runtime)

    async def create_doc_async(
        self,
        request: chatbot_20220408_models.CreateDocRequest,
    ) -> chatbot_20220408_models.CreateDocResponse:
        """
        @summary 创建文档
        
        @param request: CreateDocRequest
        @return: CreateDocResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_doc_with_options_async(request, runtime)

    def create_faq_with_options(
        self,
        tmp_req: chatbot_20220408_models.CreateFaqRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateFaqResponse:
        """
        @summary 新建FAQ
        
        @param tmp_req: CreateFaqRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFaqResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreateFaqShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag_id_list):
            request.tag_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_id_list, 'TagIdList', 'json')
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
        if not UtilClient.is_unset(request.tag_id_list_shrink):
            body['TagIdList'] = request.tag_id_list_shrink
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
        tmp_req: chatbot_20220408_models.CreateFaqRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateFaqResponse:
        """
        @summary 新建FAQ
        
        @param tmp_req: CreateFaqRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFaqResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreateFaqShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag_id_list):
            request.tag_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_id_list, 'TagIdList', 'json')
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
        if not UtilClient.is_unset(request.tag_id_list_shrink):
            body['TagIdList'] = request.tag_id_list_shrink
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
        """
        @summary 新建FAQ
        
        @param request: CreateFaqRequest
        @return: CreateFaqResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_faq_with_options(request, runtime)

    async def create_faq_async(
        self,
        request: chatbot_20220408_models.CreateFaqRequest,
    ) -> chatbot_20220408_models.CreateFaqResponse:
        """
        @summary 新建FAQ
        
        @param request: CreateFaqRequest
        @return: CreateFaqResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_faq_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: chatbot_20220408_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateInstanceResponse:
        """
        @summary 机器人-创建
        
        @param request: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
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
        """
        @summary 机器人-创建
        
        @param request: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
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
        """
        @summary 机器人-创建
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: chatbot_20220408_models.CreateInstanceRequest,
    ) -> chatbot_20220408_models.CreateInstanceResponse:
        """
        @summary 机器人-创建
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_instance_publish_task_with_options(
        self,
        request: chatbot_20220408_models.CreateInstancePublishTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateInstancePublishTaskResponse:
        """
        @summary 创建机器人发布任务
        
        @param request: CreateInstancePublishTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstancePublishTaskResponse
        """
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
        """
        @summary 创建机器人发布任务
        
        @param request: CreateInstancePublishTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstancePublishTaskResponse
        """
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
        """
        @summary 创建机器人发布任务
        
        @param request: CreateInstancePublishTaskRequest
        @return: CreateInstancePublishTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instance_publish_task_with_options(request, runtime)

    async def create_instance_publish_task_async(
        self,
        request: chatbot_20220408_models.CreateInstancePublishTaskRequest,
    ) -> chatbot_20220408_models.CreateInstancePublishTaskResponse:
        """
        @summary 创建机器人发布任务
        
        @param request: CreateInstancePublishTaskRequest
        @return: CreateInstancePublishTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_publish_task_with_options_async(request, runtime)

    def create_intent_with_options(
        self,
        tmp_req: chatbot_20220408_models.CreateIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateIntentResponse:
        """
        @summary 意图-创建
        
        @param tmp_req: CreateIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIntentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreateIntentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_definition):
            request.intent_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.intent_definition, 'IntentDefinition', 'json')
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
        """
        @summary 意图-创建
        
        @param tmp_req: CreateIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIntentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreateIntentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_definition):
            request.intent_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.intent_definition, 'IntentDefinition', 'json')
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
        """
        @summary 意图-创建
        
        @param request: CreateIntentRequest
        @return: CreateIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_intent_with_options(request, runtime)

    async def create_intent_async(
        self,
        request: chatbot_20220408_models.CreateIntentRequest,
    ) -> chatbot_20220408_models.CreateIntentResponse:
        """
        @summary 意图-创建
        
        @param request: CreateIntentRequest
        @return: CreateIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_intent_with_options_async(request, runtime)

    def create_lgf_with_options(
        self,
        tmp_req: chatbot_20220408_models.CreateLgfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateLgfResponse:
        """
        @summary 意图-LGF-创建
        
        @param tmp_req: CreateLgfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLgfResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreateLgfShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lgf_definition):
            request.lgf_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lgf_definition, 'LgfDefinition', 'json')
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
        """
        @summary 意图-LGF-创建
        
        @param tmp_req: CreateLgfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLgfResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreateLgfShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lgf_definition):
            request.lgf_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lgf_definition, 'LgfDefinition', 'json')
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
        """
        @summary 意图-LGF-创建
        
        @param request: CreateLgfRequest
        @return: CreateLgfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_lgf_with_options(request, runtime)

    async def create_lgf_async(
        self,
        request: chatbot_20220408_models.CreateLgfRequest,
    ) -> chatbot_20220408_models.CreateLgfResponse:
        """
        @summary 意图-LGF-创建
        
        @param request: CreateLgfRequest
        @return: CreateLgfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_lgf_with_options_async(request, runtime)

    def create_perspective_with_options(
        self,
        request: chatbot_20220408_models.CreatePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreatePerspectiveResponse:
        """
        @summary 视角-创建
        
        @param request: CreatePerspectiveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePerspectiveResponse
        """
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
        """
        @summary 视角-创建
        
        @param request: CreatePerspectiveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePerspectiveResponse
        """
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
        """
        @summary 视角-创建
        
        @param request: CreatePerspectiveRequest
        @return: CreatePerspectiveResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_perspective_with_options(request, runtime)

    async def create_perspective_async(
        self,
        request: chatbot_20220408_models.CreatePerspectiveRequest,
    ) -> chatbot_20220408_models.CreatePerspectiveResponse:
        """
        @summary 视角-创建
        
        @param request: CreatePerspectiveRequest
        @return: CreatePerspectiveResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_perspective_with_options_async(request, runtime)

    def create_publish_task_with_options(
        self,
        tmp_req: chatbot_20220408_models.CreatePublishTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreatePublishTaskResponse:
        """
        @summary 创建发布任务
        
        @param tmp_req: CreatePublishTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePublishTaskResponse
        """
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
        """
        @summary 创建发布任务
        
        @param tmp_req: CreatePublishTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePublishTaskResponse
        """
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
        """
        @summary 创建发布任务
        
        @param request: CreatePublishTaskRequest
        @return: CreatePublishTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_publish_task_with_options(request, runtime)

    async def create_publish_task_async(
        self,
        request: chatbot_20220408_models.CreatePublishTaskRequest,
    ) -> chatbot_20220408_models.CreatePublishTaskResponse:
        """
        @summary 创建发布任务
        
        @param request: CreatePublishTaskRequest
        @return: CreatePublishTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_publish_task_with_options_async(request, runtime)

    def create_sim_question_with_options(
        self,
        request: chatbot_20220408_models.CreateSimQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateSimQuestionResponse:
        """
        @summary 新建FAQ相似问
        
        @param request: CreateSimQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSimQuestionResponse
        """
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
        """
        @summary 新建FAQ相似问
        
        @param request: CreateSimQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSimQuestionResponse
        """
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
        """
        @summary 新建FAQ相似问
        
        @param request: CreateSimQuestionRequest
        @return: CreateSimQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sim_question_with_options(request, runtime)

    async def create_sim_question_async(
        self,
        request: chatbot_20220408_models.CreateSimQuestionRequest,
    ) -> chatbot_20220408_models.CreateSimQuestionResponse:
        """
        @summary 新建FAQ相似问
        
        @param request: CreateSimQuestionRequest
        @return: CreateSimQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sim_question_with_options_async(request, runtime)

    def create_solution_with_options(
        self,
        tmp_req: chatbot_20220408_models.CreateSolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateSolutionResponse:
        """
        @summary 新建FAQ答案
        
        @param tmp_req: CreateSolutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSolutionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreateSolutionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag_id_list):
            request.tag_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_id_list, 'TagIdList', 'json')
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
        body = {}
        if not UtilClient.is_unset(request.tag_id_list_shrink):
            body['TagIdList'] = request.tag_id_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        tmp_req: chatbot_20220408_models.CreateSolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateSolutionResponse:
        """
        @summary 新建FAQ答案
        
        @param tmp_req: CreateSolutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSolutionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreateSolutionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag_id_list):
            request.tag_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_id_list, 'TagIdList', 'json')
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
        body = {}
        if not UtilClient.is_unset(request.tag_id_list_shrink):
            body['TagIdList'] = request.tag_id_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        """
        @summary 新建FAQ答案
        
        @param request: CreateSolutionRequest
        @return: CreateSolutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_solution_with_options(request, runtime)

    async def create_solution_async(
        self,
        request: chatbot_20220408_models.CreateSolutionRequest,
    ) -> chatbot_20220408_models.CreateSolutionResponse:
        """
        @summary 新建FAQ答案
        
        @param request: CreateSolutionRequest
        @return: CreateSolutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_solution_with_options_async(request, runtime)

    def create_tag_with_options(
        self,
        request: chatbot_20220408_models.CreateTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateTagResponse:
        """
        @summary 标签创建
        
        @param request: CreateTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.tag_name):
            body['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTag',
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
            chatbot_20220408_models.CreateTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tag_with_options_async(
        self,
        request: chatbot_20220408_models.CreateTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateTagResponse:
        """
        @summary 标签创建
        
        @param request: CreateTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.tag_name):
            body['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTag',
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
            chatbot_20220408_models.CreateTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tag(
        self,
        request: chatbot_20220408_models.CreateTagRequest,
    ) -> chatbot_20220408_models.CreateTagResponse:
        """
        @summary 标签创建
        
        @param request: CreateTagRequest
        @return: CreateTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_tag_with_options(request, runtime)

    async def create_tag_async(
        self,
        request: chatbot_20220408_models.CreateTagRequest,
    ) -> chatbot_20220408_models.CreateTagResponse:
        """
        @summary 标签创建
        
        @param request: CreateTagRequest
        @return: CreateTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_tag_with_options_async(request, runtime)

    def create_tag_group_with_options(
        self,
        request: chatbot_20220408_models.CreateTagGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateTagGroupResponse:
        """
        @summary 标签组创建
        
        @param request: CreateTagGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTagGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTagGroup',
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
            chatbot_20220408_models.CreateTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tag_group_with_options_async(
        self,
        request: chatbot_20220408_models.CreateTagGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateTagGroupResponse:
        """
        @summary 标签组创建
        
        @param request: CreateTagGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTagGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTagGroup',
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
            chatbot_20220408_models.CreateTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tag_group(
        self,
        request: chatbot_20220408_models.CreateTagGroupRequest,
    ) -> chatbot_20220408_models.CreateTagGroupResponse:
        """
        @summary 标签组创建
        
        @param request: CreateTagGroupRequest
        @return: CreateTagGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_tag_group_with_options(request, runtime)

    async def create_tag_group_async(
        self,
        request: chatbot_20220408_models.CreateTagGroupRequest,
    ) -> chatbot_20220408_models.CreateTagGroupResponse:
        """
        @summary 标签组创建
        
        @param request: CreateTagGroupRequest
        @return: CreateTagGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_tag_group_with_options_async(request, runtime)

    def create_user_say_with_options(
        self,
        tmp_req: chatbot_20220408_models.CreateUserSayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.CreateUserSayResponse:
        """
        @summary 意图-话术-创建
        
        @param tmp_req: CreateUserSayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserSayResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreateUserSayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_say_definition):
            request.user_say_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_say_definition, 'UserSayDefinition', 'json')
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
        """
        @summary 意图-话术-创建
        
        @param tmp_req: CreateUserSayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserSayResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.CreateUserSayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_say_definition):
            request.user_say_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_say_definition, 'UserSayDefinition', 'json')
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
        """
        @summary 意图-话术-创建
        
        @param request: CreateUserSayRequest
        @return: CreateUserSayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_user_say_with_options(request, runtime)

    async def create_user_say_async(
        self,
        request: chatbot_20220408_models.CreateUserSayRequest,
    ) -> chatbot_20220408_models.CreateUserSayResponse:
        """
        @summary 意图-话术-创建
        
        @param request: CreateUserSayRequest
        @return: CreateUserSayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_user_say_with_options_async(request, runtime)

    def delete_category_with_options(
        self,
        request: chatbot_20220408_models.DeleteCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteCategoryResponse:
        """
        @summary 删除类目
        
        @param request: DeleteCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCategoryResponse
        """
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
        """
        @summary 删除类目
        
        @param request: DeleteCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCategoryResponse
        """
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
        """
        @summary 删除类目
        
        @param request: DeleteCategoryRequest
        @return: DeleteCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_category_with_options(request, runtime)

    async def delete_category_async(
        self,
        request: chatbot_20220408_models.DeleteCategoryRequest,
    ) -> chatbot_20220408_models.DeleteCategoryResponse:
        """
        @summary 删除类目
        
        @param request: DeleteCategoryRequest
        @return: DeleteCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_category_with_options_async(request, runtime)

    def delete_conn_question_with_options(
        self,
        request: chatbot_20220408_models.DeleteConnQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteConnQuestionResponse:
        """
        @summary 删除FAQ关联问
        
        @param request: DeleteConnQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConnQuestionResponse
        """
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
        """
        @summary 删除FAQ关联问
        
        @param request: DeleteConnQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConnQuestionResponse
        """
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
        """
        @summary 删除FAQ关联问
        
        @param request: DeleteConnQuestionRequest
        @return: DeleteConnQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_conn_question_with_options(request, runtime)

    async def delete_conn_question_async(
        self,
        request: chatbot_20220408_models.DeleteConnQuestionRequest,
    ) -> chatbot_20220408_models.DeleteConnQuestionResponse:
        """
        @summary 删除FAQ关联问
        
        @param request: DeleteConnQuestionRequest
        @return: DeleteConnQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_conn_question_with_options_async(request, runtime)

    def delete_dsentity_with_options(
        self,
        request: chatbot_20220408_models.DeleteDSEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteDSEntityResponse:
        """
        @summary 实体-删除
        
        @param request: DeleteDSEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDSEntityResponse
        """
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
        """
        @summary 实体-删除
        
        @param request: DeleteDSEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDSEntityResponse
        """
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
        """
        @summary 实体-删除
        
        @param request: DeleteDSEntityRequest
        @return: DeleteDSEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dsentity_with_options(request, runtime)

    async def delete_dsentity_async(
        self,
        request: chatbot_20220408_models.DeleteDSEntityRequest,
    ) -> chatbot_20220408_models.DeleteDSEntityResponse:
        """
        @summary 实体-删除
        
        @param request: DeleteDSEntityRequest
        @return: DeleteDSEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dsentity_with_options_async(request, runtime)

    def delete_dsentity_value_with_options(
        self,
        request: chatbot_20220408_models.DeleteDSEntityValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteDSEntityValueResponse:
        """
        @summary 实体成员-删除
        
        @param request: DeleteDSEntityValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDSEntityValueResponse
        """
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
        """
        @summary 实体成员-删除
        
        @param request: DeleteDSEntityValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDSEntityValueResponse
        """
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
        """
        @summary 实体成员-删除
        
        @param request: DeleteDSEntityValueRequest
        @return: DeleteDSEntityValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dsentity_value_with_options(request, runtime)

    async def delete_dsentity_value_async(
        self,
        request: chatbot_20220408_models.DeleteDSEntityValueRequest,
    ) -> chatbot_20220408_models.DeleteDSEntityValueResponse:
        """
        @summary 实体成员-删除
        
        @param request: DeleteDSEntityValueRequest
        @return: DeleteDSEntityValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dsentity_value_with_options_async(request, runtime)

    def delete_doc_with_options(
        self,
        request: chatbot_20220408_models.DeleteDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteDocResponse:
        """
        @summary 文档删除
        
        @param request: DeleteDocRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDocResponse
        """
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
            action='DeleteDoc',
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
            chatbot_20220408_models.DeleteDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_doc_with_options_async(
        self,
        request: chatbot_20220408_models.DeleteDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteDocResponse:
        """
        @summary 文档删除
        
        @param request: DeleteDocRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDocResponse
        """
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
            action='DeleteDoc',
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
            chatbot_20220408_models.DeleteDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_doc(
        self,
        request: chatbot_20220408_models.DeleteDocRequest,
    ) -> chatbot_20220408_models.DeleteDocResponse:
        """
        @summary 文档删除
        
        @param request: DeleteDocRequest
        @return: DeleteDocResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_doc_with_options(request, runtime)

    async def delete_doc_async(
        self,
        request: chatbot_20220408_models.DeleteDocRequest,
    ) -> chatbot_20220408_models.DeleteDocResponse:
        """
        @summary 文档删除
        
        @param request: DeleteDocRequest
        @return: DeleteDocResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_doc_with_options_async(request, runtime)

    def delete_faq_with_options(
        self,
        request: chatbot_20220408_models.DeleteFaqRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteFaqResponse:
        """
        @summary 删除FAQ，如果是已发布的知识，删除之后，变成已删除未发布，需要发布才能真正删除
        
        @param request: DeleteFaqRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFaqResponse
        """
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
        """
        @summary 删除FAQ，如果是已发布的知识，删除之后，变成已删除未发布，需要发布才能真正删除
        
        @param request: DeleteFaqRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFaqResponse
        """
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
        """
        @summary 删除FAQ，如果是已发布的知识，删除之后，变成已删除未发布，需要发布才能真正删除
        
        @param request: DeleteFaqRequest
        @return: DeleteFaqResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_faq_with_options(request, runtime)

    async def delete_faq_async(
        self,
        request: chatbot_20220408_models.DeleteFaqRequest,
    ) -> chatbot_20220408_models.DeleteFaqResponse:
        """
        @summary 删除FAQ，如果是已发布的知识，删除之后，变成已删除未发布，需要发布才能真正删除
        
        @param request: DeleteFaqRequest
        @return: DeleteFaqResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_faq_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: chatbot_20220408_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteInstanceResponse:
        """
        @summary 机器人-删除
        
        @param request: DeleteInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
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
        """
        @summary 机器人-删除
        
        @param request: DeleteInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
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
        """
        @summary 机器人-删除
        
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: chatbot_20220408_models.DeleteInstanceRequest,
    ) -> chatbot_20220408_models.DeleteInstanceResponse:
        """
        @summary 机器人-删除
        
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_intent_with_options(
        self,
        request: chatbot_20220408_models.DeleteIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteIntentResponse:
        """
        @summary 意图-删除
        
        @param request: DeleteIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIntentResponse
        """
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
        """
        @summary 意图-删除
        
        @param request: DeleteIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIntentResponse
        """
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
        """
        @summary 意图-删除
        
        @param request: DeleteIntentRequest
        @return: DeleteIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_intent_with_options(request, runtime)

    async def delete_intent_async(
        self,
        request: chatbot_20220408_models.DeleteIntentRequest,
    ) -> chatbot_20220408_models.DeleteIntentResponse:
        """
        @summary 意图-删除
        
        @param request: DeleteIntentRequest
        @return: DeleteIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_intent_with_options_async(request, runtime)

    def delete_lgf_with_options(
        self,
        request: chatbot_20220408_models.DeleteLgfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteLgfResponse:
        """
        @summary 意图-LGF-删除
        
        @param request: DeleteLgfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLgfResponse
        """
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
        """
        @summary 意图-LGF-删除
        
        @param request: DeleteLgfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLgfResponse
        """
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
        """
        @summary 意图-LGF-删除
        
        @param request: DeleteLgfRequest
        @return: DeleteLgfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_lgf_with_options(request, runtime)

    async def delete_lgf_async(
        self,
        request: chatbot_20220408_models.DeleteLgfRequest,
    ) -> chatbot_20220408_models.DeleteLgfResponse:
        """
        @summary 意图-LGF-删除
        
        @param request: DeleteLgfRequest
        @return: DeleteLgfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_lgf_with_options_async(request, runtime)

    def delete_perspective_with_options(
        self,
        request: chatbot_20220408_models.DeletePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeletePerspectiveResponse:
        """
        @summary 视角-删除
        
        @param request: DeletePerspectiveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePerspectiveResponse
        """
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
        """
        @summary 视角-删除
        
        @param request: DeletePerspectiveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePerspectiveResponse
        """
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
        """
        @summary 视角-删除
        
        @param request: DeletePerspectiveRequest
        @return: DeletePerspectiveResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_perspective_with_options(request, runtime)

    async def delete_perspective_async(
        self,
        request: chatbot_20220408_models.DeletePerspectiveRequest,
    ) -> chatbot_20220408_models.DeletePerspectiveResponse:
        """
        @summary 视角-删除
        
        @param request: DeletePerspectiveRequest
        @return: DeletePerspectiveResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_perspective_with_options_async(request, runtime)

    def delete_sim_question_with_options(
        self,
        request: chatbot_20220408_models.DeleteSimQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteSimQuestionResponse:
        """
        @summary 删除FAQ相似问
        
        @param request: DeleteSimQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSimQuestionResponse
        """
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
        """
        @summary 删除FAQ相似问
        
        @param request: DeleteSimQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSimQuestionResponse
        """
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
        """
        @summary 删除FAQ相似问
        
        @param request: DeleteSimQuestionRequest
        @return: DeleteSimQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_sim_question_with_options(request, runtime)

    async def delete_sim_question_async(
        self,
        request: chatbot_20220408_models.DeleteSimQuestionRequest,
    ) -> chatbot_20220408_models.DeleteSimQuestionResponse:
        """
        @summary 删除FAQ相似问
        
        @param request: DeleteSimQuestionRequest
        @return: DeleteSimQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_sim_question_with_options_async(request, runtime)

    def delete_solution_with_options(
        self,
        request: chatbot_20220408_models.DeleteSolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteSolutionResponse:
        """
        @summary 删除FAQ答案
        
        @param request: DeleteSolutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSolutionResponse
        """
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
        """
        @summary 删除FAQ答案
        
        @param request: DeleteSolutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSolutionResponse
        """
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
        """
        @summary 删除FAQ答案
        
        @param request: DeleteSolutionRequest
        @return: DeleteSolutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_solution_with_options(request, runtime)

    async def delete_solution_async(
        self,
        request: chatbot_20220408_models.DeleteSolutionRequest,
    ) -> chatbot_20220408_models.DeleteSolutionResponse:
        """
        @summary 删除FAQ答案
        
        @param request: DeleteSolutionRequest
        @return: DeleteSolutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_solution_with_options_async(request, runtime)

    def delete_tag_with_options(
        self,
        request: chatbot_20220408_models.DeleteTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteTagResponse:
        """
        @summary 标签删除
        
        @param request: DeleteTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTag',
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
            chatbot_20220408_models.DeleteTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tag_with_options_async(
        self,
        request: chatbot_20220408_models.DeleteTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteTagResponse:
        """
        @summary 标签删除
        
        @param request: DeleteTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTag',
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
            chatbot_20220408_models.DeleteTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tag(
        self,
        request: chatbot_20220408_models.DeleteTagRequest,
    ) -> chatbot_20220408_models.DeleteTagResponse:
        """
        @summary 标签删除
        
        @param request: DeleteTagRequest
        @return: DeleteTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_with_options(request, runtime)

    async def delete_tag_async(
        self,
        request: chatbot_20220408_models.DeleteTagRequest,
    ) -> chatbot_20220408_models.DeleteTagResponse:
        """
        @summary 标签删除
        
        @param request: DeleteTagRequest
        @return: DeleteTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_tag_with_options_async(request, runtime)

    def delete_tag_group_with_options(
        self,
        request: chatbot_20220408_models.DeleteTagGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteTagGroupResponse:
        """
        @summary 标签组删除
        
        @param request: DeleteTagGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTagGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTagGroup',
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
            chatbot_20220408_models.DeleteTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tag_group_with_options_async(
        self,
        request: chatbot_20220408_models.DeleteTagGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteTagGroupResponse:
        """
        @summary 标签组删除
        
        @param request: DeleteTagGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTagGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTagGroup',
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
            chatbot_20220408_models.DeleteTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tag_group(
        self,
        request: chatbot_20220408_models.DeleteTagGroupRequest,
    ) -> chatbot_20220408_models.DeleteTagGroupResponse:
        """
        @summary 标签组删除
        
        @param request: DeleteTagGroupRequest
        @return: DeleteTagGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_group_with_options(request, runtime)

    async def delete_tag_group_async(
        self,
        request: chatbot_20220408_models.DeleteTagGroupRequest,
    ) -> chatbot_20220408_models.DeleteTagGroupResponse:
        """
        @summary 标签组删除
        
        @param request: DeleteTagGroupRequest
        @return: DeleteTagGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_tag_group_with_options_async(request, runtime)

    def delete_user_say_with_options(
        self,
        request: chatbot_20220408_models.DeleteUserSayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DeleteUserSayResponse:
        """
        @summary 意图-用户话术-删除
        
        @param request: DeleteUserSayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserSayResponse
        """
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
        """
        @summary 意图-用户话术-删除
        
        @param request: DeleteUserSayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserSayResponse
        """
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
        """
        @summary 意图-用户话术-删除
        
        @param request: DeleteUserSayRequest
        @return: DeleteUserSayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_say_with_options(request, runtime)

    async def delete_user_say_async(
        self,
        request: chatbot_20220408_models.DeleteUserSayRequest,
    ) -> chatbot_20220408_models.DeleteUserSayResponse:
        """
        @summary 意图-用户话术-删除
        
        @param request: DeleteUserSayRequest
        @return: DeleteUserSayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_say_with_options_async(request, runtime)

    def describe_category_with_options(
        self,
        request: chatbot_20220408_models.DescribeCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeCategoryResponse:
        """
        @summary 查看单个类目信息
        
        @param request: DescribeCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCategoryResponse
        """
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
        """
        @summary 查看单个类目信息
        
        @param request: DescribeCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCategoryResponse
        """
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
        """
        @summary 查看单个类目信息
        
        @param request: DescribeCategoryRequest
        @return: DescribeCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_category_with_options(request, runtime)

    async def describe_category_async(
        self,
        request: chatbot_20220408_models.DescribeCategoryRequest,
    ) -> chatbot_20220408_models.DescribeCategoryResponse:
        """
        @summary 查看单个类目信息
        
        @param request: DescribeCategoryRequest
        @return: DescribeCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_category_with_options_async(request, runtime)

    def describe_dsentity_with_options(
        self,
        request: chatbot_20220408_models.DescribeDSEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeDSEntityResponse:
        """
        @summary 实体-详情
        
        @param request: DescribeDSEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDSEntityResponse
        """
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
        """
        @summary 实体-详情
        
        @param request: DescribeDSEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDSEntityResponse
        """
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
        """
        @summary 实体-详情
        
        @param request: DescribeDSEntityRequest
        @return: DescribeDSEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dsentity_with_options(request, runtime)

    async def describe_dsentity_async(
        self,
        request: chatbot_20220408_models.DescribeDSEntityRequest,
    ) -> chatbot_20220408_models.DescribeDSEntityResponse:
        """
        @summary 实体-详情
        
        @param request: DescribeDSEntityRequest
        @return: DescribeDSEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dsentity_with_options_async(request, runtime)

    def describe_doc_with_options(
        self,
        request: chatbot_20220408_models.DescribeDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeDocResponse:
        """
        @summary 文档详情
        
        @param request: DescribeDocRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDocResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        if not UtilClient.is_unset(request.show_detail):
            query['ShowDetail'] = request.show_detail
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDoc',
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
            chatbot_20220408_models.DescribeDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_doc_with_options_async(
        self,
        request: chatbot_20220408_models.DescribeDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeDocResponse:
        """
        @summary 文档详情
        
        @param request: DescribeDocRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDocResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        if not UtilClient.is_unset(request.show_detail):
            query['ShowDetail'] = request.show_detail
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDoc',
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
            chatbot_20220408_models.DescribeDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_doc(
        self,
        request: chatbot_20220408_models.DescribeDocRequest,
    ) -> chatbot_20220408_models.DescribeDocResponse:
        """
        @summary 文档详情
        
        @param request: DescribeDocRequest
        @return: DescribeDocResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_doc_with_options(request, runtime)

    async def describe_doc_async(
        self,
        request: chatbot_20220408_models.DescribeDocRequest,
    ) -> chatbot_20220408_models.DescribeDocResponse:
        """
        @summary 文档详情
        
        @param request: DescribeDocRequest
        @return: DescribeDocResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_doc_with_options_async(request, runtime)

    def describe_faq_with_options(
        self,
        request: chatbot_20220408_models.DescribeFaqRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeFaqResponse:
        """
        @summary 知识详情
        
        @param request: DescribeFaqRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFaqResponse
        """
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
        """
        @summary 知识详情
        
        @param request: DescribeFaqRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFaqResponse
        """
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
        """
        @summary 知识详情
        
        @param request: DescribeFaqRequest
        @return: DescribeFaqResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_faq_with_options(request, runtime)

    async def describe_faq_async(
        self,
        request: chatbot_20220408_models.DescribeFaqRequest,
    ) -> chatbot_20220408_models.DescribeFaqResponse:
        """
        @summary 知识详情
        
        @param request: DescribeFaqRequest
        @return: DescribeFaqResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_faq_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: chatbot_20220408_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeInstanceResponse:
        """
        @summary 机器人-详情
        
        @param request: DescribeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceResponse
        """
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
        """
        @summary 机器人-详情
        
        @param request: DescribeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceResponse
        """
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
        """
        @summary 机器人-详情
        
        @param request: DescribeInstanceRequest
        @return: DescribeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: chatbot_20220408_models.DescribeInstanceRequest,
    ) -> chatbot_20220408_models.DescribeInstanceResponse:
        """
        @summary 机器人-详情
        
        @param request: DescribeInstanceRequest
        @return: DescribeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_intent_with_options(
        self,
        request: chatbot_20220408_models.DescribeIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeIntentResponse:
        """
        @summary 意图-详情
        
        @param request: DescribeIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIntentResponse
        """
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
        """
        @summary 意图-详情
        
        @param request: DescribeIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIntentResponse
        """
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
        """
        @summary 意图-详情
        
        @param request: DescribeIntentRequest
        @return: DescribeIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_intent_with_options(request, runtime)

    async def describe_intent_async(
        self,
        request: chatbot_20220408_models.DescribeIntentRequest,
    ) -> chatbot_20220408_models.DescribeIntentResponse:
        """
        @summary 意图-详情
        
        @param request: DescribeIntentRequest
        @return: DescribeIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_intent_with_options_async(request, runtime)

    def describe_perspective_with_options(
        self,
        request: chatbot_20220408_models.DescribePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribePerspectiveResponse:
        """
        @summary 视角-详情
        
        @param request: DescribePerspectiveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePerspectiveResponse
        """
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
        """
        @summary 视角-详情
        
        @param request: DescribePerspectiveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePerspectiveResponse
        """
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
        """
        @summary 视角-详情
        
        @param request: DescribePerspectiveRequest
        @return: DescribePerspectiveResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_perspective_with_options(request, runtime)

    async def describe_perspective_async(
        self,
        request: chatbot_20220408_models.DescribePerspectiveRequest,
    ) -> chatbot_20220408_models.DescribePerspectiveResponse:
        """
        @summary 视角-详情
        
        @param request: DescribePerspectiveRequest
        @return: DescribePerspectiveResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_perspective_with_options_async(request, runtime)

    def describe_tag_with_options(
        self,
        request: chatbot_20220408_models.DescribeTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeTagResponse:
        """
        @summary 标签详情
        
        @param request: DescribeTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTag',
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
            chatbot_20220408_models.DescribeTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_with_options_async(
        self,
        request: chatbot_20220408_models.DescribeTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeTagResponse:
        """
        @summary 标签详情
        
        @param request: DescribeTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTag',
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
            chatbot_20220408_models.DescribeTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tag(
        self,
        request: chatbot_20220408_models.DescribeTagRequest,
    ) -> chatbot_20220408_models.DescribeTagResponse:
        """
        @summary 标签详情
        
        @param request: DescribeTagRequest
        @return: DescribeTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_with_options(request, runtime)

    async def describe_tag_async(
        self,
        request: chatbot_20220408_models.DescribeTagRequest,
    ) -> chatbot_20220408_models.DescribeTagResponse:
        """
        @summary 标签详情
        
        @param request: DescribeTagRequest
        @return: DescribeTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tag_with_options_async(request, runtime)

    def describe_tag_group_with_options(
        self,
        request: chatbot_20220408_models.DescribeTagGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeTagGroupResponse:
        """
        @summary 标签组详情
        
        @param request: DescribeTagGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTagGroup',
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
            chatbot_20220408_models.DescribeTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_group_with_options_async(
        self,
        request: chatbot_20220408_models.DescribeTagGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.DescribeTagGroupResponse:
        """
        @summary 标签组详情
        
        @param request: DescribeTagGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTagGroup',
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
            chatbot_20220408_models.DescribeTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tag_group(
        self,
        request: chatbot_20220408_models.DescribeTagGroupRequest,
    ) -> chatbot_20220408_models.DescribeTagGroupResponse:
        """
        @summary 标签组详情
        
        @param request: DescribeTagGroupRequest
        @return: DescribeTagGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_group_with_options(request, runtime)

    async def describe_tag_group_async(
        self,
        request: chatbot_20220408_models.DescribeTagGroupRequest,
    ) -> chatbot_20220408_models.DescribeTagGroupResponse:
        """
        @summary 标签组详情
        
        @param request: DescribeTagGroupRequest
        @return: DescribeTagGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tag_group_with_options_async(request, runtime)

    def feedback_with_options(
        self,
        request: chatbot_20220408_models.FeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.FeedbackResponse:
        """
        @summary 问答点赞、点踩API
        
        @param request: FeedbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FeedbackResponse
        """
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
        """
        @summary 问答点赞、点踩API
        
        @param request: FeedbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FeedbackResponse
        """
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
        """
        @summary 问答点赞、点踩API
        
        @param request: FeedbackRequest
        @return: FeedbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.feedback_with_options(request, runtime)

    async def feedback_async(
        self,
        request: chatbot_20220408_models.FeedbackRequest,
    ) -> chatbot_20220408_models.FeedbackResponse:
        """
        @summary 问答点赞、点踩API
        
        @param request: FeedbackRequest
        @return: FeedbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.feedback_with_options_async(request, runtime)

    def generate_user_access_token_with_options(
        self,
        request: chatbot_20220408_models.GenerateUserAccessTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.GenerateUserAccessTokenResponse:
        """
        @summary 生成用户免登Token
        
        @param request: GenerateUserAccessTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateUserAccessTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.extra_info):
            query['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.foreign_id):
            query['ForeignId'] = request.foreign_id
        if not UtilClient.is_unset(request.nick):
            query['Nick'] = request.nick
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateUserAccessToken',
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
            chatbot_20220408_models.GenerateUserAccessTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_user_access_token_with_options_async(
        self,
        request: chatbot_20220408_models.GenerateUserAccessTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.GenerateUserAccessTokenResponse:
        """
        @summary 生成用户免登Token
        
        @param request: GenerateUserAccessTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateUserAccessTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.extra_info):
            query['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.foreign_id):
            query['ForeignId'] = request.foreign_id
        if not UtilClient.is_unset(request.nick):
            query['Nick'] = request.nick
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateUserAccessToken',
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
            chatbot_20220408_models.GenerateUserAccessTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_user_access_token(
        self,
        request: chatbot_20220408_models.GenerateUserAccessTokenRequest,
    ) -> chatbot_20220408_models.GenerateUserAccessTokenResponse:
        """
        @summary 生成用户免登Token
        
        @param request: GenerateUserAccessTokenRequest
        @return: GenerateUserAccessTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_user_access_token_with_options(request, runtime)

    async def generate_user_access_token_async(
        self,
        request: chatbot_20220408_models.GenerateUserAccessTokenRequest,
    ) -> chatbot_20220408_models.GenerateUserAccessTokenResponse:
        """
        @summary 生成用户免登Token
        
        @param request: GenerateUserAccessTokenRequest
        @return: GenerateUserAccessTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_user_access_token_with_options_async(request, runtime)

    def get_agent_info_with_options(
        self,
        request: chatbot_20220408_models.GetAgentInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.GetAgentInfoResponse:
        """
        @summary 获取业务空间信息
        
        @param request: GetAgentInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentInfo',
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
            chatbot_20220408_models.GetAgentInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_info_with_options_async(
        self,
        request: chatbot_20220408_models.GetAgentInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.GetAgentInfoResponse:
        """
        @summary 获取业务空间信息
        
        @param request: GetAgentInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentInfo',
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
            chatbot_20220408_models.GetAgentInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_info(
        self,
        request: chatbot_20220408_models.GetAgentInfoRequest,
    ) -> chatbot_20220408_models.GetAgentInfoResponse:
        """
        @summary 获取业务空间信息
        
        @param request: GetAgentInfoRequest
        @return: GetAgentInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_agent_info_with_options(request, runtime)

    async def get_agent_info_async(
        self,
        request: chatbot_20220408_models.GetAgentInfoRequest,
    ) -> chatbot_20220408_models.GetAgentInfoResponse:
        """
        @summary 获取业务空间信息
        
        @param request: GetAgentInfoRequest
        @return: GetAgentInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_info_with_options_async(request, runtime)

    def get_async_result_with_options(
        self,
        request: chatbot_20220408_models.GetAsyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.GetAsyncResultResponse:
        """
        @summary 获取异步函数执行结果接口
        
        @param request: GetAsyncResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsyncResultResponse
        """
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
        """
        @summary 获取异步函数执行结果接口
        
        @param request: GetAsyncResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsyncResultResponse
        """
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
        """
        @summary 获取异步函数执行结果接口
        
        @param request: GetAsyncResultRequest
        @return: GetAsyncResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_async_result_with_options(request, runtime)

    async def get_async_result_async(
        self,
        request: chatbot_20220408_models.GetAsyncResultRequest,
    ) -> chatbot_20220408_models.GetAsyncResultResponse:
        """
        @summary 获取异步函数执行结果接口
        
        @param request: GetAsyncResultRequest
        @return: GetAsyncResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_async_result_with_options_async(request, runtime)

    def get_bot_session_data_with_options(
        self,
        request: chatbot_20220408_models.GetBotSessionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.GetBotSessionDataResponse:
        """
        @summary 查询机器人接待人次和对话轮次
        
        @param request: GetBotSessionDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBotSessionDataResponse
        """
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
            chatbot_20220408_models.GetBotSessionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bot_session_data_with_options_async(
        self,
        request: chatbot_20220408_models.GetBotSessionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.GetBotSessionDataResponse:
        """
        @summary 查询机器人接待人次和对话轮次
        
        @param request: GetBotSessionDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBotSessionDataResponse
        """
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
            chatbot_20220408_models.GetBotSessionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bot_session_data(
        self,
        request: chatbot_20220408_models.GetBotSessionDataRequest,
    ) -> chatbot_20220408_models.GetBotSessionDataResponse:
        """
        @summary 查询机器人接待人次和对话轮次
        
        @param request: GetBotSessionDataRequest
        @return: GetBotSessionDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_bot_session_data_with_options(request, runtime)

    async def get_bot_session_data_async(
        self,
        request: chatbot_20220408_models.GetBotSessionDataRequest,
    ) -> chatbot_20220408_models.GetBotSessionDataResponse:
        """
        @summary 查询机器人接待人次和对话轮次
        
        @param request: GetBotSessionDataRequest
        @return: GetBotSessionDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_bot_session_data_with_options_async(request, runtime)

    def get_instance_publish_task_state_with_options(
        self,
        request: chatbot_20220408_models.GetInstancePublishTaskStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.GetInstancePublishTaskStateResponse:
        """
        @summary 查询机器人发布进度
        
        @param request: GetInstancePublishTaskStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstancePublishTaskStateResponse
        """
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
        """
        @summary 查询机器人发布进度
        
        @param request: GetInstancePublishTaskStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstancePublishTaskStateResponse
        """
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
        """
        @summary 查询机器人发布进度
        
        @param request: GetInstancePublishTaskStateRequest
        @return: GetInstancePublishTaskStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_publish_task_state_with_options(request, runtime)

    async def get_instance_publish_task_state_async(
        self,
        request: chatbot_20220408_models.GetInstancePublishTaskStateRequest,
    ) -> chatbot_20220408_models.GetInstancePublishTaskStateResponse:
        """
        @summary 查询机器人发布进度
        
        @param request: GetInstancePublishTaskStateRequest
        @return: GetInstancePublishTaskStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_publish_task_state_with_options_async(request, runtime)

    def get_publish_task_state_with_options(
        self,
        request: chatbot_20220408_models.GetPublishTaskStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.GetPublishTaskStateResponse:
        """
        @summary 查询发布进度
        
        @param request: GetPublishTaskStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPublishTaskStateResponse
        """
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
        """
        @summary 查询发布进度
        
        @param request: GetPublishTaskStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPublishTaskStateResponse
        """
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
        """
        @summary 查询发布进度
        
        @param request: GetPublishTaskStateRequest
        @return: GetPublishTaskStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_publish_task_state_with_options(request, runtime)

    async def get_publish_task_state_async(
        self,
        request: chatbot_20220408_models.GetPublishTaskStateRequest,
    ) -> chatbot_20220408_models.GetPublishTaskStateResponse:
        """
        @summary 查询发布进度
        
        @param request: GetPublishTaskStateRequest
        @return: GetPublishTaskStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_publish_task_state_with_options_async(request, runtime)

    def init_imconnect_with_options(
        self,
        request: chatbot_20220408_models.InitIMConnectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.InitIMConnectResponse:
        """
        @summary 初始化im连接信息
        
        @param request: InitIMConnectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitIMConnectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.user_access_token):
            query['UserAccessToken'] = request.user_access_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitIMConnect',
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
            chatbot_20220408_models.InitIMConnectResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_imconnect_with_options_async(
        self,
        request: chatbot_20220408_models.InitIMConnectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.InitIMConnectResponse:
        """
        @summary 初始化im连接信息
        
        @param request: InitIMConnectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitIMConnectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.user_access_token):
            query['UserAccessToken'] = request.user_access_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitIMConnect',
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
            chatbot_20220408_models.InitIMConnectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_imconnect(
        self,
        request: chatbot_20220408_models.InitIMConnectRequest,
    ) -> chatbot_20220408_models.InitIMConnectResponse:
        """
        @summary 初始化im连接信息
        
        @param request: InitIMConnectRequest
        @return: InitIMConnectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.init_imconnect_with_options(request, runtime)

    async def init_imconnect_async(
        self,
        request: chatbot_20220408_models.InitIMConnectRequest,
    ) -> chatbot_20220408_models.InitIMConnectResponse:
        """
        @summary 初始化im连接信息
        
        @param request: InitIMConnectRequest
        @return: InitIMConnectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.init_imconnect_with_options_async(request, runtime)

    def link_instance_category_with_options(
        self,
        request: chatbot_20220408_models.LinkInstanceCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.LinkInstanceCategoryResponse:
        """
        @summary 机器人-绑定类目
        
        @param request: LinkInstanceCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LinkInstanceCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ability_type):
            query['AbilityType'] = request.ability_type
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
        """
        @summary 机器人-绑定类目
        
        @param request: LinkInstanceCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LinkInstanceCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ability_type):
            query['AbilityType'] = request.ability_type
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
        """
        @summary 机器人-绑定类目
        
        @param request: LinkInstanceCategoryRequest
        @return: LinkInstanceCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.link_instance_category_with_options(request, runtime)

    async def link_instance_category_async(
        self,
        request: chatbot_20220408_models.LinkInstanceCategoryRequest,
    ) -> chatbot_20220408_models.LinkInstanceCategoryResponse:
        """
        @summary 机器人-绑定类目
        
        @param request: LinkInstanceCategoryRequest
        @return: LinkInstanceCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.link_instance_category_with_options_async(request, runtime)

    def list_agent_with_options(
        self,
        request: chatbot_20220408_models.ListAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListAgentResponse:
        """
        @summary 获取业务空间列表
        
        @param request: ListAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_name):
            query['AgentName'] = request.agent_name
        if not UtilClient.is_unset(request.goods_codes):
            query['GoodsCodes'] = request.goods_codes
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
        """
        @summary 获取业务空间列表
        
        @param request: ListAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_name):
            query['AgentName'] = request.agent_name
        if not UtilClient.is_unset(request.goods_codes):
            query['GoodsCodes'] = request.goods_codes
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
        """
        @summary 获取业务空间列表
        
        @param request: ListAgentRequest
        @return: ListAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_agent_with_options(request, runtime)

    async def list_agent_async(
        self,
        request: chatbot_20220408_models.ListAgentRequest,
    ) -> chatbot_20220408_models.ListAgentResponse:
        """
        @summary 获取业务空间列表
        
        @param request: ListAgentRequest
        @return: ListAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_agent_with_options_async(request, runtime)

    def list_category_with_options(
        self,
        request: chatbot_20220408_models.ListCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListCategoryResponse:
        """
        @summary 类目列表
        
        @param request: ListCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.knowledge_type):
            body['KnowledgeType'] = request.knowledge_type
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
        """
        @summary 类目列表
        
        @param request: ListCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.knowledge_type):
            body['KnowledgeType'] = request.knowledge_type
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
        """
        @summary 类目列表
        
        @param request: ListCategoryRequest
        @return: ListCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_category_with_options(request, runtime)

    async def list_category_async(
        self,
        request: chatbot_20220408_models.ListCategoryRequest,
    ) -> chatbot_20220408_models.ListCategoryResponse:
        """
        @summary 类目列表
        
        @param request: ListCategoryRequest
        @return: ListCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_category_with_options_async(request, runtime)

    def list_conn_question_with_options(
        self,
        request: chatbot_20220408_models.ListConnQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListConnQuestionResponse:
        """
        @summary 查询FAQ关联问列表
        
        @param request: ListConnQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConnQuestionResponse
        """
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
        """
        @summary 查询FAQ关联问列表
        
        @param request: ListConnQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConnQuestionResponse
        """
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
        """
        @summary 查询FAQ关联问列表
        
        @param request: ListConnQuestionRequest
        @return: ListConnQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_conn_question_with_options(request, runtime)

    async def list_conn_question_async(
        self,
        request: chatbot_20220408_models.ListConnQuestionRequest,
    ) -> chatbot_20220408_models.ListConnQuestionResponse:
        """
        @summary 查询FAQ关联问列表
        
        @param request: ListConnQuestionRequest
        @return: ListConnQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_conn_question_with_options_async(request, runtime)

    def list_dsentity_with_options(
        self,
        request: chatbot_20220408_models.ListDSEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListDSEntityResponse:
        """
        @summary 实体-列表
        
        @param request: ListDSEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDSEntityResponse
        """
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
        """
        @summary 实体-列表
        
        @param request: ListDSEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDSEntityResponse
        """
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
        """
        @summary 实体-列表
        
        @param request: ListDSEntityRequest
        @return: ListDSEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dsentity_with_options(request, runtime)

    async def list_dsentity_async(
        self,
        request: chatbot_20220408_models.ListDSEntityRequest,
    ) -> chatbot_20220408_models.ListDSEntityResponse:
        """
        @summary 实体-列表
        
        @param request: ListDSEntityRequest
        @return: ListDSEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_dsentity_with_options_async(request, runtime)

    def list_dsentity_value_with_options(
        self,
        request: chatbot_20220408_models.ListDSEntityValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListDSEntityValueResponse:
        """
        @summary 实体成员-列表
        
        @param request: ListDSEntityValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDSEntityValueResponse
        """
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
        """
        @summary 实体成员-列表
        
        @param request: ListDSEntityValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDSEntityValueResponse
        """
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
        """
        @summary 实体成员-列表
        
        @param request: ListDSEntityValueRequest
        @return: ListDSEntityValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dsentity_value_with_options(request, runtime)

    async def list_dsentity_value_async(
        self,
        request: chatbot_20220408_models.ListDSEntityValueRequest,
    ) -> chatbot_20220408_models.ListDSEntityValueResponse:
        """
        @summary 实体成员-列表
        
        @param request: ListDSEntityValueRequest
        @return: ListDSEntityValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_dsentity_value_with_options_async(request, runtime)

    def list_instance_with_options(
        self,
        request: chatbot_20220408_models.ListInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListInstanceResponse:
        """
        @summary 机器人-修改
        
        @param request: ListInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceResponse
        """
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
        """
        @summary 机器人-修改
        
        @param request: ListInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceResponse
        """
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
        """
        @summary 机器人-修改
        
        @param request: ListInstanceRequest
        @return: ListInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instance_with_options(request, runtime)

    async def list_instance_async(
        self,
        request: chatbot_20220408_models.ListInstanceRequest,
    ) -> chatbot_20220408_models.ListInstanceResponse:
        """
        @summary 机器人-修改
        
        @param request: ListInstanceRequest
        @return: ListInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_with_options_async(request, runtime)

    def list_intent_with_options(
        self,
        request: chatbot_20220408_models.ListIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListIntentResponse:
        """
        @summary 意图-列表
        
        @param request: ListIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntentResponse
        """
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
        """
        @summary 意图-列表
        
        @param request: ListIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIntentResponse
        """
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
        """
        @summary 意图-列表
        
        @param request: ListIntentRequest
        @return: ListIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_intent_with_options(request, runtime)

    async def list_intent_async(
        self,
        request: chatbot_20220408_models.ListIntentRequest,
    ) -> chatbot_20220408_models.ListIntentResponse:
        """
        @summary 意图-列表
        
        @param request: ListIntentRequest
        @return: ListIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_intent_with_options_async(request, runtime)

    def list_lgf_with_options(
        self,
        request: chatbot_20220408_models.ListLgfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListLgfResponse:
        """
        @summary 意图-LGF-列表
        
        @param request: ListLgfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLgfResponse
        """
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
        """
        @summary 意图-LGF-列表
        
        @param request: ListLgfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLgfResponse
        """
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
        """
        @summary 意图-LGF-列表
        
        @param request: ListLgfRequest
        @return: ListLgfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_lgf_with_options(request, runtime)

    async def list_lgf_async(
        self,
        request: chatbot_20220408_models.ListLgfRequest,
    ) -> chatbot_20220408_models.ListLgfResponse:
        """
        @summary 意图-LGF-列表
        
        @param request: ListLgfRequest
        @return: ListLgfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_lgf_with_options_async(request, runtime)

    def list_saas_info_with_options(
        self,
        request: chatbot_20220408_models.ListSaasInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListSaasInfoResponse:
        """
        @summary 获取业务空间下可集成的SaaS信息列表
        
        @param request: ListSaasInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSaasInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.saas_group_codes):
            query['SaasGroupCodes'] = request.saas_group_codes
        if not UtilClient.is_unset(request.saas_name):
            query['SaasName'] = request.saas_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSaasInfo',
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
            chatbot_20220408_models.ListSaasInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_saas_info_with_options_async(
        self,
        request: chatbot_20220408_models.ListSaasInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListSaasInfoResponse:
        """
        @summary 获取业务空间下可集成的SaaS信息列表
        
        @param request: ListSaasInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSaasInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.saas_group_codes):
            query['SaasGroupCodes'] = request.saas_group_codes
        if not UtilClient.is_unset(request.saas_name):
            query['SaasName'] = request.saas_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSaasInfo',
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
            chatbot_20220408_models.ListSaasInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_saas_info(
        self,
        request: chatbot_20220408_models.ListSaasInfoRequest,
    ) -> chatbot_20220408_models.ListSaasInfoResponse:
        """
        @summary 获取业务空间下可集成的SaaS信息列表
        
        @param request: ListSaasInfoRequest
        @return: ListSaasInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_saas_info_with_options(request, runtime)

    async def list_saas_info_async(
        self,
        request: chatbot_20220408_models.ListSaasInfoRequest,
    ) -> chatbot_20220408_models.ListSaasInfoResponse:
        """
        @summary 获取业务空间下可集成的SaaS信息列表
        
        @param request: ListSaasInfoRequest
        @return: ListSaasInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_saas_info_with_options_async(request, runtime)

    def list_saas_permission_group_infos_with_options(
        self,
        request: chatbot_20220408_models.ListSaasPermissionGroupInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListSaasPermissionGroupInfosResponse:
        """
        @summary 获取业务空间下可集成的权限组信息
        
        @param request: ListSaasPermissionGroupInfosRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSaasPermissionGroupInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSaasPermissionGroupInfos',
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
            chatbot_20220408_models.ListSaasPermissionGroupInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_saas_permission_group_infos_with_options_async(
        self,
        request: chatbot_20220408_models.ListSaasPermissionGroupInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListSaasPermissionGroupInfosResponse:
        """
        @summary 获取业务空间下可集成的权限组信息
        
        @param request: ListSaasPermissionGroupInfosRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSaasPermissionGroupInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSaasPermissionGroupInfos',
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
            chatbot_20220408_models.ListSaasPermissionGroupInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_saas_permission_group_infos(
        self,
        request: chatbot_20220408_models.ListSaasPermissionGroupInfosRequest,
    ) -> chatbot_20220408_models.ListSaasPermissionGroupInfosResponse:
        """
        @summary 获取业务空间下可集成的权限组信息
        
        @param request: ListSaasPermissionGroupInfosRequest
        @return: ListSaasPermissionGroupInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_saas_permission_group_infos_with_options(request, runtime)

    async def list_saas_permission_group_infos_async(
        self,
        request: chatbot_20220408_models.ListSaasPermissionGroupInfosRequest,
    ) -> chatbot_20220408_models.ListSaasPermissionGroupInfosResponse:
        """
        @summary 获取业务空间下可集成的权限组信息
        
        @param request: ListSaasPermissionGroupInfosRequest
        @return: ListSaasPermissionGroupInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_saas_permission_group_infos_with_options_async(request, runtime)

    def list_sim_question_with_options(
        self,
        request: chatbot_20220408_models.ListSimQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListSimQuestionResponse:
        """
        @summary FAQ相似问列表
        
        @param request: ListSimQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSimQuestionResponse
        """
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
        """
        @summary FAQ相似问列表
        
        @param request: ListSimQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSimQuestionResponse
        """
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
        """
        @summary FAQ相似问列表
        
        @param request: ListSimQuestionRequest
        @return: ListSimQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_sim_question_with_options(request, runtime)

    async def list_sim_question_async(
        self,
        request: chatbot_20220408_models.ListSimQuestionRequest,
    ) -> chatbot_20220408_models.ListSimQuestionResponse:
        """
        @summary FAQ相似问列表
        
        @param request: ListSimQuestionRequest
        @return: ListSimQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_sim_question_with_options_async(request, runtime)

    def list_solution_with_options(
        self,
        request: chatbot_20220408_models.ListSolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListSolutionResponse:
        """
        @summary FAQ答案列表
        
        @param request: ListSolutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSolutionResponse
        """
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
        """
        @summary FAQ答案列表
        
        @param request: ListSolutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSolutionResponse
        """
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
        """
        @summary FAQ答案列表
        
        @param request: ListSolutionRequest
        @return: ListSolutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_solution_with_options(request, runtime)

    async def list_solution_async(
        self,
        request: chatbot_20220408_models.ListSolutionRequest,
    ) -> chatbot_20220408_models.ListSolutionResponse:
        """
        @summary FAQ答案列表
        
        @param request: ListSolutionRequest
        @return: ListSolutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_solution_with_options_async(request, runtime)

    def list_tag_with_options(
        self,
        request: chatbot_20220408_models.ListTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListTagResponse:
        """
        @summary 标签查询
        
        @param request: ListTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag_name):
            body['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTag',
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
            chatbot_20220408_models.ListTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_with_options_async(
        self,
        request: chatbot_20220408_models.ListTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListTagResponse:
        """
        @summary 标签查询
        
        @param request: ListTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag_name):
            body['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTag',
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
            chatbot_20220408_models.ListTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag(
        self,
        request: chatbot_20220408_models.ListTagRequest,
    ) -> chatbot_20220408_models.ListTagResponse:
        """
        @summary 标签查询
        
        @param request: ListTagRequest
        @return: ListTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_with_options(request, runtime)

    async def list_tag_async(
        self,
        request: chatbot_20220408_models.ListTagRequest,
    ) -> chatbot_20220408_models.ListTagResponse:
        """
        @summary 标签查询
        
        @param request: ListTagRequest
        @return: ListTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_with_options_async(request, runtime)

    def list_tag_group_with_options(
        self,
        request: chatbot_20220408_models.ListTagGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListTagGroupResponse:
        """
        @summary 标签组查询
        
        @param request: ListTagGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTagGroup',
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
            chatbot_20220408_models.ListTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_group_with_options_async(
        self,
        request: chatbot_20220408_models.ListTagGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListTagGroupResponse:
        """
        @summary 标签组查询
        
        @param request: ListTagGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTagGroup',
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
            chatbot_20220408_models.ListTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_group(
        self,
        request: chatbot_20220408_models.ListTagGroupRequest,
    ) -> chatbot_20220408_models.ListTagGroupResponse:
        """
        @summary 标签组查询
        
        @param request: ListTagGroupRequest
        @return: ListTagGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_group_with_options(request, runtime)

    async def list_tag_group_async(
        self,
        request: chatbot_20220408_models.ListTagGroupRequest,
    ) -> chatbot_20220408_models.ListTagGroupResponse:
        """
        @summary 标签组查询
        
        @param request: ListTagGroupRequest
        @return: ListTagGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_group_with_options_async(request, runtime)

    def list_tongyi_chat_historys_with_options(
        self,
        request: chatbot_20220408_models.ListTongyiChatHistorysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListTongyiChatHistorysResponse:
        """
        @summary Tongyi对话明细查询接口
        
        @param request: ListTongyiChatHistorysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTongyiChatHistorysResponse
        """
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
            action='ListTongyiChatHistorys',
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
            chatbot_20220408_models.ListTongyiChatHistorysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tongyi_chat_historys_with_options_async(
        self,
        request: chatbot_20220408_models.ListTongyiChatHistorysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListTongyiChatHistorysResponse:
        """
        @summary Tongyi对话明细查询接口
        
        @param request: ListTongyiChatHistorysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTongyiChatHistorysResponse
        """
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
            action='ListTongyiChatHistorys',
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
            chatbot_20220408_models.ListTongyiChatHistorysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tongyi_chat_historys(
        self,
        request: chatbot_20220408_models.ListTongyiChatHistorysRequest,
    ) -> chatbot_20220408_models.ListTongyiChatHistorysResponse:
        """
        @summary Tongyi对话明细查询接口
        
        @param request: ListTongyiChatHistorysRequest
        @return: ListTongyiChatHistorysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tongyi_chat_historys_with_options(request, runtime)

    async def list_tongyi_chat_historys_async(
        self,
        request: chatbot_20220408_models.ListTongyiChatHistorysRequest,
    ) -> chatbot_20220408_models.ListTongyiChatHistorysResponse:
        """
        @summary Tongyi对话明细查询接口
        
        @param request: ListTongyiChatHistorysRequest
        @return: ListTongyiChatHistorysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tongyi_chat_historys_with_options_async(request, runtime)

    def list_tongyi_conversation_logs_with_options(
        self,
        request: chatbot_20220408_models.ListTongyiConversationLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListTongyiConversationLogsResponse:
        """
        @summary 查询通义晓蜜的单个会话对话记录
        
        @param request: ListTongyiConversationLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTongyiConversationLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTongyiConversationLogs',
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
            chatbot_20220408_models.ListTongyiConversationLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tongyi_conversation_logs_with_options_async(
        self,
        request: chatbot_20220408_models.ListTongyiConversationLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListTongyiConversationLogsResponse:
        """
        @summary 查询通义晓蜜的单个会话对话记录
        
        @param request: ListTongyiConversationLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTongyiConversationLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTongyiConversationLogs',
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
            chatbot_20220408_models.ListTongyiConversationLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tongyi_conversation_logs(
        self,
        request: chatbot_20220408_models.ListTongyiConversationLogsRequest,
    ) -> chatbot_20220408_models.ListTongyiConversationLogsResponse:
        """
        @summary 查询通义晓蜜的单个会话对话记录
        
        @param request: ListTongyiConversationLogsRequest
        @return: ListTongyiConversationLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tongyi_conversation_logs_with_options(request, runtime)

    async def list_tongyi_conversation_logs_async(
        self,
        request: chatbot_20220408_models.ListTongyiConversationLogsRequest,
    ) -> chatbot_20220408_models.ListTongyiConversationLogsResponse:
        """
        @summary 查询通义晓蜜的单个会话对话记录
        
        @param request: ListTongyiConversationLogsRequest
        @return: ListTongyiConversationLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tongyi_conversation_logs_with_options_async(request, runtime)

    def list_user_say_with_options(
        self,
        request: chatbot_20220408_models.ListUserSayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.ListUserSayResponse:
        """
        @summary 话术-列表
        
        @param request: ListUserSayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserSayResponse
        """
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
        """
        @summary 话术-列表
        
        @param request: ListUserSayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserSayResponse
        """
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
        """
        @summary 话术-列表
        
        @param request: ListUserSayRequest
        @return: ListUserSayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_say_with_options(request, runtime)

    async def list_user_say_async(
        self,
        request: chatbot_20220408_models.ListUserSayRequest,
    ) -> chatbot_20220408_models.ListUserSayResponse:
        """
        @summary 话术-列表
        
        @param request: ListUserSayRequest
        @return: ListUserSayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_say_with_options_async(request, runtime)

    def nlu_with_options(
        self,
        request: chatbot_20220408_models.NluRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.NluResponse:
        """
        @summary 统一NLU接口
        
        @param request: NluRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: NluResponse
        """
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
        """
        @summary 统一NLU接口
        
        @param request: NluRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: NluResponse
        """
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
        """
        @summary 统一NLU接口
        
        @param request: NluRequest
        @return: NluResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.nlu_with_options(request, runtime)

    async def nlu_async(
        self,
        request: chatbot_20220408_models.NluRequest,
    ) -> chatbot_20220408_models.NluResponse:
        """
        @summary 统一NLU接口
        
        @param request: NluRequest
        @return: NluResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.nlu_with_options_async(request, runtime)

    def query_perspectives_with_options(
        self,
        request: chatbot_20220408_models.QueryPerspectivesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.QueryPerspectivesResponse:
        """
        @summary 视角-列表
        
        @param request: QueryPerspectivesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPerspectivesResponse
        """
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
        """
        @summary 视角-列表
        
        @param request: QueryPerspectivesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPerspectivesResponse
        """
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
        """
        @summary 视角-列表
        
        @param request: QueryPerspectivesRequest
        @return: QueryPerspectivesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_perspectives_with_options(request, runtime)

    async def query_perspectives_async(
        self,
        request: chatbot_20220408_models.QueryPerspectivesRequest,
    ) -> chatbot_20220408_models.QueryPerspectivesResponse:
        """
        @summary 视角-列表
        
        @param request: QueryPerspectivesRequest
        @return: QueryPerspectivesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_perspectives_with_options_async(request, runtime)

    def retry_doc_with_options(
        self,
        request: chatbot_20220408_models.RetryDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.RetryDocResponse:
        """
        @summary 文档重试
        
        @param request: RetryDocRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetryDocResponse
        """
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
            action='RetryDoc',
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
            chatbot_20220408_models.RetryDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_doc_with_options_async(
        self,
        request: chatbot_20220408_models.RetryDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.RetryDocResponse:
        """
        @summary 文档重试
        
        @param request: RetryDocRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetryDocResponse
        """
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
            action='RetryDoc',
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
            chatbot_20220408_models.RetryDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_doc(
        self,
        request: chatbot_20220408_models.RetryDocRequest,
    ) -> chatbot_20220408_models.RetryDocResponse:
        """
        @summary 文档重试
        
        @param request: RetryDocRequest
        @return: RetryDocResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.retry_doc_with_options(request, runtime)

    async def retry_doc_async(
        self,
        request: chatbot_20220408_models.RetryDocRequest,
    ) -> chatbot_20220408_models.RetryDocResponse:
        """
        @summary 文档重试
        
        @param request: RetryDocRequest
        @return: RetryDocResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.retry_doc_with_options_async(request, runtime)

    def search_doc_with_options(
        self,
        tmp_req: chatbot_20220408_models.SearchDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.SearchDocResponse:
        """
        @summary 文档搜索
        
        @param tmp_req: SearchDocRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchDocResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.SearchDocShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.category_ids):
            request.category_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_ids_shrink):
            query['CategoryIds'] = request.category_ids_shrink
        if not UtilClient.is_unset(request.create_time_begin):
            query['CreateTimeBegin'] = request.create_time_begin
        if not UtilClient.is_unset(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_user_name):
            query['CreateUserName'] = request.create_user_name
        if not UtilClient.is_unset(request.end_time_begin):
            query['EndTimeBegin'] = request.end_time_begin
        if not UtilClient.is_unset(request.end_time_end):
            query['EndTimeEnd'] = request.end_time_end
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.modify_time_begin):
            query['ModifyTimeBegin'] = request.modify_time_begin
        if not UtilClient.is_unset(request.modify_time_end):
            query['ModifyTimeEnd'] = request.modify_time_end
        if not UtilClient.is_unset(request.modify_user_name):
            query['ModifyUserName'] = request.modify_user_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.process_status):
            query['ProcessStatus'] = request.process_status
        if not UtilClient.is_unset(request.search_scope):
            query['SearchScope'] = request.search_scope
        if not UtilClient.is_unset(request.start_time_begin):
            query['StartTimeBegin'] = request.start_time_begin
        if not UtilClient.is_unset(request.start_time_end):
            query['StartTimeEnd'] = request.start_time_end
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids_shrink):
            query['TagIds'] = request.tag_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchDoc',
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
            chatbot_20220408_models.SearchDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_doc_with_options_async(
        self,
        tmp_req: chatbot_20220408_models.SearchDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.SearchDocResponse:
        """
        @summary 文档搜索
        
        @param tmp_req: SearchDocRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchDocResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.SearchDocShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.category_ids):
            request.category_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_ids_shrink):
            query['CategoryIds'] = request.category_ids_shrink
        if not UtilClient.is_unset(request.create_time_begin):
            query['CreateTimeBegin'] = request.create_time_begin
        if not UtilClient.is_unset(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_user_name):
            query['CreateUserName'] = request.create_user_name
        if not UtilClient.is_unset(request.end_time_begin):
            query['EndTimeBegin'] = request.end_time_begin
        if not UtilClient.is_unset(request.end_time_end):
            query['EndTimeEnd'] = request.end_time_end
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.modify_time_begin):
            query['ModifyTimeBegin'] = request.modify_time_begin
        if not UtilClient.is_unset(request.modify_time_end):
            query['ModifyTimeEnd'] = request.modify_time_end
        if not UtilClient.is_unset(request.modify_user_name):
            query['ModifyUserName'] = request.modify_user_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.process_status):
            query['ProcessStatus'] = request.process_status
        if not UtilClient.is_unset(request.search_scope):
            query['SearchScope'] = request.search_scope
        if not UtilClient.is_unset(request.start_time_begin):
            query['StartTimeBegin'] = request.start_time_begin
        if not UtilClient.is_unset(request.start_time_end):
            query['StartTimeEnd'] = request.start_time_end
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids_shrink):
            query['TagIds'] = request.tag_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchDoc',
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
            chatbot_20220408_models.SearchDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_doc(
        self,
        request: chatbot_20220408_models.SearchDocRequest,
    ) -> chatbot_20220408_models.SearchDocResponse:
        """
        @summary 文档搜索
        
        @param request: SearchDocRequest
        @return: SearchDocResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_doc_with_options(request, runtime)

    async def search_doc_async(
        self,
        request: chatbot_20220408_models.SearchDocRequest,
    ) -> chatbot_20220408_models.SearchDocResponse:
        """
        @summary 文档搜索
        
        @param request: SearchDocRequest
        @return: SearchDocResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_doc_with_options_async(request, runtime)

    def search_faq_with_options(
        self,
        tmp_req: chatbot_20220408_models.SearchFaqRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.SearchFaqResponse:
        """
        @summary 知识搜索
        
        @param tmp_req: SearchFaqRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchFaqResponse
        """
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
        """
        @summary 知识搜索
        
        @param tmp_req: SearchFaqRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchFaqResponse
        """
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
        """
        @summary 知识搜索
        
        @param request: SearchFaqRequest
        @return: SearchFaqResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_faq_with_options(request, runtime)

    async def search_faq_async(
        self,
        request: chatbot_20220408_models.SearchFaqRequest,
    ) -> chatbot_20220408_models.SearchFaqResponse:
        """
        @summary 知识搜索
        
        @param request: SearchFaqRequest
        @return: SearchFaqResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_faq_with_options_async(request, runtime)

    def tongyi_chat_debug_info_with_options(
        self,
        request: chatbot_20220408_models.TongyiChatDebugInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.TongyiChatDebugInfoResponse:
        """
        @summary 大模型问答调试信息
        
        @param request: TongyiChatDebugInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TongyiChatDebugInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TongyiChatDebugInfo',
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
            chatbot_20220408_models.TongyiChatDebugInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def tongyi_chat_debug_info_with_options_async(
        self,
        request: chatbot_20220408_models.TongyiChatDebugInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.TongyiChatDebugInfoResponse:
        """
        @summary 大模型问答调试信息
        
        @param request: TongyiChatDebugInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TongyiChatDebugInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TongyiChatDebugInfo',
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
            chatbot_20220408_models.TongyiChatDebugInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tongyi_chat_debug_info(
        self,
        request: chatbot_20220408_models.TongyiChatDebugInfoRequest,
    ) -> chatbot_20220408_models.TongyiChatDebugInfoResponse:
        """
        @summary 大模型问答调试信息
        
        @param request: TongyiChatDebugInfoRequest
        @return: TongyiChatDebugInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tongyi_chat_debug_info_with_options(request, runtime)

    async def tongyi_chat_debug_info_async(
        self,
        request: chatbot_20220408_models.TongyiChatDebugInfoRequest,
    ) -> chatbot_20220408_models.TongyiChatDebugInfoResponse:
        """
        @summary 大模型问答调试信息
        
        @param request: TongyiChatDebugInfoRequest
        @return: TongyiChatDebugInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tongyi_chat_debug_info_with_options_async(request, runtime)

    def update_category_with_options(
        self,
        request: chatbot_20220408_models.UpdateCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateCategoryResponse:
        """
        @summary 编辑类目
        
        @param request: UpdateCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.biz_code):
            body['BizCode'] = request.biz_code
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
        """
        @summary 编辑类目
        
        @param request: UpdateCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.biz_code):
            body['BizCode'] = request.biz_code
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
        """
        @summary 编辑类目
        
        @param request: UpdateCategoryRequest
        @return: UpdateCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_category_with_options(request, runtime)

    async def update_category_async(
        self,
        request: chatbot_20220408_models.UpdateCategoryRequest,
    ) -> chatbot_20220408_models.UpdateCategoryResponse:
        """
        @summary 编辑类目
        
        @param request: UpdateCategoryRequest
        @return: UpdateCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_category_with_options_async(request, runtime)

    def update_conn_question_with_options(
        self,
        request: chatbot_20220408_models.UpdateConnQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateConnQuestionResponse:
        """
        @summary 更新FAQ关联问
        
        @param request: UpdateConnQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConnQuestionResponse
        """
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
        """
        @summary 更新FAQ关联问
        
        @param request: UpdateConnQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConnQuestionResponse
        """
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
        """
        @summary 更新FAQ关联问
        
        @param request: UpdateConnQuestionRequest
        @return: UpdateConnQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_conn_question_with_options(request, runtime)

    async def update_conn_question_async(
        self,
        request: chatbot_20220408_models.UpdateConnQuestionRequest,
    ) -> chatbot_20220408_models.UpdateConnQuestionResponse:
        """
        @summary 更新FAQ关联问
        
        @param request: UpdateConnQuestionRequest
        @return: UpdateConnQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_conn_question_with_options_async(request, runtime)

    def update_dsentity_with_options(
        self,
        request: chatbot_20220408_models.UpdateDSEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateDSEntityResponse:
        """
        @summary 实体-更新
        
        @param request: UpdateDSEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDSEntityResponse
        """
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
        """
        @summary 实体-更新
        
        @param request: UpdateDSEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDSEntityResponse
        """
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
        """
        @summary 实体-更新
        
        @param request: UpdateDSEntityRequest
        @return: UpdateDSEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dsentity_with_options(request, runtime)

    async def update_dsentity_async(
        self,
        request: chatbot_20220408_models.UpdateDSEntityRequest,
    ) -> chatbot_20220408_models.UpdateDSEntityResponse:
        """
        @summary 实体-更新
        
        @param request: UpdateDSEntityRequest
        @return: UpdateDSEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dsentity_with_options_async(request, runtime)

    def update_dsentity_value_with_options(
        self,
        tmp_req: chatbot_20220408_models.UpdateDSEntityValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateDSEntityValueResponse:
        """
        @summary 实体成员-更新
        
        @param tmp_req: UpdateDSEntityValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDSEntityValueResponse
        """
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
        """
        @summary 实体成员-更新
        
        @param tmp_req: UpdateDSEntityValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDSEntityValueResponse
        """
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
        """
        @summary 实体成员-更新
        
        @param request: UpdateDSEntityValueRequest
        @return: UpdateDSEntityValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dsentity_value_with_options(request, runtime)

    async def update_dsentity_value_async(
        self,
        request: chatbot_20220408_models.UpdateDSEntityValueRequest,
    ) -> chatbot_20220408_models.UpdateDSEntityValueResponse:
        """
        @summary 实体成员-更新
        
        @param request: UpdateDSEntityValueRequest
        @return: UpdateDSEntityValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dsentity_value_with_options_async(request, runtime)

    def update_doc_with_options(
        self,
        tmp_req: chatbot_20220408_models.UpdateDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateDocResponse:
        """
        @summary 文档变更
        
        @param tmp_req: UpdateDocRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDocResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.UpdateDocShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_metadata):
            request.doc_metadata_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_metadata, 'DocMetadata', 'json')
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.doc_metadata_shrink):
            query['DocMetadata'] = request.doc_metadata_shrink
        if not UtilClient.is_unset(request.doc_name):
            query['DocName'] = request.doc_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        if not UtilClient.is_unset(request.meta):
            query['Meta'] = request.meta
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.tag_ids_shrink):
            query['TagIds'] = request.tag_ids_shrink
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDoc',
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
            chatbot_20220408_models.UpdateDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_doc_with_options_async(
        self,
        tmp_req: chatbot_20220408_models.UpdateDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateDocResponse:
        """
        @summary 文档变更
        
        @param tmp_req: UpdateDocRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDocResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.UpdateDocShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_metadata):
            request.doc_metadata_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_metadata, 'DocMetadata', 'json')
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.doc_metadata_shrink):
            query['DocMetadata'] = request.doc_metadata_shrink
        if not UtilClient.is_unset(request.doc_name):
            query['DocName'] = request.doc_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        if not UtilClient.is_unset(request.meta):
            query['Meta'] = request.meta
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.tag_ids_shrink):
            query['TagIds'] = request.tag_ids_shrink
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDoc',
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
            chatbot_20220408_models.UpdateDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_doc(
        self,
        request: chatbot_20220408_models.UpdateDocRequest,
    ) -> chatbot_20220408_models.UpdateDocResponse:
        """
        @summary 文档变更
        
        @param request: UpdateDocRequest
        @return: UpdateDocResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_doc_with_options(request, runtime)

    async def update_doc_async(
        self,
        request: chatbot_20220408_models.UpdateDocRequest,
    ) -> chatbot_20220408_models.UpdateDocResponse:
        """
        @summary 文档变更
        
        @param request: UpdateDocRequest
        @return: UpdateDocResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_doc_with_options_async(request, runtime)

    def update_faq_with_options(
        self,
        tmp_req: chatbot_20220408_models.UpdateFaqRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateFaqResponse:
        """
        @summary 更新FAQ
        
        @param tmp_req: UpdateFaqRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFaqResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.UpdateFaqShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag_id_list):
            request.tag_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_id_list, 'TagIdList', 'json')
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
        if not UtilClient.is_unset(request.tag_id_list_shrink):
            body['TagIdList'] = request.tag_id_list_shrink
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
        tmp_req: chatbot_20220408_models.UpdateFaqRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateFaqResponse:
        """
        @summary 更新FAQ
        
        @param tmp_req: UpdateFaqRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFaqResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.UpdateFaqShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag_id_list):
            request.tag_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_id_list, 'TagIdList', 'json')
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
        if not UtilClient.is_unset(request.tag_id_list_shrink):
            body['TagIdList'] = request.tag_id_list_shrink
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
        """
        @summary 更新FAQ
        
        @param request: UpdateFaqRequest
        @return: UpdateFaqResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_faq_with_options(request, runtime)

    async def update_faq_async(
        self,
        request: chatbot_20220408_models.UpdateFaqRequest,
    ) -> chatbot_20220408_models.UpdateFaqResponse:
        """
        @summary 更新FAQ
        
        @param request: UpdateFaqRequest
        @return: UpdateFaqResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_faq_with_options_async(request, runtime)

    def update_instance_with_options(
        self,
        request: chatbot_20220408_models.UpdateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateInstanceResponse:
        """
        @summary 机器人-修改
        
        @param request: UpdateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceResponse
        """
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
        """
        @summary 机器人-修改
        
        @param request: UpdateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceResponse
        """
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
        """
        @summary 机器人-修改
        
        @param request: UpdateInstanceRequest
        @return: UpdateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_instance_with_options(request, runtime)

    async def update_instance_async(
        self,
        request: chatbot_20220408_models.UpdateInstanceRequest,
    ) -> chatbot_20220408_models.UpdateInstanceResponse:
        """
        @summary 机器人-修改
        
        @param request: UpdateInstanceRequest
        @return: UpdateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_with_options_async(request, runtime)

    def update_intent_with_options(
        self,
        tmp_req: chatbot_20220408_models.UpdateIntentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateIntentResponse:
        """
        @summary 意图-更新
        
        @param tmp_req: UpdateIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIntentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.UpdateIntentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_definition):
            request.intent_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.intent_definition, 'IntentDefinition', 'json')
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
        """
        @summary 意图-更新
        
        @param tmp_req: UpdateIntentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIntentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.UpdateIntentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_definition):
            request.intent_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.intent_definition, 'IntentDefinition', 'json')
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
        """
        @summary 意图-更新
        
        @param request: UpdateIntentRequest
        @return: UpdateIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_intent_with_options(request, runtime)

    async def update_intent_async(
        self,
        request: chatbot_20220408_models.UpdateIntentRequest,
    ) -> chatbot_20220408_models.UpdateIntentResponse:
        """
        @summary 意图-更新
        
        @param request: UpdateIntentRequest
        @return: UpdateIntentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_intent_with_options_async(request, runtime)

    def update_lgf_with_options(
        self,
        tmp_req: chatbot_20220408_models.UpdateLgfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateLgfResponse:
        """
        @summary 意图-LGF-更新
        
        @param tmp_req: UpdateLgfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLgfResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.UpdateLgfShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lgf_definition):
            request.lgf_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lgf_definition, 'LgfDefinition', 'json')
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
        """
        @summary 意图-LGF-更新
        
        @param tmp_req: UpdateLgfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLgfResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.UpdateLgfShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lgf_definition):
            request.lgf_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lgf_definition, 'LgfDefinition', 'json')
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
        """
        @summary 意图-LGF-更新
        
        @param request: UpdateLgfRequest
        @return: UpdateLgfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_lgf_with_options(request, runtime)

    async def update_lgf_async(
        self,
        request: chatbot_20220408_models.UpdateLgfRequest,
    ) -> chatbot_20220408_models.UpdateLgfResponse:
        """
        @summary 意图-LGF-更新
        
        @param request: UpdateLgfRequest
        @return: UpdateLgfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_lgf_with_options_async(request, runtime)

    def update_perspective_with_options(
        self,
        request: chatbot_20220408_models.UpdatePerspectiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdatePerspectiveResponse:
        """
        @summary 视角-修改
        
        @param request: UpdatePerspectiveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePerspectiveResponse
        """
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
        """
        @summary 视角-修改
        
        @param request: UpdatePerspectiveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePerspectiveResponse
        """
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
        """
        @summary 视角-修改
        
        @param request: UpdatePerspectiveRequest
        @return: UpdatePerspectiveResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_perspective_with_options(request, runtime)

    async def update_perspective_async(
        self,
        request: chatbot_20220408_models.UpdatePerspectiveRequest,
    ) -> chatbot_20220408_models.UpdatePerspectiveResponse:
        """
        @summary 视角-修改
        
        @param request: UpdatePerspectiveRequest
        @return: UpdatePerspectiveResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_perspective_with_options_async(request, runtime)

    def update_sim_question_with_options(
        self,
        request: chatbot_20220408_models.UpdateSimQuestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateSimQuestionResponse:
        """
        @summary 更新FAQ相似问
        
        @param request: UpdateSimQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSimQuestionResponse
        """
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
        """
        @summary 更新FAQ相似问
        
        @param request: UpdateSimQuestionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSimQuestionResponse
        """
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
        """
        @summary 更新FAQ相似问
        
        @param request: UpdateSimQuestionRequest
        @return: UpdateSimQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_sim_question_with_options(request, runtime)

    async def update_sim_question_async(
        self,
        request: chatbot_20220408_models.UpdateSimQuestionRequest,
    ) -> chatbot_20220408_models.UpdateSimQuestionResponse:
        """
        @summary 更新FAQ相似问
        
        @param request: UpdateSimQuestionRequest
        @return: UpdateSimQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_sim_question_with_options_async(request, runtime)

    def update_solution_with_options(
        self,
        tmp_req: chatbot_20220408_models.UpdateSolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateSolutionResponse:
        """
        @summary 更新FAQ答案
        
        @param tmp_req: UpdateSolutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSolutionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.UpdateSolutionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag_id_list):
            request.tag_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_id_list, 'TagIdList', 'json')
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
        if not UtilClient.is_unset(request.tag_id_list_shrink):
            body['TagIdList'] = request.tag_id_list_shrink
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
        tmp_req: chatbot_20220408_models.UpdateSolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateSolutionResponse:
        """
        @summary 更新FAQ答案
        
        @param tmp_req: UpdateSolutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSolutionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.UpdateSolutionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag_id_list):
            request.tag_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_id_list, 'TagIdList', 'json')
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
        if not UtilClient.is_unset(request.tag_id_list_shrink):
            body['TagIdList'] = request.tag_id_list_shrink
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
        """
        @summary 更新FAQ答案
        
        @param request: UpdateSolutionRequest
        @return: UpdateSolutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_solution_with_options(request, runtime)

    async def update_solution_async(
        self,
        request: chatbot_20220408_models.UpdateSolutionRequest,
    ) -> chatbot_20220408_models.UpdateSolutionResponse:
        """
        @summary 更新FAQ答案
        
        @param request: UpdateSolutionRequest
        @return: UpdateSolutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_solution_with_options_async(request, runtime)

    def update_tag_with_options(
        self,
        request: chatbot_20220408_models.UpdateTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateTagResponse:
        """
        @summary 标签编辑
        
        @param request: UpdateTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tag_name):
            body['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTag',
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
            chatbot_20220408_models.UpdateTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_tag_with_options_async(
        self,
        request: chatbot_20220408_models.UpdateTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateTagResponse:
        """
        @summary 标签编辑
        
        @param request: UpdateTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tag_name):
            body['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTag',
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
            chatbot_20220408_models.UpdateTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_tag(
        self,
        request: chatbot_20220408_models.UpdateTagRequest,
    ) -> chatbot_20220408_models.UpdateTagResponse:
        """
        @summary 标签编辑
        
        @param request: UpdateTagRequest
        @return: UpdateTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_tag_with_options(request, runtime)

    async def update_tag_async(
        self,
        request: chatbot_20220408_models.UpdateTagRequest,
    ) -> chatbot_20220408_models.UpdateTagResponse:
        """
        @summary 标签编辑
        
        @param request: UpdateTagRequest
        @return: UpdateTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_tag_with_options_async(request, runtime)

    def update_tag_group_with_options(
        self,
        request: chatbot_20220408_models.UpdateTagGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateTagGroupResponse:
        """
        @summary 标签组编辑
        
        @param request: UpdateTagGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTagGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTagGroup',
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
            chatbot_20220408_models.UpdateTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_tag_group_with_options_async(
        self,
        request: chatbot_20220408_models.UpdateTagGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateTagGroupResponse:
        """
        @summary 标签组编辑
        
        @param request: UpdateTagGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTagGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTagGroup',
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
            chatbot_20220408_models.UpdateTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_tag_group(
        self,
        request: chatbot_20220408_models.UpdateTagGroupRequest,
    ) -> chatbot_20220408_models.UpdateTagGroupResponse:
        """
        @summary 标签组编辑
        
        @param request: UpdateTagGroupRequest
        @return: UpdateTagGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_tag_group_with_options(request, runtime)

    async def update_tag_group_async(
        self,
        request: chatbot_20220408_models.UpdateTagGroupRequest,
    ) -> chatbot_20220408_models.UpdateTagGroupResponse:
        """
        @summary 标签组编辑
        
        @param request: UpdateTagGroupRequest
        @return: UpdateTagGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_tag_group_with_options_async(request, runtime)

    def update_user_say_with_options(
        self,
        tmp_req: chatbot_20220408_models.UpdateUserSayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> chatbot_20220408_models.UpdateUserSayResponse:
        """
        @summary 意图-话术-更新
        
        @param tmp_req: UpdateUserSayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserSayResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.UpdateUserSayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_say_definition):
            request.user_say_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_say_definition, 'UserSayDefinition', 'json')
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
        """
        @summary 意图-话术-更新
        
        @param tmp_req: UpdateUserSayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserSayResponse
        """
        UtilClient.validate_model(tmp_req)
        request = chatbot_20220408_models.UpdateUserSayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_say_definition):
            request.user_say_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_say_definition, 'UserSayDefinition', 'json')
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
        """
        @summary 意图-话术-更新
        
        @param request: UpdateUserSayRequest
        @return: UpdateUserSayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_say_with_options(request, runtime)

    async def update_user_say_async(
        self,
        request: chatbot_20220408_models.UpdateUserSayRequest,
    ) -> chatbot_20220408_models.UpdateUserSayResponse:
        """
        @summary 意图-话术-更新
        
        @param request: UpdateUserSayRequest
        @return: UpdateUserSayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_say_with_options_async(request, runtime)
