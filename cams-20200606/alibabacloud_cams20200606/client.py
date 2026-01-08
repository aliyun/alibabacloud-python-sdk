# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cams20200606 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_address_recover_suspend_with_options(
        self,
        tmp_req: main_models.AddAddressRecoverSuspendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAddressRecoverSuspendResponse:
        tmp_req.validate()
        request = main_models.AddAddressRecoverSuspendShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.audit_record):
            request.audit_record_shrink = Utils.array_to_string_with_specified_style(tmp_req.audit_record, 'AuditRecord', 'json')
        query = {}
        if not DaraCore.is_null(request.audit_record_shrink):
            query['AuditRecord'] = request.audit_record_shrink
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.request_type):
            query['RequestType'] = request.request_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAddressRecoverSuspend',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAddressRecoverSuspendResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_address_recover_suspend_with_options_async(
        self,
        tmp_req: main_models.AddAddressRecoverSuspendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAddressRecoverSuspendResponse:
        tmp_req.validate()
        request = main_models.AddAddressRecoverSuspendShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.audit_record):
            request.audit_record_shrink = Utils.array_to_string_with_specified_style(tmp_req.audit_record, 'AuditRecord', 'json')
        query = {}
        if not DaraCore.is_null(request.audit_record_shrink):
            query['AuditRecord'] = request.audit_record_shrink
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.request_type):
            query['RequestType'] = request.request_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAddressRecoverSuspend',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAddressRecoverSuspendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_address_recover_suspend(
        self,
        request: main_models.AddAddressRecoverSuspendRequest,
    ) -> main_models.AddAddressRecoverSuspendResponse:
        runtime = RuntimeOptions()
        return self.add_address_recover_suspend_with_options(request, runtime)

    async def add_address_recover_suspend_async(
        self,
        request: main_models.AddAddressRecoverSuspendRequest,
    ) -> main_models.AddAddressRecoverSuspendResponse:
        runtime = RuntimeOptions()
        return await self.add_address_recover_suspend_with_options_async(request, runtime)

    def add_audit_viber_open_with_options(
        self,
        tmp_req: main_models.AddAuditViberOpenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAuditViberOpenResponse:
        tmp_req.validate()
        request = main_models.AddAuditViberOpenShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.audit_record):
            request.audit_record_shrink = Utils.array_to_string_with_specified_style(tmp_req.audit_record, 'AuditRecord', 'json')
        query = {}
        if not DaraCore.is_null(request.audit_record_shrink):
            query['AuditRecord'] = request.audit_record_shrink
        if not DaraCore.is_null(request.audit_result):
            query['AuditResult'] = request.audit_result
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAuditViberOpen',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAuditViberOpenResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_audit_viber_open_with_options_async(
        self,
        tmp_req: main_models.AddAuditViberOpenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAuditViberOpenResponse:
        tmp_req.validate()
        request = main_models.AddAuditViberOpenShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.audit_record):
            request.audit_record_shrink = Utils.array_to_string_with_specified_style(tmp_req.audit_record, 'AuditRecord', 'json')
        query = {}
        if not DaraCore.is_null(request.audit_record_shrink):
            query['AuditRecord'] = request.audit_record_shrink
        if not DaraCore.is_null(request.audit_result):
            query['AuditResult'] = request.audit_result
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAuditViberOpen',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAuditViberOpenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_audit_viber_open(
        self,
        request: main_models.AddAuditViberOpenRequest,
    ) -> main_models.AddAuditViberOpenResponse:
        runtime = RuntimeOptions()
        return self.add_audit_viber_open_with_options(request, runtime)

    async def add_audit_viber_open_async(
        self,
        request: main_models.AddAuditViberOpenRequest,
    ) -> main_models.AddAuditViberOpenResponse:
        runtime = RuntimeOptions()
        return await self.add_audit_viber_open_with_options_async(request, runtime)

    def add_chat_group_with_options(
        self,
        request: main_models.AddChatGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddChatGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.subject):
            query['Subject'] = request.subject
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddChatGroup',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddChatGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_chat_group_with_options_async(
        self,
        request: main_models.AddChatGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddChatGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.subject):
            query['Subject'] = request.subject
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddChatGroup',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddChatGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_chat_group(
        self,
        request: main_models.AddChatGroupRequest,
    ) -> main_models.AddChatGroupResponse:
        runtime = RuntimeOptions()
        return self.add_chat_group_with_options(request, runtime)

    async def add_chat_group_async(
        self,
        request: main_models.AddChatGroupRequest,
    ) -> main_models.AddChatGroupResponse:
        runtime = RuntimeOptions()
        return await self.add_chat_group_with_options_async(request, runtime)

    def add_chat_group_invite_link_with_options(
        self,
        request: main_models.AddChatGroupInviteLinkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddChatGroupInviteLinkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddChatGroupInviteLink',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddChatGroupInviteLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_chat_group_invite_link_with_options_async(
        self,
        request: main_models.AddChatGroupInviteLinkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddChatGroupInviteLinkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddChatGroupInviteLink',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddChatGroupInviteLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_chat_group_invite_link(
        self,
        request: main_models.AddChatGroupInviteLinkRequest,
    ) -> main_models.AddChatGroupInviteLinkResponse:
        runtime = RuntimeOptions()
        return self.add_chat_group_invite_link_with_options(request, runtime)

    async def add_chat_group_invite_link_async(
        self,
        request: main_models.AddChatGroupInviteLinkRequest,
    ) -> main_models.AddChatGroupInviteLinkResponse:
        runtime = RuntimeOptions()
        return await self.add_chat_group_invite_link_with_options_async(request, runtime)

    def add_chatapp_phone_number_with_options(
        self,
        request: main_models.AddChatappPhoneNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddChatappPhoneNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cc):
            query['Cc'] = request.cc
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.pre_validate_id):
            query['PreValidateId'] = request.pre_validate_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.verified_name):
            query['VerifiedName'] = request.verified_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddChatappPhoneNumber',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddChatappPhoneNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_chatapp_phone_number_with_options_async(
        self,
        request: main_models.AddChatappPhoneNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddChatappPhoneNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cc):
            query['Cc'] = request.cc
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.pre_validate_id):
            query['PreValidateId'] = request.pre_validate_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.verified_name):
            query['VerifiedName'] = request.verified_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddChatappPhoneNumber',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddChatappPhoneNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_chatapp_phone_number(
        self,
        request: main_models.AddChatappPhoneNumberRequest,
    ) -> main_models.AddChatappPhoneNumberResponse:
        runtime = RuntimeOptions()
        return self.add_chatapp_phone_number_with_options(request, runtime)

    async def add_chatapp_phone_number_async(
        self,
        request: main_models.AddChatappPhoneNumberRequest,
    ) -> main_models.AddChatappPhoneNumberResponse:
        runtime = RuntimeOptions()
        return await self.add_chatapp_phone_number_with_options_async(request, runtime)

    def add_contacts_with_options(
        self,
        tmp_req: main_models.AddContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddContactsResponse:
        tmp_req.validate()
        request = main_models.AddContactsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.contact_details):
            query['ContactDetails'] = request.contact_details
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.groups):
            query['Groups'] = request.groups
        if not DaraCore.is_null(request.need_update):
            query['NeedUpdate'] = request.need_update
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddContacts',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_contacts_with_options_async(
        self,
        tmp_req: main_models.AddContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddContactsResponse:
        tmp_req.validate()
        request = main_models.AddContactsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.contact_details):
            query['ContactDetails'] = request.contact_details
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.groups):
            query['Groups'] = request.groups
        if not DaraCore.is_null(request.need_update):
            query['NeedUpdate'] = request.need_update
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddContacts',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_contacts(
        self,
        request: main_models.AddContactsRequest,
    ) -> main_models.AddContactsResponse:
        runtime = RuntimeOptions()
        return self.add_contacts_with_options(request, runtime)

    async def add_contacts_async(
        self,
        request: main_models.AddContactsRequest,
    ) -> main_models.AddContactsResponse:
        runtime = RuntimeOptions()
        return await self.add_contacts_with_options_async(request, runtime)

    def add_custom_audience_user_with_options(
        self,
        tmp_req: main_models.AddCustomAudienceUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomAudienceUserResponse:
        tmp_req.validate()
        request = main_models.AddCustomAudienceUserShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.users):
            request.users_shrink = Utils.array_to_string_with_specified_style(tmp_req.users, 'Users', 'json')
        query = {}
        if not DaraCore.is_null(request.ad_account_id):
            query['AdAccountId'] = request.ad_account_id
        if not DaraCore.is_null(request.batch_last_flag):
            query['BatchLastFlag'] = request.batch_last_flag
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.custom_audience_id):
            query['CustomAudienceId'] = request.custom_audience_id
        if not DaraCore.is_null(request.estimated_num_total):
            query['EstimatedNumTotal'] = request.estimated_num_total
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.users_shrink):
            query['Users'] = request.users_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomAudienceUser',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomAudienceUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_custom_audience_user_with_options_async(
        self,
        tmp_req: main_models.AddCustomAudienceUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomAudienceUserResponse:
        tmp_req.validate()
        request = main_models.AddCustomAudienceUserShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.users):
            request.users_shrink = Utils.array_to_string_with_specified_style(tmp_req.users, 'Users', 'json')
        query = {}
        if not DaraCore.is_null(request.ad_account_id):
            query['AdAccountId'] = request.ad_account_id
        if not DaraCore.is_null(request.batch_last_flag):
            query['BatchLastFlag'] = request.batch_last_flag
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.custom_audience_id):
            query['CustomAudienceId'] = request.custom_audience_id
        if not DaraCore.is_null(request.estimated_num_total):
            query['EstimatedNumTotal'] = request.estimated_num_total
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.users_shrink):
            query['Users'] = request.users_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomAudienceUser',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomAudienceUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_custom_audience_user(
        self,
        request: main_models.AddCustomAudienceUserRequest,
    ) -> main_models.AddCustomAudienceUserResponse:
        runtime = RuntimeOptions()
        return self.add_custom_audience_user_with_options(request, runtime)

    async def add_custom_audience_user_async(
        self,
        request: main_models.AddCustomAudienceUserRequest,
    ) -> main_models.AddCustomAudienceUserResponse:
        runtime = RuntimeOptions()
        return await self.add_custom_audience_user_with_options_async(request, runtime)

    def add_group_with_options(
        self,
        tmp_req: main_models.AddGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGroupResponse:
        tmp_req.validate()
        request = main_models.AddGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.contact_details):
            query['ContactDetails'] = request.contact_details
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGroup',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_group_with_options_async(
        self,
        tmp_req: main_models.AddGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGroupResponse:
        tmp_req.validate()
        request = main_models.AddGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.contact_details):
            query['ContactDetails'] = request.contact_details
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGroup',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_group(
        self,
        request: main_models.AddGroupRequest,
    ) -> main_models.AddGroupResponse:
        runtime = RuntimeOptions()
        return self.add_group_with_options(request, runtime)

    async def add_group_async(
        self,
        request: main_models.AddGroupRequest,
    ) -> main_models.AddGroupResponse:
        runtime = RuntimeOptions()
        return await self.add_group_with_options_async(request, runtime)

    def add_marketing_flow_with_options(
        self,
        tmp_req: main_models.AddMarketingFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddMarketingFlowResponse:
        tmp_req.validate()
        request = main_models.AddMarketingFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        query = {}
        if not DaraCore.is_null(request.activity_desc):
            query['ActivityDesc'] = request.activity_desc
        if not DaraCore.is_null(request.activity_name):
            query['ActivityName'] = request.activity_name
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.execution_type):
            query['ExecutionType'] = request.execution_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.param_flag):
            query['ParamFlag'] = request.param_flag
        if not DaraCore.is_null(request.params_shrink):
            query['Params'] = request.params_shrink
        if not DaraCore.is_null(request.related_flow_code):
            query['RelatedFlowCode'] = request.related_flow_code
        if not DaraCore.is_null(request.related_flow_name):
            query['RelatedFlowName'] = request.related_flow_name
        if not DaraCore.is_null(request.related_group_id):
            query['RelatedGroupId'] = request.related_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddMarketingFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMarketingFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_marketing_flow_with_options_async(
        self,
        tmp_req: main_models.AddMarketingFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddMarketingFlowResponse:
        tmp_req.validate()
        request = main_models.AddMarketingFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        query = {}
        if not DaraCore.is_null(request.activity_desc):
            query['ActivityDesc'] = request.activity_desc
        if not DaraCore.is_null(request.activity_name):
            query['ActivityName'] = request.activity_name
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.execution_type):
            query['ExecutionType'] = request.execution_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.param_flag):
            query['ParamFlag'] = request.param_flag
        if not DaraCore.is_null(request.params_shrink):
            query['Params'] = request.params_shrink
        if not DaraCore.is_null(request.related_flow_code):
            query['RelatedFlowCode'] = request.related_flow_code
        if not DaraCore.is_null(request.related_flow_name):
            query['RelatedFlowName'] = request.related_flow_name
        if not DaraCore.is_null(request.related_group_id):
            query['RelatedGroupId'] = request.related_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddMarketingFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMarketingFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_marketing_flow(
        self,
        request: main_models.AddMarketingFlowRequest,
    ) -> main_models.AddMarketingFlowResponse:
        runtime = RuntimeOptions()
        return self.add_marketing_flow_with_options(request, runtime)

    async def add_marketing_flow_async(
        self,
        request: main_models.AddMarketingFlowRequest,
    ) -> main_models.AddMarketingFlowResponse:
        runtime = RuntimeOptions()
        return await self.add_marketing_flow_with_options_async(request, runtime)

    def bind_dm_account_with_options(
        self,
        tmp_req: main_models.BindDmAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindDmAccountResponse:
        tmp_req.validate()
        request = main_models.BindDmAccountShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extend_attr):
            request.extend_attr_shrink = Utils.array_to_string_with_specified_style(tmp_req.extend_attr, 'ExtendAttr', 'json')
        query = {}
        if not DaraCore.is_null(request.account_code):
            query['AccountCode'] = request.account_code
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.extend_attr_shrink):
            query['ExtendAttr'] = request.extend_attr_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindDmAccount',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindDmAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_dm_account_with_options_async(
        self,
        tmp_req: main_models.BindDmAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindDmAccountResponse:
        tmp_req.validate()
        request = main_models.BindDmAccountShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extend_attr):
            request.extend_attr_shrink = Utils.array_to_string_with_specified_style(tmp_req.extend_attr, 'ExtendAttr', 'json')
        query = {}
        if not DaraCore.is_null(request.account_code):
            query['AccountCode'] = request.account_code
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.extend_attr_shrink):
            query['ExtendAttr'] = request.extend_attr_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindDmAccount',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindDmAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_dm_account(
        self,
        request: main_models.BindDmAccountRequest,
    ) -> main_models.BindDmAccountResponse:
        runtime = RuntimeOptions()
        return self.bind_dm_account_with_options(request, runtime)

    async def bind_dm_account_async(
        self,
        request: main_models.BindDmAccountRequest,
    ) -> main_models.BindDmAccountResponse:
        runtime = RuntimeOptions()
        return await self.bind_dm_account_with_options_async(request, runtime)

    def bind_instagram_page_with_options(
        self,
        request: main_models.BindInstagramPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindInstagramPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindInstagramPage',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindInstagramPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_instagram_page_with_options_async(
        self,
        request: main_models.BindInstagramPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindInstagramPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindInstagramPage',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindInstagramPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_instagram_page(
        self,
        request: main_models.BindInstagramPageRequest,
    ) -> main_models.BindInstagramPageResponse:
        runtime = RuntimeOptions()
        return self.bind_instagram_page_with_options(request, runtime)

    async def bind_instagram_page_async(
        self,
        request: main_models.BindInstagramPageRequest,
    ) -> main_models.BindInstagramPageResponse:
        runtime = RuntimeOptions()
        return await self.bind_instagram_page_with_options_async(request, runtime)

    def bind_messenger_page_with_options(
        self,
        request: main_models.BindMessengerPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindMessengerPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindMessengerPage',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindMessengerPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_messenger_page_with_options_async(
        self,
        request: main_models.BindMessengerPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindMessengerPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindMessengerPage',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindMessengerPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_messenger_page(
        self,
        request: main_models.BindMessengerPageRequest,
    ) -> main_models.BindMessengerPageResponse:
        runtime = RuntimeOptions()
        return self.bind_messenger_page_with_options(request, runtime)

    async def bind_messenger_page_async(
        self,
        request: main_models.BindMessengerPageRequest,
    ) -> main_models.BindMessengerPageResponse:
        runtime = RuntimeOptions()
        return await self.bind_messenger_page_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def chatapp_bind_waba_with_options(
        self,
        request: main_models.ChatappBindWabaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatappBindWabaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatappBindWaba',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatappBindWabaResponse(),
            self.call_api(params, req, runtime)
        )

    async def chatapp_bind_waba_with_options_async(
        self,
        request: main_models.ChatappBindWabaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatappBindWabaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatappBindWaba',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatappBindWabaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chatapp_bind_waba(
        self,
        request: main_models.ChatappBindWabaRequest,
    ) -> main_models.ChatappBindWabaResponse:
        runtime = RuntimeOptions()
        return self.chatapp_bind_waba_with_options(request, runtime)

    async def chatapp_bind_waba_async(
        self,
        request: main_models.ChatappBindWabaRequest,
    ) -> main_models.ChatappBindWabaResponse:
        runtime = RuntimeOptions()
        return await self.chatapp_bind_waba_with_options_async(request, runtime)

    def chatapp_migration_register_with_options(
        self,
        request: main_models.ChatappMigrationRegisterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatappMigrationRegisterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatappMigrationRegister',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatappMigrationRegisterResponse(),
            self.call_api(params, req, runtime)
        )

    async def chatapp_migration_register_with_options_async(
        self,
        request: main_models.ChatappMigrationRegisterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatappMigrationRegisterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatappMigrationRegister',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatappMigrationRegisterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chatapp_migration_register(
        self,
        request: main_models.ChatappMigrationRegisterRequest,
    ) -> main_models.ChatappMigrationRegisterResponse:
        runtime = RuntimeOptions()
        return self.chatapp_migration_register_with_options(request, runtime)

    async def chatapp_migration_register_async(
        self,
        request: main_models.ChatappMigrationRegisterRequest,
    ) -> main_models.ChatappMigrationRegisterResponse:
        runtime = RuntimeOptions()
        return await self.chatapp_migration_register_with_options_async(request, runtime)

    def chatapp_migration_verified_with_options(
        self,
        request: main_models.ChatappMigrationVerifiedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatappMigrationVerifiedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatappMigrationVerified',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatappMigrationVerifiedResponse(),
            self.call_api(params, req, runtime)
        )

    async def chatapp_migration_verified_with_options_async(
        self,
        request: main_models.ChatappMigrationVerifiedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatappMigrationVerifiedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatappMigrationVerified',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatappMigrationVerifiedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chatapp_migration_verified(
        self,
        request: main_models.ChatappMigrationVerifiedRequest,
    ) -> main_models.ChatappMigrationVerifiedResponse:
        runtime = RuntimeOptions()
        return self.chatapp_migration_verified_with_options(request, runtime)

    async def chatapp_migration_verified_async(
        self,
        request: main_models.ChatappMigrationVerifiedRequest,
    ) -> main_models.ChatappMigrationVerifiedResponse:
        runtime = RuntimeOptions()
        return await self.chatapp_migration_verified_with_options_async(request, runtime)

    def chatapp_phone_number_deregister_with_options(
        self,
        request: main_models.ChatappPhoneNumberDeregisterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatappPhoneNumberDeregisterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatappPhoneNumberDeregister',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatappPhoneNumberDeregisterResponse(),
            self.call_api(params, req, runtime)
        )

    async def chatapp_phone_number_deregister_with_options_async(
        self,
        request: main_models.ChatappPhoneNumberDeregisterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatappPhoneNumberDeregisterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatappPhoneNumberDeregister',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatappPhoneNumberDeregisterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chatapp_phone_number_deregister(
        self,
        request: main_models.ChatappPhoneNumberDeregisterRequest,
    ) -> main_models.ChatappPhoneNumberDeregisterResponse:
        runtime = RuntimeOptions()
        return self.chatapp_phone_number_deregister_with_options(request, runtime)

    async def chatapp_phone_number_deregister_async(
        self,
        request: main_models.ChatappPhoneNumberDeregisterRequest,
    ) -> main_models.ChatappPhoneNumberDeregisterResponse:
        runtime = RuntimeOptions()
        return await self.chatapp_phone_number_deregister_with_options_async(request, runtime)

    def chatapp_phone_number_register_with_options(
        self,
        request: main_models.ChatappPhoneNumberRegisterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatappPhoneNumberRegisterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatappPhoneNumberRegister',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatappPhoneNumberRegisterResponse(),
            self.call_api(params, req, runtime)
        )

    async def chatapp_phone_number_register_with_options_async(
        self,
        request: main_models.ChatappPhoneNumberRegisterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatappPhoneNumberRegisterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatappPhoneNumberRegister',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatappPhoneNumberRegisterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chatapp_phone_number_register(
        self,
        request: main_models.ChatappPhoneNumberRegisterRequest,
    ) -> main_models.ChatappPhoneNumberRegisterResponse:
        runtime = RuntimeOptions()
        return self.chatapp_phone_number_register_with_options(request, runtime)

    async def chatapp_phone_number_register_async(
        self,
        request: main_models.ChatappPhoneNumberRegisterRequest,
    ) -> main_models.ChatappPhoneNumberRegisterResponse:
        runtime = RuntimeOptions()
        return await self.chatapp_phone_number_register_with_options_async(request, runtime)

    def chatapp_sync_phone_number_with_options(
        self,
        request: main_models.ChatappSyncPhoneNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatappSyncPhoneNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatappSyncPhoneNumber',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatappSyncPhoneNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def chatapp_sync_phone_number_with_options_async(
        self,
        request: main_models.ChatappSyncPhoneNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatappSyncPhoneNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatappSyncPhoneNumber',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatappSyncPhoneNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chatapp_sync_phone_number(
        self,
        request: main_models.ChatappSyncPhoneNumberRequest,
    ) -> main_models.ChatappSyncPhoneNumberResponse:
        runtime = RuntimeOptions()
        return self.chatapp_sync_phone_number_with_options(request, runtime)

    async def chatapp_sync_phone_number_async(
        self,
        request: main_models.ChatappSyncPhoneNumberRequest,
    ) -> main_models.ChatappSyncPhoneNumberResponse:
        runtime = RuntimeOptions()
        return await self.chatapp_sync_phone_number_with_options_async(request, runtime)

    def chatapp_verify_and_register_with_options(
        self,
        request: main_models.ChatappVerifyAndRegisterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatappVerifyAndRegisterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatappVerifyAndRegister',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatappVerifyAndRegisterResponse(),
            self.call_api(params, req, runtime)
        )

    async def chatapp_verify_and_register_with_options_async(
        self,
        request: main_models.ChatappVerifyAndRegisterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatappVerifyAndRegisterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatappVerifyAndRegister',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatappVerifyAndRegisterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chatapp_verify_and_register(
        self,
        request: main_models.ChatappVerifyAndRegisterRequest,
    ) -> main_models.ChatappVerifyAndRegisterResponse:
        runtime = RuntimeOptions()
        return self.chatapp_verify_and_register_with_options(request, runtime)

    async def chatapp_verify_and_register_async(
        self,
        request: main_models.ChatappVerifyAndRegisterRequest,
    ) -> main_models.ChatappVerifyAndRegisterResponse:
        runtime = RuntimeOptions()
        return await self.chatapp_verify_and_register_with_options_async(request, runtime)

    def copy_template_with_options(
        self,
        request: main_models.CopyTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scene_template_code):
            query['SceneTemplateCode'] = request.scene_template_code
        if not DaraCore.is_null(request.scene_template_name):
            query['SceneTemplateName'] = request.scene_template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CopyTemplate',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_template_with_options_async(
        self,
        request: main_models.CopyTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scene_template_code):
            query['SceneTemplateCode'] = request.scene_template_code
        if not DaraCore.is_null(request.scene_template_name):
            query['SceneTemplateName'] = request.scene_template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CopyTemplate',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_template(
        self,
        request: main_models.CopyTemplateRequest,
    ) -> main_models.CopyTemplateResponse:
        runtime = RuntimeOptions()
        return self.copy_template_with_options(request, runtime)

    async def copy_template_async(
        self,
        request: main_models.CopyTemplateRequest,
    ) -> main_models.CopyTemplateResponse:
        runtime = RuntimeOptions()
        return await self.copy_template_with_options_async(request, runtime)

    def create_chat_flow_with_options(
        self,
        tmp_req: main_models.CreateChatFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatFlowResponse:
        tmp_req.validate()
        request = main_models.CreateChatFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_trigger_type):
            query['FlowTriggerType'] = request.flow_trigger_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateChatFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chat_flow_with_options_async(
        self,
        tmp_req: main_models.CreateChatFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatFlowResponse:
        tmp_req.validate()
        request = main_models.CreateChatFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_trigger_type):
            query['FlowTriggerType'] = request.flow_trigger_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateChatFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chat_flow(
        self,
        request: main_models.CreateChatFlowRequest,
    ) -> main_models.CreateChatFlowResponse:
        runtime = RuntimeOptions()
        return self.create_chat_flow_with_options(request, runtime)

    async def create_chat_flow_async(
        self,
        request: main_models.CreateChatFlowRequest,
    ) -> main_models.CreateChatFlowResponse:
        runtime = RuntimeOptions()
        return await self.create_chat_flow_with_options_async(request, runtime)

    def create_chat_flow_by_import_with_options(
        self,
        tmp_req: main_models.CreateChatFlowByImportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatFlowByImportResponse:
        tmp_req.validate()
        request = main_models.CreateChatFlowByImportShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_view_model):
            query['FlowViewModel'] = request.flow_view_model
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateChatFlowByImport',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatFlowByImportResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chat_flow_by_import_with_options_async(
        self,
        tmp_req: main_models.CreateChatFlowByImportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatFlowByImportResponse:
        tmp_req.validate()
        request = main_models.CreateChatFlowByImportShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_view_model):
            query['FlowViewModel'] = request.flow_view_model
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateChatFlowByImport',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatFlowByImportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chat_flow_by_import(
        self,
        request: main_models.CreateChatFlowByImportRequest,
    ) -> main_models.CreateChatFlowByImportResponse:
        runtime = RuntimeOptions()
        return self.create_chat_flow_by_import_with_options(request, runtime)

    async def create_chat_flow_by_import_async(
        self,
        request: main_models.CreateChatFlowByImportRequest,
    ) -> main_models.CreateChatFlowByImportResponse:
        runtime = RuntimeOptions()
        return await self.create_chat_flow_by_import_with_options_async(request, runtime)

    def create_chat_flow_log_setting_with_options(
        self,
        request: main_models.CreateChatFlowLogSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatFlowLogSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateChatFlowLogSetting',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatFlowLogSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chat_flow_log_setting_with_options_async(
        self,
        request: main_models.CreateChatFlowLogSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatFlowLogSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateChatFlowLogSetting',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatFlowLogSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chat_flow_log_setting(
        self,
        request: main_models.CreateChatFlowLogSettingRequest,
    ) -> main_models.CreateChatFlowLogSettingResponse:
        runtime = RuntimeOptions()
        return self.create_chat_flow_log_setting_with_options(request, runtime)

    async def create_chat_flow_log_setting_async(
        self,
        request: main_models.CreateChatFlowLogSettingRequest,
    ) -> main_models.CreateChatFlowLogSettingResponse:
        runtime = RuntimeOptions()
        return await self.create_chat_flow_log_setting_with_options_async(request, runtime)

    def create_chatapp_migration_initiate_with_options(
        self,
        request: main_models.CreateChatappMigrationInitiateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatappMigrationInitiateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.country_code):
            query['CountryCode'] = request.country_code
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.mobile_number):
            query['MobileNumber'] = request.mobile_number
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateChatappMigrationInitiate',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatappMigrationInitiateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chatapp_migration_initiate_with_options_async(
        self,
        request: main_models.CreateChatappMigrationInitiateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatappMigrationInitiateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.country_code):
            query['CountryCode'] = request.country_code
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.mobile_number):
            query['MobileNumber'] = request.mobile_number
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateChatappMigrationInitiate',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatappMigrationInitiateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chatapp_migration_initiate(
        self,
        request: main_models.CreateChatappMigrationInitiateRequest,
    ) -> main_models.CreateChatappMigrationInitiateResponse:
        runtime = RuntimeOptions()
        return self.create_chatapp_migration_initiate_with_options(request, runtime)

    async def create_chatapp_migration_initiate_async(
        self,
        request: main_models.CreateChatappMigrationInitiateRequest,
    ) -> main_models.CreateChatappMigrationInitiateResponse:
        runtime = RuntimeOptions()
        return await self.create_chatapp_migration_initiate_with_options_async(request, runtime)

    def create_chatapp_template_with_options(
        self,
        tmp_req: main_models.CreateChatappTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatappTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateChatappTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.components):
            request.components_shrink = Utils.array_to_string_with_specified_style(tmp_req.components, 'Components', 'json')
        if not DaraCore.is_null(tmp_req.example):
            request.example_shrink = Utils.array_to_string_with_specified_style(tmp_req.example, 'Example', 'json')
        body = {}
        if not DaraCore.is_null(request.allow_category_change):
            body['AllowCategoryChange'] = request.allow_category_change
        if not DaraCore.is_null(request.category):
            body['Category'] = request.category
        if not DaraCore.is_null(request.category_change_paused):
            body['CategoryChangePaused'] = request.category_change_paused
        if not DaraCore.is_null(request.components_shrink):
            body['Components'] = request.components_shrink
        if not DaraCore.is_null(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.cust_waba_id):
            body['CustWabaId'] = request.cust_waba_id
        if not DaraCore.is_null(request.example_shrink):
            body['Example'] = request.example_shrink
        if not DaraCore.is_null(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.language):
            body['Language'] = request.language
        if not DaraCore.is_null(request.message_send_ttl_seconds):
            body['MessageSendTtlSeconds'] = request.message_send_ttl_seconds
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.template_type):
            body['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateChatappTemplate',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatappTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chatapp_template_with_options_async(
        self,
        tmp_req: main_models.CreateChatappTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateChatappTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateChatappTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.components):
            request.components_shrink = Utils.array_to_string_with_specified_style(tmp_req.components, 'Components', 'json')
        if not DaraCore.is_null(tmp_req.example):
            request.example_shrink = Utils.array_to_string_with_specified_style(tmp_req.example, 'Example', 'json')
        body = {}
        if not DaraCore.is_null(request.allow_category_change):
            body['AllowCategoryChange'] = request.allow_category_change
        if not DaraCore.is_null(request.category):
            body['Category'] = request.category
        if not DaraCore.is_null(request.category_change_paused):
            body['CategoryChangePaused'] = request.category_change_paused
        if not DaraCore.is_null(request.components_shrink):
            body['Components'] = request.components_shrink
        if not DaraCore.is_null(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.cust_waba_id):
            body['CustWabaId'] = request.cust_waba_id
        if not DaraCore.is_null(request.example_shrink):
            body['Example'] = request.example_shrink
        if not DaraCore.is_null(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.language):
            body['Language'] = request.language
        if not DaraCore.is_null(request.message_send_ttl_seconds):
            body['MessageSendTtlSeconds'] = request.message_send_ttl_seconds
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.template_type):
            body['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateChatappTemplate',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChatappTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chatapp_template(
        self,
        request: main_models.CreateChatappTemplateRequest,
    ) -> main_models.CreateChatappTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_chatapp_template_with_options(request, runtime)

    async def create_chatapp_template_async(
        self,
        request: main_models.CreateChatappTemplateRequest,
    ) -> main_models.CreateChatappTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_chatapp_template_with_options_async(request, runtime)

    def create_custom_audience_with_options(
        self,
        request: main_models.CreateCustomAudienceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomAudienceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ad_account_id):
            query['AdAccountId'] = request.ad_account_id
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomAudience',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomAudienceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_audience_with_options_async(
        self,
        request: main_models.CreateCustomAudienceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomAudienceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ad_account_id):
            query['AdAccountId'] = request.ad_account_id
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomAudience',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomAudienceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_audience(
        self,
        request: main_models.CreateCustomAudienceRequest,
    ) -> main_models.CreateCustomAudienceResponse:
        runtime = RuntimeOptions()
        return self.create_custom_audience_with_options(request, runtime)

    async def create_custom_audience_async(
        self,
        request: main_models.CreateCustomAudienceRequest,
    ) -> main_models.CreateCustomAudienceResponse:
        runtime = RuntimeOptions()
        return await self.create_custom_audience_with_options_async(request, runtime)

    def create_flow_with_options(
        self,
        tmp_req: main_models.CreateFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFlowResponse:
        tmp_req.validate()
        request = main_models.CreateFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.categories):
            request.categories_shrink = Utils.array_to_string_with_specified_style(tmp_req.categories, 'Categories', 'json')
        query = {}
        if not DaraCore.is_null(request.categories_shrink):
            query['Categories'] = request.categories_shrink
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.flow_name):
            query['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_with_options_async(
        self,
        tmp_req: main_models.CreateFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFlowResponse:
        tmp_req.validate()
        request = main_models.CreateFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.categories):
            request.categories_shrink = Utils.array_to_string_with_specified_style(tmp_req.categories, 'Categories', 'json')
        query = {}
        if not DaraCore.is_null(request.categories_shrink):
            query['Categories'] = request.categories_shrink
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.flow_name):
            query['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow(
        self,
        request: main_models.CreateFlowRequest,
    ) -> main_models.CreateFlowResponse:
        runtime = RuntimeOptions()
        return self.create_flow_with_options(request, runtime)

    async def create_flow_async(
        self,
        request: main_models.CreateFlowRequest,
    ) -> main_models.CreateFlowResponse:
        runtime = RuntimeOptions()
        return await self.create_flow_with_options_async(request, runtime)

    def create_flow_version_with_options(
        self,
        tmp_req: main_models.CreateFlowVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFlowVersionResponse:
        tmp_req.validate()
        request = main_models.CreateFlowVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.flow_version_copy_from):
            query['FlowVersionCopyFrom'] = request.flow_version_copy_from
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFlowVersion',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFlowVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_version_with_options_async(
        self,
        tmp_req: main_models.CreateFlowVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFlowVersionResponse:
        tmp_req.validate()
        request = main_models.CreateFlowVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.flow_version_copy_from):
            query['FlowVersionCopyFrom'] = request.flow_version_copy_from
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFlowVersion',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFlowVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow_version(
        self,
        request: main_models.CreateFlowVersionRequest,
    ) -> main_models.CreateFlowVersionResponse:
        runtime = RuntimeOptions()
        return self.create_flow_version_with_options(request, runtime)

    async def create_flow_version_async(
        self,
        request: main_models.CreateFlowVersionRequest,
    ) -> main_models.CreateFlowVersionResponse:
        runtime = RuntimeOptions()
        return await self.create_flow_version_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.contact_mail):
            query['ContactMail'] = request.contact_mail
        if not DaraCore.is_null(request.country_id):
            query['CountryId'] = request.country_id
        if not DaraCore.is_null(request.facebook_bm_id):
            query['FacebookBmId'] = request.facebook_bm_id
        if not DaraCore.is_null(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.is_confirm_audit):
            query['IsConfirmAudit'] = request.is_confirm_audit
        if not DaraCore.is_null(request.isv_terms):
            query['IsvTerms'] = request.isv_terms
        if not DaraCore.is_null(request.office_address):
            query['OfficeAddress'] = request.office_address
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2020-06-06',
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
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.contact_mail):
            query['ContactMail'] = request.contact_mail
        if not DaraCore.is_null(request.country_id):
            query['CountryId'] = request.country_id
        if not DaraCore.is_null(request.facebook_bm_id):
            query['FacebookBmId'] = request.facebook_bm_id
        if not DaraCore.is_null(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.is_confirm_audit):
            query['IsConfirmAudit'] = request.is_confirm_audit
        if not DaraCore.is_null(request.isv_terms):
            query['IsvTerms'] = request.isv_terms
        if not DaraCore.is_null(request.office_address):
            query['OfficeAddress'] = request.office_address
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2020-06-06',
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

    def create_message_campaign_with_options(
        self,
        request: main_models.CreateMessageCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMessageCampaignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ad_account_id):
            query['AdAccountId'] = request.ad_account_id
        if not DaraCore.is_null(request.budget):
            query['Budget'] = request.budget
        if not DaraCore.is_null(request.budget_type):
            query['BudgetType'] = request.budget_type
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMessageCampaign',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMessageCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_message_campaign_with_options_async(
        self,
        request: main_models.CreateMessageCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMessageCampaignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ad_account_id):
            query['AdAccountId'] = request.ad_account_id
        if not DaraCore.is_null(request.budget):
            query['Budget'] = request.budget
        if not DaraCore.is_null(request.budget_type):
            query['BudgetType'] = request.budget_type
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMessageCampaign',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMessageCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_message_campaign(
        self,
        request: main_models.CreateMessageCampaignRequest,
    ) -> main_models.CreateMessageCampaignResponse:
        runtime = RuntimeOptions()
        return self.create_message_campaign_with_options(request, runtime)

    async def create_message_campaign_async(
        self,
        request: main_models.CreateMessageCampaignRequest,
    ) -> main_models.CreateMessageCampaignResponse:
        runtime = RuntimeOptions()
        return await self.create_message_campaign_with_options_async(request, runtime)

    def create_messenger_page_with_options(
        self,
        tmp_req: main_models.CreateMessengerPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMessengerPageResponse:
        tmp_req.validate()
        request = main_models.CreateMessengerPageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ad_account_ids):
            request.ad_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ad_account_ids, 'AdAccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.ad_account_ids_shrink):
            query['AdAccountIds'] = request.ad_account_ids_shrink
        if not DaraCore.is_null(request.authentication_code):
            query['AuthenticationCode'] = request.authentication_code
        if not DaraCore.is_null(request.business_id):
            query['BusinessId'] = request.business_id
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMessengerPage',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMessengerPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_messenger_page_with_options_async(
        self,
        tmp_req: main_models.CreateMessengerPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMessengerPageResponse:
        tmp_req.validate()
        request = main_models.CreateMessengerPageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ad_account_ids):
            request.ad_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ad_account_ids, 'AdAccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.ad_account_ids_shrink):
            query['AdAccountIds'] = request.ad_account_ids_shrink
        if not DaraCore.is_null(request.authentication_code):
            query['AuthenticationCode'] = request.authentication_code
        if not DaraCore.is_null(request.business_id):
            query['BusinessId'] = request.business_id
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMessengerPage',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMessengerPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_messenger_page(
        self,
        request: main_models.CreateMessengerPageRequest,
    ) -> main_models.CreateMessengerPageResponse:
        runtime = RuntimeOptions()
        return self.create_messenger_page_with_options(request, runtime)

    async def create_messenger_page_async(
        self,
        request: main_models.CreateMessengerPageRequest,
    ) -> main_models.CreateMessengerPageResponse:
        runtime = RuntimeOptions()
        return await self.create_messenger_page_with_options_async(request, runtime)

    def create_phone_message_qrdl_with_options(
        self,
        request: main_models.CreatePhoneMessageQrdlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePhoneMessageQrdlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.generate_qr_image):
            query['GenerateQrImage'] = request.generate_qr_image
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.prefilled_message):
            query['PrefilledMessage'] = request.prefilled_message
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePhoneMessageQrdl',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePhoneMessageQrdlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_phone_message_qrdl_with_options_async(
        self,
        request: main_models.CreatePhoneMessageQrdlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePhoneMessageQrdlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.generate_qr_image):
            query['GenerateQrImage'] = request.generate_qr_image
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.prefilled_message):
            query['PrefilledMessage'] = request.prefilled_message
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePhoneMessageQrdl',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePhoneMessageQrdlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_phone_message_qrdl(
        self,
        request: main_models.CreatePhoneMessageQrdlRequest,
    ) -> main_models.CreatePhoneMessageQrdlResponse:
        runtime = RuntimeOptions()
        return self.create_phone_message_qrdl_with_options(request, runtime)

    async def create_phone_message_qrdl_async(
        self,
        request: main_models.CreatePhoneMessageQrdlRequest,
    ) -> main_models.CreatePhoneMessageQrdlResponse:
        runtime = RuntimeOptions()
        return await self.create_phone_message_qrdl_with_options_async(request, runtime)

    def create_whatsapp_conversion_api_with_options(
        self,
        tmp_req: main_models.CreateWhatsappConversionApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWhatsappConversionApiResponse:
        tmp_req.validate()
        request = main_models.CreateWhatsappConversionApiShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.permissions):
            request.permissions_shrink = Utils.array_to_string_with_specified_style(tmp_req.permissions, 'Permissions', 'json')
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.permissions_shrink):
            query['Permissions'] = request.permissions_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWhatsappConversionApi',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWhatsappConversionApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_whatsapp_conversion_api_with_options_async(
        self,
        tmp_req: main_models.CreateWhatsappConversionApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWhatsappConversionApiResponse:
        tmp_req.validate()
        request = main_models.CreateWhatsappConversionApiShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.permissions):
            request.permissions_shrink = Utils.array_to_string_with_specified_style(tmp_req.permissions, 'Permissions', 'json')
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.permissions_shrink):
            query['Permissions'] = request.permissions_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWhatsappConversionApi',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWhatsappConversionApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_whatsapp_conversion_api(
        self,
        request: main_models.CreateWhatsappConversionApiRequest,
    ) -> main_models.CreateWhatsappConversionApiResponse:
        runtime = RuntimeOptions()
        return self.create_whatsapp_conversion_api_with_options(request, runtime)

    async def create_whatsapp_conversion_api_async(
        self,
        request: main_models.CreateWhatsappConversionApiRequest,
    ) -> main_models.CreateWhatsappConversionApiResponse:
        runtime = RuntimeOptions()
        return await self.create_whatsapp_conversion_api_with_options_async(request, runtime)

    def delete_chat_flow_with_options(
        self,
        tmp_req: main_models.DeleteChatFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChatFlowResponse:
        tmp_req.validate()
        request = main_models.DeleteChatFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChatFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChatFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chat_flow_with_options_async(
        self,
        tmp_req: main_models.DeleteChatFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChatFlowResponse:
        tmp_req.validate()
        request = main_models.DeleteChatFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChatFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChatFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chat_flow(
        self,
        request: main_models.DeleteChatFlowRequest,
    ) -> main_models.DeleteChatFlowResponse:
        runtime = RuntimeOptions()
        return self.delete_chat_flow_with_options(request, runtime)

    async def delete_chat_flow_async(
        self,
        request: main_models.DeleteChatFlowRequest,
    ) -> main_models.DeleteChatFlowResponse:
        runtime = RuntimeOptions()
        return await self.delete_chat_flow_with_options_async(request, runtime)

    def delete_chat_group_with_options(
        self,
        request: main_models.DeleteChatGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChatGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChatGroup',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChatGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chat_group_with_options_async(
        self,
        request: main_models.DeleteChatGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChatGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChatGroup',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChatGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chat_group(
        self,
        request: main_models.DeleteChatGroupRequest,
    ) -> main_models.DeleteChatGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_chat_group_with_options(request, runtime)

    async def delete_chat_group_async(
        self,
        request: main_models.DeleteChatGroupRequest,
    ) -> main_models.DeleteChatGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_chat_group_with_options_async(request, runtime)

    def delete_chat_group_invite_link_with_options(
        self,
        request: main_models.DeleteChatGroupInviteLinkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChatGroupInviteLinkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChatGroupInviteLink',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChatGroupInviteLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chat_group_invite_link_with_options_async(
        self,
        request: main_models.DeleteChatGroupInviteLinkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChatGroupInviteLinkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChatGroupInviteLink',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChatGroupInviteLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chat_group_invite_link(
        self,
        request: main_models.DeleteChatGroupInviteLinkRequest,
    ) -> main_models.DeleteChatGroupInviteLinkResponse:
        runtime = RuntimeOptions()
        return self.delete_chat_group_invite_link_with_options(request, runtime)

    async def delete_chat_group_invite_link_async(
        self,
        request: main_models.DeleteChatGroupInviteLinkRequest,
    ) -> main_models.DeleteChatGroupInviteLinkResponse:
        runtime = RuntimeOptions()
        return await self.delete_chat_group_invite_link_with_options_async(request, runtime)

    def delete_chat_group_participants_with_options(
        self,
        tmp_req: main_models.DeleteChatGroupParticipantsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChatGroupParticipantsResponse:
        tmp_req.validate()
        request = main_models.DeleteChatGroupParticipantsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list):
            request.list_shrink = Utils.array_to_string_with_specified_style(tmp_req.list, 'List', 'json')
        query = {}
        if not DaraCore.is_null(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.list_shrink):
            query['List'] = request.list_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChatGroupParticipants',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChatGroupParticipantsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chat_group_participants_with_options_async(
        self,
        tmp_req: main_models.DeleteChatGroupParticipantsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChatGroupParticipantsResponse:
        tmp_req.validate()
        request = main_models.DeleteChatGroupParticipantsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list):
            request.list_shrink = Utils.array_to_string_with_specified_style(tmp_req.list, 'List', 'json')
        query = {}
        if not DaraCore.is_null(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.list_shrink):
            query['List'] = request.list_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChatGroupParticipants',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChatGroupParticipantsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chat_group_participants(
        self,
        request: main_models.DeleteChatGroupParticipantsRequest,
    ) -> main_models.DeleteChatGroupParticipantsResponse:
        runtime = RuntimeOptions()
        return self.delete_chat_group_participants_with_options(request, runtime)

    async def delete_chat_group_participants_async(
        self,
        request: main_models.DeleteChatGroupParticipantsRequest,
    ) -> main_models.DeleteChatGroupParticipantsResponse:
        runtime = RuntimeOptions()
        return await self.delete_chat_group_participants_with_options_async(request, runtime)

    def delete_chatapp_template_with_options(
        self,
        request: main_models.DeleteChatappTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChatappTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not DaraCore.is_null(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChatappTemplate',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChatappTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chatapp_template_with_options_async(
        self,
        request: main_models.DeleteChatappTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChatappTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not DaraCore.is_null(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChatappTemplate',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChatappTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chatapp_template(
        self,
        request: main_models.DeleteChatappTemplateRequest,
    ) -> main_models.DeleteChatappTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_chatapp_template_with_options(request, runtime)

    async def delete_chatapp_template_async(
        self,
        request: main_models.DeleteChatappTemplateRequest,
    ) -> main_models.DeleteChatappTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_chatapp_template_with_options_async(request, runtime)

    def delete_contacts_with_options(
        self,
        tmp_req: main_models.DeleteContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactsResponse:
        tmp_req.validate()
        request = main_models.DeleteContactsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.contact_details):
            query['ContactDetails'] = request.contact_details
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContacts',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contacts_with_options_async(
        self,
        tmp_req: main_models.DeleteContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactsResponse:
        tmp_req.validate()
        request = main_models.DeleteContactsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.contact_details):
            query['ContactDetails'] = request.contact_details
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContacts',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contacts(
        self,
        request: main_models.DeleteContactsRequest,
    ) -> main_models.DeleteContactsResponse:
        runtime = RuntimeOptions()
        return self.delete_contacts_with_options(request, runtime)

    async def delete_contacts_async(
        self,
        request: main_models.DeleteContactsRequest,
    ) -> main_models.DeleteContactsResponse:
        runtime = RuntimeOptions()
        return await self.delete_contacts_with_options_async(request, runtime)

    def delete_contacts_by_ids_with_options(
        self,
        request: main_models.DeleteContactsByIdsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactsByIdsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contacts):
            query['Contacts'] = request.contacts
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContactsByIds',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactsByIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contacts_by_ids_with_options_async(
        self,
        request: main_models.DeleteContactsByIdsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactsByIdsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contacts):
            query['Contacts'] = request.contacts
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContactsByIds',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactsByIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contacts_by_ids(
        self,
        request: main_models.DeleteContactsByIdsRequest,
    ) -> main_models.DeleteContactsByIdsResponse:
        runtime = RuntimeOptions()
        return self.delete_contacts_by_ids_with_options(request, runtime)

    async def delete_contacts_by_ids_async(
        self,
        request: main_models.DeleteContactsByIdsRequest,
    ) -> main_models.DeleteContactsByIdsResponse:
        runtime = RuntimeOptions()
        return await self.delete_contacts_by_ids_with_options_async(request, runtime)

    def delete_flow_with_options(
        self,
        request: main_models.DeleteFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_with_options_async(
        self,
        request: main_models.DeleteFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow(
        self,
        request: main_models.DeleteFlowRequest,
    ) -> main_models.DeleteFlowResponse:
        runtime = RuntimeOptions()
        return self.delete_flow_with_options(request, runtime)

    async def delete_flow_async(
        self,
        request: main_models.DeleteFlowRequest,
    ) -> main_models.DeleteFlowResponse:
        runtime = RuntimeOptions()
        return await self.delete_flow_with_options_async(request, runtime)

    def delete_flow_version_with_options(
        self,
        tmp_req: main_models.DeleteFlowVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlowVersionResponse:
        tmp_req.validate()
        request = main_models.DeleteFlowVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlowVersion',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlowVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_version_with_options_async(
        self,
        tmp_req: main_models.DeleteFlowVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlowVersionResponse:
        tmp_req.validate()
        request = main_models.DeleteFlowVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlowVersion',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlowVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flow_version(
        self,
        request: main_models.DeleteFlowVersionRequest,
    ) -> main_models.DeleteFlowVersionResponse:
        runtime = RuntimeOptions()
        return self.delete_flow_version_with_options(request, runtime)

    async def delete_flow_version_async(
        self,
        request: main_models.DeleteFlowVersionRequest,
    ) -> main_models.DeleteFlowVersionResponse:
        runtime = RuntimeOptions()
        return await self.delete_flow_version_with_options_async(request, runtime)

    def delete_group_by_id_with_options(
        self,
        request: main_models.DeleteGroupByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGroupByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGroupById',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGroupByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_by_id_with_options_async(
        self,
        request: main_models.DeleteGroupByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGroupByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGroupById',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGroupByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group_by_id(
        self,
        request: main_models.DeleteGroupByIdRequest,
    ) -> main_models.DeleteGroupByIdResponse:
        runtime = RuntimeOptions()
        return self.delete_group_by_id_with_options(request, runtime)

    async def delete_group_by_id_async(
        self,
        request: main_models.DeleteGroupByIdRequest,
    ) -> main_models.DeleteGroupByIdResponse:
        runtime = RuntimeOptions()
        return await self.delete_group_by_id_with_options_async(request, runtime)

    def delete_instagram_page_with_options(
        self,
        request: main_models.DeleteInstagramPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstagramPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstagramPage',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstagramPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instagram_page_with_options_async(
        self,
        request: main_models.DeleteInstagramPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstagramPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstagramPage',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstagramPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instagram_page(
        self,
        request: main_models.DeleteInstagramPageRequest,
    ) -> main_models.DeleteInstagramPageResponse:
        runtime = RuntimeOptions()
        return self.delete_instagram_page_with_options(request, runtime)

    async def delete_instagram_page_async(
        self,
        request: main_models.DeleteInstagramPageRequest,
    ) -> main_models.DeleteInstagramPageResponse:
        runtime = RuntimeOptions()
        return await self.delete_instagram_page_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2020-06-06',
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
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2020-06-06',
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

    def delete_marketing_flow_with_options(
        self,
        request: main_models.DeleteMarketingFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMarketingFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_code):
            query['ActivityCode'] = request.activity_code
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMarketingFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMarketingFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_marketing_flow_with_options_async(
        self,
        request: main_models.DeleteMarketingFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMarketingFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_code):
            query['ActivityCode'] = request.activity_code
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMarketingFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMarketingFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_marketing_flow(
        self,
        request: main_models.DeleteMarketingFlowRequest,
    ) -> main_models.DeleteMarketingFlowResponse:
        runtime = RuntimeOptions()
        return self.delete_marketing_flow_with_options(request, runtime)

    async def delete_marketing_flow_async(
        self,
        request: main_models.DeleteMarketingFlowRequest,
    ) -> main_models.DeleteMarketingFlowResponse:
        runtime = RuntimeOptions()
        return await self.delete_marketing_flow_with_options_async(request, runtime)

    def delete_message_campaign_with_options(
        self,
        request: main_models.DeleteMessageCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMessageCampaignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ad_account_id):
            query['AdAccountId'] = request.ad_account_id
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMessageCampaign',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMessageCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_message_campaign_with_options_async(
        self,
        request: main_models.DeleteMessageCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMessageCampaignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ad_account_id):
            query['AdAccountId'] = request.ad_account_id
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMessageCampaign',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMessageCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_message_campaign(
        self,
        request: main_models.DeleteMessageCampaignRequest,
    ) -> main_models.DeleteMessageCampaignResponse:
        runtime = RuntimeOptions()
        return self.delete_message_campaign_with_options(request, runtime)

    async def delete_message_campaign_async(
        self,
        request: main_models.DeleteMessageCampaignRequest,
    ) -> main_models.DeleteMessageCampaignResponse:
        runtime = RuntimeOptions()
        return await self.delete_message_campaign_with_options_async(request, runtime)

    def delete_messenger_page_with_options(
        self,
        request: main_models.DeleteMessengerPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMessengerPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMessengerPage',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMessengerPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_messenger_page_with_options_async(
        self,
        request: main_models.DeleteMessengerPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMessengerPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMessengerPage',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMessengerPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_messenger_page(
        self,
        request: main_models.DeleteMessengerPageRequest,
    ) -> main_models.DeleteMessengerPageResponse:
        runtime = RuntimeOptions()
        return self.delete_messenger_page_with_options(request, runtime)

    async def delete_messenger_page_async(
        self,
        request: main_models.DeleteMessengerPageRequest,
    ) -> main_models.DeleteMessengerPageResponse:
        runtime = RuntimeOptions()
        return await self.delete_messenger_page_with_options_async(request, runtime)

    def delete_phone_message_qrdl_with_options(
        self,
        request: main_models.DeletePhoneMessageQrdlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePhoneMessageQrdlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.qrdl_code):
            query['QrdlCode'] = request.qrdl_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePhoneMessageQrdl',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePhoneMessageQrdlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_phone_message_qrdl_with_options_async(
        self,
        request: main_models.DeletePhoneMessageQrdlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePhoneMessageQrdlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.qrdl_code):
            query['QrdlCode'] = request.qrdl_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePhoneMessageQrdl',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePhoneMessageQrdlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_phone_message_qrdl(
        self,
        request: main_models.DeletePhoneMessageQrdlRequest,
    ) -> main_models.DeletePhoneMessageQrdlResponse:
        runtime = RuntimeOptions()
        return self.delete_phone_message_qrdl_with_options(request, runtime)

    async def delete_phone_message_qrdl_async(
        self,
        request: main_models.DeletePhoneMessageQrdlRequest,
    ) -> main_models.DeletePhoneMessageQrdlResponse:
        runtime = RuntimeOptions()
        return await self.delete_phone_message_qrdl_with_options_async(request, runtime)

    def deprecate_flow_with_options(
        self,
        request: main_models.DeprecateFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeprecateFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeprecateFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeprecateFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def deprecate_flow_with_options_async(
        self,
        request: main_models.DeprecateFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeprecateFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeprecateFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeprecateFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deprecate_flow(
        self,
        request: main_models.DeprecateFlowRequest,
    ) -> main_models.DeprecateFlowResponse:
        runtime = RuntimeOptions()
        return self.deprecate_flow_with_options(request, runtime)

    async def deprecate_flow_async(
        self,
        request: main_models.DeprecateFlowRequest,
    ) -> main_models.DeprecateFlowResponse:
        runtime = RuntimeOptions()
        return await self.deprecate_flow_with_options_async(request, runtime)

    def enable_whatsapp_roimetric_with_options(
        self,
        request: main_models.EnableWhatsappROIMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableWhatsappROIMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableWhatsappROIMetric',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableWhatsappROIMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_whatsapp_roimetric_with_options_async(
        self,
        request: main_models.EnableWhatsappROIMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableWhatsappROIMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableWhatsappROIMetric',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableWhatsappROIMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_whatsapp_roimetric(
        self,
        request: main_models.EnableWhatsappROIMetricRequest,
    ) -> main_models.EnableWhatsappROIMetricResponse:
        runtime = RuntimeOptions()
        return self.enable_whatsapp_roimetric_with_options(request, runtime)

    async def enable_whatsapp_roimetric_async(
        self,
        request: main_models.EnableWhatsappROIMetricRequest,
    ) -> main_models.EnableWhatsappROIMetricResponse:
        runtime = RuntimeOptions()
        return await self.enable_whatsapp_roimetric_with_options_async(request, runtime)

    def flow_bind_phone_with_options(
        self,
        tmp_req: main_models.FlowBindPhoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FlowBindPhoneResponse:
        tmp_req.validate()
        request = main_models.FlowBindPhoneShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.phone_numbers):
            request.phone_numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.phone_numbers, 'PhoneNumbers', 'json')
        query = {}
        if not DaraCore.is_null(request.channel_code):
            query['ChannelCode'] = request.channel_code
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_numbers_shrink):
            query['PhoneNumbers'] = request.phone_numbers_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FlowBindPhone',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FlowBindPhoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def flow_bind_phone_with_options_async(
        self,
        tmp_req: main_models.FlowBindPhoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FlowBindPhoneResponse:
        tmp_req.validate()
        request = main_models.FlowBindPhoneShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.phone_numbers):
            request.phone_numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.phone_numbers, 'PhoneNumbers', 'json')
        query = {}
        if not DaraCore.is_null(request.channel_code):
            query['ChannelCode'] = request.channel_code
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_numbers_shrink):
            query['PhoneNumbers'] = request.phone_numbers_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FlowBindPhone',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FlowBindPhoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flow_bind_phone(
        self,
        request: main_models.FlowBindPhoneRequest,
    ) -> main_models.FlowBindPhoneResponse:
        runtime = RuntimeOptions()
        return self.flow_bind_phone_with_options(request, runtime)

    async def flow_bind_phone_async(
        self,
        request: main_models.FlowBindPhoneRequest,
    ) -> main_models.FlowBindPhoneResponse:
        runtime = RuntimeOptions()
        return await self.flow_bind_phone_with_options_async(request, runtime)

    def flow_rebind_phone_with_options(
        self,
        tmp_req: main_models.FlowRebindPhoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FlowRebindPhoneResponse:
        tmp_req.validate()
        request = main_models.FlowRebindPhoneShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.phone_numbers):
            request.phone_numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.phone_numbers, 'PhoneNumbers', 'json')
        query = {}
        if not DaraCore.is_null(request.channel_code):
            query['ChannelCode'] = request.channel_code
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_numbers_shrink):
            query['PhoneNumbers'] = request.phone_numbers_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FlowRebindPhone',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FlowRebindPhoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def flow_rebind_phone_with_options_async(
        self,
        tmp_req: main_models.FlowRebindPhoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FlowRebindPhoneResponse:
        tmp_req.validate()
        request = main_models.FlowRebindPhoneShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.phone_numbers):
            request.phone_numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.phone_numbers, 'PhoneNumbers', 'json')
        query = {}
        if not DaraCore.is_null(request.channel_code):
            query['ChannelCode'] = request.channel_code
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_numbers_shrink):
            query['PhoneNumbers'] = request.phone_numbers_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FlowRebindPhone',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FlowRebindPhoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flow_rebind_phone(
        self,
        request: main_models.FlowRebindPhoneRequest,
    ) -> main_models.FlowRebindPhoneResponse:
        runtime = RuntimeOptions()
        return self.flow_rebind_phone_with_options(request, runtime)

    async def flow_rebind_phone_async(
        self,
        request: main_models.FlowRebindPhoneRequest,
    ) -> main_models.FlowRebindPhoneResponse:
        runtime = RuntimeOptions()
        return await self.flow_rebind_phone_with_options_async(request, runtime)

    def flow_unbind_phone_with_options(
        self,
        tmp_req: main_models.FlowUnbindPhoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FlowUnbindPhoneResponse:
        tmp_req.validate()
        request = main_models.FlowUnbindPhoneShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.phone_numbers):
            request.phone_numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.phone_numbers, 'PhoneNumbers', 'json')
        query = {}
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_numbers_shrink):
            query['PhoneNumbers'] = request.phone_numbers_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FlowUnbindPhone',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FlowUnbindPhoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def flow_unbind_phone_with_options_async(
        self,
        tmp_req: main_models.FlowUnbindPhoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FlowUnbindPhoneResponse:
        tmp_req.validate()
        request = main_models.FlowUnbindPhoneShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.phone_numbers):
            request.phone_numbers_shrink = Utils.array_to_string_with_specified_style(tmp_req.phone_numbers, 'PhoneNumbers', 'json')
        query = {}
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_numbers_shrink):
            query['PhoneNumbers'] = request.phone_numbers_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FlowUnbindPhone',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FlowUnbindPhoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flow_unbind_phone(
        self,
        request: main_models.FlowUnbindPhoneRequest,
    ) -> main_models.FlowUnbindPhoneResponse:
        runtime = RuntimeOptions()
        return self.flow_unbind_phone_with_options(request, runtime)

    async def flow_unbind_phone_async(
        self,
        request: main_models.FlowUnbindPhoneRequest,
    ) -> main_models.FlowUnbindPhoneResponse:
        runtime = RuntimeOptions()
        return await self.flow_unbind_phone_with_options_async(request, runtime)

    def generate_presigned_url_with_options(
        self,
        request: main_models.GeneratePresignedUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GeneratePresignedUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GeneratePresignedUrl',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GeneratePresignedUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_presigned_url_with_options_async(
        self,
        request: main_models.GeneratePresignedUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GeneratePresignedUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GeneratePresignedUrl',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GeneratePresignedUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_presigned_url(
        self,
        request: main_models.GeneratePresignedUrlRequest,
    ) -> main_models.GeneratePresignedUrlResponse:
        runtime = RuntimeOptions()
        return self.generate_presigned_url_with_options(request, runtime)

    async def generate_presigned_url_async(
        self,
        request: main_models.GeneratePresignedUrlRequest,
    ) -> main_models.GeneratePresignedUrlResponse:
        runtime = RuntimeOptions()
        return await self.generate_presigned_url_with_options_async(request, runtime)

    def get_audit_request_by_type_un_audit_with_options(
        self,
        request: main_models.GetAuditRequestByTypeUnAuditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAuditRequestByTypeUnAuditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.request_type):
            query['RequestType'] = request.request_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAuditRequestByTypeUnAudit',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAuditRequestByTypeUnAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_audit_request_by_type_un_audit_with_options_async(
        self,
        request: main_models.GetAuditRequestByTypeUnAuditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAuditRequestByTypeUnAuditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.request_type):
            query['RequestType'] = request.request_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAuditRequestByTypeUnAudit',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAuditRequestByTypeUnAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_audit_request_by_type_un_audit(
        self,
        request: main_models.GetAuditRequestByTypeUnAuditRequest,
    ) -> main_models.GetAuditRequestByTypeUnAuditResponse:
        runtime = RuntimeOptions()
        return self.get_audit_request_by_type_un_audit_with_options(request, runtime)

    async def get_audit_request_by_type_un_audit_async(
        self,
        request: main_models.GetAuditRequestByTypeUnAuditRequest,
    ) -> main_models.GetAuditRequestByTypeUnAuditResponse:
        runtime = RuntimeOptions()
        return await self.get_audit_request_by_type_un_audit_with_options_async(request, runtime)

    def get_chat_flow_metric_with_options(
        self,
        tmp_req: main_models.GetChatFlowMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatFlowMetricResponse:
        tmp_req.validate()
        request = main_models.GetChatFlowMetricShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        if not DaraCore.is_null(tmp_req.metric_param):
            request.metric_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.metric_param, 'MetricParam', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.metric_param_shrink):
            query['MetricParam'] = request.metric_param_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.to):
            query['To'] = request.to
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatFlowMetric',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatFlowMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chat_flow_metric_with_options_async(
        self,
        tmp_req: main_models.GetChatFlowMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatFlowMetricResponse:
        tmp_req.validate()
        request = main_models.GetChatFlowMetricShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        if not DaraCore.is_null(tmp_req.metric_param):
            request.metric_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.metric_param, 'MetricParam', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.metric_param_shrink):
            query['MetricParam'] = request.metric_param_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.to):
            query['To'] = request.to
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatFlowMetric',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatFlowMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chat_flow_metric(
        self,
        request: main_models.GetChatFlowMetricRequest,
    ) -> main_models.GetChatFlowMetricResponse:
        runtime = RuntimeOptions()
        return self.get_chat_flow_metric_with_options(request, runtime)

    async def get_chat_flow_metric_async(
        self,
        request: main_models.GetChatFlowMetricRequest,
    ) -> main_models.GetChatFlowMetricResponse:
        runtime = RuntimeOptions()
        return await self.get_chat_flow_metric_with_options_async(request, runtime)

    def get_chat_flow_template_with_options(
        self,
        request: main_models.GetChatFlowTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatFlowTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatFlowTemplate',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatFlowTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chat_flow_template_with_options_async(
        self,
        request: main_models.GetChatFlowTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatFlowTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatFlowTemplate',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatFlowTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chat_flow_template(
        self,
        request: main_models.GetChatFlowTemplateRequest,
    ) -> main_models.GetChatFlowTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_chat_flow_template_with_options(request, runtime)

    async def get_chat_flow_template_async(
        self,
        request: main_models.GetChatFlowTemplateRequest,
    ) -> main_models.GetChatFlowTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_chat_flow_template_with_options_async(request, runtime)

    def get_chatapp_open_status_with_options(
        self,
        request: main_models.GetChatappOpenStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatappOpenStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatappOpenStatus',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatappOpenStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chatapp_open_status_with_options_async(
        self,
        request: main_models.GetChatappOpenStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatappOpenStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatappOpenStatus',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatappOpenStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chatapp_open_status(
        self,
        request: main_models.GetChatappOpenStatusRequest,
    ) -> main_models.GetChatappOpenStatusResponse:
        runtime = RuntimeOptions()
        return self.get_chatapp_open_status_with_options(request, runtime)

    async def get_chatapp_open_status_async(
        self,
        request: main_models.GetChatappOpenStatusRequest,
    ) -> main_models.GetChatappOpenStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_chatapp_open_status_with_options_async(request, runtime)

    def get_chatapp_phone_number_metric_with_options(
        self,
        request: main_models.GetChatappPhoneNumberMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatappPhoneNumberMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatappPhoneNumberMetric',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatappPhoneNumberMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chatapp_phone_number_metric_with_options_async(
        self,
        request: main_models.GetChatappPhoneNumberMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatappPhoneNumberMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatappPhoneNumberMetric',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatappPhoneNumberMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chatapp_phone_number_metric(
        self,
        request: main_models.GetChatappPhoneNumberMetricRequest,
    ) -> main_models.GetChatappPhoneNumberMetricResponse:
        runtime = RuntimeOptions()
        return self.get_chatapp_phone_number_metric_with_options(request, runtime)

    async def get_chatapp_phone_number_metric_async(
        self,
        request: main_models.GetChatappPhoneNumberMetricRequest,
    ) -> main_models.GetChatappPhoneNumberMetricResponse:
        runtime = RuntimeOptions()
        return await self.get_chatapp_phone_number_metric_with_options_async(request, runtime)

    def get_chatapp_phone_number_setting_with_options(
        self,
        request: main_models.GetChatappPhoneNumberSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatappPhoneNumberSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatappPhoneNumberSetting',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatappPhoneNumberSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chatapp_phone_number_setting_with_options_async(
        self,
        request: main_models.GetChatappPhoneNumberSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatappPhoneNumberSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatappPhoneNumberSetting',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatappPhoneNumberSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chatapp_phone_number_setting(
        self,
        request: main_models.GetChatappPhoneNumberSettingRequest,
    ) -> main_models.GetChatappPhoneNumberSettingResponse:
        runtime = RuntimeOptions()
        return self.get_chatapp_phone_number_setting_with_options(request, runtime)

    async def get_chatapp_phone_number_setting_async(
        self,
        request: main_models.GetChatappPhoneNumberSettingRequest,
    ) -> main_models.GetChatappPhoneNumberSettingResponse:
        runtime = RuntimeOptions()
        return await self.get_chatapp_phone_number_setting_with_options_async(request, runtime)

    def get_chatapp_template_detail_with_options(
        self,
        request: main_models.GetChatappTemplateDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatappTemplateDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not DaraCore.is_null(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatappTemplateDetail',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatappTemplateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chatapp_template_detail_with_options_async(
        self,
        request: main_models.GetChatappTemplateDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatappTemplateDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not DaraCore.is_null(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatappTemplateDetail',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatappTemplateDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chatapp_template_detail(
        self,
        request: main_models.GetChatappTemplateDetailRequest,
    ) -> main_models.GetChatappTemplateDetailResponse:
        runtime = RuntimeOptions()
        return self.get_chatapp_template_detail_with_options(request, runtime)

    async def get_chatapp_template_detail_async(
        self,
        request: main_models.GetChatappTemplateDetailRequest,
    ) -> main_models.GetChatappTemplateDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_chatapp_template_detail_with_options_async(request, runtime)

    def get_chatapp_template_metric_with_options(
        self,
        request: main_models.GetChatappTemplateMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatappTemplateMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatappTemplateMetric',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatappTemplateMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chatapp_template_metric_with_options_async(
        self,
        request: main_models.GetChatappTemplateMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatappTemplateMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatappTemplateMetric',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatappTemplateMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chatapp_template_metric(
        self,
        request: main_models.GetChatappTemplateMetricRequest,
    ) -> main_models.GetChatappTemplateMetricResponse:
        runtime = RuntimeOptions()
        return self.get_chatapp_template_metric_with_options(request, runtime)

    async def get_chatapp_template_metric_async(
        self,
        request: main_models.GetChatappTemplateMetricRequest,
    ) -> main_models.GetChatappTemplateMetricResponse:
        runtime = RuntimeOptions()
        return await self.get_chatapp_template_metric_with_options_async(request, runtime)

    def get_chatapp_upload_authorization_with_options(
        self,
        request: main_models.GetChatappUploadAuthorizationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatappUploadAuthorizationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatappUploadAuthorization',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatappUploadAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chatapp_upload_authorization_with_options_async(
        self,
        request: main_models.GetChatappUploadAuthorizationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatappUploadAuthorizationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatappUploadAuthorization',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatappUploadAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chatapp_upload_authorization(
        self,
        request: main_models.GetChatappUploadAuthorizationRequest,
    ) -> main_models.GetChatappUploadAuthorizationResponse:
        runtime = RuntimeOptions()
        return self.get_chatapp_upload_authorization_with_options(request, runtime)

    async def get_chatapp_upload_authorization_async(
        self,
        request: main_models.GetChatappUploadAuthorizationRequest,
    ) -> main_models.GetChatappUploadAuthorizationResponse:
        runtime = RuntimeOptions()
        return await self.get_chatapp_upload_authorization_with_options_async(request, runtime)

    def get_chatapp_verify_code_with_options(
        self,
        request: main_models.GetChatappVerifyCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatappVerifyCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.locale):
            query['Locale'] = request.locale
        if not DaraCore.is_null(request.method):
            query['Method'] = request.method
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatappVerifyCode',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatappVerifyCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chatapp_verify_code_with_options_async(
        self,
        request: main_models.GetChatappVerifyCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatappVerifyCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.locale):
            query['Locale'] = request.locale
        if not DaraCore.is_null(request.method):
            query['Method'] = request.method
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatappVerifyCode',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatappVerifyCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chatapp_verify_code(
        self,
        request: main_models.GetChatappVerifyCodeRequest,
    ) -> main_models.GetChatappVerifyCodeResponse:
        runtime = RuntimeOptions()
        return self.get_chatapp_verify_code_with_options(request, runtime)

    async def get_chatapp_verify_code_async(
        self,
        request: main_models.GetChatappVerifyCodeRequest,
    ) -> main_models.GetChatappVerifyCodeResponse:
        runtime = RuntimeOptions()
        return await self.get_chatapp_verify_code_with_options_async(request, runtime)

    def get_commerce_setting_with_options(
        self,
        request: main_models.GetCommerceSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCommerceSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCommerceSetting',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCommerceSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_commerce_setting_with_options_async(
        self,
        request: main_models.GetCommerceSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCommerceSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCommerceSetting',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCommerceSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_commerce_setting(
        self,
        request: main_models.GetCommerceSettingRequest,
    ) -> main_models.GetCommerceSettingResponse:
        runtime = RuntimeOptions()
        return self.get_commerce_setting_with_options(request, runtime)

    async def get_commerce_setting_async(
        self,
        request: main_models.GetCommerceSettingRequest,
    ) -> main_models.GetCommerceSettingResponse:
        runtime = RuntimeOptions()
        return await self.get_commerce_setting_with_options_async(request, runtime)

    def get_conversational_automation_with_options(
        self,
        request: main_models.GetConversationalAutomationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConversationalAutomationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConversationalAutomation',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConversationalAutomationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_conversational_automation_with_options_async(
        self,
        request: main_models.GetConversationalAutomationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConversationalAutomationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConversationalAutomation',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConversationalAutomationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_conversational_automation(
        self,
        request: main_models.GetConversationalAutomationRequest,
    ) -> main_models.GetConversationalAutomationResponse:
        runtime = RuntimeOptions()
        return self.get_conversational_automation_with_options(request, runtime)

    async def get_conversational_automation_async(
        self,
        request: main_models.GetConversationalAutomationRequest,
    ) -> main_models.GetConversationalAutomationResponse:
        runtime = RuntimeOptions()
        return await self.get_conversational_automation_with_options_async(request, runtime)

    def get_customer_site_with_options(
        self,
        request: main_models.GetCustomerSiteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomerSiteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomerSite',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomerSiteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_customer_site_with_options_async(
        self,
        request: main_models.GetCustomerSiteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomerSiteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomerSite',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomerSiteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_customer_site(
        self,
        request: main_models.GetCustomerSiteRequest,
    ) -> main_models.GetCustomerSiteResponse:
        runtime = RuntimeOptions()
        return self.get_customer_site_with_options(request, runtime)

    async def get_customer_site_async(
        self,
        request: main_models.GetCustomerSiteRequest,
    ) -> main_models.GetCustomerSiteResponse:
        runtime = RuntimeOptions()
        return await self.get_customer_site_with_options_async(request, runtime)

    def get_download_excel_list_with_options(
        self,
        tmp_req: main_models.GetDownloadExcelListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDownloadExcelListResponse:
        tmp_req.validate()
        request = main_models.GetDownloadExcelListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        if not DaraCore.is_null(tmp_req.country_names):
            request.country_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.country_names, 'CountryNames', 'json')
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.condition):
            query['Condition'] = request.condition
        if not DaraCore.is_null(request.country_names_shrink):
            query['CountryNames'] = request.country_names_shrink
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_ids_shrink):
            query['GroupIds'] = request.group_ids_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDownloadExcelList',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDownloadExcelListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_download_excel_list_with_options_async(
        self,
        tmp_req: main_models.GetDownloadExcelListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDownloadExcelListResponse:
        tmp_req.validate()
        request = main_models.GetDownloadExcelListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        if not DaraCore.is_null(tmp_req.country_names):
            request.country_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.country_names, 'CountryNames', 'json')
        if not DaraCore.is_null(tmp_req.group_ids):
            request.group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.condition):
            query['Condition'] = request.condition
        if not DaraCore.is_null(request.country_names_shrink):
            query['CountryNames'] = request.country_names_shrink
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_ids_shrink):
            query['GroupIds'] = request.group_ids_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDownloadExcelList',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDownloadExcelListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_download_excel_list(
        self,
        request: main_models.GetDownloadExcelListRequest,
    ) -> main_models.GetDownloadExcelListResponse:
        runtime = RuntimeOptions()
        return self.get_download_excel_list_with_options(request, runtime)

    async def get_download_excel_list_async(
        self,
        request: main_models.GetDownloadExcelListRequest,
    ) -> main_models.GetDownloadExcelListResponse:
        runtime = RuntimeOptions()
        return await self.get_download_excel_list_with_options_async(request, runtime)

    def get_fb_instagram_pages_with_options(
        self,
        request: main_models.GetFbInstagramPagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFbInstagramPagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_token):
            query['AccessToken'] = request.access_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFbInstagramPages',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFbInstagramPagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fb_instagram_pages_with_options_async(
        self,
        request: main_models.GetFbInstagramPagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFbInstagramPagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_token):
            query['AccessToken'] = request.access_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFbInstagramPages',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFbInstagramPagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fb_instagram_pages(
        self,
        request: main_models.GetFbInstagramPagesRequest,
    ) -> main_models.GetFbInstagramPagesResponse:
        runtime = RuntimeOptions()
        return self.get_fb_instagram_pages_with_options(request, runtime)

    async def get_fb_instagram_pages_async(
        self,
        request: main_models.GetFbInstagramPagesRequest,
    ) -> main_models.GetFbInstagramPagesResponse:
        runtime = RuntimeOptions()
        return await self.get_fb_instagram_pages_with_options_async(request, runtime)

    def get_fb_messenger_pages_with_options(
        self,
        request: main_models.GetFbMessengerPagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFbMessengerPagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_token):
            query['AccessToken'] = request.access_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFbMessengerPages',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFbMessengerPagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fb_messenger_pages_with_options_async(
        self,
        request: main_models.GetFbMessengerPagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFbMessengerPagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_token):
            query['AccessToken'] = request.access_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFbMessengerPages',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFbMessengerPagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fb_messenger_pages(
        self,
        request: main_models.GetFbMessengerPagesRequest,
    ) -> main_models.GetFbMessengerPagesResponse:
        runtime = RuntimeOptions()
        return self.get_fb_messenger_pages_with_options(request, runtime)

    async def get_fb_messenger_pages_async(
        self,
        request: main_models.GetFbMessengerPagesRequest,
    ) -> main_models.GetFbMessengerPagesResponse:
        runtime = RuntimeOptions()
        return await self.get_fb_messenger_pages_with_options_async(request, runtime)

    def get_flow_with_options(
        self,
        request: main_models.GetFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_flow_with_options_async(
        self,
        request: main_models.GetFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_flow(
        self,
        request: main_models.GetFlowRequest,
    ) -> main_models.GetFlowResponse:
        runtime = RuntimeOptions()
        return self.get_flow_with_options(request, runtime)

    async def get_flow_async(
        self,
        request: main_models.GetFlowRequest,
    ) -> main_models.GetFlowResponse:
        runtime = RuntimeOptions()
        return await self.get_flow_with_options_async(request, runtime)

    def get_flow_jsonassest_with_options(
        self,
        request: main_models.GetFlowJSONAssestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFlowJSONAssestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFlowJSONAssest',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFlowJSONAssestResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_flow_jsonassest_with_options_async(
        self,
        request: main_models.GetFlowJSONAssestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFlowJSONAssestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFlowJSONAssest',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFlowJSONAssestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_flow_jsonassest(
        self,
        request: main_models.GetFlowJSONAssestRequest,
    ) -> main_models.GetFlowJSONAssestResponse:
        runtime = RuntimeOptions()
        return self.get_flow_jsonassest_with_options(request, runtime)

    async def get_flow_jsonassest_async(
        self,
        request: main_models.GetFlowJSONAssestRequest,
    ) -> main_models.GetFlowJSONAssestResponse:
        runtime = RuntimeOptions()
        return await self.get_flow_jsonassest_with_options_async(request, runtime)

    def get_flow_preview_url_with_options(
        self,
        request: main_models.GetFlowPreviewUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFlowPreviewUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFlowPreviewUrl',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFlowPreviewUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_flow_preview_url_with_options_async(
        self,
        request: main_models.GetFlowPreviewUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFlowPreviewUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFlowPreviewUrl',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFlowPreviewUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_flow_preview_url(
        self,
        request: main_models.GetFlowPreviewUrlRequest,
    ) -> main_models.GetFlowPreviewUrlResponse:
        runtime = RuntimeOptions()
        return self.get_flow_preview_url_with_options(request, runtime)

    async def get_flow_preview_url_async(
        self,
        request: main_models.GetFlowPreviewUrlRequest,
    ) -> main_models.GetFlowPreviewUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_flow_preview_url_with_options_async(request, runtime)

    def get_group_exist_with_options(
        self,
        tmp_req: main_models.GetGroupExistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGroupExistResponse:
        tmp_req.validate()
        request = main_models.GetGroupExistShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGroupExist',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGroupExistResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_group_exist_with_options_async(
        self,
        tmp_req: main_models.GetGroupExistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGroupExistResponse:
        tmp_req.validate()
        request = main_models.GetGroupExistShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGroupExist',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGroupExistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_group_exist(
        self,
        request: main_models.GetGroupExistRequest,
    ) -> main_models.GetGroupExistResponse:
        runtime = RuntimeOptions()
        return self.get_group_exist_with_options(request, runtime)

    async def get_group_exist_async(
        self,
        request: main_models.GetGroupExistRequest,
    ) -> main_models.GetGroupExistResponse:
        runtime = RuntimeOptions()
        return await self.get_group_exist_with_options_async(request, runtime)

    def get_message_campaign_insights_with_options(
        self,
        request: main_models.GetMessageCampaignInsightsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMessageCampaignInsightsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ad_account_id):
            query['AdAccountId'] = request.ad_account_id
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMessageCampaignInsights',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMessageCampaignInsightsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_message_campaign_insights_with_options_async(
        self,
        request: main_models.GetMessageCampaignInsightsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMessageCampaignInsightsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ad_account_id):
            query['AdAccountId'] = request.ad_account_id
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMessageCampaignInsights',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMessageCampaignInsightsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_message_campaign_insights(
        self,
        request: main_models.GetMessageCampaignInsightsRequest,
    ) -> main_models.GetMessageCampaignInsightsResponse:
        runtime = RuntimeOptions()
        return self.get_message_campaign_insights_with_options(request, runtime)

    async def get_message_campaign_insights_async(
        self,
        request: main_models.GetMessageCampaignInsightsRequest,
    ) -> main_models.GetMessageCampaignInsightsResponse:
        runtime = RuntimeOptions()
        return await self.get_message_campaign_insights_with_options_async(request, runtime)

    def get_migration_verify_code_with_options(
        self,
        request: main_models.GetMigrationVerifyCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMigrationVerifyCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.locale):
            query['Locale'] = request.locale
        if not DaraCore.is_null(request.method):
            query['Method'] = request.method
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMigrationVerifyCode',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMigrationVerifyCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_migration_verify_code_with_options_async(
        self,
        request: main_models.GetMigrationVerifyCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMigrationVerifyCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.locale):
            query['Locale'] = request.locale
        if not DaraCore.is_null(request.method):
            query['Method'] = request.method
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMigrationVerifyCode',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMigrationVerifyCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_migration_verify_code(
        self,
        request: main_models.GetMigrationVerifyCodeRequest,
    ) -> main_models.GetMigrationVerifyCodeResponse:
        runtime = RuntimeOptions()
        return self.get_migration_verify_code_with_options(request, runtime)

    async def get_migration_verify_code_async(
        self,
        request: main_models.GetMigrationVerifyCodeRequest,
    ) -> main_models.GetMigrationVerifyCodeResponse:
        runtime = RuntimeOptions()
        return await self.get_migration_verify_code_with_options_async(request, runtime)

    def get_permission_by_code_with_options(
        self,
        tmp_req: main_models.GetPermissionByCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPermissionByCodeResponse:
        tmp_req.validate()
        request = main_models.GetPermissionByCodeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.permissions):
            request.permissions_shrink = Utils.array_to_string_with_specified_style(tmp_req.permissions, 'Permissions', 'json')
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.permissions_shrink):
            query['Permissions'] = request.permissions_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPermissionByCode',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPermissionByCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_permission_by_code_with_options_async(
        self,
        tmp_req: main_models.GetPermissionByCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPermissionByCodeResponse:
        tmp_req.validate()
        request = main_models.GetPermissionByCodeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.permissions):
            request.permissions_shrink = Utils.array_to_string_with_specified_style(tmp_req.permissions, 'Permissions', 'json')
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.permissions_shrink):
            query['Permissions'] = request.permissions_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPermissionByCode',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPermissionByCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_permission_by_code(
        self,
        request: main_models.GetPermissionByCodeRequest,
    ) -> main_models.GetPermissionByCodeResponse:
        runtime = RuntimeOptions()
        return self.get_permission_by_code_with_options(request, runtime)

    async def get_permission_by_code_async(
        self,
        request: main_models.GetPermissionByCodeRequest,
    ) -> main_models.GetPermissionByCodeResponse:
        runtime = RuntimeOptions()
        return await self.get_permission_by_code_with_options_async(request, runtime)

    def get_phone_encryption_public_key_with_options(
        self,
        request: main_models.GetPhoneEncryptionPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhoneEncryptionPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhoneEncryptionPublicKey',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhoneEncryptionPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_phone_encryption_public_key_with_options_async(
        self,
        request: main_models.GetPhoneEncryptionPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhoneEncryptionPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhoneEncryptionPublicKey',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhoneEncryptionPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_phone_encryption_public_key(
        self,
        request: main_models.GetPhoneEncryptionPublicKeyRequest,
    ) -> main_models.GetPhoneEncryptionPublicKeyResponse:
        runtime = RuntimeOptions()
        return self.get_phone_encryption_public_key_with_options(request, runtime)

    async def get_phone_encryption_public_key_async(
        self,
        request: main_models.GetPhoneEncryptionPublicKeyRequest,
    ) -> main_models.GetPhoneEncryptionPublicKeyResponse:
        runtime = RuntimeOptions()
        return await self.get_phone_encryption_public_key_with_options_async(request, runtime)

    def get_phone_number_verification_status_with_options(
        self,
        request: main_models.GetPhoneNumberVerificationStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhoneNumberVerificationStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhoneNumberVerificationStatus',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhoneNumberVerificationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_phone_number_verification_status_with_options_async(
        self,
        request: main_models.GetPhoneNumberVerificationStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhoneNumberVerificationStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhoneNumberVerificationStatus',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhoneNumberVerificationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_phone_number_verification_status(
        self,
        request: main_models.GetPhoneNumberVerificationStatusRequest,
    ) -> main_models.GetPhoneNumberVerificationStatusResponse:
        runtime = RuntimeOptions()
        return self.get_phone_number_verification_status_with_options(request, runtime)

    async def get_phone_number_verification_status_async(
        self,
        request: main_models.GetPhoneNumberVerificationStatusRequest,
    ) -> main_models.GetPhoneNumberVerificationStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_phone_number_verification_status_with_options_async(request, runtime)

    def get_pledge_template_address_with_options(
        self,
        request: main_models.GetPledgeTemplateAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPledgeTemplateAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.industry_type):
            query['IndustryType'] = request.industry_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPledgeTemplateAddress',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPledgeTemplateAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pledge_template_address_with_options_async(
        self,
        request: main_models.GetPledgeTemplateAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPledgeTemplateAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.industry_type):
            query['IndustryType'] = request.industry_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPledgeTemplateAddress',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPledgeTemplateAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pledge_template_address(
        self,
        request: main_models.GetPledgeTemplateAddressRequest,
    ) -> main_models.GetPledgeTemplateAddressResponse:
        runtime = RuntimeOptions()
        return self.get_pledge_template_address_with_options(request, runtime)

    async def get_pledge_template_address_async(
        self,
        request: main_models.GetPledgeTemplateAddressRequest,
    ) -> main_models.GetPledgeTemplateAddressResponse:
        runtime = RuntimeOptions()
        return await self.get_pledge_template_address_with_options_async(request, runtime)

    def get_pre_validate_phone_id_with_options(
        self,
        request: main_models.GetPreValidatePhoneIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPreValidatePhoneIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.verify_code):
            body['VerifyCode'] = request.verify_code
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPreValidatePhoneId',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPreValidatePhoneIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pre_validate_phone_id_with_options_async(
        self,
        request: main_models.GetPreValidatePhoneIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPreValidatePhoneIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.verify_code):
            body['VerifyCode'] = request.verify_code
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPreValidatePhoneId',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPreValidatePhoneIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pre_validate_phone_id(
        self,
        request: main_models.GetPreValidatePhoneIdRequest,
    ) -> main_models.GetPreValidatePhoneIdResponse:
        runtime = RuntimeOptions()
        return self.get_pre_validate_phone_id_with_options(request, runtime)

    async def get_pre_validate_phone_id_async(
        self,
        request: main_models.GetPreValidatePhoneIdRequest,
    ) -> main_models.GetPreValidatePhoneIdResponse:
        runtime = RuntimeOptions()
        return await self.get_pre_validate_phone_id_with_options_async(request, runtime)

    def get_viber_by_request_no_with_options(
        self,
        request: main_models.GetViberByRequestNoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetViberByRequestNoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.request_no):
            query['RequestNo'] = request.request_no
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetViberByRequestNo',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetViberByRequestNoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_viber_by_request_no_with_options_async(
        self,
        request: main_models.GetViberByRequestNoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetViberByRequestNoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.request_no):
            query['RequestNo'] = request.request_no
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetViberByRequestNo',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetViberByRequestNoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_viber_by_request_no(
        self,
        request: main_models.GetViberByRequestNoRequest,
    ) -> main_models.GetViberByRequestNoResponse:
        runtime = RuntimeOptions()
        return self.get_viber_by_request_no_with_options(request, runtime)

    async def get_viber_by_request_no_async(
        self,
        request: main_models.GetViberByRequestNoRequest,
    ) -> main_models.GetViberByRequestNoResponse:
        runtime = RuntimeOptions()
        return await self.get_viber_by_request_no_with_options_async(request, runtime)

    def get_viber_pause_times_with_options(
        self,
        request: main_models.GetViberPauseTimesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetViberPauseTimesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetViberPauseTimes',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetViberPauseTimesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_viber_pause_times_with_options_async(
        self,
        request: main_models.GetViberPauseTimesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetViberPauseTimesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetViberPauseTimes',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetViberPauseTimesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_viber_pause_times(
        self,
        request: main_models.GetViberPauseTimesRequest,
    ) -> main_models.GetViberPauseTimesResponse:
        runtime = RuntimeOptions()
        return self.get_viber_pause_times_with_options(request, runtime)

    async def get_viber_pause_times_async(
        self,
        request: main_models.GetViberPauseTimesRequest,
    ) -> main_models.GetViberPauseTimesResponse:
        runtime = RuntimeOptions()
        return await self.get_viber_pause_times_with_options_async(request, runtime)

    def get_whatsapp_connection_catalog_with_options(
        self,
        request: main_models.GetWhatsappConnectionCatalogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWhatsappConnectionCatalogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWhatsappConnectionCatalog',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWhatsappConnectionCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_whatsapp_connection_catalog_with_options_async(
        self,
        request: main_models.GetWhatsappConnectionCatalogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWhatsappConnectionCatalogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWhatsappConnectionCatalog',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWhatsappConnectionCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_whatsapp_connection_catalog(
        self,
        request: main_models.GetWhatsappConnectionCatalogRequest,
    ) -> main_models.GetWhatsappConnectionCatalogResponse:
        runtime = RuntimeOptions()
        return self.get_whatsapp_connection_catalog_with_options(request, runtime)

    async def get_whatsapp_connection_catalog_async(
        self,
        request: main_models.GetWhatsappConnectionCatalogRequest,
    ) -> main_models.GetWhatsappConnectionCatalogResponse:
        runtime = RuntimeOptions()
        return await self.get_whatsapp_connection_catalog_with_options_async(request, runtime)

    def get_whatsapp_conversion_api_with_options(
        self,
        request: main_models.GetWhatsappConversionApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWhatsappConversionApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWhatsappConversionApi',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWhatsappConversionApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_whatsapp_conversion_api_with_options_async(
        self,
        request: main_models.GetWhatsappConversionApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWhatsappConversionApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWhatsappConversionApi',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWhatsappConversionApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_whatsapp_conversion_api(
        self,
        request: main_models.GetWhatsappConversionApiRequest,
    ) -> main_models.GetWhatsappConversionApiResponse:
        runtime = RuntimeOptions()
        return self.get_whatsapp_conversion_api_with_options(request, runtime)

    async def get_whatsapp_conversion_api_async(
        self,
        request: main_models.GetWhatsappConversionApiRequest,
    ) -> main_models.GetWhatsappConversionApiResponse:
        runtime = RuntimeOptions()
        return await self.get_whatsapp_conversion_api_with_options_async(request, runtime)

    def get_whatsapp_health_status_with_options(
        self,
        request: main_models.GetWhatsappHealthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWhatsappHealthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.node_type):
            query['NodeType'] = request.node_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWhatsappHealthStatus',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWhatsappHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_whatsapp_health_status_with_options_async(
        self,
        request: main_models.GetWhatsappHealthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWhatsappHealthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.node_type):
            query['NodeType'] = request.node_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWhatsappHealthStatus',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWhatsappHealthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_whatsapp_health_status(
        self,
        request: main_models.GetWhatsappHealthStatusRequest,
    ) -> main_models.GetWhatsappHealthStatusResponse:
        runtime = RuntimeOptions()
        return self.get_whatsapp_health_status_with_options(request, runtime)

    async def get_whatsapp_health_status_async(
        self,
        request: main_models.GetWhatsappHealthStatusRequest,
    ) -> main_models.GetWhatsappHealthStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_whatsapp_health_status_with_options_async(request, runtime)

    def isv_get_app_id_with_options(
        self,
        request: main_models.IsvGetAppIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IsvGetAppIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.intl_version):
            query['IntlVersion'] = request.intl_version
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.permissions):
            query['Permissions'] = request.permissions
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IsvGetAppId',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IsvGetAppIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def isv_get_app_id_with_options_async(
        self,
        request: main_models.IsvGetAppIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IsvGetAppIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.intl_version):
            query['IntlVersion'] = request.intl_version
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.permissions):
            query['Permissions'] = request.permissions
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IsvGetAppId',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IsvGetAppIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def isv_get_app_id(
        self,
        request: main_models.IsvGetAppIdRequest,
    ) -> main_models.IsvGetAppIdResponse:
        runtime = RuntimeOptions()
        return self.isv_get_app_id_with_options(request, runtime)

    async def isv_get_app_id_async(
        self,
        request: main_models.IsvGetAppIdRequest,
    ) -> main_models.IsvGetAppIdResponse:
        runtime = RuntimeOptions()
        return await self.isv_get_app_id_with_options_async(request, runtime)

    def list_all_groups_with_options(
        self,
        tmp_req: main_models.ListAllGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAllGroupsResponse:
        tmp_req.validate()
        request = main_models.ListAllGroupsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAllGroups',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAllGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_groups_with_options_async(
        self,
        tmp_req: main_models.ListAllGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAllGroupsResponse:
        tmp_req.validate()
        request = main_models.ListAllGroupsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAllGroups',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAllGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_groups(
        self,
        request: main_models.ListAllGroupsRequest,
    ) -> main_models.ListAllGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_all_groups_with_options(request, runtime)

    async def list_all_groups_async(
        self,
        request: main_models.ListAllGroupsRequest,
    ) -> main_models.ListAllGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_all_groups_with_options_async(request, runtime)

    def list_bind_dm_account_with_options(
        self,
        request: main_models.ListBindDmAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBindDmAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBindDmAccount',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBindDmAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bind_dm_account_with_options_async(
        self,
        request: main_models.ListBindDmAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBindDmAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBindDmAccount',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBindDmAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_bind_dm_account(
        self,
        request: main_models.ListBindDmAccountRequest,
    ) -> main_models.ListBindDmAccountResponse:
        runtime = RuntimeOptions()
        return self.list_bind_dm_account_with_options(request, runtime)

    async def list_bind_dm_account_async(
        self,
        request: main_models.ListBindDmAccountRequest,
    ) -> main_models.ListBindDmAccountResponse:
        runtime = RuntimeOptions()
        return await self.list_bind_dm_account_with_options_async(request, runtime)

    def list_binding_relations_for_flow_version_with_options(
        self,
        request: main_models.ListBindingRelationsForFlowVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBindingRelationsForFlowVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBindingRelationsForFlowVersion',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBindingRelationsForFlowVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_binding_relations_for_flow_version_with_options_async(
        self,
        request: main_models.ListBindingRelationsForFlowVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBindingRelationsForFlowVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBindingRelationsForFlowVersion',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBindingRelationsForFlowVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_binding_relations_for_flow_version(
        self,
        request: main_models.ListBindingRelationsForFlowVersionRequest,
    ) -> main_models.ListBindingRelationsForFlowVersionResponse:
        runtime = RuntimeOptions()
        return self.list_binding_relations_for_flow_version_with_options(request, runtime)

    async def list_binding_relations_for_flow_version_async(
        self,
        request: main_models.ListBindingRelationsForFlowVersionRequest,
    ) -> main_models.ListBindingRelationsForFlowVersionResponse:
        runtime = RuntimeOptions()
        return await self.list_binding_relations_for_flow_version_with_options_async(request, runtime)

    def list_chat_flow_with_options(
        self,
        tmp_req: main_models.ListChatFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChatFlowResponse:
        tmp_req.validate()
        request = main_models.ListChatFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_trigger_type):
            query['FlowTriggerType'] = request.flow_trigger_type
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.return_with_online_version):
            query['ReturnWithOnlineVersion'] = request.return_with_online_version
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChatFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chat_flow_with_options_async(
        self,
        tmp_req: main_models.ListChatFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChatFlowResponse:
        tmp_req.validate()
        request = main_models.ListChatFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_trigger_type):
            query['FlowTriggerType'] = request.flow_trigger_type
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.return_with_online_version):
            query['ReturnWithOnlineVersion'] = request.return_with_online_version
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChatFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chat_flow(
        self,
        request: main_models.ListChatFlowRequest,
    ) -> main_models.ListChatFlowResponse:
        runtime = RuntimeOptions()
        return self.list_chat_flow_with_options(request, runtime)

    async def list_chat_flow_async(
        self,
        request: main_models.ListChatFlowRequest,
    ) -> main_models.ListChatFlowResponse:
        runtime = RuntimeOptions()
        return await self.list_chat_flow_with_options_async(request, runtime)

    def list_chat_flow_template_with_options(
        self,
        request: main_models.ListChatFlowTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChatFlowTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChatFlowTemplate',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatFlowTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chat_flow_template_with_options_async(
        self,
        request: main_models.ListChatFlowTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChatFlowTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChatFlowTemplate',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatFlowTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chat_flow_template(
        self,
        request: main_models.ListChatFlowTemplateRequest,
    ) -> main_models.ListChatFlowTemplateResponse:
        runtime = RuntimeOptions()
        return self.list_chat_flow_template_with_options(request, runtime)

    async def list_chat_flow_template_async(
        self,
        request: main_models.ListChatFlowTemplateRequest,
    ) -> main_models.ListChatFlowTemplateResponse:
        runtime = RuntimeOptions()
        return await self.list_chat_flow_template_with_options_async(request, runtime)

    def list_chat_group_with_options(
        self,
        tmp_req: main_models.ListChatGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChatGroupResponse:
        tmp_req.validate()
        request = main_models.ListChatGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not DaraCore.is_null(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.group_status):
            query['GroupStatus'] = request.group_status
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_shrink):
            query['Page'] = request.page_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.subject):
            query['Subject'] = request.subject
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChatGroup',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chat_group_with_options_async(
        self,
        tmp_req: main_models.ListChatGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChatGroupResponse:
        tmp_req.validate()
        request = main_models.ListChatGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not DaraCore.is_null(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.group_status):
            query['GroupStatus'] = request.group_status
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_shrink):
            query['Page'] = request.page_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.subject):
            query['Subject'] = request.subject
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChatGroup',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chat_group(
        self,
        request: main_models.ListChatGroupRequest,
    ) -> main_models.ListChatGroupResponse:
        runtime = RuntimeOptions()
        return self.list_chat_group_with_options(request, runtime)

    async def list_chat_group_async(
        self,
        request: main_models.ListChatGroupRequest,
    ) -> main_models.ListChatGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_chat_group_with_options_async(request, runtime)

    def list_chat_group_participants_with_options(
        self,
        tmp_req: main_models.ListChatGroupParticipantsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChatGroupParticipantsResponse:
        tmp_req.validate()
        request = main_models.ListChatGroupParticipantsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not DaraCore.is_null(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_shrink):
            query['Page'] = request.page_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChatGroupParticipants',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatGroupParticipantsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chat_group_participants_with_options_async(
        self,
        tmp_req: main_models.ListChatGroupParticipantsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChatGroupParticipantsResponse:
        tmp_req.validate()
        request = main_models.ListChatGroupParticipantsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not DaraCore.is_null(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_shrink):
            query['Page'] = request.page_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChatGroupParticipants',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatGroupParticipantsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chat_group_participants(
        self,
        request: main_models.ListChatGroupParticipantsRequest,
    ) -> main_models.ListChatGroupParticipantsResponse:
        runtime = RuntimeOptions()
        return self.list_chat_group_participants_with_options(request, runtime)

    async def list_chat_group_participants_async(
        self,
        request: main_models.ListChatGroupParticipantsRequest,
    ) -> main_models.ListChatGroupParticipantsResponse:
        runtime = RuntimeOptions()
        return await self.list_chat_group_participants_with_options_async(request, runtime)

    def list_chatapp_message_with_options(
        self,
        tmp_req: main_models.ListChatappMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChatappMessageResponse:
        tmp_req.validate()
        request = main_models.ListChatappMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not DaraCore.is_null(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.client_accept_status):
            query['ClientAcceptStatus'] = request.client_accept_status
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.end_time_str):
            query['EndTimeStr'] = request.end_time_str
        if not DaraCore.is_null(request.event_action):
            query['EventAction'] = request.event_action
        if not DaraCore.is_null(request.group_message_id):
            query['GroupMessageId'] = request.group_message_id
        if not DaraCore.is_null(request.message_status):
            query['MessageStatus'] = request.message_status
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_shrink):
            query['Page'] = request.page_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.start_time_str):
            query['StartTimeStr'] = request.start_time_str
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.user_number):
            query['UserNumber'] = request.user_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChatappMessage',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatappMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chatapp_message_with_options_async(
        self,
        tmp_req: main_models.ListChatappMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChatappMessageResponse:
        tmp_req.validate()
        request = main_models.ListChatappMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not DaraCore.is_null(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.client_accept_status):
            query['ClientAcceptStatus'] = request.client_accept_status
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.end_time_str):
            query['EndTimeStr'] = request.end_time_str
        if not DaraCore.is_null(request.event_action):
            query['EventAction'] = request.event_action
        if not DaraCore.is_null(request.group_message_id):
            query['GroupMessageId'] = request.group_message_id
        if not DaraCore.is_null(request.message_status):
            query['MessageStatus'] = request.message_status
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_shrink):
            query['Page'] = request.page_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.start_time_str):
            query['StartTimeStr'] = request.start_time_str
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.user_number):
            query['UserNumber'] = request.user_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChatappMessage',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatappMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chatapp_message(
        self,
        request: main_models.ListChatappMessageRequest,
    ) -> main_models.ListChatappMessageResponse:
        runtime = RuntimeOptions()
        return self.list_chatapp_message_with_options(request, runtime)

    async def list_chatapp_message_async(
        self,
        request: main_models.ListChatappMessageRequest,
    ) -> main_models.ListChatappMessageResponse:
        runtime = RuntimeOptions()
        return await self.list_chatapp_message_with_options_async(request, runtime)

    def list_chatapp_template_with_options(
        self,
        tmp_req: main_models.ListChatappTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChatappTemplateResponse:
        tmp_req.validate()
        request = main_models.ListChatappTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not DaraCore.is_null(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not DaraCore.is_null(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_shrink):
            query['Page'] = request.page_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChatappTemplate',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatappTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chatapp_template_with_options_async(
        self,
        tmp_req: main_models.ListChatappTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChatappTemplateResponse:
        tmp_req.validate()
        request = main_models.ListChatappTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not DaraCore.is_null(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not DaraCore.is_null(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_shrink):
            query['Page'] = request.page_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChatappTemplate',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChatappTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chatapp_template(
        self,
        request: main_models.ListChatappTemplateRequest,
    ) -> main_models.ListChatappTemplateResponse:
        runtime = RuntimeOptions()
        return self.list_chatapp_template_with_options(request, runtime)

    async def list_chatapp_template_async(
        self,
        request: main_models.ListChatappTemplateRequest,
    ) -> main_models.ListChatappTemplateResponse:
        runtime = RuntimeOptions()
        return await self.list_chatapp_template_with_options_async(request, runtime)

    def list_custom_audience_with_options(
        self,
        tmp_req: main_models.ListCustomAudienceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomAudienceResponse:
        tmp_req.validate()
        request = main_models.ListCustomAudienceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not DaraCore.is_null(request.ad_account_id):
            query['AdAccountId'] = request.ad_account_id
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.custom_audience_id):
            query['CustomAudienceId'] = request.custom_audience_id
        if not DaraCore.is_null(request.custom_audience_name):
            query['CustomAudienceName'] = request.custom_audience_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_shrink):
            query['Page'] = request.page_shrink
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.token_type):
            query['TokenType'] = request.token_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomAudience',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomAudienceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_audience_with_options_async(
        self,
        tmp_req: main_models.ListCustomAudienceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomAudienceResponse:
        tmp_req.validate()
        request = main_models.ListCustomAudienceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not DaraCore.is_null(request.ad_account_id):
            query['AdAccountId'] = request.ad_account_id
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.custom_audience_id):
            query['CustomAudienceId'] = request.custom_audience_id
        if not DaraCore.is_null(request.custom_audience_name):
            query['CustomAudienceName'] = request.custom_audience_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_shrink):
            query['Page'] = request.page_shrink
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.token_type):
            query['TokenType'] = request.token_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomAudience',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomAudienceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_audience(
        self,
        request: main_models.ListCustomAudienceRequest,
    ) -> main_models.ListCustomAudienceResponse:
        runtime = RuntimeOptions()
        return self.list_custom_audience_with_options(request, runtime)

    async def list_custom_audience_async(
        self,
        request: main_models.ListCustomAudienceRequest,
    ) -> main_models.ListCustomAudienceResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_audience_with_options_async(request, runtime)

    def list_dm_account_with_options(
        self,
        request: main_models.ListDmAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDmAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.send_type):
            query['SendType'] = request.send_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDmAccount',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDmAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dm_account_with_options_async(
        self,
        request: main_models.ListDmAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDmAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.send_type):
            query['SendType'] = request.send_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDmAccount',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDmAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dm_account(
        self,
        request: main_models.ListDmAccountRequest,
    ) -> main_models.ListDmAccountResponse:
        runtime = RuntimeOptions()
        return self.list_dm_account_with_options(request, runtime)

    async def list_dm_account_async(
        self,
        request: main_models.ListDmAccountRequest,
    ) -> main_models.ListDmAccountResponse:
        runtime = RuntimeOptions()
        return await self.list_dm_account_with_options_async(request, runtime)

    def list_dm_tag_with_options(
        self,
        request: main_models.ListDmTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDmTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDmTag',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDmTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dm_tag_with_options_async(
        self,
        request: main_models.ListDmTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDmTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDmTag',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDmTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dm_tag(
        self,
        request: main_models.ListDmTagRequest,
    ) -> main_models.ListDmTagResponse:
        runtime = RuntimeOptions()
        return self.list_dm_tag_with_options(request, runtime)

    async def list_dm_tag_async(
        self,
        request: main_models.ListDmTagRequest,
    ) -> main_models.ListDmTagResponse:
        runtime = RuntimeOptions()
        return await self.list_dm_tag_with_options_async(request, runtime)

    def list_facebook_posts_with_options(
        self,
        request: main_models.ListFacebookPostsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFacebookPostsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFacebookPosts',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFacebookPostsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_facebook_posts_with_options_async(
        self,
        request: main_models.ListFacebookPostsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFacebookPostsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFacebookPosts',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFacebookPostsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_facebook_posts(
        self,
        request: main_models.ListFacebookPostsRequest,
    ) -> main_models.ListFacebookPostsResponse:
        runtime = RuntimeOptions()
        return self.list_facebook_posts_with_options(request, runtime)

    async def list_facebook_posts_async(
        self,
        request: main_models.ListFacebookPostsRequest,
    ) -> main_models.ListFacebookPostsResponse:
        runtime = RuntimeOptions()
        return await self.list_facebook_posts_with_options_async(request, runtime)

    def list_flow_with_options(
        self,
        tmp_req: main_models.ListFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlowResponse:
        tmp_req.validate()
        request = main_models.ListFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.flow_name):
            query['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_shrink):
            query['Page'] = request.page_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_with_options_async(
        self,
        tmp_req: main_models.ListFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlowResponse:
        tmp_req.validate()
        request = main_models.ListFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.flow_name):
            query['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_shrink):
            query['Page'] = request.page_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow(
        self,
        request: main_models.ListFlowRequest,
    ) -> main_models.ListFlowResponse:
        runtime = RuntimeOptions()
        return self.list_flow_with_options(request, runtime)

    async def list_flow_async(
        self,
        request: main_models.ListFlowRequest,
    ) -> main_models.ListFlowResponse:
        runtime = RuntimeOptions()
        return await self.list_flow_with_options_async(request, runtime)

    def list_flow_node_group_with_options(
        self,
        request: main_models.ListFlowNodeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlowNodeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlowNodeGroup',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlowNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_node_group_with_options_async(
        self,
        request: main_models.ListFlowNodeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlowNodeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlowNodeGroup',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlowNodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow_node_group(
        self,
        request: main_models.ListFlowNodeGroupRequest,
    ) -> main_models.ListFlowNodeGroupResponse:
        runtime = RuntimeOptions()
        return self.list_flow_node_group_with_options(request, runtime)

    async def list_flow_node_group_async(
        self,
        request: main_models.ListFlowNodeGroupRequest,
    ) -> main_models.ListFlowNodeGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_flow_node_group_with_options_async(request, runtime)

    def list_flow_node_prototype_v2with_options(
        self,
        request: main_models.ListFlowNodePrototypeV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlowNodePrototypeV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.group_code):
            query['GroupCode'] = request.group_code
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlowNodePrototypeV2',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlowNodePrototypeV2Response(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_node_prototype_v2with_options_async(
        self,
        request: main_models.ListFlowNodePrototypeV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlowNodePrototypeV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.group_code):
            query['GroupCode'] = request.group_code
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlowNodePrototypeV2',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlowNodePrototypeV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow_node_prototype_v2(
        self,
        request: main_models.ListFlowNodePrototypeV2Request,
    ) -> main_models.ListFlowNodePrototypeV2Response:
        runtime = RuntimeOptions()
        return self.list_flow_node_prototype_v2with_options(request, runtime)

    async def list_flow_node_prototype_v2_async(
        self,
        request: main_models.ListFlowNodePrototypeV2Request,
    ) -> main_models.ListFlowNodePrototypeV2Response:
        runtime = RuntimeOptions()
        return await self.list_flow_node_prototype_v2with_options_async(request, runtime)

    def list_flow_version_with_options(
        self,
        tmp_req: main_models.ListFlowVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlowVersionResponse:
        tmp_req.validate()
        request = main_models.ListFlowVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlowVersion',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlowVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_version_with_options_async(
        self,
        tmp_req: main_models.ListFlowVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFlowVersionResponse:
        tmp_req.validate()
        request = main_models.ListFlowVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFlowVersion',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFlowVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_flow_version(
        self,
        request: main_models.ListFlowVersionRequest,
    ) -> main_models.ListFlowVersionResponse:
        runtime = RuntimeOptions()
        return self.list_flow_version_with_options(request, runtime)

    async def list_flow_version_async(
        self,
        request: main_models.ListFlowVersionRequest,
    ) -> main_models.ListFlowVersionResponse:
        runtime = RuntimeOptions()
        return await self.list_flow_version_with_options_async(request, runtime)

    def list_instagram_page_with_options(
        self,
        request: main_models.ListInstagramPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstagramPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstagramPage',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstagramPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instagram_page_with_options_async(
        self,
        request: main_models.ListInstagramPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstagramPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstagramPage',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstagramPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instagram_page(
        self,
        request: main_models.ListInstagramPageRequest,
    ) -> main_models.ListInstagramPageResponse:
        runtime = RuntimeOptions()
        return self.list_instagram_page_with_options(request, runtime)

    async def list_instagram_page_async(
        self,
        request: main_models.ListInstagramPageRequest,
    ) -> main_models.ListInstagramPageResponse:
        runtime = RuntimeOptions()
        return await self.list_instagram_page_with_options_async(request, runtime)

    def list_instagram_posts_with_options(
        self,
        request: main_models.ListInstagramPostsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstagramPostsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstagramPosts',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstagramPostsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instagram_posts_with_options_async(
        self,
        request: main_models.ListInstagramPostsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstagramPostsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstagramPosts',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstagramPostsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instagram_posts(
        self,
        request: main_models.ListInstagramPostsRequest,
    ) -> main_models.ListInstagramPostsResponse:
        runtime = RuntimeOptions()
        return self.list_instagram_posts_with_options(request, runtime)

    async def list_instagram_posts_async(
        self,
        request: main_models.ListInstagramPostsRequest,
    ) -> main_models.ListInstagramPostsResponse:
        runtime = RuntimeOptions()
        return await self.list_instagram_posts_with_options_async(request, runtime)

    def list_instance_with_options(
        self,
        request: main_models.ListInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.filter_str):
            query['FilterStr'] = request.filter_str
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.submit_time):
            query['SubmitTime'] = request.submit_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstance',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_with_options_async(
        self,
        request: main_models.ListInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.filter_str):
            query['FilterStr'] = request.filter_str
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.submit_time):
            query['SubmitTime'] = request.submit_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstance',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance(
        self,
        request: main_models.ListInstanceRequest,
    ) -> main_models.ListInstanceResponse:
        runtime = RuntimeOptions()
        return self.list_instance_with_options(request, runtime)

    async def list_instance_async(
        self,
        request: main_models.ListInstanceRequest,
    ) -> main_models.ListInstanceResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_with_options_async(request, runtime)

    def list_marketing_flow_with_options(
        self,
        tmp_req: main_models.ListMarketingFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMarketingFlowResponse:
        tmp_req.validate()
        request = main_models.ListMarketingFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.activity_code):
            query['ActivityCode'] = request.activity_code
        if not DaraCore.is_null(request.activity_name):
            query['ActivityName'] = request.activity_name
        if not DaraCore.is_null(request.activity_status):
            query['ActivityStatus'] = request.activity_status
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.related_flow_code):
            query['RelatedFlowCode'] = request.related_flow_code
        if not DaraCore.is_null(request.related_group_id):
            query['RelatedGroupId'] = request.related_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMarketingFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMarketingFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_marketing_flow_with_options_async(
        self,
        tmp_req: main_models.ListMarketingFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMarketingFlowResponse:
        tmp_req.validate()
        request = main_models.ListMarketingFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.activity_code):
            query['ActivityCode'] = request.activity_code
        if not DaraCore.is_null(request.activity_name):
            query['ActivityName'] = request.activity_name
        if not DaraCore.is_null(request.activity_status):
            query['ActivityStatus'] = request.activity_status
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.related_flow_code):
            query['RelatedFlowCode'] = request.related_flow_code
        if not DaraCore.is_null(request.related_group_id):
            query['RelatedGroupId'] = request.related_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMarketingFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMarketingFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_marketing_flow(
        self,
        request: main_models.ListMarketingFlowRequest,
    ) -> main_models.ListMarketingFlowResponse:
        runtime = RuntimeOptions()
        return self.list_marketing_flow_with_options(request, runtime)

    async def list_marketing_flow_async(
        self,
        request: main_models.ListMarketingFlowRequest,
    ) -> main_models.ListMarketingFlowResponse:
        runtime = RuntimeOptions()
        return await self.list_marketing_flow_with_options_async(request, runtime)

    def list_message_campaign_with_options(
        self,
        tmp_req: main_models.ListMessageCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMessageCampaignResponse:
        tmp_req.validate()
        request = main_models.ListMessageCampaignShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not DaraCore.is_null(request.ad_account_id):
            query['AdAccountId'] = request.ad_account_id
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.campaign_name):
            query['CampaignName'] = request.campaign_name
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_shrink):
            query['Page'] = request.page_shrink
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMessageCampaign',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMessageCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_message_campaign_with_options_async(
        self,
        tmp_req: main_models.ListMessageCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMessageCampaignResponse:
        tmp_req.validate()
        request = main_models.ListMessageCampaignShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page):
            request.page_shrink = Utils.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not DaraCore.is_null(request.ad_account_id):
            query['AdAccountId'] = request.ad_account_id
        if not DaraCore.is_null(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not DaraCore.is_null(request.campaign_name):
            query['CampaignName'] = request.campaign_name
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_shrink):
            query['Page'] = request.page_shrink
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMessageCampaign',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMessageCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_message_campaign(
        self,
        request: main_models.ListMessageCampaignRequest,
    ) -> main_models.ListMessageCampaignResponse:
        runtime = RuntimeOptions()
        return self.list_message_campaign_with_options(request, runtime)

    async def list_message_campaign_async(
        self,
        request: main_models.ListMessageCampaignRequest,
    ) -> main_models.ListMessageCampaignResponse:
        runtime = RuntimeOptions()
        return await self.list_message_campaign_with_options_async(request, runtime)

    def list_messenger_subscription_token_with_options(
        self,
        request: main_models.ListMessengerSubscriptionTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMessengerSubscriptionTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.custom_audience_id):
            query['CustomAudienceId'] = request.custom_audience_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.page_key):
            query['PageKey'] = request.page_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.token_type):
            query['TokenType'] = request.token_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMessengerSubscriptionToken',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMessengerSubscriptionTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_messenger_subscription_token_with_options_async(
        self,
        request: main_models.ListMessengerSubscriptionTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMessengerSubscriptionTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.custom_audience_id):
            query['CustomAudienceId'] = request.custom_audience_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.page_key):
            query['PageKey'] = request.page_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.token_type):
            query['TokenType'] = request.token_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMessengerSubscriptionToken',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMessengerSubscriptionTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_messenger_subscription_token(
        self,
        request: main_models.ListMessengerSubscriptionTokenRequest,
    ) -> main_models.ListMessengerSubscriptionTokenResponse:
        runtime = RuntimeOptions()
        return self.list_messenger_subscription_token_with_options(request, runtime)

    async def list_messenger_subscription_token_async(
        self,
        request: main_models.ListMessengerSubscriptionTokenRequest,
    ) -> main_models.ListMessengerSubscriptionTokenResponse:
        runtime = RuntimeOptions()
        return await self.list_messenger_subscription_token_with_options_async(request, runtime)

    def list_page_ad_account_with_options(
        self,
        request: main_models.ListPageAdAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPageAdAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPageAdAccount',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPageAdAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_page_ad_account_with_options_async(
        self,
        request: main_models.ListPageAdAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPageAdAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPageAdAccount',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPageAdAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_page_ad_account(
        self,
        request: main_models.ListPageAdAccountRequest,
    ) -> main_models.ListPageAdAccountResponse:
        runtime = RuntimeOptions()
        return self.list_page_ad_account_with_options(request, runtime)

    async def list_page_ad_account_async(
        self,
        request: main_models.ListPageAdAccountRequest,
    ) -> main_models.ListPageAdAccountResponse:
        runtime = RuntimeOptions()
        return await self.list_page_ad_account_with_options_async(request, runtime)

    def list_phone_message_qrdl_with_options(
        self,
        request: main_models.ListPhoneMessageQrdlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPhoneMessageQrdlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPhoneMessageQrdl',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPhoneMessageQrdlResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_phone_message_qrdl_with_options_async(
        self,
        request: main_models.ListPhoneMessageQrdlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPhoneMessageQrdlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPhoneMessageQrdl',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPhoneMessageQrdlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_phone_message_qrdl(
        self,
        request: main_models.ListPhoneMessageQrdlRequest,
    ) -> main_models.ListPhoneMessageQrdlResponse:
        runtime = RuntimeOptions()
        return self.list_phone_message_qrdl_with_options(request, runtime)

    async def list_phone_message_qrdl_async(
        self,
        request: main_models.ListPhoneMessageQrdlRequest,
    ) -> main_models.ListPhoneMessageQrdlResponse:
        runtime = RuntimeOptions()
        return await self.list_phone_message_qrdl_with_options_async(request, runtime)

    def list_product_with_options(
        self,
        request: main_models.ListProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.after):
            query['After'] = request.after
        if not DaraCore.is_null(request.before):
            query['Before'] = request.before
        if not DaraCore.is_null(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.fields):
            query['Fields'] = request.fields
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProduct',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_with_options_async(
        self,
        request: main_models.ListProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.after):
            query['After'] = request.after
        if not DaraCore.is_null(request.before):
            query['Before'] = request.before
        if not DaraCore.is_null(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.fields):
            query['Fields'] = request.fields
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProduct',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product(
        self,
        request: main_models.ListProductRequest,
    ) -> main_models.ListProductResponse:
        runtime = RuntimeOptions()
        return self.list_product_with_options(request, runtime)

    async def list_product_async(
        self,
        request: main_models.ListProductRequest,
    ) -> main_models.ListProductResponse:
        runtime = RuntimeOptions()
        return await self.list_product_with_options_async(request, runtime)

    def list_product_catalog_with_options(
        self,
        request: main_models.ListProductCatalogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductCatalogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.after):
            query['After'] = request.after
        if not DaraCore.is_null(request.before):
            query['Before'] = request.before
        if not DaraCore.is_null(request.business_id):
            query['BusinessId'] = request.business_id
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.fields):
            query['Fields'] = request.fields
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProductCatalog',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_catalog_with_options_async(
        self,
        request: main_models.ListProductCatalogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductCatalogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.after):
            query['After'] = request.after
        if not DaraCore.is_null(request.before):
            query['Before'] = request.before
        if not DaraCore.is_null(request.business_id):
            query['BusinessId'] = request.business_id
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.fields):
            query['Fields'] = request.fields
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProductCatalog',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_catalog(
        self,
        request: main_models.ListProductCatalogRequest,
    ) -> main_models.ListProductCatalogResponse:
        runtime = RuntimeOptions()
        return self.list_product_catalog_with_options(request, runtime)

    async def list_product_catalog_async(
        self,
        request: main_models.ListProductCatalogRequest,
    ) -> main_models.ListProductCatalogResponse:
        runtime = RuntimeOptions()
        return await self.list_product_catalog_with_options_async(request, runtime)

    def list_viber_service_message_with_options(
        self,
        request: main_models.ListViberServiceMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListViberServiceMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListViberServiceMessage',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListViberServiceMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_viber_service_message_with_options_async(
        self,
        request: main_models.ListViberServiceMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListViberServiceMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListViberServiceMessage',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListViberServiceMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_viber_service_message(
        self,
        request: main_models.ListViberServiceMessageRequest,
    ) -> main_models.ListViberServiceMessageResponse:
        runtime = RuntimeOptions()
        return self.list_viber_service_message_with_options(request, runtime)

    async def list_viber_service_message_async(
        self,
        request: main_models.ListViberServiceMessageRequest,
    ) -> main_models.ListViberServiceMessageResponse:
        runtime = RuntimeOptions()
        return await self.list_viber_service_message_with_options_async(request, runtime)

    def modify_chatapp_template_with_options(
        self,
        tmp_req: main_models.ModifyChatappTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyChatappTemplateResponse:
        tmp_req.validate()
        request = main_models.ModifyChatappTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.components):
            request.components_shrink = Utils.array_to_string_with_specified_style(tmp_req.components, 'Components', 'json')
        if not DaraCore.is_null(tmp_req.example):
            request.example_shrink = Utils.array_to_string_with_specified_style(tmp_req.example, 'Example', 'json')
        body = {}
        if not DaraCore.is_null(request.category):
            body['Category'] = request.category
        if not DaraCore.is_null(request.category_change_paused):
            body['CategoryChangePaused'] = request.category_change_paused
        if not DaraCore.is_null(request.components_shrink):
            body['Components'] = request.components_shrink
        if not DaraCore.is_null(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.cust_waba_id):
            body['CustWabaId'] = request.cust_waba_id
        if not DaraCore.is_null(request.example_shrink):
            body['Example'] = request.example_shrink
        if not DaraCore.is_null(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.language):
            body['Language'] = request.language
        if not DaraCore.is_null(request.message_send_ttl_seconds):
            body['MessageSendTtlSeconds'] = request.message_send_ttl_seconds
        if not DaraCore.is_null(request.template_code):
            body['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_name):
            body['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            body['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyChatappTemplate',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyChatappTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_chatapp_template_with_options_async(
        self,
        tmp_req: main_models.ModifyChatappTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyChatappTemplateResponse:
        tmp_req.validate()
        request = main_models.ModifyChatappTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.components):
            request.components_shrink = Utils.array_to_string_with_specified_style(tmp_req.components, 'Components', 'json')
        if not DaraCore.is_null(tmp_req.example):
            request.example_shrink = Utils.array_to_string_with_specified_style(tmp_req.example, 'Example', 'json')
        body = {}
        if not DaraCore.is_null(request.category):
            body['Category'] = request.category
        if not DaraCore.is_null(request.category_change_paused):
            body['CategoryChangePaused'] = request.category_change_paused
        if not DaraCore.is_null(request.components_shrink):
            body['Components'] = request.components_shrink
        if not DaraCore.is_null(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.cust_waba_id):
            body['CustWabaId'] = request.cust_waba_id
        if not DaraCore.is_null(request.example_shrink):
            body['Example'] = request.example_shrink
        if not DaraCore.is_null(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.language):
            body['Language'] = request.language
        if not DaraCore.is_null(request.message_send_ttl_seconds):
            body['MessageSendTtlSeconds'] = request.message_send_ttl_seconds
        if not DaraCore.is_null(request.template_code):
            body['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_name):
            body['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            body['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyChatappTemplate',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyChatappTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_chatapp_template(
        self,
        request: main_models.ModifyChatappTemplateRequest,
    ) -> main_models.ModifyChatappTemplateResponse:
        runtime = RuntimeOptions()
        return self.modify_chatapp_template_with_options(request, runtime)

    async def modify_chatapp_template_async(
        self,
        request: main_models.ModifyChatappTemplateRequest,
    ) -> main_models.ModifyChatappTemplateResponse:
        runtime = RuntimeOptions()
        return await self.modify_chatapp_template_with_options_async(request, runtime)

    def modify_chatapp_template_properties_with_options(
        self,
        request: main_models.ModifyChatappTemplatePropertiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyChatappTemplatePropertiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_send):
            query['AllowSend'] = request.allow_send
        if not DaraCore.is_null(request.category_change_paused):
            query['CategoryChangePaused'] = request.category_change_paused
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyChatappTemplateProperties',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyChatappTemplatePropertiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_chatapp_template_properties_with_options_async(
        self,
        request: main_models.ModifyChatappTemplatePropertiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyChatappTemplatePropertiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_send):
            query['AllowSend'] = request.allow_send
        if not DaraCore.is_null(request.category_change_paused):
            query['CategoryChangePaused'] = request.category_change_paused
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyChatappTemplateProperties',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyChatappTemplatePropertiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_chatapp_template_properties(
        self,
        request: main_models.ModifyChatappTemplatePropertiesRequest,
    ) -> main_models.ModifyChatappTemplatePropertiesResponse:
        runtime = RuntimeOptions()
        return self.modify_chatapp_template_properties_with_options(request, runtime)

    async def modify_chatapp_template_properties_async(
        self,
        request: main_models.ModifyChatappTemplatePropertiesRequest,
    ) -> main_models.ModifyChatappTemplatePropertiesResponse:
        runtime = RuntimeOptions()
        return await self.modify_chatapp_template_properties_with_options_async(request, runtime)

    def modify_flow_with_options(
        self,
        tmp_req: main_models.ModifyFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFlowResponse:
        tmp_req.validate()
        request = main_models.ModifyFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.categories):
            request.categories_shrink = Utils.array_to_string_with_specified_style(tmp_req.categories, 'Categories', 'json')
        query = {}
        if not DaraCore.is_null(request.categories_shrink):
            query['Categories'] = request.categories_shrink
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.flow_name):
            query['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_with_options_async(
        self,
        tmp_req: main_models.ModifyFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFlowResponse:
        tmp_req.validate()
        request = main_models.ModifyFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.categories):
            request.categories_shrink = Utils.array_to_string_with_specified_style(tmp_req.categories, 'Categories', 'json')
        query = {}
        if not DaraCore.is_null(request.categories_shrink):
            query['Categories'] = request.categories_shrink
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.flow_name):
            query['FlowName'] = request.flow_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_flow(
        self,
        request: main_models.ModifyFlowRequest,
    ) -> main_models.ModifyFlowResponse:
        runtime = RuntimeOptions()
        return self.modify_flow_with_options(request, runtime)

    async def modify_flow_async(
        self,
        request: main_models.ModifyFlowRequest,
    ) -> main_models.ModifyFlowResponse:
        runtime = RuntimeOptions()
        return await self.modify_flow_with_options_async(request, runtime)

    def modify_phone_business_profile_with_options(
        self,
        tmp_req: main_models.ModifyPhoneBusinessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPhoneBusinessProfileResponse:
        tmp_req.validate()
        request = main_models.ModifyPhoneBusinessProfileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.websites):
            request.websites_shrink = Utils.array_to_string_with_specified_style(tmp_req.websites, 'Websites', 'json')
        query = {}
        if not DaraCore.is_null(request.about):
            query['About'] = request.about
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.profile_picture_url):
            query['ProfilePictureUrl'] = request.profile_picture_url
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.vertical):
            query['Vertical'] = request.vertical
        if not DaraCore.is_null(request.websites_shrink):
            query['Websites'] = request.websites_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPhoneBusinessProfile',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPhoneBusinessProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_phone_business_profile_with_options_async(
        self,
        tmp_req: main_models.ModifyPhoneBusinessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPhoneBusinessProfileResponse:
        tmp_req.validate()
        request = main_models.ModifyPhoneBusinessProfileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.websites):
            request.websites_shrink = Utils.array_to_string_with_specified_style(tmp_req.websites, 'Websites', 'json')
        query = {}
        if not DaraCore.is_null(request.about):
            query['About'] = request.about
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.profile_picture_url):
            query['ProfilePictureUrl'] = request.profile_picture_url
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.vertical):
            query['Vertical'] = request.vertical
        if not DaraCore.is_null(request.websites_shrink):
            query['Websites'] = request.websites_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPhoneBusinessProfile',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPhoneBusinessProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_phone_business_profile(
        self,
        request: main_models.ModifyPhoneBusinessProfileRequest,
    ) -> main_models.ModifyPhoneBusinessProfileResponse:
        runtime = RuntimeOptions()
        return self.modify_phone_business_profile_with_options(request, runtime)

    async def modify_phone_business_profile_async(
        self,
        request: main_models.ModifyPhoneBusinessProfileRequest,
    ) -> main_models.ModifyPhoneBusinessProfileResponse:
        runtime = RuntimeOptions()
        return await self.modify_phone_business_profile_with_options_async(request, runtime)

    def move_contact_to_group_with_options(
        self,
        tmp_req: main_models.MoveContactToGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveContactToGroupResponse:
        tmp_req.validate()
        request = main_models.MoveContactToGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.contacts):
            query['Contacts'] = request.contacts
        if not DaraCore.is_null(request.link_exist_groups):
            query['LinkExistGroups'] = request.link_exist_groups
        if not DaraCore.is_null(request.link_new_groups):
            query['LinkNewGroups'] = request.link_new_groups
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveContactToGroup',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveContactToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_contact_to_group_with_options_async(
        self,
        tmp_req: main_models.MoveContactToGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveContactToGroupResponse:
        tmp_req.validate()
        request = main_models.MoveContactToGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.contacts):
            query['Contacts'] = request.contacts
        if not DaraCore.is_null(request.link_exist_groups):
            query['LinkExistGroups'] = request.link_exist_groups
        if not DaraCore.is_null(request.link_new_groups):
            query['LinkNewGroups'] = request.link_new_groups
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveContactToGroup',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveContactToGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_contact_to_group(
        self,
        request: main_models.MoveContactToGroupRequest,
    ) -> main_models.MoveContactToGroupResponse:
        runtime = RuntimeOptions()
        return self.move_contact_to_group_with_options(request, runtime)

    async def move_contact_to_group_async(
        self,
        request: main_models.MoveContactToGroupRequest,
    ) -> main_models.MoveContactToGroupResponse:
        runtime = RuntimeOptions()
        return await self.move_contact_to_group_with_options_async(request, runtime)

    def offline_flow_version_with_options(
        self,
        tmp_req: main_models.OfflineFlowVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OfflineFlowVersionResponse:
        tmp_req.validate()
        request = main_models.OfflineFlowVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OfflineFlowVersion',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineFlowVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_flow_version_with_options_async(
        self,
        tmp_req: main_models.OfflineFlowVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OfflineFlowVersionResponse:
        tmp_req.validate()
        request = main_models.OfflineFlowVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OfflineFlowVersion',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineFlowVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_flow_version(
        self,
        request: main_models.OfflineFlowVersionRequest,
    ) -> main_models.OfflineFlowVersionResponse:
        runtime = RuntimeOptions()
        return self.offline_flow_version_with_options(request, runtime)

    async def offline_flow_version_async(
        self,
        request: main_models.OfflineFlowVersionRequest,
    ) -> main_models.OfflineFlowVersionResponse:
        runtime = RuntimeOptions()
        return await self.offline_flow_version_with_options_async(request, runtime)

    def online_flow_version_with_options(
        self,
        tmp_req: main_models.OnlineFlowVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnlineFlowVersionResponse:
        tmp_req.validate()
        request = main_models.OnlineFlowVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnlineFlowVersion',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnlineFlowVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def online_flow_version_with_options_async(
        self,
        tmp_req: main_models.OnlineFlowVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnlineFlowVersionResponse:
        tmp_req.validate()
        request = main_models.OnlineFlowVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnlineFlowVersion',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnlineFlowVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def online_flow_version(
        self,
        request: main_models.OnlineFlowVersionRequest,
    ) -> main_models.OnlineFlowVersionResponse:
        runtime = RuntimeOptions()
        return self.online_flow_version_with_options(request, runtime)

    async def online_flow_version_async(
        self,
        request: main_models.OnlineFlowVersionRequest,
    ) -> main_models.OnlineFlowVersionResponse:
        runtime = RuntimeOptions()
        return await self.online_flow_version_with_options_async(request, runtime)

    def open_chatapp_service_with_options(
        self,
        request: main_models.OpenChatappServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenChatappServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenChatappService',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenChatappServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_chatapp_service_with_options_async(
        self,
        request: main_models.OpenChatappServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenChatappServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenChatappService',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenChatappServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_chatapp_service(
        self,
        request: main_models.OpenChatappServiceRequest,
    ) -> main_models.OpenChatappServiceResponse:
        runtime = RuntimeOptions()
        return self.open_chatapp_service_with_options(request, runtime)

    async def open_chatapp_service_async(
        self,
        request: main_models.OpenChatappServiceRequest,
    ) -> main_models.OpenChatappServiceResponse:
        runtime = RuntimeOptions()
        return await self.open_chatapp_service_with_options_async(request, runtime)

    def pause_marketing_flow_with_options(
        self,
        request: main_models.PauseMarketingFLowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PauseMarketingFLowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_code):
            query['ActivityCode'] = request.activity_code
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PauseMarketingFLow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PauseMarketingFLowResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_marketing_flow_with_options_async(
        self,
        request: main_models.PauseMarketingFLowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PauseMarketingFLowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.activity_code):
            query['ActivityCode'] = request.activity_code
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PauseMarketingFLow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PauseMarketingFLowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_marketing_flow(
        self,
        request: main_models.PauseMarketingFLowRequest,
    ) -> main_models.PauseMarketingFLowResponse:
        runtime = RuntimeOptions()
        return self.pause_marketing_flow_with_options(request, runtime)

    async def pause_marketing_flow_async(
        self,
        request: main_models.PauseMarketingFLowRequest,
    ) -> main_models.PauseMarketingFLowResponse:
        runtime = RuntimeOptions()
        return await self.pause_marketing_flow_with_options_async(request, runtime)

    def publish_flow_with_options(
        self,
        request: main_models.PublishFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_flow_with_options_async(
        self,
        request: main_models.PublishFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_flow(
        self,
        request: main_models.PublishFlowRequest,
    ) -> main_models.PublishFlowResponse:
        runtime = RuntimeOptions()
        return self.publish_flow_with_options(request, runtime)

    async def publish_flow_async(
        self,
        request: main_models.PublishFlowRequest,
    ) -> main_models.PublishFlowResponse:
        runtime = RuntimeOptions()
        return await self.publish_flow_with_options_async(request, runtime)

    def query_chatapp_bind_waba_with_options(
        self,
        request: main_models.QueryChatappBindWabaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryChatappBindWabaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryChatappBindWaba',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryChatappBindWabaResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_chatapp_bind_waba_with_options_async(
        self,
        request: main_models.QueryChatappBindWabaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryChatappBindWabaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryChatappBindWaba',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryChatappBindWabaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_chatapp_bind_waba(
        self,
        request: main_models.QueryChatappBindWabaRequest,
    ) -> main_models.QueryChatappBindWabaResponse:
        runtime = RuntimeOptions()
        return self.query_chatapp_bind_waba_with_options(request, runtime)

    async def query_chatapp_bind_waba_async(
        self,
        request: main_models.QueryChatappBindWabaRequest,
    ) -> main_models.QueryChatappBindWabaResponse:
        runtime = RuntimeOptions()
        return await self.query_chatapp_bind_waba_with_options_async(request, runtime)

    def query_chatapp_phone_numbers_with_options(
        self,
        request: main_models.QueryChatappPhoneNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryChatappPhoneNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryChatappPhoneNumbers',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryChatappPhoneNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_chatapp_phone_numbers_with_options_async(
        self,
        request: main_models.QueryChatappPhoneNumbersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryChatappPhoneNumbersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryChatappPhoneNumbers',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryChatappPhoneNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_chatapp_phone_numbers(
        self,
        request: main_models.QueryChatappPhoneNumbersRequest,
    ) -> main_models.QueryChatappPhoneNumbersResponse:
        runtime = RuntimeOptions()
        return self.query_chatapp_phone_numbers_with_options(request, runtime)

    async def query_chatapp_phone_numbers_async(
        self,
        request: main_models.QueryChatappPhoneNumbersRequest,
    ) -> main_models.QueryChatappPhoneNumbersResponse:
        runtime = RuntimeOptions()
        return await self.query_chatapp_phone_numbers_with_options_async(request, runtime)

    def query_instance_with_options(
        self,
        request: main_models.QueryInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInstance',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_instance_with_options_async(
        self,
        request: main_models.QueryInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInstance',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_instance(
        self,
        request: main_models.QueryInstanceRequest,
    ) -> main_models.QueryInstanceResponse:
        runtime = RuntimeOptions()
        return self.query_instance_with_options(request, runtime)

    async def query_instance_async(
        self,
        request: main_models.QueryInstanceRequest,
    ) -> main_models.QueryInstanceResponse:
        runtime = RuntimeOptions()
        return await self.query_instance_with_options_async(request, runtime)

    def query_mmlactive_with_options(
        self,
        request: main_models.QueryMMLActiveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMMLActiveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMMLActive',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMMLActiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mmlactive_with_options_async(
        self,
        request: main_models.QueryMMLActiveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMMLActiveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMMLActive',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMMLActiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mmlactive(
        self,
        request: main_models.QueryMMLActiveRequest,
    ) -> main_models.QueryMMLActiveResponse:
        runtime = RuntimeOptions()
        return self.query_mmlactive_with_options(request, runtime)

    async def query_mmlactive_async(
        self,
        request: main_models.QueryMMLActiveRequest,
    ) -> main_models.QueryMMLActiveResponse:
        runtime = RuntimeOptions()
        return await self.query_mmlactive_with_options_async(request, runtime)

    def query_phone_business_profile_with_options(
        self,
        request: main_models.QueryPhoneBusinessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPhoneBusinessProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPhoneBusinessProfile',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPhoneBusinessProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_phone_business_profile_with_options_async(
        self,
        request: main_models.QueryPhoneBusinessProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPhoneBusinessProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPhoneBusinessProfile',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPhoneBusinessProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_phone_business_profile(
        self,
        request: main_models.QueryPhoneBusinessProfileRequest,
    ) -> main_models.QueryPhoneBusinessProfileResponse:
        runtime = RuntimeOptions()
        return self.query_phone_business_profile_with_options(request, runtime)

    async def query_phone_business_profile_async(
        self,
        request: main_models.QueryPhoneBusinessProfileRequest,
    ) -> main_models.QueryPhoneBusinessProfileResponse:
        runtime = RuntimeOptions()
        return await self.query_phone_business_profile_with_options_async(request, runtime)

    def query_waba_business_info_with_options(
        self,
        request: main_models.QueryWabaBusinessInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryWabaBusinessInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryWabaBusinessInfo',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryWabaBusinessInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_waba_business_info_with_options_async(
        self,
        request: main_models.QueryWabaBusinessInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryWabaBusinessInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryWabaBusinessInfo',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryWabaBusinessInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_waba_business_info(
        self,
        request: main_models.QueryWabaBusinessInfoRequest,
    ) -> main_models.QueryWabaBusinessInfoResponse:
        runtime = RuntimeOptions()
        return self.query_waba_business_info_with_options(request, runtime)

    async def query_waba_business_info_async(
        self,
        request: main_models.QueryWabaBusinessInfoRequest,
    ) -> main_models.QueryWabaBusinessInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_waba_business_info_with_options_async(request, runtime)

    def read_chat_flow_with_options(
        self,
        tmp_req: main_models.ReadChatFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadChatFlowResponse:
        tmp_req.validate()
        request = main_models.ReadChatFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReadChatFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadChatFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_chat_flow_with_options_async(
        self,
        tmp_req: main_models.ReadChatFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadChatFlowResponse:
        tmp_req.validate()
        request = main_models.ReadChatFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReadChatFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadChatFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_chat_flow(
        self,
        request: main_models.ReadChatFlowRequest,
    ) -> main_models.ReadChatFlowResponse:
        runtime = RuntimeOptions()
        return self.read_chat_flow_with_options(request, runtime)

    async def read_chat_flow_async(
        self,
        request: main_models.ReadChatFlowRequest,
    ) -> main_models.ReadChatFlowResponse:
        runtime = RuntimeOptions()
        return await self.read_chat_flow_with_options_async(request, runtime)

    def read_chat_flow_log_setting_with_options(
        self,
        request: main_models.ReadChatFlowLogSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadChatFlowLogSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReadChatFlowLogSetting',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadChatFlowLogSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_chat_flow_log_setting_with_options_async(
        self,
        request: main_models.ReadChatFlowLogSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadChatFlowLogSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReadChatFlowLogSetting',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadChatFlowLogSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_chat_flow_log_setting(
        self,
        request: main_models.ReadChatFlowLogSettingRequest,
    ) -> main_models.ReadChatFlowLogSettingResponse:
        runtime = RuntimeOptions()
        return self.read_chat_flow_log_setting_with_options(request, runtime)

    async def read_chat_flow_log_setting_async(
        self,
        request: main_models.ReadChatFlowLogSettingRequest,
    ) -> main_models.ReadChatFlowLogSettingResponse:
        runtime = RuntimeOptions()
        return await self.read_chat_flow_log_setting_with_options_async(request, runtime)

    def read_flow_version_with_options(
        self,
        tmp_req: main_models.ReadFlowVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadFlowVersionResponse:
        tmp_req.validate()
        request = main_models.ReadFlowVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReadFlowVersion',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadFlowVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_flow_version_with_options_async(
        self,
        tmp_req: main_models.ReadFlowVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReadFlowVersionResponse:
        tmp_req.validate()
        request = main_models.ReadFlowVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReadFlowVersion',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadFlowVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_flow_version(
        self,
        request: main_models.ReadFlowVersionRequest,
    ) -> main_models.ReadFlowVersionResponse:
        runtime = RuntimeOptions()
        return self.read_flow_version_with_options(request, runtime)

    async def read_flow_version_async(
        self,
        request: main_models.ReadFlowVersionRequest,
    ) -> main_models.ReadFlowVersionResponse:
        runtime = RuntimeOptions()
        return await self.read_flow_version_with_options_async(request, runtime)

    def remove_contact_by_id_with_options(
        self,
        request: main_models.RemoveContactByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveContactByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveContactById',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveContactByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_contact_by_id_with_options_async(
        self,
        request: main_models.RemoveContactByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveContactByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveContactById',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveContactByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_contact_by_id(
        self,
        request: main_models.RemoveContactByIdRequest,
    ) -> main_models.RemoveContactByIdResponse:
        runtime = RuntimeOptions()
        return self.remove_contact_by_id_with_options(request, runtime)

    async def remove_contact_by_id_async(
        self,
        request: main_models.RemoveContactByIdRequest,
    ) -> main_models.RemoveContactByIdResponse:
        runtime = RuntimeOptions()
        return await self.remove_contact_by_id_with_options_async(request, runtime)

    def request_whatsapp_conversion_api_with_options(
        self,
        tmp_req: main_models.RequestWhatsappConversionApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RequestWhatsappConversionApiResponse:
        tmp_req.validate()
        request = main_models.RequestWhatsappConversionApiShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.request_data):
            request.request_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.request_data, 'RequestData', 'json')
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.request_data_shrink):
            query['RequestData'] = request.request_data_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RequestWhatsappConversionApi',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RequestWhatsappConversionApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_whatsapp_conversion_api_with_options_async(
        self,
        tmp_req: main_models.RequestWhatsappConversionApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RequestWhatsappConversionApiResponse:
        tmp_req.validate()
        request = main_models.RequestWhatsappConversionApiShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.request_data):
            request.request_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.request_data, 'RequestData', 'json')
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.request_data_shrink):
            query['RequestData'] = request.request_data_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RequestWhatsappConversionApi',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RequestWhatsappConversionApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_whatsapp_conversion_api(
        self,
        request: main_models.RequestWhatsappConversionApiRequest,
    ) -> main_models.RequestWhatsappConversionApiResponse:
        runtime = RuntimeOptions()
        return self.request_whatsapp_conversion_api_with_options(request, runtime)

    async def request_whatsapp_conversion_api_async(
        self,
        request: main_models.RequestWhatsappConversionApiRequest,
    ) -> main_models.RequestWhatsappConversionApiResponse:
        runtime = RuntimeOptions()
        return await self.request_whatsapp_conversion_api_with_options_async(request, runtime)

    def send_chatapp_mass_message_with_options(
        self,
        tmp_req: main_models.SendChatappMassMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendChatappMassMessageResponse:
        tmp_req.validate()
        request = main_models.SendChatappMassMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sender_list):
            request.sender_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.sender_list, 'SenderList', 'json')
        query = {}
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not DaraCore.is_null(request.fall_back_content):
            query['FallBackContent'] = request.fall_back_content
        if not DaraCore.is_null(request.fall_back_duration):
            query['FallBackDuration'] = request.fall_back_duration
        if not DaraCore.is_null(request.fall_back_id):
            query['FallBackId'] = request.fall_back_id
        if not DaraCore.is_null(request.fall_back_rule):
            query['FallBackRule'] = request.fall_back_rule
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.label):
            query['Label'] = request.label
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sender_list_shrink):
            query['SenderList'] = request.sender_list_shrink
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendChatappMassMessage',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendChatappMassMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_chatapp_mass_message_with_options_async(
        self,
        tmp_req: main_models.SendChatappMassMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendChatappMassMessageResponse:
        tmp_req.validate()
        request = main_models.SendChatappMassMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sender_list):
            request.sender_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.sender_list, 'SenderList', 'json')
        query = {}
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not DaraCore.is_null(request.fall_back_content):
            query['FallBackContent'] = request.fall_back_content
        if not DaraCore.is_null(request.fall_back_duration):
            query['FallBackDuration'] = request.fall_back_duration
        if not DaraCore.is_null(request.fall_back_id):
            query['FallBackId'] = request.fall_back_id
        if not DaraCore.is_null(request.fall_back_rule):
            query['FallBackRule'] = request.fall_back_rule
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.label):
            query['Label'] = request.label
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sender_list_shrink):
            query['SenderList'] = request.sender_list_shrink
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendChatappMassMessage',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendChatappMassMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_chatapp_mass_message(
        self,
        request: main_models.SendChatappMassMessageRequest,
    ) -> main_models.SendChatappMassMessageResponse:
        runtime = RuntimeOptions()
        return self.send_chatapp_mass_message_with_options(request, runtime)

    async def send_chatapp_mass_message_async(
        self,
        request: main_models.SendChatappMassMessageRequest,
    ) -> main_models.SendChatappMassMessageResponse:
        runtime = RuntimeOptions()
        return await self.send_chatapp_mass_message_with_options_async(request, runtime)

    def send_chatapp_message_with_options(
        self,
        tmp_req: main_models.SendChatappMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendChatappMessageResponse:
        tmp_req.validate()
        request = main_models.SendChatappMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.flow_action):
            request.flow_action_shrink = Utils.array_to_string_with_specified_style(tmp_req.flow_action, 'FlowAction', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.product_action):
            request.product_action_shrink = Utils.array_to_string_with_specified_style(tmp_req.product_action, 'ProductAction', 'json')
        if not DaraCore.is_null(tmp_req.template_params):
            request.template_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.template_params, 'TemplateParams', 'json')
        query = {}
        if not DaraCore.is_null(request.ad_account_id):
            query['AdAccountId'] = request.ad_account_id
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.context_message_id):
            query['ContextMessageId'] = request.context_message_id
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not DaraCore.is_null(request.fall_back_content):
            query['FallBackContent'] = request.fall_back_content
        if not DaraCore.is_null(request.fall_back_duration):
            query['FallBackDuration'] = request.fall_back_duration
        if not DaraCore.is_null(request.fall_back_id):
            query['FallBackId'] = request.fall_back_id
        if not DaraCore.is_null(request.fall_back_rule):
            query['FallBackRule'] = request.fall_back_rule
        if not DaraCore.is_null(request.flow_action_shrink):
            query['FlowAction'] = request.flow_action_shrink
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.label):
            query['Label'] = request.label
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.message_campaign_id):
            query['MessageCampaignId'] = request.message_campaign_id
        if not DaraCore.is_null(request.message_type):
            query['MessageType'] = request.message_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.product_action_shrink):
            query['ProductAction'] = request.product_action_shrink
        if not DaraCore.is_null(request.recipient_type):
            query['RecipientType'] = request.recipient_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_params_shrink):
            query['TemplateParams'] = request.template_params_shrink
        if not DaraCore.is_null(request.to):
            query['To'] = request.to
        if not DaraCore.is_null(request.token_type):
            query['TokenType'] = request.token_type
        if not DaraCore.is_null(request.tracking_data):
            query['TrackingData'] = request.tracking_data
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendChatappMessage',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendChatappMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_chatapp_message_with_options_async(
        self,
        tmp_req: main_models.SendChatappMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendChatappMessageResponse:
        tmp_req.validate()
        request = main_models.SendChatappMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.flow_action):
            request.flow_action_shrink = Utils.array_to_string_with_specified_style(tmp_req.flow_action, 'FlowAction', 'json')
        if not DaraCore.is_null(tmp_req.payload):
            request.payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not DaraCore.is_null(tmp_req.product_action):
            request.product_action_shrink = Utils.array_to_string_with_specified_style(tmp_req.product_action, 'ProductAction', 'json')
        if not DaraCore.is_null(tmp_req.template_params):
            request.template_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.template_params, 'TemplateParams', 'json')
        query = {}
        if not DaraCore.is_null(request.ad_account_id):
            query['AdAccountId'] = request.ad_account_id
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.context_message_id):
            query['ContextMessageId'] = request.context_message_id
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not DaraCore.is_null(request.fall_back_content):
            query['FallBackContent'] = request.fall_back_content
        if not DaraCore.is_null(request.fall_back_duration):
            query['FallBackDuration'] = request.fall_back_duration
        if not DaraCore.is_null(request.fall_back_id):
            query['FallBackId'] = request.fall_back_id
        if not DaraCore.is_null(request.fall_back_rule):
            query['FallBackRule'] = request.fall_back_rule
        if not DaraCore.is_null(request.flow_action_shrink):
            query['FlowAction'] = request.flow_action_shrink
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not DaraCore.is_null(request.label):
            query['Label'] = request.label
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.message_campaign_id):
            query['MessageCampaignId'] = request.message_campaign_id
        if not DaraCore.is_null(request.message_type):
            query['MessageType'] = request.message_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        if not DaraCore.is_null(request.product_action_shrink):
            query['ProductAction'] = request.product_action_shrink
        if not DaraCore.is_null(request.recipient_type):
            query['RecipientType'] = request.recipient_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_params_shrink):
            query['TemplateParams'] = request.template_params_shrink
        if not DaraCore.is_null(request.to):
            query['To'] = request.to
        if not DaraCore.is_null(request.token_type):
            query['TokenType'] = request.token_type
        if not DaraCore.is_null(request.tracking_data):
            query['TrackingData'] = request.tracking_data
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendChatappMessage',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendChatappMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_chatapp_message(
        self,
        request: main_models.SendChatappMessageRequest,
    ) -> main_models.SendChatappMessageResponse:
        runtime = RuntimeOptions()
        return self.send_chatapp_message_with_options(request, runtime)

    async def send_chatapp_message_async(
        self,
        request: main_models.SendChatappMessageRequest,
    ) -> main_models.SendChatappMessageResponse:
        runtime = RuntimeOptions()
        return await self.send_chatapp_message_with_options_async(request, runtime)

    def sync_flow_with_options(
        self,
        request: main_models.SyncFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_flow_with_options_async(
        self,
        request: main_models.SyncFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_flow(
        self,
        request: main_models.SyncFlowRequest,
    ) -> main_models.SyncFlowResponse:
        runtime = RuntimeOptions()
        return self.sync_flow_with_options(request, runtime)

    async def sync_flow_async(
        self,
        request: main_models.SyncFlowRequest,
    ) -> main_models.SyncFlowResponse:
        runtime = RuntimeOptions()
        return await self.sync_flow_with_options_async(request, runtime)

    def sync_message_campaign_with_options(
        self,
        request: main_models.SyncMessageCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncMessageCampaignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ad_account_id):
            query['AdAccountId'] = request.ad_account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncMessageCampaign',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncMessageCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_message_campaign_with_options_async(
        self,
        request: main_models.SyncMessageCampaignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncMessageCampaignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ad_account_id):
            query['AdAccountId'] = request.ad_account_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncMessageCampaign',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncMessageCampaignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_message_campaign(
        self,
        request: main_models.SyncMessageCampaignRequest,
    ) -> main_models.SyncMessageCampaignResponse:
        runtime = RuntimeOptions()
        return self.sync_message_campaign_with_options(request, runtime)

    async def sync_message_campaign_async(
        self,
        request: main_models.SyncMessageCampaignRequest,
    ) -> main_models.SyncMessageCampaignResponse:
        runtime = RuntimeOptions()
        return await self.sync_message_campaign_with_options_async(request, runtime)

    def sync_messenger_subscription_token_with_options(
        self,
        request: main_models.SyncMessengerSubscriptionTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncMessengerSubscriptionTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.custom_audience_id):
            query['CustomAudienceId'] = request.custom_audience_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.token_type):
            query['TokenType'] = request.token_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncMessengerSubscriptionToken',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncMessengerSubscriptionTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_messenger_subscription_token_with_options_async(
        self,
        request: main_models.SyncMessengerSubscriptionTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncMessengerSubscriptionTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.custom_audience_id):
            query['CustomAudienceId'] = request.custom_audience_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_id):
            query['PageId'] = request.page_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.token_type):
            query['TokenType'] = request.token_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncMessengerSubscriptionToken',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncMessengerSubscriptionTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_messenger_subscription_token(
        self,
        request: main_models.SyncMessengerSubscriptionTokenRequest,
    ) -> main_models.SyncMessengerSubscriptionTokenResponse:
        runtime = RuntimeOptions()
        return self.sync_messenger_subscription_token_with_options(request, runtime)

    async def sync_messenger_subscription_token_async(
        self,
        request: main_models.SyncMessengerSubscriptionTokenRequest,
    ) -> main_models.SyncMessengerSubscriptionTokenResponse:
        runtime = RuntimeOptions()
        return await self.sync_messenger_subscription_token_with_options_async(request, runtime)

    def trigger_chat_flow_with_options(
        self,
        tmp_req: main_models.TriggerChatFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TriggerChatFlowResponse:
        tmp_req.validate()
        request = main_models.TriggerChatFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data):
            request.data_shrink = Utils.array_to_string_with_specified_style(tmp_req.data, 'Data', 'json')
        query = {}
        if not DaraCore.is_null(request.claim_time_millis):
            query['ClaimTimeMillis'] = request.claim_time_millis
        if not DaraCore.is_null(request.data_shrink):
            query['Data'] = request.data_shrink
        if not DaraCore.is_null(request.discard_time_millis):
            query['DiscardTimeMillis'] = request.discard_time_millis
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TriggerChatFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerChatFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_chat_flow_with_options_async(
        self,
        tmp_req: main_models.TriggerChatFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TriggerChatFlowResponse:
        tmp_req.validate()
        request = main_models.TriggerChatFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data):
            request.data_shrink = Utils.array_to_string_with_specified_style(tmp_req.data, 'Data', 'json')
        query = {}
        if not DaraCore.is_null(request.claim_time_millis):
            query['ClaimTimeMillis'] = request.claim_time_millis
        if not DaraCore.is_null(request.data_shrink):
            query['Data'] = request.data_shrink
        if not DaraCore.is_null(request.discard_time_millis):
            query['DiscardTimeMillis'] = request.discard_time_millis
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TriggerChatFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerChatFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_chat_flow(
        self,
        request: main_models.TriggerChatFlowRequest,
    ) -> main_models.TriggerChatFlowResponse:
        runtime = RuntimeOptions()
        return self.trigger_chat_flow_with_options(request, runtime)

    async def trigger_chat_flow_async(
        self,
        request: main_models.TriggerChatFlowRequest,
    ) -> main_models.TriggerChatFlowResponse:
        runtime = RuntimeOptions()
        return await self.trigger_chat_flow_with_options_async(request, runtime)

    def unbind_dm_account_with_options(
        self,
        request: main_models.UnbindDmAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindDmAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindDmAccount',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindDmAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_dm_account_with_options_async(
        self,
        request: main_models.UnbindDmAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindDmAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindDmAccount',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindDmAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_dm_account(
        self,
        request: main_models.UnbindDmAccountRequest,
    ) -> main_models.UnbindDmAccountResponse:
        runtime = RuntimeOptions()
        return self.unbind_dm_account_with_options(request, runtime)

    async def unbind_dm_account_async(
        self,
        request: main_models.UnbindDmAccountRequest,
    ) -> main_models.UnbindDmAccountResponse:
        runtime = RuntimeOptions()
        return await self.unbind_dm_account_with_options_async(request, runtime)

    def update_account_webhook_with_options(
        self,
        request: main_models.UpdateAccountWebhookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAccountWebhookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.http_flag):
            query['HttpFlag'] = request.http_flag
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.queue_flag):
            query['QueueFlag'] = request.queue_flag
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status_callback_url):
            query['StatusCallbackUrl'] = request.status_callback_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccountWebhook',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAccountWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_account_webhook_with_options_async(
        self,
        request: main_models.UpdateAccountWebhookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAccountWebhookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.http_flag):
            query['HttpFlag'] = request.http_flag
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.queue_flag):
            query['QueueFlag'] = request.queue_flag
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status_callback_url):
            query['StatusCallbackUrl'] = request.status_callback_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccountWebhook',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAccountWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_account_webhook(
        self,
        request: main_models.UpdateAccountWebhookRequest,
    ) -> main_models.UpdateAccountWebhookResponse:
        runtime = RuntimeOptions()
        return self.update_account_webhook_with_options(request, runtime)

    async def update_account_webhook_async(
        self,
        request: main_models.UpdateAccountWebhookRequest,
    ) -> main_models.UpdateAccountWebhookResponse:
        runtime = RuntimeOptions()
        return await self.update_account_webhook_with_options_async(request, runtime)

    def update_audit_request_with_options(
        self,
        tmp_req: main_models.UpdateAuditRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAuditRequestResponse:
        tmp_req.validate()
        request = main_models.UpdateAuditRequestShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.audit_record):
            request.audit_record_shrink = Utils.array_to_string_with_specified_style(tmp_req.audit_record, 'AuditRecord', 'json')
        query = {}
        if not DaraCore.is_null(request.audit_record_shrink):
            query['AuditRecord'] = request.audit_record_shrink
        if not DaraCore.is_null(request.audit_result):
            query['AuditResult'] = request.audit_result
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.request_no):
            query['RequestNo'] = request.request_no
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAuditRequest',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAuditRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_audit_request_with_options_async(
        self,
        tmp_req: main_models.UpdateAuditRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAuditRequestResponse:
        tmp_req.validate()
        request = main_models.UpdateAuditRequestShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.audit_record):
            request.audit_record_shrink = Utils.array_to_string_with_specified_style(tmp_req.audit_record, 'AuditRecord', 'json')
        query = {}
        if not DaraCore.is_null(request.audit_record_shrink):
            query['AuditRecord'] = request.audit_record_shrink
        if not DaraCore.is_null(request.audit_result):
            query['AuditResult'] = request.audit_result
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.request_no):
            query['RequestNo'] = request.request_no
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAuditRequest',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAuditRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_audit_request(
        self,
        request: main_models.UpdateAuditRequestRequest,
    ) -> main_models.UpdateAuditRequestResponse:
        runtime = RuntimeOptions()
        return self.update_audit_request_with_options(request, runtime)

    async def update_audit_request_async(
        self,
        request: main_models.UpdateAuditRequestRequest,
    ) -> main_models.UpdateAuditRequestResponse:
        runtime = RuntimeOptions()
        return await self.update_audit_request_with_options_async(request, runtime)

    def update_chat_flow_with_options(
        self,
        tmp_req: main_models.UpdateChatFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateChatFlowResponse:
        tmp_req.validate()
        request = main_models.UpdateChatFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateChatFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateChatFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_chat_flow_with_options_async(
        self,
        tmp_req: main_models.UpdateChatFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateChatFlowResponse:
        tmp_req.validate()
        request = main_models.UpdateChatFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateChatFlow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateChatFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_chat_flow(
        self,
        request: main_models.UpdateChatFlowRequest,
    ) -> main_models.UpdateChatFlowResponse:
        runtime = RuntimeOptions()
        return self.update_chat_flow_with_options(request, runtime)

    async def update_chat_flow_async(
        self,
        request: main_models.UpdateChatFlowRequest,
    ) -> main_models.UpdateChatFlowResponse:
        runtime = RuntimeOptions()
        return await self.update_chat_flow_with_options_async(request, runtime)

    def update_chat_flow_log_setting_with_options(
        self,
        request: main_models.UpdateChatFlowLogSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateChatFlowLogSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateChatFlowLogSetting',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateChatFlowLogSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_chat_flow_log_setting_with_options_async(
        self,
        request: main_models.UpdateChatFlowLogSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateChatFlowLogSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateChatFlowLogSetting',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateChatFlowLogSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_chat_flow_log_setting(
        self,
        request: main_models.UpdateChatFlowLogSettingRequest,
    ) -> main_models.UpdateChatFlowLogSettingResponse:
        runtime = RuntimeOptions()
        return self.update_chat_flow_log_setting_with_options(request, runtime)

    async def update_chat_flow_log_setting_async(
        self,
        request: main_models.UpdateChatFlowLogSettingRequest,
    ) -> main_models.UpdateChatFlowLogSettingResponse:
        runtime = RuntimeOptions()
        return await self.update_chat_flow_log_setting_with_options_async(request, runtime)

    def update_chat_group_with_options(
        self,
        request: main_models.UpdateChatGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateChatGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.profile_picture_file):
            query['ProfilePictureFile'] = request.profile_picture_file
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.subject):
            query['Subject'] = request.subject
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateChatGroup',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateChatGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_chat_group_with_options_async(
        self,
        request: main_models.UpdateChatGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateChatGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_number):
            query['BusinessNumber'] = request.business_number
        if not DaraCore.is_null(request.channel_type):
            query['ChannelType'] = request.channel_type
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.profile_picture_file):
            query['ProfilePictureFile'] = request.profile_picture_file
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.subject):
            query['Subject'] = request.subject
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateChatGroup',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateChatGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_chat_group(
        self,
        request: main_models.UpdateChatGroupRequest,
    ) -> main_models.UpdateChatGroupResponse:
        runtime = RuntimeOptions()
        return self.update_chat_group_with_options(request, runtime)

    async def update_chat_group_async(
        self,
        request: main_models.UpdateChatGroupRequest,
    ) -> main_models.UpdateChatGroupResponse:
        runtime = RuntimeOptions()
        return await self.update_chat_group_with_options_async(request, runtime)

    def update_commerce_setting_with_options(
        self,
        request: main_models.UpdateCommerceSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCommerceSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cart_enable):
            query['CartEnable'] = request.cart_enable
        if not DaraCore.is_null(request.catalog_visible):
            query['CatalogVisible'] = request.catalog_visible
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCommerceSetting',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCommerceSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_commerce_setting_with_options_async(
        self,
        request: main_models.UpdateCommerceSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCommerceSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cart_enable):
            query['CartEnable'] = request.cart_enable
        if not DaraCore.is_null(request.catalog_visible):
            query['CatalogVisible'] = request.catalog_visible
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCommerceSetting',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCommerceSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_commerce_setting(
        self,
        request: main_models.UpdateCommerceSettingRequest,
    ) -> main_models.UpdateCommerceSettingResponse:
        runtime = RuntimeOptions()
        return self.update_commerce_setting_with_options(request, runtime)

    async def update_commerce_setting_async(
        self,
        request: main_models.UpdateCommerceSettingRequest,
    ) -> main_models.UpdateCommerceSettingResponse:
        runtime = RuntimeOptions()
        return await self.update_commerce_setting_with_options_async(request, runtime)

    def update_contact_by_id_with_options(
        self,
        tmp_req: main_models.UpdateContactByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateContactByIdResponse:
        tmp_req.validate()
        request = main_models.UpdateContactByIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.contact_details):
            query['ContactDetails'] = request.contact_details
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateContactById',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateContactByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_contact_by_id_with_options_async(
        self,
        tmp_req: main_models.UpdateContactByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateContactByIdResponse:
        tmp_req.validate()
        request = main_models.UpdateContactByIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.contact_details):
            query['ContactDetails'] = request.contact_details
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateContactById',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateContactByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_contact_by_id(
        self,
        request: main_models.UpdateContactByIdRequest,
    ) -> main_models.UpdateContactByIdResponse:
        runtime = RuntimeOptions()
        return self.update_contact_by_id_with_options(request, runtime)

    async def update_contact_by_id_async(
        self,
        request: main_models.UpdateContactByIdRequest,
    ) -> main_models.UpdateContactByIdResponse:
        runtime = RuntimeOptions()
        return await self.update_contact_by_id_with_options_async(request, runtime)

    def update_conversational_automation_with_options(
        self,
        tmp_req: main_models.UpdateConversationalAutomationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConversationalAutomationResponse:
        tmp_req.validate()
        request = main_models.UpdateConversationalAutomationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.commands):
            request.commands_shrink = Utils.array_to_string_with_specified_style(tmp_req.commands, 'Commands', 'json')
        if not DaraCore.is_null(tmp_req.prompts):
            request.prompts_shrink = Utils.array_to_string_with_specified_style(tmp_req.prompts, 'Prompts', 'json')
        query = {}
        if not DaraCore.is_null(request.commands_shrink):
            query['Commands'] = request.commands_shrink
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.enable_welcome_message):
            query['EnableWelcomeMessage'] = request.enable_welcome_message
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.prompts_shrink):
            query['Prompts'] = request.prompts_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConversationalAutomation',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConversationalAutomationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_conversational_automation_with_options_async(
        self,
        tmp_req: main_models.UpdateConversationalAutomationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConversationalAutomationResponse:
        tmp_req.validate()
        request = main_models.UpdateConversationalAutomationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.commands):
            request.commands_shrink = Utils.array_to_string_with_specified_style(tmp_req.commands, 'Commands', 'json')
        if not DaraCore.is_null(tmp_req.prompts):
            request.prompts_shrink = Utils.array_to_string_with_specified_style(tmp_req.prompts, 'Prompts', 'json')
        query = {}
        if not DaraCore.is_null(request.commands_shrink):
            query['Commands'] = request.commands_shrink
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.enable_welcome_message):
            query['EnableWelcomeMessage'] = request.enable_welcome_message
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.prompts_shrink):
            query['Prompts'] = request.prompts_shrink
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConversationalAutomation',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConversationalAutomationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_conversational_automation(
        self,
        request: main_models.UpdateConversationalAutomationRequest,
    ) -> main_models.UpdateConversationalAutomationResponse:
        runtime = RuntimeOptions()
        return self.update_conversational_automation_with_options(request, runtime)

    async def update_conversational_automation_async(
        self,
        request: main_models.UpdateConversationalAutomationRequest,
    ) -> main_models.UpdateConversationalAutomationResponse:
        runtime = RuntimeOptions()
        return await self.update_conversational_automation_with_options_async(request, runtime)

    def update_flow_jsonasset_with_options(
        self,
        request: main_models.UpdateFlowJSONAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFlowJSONAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFlowJSONAsset',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFlowJSONAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_flow_jsonasset_with_options_async(
        self,
        request: main_models.UpdateFlowJSONAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFlowJSONAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.flow_id):
            query['FlowId'] = request.flow_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFlowJSONAsset',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFlowJSONAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_flow_jsonasset(
        self,
        request: main_models.UpdateFlowJSONAssetRequest,
    ) -> main_models.UpdateFlowJSONAssetResponse:
        runtime = RuntimeOptions()
        return self.update_flow_jsonasset_with_options(request, runtime)

    async def update_flow_jsonasset_async(
        self,
        request: main_models.UpdateFlowJSONAssetRequest,
    ) -> main_models.UpdateFlowJSONAssetResponse:
        runtime = RuntimeOptions()
        return await self.update_flow_jsonasset_with_options_async(request, runtime)

    def update_flow_version_with_options(
        self,
        tmp_req: main_models.UpdateFlowVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFlowVersionResponse:
        tmp_req.validate()
        request = main_models.UpdateFlowVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not DaraCore.is_null(request.flow_view_model):
            query['FlowViewModel'] = request.flow_view_model
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFlowVersion',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFlowVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_flow_version_with_options_async(
        self,
        tmp_req: main_models.UpdateFlowVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFlowVersionResponse:
        tmp_req.validate()
        request = main_models.UpdateFlowVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_extend):
            request.biz_extend_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_extend, 'BizExtend', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_code):
            query['BizCode'] = request.biz_code
        if not DaraCore.is_null(request.biz_extend_shrink):
            query['BizExtend'] = request.biz_extend_shrink
        if not DaraCore.is_null(request.flow_code):
            query['FlowCode'] = request.flow_code
        if not DaraCore.is_null(request.flow_version):
            query['FlowVersion'] = request.flow_version
        if not DaraCore.is_null(request.flow_view_model):
            query['FlowViewModel'] = request.flow_view_model
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFlowVersion',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFlowVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_flow_version(
        self,
        request: main_models.UpdateFlowVersionRequest,
    ) -> main_models.UpdateFlowVersionResponse:
        runtime = RuntimeOptions()
        return self.update_flow_version_with_options(request, runtime)

    async def update_flow_version_async(
        self,
        request: main_models.UpdateFlowVersionRequest,
    ) -> main_models.UpdateFlowVersionResponse:
        runtime = RuntimeOptions()
        return await self.update_flow_version_with_options_async(request, runtime)

    def update_group_name_with_options(
        self,
        request: main_models.UpdateGroupNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGroupNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGroupName',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGroupNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_group_name_with_options_async(
        self,
        request: main_models.UpdateGroupNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGroupNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGroupName',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGroupNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_group_name(
        self,
        request: main_models.UpdateGroupNameRequest,
    ) -> main_models.UpdateGroupNameResponse:
        runtime = RuntimeOptions()
        return self.update_group_name_with_options(request, runtime)

    async def update_group_name_async(
        self,
        request: main_models.UpdateGroupNameRequest,
    ) -> main_models.UpdateGroupNameResponse:
        runtime = RuntimeOptions()
        return await self.update_group_name_with_options_async(request, runtime)

    def update_instance_with_options(
        self,
        request: main_models.UpdateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_mail):
            query['ContactMail'] = request.contact_mail
        if not DaraCore.is_null(request.country_id):
            query['CountryId'] = request.country_id
        if not DaraCore.is_null(request.facebook_bm_id):
            query['FacebookBmId'] = request.facebook_bm_id
        if not DaraCore.is_null(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.is_confirm_audit):
            query['IsConfirmAudit'] = request.is_confirm_audit
        if not DaraCore.is_null(request.isv_terms):
            query['IsvTerms'] = request.isv_terms
        if not DaraCore.is_null(request.office_address):
            query['OfficeAddress'] = request.office_address
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        request: main_models.UpdateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_mail):
            query['ContactMail'] = request.contact_mail
        if not DaraCore.is_null(request.country_id):
            query['CountryId'] = request.country_id
        if not DaraCore.is_null(request.facebook_bm_id):
            query['FacebookBmId'] = request.facebook_bm_id
        if not DaraCore.is_null(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.is_confirm_audit):
            query['IsConfirmAudit'] = request.is_confirm_audit
        if not DaraCore.is_null(request.isv_terms):
            query['IsvTerms'] = request.isv_terms
        if not DaraCore.is_null(request.office_address):
            query['OfficeAddress'] = request.office_address
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        return self.update_instance_with_options(request, runtime)

    async def update_instance_async(
        self,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        return await self.update_instance_with_options_async(request, runtime)

    def update_marketing_flow_with_options(
        self,
        tmp_req: main_models.UpdateMarketingFLowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMarketingFLowResponse:
        tmp_req.validate()
        request = main_models.UpdateMarketingFLowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        query = {}
        if not DaraCore.is_null(request.activity_code):
            query['ActivityCode'] = request.activity_code
        if not DaraCore.is_null(request.activity_desc):
            query['ActivityDesc'] = request.activity_desc
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.activity_name):
            query['ActivityName'] = request.activity_name
        if not DaraCore.is_null(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.execution_type):
            query['ExecutionType'] = request.execution_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.param_flag):
            query['ParamFlag'] = request.param_flag
        if not DaraCore.is_null(request.params_shrink):
            query['Params'] = request.params_shrink
        if not DaraCore.is_null(request.related_flow_code):
            query['RelatedFlowCode'] = request.related_flow_code
        if not DaraCore.is_null(request.related_flow_name):
            query['RelatedFlowName'] = request.related_flow_name
        if not DaraCore.is_null(request.related_group_id):
            query['RelatedGroupId'] = request.related_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMarketingFLow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMarketingFLowResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_marketing_flow_with_options_async(
        self,
        tmp_req: main_models.UpdateMarketingFLowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMarketingFLowResponse:
        tmp_req.validate()
        request = main_models.UpdateMarketingFLowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        query = {}
        if not DaraCore.is_null(request.activity_code):
            query['ActivityCode'] = request.activity_code
        if not DaraCore.is_null(request.activity_desc):
            query['ActivityDesc'] = request.activity_desc
        if not DaraCore.is_null(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not DaraCore.is_null(request.activity_name):
            query['ActivityName'] = request.activity_name
        if not DaraCore.is_null(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.execution_type):
            query['ExecutionType'] = request.execution_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.param_flag):
            query['ParamFlag'] = request.param_flag
        if not DaraCore.is_null(request.params_shrink):
            query['Params'] = request.params_shrink
        if not DaraCore.is_null(request.related_flow_code):
            query['RelatedFlowCode'] = request.related_flow_code
        if not DaraCore.is_null(request.related_flow_name):
            query['RelatedFlowName'] = request.related_flow_name
        if not DaraCore.is_null(request.related_group_id):
            query['RelatedGroupId'] = request.related_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMarketingFLow',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMarketingFLowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_marketing_flow(
        self,
        request: main_models.UpdateMarketingFLowRequest,
    ) -> main_models.UpdateMarketingFLowResponse:
        runtime = RuntimeOptions()
        return self.update_marketing_flow_with_options(request, runtime)

    async def update_marketing_flow_async(
        self,
        request: main_models.UpdateMarketingFLowRequest,
    ) -> main_models.UpdateMarketingFLowResponse:
        runtime = RuntimeOptions()
        return await self.update_marketing_flow_with_options_async(request, runtime)

    def update_phone_encryption_public_key_with_options(
        self,
        request: main_models.UpdatePhoneEncryptionPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePhoneEncryptionPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.encryption_public_key):
            query['EncryptionPublicKey'] = request.encryption_public_key
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePhoneEncryptionPublicKey',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePhoneEncryptionPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_phone_encryption_public_key_with_options_async(
        self,
        request: main_models.UpdatePhoneEncryptionPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePhoneEncryptionPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.encryption_public_key):
            query['EncryptionPublicKey'] = request.encryption_public_key
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePhoneEncryptionPublicKey',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePhoneEncryptionPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_phone_encryption_public_key(
        self,
        request: main_models.UpdatePhoneEncryptionPublicKeyRequest,
    ) -> main_models.UpdatePhoneEncryptionPublicKeyResponse:
        runtime = RuntimeOptions()
        return self.update_phone_encryption_public_key_with_options(request, runtime)

    async def update_phone_encryption_public_key_async(
        self,
        request: main_models.UpdatePhoneEncryptionPublicKeyRequest,
    ) -> main_models.UpdatePhoneEncryptionPublicKeyResponse:
        runtime = RuntimeOptions()
        return await self.update_phone_encryption_public_key_with_options_async(request, runtime)

    def update_phone_message_qrdl_with_options(
        self,
        request: main_models.UpdatePhoneMessageQrdlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePhoneMessageQrdlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.generate_qr_image):
            query['GenerateQrImage'] = request.generate_qr_image
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.prefilled_message):
            query['PrefilledMessage'] = request.prefilled_message
        if not DaraCore.is_null(request.qrdl_code):
            query['QrdlCode'] = request.qrdl_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePhoneMessageQrdl',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePhoneMessageQrdlResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_phone_message_qrdl_with_options_async(
        self,
        request: main_models.UpdatePhoneMessageQrdlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePhoneMessageQrdlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.generate_qr_image):
            query['GenerateQrImage'] = request.generate_qr_image
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.prefilled_message):
            query['PrefilledMessage'] = request.prefilled_message
        if not DaraCore.is_null(request.qrdl_code):
            query['QrdlCode'] = request.qrdl_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePhoneMessageQrdl',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePhoneMessageQrdlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_phone_message_qrdl(
        self,
        request: main_models.UpdatePhoneMessageQrdlRequest,
    ) -> main_models.UpdatePhoneMessageQrdlResponse:
        runtime = RuntimeOptions()
        return self.update_phone_message_qrdl_with_options(request, runtime)

    async def update_phone_message_qrdl_async(
        self,
        request: main_models.UpdatePhoneMessageQrdlRequest,
    ) -> main_models.UpdatePhoneMessageQrdlResponse:
        runtime = RuntimeOptions()
        return await self.update_phone_message_qrdl_with_options_async(request, runtime)

    def update_phone_webhook_with_options(
        self,
        request: main_models.UpdatePhoneWebhookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePhoneWebhookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.http_flag):
            query['HttpFlag'] = request.http_flag
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.queue_flag):
            query['QueueFlag'] = request.queue_flag
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status_callback_url):
            query['StatusCallbackUrl'] = request.status_callback_url
        if not DaraCore.is_null(request.up_callback_url):
            query['UpCallbackUrl'] = request.up_callback_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePhoneWebhook',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePhoneWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_phone_webhook_with_options_async(
        self,
        request: main_models.UpdatePhoneWebhookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePhoneWebhookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.http_flag):
            query['HttpFlag'] = request.http_flag
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.queue_flag):
            query['QueueFlag'] = request.queue_flag
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status_callback_url):
            query['StatusCallbackUrl'] = request.status_callback_url
        if not DaraCore.is_null(request.up_callback_url):
            query['UpCallbackUrl'] = request.up_callback_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePhoneWebhook',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePhoneWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_phone_webhook(
        self,
        request: main_models.UpdatePhoneWebhookRequest,
    ) -> main_models.UpdatePhoneWebhookResponse:
        runtime = RuntimeOptions()
        return self.update_phone_webhook_with_options(request, runtime)

    async def update_phone_webhook_async(
        self,
        request: main_models.UpdatePhoneWebhookRequest,
    ) -> main_models.UpdatePhoneWebhookResponse:
        runtime = RuntimeOptions()
        return await self.update_phone_webhook_with_options_async(request, runtime)

    def update_waba_mml_status_with_options(
        self,
        request: main_models.UpdateWabaMmlStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWabaMmlStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWabaMmlStatus',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWabaMmlStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_waba_mml_status_with_options_async(
        self,
        request: main_models.UpdateWabaMmlStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWabaMmlStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWabaMmlStatus',
            version = '2020-06-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWabaMmlStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_waba_mml_status(
        self,
        request: main_models.UpdateWabaMmlStatusRequest,
    ) -> main_models.UpdateWabaMmlStatusResponse:
        runtime = RuntimeOptions()
        return self.update_waba_mml_status_with_options(request, runtime)

    async def update_waba_mml_status_async(
        self,
        request: main_models.UpdateWabaMmlStatusRequest,
    ) -> main_models.UpdateWabaMmlStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_waba_mml_status_with_options_async(request, runtime)
