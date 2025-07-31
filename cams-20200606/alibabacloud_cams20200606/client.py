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

    def add_chat_group_with_options(
        self,
        request: cams_20200606_models.AddChatGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.AddChatGroupResponse:
        """
        @summary AddChatGroup
        
        @param request: AddChatGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddChatGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddChatGroup',
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
            cams_20200606_models.AddChatGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_chat_group_with_options_async(
        self,
        request: cams_20200606_models.AddChatGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.AddChatGroupResponse:
        """
        @summary AddChatGroup
        
        @param request: AddChatGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddChatGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddChatGroup',
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
            cams_20200606_models.AddChatGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_chat_group(
        self,
        request: cams_20200606_models.AddChatGroupRequest,
    ) -> cams_20200606_models.AddChatGroupResponse:
        """
        @summary AddChatGroup
        
        @param request: AddChatGroupRequest
        @return: AddChatGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_chat_group_with_options(request, runtime)

    async def add_chat_group_async(
        self,
        request: cams_20200606_models.AddChatGroupRequest,
    ) -> cams_20200606_models.AddChatGroupResponse:
        """
        @summary AddChatGroup
        
        @param request: AddChatGroupRequest
        @return: AddChatGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_chat_group_with_options_async(request, runtime)

    def add_chat_group_invite_link_with_options(
        self,
        request: cams_20200606_models.AddChatGroupInviteLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.AddChatGroupInviteLinkResponse:
        """
        @summary AddChatGroupInviteLink
        
        @param request: AddChatGroupInviteLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddChatGroupInviteLinkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
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
            action='AddChatGroupInviteLink',
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
            cams_20200606_models.AddChatGroupInviteLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_chat_group_invite_link_with_options_async(
        self,
        request: cams_20200606_models.AddChatGroupInviteLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.AddChatGroupInviteLinkResponse:
        """
        @summary AddChatGroupInviteLink
        
        @param request: AddChatGroupInviteLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddChatGroupInviteLinkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
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
            action='AddChatGroupInviteLink',
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
            cams_20200606_models.AddChatGroupInviteLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_chat_group_invite_link(
        self,
        request: cams_20200606_models.AddChatGroupInviteLinkRequest,
    ) -> cams_20200606_models.AddChatGroupInviteLinkResponse:
        """
        @summary AddChatGroupInviteLink
        
        @param request: AddChatGroupInviteLinkRequest
        @return: AddChatGroupInviteLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_chat_group_invite_link_with_options(request, runtime)

    async def add_chat_group_invite_link_async(
        self,
        request: cams_20200606_models.AddChatGroupInviteLinkRequest,
    ) -> cams_20200606_models.AddChatGroupInviteLinkResponse:
        """
        @summary AddChatGroupInviteLink
        
        @param request: AddChatGroupInviteLinkRequest
        @return: AddChatGroupInviteLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_chat_group_invite_link_with_options_async(request, runtime)

    def add_chatapp_phone_number_with_options(
        self,
        request: cams_20200606_models.AddChatappPhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.AddChatappPhoneNumberResponse:
        """
        @summary Adds a phone number for a WhatsApp Business account (WABA).
        
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
        
        @param request: AddChatappPhoneNumberRequest
        @return: AddChatappPhoneNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_chatapp_phone_number_with_options_async(request, runtime)

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
        query = {}
        if not UtilClient.is_unset(request.input_token):
            query['InputToken'] = request.input_token
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
        query = {}
        if not UtilClient.is_unset(request.input_token):
            query['InputToken'] = request.input_token
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
        
        @description The space ID of the RAM user within the independent software vendor (ISV) account.
        
        @param request: ChatappMigrationRegisterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatappMigrationRegisterResponse
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
        
        @description The space ID of the RAM user within the independent software vendor (ISV) account.
        
        @param request: ChatappMigrationRegisterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatappMigrationRegisterResponse
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
        
        @description The space ID of the RAM user within the independent software vendor (ISV) account.
        
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
        
        @description The space ID of the RAM user within the independent software vendor (ISV) account.
        
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

    def create_chat_flow_with_options(
        self,
        tmp_req: cams_20200606_models.CreateChatFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.CreateChatFlowResponse:
        """
        @summary Create Chatflow
        
        @param tmp_req: CreateChatFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChatFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.CreateChatFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_trigger_type):
            query['FlowTriggerType'] = request.flow_trigger_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChatFlow',
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
            cams_20200606_models.CreateChatFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chat_flow_with_options_async(
        self,
        tmp_req: cams_20200606_models.CreateChatFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.CreateChatFlowResponse:
        """
        @summary Create Chatflow
        
        @param tmp_req: CreateChatFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChatFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.CreateChatFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_trigger_type):
            query['FlowTriggerType'] = request.flow_trigger_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChatFlow',
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
            cams_20200606_models.CreateChatFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chat_flow(
        self,
        request: cams_20200606_models.CreateChatFlowRequest,
    ) -> cams_20200606_models.CreateChatFlowResponse:
        """
        @summary Create Chatflow
        
        @param request: CreateChatFlowRequest
        @return: CreateChatFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_chat_flow_with_options(request, runtime)

    async def create_chat_flow_async(
        self,
        request: cams_20200606_models.CreateChatFlowRequest,
    ) -> cams_20200606_models.CreateChatFlowResponse:
        """
        @summary Create Chatflow
        
        @param request: CreateChatFlowRequest
        @return: CreateChatFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_chat_flow_with_options_async(request, runtime)

    def create_chat_flow_by_import_with_options(
        self,
        tmp_req: cams_20200606_models.CreateChatFlowByImportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.CreateChatFlowByImportResponse:
        """
        @summary Import and create flow
        
        @param tmp_req: CreateChatFlowByImportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChatFlowByImportResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.CreateChatFlowByImportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_view_model):
            query['FlowViewModel'] = request.flow_view_model
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChatFlowByImport',
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
            cams_20200606_models.CreateChatFlowByImportResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chat_flow_by_import_with_options_async(
        self,
        tmp_req: cams_20200606_models.CreateChatFlowByImportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.CreateChatFlowByImportResponse:
        """
        @summary Import and create flow
        
        @param tmp_req: CreateChatFlowByImportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChatFlowByImportResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.CreateChatFlowByImportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_view_model):
            query['FlowViewModel'] = request.flow_view_model
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChatFlowByImport',
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
            cams_20200606_models.CreateChatFlowByImportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chat_flow_by_import(
        self,
        request: cams_20200606_models.CreateChatFlowByImportRequest,
    ) -> cams_20200606_models.CreateChatFlowByImportResponse:
        """
        @summary Import and create flow
        
        @param request: CreateChatFlowByImportRequest
        @return: CreateChatFlowByImportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_chat_flow_by_import_with_options(request, runtime)

    async def create_chat_flow_by_import_async(
        self,
        request: cams_20200606_models.CreateChatFlowByImportRequest,
    ) -> cams_20200606_models.CreateChatFlowByImportResponse:
        """
        @summary Import and create flow
        
        @param request: CreateChatFlowByImportRequest
        @return: CreateChatFlowByImportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_chat_flow_by_import_with_options_async(request, runtime)

    def create_chat_flow_log_setting_with_options(
        self,
        request: cams_20200606_models.CreateChatFlowLogSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.CreateChatFlowLogSettingResponse:
        """
        @summary Create chatFlow log setting
        
        @param request: CreateChatFlowLogSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChatFlowLogSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
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
            action='CreateChatFlowLogSetting',
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
            cams_20200606_models.CreateChatFlowLogSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chat_flow_log_setting_with_options_async(
        self,
        request: cams_20200606_models.CreateChatFlowLogSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.CreateChatFlowLogSettingResponse:
        """
        @summary Create chatFlow log setting
        
        @param request: CreateChatFlowLogSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChatFlowLogSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
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
            action='CreateChatFlowLogSetting',
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
            cams_20200606_models.CreateChatFlowLogSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chat_flow_log_setting(
        self,
        request: cams_20200606_models.CreateChatFlowLogSettingRequest,
    ) -> cams_20200606_models.CreateChatFlowLogSettingResponse:
        """
        @summary Create chatFlow log setting
        
        @param request: CreateChatFlowLogSettingRequest
        @return: CreateChatFlowLogSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_chat_flow_log_setting_with_options(request, runtime)

    async def create_chat_flow_log_setting_async(
        self,
        request: cams_20200606_models.CreateChatFlowLogSettingRequest,
    ) -> cams_20200606_models.CreateChatFlowLogSettingResponse:
        """
        @summary Create chatFlow log setting
        
        @param request: CreateChatFlowLogSettingRequest
        @return: CreateChatFlowLogSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_chat_flow_log_setting_with_options_async(request, runtime)

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
        \\\\\\\\   Example: OK. This parameter indicates that the request is successful.
        \\\\\\\\   Other values indicate that the request fails. For more information, see \\\\\\[Error codes]\\\\\\(https://www.alibabacloud.com/help/zh/cams/latest/api-error-codes).
        
        @description ### [](#qps-)QPS limit
        You can call this operation up to 50 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        if not UtilClient.is_unset(request.category_change_paused):
            body['CategoryChangePaused'] = request.category_change_paused
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
        \\\\\\\\   Example: OK. This parameter indicates that the request is successful.
        \\\\\\\\   Other values indicate that the request fails. For more information, see \\\\\\[Error codes]\\\\\\(https://www.alibabacloud.com/help/zh/cams/latest/api-error-codes).
        
        @description ### [](#qps-)QPS limit
        You can call this operation up to 50 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        if not UtilClient.is_unset(request.category_change_paused):
            body['CategoryChangePaused'] = request.category_change_paused
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
        \\\\\\\\   Example: OK. This parameter indicates that the request is successful.
        \\\\\\\\   Other values indicate that the request fails. For more information, see \\\\\\[Error codes]\\\\\\(https://www.alibabacloud.com/help/zh/cams/latest/api-error-codes).
        
        @description ### [](#qps-)QPS limit
        You can call this operation up to 50 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        \\\\\\\\   Example: OK. This parameter indicates that the request is successful.
        \\\\\\\\   Other values indicate that the request fails. For more information, see \\\\\\[Error codes]\\\\\\(https://www.alibabacloud.com/help/zh/cams/latest/api-error-codes).
        
        @description ### [](#qps-)QPS limit
        You can call this operation up to 50 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        query = {}
        if not UtilClient.is_unset(request.categories_shrink):
            query['Categories'] = request.categories_shrink
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_name):
            query['FlowName'] = request.flow_name
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
        query = {}
        if not UtilClient.is_unset(request.categories_shrink):
            query['Categories'] = request.categories_shrink
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_name):
            query['FlowName'] = request.flow_name
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

    def create_flow_version_with_options(
        self,
        tmp_req: cams_20200606_models.CreateFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.CreateFlowVersionResponse:
        """
        @summary CreateFlowVersion
        
        @param tmp_req: CreateFlowVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFlowVersionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.CreateFlowVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.flow_version_copy_from):
            query['FlowVersionCopyFrom'] = request.flow_version_copy_from
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowVersion',
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
            cams_20200606_models.CreateFlowVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_version_with_options_async(
        self,
        tmp_req: cams_20200606_models.CreateFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.CreateFlowVersionResponse:
        """
        @summary CreateFlowVersion
        
        @param tmp_req: CreateFlowVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFlowVersionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.CreateFlowVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.flow_version_copy_from):
            query['FlowVersionCopyFrom'] = request.flow_version_copy_from
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowVersion',
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
            cams_20200606_models.CreateFlowVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow_version(
        self,
        request: cams_20200606_models.CreateFlowVersionRequest,
    ) -> cams_20200606_models.CreateFlowVersionResponse:
        """
        @summary CreateFlowVersion
        
        @param request: CreateFlowVersionRequest
        @return: CreateFlowVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_flow_version_with_options(request, runtime)

    async def create_flow_version_async(
        self,
        request: cams_20200606_models.CreateFlowVersionRequest,
    ) -> cams_20200606_models.CreateFlowVersionResponse:
        """
        @summary CreateFlowVersion
        
        @param request: CreateFlowVersionRequest
        @return: CreateFlowVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_version_with_options_async(request, runtime)

    def create_phone_message_qrdl_with_options(
        self,
        request: cams_20200606_models.CreatePhoneMessageQrdlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.CreatePhoneMessageQrdlResponse:
        """
        @summary Creates a quick-response (QR) code that contains a message.
        
        @param request: CreatePhoneMessageQrdlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePhoneMessageQrdlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.generate_qr_image):
            query['GenerateQrImage'] = request.generate_qr_image
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.prefilled_message):
            query['PrefilledMessage'] = request.prefilled_message
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
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
        @summary Creates a quick-response (QR) code that contains a message.
        
        @param request: CreatePhoneMessageQrdlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePhoneMessageQrdlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.generate_qr_image):
            query['GenerateQrImage'] = request.generate_qr_image
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.prefilled_message):
            query['PrefilledMessage'] = request.prefilled_message
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
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
        @summary Creates a quick-response (QR) code that contains a message.
        
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
        @summary Creates a quick-response (QR) code that contains a message.
        
        @param request: CreatePhoneMessageQrdlRequest
        @return: CreatePhoneMessageQrdlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_phone_message_qrdl_with_options_async(request, runtime)

    def delete_chat_flow_with_options(
        self,
        tmp_req: cams_20200606_models.DeleteChatFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.DeleteChatFlowResponse:
        """
        @summary Delete Process
        
        @param tmp_req: DeleteChatFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteChatFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.DeleteChatFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
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
            action='DeleteChatFlow',
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
            cams_20200606_models.DeleteChatFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chat_flow_with_options_async(
        self,
        tmp_req: cams_20200606_models.DeleteChatFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.DeleteChatFlowResponse:
        """
        @summary Delete Process
        
        @param tmp_req: DeleteChatFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteChatFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.DeleteChatFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
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
            action='DeleteChatFlow',
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
            cams_20200606_models.DeleteChatFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chat_flow(
        self,
        request: cams_20200606_models.DeleteChatFlowRequest,
    ) -> cams_20200606_models.DeleteChatFlowResponse:
        """
        @summary Delete Process
        
        @param request: DeleteChatFlowRequest
        @return: DeleteChatFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_chat_flow_with_options(request, runtime)

    async def delete_chat_flow_async(
        self,
        request: cams_20200606_models.DeleteChatFlowRequest,
    ) -> cams_20200606_models.DeleteChatFlowResponse:
        """
        @summary Delete Process
        
        @param request: DeleteChatFlowRequest
        @return: DeleteChatFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_chat_flow_with_options_async(request, runtime)

    def delete_chat_group_with_options(
        self,
        request: cams_20200606_models.DeleteChatGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.DeleteChatGroupResponse:
        """
        @summary DeleteChatGroup
        
        @param request: DeleteChatGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteChatGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
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
            action='DeleteChatGroup',
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
            cams_20200606_models.DeleteChatGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chat_group_with_options_async(
        self,
        request: cams_20200606_models.DeleteChatGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.DeleteChatGroupResponse:
        """
        @summary DeleteChatGroup
        
        @param request: DeleteChatGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteChatGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
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
            action='DeleteChatGroup',
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
            cams_20200606_models.DeleteChatGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chat_group(
        self,
        request: cams_20200606_models.DeleteChatGroupRequest,
    ) -> cams_20200606_models.DeleteChatGroupResponse:
        """
        @summary DeleteChatGroup
        
        @param request: DeleteChatGroupRequest
        @return: DeleteChatGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_chat_group_with_options(request, runtime)

    async def delete_chat_group_async(
        self,
        request: cams_20200606_models.DeleteChatGroupRequest,
    ) -> cams_20200606_models.DeleteChatGroupResponse:
        """
        @summary DeleteChatGroup
        
        @param request: DeleteChatGroupRequest
        @return: DeleteChatGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_chat_group_with_options_async(request, runtime)

    def delete_chat_group_invite_link_with_options(
        self,
        request: cams_20200606_models.DeleteChatGroupInviteLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.DeleteChatGroupInviteLinkResponse:
        """
        @summary DeleteChatGroupInviteLink
        
        @param request: DeleteChatGroupInviteLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteChatGroupInviteLinkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
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
            action='DeleteChatGroupInviteLink',
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
            cams_20200606_models.DeleteChatGroupInviteLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chat_group_invite_link_with_options_async(
        self,
        request: cams_20200606_models.DeleteChatGroupInviteLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.DeleteChatGroupInviteLinkResponse:
        """
        @summary DeleteChatGroupInviteLink
        
        @param request: DeleteChatGroupInviteLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteChatGroupInviteLinkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
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
            action='DeleteChatGroupInviteLink',
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
            cams_20200606_models.DeleteChatGroupInviteLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chat_group_invite_link(
        self,
        request: cams_20200606_models.DeleteChatGroupInviteLinkRequest,
    ) -> cams_20200606_models.DeleteChatGroupInviteLinkResponse:
        """
        @summary DeleteChatGroupInviteLink
        
        @param request: DeleteChatGroupInviteLinkRequest
        @return: DeleteChatGroupInviteLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_chat_group_invite_link_with_options(request, runtime)

    async def delete_chat_group_invite_link_async(
        self,
        request: cams_20200606_models.DeleteChatGroupInviteLinkRequest,
    ) -> cams_20200606_models.DeleteChatGroupInviteLinkResponse:
        """
        @summary DeleteChatGroupInviteLink
        
        @param request: DeleteChatGroupInviteLinkRequest
        @return: DeleteChatGroupInviteLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_chat_group_invite_link_with_options_async(request, runtime)

    def delete_chat_group_participants_with_options(
        self,
        tmp_req: cams_20200606_models.DeleteChatGroupParticipantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.DeleteChatGroupParticipantsResponse:
        """
        @summary DeleteChatGroupParticipants
        
        @param tmp_req: DeleteChatGroupParticipantsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteChatGroupParticipantsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.DeleteChatGroupParticipantsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list):
            request.list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list, 'List', 'json')
        query = {}
        if not UtilClient.is_unset(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.list_shrink):
            query['List'] = request.list_shrink
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
            action='DeleteChatGroupParticipants',
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
            cams_20200606_models.DeleteChatGroupParticipantsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chat_group_participants_with_options_async(
        self,
        tmp_req: cams_20200606_models.DeleteChatGroupParticipantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.DeleteChatGroupParticipantsResponse:
        """
        @summary DeleteChatGroupParticipants
        
        @param tmp_req: DeleteChatGroupParticipantsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteChatGroupParticipantsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.DeleteChatGroupParticipantsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list):
            request.list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list, 'List', 'json')
        query = {}
        if not UtilClient.is_unset(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.list_shrink):
            query['List'] = request.list_shrink
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
            action='DeleteChatGroupParticipants',
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
            cams_20200606_models.DeleteChatGroupParticipantsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chat_group_participants(
        self,
        request: cams_20200606_models.DeleteChatGroupParticipantsRequest,
    ) -> cams_20200606_models.DeleteChatGroupParticipantsResponse:
        """
        @summary DeleteChatGroupParticipants
        
        @param request: DeleteChatGroupParticipantsRequest
        @return: DeleteChatGroupParticipantsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_chat_group_participants_with_options(request, runtime)

    async def delete_chat_group_participants_async(
        self,
        request: cams_20200606_models.DeleteChatGroupParticipantsRequest,
    ) -> cams_20200606_models.DeleteChatGroupParticipantsResponse:
        """
        @summary DeleteChatGroupParticipants
        
        @param request: DeleteChatGroupParticipantsRequest
        @return: DeleteChatGroupParticipantsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_chat_group_participants_with_options_async(request, runtime)

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
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
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
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
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

    def delete_flow_version_with_options(
        self,
        tmp_req: cams_20200606_models.DeleteFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.DeleteFlowVersionResponse:
        """
        @summary Delete Flow Version
        
        @param tmp_req: DeleteFlowVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFlowVersionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.DeleteFlowVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.flow_version):
            query['FlowVersion'] = request.flow_version
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
            action='DeleteFlowVersion',
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
            cams_20200606_models.DeleteFlowVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_version_with_options_async(
        self,
        tmp_req: cams_20200606_models.DeleteFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.DeleteFlowVersionResponse:
        """
        @summary Delete Flow Version
        
        @param tmp_req: DeleteFlowVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFlowVersionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.DeleteFlowVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.flow_version):
            query['FlowVersion'] = request.flow_version
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
            action='DeleteFlowVersion',
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
            cams_20200606_models.DeleteFlowVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow_version(
        self,
        request: cams_20200606_models.DeleteFlowVersionRequest,
    ) -> cams_20200606_models.DeleteFlowVersionResponse:
        """
        @summary Delete Flow Version
        
        @param request: DeleteFlowVersionRequest
        @return: DeleteFlowVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_version_with_options(request, runtime)

    async def delete_flow_version_async(
        self,
        request: cams_20200606_models.DeleteFlowVersionRequest,
    ) -> cams_20200606_models.DeleteFlowVersionResponse:
        """
        @summary Delete Flow Version
        
        @param request: DeleteFlowVersionRequest
        @return: DeleteFlowVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_version_with_options_async(request, runtime)

    def delete_phone_message_qrdl_with_options(
        self,
        request: cams_20200606_models.DeletePhoneMessageQrdlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.DeletePhoneMessageQrdlResponse:
        """
        @summary Deletes a quick-response (QR) code that contains a message.
        
        @param request: DeletePhoneMessageQrdlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePhoneMessageQrdlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.qrdl_code):
            query['QrdlCode'] = request.qrdl_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
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
        @summary Deletes a quick-response (QR) code that contains a message.
        
        @param request: DeletePhoneMessageQrdlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePhoneMessageQrdlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.qrdl_code):
            query['QrdlCode'] = request.qrdl_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
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
        @summary Deletes a quick-response (QR) code that contains a message.
        
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
        @summary Deletes a quick-response (QR) code that contains a message.
        
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
        @summary Deprecates a Flow.
        
        @param request: DeprecateFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeprecateFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
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
        @summary Deprecates a Flow.
        
        @param request: DeprecateFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeprecateFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
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
        @summary Deprecates a Flow.
        
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
        @summary Deprecates a Flow.
        
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

    def flow_bind_phone_with_options(
        self,
        tmp_req: cams_20200606_models.FlowBindPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.FlowBindPhoneResponse:
        """
        @summary Bind phone numbers to flow
        
        @param tmp_req: FlowBindPhoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FlowBindPhoneResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.FlowBindPhoneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phone_numbers):
            request.phone_numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phone_numbers, 'PhoneNumbers', 'json')
        query = {}
        if not UtilClient.is_unset(request.channel_code):
            query['ChannelCode'] = request.channel_code
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_numbers_shrink):
            query['PhoneNumbers'] = request.phone_numbers_shrink
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
            action='FlowBindPhone',
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
            cams_20200606_models.FlowBindPhoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def flow_bind_phone_with_options_async(
        self,
        tmp_req: cams_20200606_models.FlowBindPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.FlowBindPhoneResponse:
        """
        @summary Bind phone numbers to flow
        
        @param tmp_req: FlowBindPhoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FlowBindPhoneResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.FlowBindPhoneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phone_numbers):
            request.phone_numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phone_numbers, 'PhoneNumbers', 'json')
        query = {}
        if not UtilClient.is_unset(request.channel_code):
            query['ChannelCode'] = request.channel_code
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_numbers_shrink):
            query['PhoneNumbers'] = request.phone_numbers_shrink
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
            action='FlowBindPhone',
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
            cams_20200606_models.FlowBindPhoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flow_bind_phone(
        self,
        request: cams_20200606_models.FlowBindPhoneRequest,
    ) -> cams_20200606_models.FlowBindPhoneResponse:
        """
        @summary Bind phone numbers to flow
        
        @param request: FlowBindPhoneRequest
        @return: FlowBindPhoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.flow_bind_phone_with_options(request, runtime)

    async def flow_bind_phone_async(
        self,
        request: cams_20200606_models.FlowBindPhoneRequest,
    ) -> cams_20200606_models.FlowBindPhoneResponse:
        """
        @summary Bind phone numbers to flow
        
        @param request: FlowBindPhoneRequest
        @return: FlowBindPhoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.flow_bind_phone_with_options_async(request, runtime)

    def flow_rebind_phone_with_options(
        self,
        tmp_req: cams_20200606_models.FlowRebindPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.FlowRebindPhoneResponse:
        """
        @summary Rebind phone number for flow
        
        @param tmp_req: FlowRebindPhoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FlowRebindPhoneResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.FlowRebindPhoneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phone_numbers):
            request.phone_numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phone_numbers, 'PhoneNumbers', 'json')
        query = {}
        if not UtilClient.is_unset(request.channel_code):
            query['ChannelCode'] = request.channel_code
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_numbers_shrink):
            query['PhoneNumbers'] = request.phone_numbers_shrink
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
            action='FlowRebindPhone',
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
            cams_20200606_models.FlowRebindPhoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def flow_rebind_phone_with_options_async(
        self,
        tmp_req: cams_20200606_models.FlowRebindPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.FlowRebindPhoneResponse:
        """
        @summary Rebind phone number for flow
        
        @param tmp_req: FlowRebindPhoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FlowRebindPhoneResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.FlowRebindPhoneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phone_numbers):
            request.phone_numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phone_numbers, 'PhoneNumbers', 'json')
        query = {}
        if not UtilClient.is_unset(request.channel_code):
            query['ChannelCode'] = request.channel_code
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_numbers_shrink):
            query['PhoneNumbers'] = request.phone_numbers_shrink
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
            action='FlowRebindPhone',
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
            cams_20200606_models.FlowRebindPhoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flow_rebind_phone(
        self,
        request: cams_20200606_models.FlowRebindPhoneRequest,
    ) -> cams_20200606_models.FlowRebindPhoneResponse:
        """
        @summary Rebind phone number for flow
        
        @param request: FlowRebindPhoneRequest
        @return: FlowRebindPhoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.flow_rebind_phone_with_options(request, runtime)

    async def flow_rebind_phone_async(
        self,
        request: cams_20200606_models.FlowRebindPhoneRequest,
    ) -> cams_20200606_models.FlowRebindPhoneResponse:
        """
        @summary Rebind phone number for flow
        
        @param request: FlowRebindPhoneRequest
        @return: FlowRebindPhoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.flow_rebind_phone_with_options_async(request, runtime)

    def flow_unbind_phone_with_options(
        self,
        tmp_req: cams_20200606_models.FlowUnbindPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.FlowUnbindPhoneResponse:
        """
        @summary Unbind phone number from flow
        
        @param tmp_req: FlowUnbindPhoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FlowUnbindPhoneResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.FlowUnbindPhoneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phone_numbers):
            request.phone_numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phone_numbers, 'PhoneNumbers', 'json')
        query = {}
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_numbers_shrink):
            query['PhoneNumbers'] = request.phone_numbers_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlowUnbindPhone',
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
            cams_20200606_models.FlowUnbindPhoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def flow_unbind_phone_with_options_async(
        self,
        tmp_req: cams_20200606_models.FlowUnbindPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.FlowUnbindPhoneResponse:
        """
        @summary Unbind phone number from flow
        
        @param tmp_req: FlowUnbindPhoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FlowUnbindPhoneResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.FlowUnbindPhoneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phone_numbers):
            request.phone_numbers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phone_numbers, 'PhoneNumbers', 'json')
        query = {}
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_numbers_shrink):
            query['PhoneNumbers'] = request.phone_numbers_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlowUnbindPhone',
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
            cams_20200606_models.FlowUnbindPhoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flow_unbind_phone(
        self,
        request: cams_20200606_models.FlowUnbindPhoneRequest,
    ) -> cams_20200606_models.FlowUnbindPhoneResponse:
        """
        @summary Unbind phone number from flow
        
        @param request: FlowUnbindPhoneRequest
        @return: FlowUnbindPhoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.flow_unbind_phone_with_options(request, runtime)

    async def flow_unbind_phone_async(
        self,
        request: cams_20200606_models.FlowUnbindPhoneRequest,
    ) -> cams_20200606_models.FlowUnbindPhoneResponse:
        """
        @summary Unbind phone number from flow
        
        @param request: FlowUnbindPhoneRequest
        @return: FlowUnbindPhoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.flow_unbind_phone_with_options_async(request, runtime)

    def get_chat_flow_metric_with_options(
        self,
        tmp_req: cams_20200606_models.GetChatFlowMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetChatFlowMetricResponse:
        """
        @summary Get ChatFlow Runtime Data
        
        @param tmp_req: GetChatFlowMetricRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatFlowMetricResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.GetChatFlowMetricShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        if not UtilClient.is_unset(tmp_req.metric_param):
            request.metric_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.metric_param, 'MetricParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.metric_param_shrink):
            query['MetricParam'] = request.metric_param_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChatFlowMetric',
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
            cams_20200606_models.GetChatFlowMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chat_flow_metric_with_options_async(
        self,
        tmp_req: cams_20200606_models.GetChatFlowMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetChatFlowMetricResponse:
        """
        @summary Get ChatFlow Runtime Data
        
        @param tmp_req: GetChatFlowMetricRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatFlowMetricResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.GetChatFlowMetricShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        if not UtilClient.is_unset(tmp_req.metric_param):
            request.metric_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.metric_param, 'MetricParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.metric_param_shrink):
            query['MetricParam'] = request.metric_param_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChatFlowMetric',
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
            cams_20200606_models.GetChatFlowMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chat_flow_metric(
        self,
        request: cams_20200606_models.GetChatFlowMetricRequest,
    ) -> cams_20200606_models.GetChatFlowMetricResponse:
        """
        @summary Get ChatFlow Runtime Data
        
        @param request: GetChatFlowMetricRequest
        @return: GetChatFlowMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_chat_flow_metric_with_options(request, runtime)

    async def get_chat_flow_metric_async(
        self,
        request: cams_20200606_models.GetChatFlowMetricRequest,
    ) -> cams_20200606_models.GetChatFlowMetricResponse:
        """
        @summary Get ChatFlow Runtime Data
        
        @param request: GetChatFlowMetricRequest
        @return: GetChatFlowMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_chat_flow_metric_with_options_async(request, runtime)

    def get_chat_flow_template_with_options(
        self,
        request: cams_20200606_models.GetChatFlowTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetChatFlowTemplateResponse:
        """
        @summary Query chatFlow template
        
        @param request: GetChatFlowTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatFlowTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
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
            action='GetChatFlowTemplate',
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
            cams_20200606_models.GetChatFlowTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chat_flow_template_with_options_async(
        self,
        request: cams_20200606_models.GetChatFlowTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetChatFlowTemplateResponse:
        """
        @summary Query chatFlow template
        
        @param request: GetChatFlowTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatFlowTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
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
            action='GetChatFlowTemplate',
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
            cams_20200606_models.GetChatFlowTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chat_flow_template(
        self,
        request: cams_20200606_models.GetChatFlowTemplateRequest,
    ) -> cams_20200606_models.GetChatFlowTemplateResponse:
        """
        @summary Query chatFlow template
        
        @param request: GetChatFlowTemplateRequest
        @return: GetChatFlowTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_chat_flow_template_with_options(request, runtime)

    async def get_chat_flow_template_async(
        self,
        request: cams_20200606_models.GetChatFlowTemplateRequest,
    ) -> cams_20200606_models.GetChatFlowTemplateResponse:
        """
        @summary Query chatFlow template
        
        @param request: GetChatFlowTemplateRequest
        @return: GetChatFlowTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_chat_flow_template_with_options_async(request, runtime)

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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
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

    def get_conversational_automation_with_options(
        self,
        request: cams_20200606_models.GetConversationalAutomationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetConversationalAutomationResponse:
        """
        @summary Configures welcoming messages, opening remarks, and commands.
        
        @description ### [](#qps-)QPS limit
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        This operation will directly obtain data from Facebook, which sets an upper limit on the total number of calls for operations. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetConversationalAutomationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConversationalAutomationResponse
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
            action='GetConversationalAutomation',
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
            cams_20200606_models.GetConversationalAutomationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_conversational_automation_with_options_async(
        self,
        request: cams_20200606_models.GetConversationalAutomationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetConversationalAutomationResponse:
        """
        @summary Configures welcoming messages, opening remarks, and commands.
        
        @description ### [](#qps-)QPS limit
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        This operation will directly obtain data from Facebook, which sets an upper limit on the total number of calls for operations. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetConversationalAutomationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConversationalAutomationResponse
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
            action='GetConversationalAutomation',
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
            cams_20200606_models.GetConversationalAutomationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_conversational_automation(
        self,
        request: cams_20200606_models.GetConversationalAutomationRequest,
    ) -> cams_20200606_models.GetConversationalAutomationResponse:
        """
        @summary Configures welcoming messages, opening remarks, and commands.
        
        @description ### [](#qps-)QPS limit
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        This operation will directly obtain data from Facebook, which sets an upper limit on the total number of calls for operations. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetConversationalAutomationRequest
        @return: GetConversationalAutomationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_conversational_automation_with_options(request, runtime)

    async def get_conversational_automation_async(
        self,
        request: cams_20200606_models.GetConversationalAutomationRequest,
    ) -> cams_20200606_models.GetConversationalAutomationResponse:
        """
        @summary Configures welcoming messages, opening remarks, and commands.
        
        @description ### [](#qps-)QPS limit
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        This operation will directly obtain data from Facebook, which sets an upper limit on the total number of calls for operations. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetConversationalAutomationRequest
        @return: GetConversationalAutomationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_conversational_automation_with_options_async(request, runtime)

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
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
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
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
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
        @summary Queries the JSON content of a Flow.
        
        @param request: GetFlowJSONAssestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFlowJSONAssestResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
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
        @summary Queries the JSON content of a Flow.
        
        @param request: GetFlowJSONAssestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFlowJSONAssestResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
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
        @summary Queries the JSON content of a Flow.
        
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
        @summary Queries the JSON content of a Flow.
        
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
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
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
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
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
        @summary Obtain the verification code for the migration number.
        
        @description The single user QPS limit for this interface is 10 times per second. Exceeding the limit may result in restricted API calls, which may affect your business. Please make reasonable calls.
        
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
        @summary Obtain the verification code for the migration number.
        
        @description The single user QPS limit for this interface is 10 times per second. Exceeding the limit may result in restricted API calls, which may affect your business. Please make reasonable calls.
        
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
        @summary Obtain the verification code for the migration number.
        
        @description The single user QPS limit for this interface is 10 times per second. Exceeding the limit may result in restricted API calls, which may affect your business. Please make reasonable calls.
        
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
        @summary Obtain the verification code for the migration number.
        
        @description The single user QPS limit for this interface is 10 times per second. Exceeding the limit may result in restricted API calls, which may affect your business. Please make reasonable calls.
        
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
        @summary Obtains permissions based on the authorization code obtained from embedded signup.
        
        @param tmp_req: GetPermissionByCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPermissionByCodeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.GetPermissionByCodeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.permissions):
            request.permissions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.permissions, 'Permissions', 'json')
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.permissions_shrink):
            query['Permissions'] = request.permissions_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
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
        @summary Obtains permissions based on the authorization code obtained from embedded signup.
        
        @param tmp_req: GetPermissionByCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPermissionByCodeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.GetPermissionByCodeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.permissions):
            request.permissions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.permissions, 'Permissions', 'json')
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.permissions_shrink):
            query['Permissions'] = request.permissions_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
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
        @summary Obtains permissions based on the authorization code obtained from embedded signup.
        
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
        @summary Obtains permissions based on the authorization code obtained from embedded signup.
        
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
        @summary Queries the encryption public key of a phone number.
        
        @param request: GetPhoneEncryptionPublicKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPhoneEncryptionPublicKeyResponse
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
        @summary Queries the encryption public key of a phone number.
        
        @param request: GetPhoneEncryptionPublicKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPhoneEncryptionPublicKeyResponse
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
        @summary Queries the encryption public key of a phone number.
        
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
        @summary Queries the encryption public key of a phone number.
        
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

    def get_whatsapp_health_status_with_options(
        self,
        request: cams_20200606_models.GetWhatsappHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetWhatsappHealthStatusResponse:
        """
        @summary Queries the messaging health status of different types of nodes.
        
        @description ### [](#qps-)QPS limit
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        This operation will directly obtain data from Facebook, which sets an upper limit on the total number of calls for operations. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetWhatsappHealthStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWhatsappHealthStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWhatsappHealthStatus',
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
            cams_20200606_models.GetWhatsappHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_whatsapp_health_status_with_options_async(
        self,
        request: cams_20200606_models.GetWhatsappHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.GetWhatsappHealthStatusResponse:
        """
        @summary Queries the messaging health status of different types of nodes.
        
        @description ### [](#qps-)QPS limit
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        This operation will directly obtain data from Facebook, which sets an upper limit on the total number of calls for operations. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetWhatsappHealthStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWhatsappHealthStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWhatsappHealthStatus',
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
            cams_20200606_models.GetWhatsappHealthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_whatsapp_health_status(
        self,
        request: cams_20200606_models.GetWhatsappHealthStatusRequest,
    ) -> cams_20200606_models.GetWhatsappHealthStatusResponse:
        """
        @summary Queries the messaging health status of different types of nodes.
        
        @description ### [](#qps-)QPS limit
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        This operation will directly obtain data from Facebook, which sets an upper limit on the total number of calls for operations. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetWhatsappHealthStatusRequest
        @return: GetWhatsappHealthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_whatsapp_health_status_with_options(request, runtime)

    async def get_whatsapp_health_status_async(
        self,
        request: cams_20200606_models.GetWhatsappHealthStatusRequest,
    ) -> cams_20200606_models.GetWhatsappHealthStatusResponse:
        """
        @summary Queries the messaging health status of different types of nodes.
        
        @description ### [](#qps-)QPS limit
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        This operation will directly obtain data from Facebook, which sets an upper limit on the total number of calls for operations. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetWhatsappHealthStatusRequest
        @return: GetWhatsappHealthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_whatsapp_health_status_with_options_async(request, runtime)

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
        query = {}
        if not UtilClient.is_unset(request.intl_version):
            query['IntlVersion'] = request.intl_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.permissions):
            query['Permissions'] = request.permissions
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
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
        query = {}
        if not UtilClient.is_unset(request.intl_version):
            query['IntlVersion'] = request.intl_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.permissions):
            query['Permissions'] = request.permissions
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
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

    def list_binding_relations_for_flow_version_with_options(
        self,
        request: cams_20200606_models.ListBindingRelationsForFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListBindingRelationsForFlowVersionResponse:
        """
        @summary Query Bound List Based on flowCode
        
        @description - You can call this interface to query the list of phone numbers or merchant account IDs bound to a process, or you can view the list in the [*Flow Editor**](https://chatapp.console.aliyun.com/ChatFlowBuilder) > **Settings** interface.
        - Before calling this interface, make sure that the process you created has already been bound to a phone number or merchant account ID.
        - If the process you created is not bound to a phone number or merchant account ID, you can manually bind a phone number or merchant account ID in the [*Flow Editor**](https://chatapp.console.aliyun.com/ChatFlowBuilder) > **Settings** interface, or bind it through the [FlowBindPhone](https://help.aliyun.com/document_detail/2937190.html) interface.
        
        @param request: ListBindingRelationsForFlowVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBindingRelationsForFlowVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
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
            action='ListBindingRelationsForFlowVersion',
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
            cams_20200606_models.ListBindingRelationsForFlowVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_binding_relations_for_flow_version_with_options_async(
        self,
        request: cams_20200606_models.ListBindingRelationsForFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListBindingRelationsForFlowVersionResponse:
        """
        @summary Query Bound List Based on flowCode
        
        @description - You can call this interface to query the list of phone numbers or merchant account IDs bound to a process, or you can view the list in the [*Flow Editor**](https://chatapp.console.aliyun.com/ChatFlowBuilder) > **Settings** interface.
        - Before calling this interface, make sure that the process you created has already been bound to a phone number or merchant account ID.
        - If the process you created is not bound to a phone number or merchant account ID, you can manually bind a phone number or merchant account ID in the [*Flow Editor**](https://chatapp.console.aliyun.com/ChatFlowBuilder) > **Settings** interface, or bind it through the [FlowBindPhone](https://help.aliyun.com/document_detail/2937190.html) interface.
        
        @param request: ListBindingRelationsForFlowVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBindingRelationsForFlowVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
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
            action='ListBindingRelationsForFlowVersion',
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
            cams_20200606_models.ListBindingRelationsForFlowVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_binding_relations_for_flow_version(
        self,
        request: cams_20200606_models.ListBindingRelationsForFlowVersionRequest,
    ) -> cams_20200606_models.ListBindingRelationsForFlowVersionResponse:
        """
        @summary Query Bound List Based on flowCode
        
        @description - You can call this interface to query the list of phone numbers or merchant account IDs bound to a process, or you can view the list in the [*Flow Editor**](https://chatapp.console.aliyun.com/ChatFlowBuilder) > **Settings** interface.
        - Before calling this interface, make sure that the process you created has already been bound to a phone number or merchant account ID.
        - If the process you created is not bound to a phone number or merchant account ID, you can manually bind a phone number or merchant account ID in the [*Flow Editor**](https://chatapp.console.aliyun.com/ChatFlowBuilder) > **Settings** interface, or bind it through the [FlowBindPhone](https://help.aliyun.com/document_detail/2937190.html) interface.
        
        @param request: ListBindingRelationsForFlowVersionRequest
        @return: ListBindingRelationsForFlowVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_binding_relations_for_flow_version_with_options(request, runtime)

    async def list_binding_relations_for_flow_version_async(
        self,
        request: cams_20200606_models.ListBindingRelationsForFlowVersionRequest,
    ) -> cams_20200606_models.ListBindingRelationsForFlowVersionResponse:
        """
        @summary Query Bound List Based on flowCode
        
        @description - You can call this interface to query the list of phone numbers or merchant account IDs bound to a process, or you can view the list in the [*Flow Editor**](https://chatapp.console.aliyun.com/ChatFlowBuilder) > **Settings** interface.
        - Before calling this interface, make sure that the process you created has already been bound to a phone number or merchant account ID.
        - If the process you created is not bound to a phone number or merchant account ID, you can manually bind a phone number or merchant account ID in the [*Flow Editor**](https://chatapp.console.aliyun.com/ChatFlowBuilder) > **Settings** interface, or bind it through the [FlowBindPhone](https://help.aliyun.com/document_detail/2937190.html) interface.
        
        @param request: ListBindingRelationsForFlowVersionRequest
        @return: ListBindingRelationsForFlowVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_binding_relations_for_flow_version_with_options_async(request, runtime)

    def list_chat_flow_with_options(
        self,
        tmp_req: cams_20200606_models.ListChatFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListChatFlowResponse:
        """
        @summary List Flows
        
        @param tmp_req: ListChatFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChatFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ListChatFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_trigger_type):
            query['FlowTriggerType'] = request.flow_trigger_type
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.return_with_online_version):
            query['ReturnWithOnlineVersion'] = request.return_with_online_version
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChatFlow',
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
            cams_20200606_models.ListChatFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chat_flow_with_options_async(
        self,
        tmp_req: cams_20200606_models.ListChatFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListChatFlowResponse:
        """
        @summary List Flows
        
        @param tmp_req: ListChatFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChatFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ListChatFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_trigger_type):
            query['FlowTriggerType'] = request.flow_trigger_type
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.return_with_online_version):
            query['ReturnWithOnlineVersion'] = request.return_with_online_version
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChatFlow',
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
            cams_20200606_models.ListChatFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chat_flow(
        self,
        request: cams_20200606_models.ListChatFlowRequest,
    ) -> cams_20200606_models.ListChatFlowResponse:
        """
        @summary List Flows
        
        @param request: ListChatFlowRequest
        @return: ListChatFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_chat_flow_with_options(request, runtime)

    async def list_chat_flow_async(
        self,
        request: cams_20200606_models.ListChatFlowRequest,
    ) -> cams_20200606_models.ListChatFlowResponse:
        """
        @summary List Flows
        
        @param request: ListChatFlowRequest
        @return: ListChatFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_chat_flow_with_options_async(request, runtime)

    def list_chat_flow_template_with_options(
        self,
        request: cams_20200606_models.ListChatFlowTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListChatFlowTemplateResponse:
        """
        @summary ChatFlow Template List
        
        @param request: ListChatFlowTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChatFlowTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChatFlowTemplate',
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
            cams_20200606_models.ListChatFlowTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chat_flow_template_with_options_async(
        self,
        request: cams_20200606_models.ListChatFlowTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListChatFlowTemplateResponse:
        """
        @summary ChatFlow Template List
        
        @param request: ListChatFlowTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChatFlowTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChatFlowTemplate',
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
            cams_20200606_models.ListChatFlowTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chat_flow_template(
        self,
        request: cams_20200606_models.ListChatFlowTemplateRequest,
    ) -> cams_20200606_models.ListChatFlowTemplateResponse:
        """
        @summary ChatFlow Template List
        
        @param request: ListChatFlowTemplateRequest
        @return: ListChatFlowTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_chat_flow_template_with_options(request, runtime)

    async def list_chat_flow_template_async(
        self,
        request: cams_20200606_models.ListChatFlowTemplateRequest,
    ) -> cams_20200606_models.ListChatFlowTemplateResponse:
        """
        @summary ChatFlow Template List
        
        @param request: ListChatFlowTemplateRequest
        @return: ListChatFlowTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_chat_flow_template_with_options_async(request, runtime)

    def list_chat_group_with_options(
        self,
        tmp_req: cams_20200606_models.ListChatGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListChatGroupResponse:
        """
        @summary ListChatGroup
        
        @param tmp_req: ListChatGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChatGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ListChatGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not UtilClient.is_unset(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.group_status):
            query['GroupStatus'] = request.group_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChatGroup',
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
            cams_20200606_models.ListChatGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chat_group_with_options_async(
        self,
        tmp_req: cams_20200606_models.ListChatGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListChatGroupResponse:
        """
        @summary ListChatGroup
        
        @param tmp_req: ListChatGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChatGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ListChatGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not UtilClient.is_unset(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.group_status):
            query['GroupStatus'] = request.group_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChatGroup',
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
            cams_20200606_models.ListChatGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chat_group(
        self,
        request: cams_20200606_models.ListChatGroupRequest,
    ) -> cams_20200606_models.ListChatGroupResponse:
        """
        @summary ListChatGroup
        
        @param request: ListChatGroupRequest
        @return: ListChatGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_chat_group_with_options(request, runtime)

    async def list_chat_group_async(
        self,
        request: cams_20200606_models.ListChatGroupRequest,
    ) -> cams_20200606_models.ListChatGroupResponse:
        """
        @summary ListChatGroup
        
        @param request: ListChatGroupRequest
        @return: ListChatGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_chat_group_with_options_async(request, runtime)

    def list_chat_group_participants_with_options(
        self,
        tmp_req: cams_20200606_models.ListChatGroupParticipantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListChatGroupParticipantsResponse:
        """
        @summary ListChatGroupParticipants
        
        @param tmp_req: ListChatGroupParticipantsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChatGroupParticipantsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ListChatGroupParticipantsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not UtilClient.is_unset(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChatGroupParticipants',
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
            cams_20200606_models.ListChatGroupParticipantsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chat_group_participants_with_options_async(
        self,
        tmp_req: cams_20200606_models.ListChatGroupParticipantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListChatGroupParticipantsResponse:
        """
        @summary ListChatGroupParticipants
        
        @param tmp_req: ListChatGroupParticipantsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChatGroupParticipantsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ListChatGroupParticipantsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not UtilClient.is_unset(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChatGroupParticipants',
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
            cams_20200606_models.ListChatGroupParticipantsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chat_group_participants(
        self,
        request: cams_20200606_models.ListChatGroupParticipantsRequest,
    ) -> cams_20200606_models.ListChatGroupParticipantsResponse:
        """
        @summary ListChatGroupParticipants
        
        @param request: ListChatGroupParticipantsRequest
        @return: ListChatGroupParticipantsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_chat_group_participants_with_options(request, runtime)

    async def list_chat_group_participants_async(
        self,
        request: cams_20200606_models.ListChatGroupParticipantsRequest,
    ) -> cams_20200606_models.ListChatGroupParticipantsResponse:
        """
        @summary ListChatGroupParticipants
        
        @param request: ListChatGroupParticipantsRequest
        @return: ListChatGroupParticipantsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_chat_group_participants_with_options_async(request, runtime)

    def list_chatapp_message_with_options(
        self,
        tmp_req: cams_20200606_models.ListChatappMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListChatappMessageResponse:
        """
        @summary 查询消息列表
        
        @param tmp_req: ListChatappMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChatappMessageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ListChatappMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not UtilClient.is_unset(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.client_accept_status):
            query['ClientAcceptStatus'] = request.client_accept_status
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_action):
            query['EventAction'] = request.event_action
        if not UtilClient.is_unset(request.group_message_id):
            query['GroupMessageId'] = request.group_message_id
        if not UtilClient.is_unset(request.message_status):
            query['MessageStatus'] = request.message_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.user_number):
            query['UserNumber'] = request.user_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChatappMessage',
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
            cams_20200606_models.ListChatappMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chatapp_message_with_options_async(
        self,
        tmp_req: cams_20200606_models.ListChatappMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListChatappMessageResponse:
        """
        @summary 查询消息列表
        
        @param tmp_req: ListChatappMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChatappMessageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ListChatappMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not UtilClient.is_unset(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.client_accept_status):
            query['ClientAcceptStatus'] = request.client_accept_status
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_action):
            query['EventAction'] = request.event_action
        if not UtilClient.is_unset(request.group_message_id):
            query['GroupMessageId'] = request.group_message_id
        if not UtilClient.is_unset(request.message_status):
            query['MessageStatus'] = request.message_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.user_number):
            query['UserNumber'] = request.user_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChatappMessage',
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
            cams_20200606_models.ListChatappMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chatapp_message(
        self,
        request: cams_20200606_models.ListChatappMessageRequest,
    ) -> cams_20200606_models.ListChatappMessageResponse:
        """
        @summary 查询消息列表
        
        @param request: ListChatappMessageRequest
        @return: ListChatappMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_chatapp_message_with_options(request, runtime)

    async def list_chatapp_message_async(
        self,
        request: cams_20200606_models.ListChatappMessageRequest,
    ) -> cams_20200606_models.ListChatappMessageResponse:
        """
        @summary 查询消息列表
        
        @param request: ListChatappMessageRequest
        @return: ListChatappMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_chatapp_message_with_options_async(request, runtime)

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
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
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
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
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
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_name):
            query['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
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
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_name):
            query['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
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

    def list_flow_node_prototype_v2with_options(
        self,
        request: cams_20200606_models.ListFlowNodePrototypeV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListFlowNodePrototypeV2Response:
        """
        @summary ListFlowNodePrototypeV2
        
        @param request: ListFlowNodePrototypeV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowNodePrototypeV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.group_code):
            query['GroupCode'] = request.group_code
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowNodePrototypeV2',
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
            cams_20200606_models.ListFlowNodePrototypeV2Response(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_node_prototype_v2with_options_async(
        self,
        request: cams_20200606_models.ListFlowNodePrototypeV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListFlowNodePrototypeV2Response:
        """
        @summary ListFlowNodePrototypeV2
        
        @param request: ListFlowNodePrototypeV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowNodePrototypeV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.group_code):
            query['GroupCode'] = request.group_code
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowNodePrototypeV2',
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
            cams_20200606_models.ListFlowNodePrototypeV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow_node_prototype_v2(
        self,
        request: cams_20200606_models.ListFlowNodePrototypeV2Request,
    ) -> cams_20200606_models.ListFlowNodePrototypeV2Response:
        """
        @summary ListFlowNodePrototypeV2
        
        @param request: ListFlowNodePrototypeV2Request
        @return: ListFlowNodePrototypeV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.list_flow_node_prototype_v2with_options(request, runtime)

    async def list_flow_node_prototype_v2_async(
        self,
        request: cams_20200606_models.ListFlowNodePrototypeV2Request,
    ) -> cams_20200606_models.ListFlowNodePrototypeV2Response:
        """
        @summary ListFlowNodePrototypeV2
        
        @param request: ListFlowNodePrototypeV2Request
        @return: ListFlowNodePrototypeV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_node_prototype_v2with_options_async(request, runtime)

    def list_flow_version_with_options(
        self,
        tmp_req: cams_20200606_models.ListFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListFlowVersionResponse:
        """
        @summary List Flow Versions
        
        @param tmp_req: ListFlowVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowVersionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ListFlowVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowVersion',
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
            cams_20200606_models.ListFlowVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_version_with_options_async(
        self,
        tmp_req: cams_20200606_models.ListFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListFlowVersionResponse:
        """
        @summary List Flow Versions
        
        @param tmp_req: ListFlowVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFlowVersionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ListFlowVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowVersion',
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
            cams_20200606_models.ListFlowVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow_version(
        self,
        request: cams_20200606_models.ListFlowVersionRequest,
    ) -> cams_20200606_models.ListFlowVersionResponse:
        """
        @summary List Flow Versions
        
        @param request: ListFlowVersionRequest
        @return: ListFlowVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_flow_version_with_options(request, runtime)

    async def list_flow_version_async(
        self,
        request: cams_20200606_models.ListFlowVersionRequest,
    ) -> cams_20200606_models.ListFlowVersionResponse:
        """
        @summary List Flow Versions
        
        @param request: ListFlowVersionRequest
        @return: ListFlowVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_version_with_options_async(request, runtime)

    def list_phone_message_qrdl_with_options(
        self,
        request: cams_20200606_models.ListPhoneMessageQrdlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ListPhoneMessageQrdlResponse:
        """
        @summary Queries the information about a list of quick-response (QR) codes that contain messages.
        
        @param request: ListPhoneMessageQrdlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPhoneMessageQrdlResponse
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
        @summary Queries the information about a list of quick-response (QR) codes that contain messages.
        
        @param request: ListPhoneMessageQrdlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPhoneMessageQrdlResponse
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
        @summary Queries the information about a list of quick-response (QR) codes that contain messages.
        
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
        @summary Queries the information about a list of quick-response (QR) codes that contain messages.
        
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
        if not UtilClient.is_unset(request.category_change_paused):
            body['CategoryChangePaused'] = request.category_change_paused
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
        if not UtilClient.is_unset(request.category_change_paused):
            body['CategoryChangePaused'] = request.category_change_paused
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

    def modify_chatapp_template_properties_with_options(
        self,
        request: cams_20200606_models.ModifyChatappTemplatePropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ModifyChatappTemplatePropertiesResponse:
        """
        @summary 修改模板上的一些属性
        
        @param request: ModifyChatappTemplatePropertiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyChatappTemplatePropertiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_send):
            query['AllowSend'] = request.allow_send
        if not UtilClient.is_unset(request.category_change_paused):
            query['CategoryChangePaused'] = request.category_change_paused
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
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
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyChatappTemplateProperties',
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
            cams_20200606_models.ModifyChatappTemplatePropertiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_chatapp_template_properties_with_options_async(
        self,
        request: cams_20200606_models.ModifyChatappTemplatePropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ModifyChatappTemplatePropertiesResponse:
        """
        @summary 修改模板上的一些属性
        
        @param request: ModifyChatappTemplatePropertiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyChatappTemplatePropertiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_send):
            query['AllowSend'] = request.allow_send
        if not UtilClient.is_unset(request.category_change_paused):
            query['CategoryChangePaused'] = request.category_change_paused
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
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
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyChatappTemplateProperties',
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
            cams_20200606_models.ModifyChatappTemplatePropertiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_chatapp_template_properties(
        self,
        request: cams_20200606_models.ModifyChatappTemplatePropertiesRequest,
    ) -> cams_20200606_models.ModifyChatappTemplatePropertiesResponse:
        """
        @summary 修改模板上的一些属性
        
        @param request: ModifyChatappTemplatePropertiesRequest
        @return: ModifyChatappTemplatePropertiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_chatapp_template_properties_with_options(request, runtime)

    async def modify_chatapp_template_properties_async(
        self,
        request: cams_20200606_models.ModifyChatappTemplatePropertiesRequest,
    ) -> cams_20200606_models.ModifyChatappTemplatePropertiesResponse:
        """
        @summary 修改模板上的一些属性
        
        @param request: ModifyChatappTemplatePropertiesRequest
        @return: ModifyChatappTemplatePropertiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_chatapp_template_properties_with_options_async(request, runtime)

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
        query = {}
        if not UtilClient.is_unset(request.categories_shrink):
            query['Categories'] = request.categories_shrink
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
        if not UtilClient.is_unset(request.flow_name):
            query['FlowName'] = request.flow_name
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
        query = {}
        if not UtilClient.is_unset(request.categories_shrink):
            query['Categories'] = request.categories_shrink
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
        if not UtilClient.is_unset(request.flow_name):
            query['FlowName'] = request.flow_name
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

    def offline_flow_version_with_options(
        self,
        tmp_req: cams_20200606_models.OfflineFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.OfflineFlowVersionResponse:
        """
        @summary Offline Flow Version
        
        @param tmp_req: OfflineFlowVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OfflineFlowVersionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.OfflineFlowVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OfflineFlowVersion',
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
            cams_20200606_models.OfflineFlowVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_flow_version_with_options_async(
        self,
        tmp_req: cams_20200606_models.OfflineFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.OfflineFlowVersionResponse:
        """
        @summary Offline Flow Version
        
        @param tmp_req: OfflineFlowVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OfflineFlowVersionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.OfflineFlowVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OfflineFlowVersion',
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
            cams_20200606_models.OfflineFlowVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_flow_version(
        self,
        request: cams_20200606_models.OfflineFlowVersionRequest,
    ) -> cams_20200606_models.OfflineFlowVersionResponse:
        """
        @summary Offline Flow Version
        
        @param request: OfflineFlowVersionRequest
        @return: OfflineFlowVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.offline_flow_version_with_options(request, runtime)

    async def offline_flow_version_async(
        self,
        request: cams_20200606_models.OfflineFlowVersionRequest,
    ) -> cams_20200606_models.OfflineFlowVersionResponse:
        """
        @summary Offline Flow Version
        
        @param request: OfflineFlowVersionRequest
        @return: OfflineFlowVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.offline_flow_version_with_options_async(request, runtime)

    def online_flow_version_with_options(
        self,
        tmp_req: cams_20200606_models.OnlineFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.OnlineFlowVersionResponse:
        """
        @summary Online Flow Version
        
        @param tmp_req: OnlineFlowVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnlineFlowVersionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.OnlineFlowVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnlineFlowVersion',
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
            cams_20200606_models.OnlineFlowVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def online_flow_version_with_options_async(
        self,
        tmp_req: cams_20200606_models.OnlineFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.OnlineFlowVersionResponse:
        """
        @summary Online Flow Version
        
        @param tmp_req: OnlineFlowVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnlineFlowVersionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.OnlineFlowVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OnlineFlowVersion',
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
            cams_20200606_models.OnlineFlowVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def online_flow_version(
        self,
        request: cams_20200606_models.OnlineFlowVersionRequest,
    ) -> cams_20200606_models.OnlineFlowVersionResponse:
        """
        @summary Online Flow Version
        
        @param request: OnlineFlowVersionRequest
        @return: OnlineFlowVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.online_flow_version_with_options(request, runtime)

    async def online_flow_version_async(
        self,
        request: cams_20200606_models.OnlineFlowVersionRequest,
    ) -> cams_20200606_models.OnlineFlowVersionResponse:
        """
        @summary Online Flow Version
        
        @param request: OnlineFlowVersionRequest
        @return: OnlineFlowVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.online_flow_version_with_options_async(request, runtime)

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
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
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
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
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

    def read_chat_flow_with_options(
        self,
        tmp_req: cams_20200606_models.ReadChatFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ReadChatFlowResponse:
        """
        @summary Retrieve Flow
        
        @param tmp_req: ReadChatFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadChatFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ReadChatFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
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
            action='ReadChatFlow',
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
            cams_20200606_models.ReadChatFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_chat_flow_with_options_async(
        self,
        tmp_req: cams_20200606_models.ReadChatFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ReadChatFlowResponse:
        """
        @summary Retrieve Flow
        
        @param tmp_req: ReadChatFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadChatFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ReadChatFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
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
            action='ReadChatFlow',
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
            cams_20200606_models.ReadChatFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_chat_flow(
        self,
        request: cams_20200606_models.ReadChatFlowRequest,
    ) -> cams_20200606_models.ReadChatFlowResponse:
        """
        @summary Retrieve Flow
        
        @param request: ReadChatFlowRequest
        @return: ReadChatFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.read_chat_flow_with_options(request, runtime)

    async def read_chat_flow_async(
        self,
        request: cams_20200606_models.ReadChatFlowRequest,
    ) -> cams_20200606_models.ReadChatFlowResponse:
        """
        @summary Retrieve Flow
        
        @param request: ReadChatFlowRequest
        @return: ReadChatFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.read_chat_flow_with_options_async(request, runtime)

    def read_chat_flow_log_setting_with_options(
        self,
        request: cams_20200606_models.ReadChatFlowLogSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ReadChatFlowLogSettingResponse:
        """
        @summary View chatFlow log settings
        
        @param request: ReadChatFlowLogSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadChatFlowLogSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
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
            action='ReadChatFlowLogSetting',
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
            cams_20200606_models.ReadChatFlowLogSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_chat_flow_log_setting_with_options_async(
        self,
        request: cams_20200606_models.ReadChatFlowLogSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ReadChatFlowLogSettingResponse:
        """
        @summary View chatFlow log settings
        
        @param request: ReadChatFlowLogSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadChatFlowLogSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
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
            action='ReadChatFlowLogSetting',
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
            cams_20200606_models.ReadChatFlowLogSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_chat_flow_log_setting(
        self,
        request: cams_20200606_models.ReadChatFlowLogSettingRequest,
    ) -> cams_20200606_models.ReadChatFlowLogSettingResponse:
        """
        @summary View chatFlow log settings
        
        @param request: ReadChatFlowLogSettingRequest
        @return: ReadChatFlowLogSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.read_chat_flow_log_setting_with_options(request, runtime)

    async def read_chat_flow_log_setting_async(
        self,
        request: cams_20200606_models.ReadChatFlowLogSettingRequest,
    ) -> cams_20200606_models.ReadChatFlowLogSettingResponse:
        """
        @summary View chatFlow log settings
        
        @param request: ReadChatFlowLogSettingRequest
        @return: ReadChatFlowLogSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.read_chat_flow_log_setting_with_options_async(request, runtime)

    def read_flow_version_with_options(
        self,
        tmp_req: cams_20200606_models.ReadFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ReadFlowVersionResponse:
        """
        @summary Get Flow Version
        
        @param tmp_req: ReadFlowVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadFlowVersionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ReadFlowVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReadFlowVersion',
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
            cams_20200606_models.ReadFlowVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_flow_version_with_options_async(
        self,
        tmp_req: cams_20200606_models.ReadFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.ReadFlowVersionResponse:
        """
        @summary Get Flow Version
        
        @param tmp_req: ReadFlowVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadFlowVersionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ReadFlowVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReadFlowVersion',
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
            cams_20200606_models.ReadFlowVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_flow_version(
        self,
        request: cams_20200606_models.ReadFlowVersionRequest,
    ) -> cams_20200606_models.ReadFlowVersionResponse:
        """
        @summary Get Flow Version
        
        @param request: ReadFlowVersionRequest
        @return: ReadFlowVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.read_flow_version_with_options(request, runtime)

    async def read_flow_version_async(
        self,
        request: cams_20200606_models.ReadFlowVersionRequest,
    ) -> cams_20200606_models.ReadFlowVersionResponse:
        """
        @summary Get Flow Version
        
        @param request: ReadFlowVersionRequest
        @return: ReadFlowVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.read_flow_version_with_options_async(request, runtime)

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
        query = {}
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.fall_back_content):
            query['FallBackContent'] = request.fall_back_content
        if not UtilClient.is_unset(request.fall_back_duration):
            query['FallBackDuration'] = request.fall_back_duration
        if not UtilClient.is_unset(request.fall_back_id):
            query['FallBackId'] = request.fall_back_id
        if not UtilClient.is_unset(request.fall_back_rule):
            query['FallBackRule'] = request.fall_back_rule
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sender_list_shrink):
            query['SenderList'] = request.sender_list_shrink
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
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
        query = {}
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.fall_back_content):
            query['FallBackContent'] = request.fall_back_content
        if not UtilClient.is_unset(request.fall_back_duration):
            query['FallBackDuration'] = request.fall_back_duration
        if not UtilClient.is_unset(request.fall_back_id):
            query['FallBackId'] = request.fall_back_id
        if not UtilClient.is_unset(request.fall_back_rule):
            query['FallBackRule'] = request.fall_back_rule
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sender_list_shrink):
            query['SenderList'] = request.sender_list_shrink
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
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
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.context_message_id):
            query['ContextMessageId'] = request.context_message_id
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.fall_back_content):
            query['FallBackContent'] = request.fall_back_content
        if not UtilClient.is_unset(request.fall_back_duration):
            query['FallBackDuration'] = request.fall_back_duration
        if not UtilClient.is_unset(request.fall_back_id):
            query['FallBackId'] = request.fall_back_id
        if not UtilClient.is_unset(request.fall_back_rule):
            query['FallBackRule'] = request.fall_back_rule
        if not UtilClient.is_unset(request.flow_action_shrink):
            query['FlowAction'] = request.flow_action_shrink
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.product_action_shrink):
            query['ProductAction'] = request.product_action_shrink
        if not UtilClient.is_unset(request.recipient_type):
            query['RecipientType'] = request.recipient_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_params_shrink):
            query['TemplateParams'] = request.template_params_shrink
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        if not UtilClient.is_unset(request.tracking_data):
            query['TrackingData'] = request.tracking_data
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
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
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.context_message_id):
            query['ContextMessageId'] = request.context_message_id
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.fall_back_content):
            query['FallBackContent'] = request.fall_back_content
        if not UtilClient.is_unset(request.fall_back_duration):
            query['FallBackDuration'] = request.fall_back_duration
        if not UtilClient.is_unset(request.fall_back_id):
            query['FallBackId'] = request.fall_back_id
        if not UtilClient.is_unset(request.fall_back_rule):
            query['FallBackRule'] = request.fall_back_rule
        if not UtilClient.is_unset(request.flow_action_shrink):
            query['FlowAction'] = request.flow_action_shrink
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not UtilClient.is_unset(request.product_action_shrink):
            query['ProductAction'] = request.product_action_shrink
        if not UtilClient.is_unset(request.recipient_type):
            query['RecipientType'] = request.recipient_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_params_shrink):
            query['TemplateParams'] = request.template_params_shrink
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        if not UtilClient.is_unset(request.tracking_data):
            query['TrackingData'] = request.tracking_data
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
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
        
        @description    You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        After you call the [GetChatappUploadAuthorization](~~GetChatappUploadAuthorization~~) operation to obtain the authentication information for uploading the file to Object Storage Service (OSS), you can use the authentication information to upload the file to the OSS server. To upload the file, you can call the SDK provided by OSS. When you upload the file, set the value of the key to the value of `Dir + "/" + file name`, such as C200293990209/isvTerms.pdf. The value of Dir is obtained from the [GetChatappUploadAuthorization](~~GetChatappUploadAuthorization~~) operation. The value of IsvTerms is obtained from the PutObject operation.
        
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
        
        @description    You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        After you call the [GetChatappUploadAuthorization](~~GetChatappUploadAuthorization~~) operation to obtain the authentication information for uploading the file to Object Storage Service (OSS), you can use the authentication information to upload the file to the OSS server. To upload the file, you can call the SDK provided by OSS. When you upload the file, set the value of the key to the value of `Dir + "/" + file name`, such as C200293990209/isvTerms.pdf. The value of Dir is obtained from the [GetChatappUploadAuthorization](~~GetChatappUploadAuthorization~~) operation. The value of IsvTerms is obtained from the PutObject operation.
        
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
        
        @description    You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        After you call the [GetChatappUploadAuthorization](~~GetChatappUploadAuthorization~~) operation to obtain the authentication information for uploading the file to Object Storage Service (OSS), you can use the authentication information to upload the file to the OSS server. To upload the file, you can call the SDK provided by OSS. When you upload the file, set the value of the key to the value of `Dir + "/" + file name`, such as C200293990209/isvTerms.pdf. The value of Dir is obtained from the [GetChatappUploadAuthorization](~~GetChatappUploadAuthorization~~) operation. The value of IsvTerms is obtained from the PutObject operation.
        
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
        
        @description    You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        After you call the [GetChatappUploadAuthorization](~~GetChatappUploadAuthorization~~) operation to obtain the authentication information for uploading the file to Object Storage Service (OSS), you can use the authentication information to upload the file to the OSS server. To upload the file, you can call the SDK provided by OSS. When you upload the file, set the value of the key to the value of `Dir + "/" + file name`, such as C200293990209/isvTerms.pdf. The value of Dir is obtained from the [GetChatappUploadAuthorization](~~GetChatappUploadAuthorization~~) operation. The value of IsvTerms is obtained from the PutObject operation.
        
        @param request: SubmitIsvCustomerTermsRequest
        @return: SubmitIsvCustomerTermsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_isv_customer_terms_with_options_async(request, runtime)

    def trigger_chat_flow_with_options(
        self,
        tmp_req: cams_20200606_models.TriggerChatFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.TriggerChatFlowResponse:
        """
        @summary Trigger an Online ChatFlow
        
        @description After triggering an online flow, if your flow contains components that incur costs for cloud products, such as message sending or function calls, please ensure you fully understand the billing methods and prices of the related products before using this interface.
        
        @param tmp_req: TriggerChatFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TriggerChatFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.TriggerChatFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data):
            request.data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data, 'Data', 'json')
        query = {}
        if not UtilClient.is_unset(request.claim_time_millis):
            query['ClaimTimeMillis'] = request.claim_time_millis
        if not UtilClient.is_unset(request.data_shrink):
            query['Data'] = request.data_shrink
        if not UtilClient.is_unset(request.discard_time_millis):
            query['DiscardTimeMillis'] = request.discard_time_millis
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerChatFlow',
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
            cams_20200606_models.TriggerChatFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_chat_flow_with_options_async(
        self,
        tmp_req: cams_20200606_models.TriggerChatFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.TriggerChatFlowResponse:
        """
        @summary Trigger an Online ChatFlow
        
        @description After triggering an online flow, if your flow contains components that incur costs for cloud products, such as message sending or function calls, please ensure you fully understand the billing methods and prices of the related products before using this interface.
        
        @param tmp_req: TriggerChatFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TriggerChatFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.TriggerChatFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data):
            request.data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data, 'Data', 'json')
        query = {}
        if not UtilClient.is_unset(request.claim_time_millis):
            query['ClaimTimeMillis'] = request.claim_time_millis
        if not UtilClient.is_unset(request.data_shrink):
            query['Data'] = request.data_shrink
        if not UtilClient.is_unset(request.discard_time_millis):
            query['DiscardTimeMillis'] = request.discard_time_millis
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerChatFlow',
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
            cams_20200606_models.TriggerChatFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_chat_flow(
        self,
        request: cams_20200606_models.TriggerChatFlowRequest,
    ) -> cams_20200606_models.TriggerChatFlowResponse:
        """
        @summary Trigger an Online ChatFlow
        
        @description After triggering an online flow, if your flow contains components that incur costs for cloud products, such as message sending or function calls, please ensure you fully understand the billing methods and prices of the related products before using this interface.
        
        @param request: TriggerChatFlowRequest
        @return: TriggerChatFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.trigger_chat_flow_with_options(request, runtime)

    async def trigger_chat_flow_async(
        self,
        request: cams_20200606_models.TriggerChatFlowRequest,
    ) -> cams_20200606_models.TriggerChatFlowResponse:
        """
        @summary Trigger an Online ChatFlow
        
        @description After triggering an online flow, if your flow contains components that incur costs for cloud products, such as message sending or function calls, please ensure you fully understand the billing methods and prices of the related products before using this interface.
        
        @param request: TriggerChatFlowRequest
        @return: TriggerChatFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.trigger_chat_flow_with_options_async(request, runtime)

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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.queue_flag):
            query['QueueFlag'] = request.queue_flag
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.queue_flag):
            query['QueueFlag'] = request.queue_flag
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
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

    def update_chat_flow_with_options(
        self,
        tmp_req: cams_20200606_models.UpdateChatFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdateChatFlowResponse:
        """
        @summary Get Process
        
        @param tmp_req: UpdateChatFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateChatFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.UpdateChatFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateChatFlow',
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
            cams_20200606_models.UpdateChatFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_chat_flow_with_options_async(
        self,
        tmp_req: cams_20200606_models.UpdateChatFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdateChatFlowResponse:
        """
        @summary Get Process
        
        @param tmp_req: UpdateChatFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateChatFlowResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.UpdateChatFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateChatFlow',
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
            cams_20200606_models.UpdateChatFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_chat_flow(
        self,
        request: cams_20200606_models.UpdateChatFlowRequest,
    ) -> cams_20200606_models.UpdateChatFlowResponse:
        """
        @summary Get Process
        
        @param request: UpdateChatFlowRequest
        @return: UpdateChatFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_chat_flow_with_options(request, runtime)

    async def update_chat_flow_async(
        self,
        request: cams_20200606_models.UpdateChatFlowRequest,
    ) -> cams_20200606_models.UpdateChatFlowResponse:
        """
        @summary Get Process
        
        @param request: UpdateChatFlowRequest
        @return: UpdateChatFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_chat_flow_with_options_async(request, runtime)

    def update_chat_flow_log_setting_with_options(
        self,
        request: cams_20200606_models.UpdateChatFlowLogSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdateChatFlowLogSettingResponse:
        """
        @summary Modify chatFlow log settings
        
        @param request: UpdateChatFlowLogSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateChatFlowLogSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateChatFlowLogSetting',
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
            cams_20200606_models.UpdateChatFlowLogSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_chat_flow_log_setting_with_options_async(
        self,
        request: cams_20200606_models.UpdateChatFlowLogSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdateChatFlowLogSettingResponse:
        """
        @summary Modify chatFlow log settings
        
        @param request: UpdateChatFlowLogSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateChatFlowLogSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateChatFlowLogSetting',
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
            cams_20200606_models.UpdateChatFlowLogSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_chat_flow_log_setting(
        self,
        request: cams_20200606_models.UpdateChatFlowLogSettingRequest,
    ) -> cams_20200606_models.UpdateChatFlowLogSettingResponse:
        """
        @summary Modify chatFlow log settings
        
        @param request: UpdateChatFlowLogSettingRequest
        @return: UpdateChatFlowLogSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_chat_flow_log_setting_with_options(request, runtime)

    async def update_chat_flow_log_setting_async(
        self,
        request: cams_20200606_models.UpdateChatFlowLogSettingRequest,
    ) -> cams_20200606_models.UpdateChatFlowLogSettingResponse:
        """
        @summary Modify chatFlow log settings
        
        @param request: UpdateChatFlowLogSettingRequest
        @return: UpdateChatFlowLogSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_chat_flow_log_setting_with_options_async(request, runtime)

    def update_chat_group_with_options(
        self,
        request: cams_20200606_models.UpdateChatGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdateChatGroupResponse:
        """
        @summary UpdateChatGroup
        
        @param request: UpdateChatGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateChatGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.profile_picture_file):
            query['ProfilePictureFile'] = request.profile_picture_file
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateChatGroup',
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
            cams_20200606_models.UpdateChatGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_chat_group_with_options_async(
        self,
        request: cams_20200606_models.UpdateChatGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdateChatGroupResponse:
        """
        @summary UpdateChatGroup
        
        @param request: UpdateChatGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateChatGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not UtilClient.is_unset(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.profile_picture_file):
            query['ProfilePictureFile'] = request.profile_picture_file
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateChatGroup',
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
            cams_20200606_models.UpdateChatGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_chat_group(
        self,
        request: cams_20200606_models.UpdateChatGroupRequest,
    ) -> cams_20200606_models.UpdateChatGroupResponse:
        """
        @summary UpdateChatGroup
        
        @param request: UpdateChatGroupRequest
        @return: UpdateChatGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_chat_group_with_options(request, runtime)

    async def update_chat_group_async(
        self,
        request: cams_20200606_models.UpdateChatGroupRequest,
    ) -> cams_20200606_models.UpdateChatGroupResponse:
        """
        @summary UpdateChatGroup
        
        @param request: UpdateChatGroupRequest
        @return: UpdateChatGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_chat_group_with_options_async(request, runtime)

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

    def update_conversational_automation_with_options(
        self,
        tmp_req: cams_20200606_models.UpdateConversationalAutomationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdateConversationalAutomationResponse:
        """
        @summary Modifies welcoming messages, opening remarks, and commands for a phone number.
        
        @description ### [](#qps-)QPS limit
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        This operation will directly obtain data from Facebook, which sets an upper limit on the total number of calls for operations. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: UpdateConversationalAutomationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConversationalAutomationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.UpdateConversationalAutomationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.commands):
            request.commands_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.commands, 'Commands', 'json')
        if not UtilClient.is_unset(tmp_req.prompts):
            request.prompts_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.prompts, 'Prompts', 'json')
        query = {}
        if not UtilClient.is_unset(request.commands_shrink):
            query['Commands'] = request.commands_shrink
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.enable_welcome_message):
            query['EnableWelcomeMessage'] = request.enable_welcome_message
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.prompts_shrink):
            query['Prompts'] = request.prompts_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConversationalAutomation',
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
            cams_20200606_models.UpdateConversationalAutomationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_conversational_automation_with_options_async(
        self,
        tmp_req: cams_20200606_models.UpdateConversationalAutomationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdateConversationalAutomationResponse:
        """
        @summary Modifies welcoming messages, opening remarks, and commands for a phone number.
        
        @description ### [](#qps-)QPS limit
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        This operation will directly obtain data from Facebook, which sets an upper limit on the total number of calls for operations. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: UpdateConversationalAutomationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConversationalAutomationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.UpdateConversationalAutomationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.commands):
            request.commands_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.commands, 'Commands', 'json')
        if not UtilClient.is_unset(tmp_req.prompts):
            request.prompts_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.prompts, 'Prompts', 'json')
        query = {}
        if not UtilClient.is_unset(request.commands_shrink):
            query['Commands'] = request.commands_shrink
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.enable_welcome_message):
            query['EnableWelcomeMessage'] = request.enable_welcome_message
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.prompts_shrink):
            query['Prompts'] = request.prompts_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConversationalAutomation',
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
            cams_20200606_models.UpdateConversationalAutomationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_conversational_automation(
        self,
        request: cams_20200606_models.UpdateConversationalAutomationRequest,
    ) -> cams_20200606_models.UpdateConversationalAutomationResponse:
        """
        @summary Modifies welcoming messages, opening remarks, and commands for a phone number.
        
        @description ### [](#qps-)QPS limit
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        This operation will directly obtain data from Facebook, which sets an upper limit on the total number of calls for operations. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateConversationalAutomationRequest
        @return: UpdateConversationalAutomationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_conversational_automation_with_options(request, runtime)

    async def update_conversational_automation_async(
        self,
        request: cams_20200606_models.UpdateConversationalAutomationRequest,
    ) -> cams_20200606_models.UpdateConversationalAutomationResponse:
        """
        @summary Modifies welcoming messages, opening remarks, and commands for a phone number.
        
        @description ### [](#qps-)QPS limit
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        This operation will directly obtain data from Facebook, which sets an upper limit on the total number of calls for operations. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateConversationalAutomationRequest
        @return: UpdateConversationalAutomationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_conversational_automation_with_options_async(request, runtime)

    def update_flow_jsonasset_with_options(
        self,
        request: cams_20200606_models.UpdateFlowJSONAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdateFlowJSONAssetResponse:
        """
        @summary Updates a Flow by using JSON content.
        
        @param request: UpdateFlowJSONAssetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFlowJSONAssetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
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
        @summary Updates a Flow by using JSON content.
        
        @param request: UpdateFlowJSONAssetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFlowJSONAssetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
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
        @summary Updates a Flow by using JSON content.
        
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
        @summary Updates a Flow by using JSON content.
        
        @param request: UpdateFlowJSONAssetRequest
        @return: UpdateFlowJSONAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_flow_jsonasset_with_options_async(request, runtime)

    def update_flow_version_with_options(
        self,
        tmp_req: cams_20200606_models.UpdateFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdateFlowVersionResponse:
        """
        @summary Update flow version, used for updating the flow DSL on the canvas
        
        @param tmp_req: UpdateFlowVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFlowVersionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.UpdateFlowVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not UtilClient.is_unset(request.flow_view_model):
            query['FlowViewModel'] = request.flow_view_model
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFlowVersion',
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
            cams_20200606_models.UpdateFlowVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_flow_version_with_options_async(
        self,
        tmp_req: cams_20200606_models.UpdateFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdateFlowVersionResponse:
        """
        @summary Update flow version, used for updating the flow DSL on the canvas
        
        @param tmp_req: UpdateFlowVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFlowVersionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.UpdateFlowVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.biz_extend):
            request.biz_extend_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not UtilClient.is_unset(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not UtilClient.is_unset(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not UtilClient.is_unset(request.flow_view_model):
            query['FlowViewModel'] = request.flow_view_model
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFlowVersion',
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
            cams_20200606_models.UpdateFlowVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_flow_version(
        self,
        request: cams_20200606_models.UpdateFlowVersionRequest,
    ) -> cams_20200606_models.UpdateFlowVersionResponse:
        """
        @summary Update flow version, used for updating the flow DSL on the canvas
        
        @param request: UpdateFlowVersionRequest
        @return: UpdateFlowVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_flow_version_with_options(request, runtime)

    async def update_flow_version_async(
        self,
        request: cams_20200606_models.UpdateFlowVersionRequest,
    ) -> cams_20200606_models.UpdateFlowVersionResponse:
        """
        @summary Update flow version, used for updating the flow DSL on the canvas
        
        @param request: UpdateFlowVersionRequest
        @return: UpdateFlowVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_flow_version_with_options_async(request, runtime)

    def update_phone_encryption_public_key_with_options(
        self,
        request: cams_20200606_models.UpdatePhoneEncryptionPublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cams_20200606_models.UpdatePhoneEncryptionPublicKeyResponse:
        """
        @summary Updates the encryption public key of a phone number.
        
        @param request: UpdatePhoneEncryptionPublicKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePhoneEncryptionPublicKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.encryption_public_key):
            query['EncryptionPublicKey'] = request.encryption_public_key
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
        @summary Updates the encryption public key of a phone number.
        
        @param request: UpdatePhoneEncryptionPublicKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePhoneEncryptionPublicKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.encryption_public_key):
            query['EncryptionPublicKey'] = request.encryption_public_key
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
        @summary Updates the encryption public key of a phone number.
        
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
        @summary Updates the encryption public key of a phone number.
        
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
        @summary Modifies a quick-response (QR) code that contains a message.
        
        @param request: UpdatePhoneMessageQrdlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePhoneMessageQrdlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.generate_qr_image):
            query['GenerateQrImage'] = request.generate_qr_image
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.prefilled_message):
            query['PrefilledMessage'] = request.prefilled_message
        if not UtilClient.is_unset(request.qrdl_code):
            query['QrdlCode'] = request.qrdl_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
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
        @summary Modifies a quick-response (QR) code that contains a message.
        
        @param request: UpdatePhoneMessageQrdlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePhoneMessageQrdlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.generate_qr_image):
            query['GenerateQrImage'] = request.generate_qr_image
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.prefilled_message):
            query['PrefilledMessage'] = request.prefilled_message
        if not UtilClient.is_unset(request.qrdl_code):
            query['QrdlCode'] = request.qrdl_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
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
        @summary Modifies a quick-response (QR) code that contains a message.
        
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
        @summary Modifies a quick-response (QR) code that contains a message.
        
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
        \\   A value of OK indicates that the call is successful.
        \\   Other values indicate that the call fails. For more information, see [Error codes]\\(~~196974~~).
        
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.queue_flag):
            query['QueueFlag'] = request.queue_flag
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
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
        \\   A value of OK indicates that the call is successful.
        \\   Other values indicate that the call fails. For more information, see [Error codes]\\(~~196974~~).
        
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
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.queue_flag):
            query['QueueFlag'] = request.queue_flag
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
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
        \\   A value of OK indicates that the call is successful.
        \\   Other values indicate that the call fails. For more information, see [Error codes]\\(~~196974~~).
        
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
        \\   A value of OK indicates that the call is successful.
        \\   Other values indicate that the call fails. For more information, see [Error codes]\\(~~196974~~).
        
        @description The error message returned.
        
        @param request: UpdatePhoneWebhookRequest
        @return: UpdatePhoneWebhookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_phone_webhook_with_options_async(request, runtime)
