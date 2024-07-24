# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cams20200606 import models as cams_20200606_models
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
        self._endpoint = self.get_endpoint('cams', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_chatapp_phone_number_with_options(
        self,
        request: cams_20200606_models.AddChatappPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.AddChatappPhoneNumberResponse:
        """
        @summary Adds a phone number for a WhatsApp Business account (WABA).
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddChatappPhoneNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddChatappPhoneNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cc):
            query['Cc'] = request.cc
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.pre_validate_id):
            query['PreValidateId'] = request.pre_validate_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.verified_name):
            query['VerifiedName'] = request.verified_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddChatappPhoneNumber',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.AddChatappPhoneNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_chatapp_phone_number_with_options_async(
        self,
        request: cams_20200606_models.AddChatappPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.AddChatappPhoneNumberResponse:
        """
        @summary Adds a phone number for a WhatsApp Business account (WABA).
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddChatappPhoneNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddChatappPhoneNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cc):
            query['Cc'] = request.cc
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.pre_validate_id):
            query['PreValidateId'] = request.pre_validate_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.verified_name):
            query['VerifiedName'] = request.verified_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddChatappPhoneNumber',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.AddChatappPhoneNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_chatapp_phone_number(
        self,
        request: cams_20200606_models.AddChatappPhoneNumberRequest,
    ) -> cams_20200606_models.AddChatappPhoneNumberResponse:
        """
        @summary Adds a phone number for a WhatsApp Business account (WABA).
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddChatappPhoneNumberRequest
        @return: AddChatappPhoneNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_chatapp_phone_number_with_options(request, runtime)

    async def add_chatapp_phone_number_async(
        self,
        request: cams_20200606_models.AddChatappPhoneNumberRequest,
    ) -> cams_20200606_models.AddChatappPhoneNumberResponse:
        """
        @summary Adds a phone number for a WhatsApp Business account (WABA).
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddChatappPhoneNumberRequest
        @return: AddChatappPhoneNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_chatapp_phone_number_with_options_async(request, runtime)

    def bee_bot_associate_with_options(
        self,
        tmp_req: cams_20200606_models.BeeBotAssociateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.BeeBotAssociateResponse:
        """
        @summary Associates FAQs in the knowledge base.
        
        @description You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: BeeBotAssociateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BeeBotAssociateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.BeeBotAssociateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.perspective):
            request.perspective_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.perspective, 'Perspective', 'json')
        body = {}
        if not UtilClient.is_unset(request.chat_bot_instance_id):
            body['ChatBotInstanceId'] = request.chat_bot_instance_id
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.perspective_shrink):
            body['Perspective'] = request.perspective_shrink
        if not UtilClient.is_unset(request.recommend_num):
            body['RecommendNum'] = request.recommend_num
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.utterance):
            body['Utterance'] = request.utterance
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BeeBotAssociate',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.BeeBotAssociateResponse(),
            self.call_api(params, req, runtime)
        )

    async def bee_bot_associate_with_options_async(
        self,
        tmp_req: cams_20200606_models.BeeBotAssociateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.BeeBotAssociateResponse:
        """
        @summary Associates FAQs in the knowledge base.
        
        @description You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: BeeBotAssociateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BeeBotAssociateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.BeeBotAssociateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.perspective):
            request.perspective_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.perspective, 'Perspective', 'json')
        body = {}
        if not UtilClient.is_unset(request.chat_bot_instance_id):
            body['ChatBotInstanceId'] = request.chat_bot_instance_id
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.perspective_shrink):
            body['Perspective'] = request.perspective_shrink
        if not UtilClient.is_unset(request.recommend_num):
            body['RecommendNum'] = request.recommend_num
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.utterance):
            body['Utterance'] = request.utterance
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BeeBotAssociate',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.BeeBotAssociateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bee_bot_associate(
        self,
        request: cams_20200606_models.BeeBotAssociateRequest,
    ) -> cams_20200606_models.BeeBotAssociateResponse:
        """
        @summary Associates FAQs in the knowledge base.
        
        @description You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: BeeBotAssociateRequest
        @return: BeeBotAssociateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bee_bot_associate_with_options(request, runtime)

    async def bee_bot_associate_async(
        self,
        request: cams_20200606_models.BeeBotAssociateRequest,
    ) -> cams_20200606_models.BeeBotAssociateResponse:
        """
        @summary Associates FAQs in the knowledge base.
        
        @description You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: BeeBotAssociateRequest
        @return: BeeBotAssociateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bee_bot_associate_with_options_async(request, runtime)

    def bee_bot_chat_with_options(
        self,
        tmp_req: cams_20200606_models.BeeBotChatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.BeeBotChatResponse:
        """
        @summary Conducts sessions with the bot based on its unique identifier (ID).
        
        @description You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: BeeBotChatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BeeBotChatResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.BeeBotChatShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.perspective):
            request.perspective_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.perspective, 'Perspective', 'json')
        if not UtilClient.is_unset(tmp_req.vendor_param):
            request.vendor_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vendor_param, 'VendorParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.chat_bot_instance_id):
            body['ChatBotInstanceId'] = request.chat_bot_instance_id
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.intent_name):
            body['IntentName'] = request.intent_name
        if not UtilClient.is_unset(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        if not UtilClient.is_unset(request.perspective_shrink):
            body['Perspective'] = request.perspective_shrink
        if not UtilClient.is_unset(request.sender_id):
            body['SenderId'] = request.sender_id
        if not UtilClient.is_unset(request.sender_nick):
            body['SenderNick'] = request.sender_nick
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.utterance):
            body['Utterance'] = request.utterance
        if not UtilClient.is_unset(request.vendor_param_shrink):
            body['VendorParam'] = request.vendor_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BeeBotChat',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.BeeBotChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def bee_bot_chat_with_options_async(
        self,
        tmp_req: cams_20200606_models.BeeBotChatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.BeeBotChatResponse:
        """
        @summary Conducts sessions with the bot based on its unique identifier (ID).
        
        @description You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: BeeBotChatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BeeBotChatResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.BeeBotChatShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.perspective):
            request.perspective_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.perspective, 'Perspective', 'json')
        if not UtilClient.is_unset(tmp_req.vendor_param):
            request.vendor_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vendor_param, 'VendorParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.chat_bot_instance_id):
            body['ChatBotInstanceId'] = request.chat_bot_instance_id
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.intent_name):
            body['IntentName'] = request.intent_name
        if not UtilClient.is_unset(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        if not UtilClient.is_unset(request.perspective_shrink):
            body['Perspective'] = request.perspective_shrink
        if not UtilClient.is_unset(request.sender_id):
            body['SenderId'] = request.sender_id
        if not UtilClient.is_unset(request.sender_nick):
            body['SenderNick'] = request.sender_nick
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.utterance):
            body['Utterance'] = request.utterance
        if not UtilClient.is_unset(request.vendor_param_shrink):
            body['VendorParam'] = request.vendor_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BeeBotChat',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.BeeBotChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bee_bot_chat(
        self,
        request: cams_20200606_models.BeeBotChatRequest,
    ) -> cams_20200606_models.BeeBotChatResponse:
        """
        @summary Conducts sessions with the bot based on its unique identifier (ID).
        
        @description You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: BeeBotChatRequest
        @return: BeeBotChatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bee_bot_chat_with_options(request, runtime)

    async def bee_bot_chat_async(
        self,
        request: cams_20200606_models.BeeBotChatRequest,
    ) -> cams_20200606_models.BeeBotChatResponse:
        """
        @summary Conducts sessions with the bot based on its unique identifier (ID).
        
        @description You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: BeeBotChatRequest
        @return: BeeBotChatResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bee_bot_chat_with_options_async(request, runtime)

    def chatapp_bind_waba_with_options(
        self,
        request: cams_20200606_models.ChatappBindWabaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ChatappBindWabaResponse:
        """
        @summary Binds the WhatsApp Business account with ChatApp.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappBindWabaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatappBindWabaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChatappBindWaba',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ChatappBindWabaResponse(),
            self.call_api(params, req, runtime)
        )

    async def chatapp_bind_waba_with_options_async(
        self,
        request: cams_20200606_models.ChatappBindWabaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ChatappBindWabaResponse:
        """
        @summary Binds the WhatsApp Business account with ChatApp.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappBindWabaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatappBindWabaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChatappBindWaba',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ChatappBindWabaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chatapp_bind_waba(
        self,
        request: cams_20200606_models.ChatappBindWabaRequest,
    ) -> cams_20200606_models.ChatappBindWabaResponse:
        """
        @summary Binds the WhatsApp Business account with ChatApp.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappBindWabaRequest
        @return: ChatappBindWabaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.chatapp_bind_waba_with_options(request, runtime)

    async def chatapp_bind_waba_async(
        self,
        request: cams_20200606_models.ChatappBindWabaRequest,
    ) -> cams_20200606_models.ChatappBindWabaResponse:
        """
        @summary Binds the WhatsApp Business account with ChatApp.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappBindWabaRequest
        @return: ChatappBindWabaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.chatapp_bind_waba_with_options_async(request, runtime)

    def chatapp_embed_sign_up_with_options(
        self,
        request: cams_20200606_models.ChatappEmbedSignUpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ChatappEmbedSignUpResponse:
        """
        @summary Queries WhatsApp Business account (WABA) information after embedded signup. You do not need to call this API operation if you use Version 2 of WhatsApp embedded signup.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappEmbedSignUpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatappEmbedSignUpResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.input_token):
            body['InputToken'] = request.input_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChatappEmbedSignUp',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ChatappEmbedSignUpResponse(),
            self.call_api(params, req, runtime)
        )

    async def chatapp_embed_sign_up_with_options_async(
        self,
        request: cams_20200606_models.ChatappEmbedSignUpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ChatappEmbedSignUpResponse:
        """
        @summary Queries WhatsApp Business account (WABA) information after embedded signup. You do not need to call this API operation if you use Version 2 of WhatsApp embedded signup.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappEmbedSignUpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatappEmbedSignUpResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.input_token):
            body['InputToken'] = request.input_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChatappEmbedSignUp',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ChatappEmbedSignUpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chatapp_embed_sign_up(
        self,
        request: cams_20200606_models.ChatappEmbedSignUpRequest,
    ) -> cams_20200606_models.ChatappEmbedSignUpResponse:
        """
        @summary Queries WhatsApp Business account (WABA) information after embedded signup. You do not need to call this API operation if you use Version 2 of WhatsApp embedded signup.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappEmbedSignUpRequest
        @return: ChatappEmbedSignUpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.chatapp_embed_sign_up_with_options(request, runtime)

    async def chatapp_embed_sign_up_async(
        self,
        request: cams_20200606_models.ChatappEmbedSignUpRequest,
    ) -> cams_20200606_models.ChatappEmbedSignUpResponse:
        """
        @summary Queries WhatsApp Business account (WABA) information after embedded signup. You do not need to call this API operation if you use Version 2 of WhatsApp embedded signup.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappEmbedSignUpRequest
        @return: ChatappEmbedSignUpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.chatapp_embed_sign_up_with_options_async(request, runtime)

    def chatapp_migration_register_with_options(
        self,
        request: cams_20200606_models.ChatappMigrationRegisterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ChatappMigrationRegisterResponse:
        """
        @summary Registers a phone number for migration.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappMigrationRegisterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatappMigrationRegisterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChatappMigrationRegister',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ChatappMigrationRegisterResponse(),
            self.call_api(params, req, runtime)
        )

    async def chatapp_migration_register_with_options_async(
        self,
        request: cams_20200606_models.ChatappMigrationRegisterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ChatappMigrationRegisterResponse:
        """
        @summary Registers a phone number for migration.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappMigrationRegisterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatappMigrationRegisterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChatappMigrationRegister',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ChatappMigrationRegisterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chatapp_migration_register(
        self,
        request: cams_20200606_models.ChatappMigrationRegisterRequest,
    ) -> cams_20200606_models.ChatappMigrationRegisterResponse:
        """
        @summary Registers a phone number for migration.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappMigrationRegisterRequest
        @return: ChatappMigrationRegisterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.chatapp_migration_register_with_options(request, runtime)

    async def chatapp_migration_register_async(
        self,
        request: cams_20200606_models.ChatappMigrationRegisterRequest,
    ) -> cams_20200606_models.ChatappMigrationRegisterResponse:
        """
        @summary Registers a phone number for migration.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappMigrationRegisterRequest
        @return: ChatappMigrationRegisterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.chatapp_migration_register_with_options_async(request, runtime)

    def chatapp_migration_verified_with_options(
        self,
        request: cams_20200606_models.ChatappMigrationVerifiedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ChatappMigrationVerifiedResponse:
        """
        @summary Verifies a specified phone number for migration.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappMigrationVerifiedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatappMigrationVerifiedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChatappMigrationVerified',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ChatappMigrationVerifiedResponse(),
            self.call_api(params, req, runtime)
        )

    async def chatapp_migration_verified_with_options_async(
        self,
        request: cams_20200606_models.ChatappMigrationVerifiedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ChatappMigrationVerifiedResponse:
        """
        @summary Verifies a specified phone number for migration.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappMigrationVerifiedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatappMigrationVerifiedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChatappMigrationVerified',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ChatappMigrationVerifiedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chatapp_migration_verified(
        self,
        request: cams_20200606_models.ChatappMigrationVerifiedRequest,
    ) -> cams_20200606_models.ChatappMigrationVerifiedResponse:
        """
        @summary Verifies a specified phone number for migration.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappMigrationVerifiedRequest
        @return: ChatappMigrationVerifiedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.chatapp_migration_verified_with_options(request, runtime)

    async def chatapp_migration_verified_async(
        self,
        request: cams_20200606_models.ChatappMigrationVerifiedRequest,
    ) -> cams_20200606_models.ChatappMigrationVerifiedResponse:
        """
        @summary Verifies a specified phone number for migration.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappMigrationVerifiedRequest
        @return: ChatappMigrationVerifiedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.chatapp_migration_verified_with_options_async(request, runtime)

    def chatapp_phone_number_deregister_with_options(
        self,
        request: cams_20200606_models.ChatappPhoneNumberDeregisterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ChatappPhoneNumberDeregisterResponse:
        """
        @summary Deregisters a phone number from a WhatsApp Business account (WABA).
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappPhoneNumberDeregisterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatappPhoneNumberDeregisterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChatappPhoneNumberDeregister',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ChatappPhoneNumberDeregisterResponse(),
            self.call_api(params, req, runtime)
        )

    async def chatapp_phone_number_deregister_with_options_async(
        self,
        request: cams_20200606_models.ChatappPhoneNumberDeregisterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ChatappPhoneNumberDeregisterResponse:
        """
        @summary Deregisters a phone number from a WhatsApp Business account (WABA).
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappPhoneNumberDeregisterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatappPhoneNumberDeregisterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChatappPhoneNumberDeregister',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ChatappPhoneNumberDeregisterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chatapp_phone_number_deregister(
        self,
        request: cams_20200606_models.ChatappPhoneNumberDeregisterRequest,
    ) -> cams_20200606_models.ChatappPhoneNumberDeregisterResponse:
        """
        @summary Deregisters a phone number from a WhatsApp Business account (WABA).
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappPhoneNumberDeregisterRequest
        @return: ChatappPhoneNumberDeregisterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.chatapp_phone_number_deregister_with_options(request, runtime)

    async def chatapp_phone_number_deregister_async(
        self,
        request: cams_20200606_models.ChatappPhoneNumberDeregisterRequest,
    ) -> cams_20200606_models.ChatappPhoneNumberDeregisterResponse:
        """
        @summary Deregisters a phone number from a WhatsApp Business account (WABA).
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappPhoneNumberDeregisterRequest
        @return: ChatappPhoneNumberDeregisterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.chatapp_phone_number_deregister_with_options_async(request, runtime)

    def chatapp_phone_number_register_with_options(
        self,
        request: cams_20200606_models.ChatappPhoneNumberRegisterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ChatappPhoneNumberRegisterResponse:
        """
        @summary Registers a phone number.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappPhoneNumberRegisterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatappPhoneNumberRegisterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChatappPhoneNumberRegister',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ChatappPhoneNumberRegisterResponse(),
            self.call_api(params, req, runtime)
        )

    async def chatapp_phone_number_register_with_options_async(
        self,
        request: cams_20200606_models.ChatappPhoneNumberRegisterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ChatappPhoneNumberRegisterResponse:
        """
        @summary Registers a phone number.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappPhoneNumberRegisterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatappPhoneNumberRegisterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChatappPhoneNumberRegister',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ChatappPhoneNumberRegisterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chatapp_phone_number_register(
        self,
        request: cams_20200606_models.ChatappPhoneNumberRegisterRequest,
    ) -> cams_20200606_models.ChatappPhoneNumberRegisterResponse:
        """
        @summary Registers a phone number.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappPhoneNumberRegisterRequest
        @return: ChatappPhoneNumberRegisterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.chatapp_phone_number_register_with_options(request, runtime)

    async def chatapp_phone_number_register_async(
        self,
        request: cams_20200606_models.ChatappPhoneNumberRegisterRequest,
    ) -> cams_20200606_models.ChatappPhoneNumberRegisterResponse:
        """
        @summary Registers a phone number.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappPhoneNumberRegisterRequest
        @return: ChatappPhoneNumberRegisterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.chatapp_phone_number_register_with_options_async(request, runtime)

    def chatapp_sync_phone_number_with_options(
        self,
        request: cams_20200606_models.ChatappSyncPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ChatappSyncPhoneNumberResponse:
        """
        @summary Synchronizes phone numbers.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappSyncPhoneNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatappSyncPhoneNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChatappSyncPhoneNumber',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ChatappSyncPhoneNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def chatapp_sync_phone_number_with_options_async(
        self,
        request: cams_20200606_models.ChatappSyncPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ChatappSyncPhoneNumberResponse:
        """
        @summary Synchronizes phone numbers.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappSyncPhoneNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatappSyncPhoneNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChatappSyncPhoneNumber',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ChatappSyncPhoneNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chatapp_sync_phone_number(
        self,
        request: cams_20200606_models.ChatappSyncPhoneNumberRequest,
    ) -> cams_20200606_models.ChatappSyncPhoneNumberResponse:
        """
        @summary Synchronizes phone numbers.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappSyncPhoneNumberRequest
        @return: ChatappSyncPhoneNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.chatapp_sync_phone_number_with_options(request, runtime)

    async def chatapp_sync_phone_number_async(
        self,
        request: cams_20200606_models.ChatappSyncPhoneNumberRequest,
    ) -> cams_20200606_models.ChatappSyncPhoneNumberResponse:
        """
        @summary Synchronizes phone numbers.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappSyncPhoneNumberRequest
        @return: ChatappSyncPhoneNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.chatapp_sync_phone_number_with_options_async(request, runtime)

    def chatapp_verify_and_register_with_options(
        self,
        request: cams_20200606_models.ChatappVerifyAndRegisterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ChatappVerifyAndRegisterResponse:
        """
        @summary Associates a phone number with a WhatsApp Business account (WABA).
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappVerifyAndRegisterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatappVerifyAndRegisterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChatappVerifyAndRegister',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ChatappVerifyAndRegisterResponse(),
            self.call_api(params, req, runtime)
        )

    async def chatapp_verify_and_register_with_options_async(
        self,
        request: cams_20200606_models.ChatappVerifyAndRegisterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ChatappVerifyAndRegisterResponse:
        """
        @summary Associates a phone number with a WhatsApp Business account (WABA).
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappVerifyAndRegisterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatappVerifyAndRegisterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChatappVerifyAndRegister',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ChatappVerifyAndRegisterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chatapp_verify_and_register(
        self,
        request: cams_20200606_models.ChatappVerifyAndRegisterRequest,
    ) -> cams_20200606_models.ChatappVerifyAndRegisterResponse:
        """
        @summary Associates a phone number with a WhatsApp Business account (WABA).
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappVerifyAndRegisterRequest
        @return: ChatappVerifyAndRegisterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.chatapp_verify_and_register_with_options(request, runtime)

    async def chatapp_verify_and_register_async(
        self,
        request: cams_20200606_models.ChatappVerifyAndRegisterRequest,
    ) -> cams_20200606_models.ChatappVerifyAndRegisterResponse:
        """
        @summary Associates a phone number with a WhatsApp Business account (WABA).
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ChatappVerifyAndRegisterRequest
        @return: ChatappVerifyAndRegisterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.chatapp_verify_and_register_with_options_async(request, runtime)

    def create_chatapp_migration_initiate_with_options(
        self,
        request: cams_20200606_models.CreateChatappMigrationInitiateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.CreateChatappMigrationInitiateResponse:
        """
        @summary The ID of the number.
        
        @description The status of the phone number.
        
        @param request: CreateChatappMigrationInitiateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChatappMigrationInitiateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.country_code):
            query['CountryCode'] = request.country_code
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.mobile_number):
            query['MobileNumber'] = request.mobile_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChatappMigrationInitiate',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.CreateChatappMigrationInitiateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chatapp_migration_initiate_with_options_async(
        self,
        request: cams_20200606_models.CreateChatappMigrationInitiateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.CreateChatappMigrationInitiateResponse:
        """
        @summary The ID of the number.
        
        @description The status of the phone number.
        
        @param request: CreateChatappMigrationInitiateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChatappMigrationInitiateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.country_code):
            query['CountryCode'] = request.country_code
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.mobile_number):
            query['MobileNumber'] = request.mobile_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChatappMigrationInitiate',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.CreateChatappMigrationInitiateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chatapp_migration_initiate(
        self,
        request: cams_20200606_models.CreateChatappMigrationInitiateRequest,
    ) -> cams_20200606_models.CreateChatappMigrationInitiateResponse:
        """
        @summary The ID of the number.
        
        @description The status of the phone number.
        
        @param request: CreateChatappMigrationInitiateRequest
        @return: CreateChatappMigrationInitiateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_chatapp_migration_initiate_with_options(request, runtime)

    async def create_chatapp_migration_initiate_async(
        self,
        request: cams_20200606_models.CreateChatappMigrationInitiateRequest,
    ) -> cams_20200606_models.CreateChatappMigrationInitiateResponse:
        """
        @summary The ID of the number.
        
        @description The status of the phone number.
        
        @param request: CreateChatappMigrationInitiateRequest
        @return: CreateChatappMigrationInitiateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_chatapp_migration_initiate_with_options_async(request, runtime)

    def create_chatapp_template_with_options(
        self,
        tmp_req: cams_20200606_models.CreateChatappTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.CreateChatappTemplateResponse:
        """
        @summary The HTTP status code.
        \\\\   Example: OK. This parameter indicates that the request is successful.
        \\\\   Other values indicate that the request fails. For more information, see \\[Error codes]\\\\(https://www.alibabacloud.com/help/zh/cams/latest/api-error-codes).
        
        @description The error message.
        
        @param tmp_req: CreateChatappTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChatappTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.CreateChatappTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.components):
            request.components_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.components, 'Components', 'json')
        if not UtilClient.is_unset(tmp_req.example):
            request.example_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.example, 'Example', 'json')
        body = {}
        if not UtilClient.is_unset(request.allow_category_change):
            body['AllowCategoryChange'] = request.allow_category_change
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.components_shrink):
            body['Components'] = request.components_shrink
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            body['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.example_shrink):
            body['Example'] = request.example_shrink
        if not UtilClient.is_unset(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.message_send_ttl_seconds):
            body['MessageSendTtlSeconds'] = request.message_send_ttl_seconds
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateChatappTemplate',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.CreateChatappTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chatapp_template_with_options_async(
        self,
        tmp_req: cams_20200606_models.CreateChatappTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.CreateChatappTemplateResponse:
        """
        @summary The HTTP status code.
        \\\\   Example: OK. This parameter indicates that the request is successful.
        \\\\   Other values indicate that the request fails. For more information, see \\[Error codes]\\\\(https://www.alibabacloud.com/help/zh/cams/latest/api-error-codes).
        
        @description The error message.
        
        @param tmp_req: CreateChatappTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChatappTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.CreateChatappTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.components):
            request.components_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.components, 'Components', 'json')
        if not UtilClient.is_unset(tmp_req.example):
            request.example_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.example, 'Example', 'json')
        body = {}
        if not UtilClient.is_unset(request.allow_category_change):
            body['AllowCategoryChange'] = request.allow_category_change
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.components_shrink):
            body['Components'] = request.components_shrink
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            body['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.example_shrink):
            body['Example'] = request.example_shrink
        if not UtilClient.is_unset(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.message_send_ttl_seconds):
            body['MessageSendTtlSeconds'] = request.message_send_ttl_seconds
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateChatappTemplate',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.CreateChatappTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chatapp_template(
        self,
        request: cams_20200606_models.CreateChatappTemplateRequest,
    ) -> cams_20200606_models.CreateChatappTemplateResponse:
        """
        @summary The HTTP status code.
        \\\\   Example: OK. This parameter indicates that the request is successful.
        \\\\   Other values indicate that the request fails. For more information, see \\[Error codes]\\\\(https://www.alibabacloud.com/help/zh/cams/latest/api-error-codes).
        
        @description The error message.
        
        @param request: CreateChatappTemplateRequest
        @return: CreateChatappTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_chatapp_template_with_options(request, runtime)

    async def create_chatapp_template_async(
        self,
        request: cams_20200606_models.CreateChatappTemplateRequest,
    ) -> cams_20200606_models.CreateChatappTemplateResponse:
        """
        @summary The HTTP status code.
        \\\\   Example: OK. This parameter indicates that the request is successful.
        \\\\   Other values indicate that the request fails. For more information, see \\[Error codes]\\\\(https://www.alibabacloud.com/help/zh/cams/latest/api-error-codes).
        
        @description The error message.
        
        @param request: CreateChatappTemplateRequest
        @return: CreateChatappTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_chatapp_template_with_options_async(request, runtime)

    def create_flow_with_options(
        self,
        tmp_req: cams_20200606_models.CreateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.CreateFlowResponse:
        """
        @summary Creates a Flow.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: CreateFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.CreateFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.categories):
            request.categories_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.categories, 'Categories', 'json')
        body = {}
        if not UtilClient.is_unset(request.categories_shrink):
            body['Categories'] = request.categories_shrink
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFlow',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.CreateFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_with_options_async(
        self,
        tmp_req: cams_20200606_models.CreateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.CreateFlowResponse:
        """
        @summary Creates a Flow.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: CreateFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.CreateFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.categories):
            request.categories_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.categories, 'Categories', 'json')
        body = {}
        if not UtilClient.is_unset(request.categories_shrink):
            body['Categories'] = request.categories_shrink
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFlow',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.CreateFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow(
        self,
        request: cams_20200606_models.CreateFlowRequest,
    ) -> cams_20200606_models.CreateFlowResponse:
        """
        @summary Creates a Flow.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateFlowRequest
        @return: CreateFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_flow_with_options(request, runtime)

    async def create_flow_async(
        self,
        request: cams_20200606_models.CreateFlowRequest,
    ) -> cams_20200606_models.CreateFlowResponse:
        """
        @summary Creates a Flow.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateFlowRequest
        @return: CreateFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_with_options_async(request, runtime)

    def create_phone_message_qrdl_with_options(
        self,
        request: cams_20200606_models.CreatePhoneMessageQrdlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.CreatePhoneMessageQrdlResponse:
        """
        @summary 创建消息发送二维码
        
        @param request: CreatePhoneMessageQrdlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePhoneMessageQrdlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.generate_qr_image):
            body['GenerateQrImage'] = request.generate_qr_image
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.prefilled_message):
            body['PrefilledMessage'] = request.prefilled_message
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePhoneMessageQrdl',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.CreatePhoneMessageQrdlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_phone_message_qrdl_with_options_async(
        self,
        request: cams_20200606_models.CreatePhoneMessageQrdlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.CreatePhoneMessageQrdlResponse:
        """
        @summary 创建消息发送二维码
        
        @param request: CreatePhoneMessageQrdlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePhoneMessageQrdlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.generate_qr_image):
            body['GenerateQrImage'] = request.generate_qr_image
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.prefilled_message):
            body['PrefilledMessage'] = request.prefilled_message
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePhoneMessageQrdl',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.CreatePhoneMessageQrdlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_phone_message_qrdl(
        self,
        request: cams_20200606_models.CreatePhoneMessageQrdlRequest,
    ) -> cams_20200606_models.CreatePhoneMessageQrdlResponse:
        """
        @summary 创建消息发送二维码
        
        @param request: CreatePhoneMessageQrdlRequest
        @return: CreatePhoneMessageQrdlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_phone_message_qrdl_with_options(request, runtime)

    async def create_phone_message_qrdl_async(
        self,
        request: cams_20200606_models.CreatePhoneMessageQrdlRequest,
    ) -> cams_20200606_models.CreatePhoneMessageQrdlResponse:
        """
        @summary 创建消息发送二维码
        
        @param request: CreatePhoneMessageQrdlRequest
        @return: CreatePhoneMessageQrdlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_phone_message_qrdl_with_options_async(request, runtime)

    def delete_chatapp_template_with_options(
        self,
        request: cams_20200606_models.DeleteChatappTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.DeleteChatappTemplateResponse:
        """
        @summary Deletes a message template.
        
        @description ### QPS limit
        You can call this operation up to five times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteChatappTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteChatappTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChatappTemplate',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.DeleteChatappTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chatapp_template_with_options_async(
        self,
        request: cams_20200606_models.DeleteChatappTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.DeleteChatappTemplateResponse:
        """
        @summary Deletes a message template.
        
        @description ### QPS limit
        You can call this operation up to five times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteChatappTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteChatappTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChatappTemplate',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.DeleteChatappTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chatapp_template(
        self,
        request: cams_20200606_models.DeleteChatappTemplateRequest,
    ) -> cams_20200606_models.DeleteChatappTemplateResponse:
        """
        @summary Deletes a message template.
        
        @description ### QPS limit
        You can call this operation up to five times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteChatappTemplateRequest
        @return: DeleteChatappTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_chatapp_template_with_options(request, runtime)

    async def delete_chatapp_template_async(
        self,
        request: cams_20200606_models.DeleteChatappTemplateRequest,
    ) -> cams_20200606_models.DeleteChatappTemplateResponse:
        """
        @summary Deletes a message template.
        
        @description ### QPS limit
        You can call this operation up to five times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteChatappTemplateRequest
        @return: DeleteChatappTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_chatapp_template_with_options_async(request, runtime)

    def delete_flow_with_options(
        self,
        request: cams_20200606_models.DeleteFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.DeleteFlowResponse:
        """
        @summary Deletes a Flow. Only Flows in the DRAFT state can be deleted.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFlowResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFlow',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.DeleteFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_with_options_async(
        self,
        request: cams_20200606_models.DeleteFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.DeleteFlowResponse:
        """
        @summary Deletes a Flow. Only Flows in the DRAFT state can be deleted.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFlowResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFlow',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.DeleteFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow(
        self,
        request: cams_20200606_models.DeleteFlowRequest,
    ) -> cams_20200606_models.DeleteFlowResponse:
        """
        @summary Deletes a Flow. Only Flows in the DRAFT state can be deleted.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteFlowRequest
        @return: DeleteFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_with_options(request, runtime)

    async def delete_flow_async(
        self,
        request: cams_20200606_models.DeleteFlowRequest,
    ) -> cams_20200606_models.DeleteFlowResponse:
        """
        @summary Deletes a Flow. Only Flows in the DRAFT state can be deleted.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteFlowRequest
        @return: DeleteFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_with_options_async(request, runtime)

    def delete_phone_message_qrdl_with_options(
        self,
        request: cams_20200606_models.DeletePhoneMessageQrdlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.DeletePhoneMessageQrdlResponse:
        """
        @summary 删除消息发送二维码
        
        @param request: DeletePhoneMessageQrdlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePhoneMessageQrdlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.qrdl_code):
            body['QrdlCode'] = request.qrdl_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePhoneMessageQrdl',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.DeletePhoneMessageQrdlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_phone_message_qrdl_with_options_async(
        self,
        request: cams_20200606_models.DeletePhoneMessageQrdlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.DeletePhoneMessageQrdlResponse:
        """
        @summary 删除消息发送二维码
        
        @param request: DeletePhoneMessageQrdlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePhoneMessageQrdlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.qrdl_code):
            body['QrdlCode'] = request.qrdl_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePhoneMessageQrdl',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.DeletePhoneMessageQrdlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_phone_message_qrdl(
        self,
        request: cams_20200606_models.DeletePhoneMessageQrdlRequest,
    ) -> cams_20200606_models.DeletePhoneMessageQrdlResponse:
        """
        @summary 删除消息发送二维码
        
        @param request: DeletePhoneMessageQrdlRequest
        @return: DeletePhoneMessageQrdlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_phone_message_qrdl_with_options(request, runtime)

    async def delete_phone_message_qrdl_async(
        self,
        request: cams_20200606_models.DeletePhoneMessageQrdlRequest,
    ) -> cams_20200606_models.DeletePhoneMessageQrdlResponse:
        """
        @summary 删除消息发送二维码
        
        @param request: DeletePhoneMessageQrdlRequest
        @return: DeletePhoneMessageQrdlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_phone_message_qrdl_with_options_async(request, runtime)

    def deprecate_flow_with_options(
        self,
        request: cams_20200606_models.DeprecateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.DeprecateFlowResponse:
        """
        @summary 弃用Flow
        
        @param request: DeprecateFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeprecateFlowResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeprecateFlow',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.DeprecateFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def deprecate_flow_with_options_async(
        self,
        request: cams_20200606_models.DeprecateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.DeprecateFlowResponse:
        """
        @summary 弃用Flow
        
        @param request: DeprecateFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeprecateFlowResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeprecateFlow',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.DeprecateFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deprecate_flow(
        self,
        request: cams_20200606_models.DeprecateFlowRequest,
    ) -> cams_20200606_models.DeprecateFlowResponse:
        """
        @summary 弃用Flow
        
        @param request: DeprecateFlowRequest
        @return: DeprecateFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deprecate_flow_with_options(request, runtime)

    async def deprecate_flow_async(
        self,
        request: cams_20200606_models.DeprecateFlowRequest,
    ) -> cams_20200606_models.DeprecateFlowResponse:
        """
        @summary 弃用Flow
        
        @param request: DeprecateFlowRequest
        @return: DeprecateFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.deprecate_flow_with_options_async(request, runtime)

    def enable_whatsapp_roimetric_with_options(
        self,
        request: cams_20200606_models.EnableWhatsappROIMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.EnableWhatsappROIMetricResponse:
        """
        @summary Enables the statistics on the metrics that are related to WhatsApp.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: EnableWhatsappROIMetricRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableWhatsappROIMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableWhatsappROIMetric',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.EnableWhatsappROIMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_whatsapp_roimetric_with_options_async(
        self,
        request: cams_20200606_models.EnableWhatsappROIMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.EnableWhatsappROIMetricResponse:
        """
        @summary Enables the statistics on the metrics that are related to WhatsApp.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: EnableWhatsappROIMetricRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableWhatsappROIMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableWhatsappROIMetric',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.EnableWhatsappROIMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_whatsapp_roimetric(
        self,
        request: cams_20200606_models.EnableWhatsappROIMetricRequest,
    ) -> cams_20200606_models.EnableWhatsappROIMetricResponse:
        """
        @summary Enables the statistics on the metrics that are related to WhatsApp.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: EnableWhatsappROIMetricRequest
        @return: EnableWhatsappROIMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_whatsapp_roimetric_with_options(request, runtime)

    async def enable_whatsapp_roimetric_async(
        self,
        request: cams_20200606_models.EnableWhatsappROIMetricRequest,
    ) -> cams_20200606_models.EnableWhatsappROIMetricResponse:
        """
        @summary Enables the statistics on the metrics that are related to WhatsApp.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: EnableWhatsappROIMetricRequest
        @return: EnableWhatsappROIMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_whatsapp_roimetric_with_options_async(request, runtime)

    def get_chatapp_phone_number_metric_with_options(
        self,
        request: cams_20200606_models.GetChatappPhoneNumberMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetChatappPhoneNumberMetricResponse:
        """
        @summary Queries the number of messages that are sent by using a phone number by a specific metric.
        
        @description You can call this operation up to 50 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetChatappPhoneNumberMetricRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatappPhoneNumberMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChatappPhoneNumberMetric',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetChatappPhoneNumberMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chatapp_phone_number_metric_with_options_async(
        self,
        request: cams_20200606_models.GetChatappPhoneNumberMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetChatappPhoneNumberMetricResponse:
        """
        @summary Queries the number of messages that are sent by using a phone number by a specific metric.
        
        @description You can call this operation up to 50 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetChatappPhoneNumberMetricRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatappPhoneNumberMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChatappPhoneNumberMetric',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetChatappPhoneNumberMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chatapp_phone_number_metric(
        self,
        request: cams_20200606_models.GetChatappPhoneNumberMetricRequest,
    ) -> cams_20200606_models.GetChatappPhoneNumberMetricResponse:
        """
        @summary Queries the number of messages that are sent by using a phone number by a specific metric.
        
        @description You can call this operation up to 50 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetChatappPhoneNumberMetricRequest
        @return: GetChatappPhoneNumberMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_chatapp_phone_number_metric_with_options(request, runtime)

    async def get_chatapp_phone_number_metric_async(
        self,
        request: cams_20200606_models.GetChatappPhoneNumberMetricRequest,
    ) -> cams_20200606_models.GetChatappPhoneNumberMetricResponse:
        """
        @summary Queries the number of messages that are sent by using a phone number by a specific metric.
        
        @description You can call this operation up to 50 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetChatappPhoneNumberMetricRequest
        @return: GetChatappPhoneNumberMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_chatapp_phone_number_metric_with_options_async(request, runtime)

    def get_chatapp_template_detail_with_options(
        self,
        request: cams_20200606_models.GetChatappTemplateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetChatappTemplateDetailResponse:
        """
        @summary Queries the information of a message template.
        
        @description ### QPS limit
        You can call this API operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetChatappTemplateDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatappTemplateDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChatappTemplateDetail',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetChatappTemplateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chatapp_template_detail_with_options_async(
        self,
        request: cams_20200606_models.GetChatappTemplateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetChatappTemplateDetailResponse:
        """
        @summary Queries the information of a message template.
        
        @description ### QPS limit
        You can call this API operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetChatappTemplateDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatappTemplateDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChatappTemplateDetail',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetChatappTemplateDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chatapp_template_detail(
        self,
        request: cams_20200606_models.GetChatappTemplateDetailRequest,
    ) -> cams_20200606_models.GetChatappTemplateDetailResponse:
        """
        @summary Queries the information of a message template.
        
        @description ### QPS limit
        You can call this API operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetChatappTemplateDetailRequest
        @return: GetChatappTemplateDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_chatapp_template_detail_with_options(request, runtime)

    async def get_chatapp_template_detail_async(
        self,
        request: cams_20200606_models.GetChatappTemplateDetailRequest,
    ) -> cams_20200606_models.GetChatappTemplateDetailResponse:
        """
        @summary Queries the information of a message template.
        
        @description ### QPS limit
        You can call this API operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetChatappTemplateDetailRequest
        @return: GetChatappTemplateDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_chatapp_template_detail_with_options_async(request, runtime)

    def get_chatapp_template_metric_with_options(
        self,
        request: cams_20200606_models.GetChatappTemplateMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetChatappTemplateMetricResponse:
        """
        @summary Queries the metrics about a marketing template.
        
        @description You can call this operation up to 50 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetChatappTemplateMetricRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatappTemplateMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChatappTemplateMetric',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetChatappTemplateMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chatapp_template_metric_with_options_async(
        self,
        request: cams_20200606_models.GetChatappTemplateMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetChatappTemplateMetricResponse:
        """
        @summary Queries the metrics about a marketing template.
        
        @description You can call this operation up to 50 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetChatappTemplateMetricRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatappTemplateMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChatappTemplateMetric',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetChatappTemplateMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chatapp_template_metric(
        self,
        request: cams_20200606_models.GetChatappTemplateMetricRequest,
    ) -> cams_20200606_models.GetChatappTemplateMetricResponse:
        """
        @summary Queries the metrics about a marketing template.
        
        @description You can call this operation up to 50 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetChatappTemplateMetricRequest
        @return: GetChatappTemplateMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_chatapp_template_metric_with_options(request, runtime)

    async def get_chatapp_template_metric_async(
        self,
        request: cams_20200606_models.GetChatappTemplateMetricRequest,
    ) -> cams_20200606_models.GetChatappTemplateMetricResponse:
        """
        @summary Queries the metrics about a marketing template.
        
        @description You can call this operation up to 50 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetChatappTemplateMetricRequest
        @return: GetChatappTemplateMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_chatapp_template_metric_with_options_async(request, runtime)

    def get_chatapp_upload_authorization_with_options(
        self,
        request: cams_20200606_models.GetChatappUploadAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetChatappUploadAuthorizationResponse:
        """
        @summary Obtains the authentication information that is used to upload a file.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetChatappUploadAuthorizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatappUploadAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChatappUploadAuthorization',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetChatappUploadAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chatapp_upload_authorization_with_options_async(
        self,
        request: cams_20200606_models.GetChatappUploadAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetChatappUploadAuthorizationResponse:
        """
        @summary Obtains the authentication information that is used to upload a file.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetChatappUploadAuthorizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatappUploadAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChatappUploadAuthorization',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetChatappUploadAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chatapp_upload_authorization(
        self,
        request: cams_20200606_models.GetChatappUploadAuthorizationRequest,
    ) -> cams_20200606_models.GetChatappUploadAuthorizationResponse:
        """
        @summary Obtains the authentication information that is used to upload a file.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetChatappUploadAuthorizationRequest
        @return: GetChatappUploadAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_chatapp_upload_authorization_with_options(request, runtime)

    async def get_chatapp_upload_authorization_async(
        self,
        request: cams_20200606_models.GetChatappUploadAuthorizationRequest,
    ) -> cams_20200606_models.GetChatappUploadAuthorizationResponse:
        """
        @summary Obtains the authentication information that is used to upload a file.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetChatappUploadAuthorizationRequest
        @return: GetChatappUploadAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_chatapp_upload_authorization_with_options_async(request, runtime)

    def get_chatapp_verify_code_with_options(
        self,
        request: cams_20200606_models.GetChatappVerifyCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetChatappVerifyCodeResponse:
        """
        @summary Obtains a verification code.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetChatappVerifyCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatappVerifyCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        if not UtilClient.is_unset(request.method):
            query['Method'] = request.method
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChatappVerifyCode',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetChatappVerifyCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chatapp_verify_code_with_options_async(
        self,
        request: cams_20200606_models.GetChatappVerifyCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetChatappVerifyCodeResponse:
        """
        @summary Obtains a verification code.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetChatappVerifyCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatappVerifyCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        if not UtilClient.is_unset(request.method):
            query['Method'] = request.method
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChatappVerifyCode',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetChatappVerifyCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chatapp_verify_code(
        self,
        request: cams_20200606_models.GetChatappVerifyCodeRequest,
    ) -> cams_20200606_models.GetChatappVerifyCodeResponse:
        """
        @summary Obtains a verification code.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetChatappVerifyCodeRequest
        @return: GetChatappVerifyCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_chatapp_verify_code_with_options(request, runtime)

    async def get_chatapp_verify_code_async(
        self,
        request: cams_20200606_models.GetChatappVerifyCodeRequest,
    ) -> cams_20200606_models.GetChatappVerifyCodeResponse:
        """
        @summary Obtains a verification code.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetChatappVerifyCodeRequest
        @return: GetChatappVerifyCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_chatapp_verify_code_with_options_async(request, runtime)

    def get_commerce_setting_with_options(
        self,
        request: cams_20200606_models.GetCommerceSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetCommerceSettingResponse:
        """
        @summary Queries the business settings of a phone number.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetCommerceSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCommerceSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCommerceSetting',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetCommerceSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_commerce_setting_with_options_async(
        self,
        request: cams_20200606_models.GetCommerceSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetCommerceSettingResponse:
        """
        @summary Queries the business settings of a phone number.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetCommerceSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCommerceSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCommerceSetting',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetCommerceSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_commerce_setting(
        self,
        request: cams_20200606_models.GetCommerceSettingRequest,
    ) -> cams_20200606_models.GetCommerceSettingResponse:
        """
        @summary Queries the business settings of a phone number.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetCommerceSettingRequest
        @return: GetCommerceSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_commerce_setting_with_options(request, runtime)

    async def get_commerce_setting_async(
        self,
        request: cams_20200606_models.GetCommerceSettingRequest,
    ) -> cams_20200606_models.GetCommerceSettingResponse:
        """
        @summary Queries the business settings of a phone number.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetCommerceSettingRequest
        @return: GetCommerceSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_commerce_setting_with_options_async(request, runtime)

    def get_flow_with_options(
        self,
        request: cams_20200606_models.GetFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetFlowResponse:
        """
        @summary Queries the information about a Flow.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFlowResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFlow',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_flow_with_options_async(
        self,
        request: cams_20200606_models.GetFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetFlowResponse:
        """
        @summary Queries the information about a Flow.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFlowResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFlow',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_flow(
        self,
        request: cams_20200606_models.GetFlowRequest,
    ) -> cams_20200606_models.GetFlowResponse:
        """
        @summary Queries the information about a Flow.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetFlowRequest
        @return: GetFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_flow_with_options(request, runtime)

    async def get_flow_async(
        self,
        request: cams_20200606_models.GetFlowRequest,
    ) -> cams_20200606_models.GetFlowResponse:
        """
        @summary Queries the information about a Flow.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetFlowRequest
        @return: GetFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_flow_with_options_async(request, runtime)

    def get_flow_jsonassest_with_options(
        self,
        request: cams_20200606_models.GetFlowJSONAssestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetFlowJSONAssestResponse:
        """
        @summary 获取flow的JSON文件
        
        @param request: GetFlowJSONAssestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFlowJSONAssestResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFlowJSONAssest',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetFlowJSONAssestResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_flow_jsonassest_with_options_async(
        self,
        request: cams_20200606_models.GetFlowJSONAssestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetFlowJSONAssestResponse:
        """
        @summary 获取flow的JSON文件
        
        @param request: GetFlowJSONAssestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFlowJSONAssestResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFlowJSONAssest',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetFlowJSONAssestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_flow_jsonassest(
        self,
        request: cams_20200606_models.GetFlowJSONAssestRequest,
    ) -> cams_20200606_models.GetFlowJSONAssestResponse:
        """
        @summary 获取flow的JSON文件
        
        @param request: GetFlowJSONAssestRequest
        @return: GetFlowJSONAssestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_flow_jsonassest_with_options(request, runtime)

    async def get_flow_jsonassest_async(
        self,
        request: cams_20200606_models.GetFlowJSONAssestRequest,
    ) -> cams_20200606_models.GetFlowJSONAssestResponse:
        """
        @summary 获取flow的JSON文件
        
        @param request: GetFlowJSONAssestRequest
        @return: GetFlowJSONAssestResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_flow_jsonassest_with_options_async(request, runtime)

    def get_flow_preview_url_with_options(
        self,
        request: cams_20200606_models.GetFlowPreviewUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetFlowPreviewUrlResponse:
        """
        @summary Obtains the preview URL of a Flow.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetFlowPreviewUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFlowPreviewUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFlowPreviewUrl',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetFlowPreviewUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_flow_preview_url_with_options_async(
        self,
        request: cams_20200606_models.GetFlowPreviewUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetFlowPreviewUrlResponse:
        """
        @summary Obtains the preview URL of a Flow.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetFlowPreviewUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFlowPreviewUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFlowPreviewUrl',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetFlowPreviewUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_flow_preview_url(
        self,
        request: cams_20200606_models.GetFlowPreviewUrlRequest,
    ) -> cams_20200606_models.GetFlowPreviewUrlResponse:
        """
        @summary Obtains the preview URL of a Flow.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetFlowPreviewUrlRequest
        @return: GetFlowPreviewUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_flow_preview_url_with_options(request, runtime)

    async def get_flow_preview_url_async(
        self,
        request: cams_20200606_models.GetFlowPreviewUrlRequest,
    ) -> cams_20200606_models.GetFlowPreviewUrlResponse:
        """
        @summary Obtains the preview URL of a Flow.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetFlowPreviewUrlRequest
        @return: GetFlowPreviewUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_flow_preview_url_with_options_async(request, runtime)

    def get_migration_verify_code_with_options(
        self,
        request: cams_20200606_models.GetMigrationVerifyCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetMigrationVerifyCodeResponse:
        """
        @summary The phone number.
        
        @description The ID of the phone number.
        
        @param request: GetMigrationVerifyCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMigrationVerifyCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        if not UtilClient.is_unset(request.method):
            query['Method'] = request.method
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMigrationVerifyCode',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetMigrationVerifyCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_migration_verify_code_with_options_async(
        self,
        request: cams_20200606_models.GetMigrationVerifyCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetMigrationVerifyCodeResponse:
        """
        @summary The phone number.
        
        @description The ID of the phone number.
        
        @param request: GetMigrationVerifyCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMigrationVerifyCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        if not UtilClient.is_unset(request.method):
            query['Method'] = request.method
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMigrationVerifyCode',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetMigrationVerifyCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_migration_verify_code(
        self,
        request: cams_20200606_models.GetMigrationVerifyCodeRequest,
    ) -> cams_20200606_models.GetMigrationVerifyCodeResponse:
        """
        @summary The phone number.
        
        @description The ID of the phone number.
        
        @param request: GetMigrationVerifyCodeRequest
        @return: GetMigrationVerifyCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_migration_verify_code_with_options(request, runtime)

    async def get_migration_verify_code_async(
        self,
        request: cams_20200606_models.GetMigrationVerifyCodeRequest,
    ) -> cams_20200606_models.GetMigrationVerifyCodeResponse:
        """
        @summary The phone number.
        
        @description The ID of the phone number.
        
        @param request: GetMigrationVerifyCodeRequest
        @return: GetMigrationVerifyCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_migration_verify_code_with_options_async(request, runtime)

    def get_permission_by_code_with_options(
        self,
        tmp_req: cams_20200606_models.GetPermissionByCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetPermissionByCodeResponse:
        """
        @summary 根据Code获取权限
        
        @param tmp_req: GetPermissionByCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPermissionByCodeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.GetPermissionByCodeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.permissions):
            request.permissions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.permissions, 'Permissions', 'json')
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.permissions_shrink):
            body['Permissions'] = request.permissions_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPermissionByCode',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetPermissionByCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_permission_by_code_with_options_async(
        self,
        tmp_req: cams_20200606_models.GetPermissionByCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetPermissionByCodeResponse:
        """
        @summary 根据Code获取权限
        
        @param tmp_req: GetPermissionByCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPermissionByCodeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.GetPermissionByCodeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.permissions):
            request.permissions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.permissions, 'Permissions', 'json')
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.permissions_shrink):
            body['Permissions'] = request.permissions_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPermissionByCode',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetPermissionByCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_permission_by_code(
        self,
        request: cams_20200606_models.GetPermissionByCodeRequest,
    ) -> cams_20200606_models.GetPermissionByCodeResponse:
        """
        @summary 根据Code获取权限
        
        @param request: GetPermissionByCodeRequest
        @return: GetPermissionByCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_permission_by_code_with_options(request, runtime)

    async def get_permission_by_code_async(
        self,
        request: cams_20200606_models.GetPermissionByCodeRequest,
    ) -> cams_20200606_models.GetPermissionByCodeResponse:
        """
        @summary 根据Code获取权限
        
        @param request: GetPermissionByCodeRequest
        @return: GetPermissionByCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_permission_by_code_with_options_async(request, runtime)

    def get_phone_encryption_public_key_with_options(
        self,
        request: cams_20200606_models.GetPhoneEncryptionPublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetPhoneEncryptionPublicKeyResponse:
        """
        @summary 获取号码的公钥
        
        @param request: GetPhoneEncryptionPublicKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPhoneEncryptionPublicKeyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPhoneEncryptionPublicKey',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetPhoneEncryptionPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_phone_encryption_public_key_with_options_async(
        self,
        request: cams_20200606_models.GetPhoneEncryptionPublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetPhoneEncryptionPublicKeyResponse:
        """
        @summary 获取号码的公钥
        
        @param request: GetPhoneEncryptionPublicKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPhoneEncryptionPublicKeyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPhoneEncryptionPublicKey',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetPhoneEncryptionPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_phone_encryption_public_key(
        self,
        request: cams_20200606_models.GetPhoneEncryptionPublicKeyRequest,
    ) -> cams_20200606_models.GetPhoneEncryptionPublicKeyResponse:
        """
        @summary 获取号码的公钥
        
        @param request: GetPhoneEncryptionPublicKeyRequest
        @return: GetPhoneEncryptionPublicKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_phone_encryption_public_key_with_options(request, runtime)

    async def get_phone_encryption_public_key_async(
        self,
        request: cams_20200606_models.GetPhoneEncryptionPublicKeyRequest,
    ) -> cams_20200606_models.GetPhoneEncryptionPublicKeyResponse:
        """
        @summary 获取号码的公钥
        
        @param request: GetPhoneEncryptionPublicKeyRequest
        @return: GetPhoneEncryptionPublicKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_phone_encryption_public_key_with_options_async(request, runtime)

    def get_phone_number_verification_status_with_options(
        self,
        request: cams_20200606_models.GetPhoneNumberVerificationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetPhoneNumberVerificationStatusResponse:
        """
        @summary Obtains the verification status of a phone number.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetPhoneNumberVerificationStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPhoneNumberVerificationStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPhoneNumberVerificationStatus',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetPhoneNumberVerificationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_phone_number_verification_status_with_options_async(
        self,
        request: cams_20200606_models.GetPhoneNumberVerificationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetPhoneNumberVerificationStatusResponse:
        """
        @summary Obtains the verification status of a phone number.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetPhoneNumberVerificationStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPhoneNumberVerificationStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPhoneNumberVerificationStatus',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetPhoneNumberVerificationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_phone_number_verification_status(
        self,
        request: cams_20200606_models.GetPhoneNumberVerificationStatusRequest,
    ) -> cams_20200606_models.GetPhoneNumberVerificationStatusResponse:
        """
        @summary Obtains the verification status of a phone number.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetPhoneNumberVerificationStatusRequest
        @return: GetPhoneNumberVerificationStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_phone_number_verification_status_with_options(request, runtime)

    async def get_phone_number_verification_status_async(
        self,
        request: cams_20200606_models.GetPhoneNumberVerificationStatusRequest,
    ) -> cams_20200606_models.GetPhoneNumberVerificationStatusResponse:
        """
        @summary Obtains the verification status of a phone number.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetPhoneNumberVerificationStatusRequest
        @return: GetPhoneNumberVerificationStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_phone_number_verification_status_with_options_async(request, runtime)

    def get_pre_validate_phone_id_with_options(
        self,
        request: cams_20200606_models.GetPreValidatePhoneIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetPreValidatePhoneIdResponse:
        """
        @summary Obtains the ID of a pre-registered phone number used for embedded signup without the need to re-obtain a verification code.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetPreValidatePhoneIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPreValidatePhoneIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.verify_code):
            body['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPreValidatePhoneId',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetPreValidatePhoneIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pre_validate_phone_id_with_options_async(
        self,
        request: cams_20200606_models.GetPreValidatePhoneIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetPreValidatePhoneIdResponse:
        """
        @summary Obtains the ID of a pre-registered phone number used for embedded signup without the need to re-obtain a verification code.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetPreValidatePhoneIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPreValidatePhoneIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.verify_code):
            body['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPreValidatePhoneId',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetPreValidatePhoneIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pre_validate_phone_id(
        self,
        request: cams_20200606_models.GetPreValidatePhoneIdRequest,
    ) -> cams_20200606_models.GetPreValidatePhoneIdResponse:
        """
        @summary Obtains the ID of a pre-registered phone number used for embedded signup without the need to re-obtain a verification code.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetPreValidatePhoneIdRequest
        @return: GetPreValidatePhoneIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_pre_validate_phone_id_with_options(request, runtime)

    async def get_pre_validate_phone_id_async(
        self,
        request: cams_20200606_models.GetPreValidatePhoneIdRequest,
    ) -> cams_20200606_models.GetPreValidatePhoneIdResponse:
        """
        @summary Obtains the ID of a pre-registered phone number used for embedded signup without the need to re-obtain a verification code.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetPreValidatePhoneIdRequest
        @return: GetPreValidatePhoneIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_pre_validate_phone_id_with_options_async(request, runtime)

    def get_whatsapp_connection_catalog_with_options(
        self,
        request: cams_20200606_models.GetWhatsappConnectionCatalogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetWhatsappConnectionCatalogResponse:
        """
        @summary Queries the product catalogs that are associated with a WhatsApp Business account (WABA).
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetWhatsappConnectionCatalogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWhatsappConnectionCatalogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWhatsappConnectionCatalog',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetWhatsappConnectionCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_whatsapp_connection_catalog_with_options_async(
        self,
        request: cams_20200606_models.GetWhatsappConnectionCatalogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetWhatsappConnectionCatalogResponse:
        """
        @summary Queries the product catalogs that are associated with a WhatsApp Business account (WABA).
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetWhatsappConnectionCatalogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWhatsappConnectionCatalogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWhatsappConnectionCatalog',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetWhatsappConnectionCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_whatsapp_connection_catalog(
        self,
        request: cams_20200606_models.GetWhatsappConnectionCatalogRequest,
    ) -> cams_20200606_models.GetWhatsappConnectionCatalogResponse:
        """
        @summary Queries the product catalogs that are associated with a WhatsApp Business account (WABA).
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetWhatsappConnectionCatalogRequest
        @return: GetWhatsappConnectionCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_whatsapp_connection_catalog_with_options(request, runtime)

    async def get_whatsapp_connection_catalog_async(
        self,
        request: cams_20200606_models.GetWhatsappConnectionCatalogRequest,
    ) -> cams_20200606_models.GetWhatsappConnectionCatalogResponse:
        """
        @summary Queries the product catalogs that are associated with a WhatsApp Business account (WABA).
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetWhatsappConnectionCatalogRequest
        @return: GetWhatsappConnectionCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_whatsapp_connection_catalog_with_options_async(request, runtime)

    def isv_get_app_id_with_options(
        self,
        request: cams_20200606_models.IsvGetAppIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.IsvGetAppIdResponse:
        """
        @summary Obtains the application ID under the ISV account.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: IsvGetAppIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IsvGetAppIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.permissions):
            body['Permissions'] = request.permissions
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IsvGetAppId',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.IsvGetAppIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def isv_get_app_id_with_options_async(
        self,
        request: cams_20200606_models.IsvGetAppIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.IsvGetAppIdResponse:
        """
        @summary Obtains the application ID under the ISV account.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: IsvGetAppIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IsvGetAppIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.permissions):
            body['Permissions'] = request.permissions
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IsvGetAppId',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.IsvGetAppIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def isv_get_app_id(
        self,
        request: cams_20200606_models.IsvGetAppIdRequest,
    ) -> cams_20200606_models.IsvGetAppIdResponse:
        """
        @summary Obtains the application ID under the ISV account.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: IsvGetAppIdRequest
        @return: IsvGetAppIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.isv_get_app_id_with_options(request, runtime)

    async def isv_get_app_id_async(
        self,
        request: cams_20200606_models.IsvGetAppIdRequest,
    ) -> cams_20200606_models.IsvGetAppIdResponse:
        """
        @summary Obtains the application ID under the ISV account.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: IsvGetAppIdRequest
        @return: IsvGetAppIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.isv_get_app_id_with_options_async(request, runtime)

    def list_chatapp_template_with_options(
        self,
        tmp_req: cams_20200606_models.ListChatappTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListChatappTemplateResponse:
        """
        @summary Queries message templates.
        
        @description ### QPS limit
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: ListChatappTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChatappTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ListChatappTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not UtilClient.is_unset(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChatappTemplate',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ListChatappTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chatapp_template_with_options_async(
        self,
        tmp_req: cams_20200606_models.ListChatappTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListChatappTemplateResponse:
        """
        @summary Queries message templates.
        
        @description ### QPS limit
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: ListChatappTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChatappTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ListChatappTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not UtilClient.is_unset(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChatappTemplate',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ListChatappTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chatapp_template(
        self,
        request: cams_20200606_models.ListChatappTemplateRequest,
    ) -> cams_20200606_models.ListChatappTemplateResponse:
        """
        @summary Queries message templates.
        
        @description ### QPS limit
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListChatappTemplateRequest
        @return: ListChatappTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_chatapp_template_with_options(request, runtime)

    async def list_chatapp_template_async(
        self,
        request: cams_20200606_models.ListChatappTemplateRequest,
    ) -> cams_20200606_models.ListChatappTemplateResponse:
        """
        @summary Queries message templates.
        
        @description ### QPS limit
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListChatappTemplateRequest
        @return: ListChatappTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_chatapp_template_with_options_async(request, runtime)

    def list_flow_with_options(
        self,
        tmp_req: cams_20200606_models.ListFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListFlowResponse:
        """
        @summary Queries a list of Flows.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: ListFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ListFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.page_shrink):
            body['Page'] = request.page_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFlow',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ListFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_with_options_async(
        self,
        tmp_req: cams_20200606_models.ListFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListFlowResponse:
        """
        @summary Queries a list of Flows.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: ListFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ListFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.page_shrink):
            body['Page'] = request.page_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFlow',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ListFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow(
        self,
        request: cams_20200606_models.ListFlowRequest,
    ) -> cams_20200606_models.ListFlowResponse:
        """
        @summary Queries a list of Flows.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListFlowRequest
        @return: ListFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_flow_with_options(request, runtime)

    async def list_flow_async(
        self,
        request: cams_20200606_models.ListFlowRequest,
    ) -> cams_20200606_models.ListFlowResponse:
        """
        @summary Queries a list of Flows.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListFlowRequest
        @return: ListFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_with_options_async(request, runtime)

    def list_phone_message_qrdl_with_options(
        self,
        request: cams_20200606_models.ListPhoneMessageQrdlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListPhoneMessageQrdlResponse:
        """
        @summary 查询消息发送二维码
        
        @param request: ListPhoneMessageQrdlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPhoneMessageQrdlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPhoneMessageQrdl',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ListPhoneMessageQrdlResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_phone_message_qrdl_with_options_async(
        self,
        request: cams_20200606_models.ListPhoneMessageQrdlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListPhoneMessageQrdlResponse:
        """
        @summary 查询消息发送二维码
        
        @param request: ListPhoneMessageQrdlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPhoneMessageQrdlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPhoneMessageQrdl',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ListPhoneMessageQrdlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_phone_message_qrdl(
        self,
        request: cams_20200606_models.ListPhoneMessageQrdlRequest,
    ) -> cams_20200606_models.ListPhoneMessageQrdlResponse:
        """
        @summary 查询消息发送二维码
        
        @param request: ListPhoneMessageQrdlRequest
        @return: ListPhoneMessageQrdlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_phone_message_qrdl_with_options(request, runtime)

    async def list_phone_message_qrdl_async(
        self,
        request: cams_20200606_models.ListPhoneMessageQrdlRequest,
    ) -> cams_20200606_models.ListPhoneMessageQrdlResponse:
        """
        @summary 查询消息发送二维码
        
        @param request: ListPhoneMessageQrdlRequest
        @return: ListPhoneMessageQrdlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_phone_message_qrdl_with_options_async(request, runtime)

    def list_product_with_options(
        self,
        request: cams_20200606_models.ListProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListProductResponse:
        """
        @summary Queries products in a product catalog.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.after):
            query['After'] = request.after
        if not UtilClient.is_unset(request.before):
            query['Before'] = request.before
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.fields):
            query['Fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProduct',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ListProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_with_options_async(
        self,
        request: cams_20200606_models.ListProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListProductResponse:
        """
        @summary Queries products in a product catalog.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.after):
            query['After'] = request.after
        if not UtilClient.is_unset(request.before):
            query['Before'] = request.before
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.fields):
            query['Fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProduct',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ListProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product(
        self,
        request: cams_20200606_models.ListProductRequest,
    ) -> cams_20200606_models.ListProductResponse:
        """
        @summary Queries products in a product catalog.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListProductRequest
        @return: ListProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_product_with_options(request, runtime)

    async def list_product_async(
        self,
        request: cams_20200606_models.ListProductRequest,
    ) -> cams_20200606_models.ListProductResponse:
        """
        @summary Queries products in a product catalog.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListProductRequest
        @return: ListProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_product_with_options_async(request, runtime)

    def list_product_catalog_with_options(
        self,
        request: cams_20200606_models.ListProductCatalogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListProductCatalogResponse:
        """
        @summary Queries the product catalogs on the Business Manager platform of Meta.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListProductCatalogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductCatalogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.after):
            query['After'] = request.after
        if not UtilClient.is_unset(request.before):
            query['Before'] = request.before
        if not UtilClient.is_unset(request.business_id):
            query['BusinessId'] = request.business_id
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.fields):
            query['Fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductCatalog',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ListProductCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_catalog_with_options_async(
        self,
        request: cams_20200606_models.ListProductCatalogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListProductCatalogResponse:
        """
        @summary Queries the product catalogs on the Business Manager platform of Meta.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListProductCatalogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductCatalogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.after):
            query['After'] = request.after
        if not UtilClient.is_unset(request.before):
            query['Before'] = request.before
        if not UtilClient.is_unset(request.business_id):
            query['BusinessId'] = request.business_id
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.fields):
            query['Fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductCatalog',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ListProductCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_catalog(
        self,
        request: cams_20200606_models.ListProductCatalogRequest,
    ) -> cams_20200606_models.ListProductCatalogResponse:
        """
        @summary Queries the product catalogs on the Business Manager platform of Meta.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListProductCatalogRequest
        @return: ListProductCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_product_catalog_with_options(request, runtime)

    async def list_product_catalog_async(
        self,
        request: cams_20200606_models.ListProductCatalogRequest,
    ) -> cams_20200606_models.ListProductCatalogResponse:
        """
        @summary Queries the product catalogs on the Business Manager platform of Meta.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListProductCatalogRequest
        @return: ListProductCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_product_catalog_with_options_async(request, runtime)

    def modify_chatapp_template_with_options(
        self,
        tmp_req: cams_20200606_models.ModifyChatappTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ModifyChatappTemplateResponse:
        """
        @summary The code of the message template.
        
        @description The name of the message template.
        
        @param tmp_req: ModifyChatappTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyChatappTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ModifyChatappTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.components):
            request.components_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.components, 'Components', 'json')
        if not UtilClient.is_unset(tmp_req.example):
            request.example_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.example, 'Example', 'json')
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.components_shrink):
            body['Components'] = request.components_shrink
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            body['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.example_shrink):
            body['Example'] = request.example_shrink
        if not UtilClient.is_unset(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.message_send_ttl_seconds):
            body['MessageSendTtlSeconds'] = request.message_send_ttl_seconds
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyChatappTemplate',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ModifyChatappTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_chatapp_template_with_options_async(
        self,
        tmp_req: cams_20200606_models.ModifyChatappTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ModifyChatappTemplateResponse:
        """
        @summary The code of the message template.
        
        @description The name of the message template.
        
        @param tmp_req: ModifyChatappTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyChatappTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ModifyChatappTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.components):
            request.components_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.components, 'Components', 'json')
        if not UtilClient.is_unset(tmp_req.example):
            request.example_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.example, 'Example', 'json')
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.components_shrink):
            body['Components'] = request.components_shrink
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            body['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.example_shrink):
            body['Example'] = request.example_shrink
        if not UtilClient.is_unset(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.message_send_ttl_seconds):
            body['MessageSendTtlSeconds'] = request.message_send_ttl_seconds
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyChatappTemplate',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ModifyChatappTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_chatapp_template(
        self,
        request: cams_20200606_models.ModifyChatappTemplateRequest,
    ) -> cams_20200606_models.ModifyChatappTemplateResponse:
        """
        @summary The code of the message template.
        
        @description The name of the message template.
        
        @param request: ModifyChatappTemplateRequest
        @return: ModifyChatappTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_chatapp_template_with_options(request, runtime)

    async def modify_chatapp_template_async(
        self,
        request: cams_20200606_models.ModifyChatappTemplateRequest,
    ) -> cams_20200606_models.ModifyChatappTemplateResponse:
        """
        @summary The code of the message template.
        
        @description The name of the message template.
        
        @param request: ModifyChatappTemplateRequest
        @return: ModifyChatappTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_chatapp_template_with_options_async(request, runtime)

    def modify_flow_with_options(
        self,
        tmp_req: cams_20200606_models.ModifyFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ModifyFlowResponse:
        """
        @summary Modifies the basic information about a Flow.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: ModifyFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ModifyFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.categories):
            request.categories_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.categories, 'Categories', 'json')
        body = {}
        if not UtilClient.is_unset(request.categories_shrink):
            body['Categories'] = request.categories_shrink
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyFlow',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ModifyFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_with_options_async(
        self,
        tmp_req: cams_20200606_models.ModifyFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ModifyFlowResponse:
        """
        @summary Modifies the basic information about a Flow.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: ModifyFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ModifyFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.categories):
            request.categories_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.categories, 'Categories', 'json')
        body = {}
        if not UtilClient.is_unset(request.categories_shrink):
            body['Categories'] = request.categories_shrink
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyFlow',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ModifyFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_flow(
        self,
        request: cams_20200606_models.ModifyFlowRequest,
    ) -> cams_20200606_models.ModifyFlowResponse:
        """
        @summary Modifies the basic information about a Flow.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyFlowRequest
        @return: ModifyFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_with_options(request, runtime)

    async def modify_flow_async(
        self,
        request: cams_20200606_models.ModifyFlowRequest,
    ) -> cams_20200606_models.ModifyFlowResponse:
        """
        @summary Modifies the basic information about a Flow.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyFlowRequest
        @return: ModifyFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_flow_with_options_async(request, runtime)

    def modify_phone_business_profile_with_options(
        self,
        tmp_req: cams_20200606_models.ModifyPhoneBusinessProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ModifyPhoneBusinessProfileResponse:
        """
        @summary The ID of the request.
        
        @description ModifyPhoneBusinessProfile
        
        @param tmp_req: ModifyPhoneBusinessProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPhoneBusinessProfileResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ModifyPhoneBusinessProfileShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.websites):
            request.websites_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.websites, 'Websites', 'json')
        query = {}
        if not UtilClient.is_unset(request.about):
            query['About'] = request.about
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.profile_picture_url):
            query['ProfilePictureUrl'] = request.profile_picture_url
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vertical):
            query['Vertical'] = request.vertical
        if not UtilClient.is_unset(request.websites_shrink):
            query['Websites'] = request.websites_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPhoneBusinessProfile',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ModifyPhoneBusinessProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_phone_business_profile_with_options_async(
        self,
        tmp_req: cams_20200606_models.ModifyPhoneBusinessProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ModifyPhoneBusinessProfileResponse:
        """
        @summary The ID of the request.
        
        @description ModifyPhoneBusinessProfile
        
        @param tmp_req: ModifyPhoneBusinessProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPhoneBusinessProfileResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ModifyPhoneBusinessProfileShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.websites):
            request.websites_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.websites, 'Websites', 'json')
        query = {}
        if not UtilClient.is_unset(request.about):
            query['About'] = request.about
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.profile_picture_url):
            query['ProfilePictureUrl'] = request.profile_picture_url
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vertical):
            query['Vertical'] = request.vertical
        if not UtilClient.is_unset(request.websites_shrink):
            query['Websites'] = request.websites_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPhoneBusinessProfile',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ModifyPhoneBusinessProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_phone_business_profile(
        self,
        request: cams_20200606_models.ModifyPhoneBusinessProfileRequest,
    ) -> cams_20200606_models.ModifyPhoneBusinessProfileResponse:
        """
        @summary The ID of the request.
        
        @description ModifyPhoneBusinessProfile
        
        @param request: ModifyPhoneBusinessProfileRequest
        @return: ModifyPhoneBusinessProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_phone_business_profile_with_options(request, runtime)

    async def modify_phone_business_profile_async(
        self,
        request: cams_20200606_models.ModifyPhoneBusinessProfileRequest,
    ) -> cams_20200606_models.ModifyPhoneBusinessProfileResponse:
        """
        @summary The ID of the request.
        
        @description ModifyPhoneBusinessProfile
        
        @param request: ModifyPhoneBusinessProfileRequest
        @return: ModifyPhoneBusinessProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_phone_business_profile_with_options_async(request, runtime)

    def publish_flow_with_options(
        self,
        request: cams_20200606_models.PublishFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.PublishFlowResponse:
        """
        @summary Publishes a Flow.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PublishFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishFlowResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishFlow',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.PublishFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_flow_with_options_async(
        self,
        request: cams_20200606_models.PublishFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.PublishFlowResponse:
        """
        @summary Publishes a Flow.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PublishFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishFlowResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishFlow',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.PublishFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_flow(
        self,
        request: cams_20200606_models.PublishFlowRequest,
    ) -> cams_20200606_models.PublishFlowResponse:
        """
        @summary Publishes a Flow.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PublishFlowRequest
        @return: PublishFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.publish_flow_with_options(request, runtime)

    async def publish_flow_async(
        self,
        request: cams_20200606_models.PublishFlowRequest,
    ) -> cams_20200606_models.PublishFlowResponse:
        """
        @summary Publishes a Flow.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PublishFlowRequest
        @return: PublishFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.publish_flow_with_options_async(request, runtime)

    def query_chatapp_bind_waba_with_options(
        self,
        request: cams_20200606_models.QueryChatappBindWabaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.QueryChatappBindWabaResponse:
        """
        @summary Query the WhatsApp Business account you associate with ChatApp.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryChatappBindWabaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryChatappBindWabaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryChatappBindWaba',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.QueryChatappBindWabaResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_chatapp_bind_waba_with_options_async(
        self,
        request: cams_20200606_models.QueryChatappBindWabaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.QueryChatappBindWabaResponse:
        """
        @summary Query the WhatsApp Business account you associate with ChatApp.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryChatappBindWabaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryChatappBindWabaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryChatappBindWaba',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.QueryChatappBindWabaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_chatapp_bind_waba(
        self,
        request: cams_20200606_models.QueryChatappBindWabaRequest,
    ) -> cams_20200606_models.QueryChatappBindWabaResponse:
        """
        @summary Query the WhatsApp Business account you associate with ChatApp.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryChatappBindWabaRequest
        @return: QueryChatappBindWabaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_chatapp_bind_waba_with_options(request, runtime)

    async def query_chatapp_bind_waba_async(
        self,
        request: cams_20200606_models.QueryChatappBindWabaRequest,
    ) -> cams_20200606_models.QueryChatappBindWabaResponse:
        """
        @summary Query the WhatsApp Business account you associate with ChatApp.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryChatappBindWabaRequest
        @return: QueryChatappBindWabaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_chatapp_bind_waba_with_options_async(request, runtime)

    def query_chatapp_phone_numbers_with_options(
        self,
        request: cams_20200606_models.QueryChatappPhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.QueryChatappPhoneNumbersResponse:
        """
        @summary Queries phone numbers that receive messages and statuses of these numbers under a specified user.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryChatappPhoneNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryChatappPhoneNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryChatappPhoneNumbers',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.QueryChatappPhoneNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_chatapp_phone_numbers_with_options_async(
        self,
        request: cams_20200606_models.QueryChatappPhoneNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.QueryChatappPhoneNumbersResponse:
        """
        @summary Queries phone numbers that receive messages and statuses of these numbers under a specified user.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryChatappPhoneNumbersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryChatappPhoneNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryChatappPhoneNumbers',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.QueryChatappPhoneNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_chatapp_phone_numbers(
        self,
        request: cams_20200606_models.QueryChatappPhoneNumbersRequest,
    ) -> cams_20200606_models.QueryChatappPhoneNumbersResponse:
        """
        @summary Queries phone numbers that receive messages and statuses of these numbers under a specified user.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryChatappPhoneNumbersRequest
        @return: QueryChatappPhoneNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_chatapp_phone_numbers_with_options(request, runtime)

    async def query_chatapp_phone_numbers_async(
        self,
        request: cams_20200606_models.QueryChatappPhoneNumbersRequest,
    ) -> cams_20200606_models.QueryChatappPhoneNumbersResponse:
        """
        @summary Queries phone numbers that receive messages and statuses of these numbers under a specified user.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryChatappPhoneNumbersRequest
        @return: QueryChatappPhoneNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_chatapp_phone_numbers_with_options_async(request, runtime)

    def query_phone_business_profile_with_options(
        self,
        request: cams_20200606_models.QueryPhoneBusinessProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.QueryPhoneBusinessProfileResponse:
        """
        @summary Queries the business information of the account to which a specified phone number is bound.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryPhoneBusinessProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPhoneBusinessProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPhoneBusinessProfile',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.QueryPhoneBusinessProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_phone_business_profile_with_options_async(
        self,
        request: cams_20200606_models.QueryPhoneBusinessProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.QueryPhoneBusinessProfileResponse:
        """
        @summary Queries the business information of the account to which a specified phone number is bound.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryPhoneBusinessProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPhoneBusinessProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPhoneBusinessProfile',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.QueryPhoneBusinessProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_phone_business_profile(
        self,
        request: cams_20200606_models.QueryPhoneBusinessProfileRequest,
    ) -> cams_20200606_models.QueryPhoneBusinessProfileResponse:
        """
        @summary Queries the business information of the account to which a specified phone number is bound.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryPhoneBusinessProfileRequest
        @return: QueryPhoneBusinessProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_phone_business_profile_with_options(request, runtime)

    async def query_phone_business_profile_async(
        self,
        request: cams_20200606_models.QueryPhoneBusinessProfileRequest,
    ) -> cams_20200606_models.QueryPhoneBusinessProfileResponse:
        """
        @summary Queries the business information of the account to which a specified phone number is bound.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryPhoneBusinessProfileRequest
        @return: QueryPhoneBusinessProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_phone_business_profile_with_options_async(request, runtime)

    def query_waba_business_info_with_options(
        self,
        request: cams_20200606_models.QueryWabaBusinessInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.QueryWabaBusinessInfoResponse:
        """
        @summary Queries the business information about the WhatsApp Business account (WABA).
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryWabaBusinessInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWabaBusinessInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWabaBusinessInfo',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.QueryWabaBusinessInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_waba_business_info_with_options_async(
        self,
        request: cams_20200606_models.QueryWabaBusinessInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.QueryWabaBusinessInfoResponse:
        """
        @summary Queries the business information about the WhatsApp Business account (WABA).
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryWabaBusinessInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWabaBusinessInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWabaBusinessInfo',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.QueryWabaBusinessInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_waba_business_info(
        self,
        request: cams_20200606_models.QueryWabaBusinessInfoRequest,
    ) -> cams_20200606_models.QueryWabaBusinessInfoResponse:
        """
        @summary Queries the business information about the WhatsApp Business account (WABA).
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryWabaBusinessInfoRequest
        @return: QueryWabaBusinessInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_waba_business_info_with_options(request, runtime)

    async def query_waba_business_info_async(
        self,
        request: cams_20200606_models.QueryWabaBusinessInfoRequest,
    ) -> cams_20200606_models.QueryWabaBusinessInfoResponse:
        """
        @summary Queries the business information about the WhatsApp Business account (WABA).
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryWabaBusinessInfoRequest
        @return: QueryWabaBusinessInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_waba_business_info_with_options_async(request, runtime)

    def send_chatapp_mass_message_with_options(
        self,
        tmp_req: cams_20200606_models.SendChatappMassMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.SendChatappMassMessageResponse:
        """
        @summary Sends a message to multiple phone numbers by using ChatAPP at a time.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        You can send messages to up to 1,000 phone numbers in a single request.
        
        @param tmp_req: SendChatappMassMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendChatappMassMessageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.SendChatappMassMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sender_list):
            request.sender_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sender_list, 'SenderList', 'json')
        body = {}
        if not UtilClient.is_unset(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            body['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.fall_back_content):
            body['FallBackContent'] = request.fall_back_content
        if not UtilClient.is_unset(request.fall_back_duration):
            body['FallBackDuration'] = request.fall_back_duration
        if not UtilClient.is_unset(request.fall_back_id):
            body['FallBackId'] = request.fall_back_id
        if not UtilClient.is_unset(request.fall_back_rule):
            body['FallBackRule'] = request.fall_back_rule
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.sender_list_shrink):
            body['SenderList'] = request.sender_list_shrink
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.ttl):
            body['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendChatappMassMessage',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.SendChatappMassMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_chatapp_mass_message_with_options_async(
        self,
        tmp_req: cams_20200606_models.SendChatappMassMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.SendChatappMassMessageResponse:
        """
        @summary Sends a message to multiple phone numbers by using ChatAPP at a time.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        You can send messages to up to 1,000 phone numbers in a single request.
        
        @param tmp_req: SendChatappMassMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendChatappMassMessageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.SendChatappMassMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sender_list):
            request.sender_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sender_list, 'SenderList', 'json')
        body = {}
        if not UtilClient.is_unset(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            body['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.fall_back_content):
            body['FallBackContent'] = request.fall_back_content
        if not UtilClient.is_unset(request.fall_back_duration):
            body['FallBackDuration'] = request.fall_back_duration
        if not UtilClient.is_unset(request.fall_back_id):
            body['FallBackId'] = request.fall_back_id
        if not UtilClient.is_unset(request.fall_back_rule):
            body['FallBackRule'] = request.fall_back_rule
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.sender_list_shrink):
            body['SenderList'] = request.sender_list_shrink
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.ttl):
            body['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendChatappMassMessage',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.SendChatappMassMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_chatapp_mass_message(
        self,
        request: cams_20200606_models.SendChatappMassMessageRequest,
    ) -> cams_20200606_models.SendChatappMassMessageResponse:
        """
        @summary Sends a message to multiple phone numbers by using ChatAPP at a time.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        You can send messages to up to 1,000 phone numbers in a single request.
        
        @param request: SendChatappMassMessageRequest
        @return: SendChatappMassMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_chatapp_mass_message_with_options(request, runtime)

    async def send_chatapp_mass_message_async(
        self,
        request: cams_20200606_models.SendChatappMassMessageRequest,
    ) -> cams_20200606_models.SendChatappMassMessageResponse:
        """
        @summary Sends a message to multiple phone numbers by using ChatAPP at a time.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        You can send messages to up to 1,000 phone numbers in a single request.
        
        @param request: SendChatappMassMessageRequest
        @return: SendChatappMassMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_chatapp_mass_message_with_options_async(request, runtime)

    def send_chatapp_message_with_options(
        self,
        tmp_req: cams_20200606_models.SendChatappMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.SendChatappMessageResponse:
        """
        @summary Sends messages by using ChatAPP.
        
        @description You can call this operation up to 200 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: SendChatappMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendChatappMessageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.SendChatappMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.flow_action):
            request.flow_action_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.flow_action, 'FlowAction', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.product_action):
            request.product_action_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.product_action, 'ProductAction', 'json')
        if not UtilClient.is_unset(tmp_req.template_params):
            request.template_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_params, 'TemplateParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        body = {}
        if not UtilClient.is_unset(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.context_message_id):
            body['ContextMessageId'] = request.context_message_id
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            body['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.fall_back_content):
            body['FallBackContent'] = request.fall_back_content
        if not UtilClient.is_unset(request.fall_back_duration):
            body['FallBackDuration'] = request.fall_back_duration
        if not UtilClient.is_unset(request.fall_back_id):
            body['FallBackId'] = request.fall_back_id
        if not UtilClient.is_unset(request.fall_back_rule):
            body['FallBackRule'] = request.fall_back_rule
        if not UtilClient.is_unset(request.flow_action_shrink):
            body['FlowAction'] = request.flow_action_shrink
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.message_type):
            body['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.product_action_shrink):
            body['ProductAction'] = request.product_action_shrink
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_params_shrink):
            body['TemplateParams'] = request.template_params_shrink
        if not UtilClient.is_unset(request.to):
            body['To'] = request.to
        if not UtilClient.is_unset(request.tracking_data):
            body['TrackingData'] = request.tracking_data
        if not UtilClient.is_unset(request.ttl):
            body['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendChatappMessage',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.SendChatappMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_chatapp_message_with_options_async(
        self,
        tmp_req: cams_20200606_models.SendChatappMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.SendChatappMessageResponse:
        """
        @summary Sends messages by using ChatAPP.
        
        @description You can call this operation up to 200 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: SendChatappMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendChatappMessageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.SendChatappMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.flow_action):
            request.flow_action_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.flow_action, 'FlowAction', 'json')
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.product_action):
            request.product_action_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.product_action, 'ProductAction', 'json')
        if not UtilClient.is_unset(tmp_req.template_params):
            request.template_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_params, 'TemplateParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        body = {}
        if not UtilClient.is_unset(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.context_message_id):
            body['ContextMessageId'] = request.context_message_id
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            body['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.fall_back_content):
            body['FallBackContent'] = request.fall_back_content
        if not UtilClient.is_unset(request.fall_back_duration):
            body['FallBackDuration'] = request.fall_back_duration
        if not UtilClient.is_unset(request.fall_back_id):
            body['FallBackId'] = request.fall_back_id
        if not UtilClient.is_unset(request.fall_back_rule):
            body['FallBackRule'] = request.fall_back_rule
        if not UtilClient.is_unset(request.flow_action_shrink):
            body['FlowAction'] = request.flow_action_shrink
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.message_type):
            body['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.product_action_shrink):
            body['ProductAction'] = request.product_action_shrink
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_params_shrink):
            body['TemplateParams'] = request.template_params_shrink
        if not UtilClient.is_unset(request.to):
            body['To'] = request.to
        if not UtilClient.is_unset(request.tracking_data):
            body['TrackingData'] = request.tracking_data
        if not UtilClient.is_unset(request.ttl):
            body['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendChatappMessage',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.SendChatappMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_chatapp_message(
        self,
        request: cams_20200606_models.SendChatappMessageRequest,
    ) -> cams_20200606_models.SendChatappMessageResponse:
        """
        @summary Sends messages by using ChatAPP.
        
        @description You can call this operation up to 200 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SendChatappMessageRequest
        @return: SendChatappMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_chatapp_message_with_options(request, runtime)

    async def send_chatapp_message_async(
        self,
        request: cams_20200606_models.SendChatappMessageRequest,
    ) -> cams_20200606_models.SendChatappMessageResponse:
        """
        @summary Sends messages by using ChatAPP.
        
        @description You can call this operation up to 200 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SendChatappMessageRequest
        @return: SendChatappMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_chatapp_message_with_options_async(request, runtime)

    def submit_isv_customer_terms_with_options(
        self,
        request: cams_20200606_models.SubmitIsvCustomerTermsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.SubmitIsvCustomerTermsResponse:
        """
        @summary Submits the agreement information for independent software vendor (ISV) customers.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SubmitIsvCustomerTermsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitIsvCustomerTermsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_desc):
            query['BusinessDesc'] = request.business_desc
        if not UtilClient.is_unset(request.contact_mail):
            query['ContactMail'] = request.contact_mail
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.cust_name):
            query['CustName'] = request.cust_name
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.isv_terms):
            query['IsvTerms'] = request.isv_terms
        if not UtilClient.is_unset(request.office_address):
            query['OfficeAddress'] = request.office_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitIsvCustomerTerms',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.SubmitIsvCustomerTermsResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_isv_customer_terms_with_options_async(
        self,
        request: cams_20200606_models.SubmitIsvCustomerTermsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.SubmitIsvCustomerTermsResponse:
        """
        @summary Submits the agreement information for independent software vendor (ISV) customers.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SubmitIsvCustomerTermsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitIsvCustomerTermsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_desc):
            query['BusinessDesc'] = request.business_desc
        if not UtilClient.is_unset(request.contact_mail):
            query['ContactMail'] = request.contact_mail
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.cust_name):
            query['CustName'] = request.cust_name
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.isv_terms):
            query['IsvTerms'] = request.isv_terms
        if not UtilClient.is_unset(request.office_address):
            query['OfficeAddress'] = request.office_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitIsvCustomerTerms',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.SubmitIsvCustomerTermsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_isv_customer_terms(
        self,
        request: cams_20200606_models.SubmitIsvCustomerTermsRequest,
    ) -> cams_20200606_models.SubmitIsvCustomerTermsResponse:
        """
        @summary Submits the agreement information for independent software vendor (ISV) customers.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SubmitIsvCustomerTermsRequest
        @return: SubmitIsvCustomerTermsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_isv_customer_terms_with_options(request, runtime)

    async def submit_isv_customer_terms_async(
        self,
        request: cams_20200606_models.SubmitIsvCustomerTermsRequest,
    ) -> cams_20200606_models.SubmitIsvCustomerTermsResponse:
        """
        @summary Submits the agreement information for independent software vendor (ISV) customers.
        
        @description You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SubmitIsvCustomerTermsRequest
        @return: SubmitIsvCustomerTermsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_isv_customer_terms_with_options_async(request, runtime)

    def update_account_webhook_with_options(
        self,
        request: cams_20200606_models.UpdateAccountWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdateAccountWebhookResponse:
        """
        @summary Modifies the callback URL of an account.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateAccountWebhookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAccountWebhookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.http_flag):
            query['HttpFlag'] = request.http_flag
        if not UtilClient.is_unset(request.queue_flag):
            query['QueueFlag'] = request.queue_flag
        if not UtilClient.is_unset(request.status_callback_url):
            query['StatusCallbackUrl'] = request.status_callback_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccountWebhook',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.UpdateAccountWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_account_webhook_with_options_async(
        self,
        request: cams_20200606_models.UpdateAccountWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdateAccountWebhookResponse:
        """
        @summary Modifies the callback URL of an account.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateAccountWebhookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAccountWebhookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.http_flag):
            query['HttpFlag'] = request.http_flag
        if not UtilClient.is_unset(request.queue_flag):
            query['QueueFlag'] = request.queue_flag
        if not UtilClient.is_unset(request.status_callback_url):
            query['StatusCallbackUrl'] = request.status_callback_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccountWebhook',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.UpdateAccountWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_account_webhook(
        self,
        request: cams_20200606_models.UpdateAccountWebhookRequest,
    ) -> cams_20200606_models.UpdateAccountWebhookResponse:
        """
        @summary Modifies the callback URL of an account.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateAccountWebhookRequest
        @return: UpdateAccountWebhookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_account_webhook_with_options(request, runtime)

    async def update_account_webhook_async(
        self,
        request: cams_20200606_models.UpdateAccountWebhookRequest,
    ) -> cams_20200606_models.UpdateAccountWebhookResponse:
        """
        @summary Modifies the callback URL of an account.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateAccountWebhookRequest
        @return: UpdateAccountWebhookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_account_webhook_with_options_async(request, runtime)

    def update_commerce_setting_with_options(
        self,
        request: cams_20200606_models.UpdateCommerceSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdateCommerceSettingResponse:
        """
        @summary Modifies the business settings of a phone number.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateCommerceSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCommerceSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cart_enable):
            query['CartEnable'] = request.cart_enable
        if not UtilClient.is_unset(request.catalog_visible):
            query['CatalogVisible'] = request.catalog_visible
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCommerceSetting',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.UpdateCommerceSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_commerce_setting_with_options_async(
        self,
        request: cams_20200606_models.UpdateCommerceSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdateCommerceSettingResponse:
        """
        @summary Modifies the business settings of a phone number.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateCommerceSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCommerceSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cart_enable):
            query['CartEnable'] = request.cart_enable
        if not UtilClient.is_unset(request.catalog_visible):
            query['CatalogVisible'] = request.catalog_visible
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCommerceSetting',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.UpdateCommerceSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_commerce_setting(
        self,
        request: cams_20200606_models.UpdateCommerceSettingRequest,
    ) -> cams_20200606_models.UpdateCommerceSettingResponse:
        """
        @summary Modifies the business settings of a phone number.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateCommerceSettingRequest
        @return: UpdateCommerceSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_commerce_setting_with_options(request, runtime)

    async def update_commerce_setting_async(
        self,
        request: cams_20200606_models.UpdateCommerceSettingRequest,
    ) -> cams_20200606_models.UpdateCommerceSettingResponse:
        """
        @summary Modifies the business settings of a phone number.
        
        @description You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateCommerceSettingRequest
        @return: UpdateCommerceSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_commerce_setting_with_options_async(request, runtime)

    def update_flow_jsonasset_with_options(
        self,
        request: cams_20200606_models.UpdateFlowJSONAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdateFlowJSONAssetResponse:
        """
        @summary 更新flow的表单内容
        
        @param request: UpdateFlowJSONAssetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFlowJSONAssetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.file_path):
            body['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFlowJSONAsset',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.UpdateFlowJSONAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_flow_jsonasset_with_options_async(
        self,
        request: cams_20200606_models.UpdateFlowJSONAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdateFlowJSONAssetResponse:
        """
        @summary 更新flow的表单内容
        
        @param request: UpdateFlowJSONAssetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFlowJSONAssetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.file_path):
            body['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.flow_id):
            body['FlowId'] = request.flow_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFlowJSONAsset',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.UpdateFlowJSONAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_flow_jsonasset(
        self,
        request: cams_20200606_models.UpdateFlowJSONAssetRequest,
    ) -> cams_20200606_models.UpdateFlowJSONAssetResponse:
        """
        @summary 更新flow的表单内容
        
        @param request: UpdateFlowJSONAssetRequest
        @return: UpdateFlowJSONAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_flow_jsonasset_with_options(request, runtime)

    async def update_flow_jsonasset_async(
        self,
        request: cams_20200606_models.UpdateFlowJSONAssetRequest,
    ) -> cams_20200606_models.UpdateFlowJSONAssetResponse:
        """
        @summary 更新flow的表单内容
        
        @param request: UpdateFlowJSONAssetRequest
        @return: UpdateFlowJSONAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_flow_jsonasset_with_options_async(request, runtime)

    def update_phone_encryption_public_key_with_options(
        self,
        request: cams_20200606_models.UpdatePhoneEncryptionPublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdatePhoneEncryptionPublicKeyResponse:
        """
        @summary 更新号码的公钥
        
        @param request: UpdatePhoneEncryptionPublicKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePhoneEncryptionPublicKeyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.encryption_public_key):
            body['EncryptionPublicKey'] = request.encryption_public_key
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePhoneEncryptionPublicKey',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.UpdatePhoneEncryptionPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_phone_encryption_public_key_with_options_async(
        self,
        request: cams_20200606_models.UpdatePhoneEncryptionPublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdatePhoneEncryptionPublicKeyResponse:
        """
        @summary 更新号码的公钥
        
        @param request: UpdatePhoneEncryptionPublicKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePhoneEncryptionPublicKeyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.encryption_public_key):
            body['EncryptionPublicKey'] = request.encryption_public_key
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePhoneEncryptionPublicKey',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.UpdatePhoneEncryptionPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_phone_encryption_public_key(
        self,
        request: cams_20200606_models.UpdatePhoneEncryptionPublicKeyRequest,
    ) -> cams_20200606_models.UpdatePhoneEncryptionPublicKeyResponse:
        """
        @summary 更新号码的公钥
        
        @param request: UpdatePhoneEncryptionPublicKeyRequest
        @return: UpdatePhoneEncryptionPublicKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_phone_encryption_public_key_with_options(request, runtime)

    async def update_phone_encryption_public_key_async(
        self,
        request: cams_20200606_models.UpdatePhoneEncryptionPublicKeyRequest,
    ) -> cams_20200606_models.UpdatePhoneEncryptionPublicKeyResponse:
        """
        @summary 更新号码的公钥
        
        @param request: UpdatePhoneEncryptionPublicKeyRequest
        @return: UpdatePhoneEncryptionPublicKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_phone_encryption_public_key_with_options_async(request, runtime)

    def update_phone_message_qrdl_with_options(
        self,
        request: cams_20200606_models.UpdatePhoneMessageQrdlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdatePhoneMessageQrdlResponse:
        """
        @summary 修改消息发送二维码
        
        @param request: UpdatePhoneMessageQrdlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePhoneMessageQrdlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.generate_qr_image):
            body['GenerateQrImage'] = request.generate_qr_image
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.prefilled_message):
            body['PrefilledMessage'] = request.prefilled_message
        if not UtilClient.is_unset(request.qrdl_code):
            body['QrdlCode'] = request.qrdl_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePhoneMessageQrdl',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.UpdatePhoneMessageQrdlResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_phone_message_qrdl_with_options_async(
        self,
        request: cams_20200606_models.UpdatePhoneMessageQrdlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdatePhoneMessageQrdlResponse:
        """
        @summary 修改消息发送二维码
        
        @param request: UpdatePhoneMessageQrdlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePhoneMessageQrdlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.generate_qr_image):
            body['GenerateQrImage'] = request.generate_qr_image
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.prefilled_message):
            body['PrefilledMessage'] = request.prefilled_message
        if not UtilClient.is_unset(request.qrdl_code):
            body['QrdlCode'] = request.qrdl_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePhoneMessageQrdl',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.UpdatePhoneMessageQrdlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_phone_message_qrdl(
        self,
        request: cams_20200606_models.UpdatePhoneMessageQrdlRequest,
    ) -> cams_20200606_models.UpdatePhoneMessageQrdlResponse:
        """
        @summary 修改消息发送二维码
        
        @param request: UpdatePhoneMessageQrdlRequest
        @return: UpdatePhoneMessageQrdlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_phone_message_qrdl_with_options(request, runtime)

    async def update_phone_message_qrdl_async(
        self,
        request: cams_20200606_models.UpdatePhoneMessageQrdlRequest,
    ) -> cams_20200606_models.UpdatePhoneMessageQrdlResponse:
        """
        @summary 修改消息发送二维码
        
        @param request: UpdatePhoneMessageQrdlRequest
        @return: UpdatePhoneMessageQrdlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_phone_message_qrdl_with_options_async(request, runtime)

    def update_phone_webhook_with_options(
        self,
        request: cams_20200606_models.UpdatePhoneWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdatePhoneWebhookResponse:
        """
        @summary The HTTP status code returned.
        A value of OK indicates that the call is successful.
        Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        
        @description The error message returned.
        
        @param request: UpdatePhoneWebhookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePhoneWebhookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.http_flag):
            query['HttpFlag'] = request.http_flag
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.queue_flag):
            query['QueueFlag'] = request.queue_flag
        if not UtilClient.is_unset(request.status_callback_url):
            query['StatusCallbackUrl'] = request.status_callback_url
        if not UtilClient.is_unset(request.up_callback_url):
            query['UpCallbackUrl'] = request.up_callback_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePhoneWebhook',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.UpdatePhoneWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_phone_webhook_with_options_async(
        self,
        request: cams_20200606_models.UpdatePhoneWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdatePhoneWebhookResponse:
        """
        @summary The HTTP status code returned.
        A value of OK indicates that the call is successful.
        Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        
        @description The error message returned.
        
        @param request: UpdatePhoneWebhookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePhoneWebhookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.http_flag):
            query['HttpFlag'] = request.http_flag
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.queue_flag):
            query['QueueFlag'] = request.queue_flag
        if not UtilClient.is_unset(request.status_callback_url):
            query['StatusCallbackUrl'] = request.status_callback_url
        if not UtilClient.is_unset(request.up_callback_url):
            query['UpCallbackUrl'] = request.up_callback_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePhoneWebhook',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.UpdatePhoneWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_phone_webhook(
        self,
        request: cams_20200606_models.UpdatePhoneWebhookRequest,
    ) -> cams_20200606_models.UpdatePhoneWebhookResponse:
        """
        @summary The HTTP status code returned.
        A value of OK indicates that the call is successful.
        Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        
        @description The error message returned.
        
        @param request: UpdatePhoneWebhookRequest
        @return: UpdatePhoneWebhookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_phone_webhook_with_options(request, runtime)

    async def update_phone_webhook_async(
        self,
        request: cams_20200606_models.UpdatePhoneWebhookRequest,
    ) -> cams_20200606_models.UpdatePhoneWebhookResponse:
        """
        @summary The HTTP status code returned.
        A value of OK indicates that the call is successful.
        Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        
        @description The error message returned.
        
        @param request: UpdatePhoneWebhookRequest
        @return: UpdatePhoneWebhookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_phone_webhook_with_options_async(request, runtime)
