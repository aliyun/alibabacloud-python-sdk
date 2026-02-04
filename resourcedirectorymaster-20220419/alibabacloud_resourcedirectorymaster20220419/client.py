# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('resourcedirectorymaster', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def accept_handshake_with_options(
        self,
        request: main_models.AcceptHandshakeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AcceptHandshakeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AcceptHandshake',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AcceptHandshakeResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_handshake_with_options_async(
        self,
        request: main_models.AcceptHandshakeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AcceptHandshakeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AcceptHandshake',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AcceptHandshakeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_handshake(
        self,
        request: main_models.AcceptHandshakeRequest,
    ) -> main_models.AcceptHandshakeResponse:
        runtime = RuntimeOptions()
        return self.accept_handshake_with_options(request, runtime)

    async def accept_handshake_async(
        self,
        request: main_models.AcceptHandshakeRequest,
    ) -> main_models.AcceptHandshakeResponse:
        runtime = RuntimeOptions()
        return await self.accept_handshake_with_options_async(request, runtime)

    def add_message_contact_with_options(
        self,
        request: main_models.AddMessageContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddMessageContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email_address):
            query['EmailAddress'] = request.email_address
        if not DaraCore.is_null(request.message_types):
            query['MessageTypes'] = request.message_types
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddMessageContact',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMessageContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_message_contact_with_options_async(
        self,
        request: main_models.AddMessageContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddMessageContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email_address):
            query['EmailAddress'] = request.email_address
        if not DaraCore.is_null(request.message_types):
            query['MessageTypes'] = request.message_types
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddMessageContact',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMessageContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_message_contact(
        self,
        request: main_models.AddMessageContactRequest,
    ) -> main_models.AddMessageContactResponse:
        runtime = RuntimeOptions()
        return self.add_message_contact_with_options(request, runtime)

    async def add_message_contact_async(
        self,
        request: main_models.AddMessageContactRequest,
    ) -> main_models.AddMessageContactResponse:
        runtime = RuntimeOptions()
        return await self.add_message_contact_with_options_async(request, runtime)

    def associate_members_with_options(
        self,
        request: main_models.AssociateMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.members):
            query['Members'] = request.members
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateMembers',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_members_with_options_async(
        self,
        request: main_models.AssociateMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.members):
            query['Members'] = request.members
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateMembers',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_members(
        self,
        request: main_models.AssociateMembersRequest,
    ) -> main_models.AssociateMembersResponse:
        runtime = RuntimeOptions()
        return self.associate_members_with_options(request, runtime)

    async def associate_members_async(
        self,
        request: main_models.AssociateMembersRequest,
    ) -> main_models.AssociateMembersResponse:
        runtime = RuntimeOptions()
        return await self.associate_members_with_options_async(request, runtime)

    def attach_control_policy_with_options(
        self,
        request: main_models.AttachControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachControlPolicy',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_control_policy_with_options_async(
        self,
        request: main_models.AttachControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachControlPolicy',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_control_policy(
        self,
        request: main_models.AttachControlPolicyRequest,
    ) -> main_models.AttachControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.attach_control_policy_with_options(request, runtime)

    async def attach_control_policy_async(
        self,
        request: main_models.AttachControlPolicyRequest,
    ) -> main_models.AttachControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.attach_control_policy_with_options_async(request, runtime)

    def bind_secure_mobile_phone_with_options(
        self,
        request: main_models.BindSecureMobilePhoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindSecureMobilePhoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        if not DaraCore.is_null(request.verification_code):
            query['VerificationCode'] = request.verification_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindSecureMobilePhone',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindSecureMobilePhoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_secure_mobile_phone_with_options_async(
        self,
        request: main_models.BindSecureMobilePhoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindSecureMobilePhoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        if not DaraCore.is_null(request.verification_code):
            query['VerificationCode'] = request.verification_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindSecureMobilePhone',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindSecureMobilePhoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_secure_mobile_phone(
        self,
        request: main_models.BindSecureMobilePhoneRequest,
    ) -> main_models.BindSecureMobilePhoneResponse:
        runtime = RuntimeOptions()
        return self.bind_secure_mobile_phone_with_options(request, runtime)

    async def bind_secure_mobile_phone_async(
        self,
        request: main_models.BindSecureMobilePhoneRequest,
    ) -> main_models.BindSecureMobilePhoneResponse:
        runtime = RuntimeOptions()
        return await self.bind_secure_mobile_phone_with_options_async(request, runtime)

    def cancel_change_account_email_with_options(
        self,
        request: main_models.CancelChangeAccountEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelChangeAccountEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelChangeAccountEmail',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelChangeAccountEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_change_account_email_with_options_async(
        self,
        request: main_models.CancelChangeAccountEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelChangeAccountEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelChangeAccountEmail',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelChangeAccountEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_change_account_email(
        self,
        request: main_models.CancelChangeAccountEmailRequest,
    ) -> main_models.CancelChangeAccountEmailResponse:
        runtime = RuntimeOptions()
        return self.cancel_change_account_email_with_options(request, runtime)

    async def cancel_change_account_email_async(
        self,
        request: main_models.CancelChangeAccountEmailRequest,
    ) -> main_models.CancelChangeAccountEmailResponse:
        runtime = RuntimeOptions()
        return await self.cancel_change_account_email_with_options_async(request, runtime)

    def cancel_handshake_with_options(
        self,
        request: main_models.CancelHandshakeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelHandshakeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelHandshake',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelHandshakeResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_handshake_with_options_async(
        self,
        request: main_models.CancelHandshakeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelHandshakeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelHandshake',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelHandshakeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_handshake(
        self,
        request: main_models.CancelHandshakeRequest,
    ) -> main_models.CancelHandshakeResponse:
        runtime = RuntimeOptions()
        return self.cancel_handshake_with_options(request, runtime)

    async def cancel_handshake_async(
        self,
        request: main_models.CancelHandshakeRequest,
    ) -> main_models.CancelHandshakeResponse:
        runtime = RuntimeOptions()
        return await self.cancel_handshake_with_options_async(request, runtime)

    def cancel_message_contact_update_with_options(
        self,
        request: main_models.CancelMessageContactUpdateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelMessageContactUpdateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.email_address):
            query['EmailAddress'] = request.email_address
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelMessageContactUpdate',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelMessageContactUpdateResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_message_contact_update_with_options_async(
        self,
        request: main_models.CancelMessageContactUpdateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelMessageContactUpdateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.email_address):
            query['EmailAddress'] = request.email_address
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelMessageContactUpdate',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelMessageContactUpdateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_message_contact_update(
        self,
        request: main_models.CancelMessageContactUpdateRequest,
    ) -> main_models.CancelMessageContactUpdateResponse:
        runtime = RuntimeOptions()
        return self.cancel_message_contact_update_with_options(request, runtime)

    async def cancel_message_contact_update_async(
        self,
        request: main_models.CancelMessageContactUpdateRequest,
    ) -> main_models.CancelMessageContactUpdateResponse:
        runtime = RuntimeOptions()
        return await self.cancel_message_contact_update_with_options_async(request, runtime)

    def change_account_email_with_options(
        self,
        request: main_models.ChangeAccountEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeAccountEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeAccountEmail',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeAccountEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_account_email_with_options_async(
        self,
        request: main_models.ChangeAccountEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeAccountEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeAccountEmail',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeAccountEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_account_email(
        self,
        request: main_models.ChangeAccountEmailRequest,
    ) -> main_models.ChangeAccountEmailResponse:
        runtime = RuntimeOptions()
        return self.change_account_email_with_options(request, runtime)

    async def change_account_email_async(
        self,
        request: main_models.ChangeAccountEmailRequest,
    ) -> main_models.ChangeAccountEmailResponse:
        runtime = RuntimeOptions()
        return await self.change_account_email_with_options_async(request, runtime)

    def check_account_delete_with_options(
        self,
        request: main_models.CheckAccountDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckAccountDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckAccountDelete',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckAccountDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_account_delete_with_options_async(
        self,
        request: main_models.CheckAccountDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckAccountDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckAccountDelete',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckAccountDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_account_delete(
        self,
        request: main_models.CheckAccountDeleteRequest,
    ) -> main_models.CheckAccountDeleteResponse:
        runtime = RuntimeOptions()
        return self.check_account_delete_with_options(request, runtime)

    async def check_account_delete_async(
        self,
        request: main_models.CheckAccountDeleteRequest,
    ) -> main_models.CheckAccountDeleteResponse:
        runtime = RuntimeOptions()
        return await self.check_account_delete_with_options_async(request, runtime)

    def create_control_policy_with_options(
        self,
        request: main_models.CreateControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.effect_scope):
            query['EffectScope'] = request.effect_scope
        if not DaraCore.is_null(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateControlPolicy',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_control_policy_with_options_async(
        self,
        request: main_models.CreateControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.effect_scope):
            query['EffectScope'] = request.effect_scope
        if not DaraCore.is_null(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateControlPolicy',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_control_policy(
        self,
        request: main_models.CreateControlPolicyRequest,
    ) -> main_models.CreateControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_control_policy_with_options(request, runtime)

    async def create_control_policy_async(
        self,
        request: main_models.CreateControlPolicyRequest,
    ) -> main_models.CreateControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_control_policy_with_options_async(request, runtime)

    def create_folder_with_options(
        self,
        request: main_models.CreateFolderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFolderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.folder_name):
            query['FolderName'] = request.folder_name
        if not DaraCore.is_null(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFolder',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_folder_with_options_async(
        self,
        request: main_models.CreateFolderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFolderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.folder_name):
            query['FolderName'] = request.folder_name
        if not DaraCore.is_null(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFolder',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_folder(
        self,
        request: main_models.CreateFolderRequest,
    ) -> main_models.CreateFolderResponse:
        runtime = RuntimeOptions()
        return self.create_folder_with_options(request, runtime)

    async def create_folder_async(
        self,
        request: main_models.CreateFolderRequest,
    ) -> main_models.CreateFolderResponse:
        runtime = RuntimeOptions()
        return await self.create_folder_with_options_async(request, runtime)

    def create_resource_account_with_options(
        self,
        request: main_models.CreateResourceAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name_prefix):
            query['AccountNamePrefix'] = request.account_name_prefix
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not DaraCore.is_null(request.payer_account_id):
            query['PayerAccountId'] = request.payer_account_id
        if not DaraCore.is_null(request.resell_account_type):
            query['ResellAccountType'] = request.resell_account_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_account_with_options_async(
        self,
        request: main_models.CreateResourceAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name_prefix):
            query['AccountNamePrefix'] = request.account_name_prefix
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not DaraCore.is_null(request.payer_account_id):
            query['PayerAccountId'] = request.payer_account_id
        if not DaraCore.is_null(request.resell_account_type):
            query['ResellAccountType'] = request.resell_account_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_account(
        self,
        request: main_models.CreateResourceAccountRequest,
    ) -> main_models.CreateResourceAccountResponse:
        runtime = RuntimeOptions()
        return self.create_resource_account_with_options(request, runtime)

    async def create_resource_account_async(
        self,
        request: main_models.CreateResourceAccountRequest,
    ) -> main_models.CreateResourceAccountResponse:
        runtime = RuntimeOptions()
        return await self.create_resource_account_with_options_async(request, runtime)

    def decline_handshake_with_options(
        self,
        request: main_models.DeclineHandshakeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeclineHandshakeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeclineHandshake',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeclineHandshakeResponse(),
            self.call_api(params, req, runtime)
        )

    async def decline_handshake_with_options_async(
        self,
        request: main_models.DeclineHandshakeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeclineHandshakeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeclineHandshake',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeclineHandshakeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def decline_handshake(
        self,
        request: main_models.DeclineHandshakeRequest,
    ) -> main_models.DeclineHandshakeResponse:
        runtime = RuntimeOptions()
        return self.decline_handshake_with_options(request, runtime)

    async def decline_handshake_async(
        self,
        request: main_models.DeclineHandshakeRequest,
    ) -> main_models.DeclineHandshakeResponse:
        runtime = RuntimeOptions()
        return await self.decline_handshake_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        tmp_req: main_models.DeleteAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccountResponse:
        tmp_req.validate()
        request = main_models.DeleteAccountShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.abandonable_check_id):
            request.abandonable_check_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.abandonable_check_id, 'AbandonableCheckId', 'json')
        query = {}
        if not DaraCore.is_null(request.abandonable_check_id_shrink):
            query['AbandonableCheckId'] = request.abandonable_check_id_shrink
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        tmp_req: main_models.DeleteAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccountResponse:
        tmp_req.validate()
        request = main_models.DeleteAccountShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.abandonable_check_id):
            request.abandonable_check_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.abandonable_check_id, 'AbandonableCheckId', 'json')
        query = {}
        if not DaraCore.is_null(request.abandonable_check_id_shrink):
            query['AbandonableCheckId'] = request.abandonable_check_id_shrink
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account(
        self,
        request: main_models.DeleteAccountRequest,
    ) -> main_models.DeleteAccountResponse:
        runtime = RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: main_models.DeleteAccountRequest,
    ) -> main_models.DeleteAccountResponse:
        runtime = RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_control_policy_with_options(
        self,
        request: main_models.DeleteControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteControlPolicy',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_control_policy_with_options_async(
        self,
        request: main_models.DeleteControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteControlPolicy',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_control_policy(
        self,
        request: main_models.DeleteControlPolicyRequest,
    ) -> main_models.DeleteControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_control_policy_with_options(request, runtime)

    async def delete_control_policy_async(
        self,
        request: main_models.DeleteControlPolicyRequest,
    ) -> main_models.DeleteControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_control_policy_with_options_async(request, runtime)

    def delete_folder_with_options(
        self,
        request: main_models.DeleteFolderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFolderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFolder',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_folder_with_options_async(
        self,
        request: main_models.DeleteFolderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFolderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFolder',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_folder(
        self,
        request: main_models.DeleteFolderRequest,
    ) -> main_models.DeleteFolderResponse:
        runtime = RuntimeOptions()
        return self.delete_folder_with_options(request, runtime)

    async def delete_folder_async(
        self,
        request: main_models.DeleteFolderRequest,
    ) -> main_models.DeleteFolderResponse:
        runtime = RuntimeOptions()
        return await self.delete_folder_with_options_async(request, runtime)

    def delete_message_contact_with_options(
        self,
        request: main_models.DeleteMessageContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMessageContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.retain_contact_in_members):
            query['RetainContactInMembers'] = request.retain_contact_in_members
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMessageContact',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMessageContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_message_contact_with_options_async(
        self,
        request: main_models.DeleteMessageContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMessageContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.retain_contact_in_members):
            query['RetainContactInMembers'] = request.retain_contact_in_members
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMessageContact',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMessageContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_message_contact(
        self,
        request: main_models.DeleteMessageContactRequest,
    ) -> main_models.DeleteMessageContactResponse:
        runtime = RuntimeOptions()
        return self.delete_message_contact_with_options(request, runtime)

    async def delete_message_contact_async(
        self,
        request: main_models.DeleteMessageContactRequest,
    ) -> main_models.DeleteMessageContactResponse:
        runtime = RuntimeOptions()
        return await self.delete_message_contact_with_options_async(request, runtime)

    def deregister_delegated_administrator_with_options(
        self,
        request: main_models.DeregisterDelegatedAdministratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeregisterDelegatedAdministratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeregisterDelegatedAdministrator',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeregisterDelegatedAdministratorResponse(),
            self.call_api(params, req, runtime)
        )

    async def deregister_delegated_administrator_with_options_async(
        self,
        request: main_models.DeregisterDelegatedAdministratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeregisterDelegatedAdministratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeregisterDelegatedAdministrator',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeregisterDelegatedAdministratorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deregister_delegated_administrator(
        self,
        request: main_models.DeregisterDelegatedAdministratorRequest,
    ) -> main_models.DeregisterDelegatedAdministratorResponse:
        runtime = RuntimeOptions()
        return self.deregister_delegated_administrator_with_options(request, runtime)

    async def deregister_delegated_administrator_async(
        self,
        request: main_models.DeregisterDelegatedAdministratorRequest,
    ) -> main_models.DeregisterDelegatedAdministratorResponse:
        runtime = RuntimeOptions()
        return await self.deregister_delegated_administrator_with_options_async(request, runtime)

    def destroy_resource_directory_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DestroyResourceDirectoryResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DestroyResourceDirectory',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DestroyResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def destroy_resource_directory_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DestroyResourceDirectoryResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DestroyResourceDirectory',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DestroyResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def destroy_resource_directory(self) -> main_models.DestroyResourceDirectoryResponse:
        runtime = RuntimeOptions()
        return self.destroy_resource_directory_with_options(runtime)

    async def destroy_resource_directory_async(self) -> main_models.DestroyResourceDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.destroy_resource_directory_with_options_async(runtime)

    def detach_control_policy_with_options(
        self,
        request: main_models.DetachControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachControlPolicy',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_control_policy_with_options_async(
        self,
        request: main_models.DetachControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachControlPolicy',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_control_policy(
        self,
        request: main_models.DetachControlPolicyRequest,
    ) -> main_models.DetachControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.detach_control_policy_with_options(request, runtime)

    async def detach_control_policy_async(
        self,
        request: main_models.DetachControlPolicyRequest,
    ) -> main_models.DetachControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.detach_control_policy_with_options_async(request, runtime)

    def disable_control_policy_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DisableControlPolicyResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DisableControlPolicy',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_control_policy_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DisableControlPolicyResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DisableControlPolicy',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_control_policy(self) -> main_models.DisableControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.disable_control_policy_with_options(runtime)

    async def disable_control_policy_async(self) -> main_models.DisableControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.disable_control_policy_with_options_async(runtime)

    def disassociate_members_with_options(
        self,
        request: main_models.DisassociateMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.members):
            query['Members'] = request.members
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateMembers',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_members_with_options_async(
        self,
        request: main_models.DisassociateMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.members):
            query['Members'] = request.members
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateMembers',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_members(
        self,
        request: main_models.DisassociateMembersRequest,
    ) -> main_models.DisassociateMembersResponse:
        runtime = RuntimeOptions()
        return self.disassociate_members_with_options(request, runtime)

    async def disassociate_members_async(
        self,
        request: main_models.DisassociateMembersRequest,
    ) -> main_models.DisassociateMembersResponse:
        runtime = RuntimeOptions()
        return await self.disassociate_members_with_options_async(request, runtime)

    def enable_control_policy_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.EnableControlPolicyResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'EnableControlPolicy',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_control_policy_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.EnableControlPolicyResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'EnableControlPolicy',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_control_policy(self) -> main_models.EnableControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.enable_control_policy_with_options(runtime)

    async def enable_control_policy_async(self) -> main_models.EnableControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.enable_control_policy_with_options_async(runtime)

    def enable_resource_directory_with_options(
        self,
        request: main_models.EnableResourceDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableResourceDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.enable_mode):
            query['EnableMode'] = request.enable_mode
        if not DaraCore.is_null(request.maname):
            query['MAName'] = request.maname
        if not DaraCore.is_null(request.masecure_mobile_phone):
            query['MASecureMobilePhone'] = request.masecure_mobile_phone
        if not DaraCore.is_null(request.verification_code):
            query['VerificationCode'] = request.verification_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableResourceDirectory',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_resource_directory_with_options_async(
        self,
        request: main_models.EnableResourceDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableResourceDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.enable_mode):
            query['EnableMode'] = request.enable_mode
        if not DaraCore.is_null(request.maname):
            query['MAName'] = request.maname
        if not DaraCore.is_null(request.masecure_mobile_phone):
            query['MASecureMobilePhone'] = request.masecure_mobile_phone
        if not DaraCore.is_null(request.verification_code):
            query['VerificationCode'] = request.verification_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableResourceDirectory',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_resource_directory(
        self,
        request: main_models.EnableResourceDirectoryRequest,
    ) -> main_models.EnableResourceDirectoryResponse:
        runtime = RuntimeOptions()
        return self.enable_resource_directory_with_options(request, runtime)

    async def enable_resource_directory_async(
        self,
        request: main_models.EnableResourceDirectoryRequest,
    ) -> main_models.EnableResourceDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.enable_resource_directory_with_options_async(request, runtime)

    def get_account_with_options(
        self,
        request: main_models.GetAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.include_tags):
            query['IncludeTags'] = request.include_tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_with_options_async(
        self,
        request: main_models.GetAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.include_tags):
            query['IncludeTags'] = request.include_tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account(
        self,
        request: main_models.GetAccountRequest,
    ) -> main_models.GetAccountResponse:
        runtime = RuntimeOptions()
        return self.get_account_with_options(request, runtime)

    async def get_account_async(
        self,
        request: main_models.GetAccountRequest,
    ) -> main_models.GetAccountResponse:
        runtime = RuntimeOptions()
        return await self.get_account_with_options_async(request, runtime)

    def get_account_deletion_check_result_with_options(
        self,
        request: main_models.GetAccountDeletionCheckResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountDeletionCheckResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccountDeletionCheckResult',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountDeletionCheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_deletion_check_result_with_options_async(
        self,
        request: main_models.GetAccountDeletionCheckResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountDeletionCheckResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccountDeletionCheckResult',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountDeletionCheckResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_deletion_check_result(
        self,
        request: main_models.GetAccountDeletionCheckResultRequest,
    ) -> main_models.GetAccountDeletionCheckResultResponse:
        runtime = RuntimeOptions()
        return self.get_account_deletion_check_result_with_options(request, runtime)

    async def get_account_deletion_check_result_async(
        self,
        request: main_models.GetAccountDeletionCheckResultRequest,
    ) -> main_models.GetAccountDeletionCheckResultResponse:
        runtime = RuntimeOptions()
        return await self.get_account_deletion_check_result_with_options_async(request, runtime)

    def get_account_deletion_status_with_options(
        self,
        request: main_models.GetAccountDeletionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountDeletionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccountDeletionStatus',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountDeletionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_deletion_status_with_options_async(
        self,
        request: main_models.GetAccountDeletionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountDeletionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccountDeletionStatus',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountDeletionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_deletion_status(
        self,
        request: main_models.GetAccountDeletionStatusRequest,
    ) -> main_models.GetAccountDeletionStatusResponse:
        runtime = RuntimeOptions()
        return self.get_account_deletion_status_with_options(request, runtime)

    async def get_account_deletion_status_async(
        self,
        request: main_models.GetAccountDeletionStatusRequest,
    ) -> main_models.GetAccountDeletionStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_account_deletion_status_with_options_async(request, runtime)

    def get_control_policy_with_options(
        self,
        request: main_models.GetControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetControlPolicy',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_control_policy_with_options_async(
        self,
        request: main_models.GetControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetControlPolicy',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_control_policy(
        self,
        request: main_models.GetControlPolicyRequest,
    ) -> main_models.GetControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.get_control_policy_with_options(request, runtime)

    async def get_control_policy_async(
        self,
        request: main_models.GetControlPolicyRequest,
    ) -> main_models.GetControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_control_policy_with_options_async(request, runtime)

    def get_control_policy_enablement_status_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetControlPolicyEnablementStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetControlPolicyEnablementStatus',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetControlPolicyEnablementStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_control_policy_enablement_status_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetControlPolicyEnablementStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetControlPolicyEnablementStatus',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetControlPolicyEnablementStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_control_policy_enablement_status(self) -> main_models.GetControlPolicyEnablementStatusResponse:
        runtime = RuntimeOptions()
        return self.get_control_policy_enablement_status_with_options(runtime)

    async def get_control_policy_enablement_status_async(self) -> main_models.GetControlPolicyEnablementStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_control_policy_enablement_status_with_options_async(runtime)

    def get_folder_with_options(
        self,
        request: main_models.GetFolderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFolderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFolder',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_folder_with_options_async(
        self,
        request: main_models.GetFolderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFolderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFolder',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_folder(
        self,
        request: main_models.GetFolderRequest,
    ) -> main_models.GetFolderResponse:
        runtime = RuntimeOptions()
        return self.get_folder_with_options(request, runtime)

    async def get_folder_async(
        self,
        request: main_models.GetFolderRequest,
    ) -> main_models.GetFolderResponse:
        runtime = RuntimeOptions()
        return await self.get_folder_with_options_async(request, runtime)

    def get_handshake_with_options(
        self,
        request: main_models.GetHandshakeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHandshakeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHandshake',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHandshakeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_handshake_with_options_async(
        self,
        request: main_models.GetHandshakeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHandshakeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHandshake',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHandshakeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_handshake(
        self,
        request: main_models.GetHandshakeRequest,
    ) -> main_models.GetHandshakeResponse:
        runtime = RuntimeOptions()
        return self.get_handshake_with_options(request, runtime)

    async def get_handshake_async(
        self,
        request: main_models.GetHandshakeRequest,
    ) -> main_models.GetHandshakeResponse:
        runtime = RuntimeOptions()
        return await self.get_handshake_with_options_async(request, runtime)

    def get_message_contact_with_options(
        self,
        request: main_models.GetMessageContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMessageContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMessageContact',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMessageContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_message_contact_with_options_async(
        self,
        request: main_models.GetMessageContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMessageContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMessageContact',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMessageContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_message_contact(
        self,
        request: main_models.GetMessageContactRequest,
    ) -> main_models.GetMessageContactResponse:
        runtime = RuntimeOptions()
        return self.get_message_contact_with_options(request, runtime)

    async def get_message_contact_async(
        self,
        request: main_models.GetMessageContactRequest,
    ) -> main_models.GetMessageContactResponse:
        runtime = RuntimeOptions()
        return await self.get_message_contact_with_options_async(request, runtime)

    def get_message_contact_deletion_status_with_options(
        self,
        request: main_models.GetMessageContactDeletionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMessageContactDeletionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMessageContactDeletionStatus',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMessageContactDeletionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_message_contact_deletion_status_with_options_async(
        self,
        request: main_models.GetMessageContactDeletionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMessageContactDeletionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMessageContactDeletionStatus',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMessageContactDeletionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_message_contact_deletion_status(
        self,
        request: main_models.GetMessageContactDeletionStatusRequest,
    ) -> main_models.GetMessageContactDeletionStatusResponse:
        runtime = RuntimeOptions()
        return self.get_message_contact_deletion_status_with_options(request, runtime)

    async def get_message_contact_deletion_status_async(
        self,
        request: main_models.GetMessageContactDeletionStatusRequest,
    ) -> main_models.GetMessageContactDeletionStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_message_contact_deletion_status_with_options_async(request, runtime)

    def get_payer_for_account_with_options(
        self,
        request: main_models.GetPayerForAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPayerForAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPayerForAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPayerForAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_payer_for_account_with_options_async(
        self,
        request: main_models.GetPayerForAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPayerForAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPayerForAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPayerForAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_payer_for_account(
        self,
        request: main_models.GetPayerForAccountRequest,
    ) -> main_models.GetPayerForAccountResponse:
        runtime = RuntimeOptions()
        return self.get_payer_for_account_with_options(request, runtime)

    async def get_payer_for_account_async(
        self,
        request: main_models.GetPayerForAccountRequest,
    ) -> main_models.GetPayerForAccountResponse:
        runtime = RuntimeOptions()
        return await self.get_payer_for_account_with_options_async(request, runtime)

    def get_resource_directory_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceDirectoryResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetResourceDirectory',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_directory_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceDirectoryResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetResourceDirectory',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_directory(self) -> main_models.GetResourceDirectoryResponse:
        runtime = RuntimeOptions()
        return self.get_resource_directory_with_options(runtime)

    async def get_resource_directory_async(self) -> main_models.GetResourceDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_directory_with_options_async(runtime)

    def invite_account_to_resource_directory_with_options(
        self,
        request: main_models.InviteAccountToResourceDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InviteAccountToResourceDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        if not DaraCore.is_null(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.target_entity):
            query['TargetEntity'] = request.target_entity
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InviteAccountToResourceDirectory',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InviteAccountToResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def invite_account_to_resource_directory_with_options_async(
        self,
        request: main_models.InviteAccountToResourceDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InviteAccountToResourceDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        if not DaraCore.is_null(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.target_entity):
            query['TargetEntity'] = request.target_entity
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InviteAccountToResourceDirectory',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InviteAccountToResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invite_account_to_resource_directory(
        self,
        request: main_models.InviteAccountToResourceDirectoryRequest,
    ) -> main_models.InviteAccountToResourceDirectoryResponse:
        runtime = RuntimeOptions()
        return self.invite_account_to_resource_directory_with_options(request, runtime)

    async def invite_account_to_resource_directory_async(
        self,
        request: main_models.InviteAccountToResourceDirectoryRequest,
    ) -> main_models.InviteAccountToResourceDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.invite_account_to_resource_directory_with_options_async(request, runtime)

    def list_accounts_with_options(
        self,
        request: main_models.ListAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccounts',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_accounts_with_options_async(
        self,
        request: main_models.ListAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccounts',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_accounts(
        self,
        request: main_models.ListAccountsRequest,
    ) -> main_models.ListAccountsResponse:
        runtime = RuntimeOptions()
        return self.list_accounts_with_options(request, runtime)

    async def list_accounts_async(
        self,
        request: main_models.ListAccountsRequest,
    ) -> main_models.ListAccountsResponse:
        runtime = RuntimeOptions()
        return await self.list_accounts_with_options_async(request, runtime)

    def list_accounts_for_parent_with_options(
        self,
        request: main_models.ListAccountsForParentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccountsForParentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not DaraCore.is_null(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccountsForParent',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccountsForParentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_accounts_for_parent_with_options_async(
        self,
        request: main_models.ListAccountsForParentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccountsForParentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not DaraCore.is_null(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccountsForParent',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccountsForParentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_accounts_for_parent(
        self,
        request: main_models.ListAccountsForParentRequest,
    ) -> main_models.ListAccountsForParentResponse:
        runtime = RuntimeOptions()
        return self.list_accounts_for_parent_with_options(request, runtime)

    async def list_accounts_for_parent_async(
        self,
        request: main_models.ListAccountsForParentRequest,
    ) -> main_models.ListAccountsForParentResponse:
        runtime = RuntimeOptions()
        return await self.list_accounts_for_parent_with_options_async(request, runtime)

    def list_ancestors_with_options(
        self,
        request: main_models.ListAncestorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAncestorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.child_id):
            query['ChildId'] = request.child_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAncestors',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAncestorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ancestors_with_options_async(
        self,
        request: main_models.ListAncestorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAncestorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.child_id):
            query['ChildId'] = request.child_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAncestors',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAncestorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ancestors(
        self,
        request: main_models.ListAncestorsRequest,
    ) -> main_models.ListAncestorsResponse:
        runtime = RuntimeOptions()
        return self.list_ancestors_with_options(request, runtime)

    async def list_ancestors_async(
        self,
        request: main_models.ListAncestorsRequest,
    ) -> main_models.ListAncestorsResponse:
        runtime = RuntimeOptions()
        return await self.list_ancestors_with_options_async(request, runtime)

    def list_authorized_accounts_with_options(
        self,
        request: main_models.ListAuthorizedAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAuthorizedAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAuthorizedAccounts',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuthorizedAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_authorized_accounts_with_options_async(
        self,
        request: main_models.ListAuthorizedAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAuthorizedAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAuthorizedAccounts',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuthorizedAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_authorized_accounts(
        self,
        request: main_models.ListAuthorizedAccountsRequest,
    ) -> main_models.ListAuthorizedAccountsResponse:
        runtime = RuntimeOptions()
        return self.list_authorized_accounts_with_options(request, runtime)

    async def list_authorized_accounts_async(
        self,
        request: main_models.ListAuthorizedAccountsRequest,
    ) -> main_models.ListAuthorizedAccountsResponse:
        runtime = RuntimeOptions()
        return await self.list_authorized_accounts_with_options_async(request, runtime)

    def list_authorized_folders_with_options(
        self,
        request: main_models.ListAuthorizedFoldersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAuthorizedFoldersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAuthorizedFolders',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuthorizedFoldersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_authorized_folders_with_options_async(
        self,
        request: main_models.ListAuthorizedFoldersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAuthorizedFoldersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAuthorizedFolders',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuthorizedFoldersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_authorized_folders(
        self,
        request: main_models.ListAuthorizedFoldersRequest,
    ) -> main_models.ListAuthorizedFoldersResponse:
        runtime = RuntimeOptions()
        return self.list_authorized_folders_with_options(request, runtime)

    async def list_authorized_folders_async(
        self,
        request: main_models.ListAuthorizedFoldersRequest,
    ) -> main_models.ListAuthorizedFoldersResponse:
        runtime = RuntimeOptions()
        return await self.list_authorized_folders_with_options_async(request, runtime)

    def list_control_policies_with_options(
        self,
        request: main_models.ListControlPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListControlPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListControlPolicies',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListControlPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_control_policies_with_options_async(
        self,
        request: main_models.ListControlPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListControlPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListControlPolicies',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListControlPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_control_policies(
        self,
        request: main_models.ListControlPoliciesRequest,
    ) -> main_models.ListControlPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_control_policies_with_options(request, runtime)

    async def list_control_policies_async(
        self,
        request: main_models.ListControlPoliciesRequest,
    ) -> main_models.ListControlPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_control_policies_with_options_async(request, runtime)

    def list_control_policy_attachments_for_target_with_options(
        self,
        request: main_models.ListControlPolicyAttachmentsForTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListControlPolicyAttachmentsForTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListControlPolicyAttachmentsForTarget',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListControlPolicyAttachmentsForTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_control_policy_attachments_for_target_with_options_async(
        self,
        request: main_models.ListControlPolicyAttachmentsForTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListControlPolicyAttachmentsForTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListControlPolicyAttachmentsForTarget',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListControlPolicyAttachmentsForTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_control_policy_attachments_for_target(
        self,
        request: main_models.ListControlPolicyAttachmentsForTargetRequest,
    ) -> main_models.ListControlPolicyAttachmentsForTargetResponse:
        runtime = RuntimeOptions()
        return self.list_control_policy_attachments_for_target_with_options(request, runtime)

    async def list_control_policy_attachments_for_target_async(
        self,
        request: main_models.ListControlPolicyAttachmentsForTargetRequest,
    ) -> main_models.ListControlPolicyAttachmentsForTargetResponse:
        runtime = RuntimeOptions()
        return await self.list_control_policy_attachments_for_target_with_options_async(request, runtime)

    def list_delegated_administrators_with_options(
        self,
        request: main_models.ListDelegatedAdministratorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDelegatedAdministratorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDelegatedAdministrators',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDelegatedAdministratorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_delegated_administrators_with_options_async(
        self,
        request: main_models.ListDelegatedAdministratorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDelegatedAdministratorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDelegatedAdministrators',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDelegatedAdministratorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_delegated_administrators(
        self,
        request: main_models.ListDelegatedAdministratorsRequest,
    ) -> main_models.ListDelegatedAdministratorsResponse:
        runtime = RuntimeOptions()
        return self.list_delegated_administrators_with_options(request, runtime)

    async def list_delegated_administrators_async(
        self,
        request: main_models.ListDelegatedAdministratorsRequest,
    ) -> main_models.ListDelegatedAdministratorsResponse:
        runtime = RuntimeOptions()
        return await self.list_delegated_administrators_with_options_async(request, runtime)

    def list_delegated_services_for_account_with_options(
        self,
        request: main_models.ListDelegatedServicesForAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDelegatedServicesForAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDelegatedServicesForAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDelegatedServicesForAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_delegated_services_for_account_with_options_async(
        self,
        request: main_models.ListDelegatedServicesForAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDelegatedServicesForAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDelegatedServicesForAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDelegatedServicesForAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_delegated_services_for_account(
        self,
        request: main_models.ListDelegatedServicesForAccountRequest,
    ) -> main_models.ListDelegatedServicesForAccountResponse:
        runtime = RuntimeOptions()
        return self.list_delegated_services_for_account_with_options(request, runtime)

    async def list_delegated_services_for_account_async(
        self,
        request: main_models.ListDelegatedServicesForAccountRequest,
    ) -> main_models.ListDelegatedServicesForAccountResponse:
        runtime = RuntimeOptions()
        return await self.list_delegated_services_for_account_with_options_async(request, runtime)

    def list_folders_for_parent_with_options(
        self,
        request: main_models.ListFoldersForParentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFoldersForParentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not DaraCore.is_null(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFoldersForParent',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFoldersForParentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_folders_for_parent_with_options_async(
        self,
        request: main_models.ListFoldersForParentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFoldersForParentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not DaraCore.is_null(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFoldersForParent',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFoldersForParentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_folders_for_parent(
        self,
        request: main_models.ListFoldersForParentRequest,
    ) -> main_models.ListFoldersForParentResponse:
        runtime = RuntimeOptions()
        return self.list_folders_for_parent_with_options(request, runtime)

    async def list_folders_for_parent_async(
        self,
        request: main_models.ListFoldersForParentRequest,
    ) -> main_models.ListFoldersForParentResponse:
        runtime = RuntimeOptions()
        return await self.list_folders_for_parent_with_options_async(request, runtime)

    def list_handshakes_for_account_with_options(
        self,
        request: main_models.ListHandshakesForAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHandshakesForAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHandshakesForAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHandshakesForAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_handshakes_for_account_with_options_async(
        self,
        request: main_models.ListHandshakesForAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHandshakesForAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHandshakesForAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHandshakesForAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_handshakes_for_account(
        self,
        request: main_models.ListHandshakesForAccountRequest,
    ) -> main_models.ListHandshakesForAccountResponse:
        runtime = RuntimeOptions()
        return self.list_handshakes_for_account_with_options(request, runtime)

    async def list_handshakes_for_account_async(
        self,
        request: main_models.ListHandshakesForAccountRequest,
    ) -> main_models.ListHandshakesForAccountResponse:
        runtime = RuntimeOptions()
        return await self.list_handshakes_for_account_with_options_async(request, runtime)

    def list_handshakes_for_resource_directory_with_options(
        self,
        request: main_models.ListHandshakesForResourceDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHandshakesForResourceDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHandshakesForResourceDirectory',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHandshakesForResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_handshakes_for_resource_directory_with_options_async(
        self,
        request: main_models.ListHandshakesForResourceDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHandshakesForResourceDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHandshakesForResourceDirectory',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHandshakesForResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_handshakes_for_resource_directory(
        self,
        request: main_models.ListHandshakesForResourceDirectoryRequest,
    ) -> main_models.ListHandshakesForResourceDirectoryResponse:
        runtime = RuntimeOptions()
        return self.list_handshakes_for_resource_directory_with_options(request, runtime)

    async def list_handshakes_for_resource_directory_async(
        self,
        request: main_models.ListHandshakesForResourceDirectoryRequest,
    ) -> main_models.ListHandshakesForResourceDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.list_handshakes_for_resource_directory_with_options_async(request, runtime)

    def list_message_contact_verifications_with_options(
        self,
        request: main_models.ListMessageContactVerificationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMessageContactVerificationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMessageContactVerifications',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMessageContactVerificationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_message_contact_verifications_with_options_async(
        self,
        request: main_models.ListMessageContactVerificationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMessageContactVerificationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMessageContactVerifications',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMessageContactVerificationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_message_contact_verifications(
        self,
        request: main_models.ListMessageContactVerificationsRequest,
    ) -> main_models.ListMessageContactVerificationsResponse:
        runtime = RuntimeOptions()
        return self.list_message_contact_verifications_with_options(request, runtime)

    async def list_message_contact_verifications_async(
        self,
        request: main_models.ListMessageContactVerificationsRequest,
    ) -> main_models.ListMessageContactVerificationsResponse:
        runtime = RuntimeOptions()
        return await self.list_message_contact_verifications_with_options_async(request, runtime)

    def list_message_contacts_with_options(
        self,
        request: main_models.ListMessageContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMessageContactsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.member):
            query['Member'] = request.member
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMessageContacts',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMessageContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_message_contacts_with_options_async(
        self,
        request: main_models.ListMessageContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMessageContactsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.member):
            query['Member'] = request.member
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMessageContacts',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMessageContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_message_contacts(
        self,
        request: main_models.ListMessageContactsRequest,
    ) -> main_models.ListMessageContactsResponse:
        runtime = RuntimeOptions()
        return self.list_message_contacts_with_options(request, runtime)

    async def list_message_contacts_async(
        self,
        request: main_models.ListMessageContactsRequest,
    ) -> main_models.ListMessageContactsResponse:
        runtime = RuntimeOptions()
        return await self.list_message_contacts_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: main_models.ListTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_filter):
            query['KeyFilter'] = request.key_filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagKeys',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: main_models.ListTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_filter):
            query['KeyFilter'] = request.key_filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagKeys',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: main_models.ListTagKeysRequest,
    ) -> main_models.ListTagKeysResponse:
        runtime = RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: main_models.ListTagKeysRequest,
    ) -> main_models.ListTagKeysResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: main_models.ListTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagValuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        if not DaraCore.is_null(request.value_filter):
            query['ValueFilter'] = request.value_filter
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagValues',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: main_models.ListTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagValuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        if not DaraCore.is_null(request.value_filter):
            query['ValueFilter'] = request.value_filter
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagValues',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: main_models.ListTagValuesRequest,
    ) -> main_models.ListTagValuesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: main_models.ListTagValuesRequest,
    ) -> main_models.ListTagValuesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def list_target_attachments_for_control_policy_with_options(
        self,
        request: main_models.ListTargetAttachmentsForControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTargetAttachmentsForControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTargetAttachmentsForControlPolicy',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTargetAttachmentsForControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_target_attachments_for_control_policy_with_options_async(
        self,
        request: main_models.ListTargetAttachmentsForControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTargetAttachmentsForControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTargetAttachmentsForControlPolicy',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTargetAttachmentsForControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_target_attachments_for_control_policy(
        self,
        request: main_models.ListTargetAttachmentsForControlPolicyRequest,
    ) -> main_models.ListTargetAttachmentsForControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.list_target_attachments_for_control_policy_with_options(request, runtime)

    async def list_target_attachments_for_control_policy_async(
        self,
        request: main_models.ListTargetAttachmentsForControlPolicyRequest,
    ) -> main_models.ListTargetAttachmentsForControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.list_target_attachments_for_control_policy_with_options_async(request, runtime)

    def list_trusted_service_status_with_options(
        self,
        request: main_models.ListTrustedServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTrustedServiceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.admin_account_id):
            query['AdminAccountId'] = request.admin_account_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTrustedServiceStatus',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrustedServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_trusted_service_status_with_options_async(
        self,
        request: main_models.ListTrustedServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTrustedServiceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.admin_account_id):
            query['AdminAccountId'] = request.admin_account_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTrustedServiceStatus',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrustedServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_trusted_service_status(
        self,
        request: main_models.ListTrustedServiceStatusRequest,
    ) -> main_models.ListTrustedServiceStatusResponse:
        runtime = RuntimeOptions()
        return self.list_trusted_service_status_with_options(request, runtime)

    async def list_trusted_service_status_async(
        self,
        request: main_models.ListTrustedServiceStatusRequest,
    ) -> main_models.ListTrustedServiceStatusResponse:
        runtime = RuntimeOptions()
        return await self.list_trusted_service_status_with_options_async(request, runtime)

    def move_account_with_options(
        self,
        request: main_models.MoveAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.destination_folder_id):
            query['DestinationFolderId'] = request.destination_folder_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_account_with_options_async(
        self,
        request: main_models.MoveAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.destination_folder_id):
            query['DestinationFolderId'] = request.destination_folder_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_account(
        self,
        request: main_models.MoveAccountRequest,
    ) -> main_models.MoveAccountResponse:
        runtime = RuntimeOptions()
        return self.move_account_with_options(request, runtime)

    async def move_account_async(
        self,
        request: main_models.MoveAccountRequest,
    ) -> main_models.MoveAccountResponse:
        runtime = RuntimeOptions()
        return await self.move_account_with_options_async(request, runtime)

    def precheck_for_consolidated_billing_account_with_options(
        self,
        request: main_models.PrecheckForConsolidatedBillingAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PrecheckForConsolidatedBillingAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.billing_account_id):
            query['BillingAccountId'] = request.billing_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PrecheckForConsolidatedBillingAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PrecheckForConsolidatedBillingAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def precheck_for_consolidated_billing_account_with_options_async(
        self,
        request: main_models.PrecheckForConsolidatedBillingAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PrecheckForConsolidatedBillingAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.billing_account_id):
            query['BillingAccountId'] = request.billing_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PrecheckForConsolidatedBillingAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PrecheckForConsolidatedBillingAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def precheck_for_consolidated_billing_account(
        self,
        request: main_models.PrecheckForConsolidatedBillingAccountRequest,
    ) -> main_models.PrecheckForConsolidatedBillingAccountResponse:
        runtime = RuntimeOptions()
        return self.precheck_for_consolidated_billing_account_with_options(request, runtime)

    async def precheck_for_consolidated_billing_account_async(
        self,
        request: main_models.PrecheckForConsolidatedBillingAccountRequest,
    ) -> main_models.PrecheckForConsolidatedBillingAccountResponse:
        runtime = RuntimeOptions()
        return await self.precheck_for_consolidated_billing_account_with_options_async(request, runtime)

    def register_delegated_administrator_with_options(
        self,
        request: main_models.RegisterDelegatedAdministratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterDelegatedAdministratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterDelegatedAdministrator',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterDelegatedAdministratorResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_delegated_administrator_with_options_async(
        self,
        request: main_models.RegisterDelegatedAdministratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterDelegatedAdministratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterDelegatedAdministrator',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterDelegatedAdministratorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_delegated_administrator(
        self,
        request: main_models.RegisterDelegatedAdministratorRequest,
    ) -> main_models.RegisterDelegatedAdministratorResponse:
        runtime = RuntimeOptions()
        return self.register_delegated_administrator_with_options(request, runtime)

    async def register_delegated_administrator_async(
        self,
        request: main_models.RegisterDelegatedAdministratorRequest,
    ) -> main_models.RegisterDelegatedAdministratorResponse:
        runtime = RuntimeOptions()
        return await self.register_delegated_administrator_with_options_async(request, runtime)

    def remove_cloud_account_with_options(
        self,
        request: main_models.RemoveCloudAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveCloudAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveCloudAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveCloudAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_cloud_account_with_options_async(
        self,
        request: main_models.RemoveCloudAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveCloudAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveCloudAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveCloudAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_cloud_account(
        self,
        request: main_models.RemoveCloudAccountRequest,
    ) -> main_models.RemoveCloudAccountResponse:
        runtime = RuntimeOptions()
        return self.remove_cloud_account_with_options(request, runtime)

    async def remove_cloud_account_async(
        self,
        request: main_models.RemoveCloudAccountRequest,
    ) -> main_models.RemoveCloudAccountResponse:
        runtime = RuntimeOptions()
        return await self.remove_cloud_account_with_options_async(request, runtime)

    def retry_change_account_email_with_options(
        self,
        request: main_models.RetryChangeAccountEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetryChangeAccountEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RetryChangeAccountEmail',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryChangeAccountEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_change_account_email_with_options_async(
        self,
        request: main_models.RetryChangeAccountEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetryChangeAccountEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RetryChangeAccountEmail',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryChangeAccountEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_change_account_email(
        self,
        request: main_models.RetryChangeAccountEmailRequest,
    ) -> main_models.RetryChangeAccountEmailResponse:
        runtime = RuntimeOptions()
        return self.retry_change_account_email_with_options(request, runtime)

    async def retry_change_account_email_async(
        self,
        request: main_models.RetryChangeAccountEmailRequest,
    ) -> main_models.RetryChangeAccountEmailResponse:
        runtime = RuntimeOptions()
        return await self.retry_change_account_email_with_options_async(request, runtime)

    def send_email_verification_for_message_contact_with_options(
        self,
        request: main_models.SendEmailVerificationForMessageContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendEmailVerificationForMessageContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.email_address):
            query['EmailAddress'] = request.email_address
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendEmailVerificationForMessageContact',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendEmailVerificationForMessageContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_email_verification_for_message_contact_with_options_async(
        self,
        request: main_models.SendEmailVerificationForMessageContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendEmailVerificationForMessageContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.email_address):
            query['EmailAddress'] = request.email_address
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendEmailVerificationForMessageContact',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendEmailVerificationForMessageContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_email_verification_for_message_contact(
        self,
        request: main_models.SendEmailVerificationForMessageContactRequest,
    ) -> main_models.SendEmailVerificationForMessageContactResponse:
        runtime = RuntimeOptions()
        return self.send_email_verification_for_message_contact_with_options(request, runtime)

    async def send_email_verification_for_message_contact_async(
        self,
        request: main_models.SendEmailVerificationForMessageContactRequest,
    ) -> main_models.SendEmailVerificationForMessageContactResponse:
        runtime = RuntimeOptions()
        return await self.send_email_verification_for_message_contact_with_options_async(request, runtime)

    def send_phone_verification_for_message_contact_with_options(
        self,
        request: main_models.SendPhoneVerificationForMessageContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendPhoneVerificationForMessageContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendPhoneVerificationForMessageContact',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendPhoneVerificationForMessageContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_phone_verification_for_message_contact_with_options_async(
        self,
        request: main_models.SendPhoneVerificationForMessageContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendPhoneVerificationForMessageContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendPhoneVerificationForMessageContact',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendPhoneVerificationForMessageContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_phone_verification_for_message_contact(
        self,
        request: main_models.SendPhoneVerificationForMessageContactRequest,
    ) -> main_models.SendPhoneVerificationForMessageContactResponse:
        runtime = RuntimeOptions()
        return self.send_phone_verification_for_message_contact_with_options(request, runtime)

    async def send_phone_verification_for_message_contact_async(
        self,
        request: main_models.SendPhoneVerificationForMessageContactRequest,
    ) -> main_models.SendPhoneVerificationForMessageContactResponse:
        runtime = RuntimeOptions()
        return await self.send_phone_verification_for_message_contact_with_options_async(request, runtime)

    def send_verification_code_for_bind_secure_mobile_phone_with_options(
        self,
        request: main_models.SendVerificationCodeForBindSecureMobilePhoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendVerificationCodeForBindSecureMobilePhoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendVerificationCodeForBindSecureMobilePhone',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendVerificationCodeForBindSecureMobilePhoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_verification_code_for_bind_secure_mobile_phone_with_options_async(
        self,
        request: main_models.SendVerificationCodeForBindSecureMobilePhoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendVerificationCodeForBindSecureMobilePhoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendVerificationCodeForBindSecureMobilePhone',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendVerificationCodeForBindSecureMobilePhoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_verification_code_for_bind_secure_mobile_phone(
        self,
        request: main_models.SendVerificationCodeForBindSecureMobilePhoneRequest,
    ) -> main_models.SendVerificationCodeForBindSecureMobilePhoneResponse:
        runtime = RuntimeOptions()
        return self.send_verification_code_for_bind_secure_mobile_phone_with_options(request, runtime)

    async def send_verification_code_for_bind_secure_mobile_phone_async(
        self,
        request: main_models.SendVerificationCodeForBindSecureMobilePhoneRequest,
    ) -> main_models.SendVerificationCodeForBindSecureMobilePhoneResponse:
        runtime = RuntimeOptions()
        return await self.send_verification_code_for_bind_secure_mobile_phone_with_options_async(request, runtime)

    def send_verification_code_for_enable_rdwith_options(
        self,
        request: main_models.SendVerificationCodeForEnableRDRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendVerificationCodeForEnableRDResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendVerificationCodeForEnableRD',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendVerificationCodeForEnableRDResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_verification_code_for_enable_rdwith_options_async(
        self,
        request: main_models.SendVerificationCodeForEnableRDRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendVerificationCodeForEnableRDResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendVerificationCodeForEnableRD',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendVerificationCodeForEnableRDResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_verification_code_for_enable_rd(
        self,
        request: main_models.SendVerificationCodeForEnableRDRequest,
    ) -> main_models.SendVerificationCodeForEnableRDResponse:
        runtime = RuntimeOptions()
        return self.send_verification_code_for_enable_rdwith_options(request, runtime)

    async def send_verification_code_for_enable_rd_async(
        self,
        request: main_models.SendVerificationCodeForEnableRDRequest,
    ) -> main_models.SendVerificationCodeForEnableRDResponse:
        runtime = RuntimeOptions()
        return await self.send_verification_code_for_enable_rdwith_options_async(request, runtime)

    def set_member_deletion_permission_with_options(
        self,
        request: main_models.SetMemberDeletionPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetMemberDeletionPermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetMemberDeletionPermission',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetMemberDeletionPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_member_deletion_permission_with_options_async(
        self,
        request: main_models.SetMemberDeletionPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetMemberDeletionPermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetMemberDeletionPermission',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetMemberDeletionPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_member_deletion_permission(
        self,
        request: main_models.SetMemberDeletionPermissionRequest,
    ) -> main_models.SetMemberDeletionPermissionResponse:
        runtime = RuntimeOptions()
        return self.set_member_deletion_permission_with_options(request, runtime)

    async def set_member_deletion_permission_async(
        self,
        request: main_models.SetMemberDeletionPermissionRequest,
    ) -> main_models.SetMemberDeletionPermissionResponse:
        runtime = RuntimeOptions()
        return await self.set_member_deletion_permission_with_options_async(request, runtime)

    def set_member_display_name_sync_status_with_options(
        self,
        request: main_models.SetMemberDisplayNameSyncStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetMemberDisplayNameSyncStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetMemberDisplayNameSyncStatus',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetMemberDisplayNameSyncStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_member_display_name_sync_status_with_options_async(
        self,
        request: main_models.SetMemberDisplayNameSyncStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetMemberDisplayNameSyncStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetMemberDisplayNameSyncStatus',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetMemberDisplayNameSyncStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_member_display_name_sync_status(
        self,
        request: main_models.SetMemberDisplayNameSyncStatusRequest,
    ) -> main_models.SetMemberDisplayNameSyncStatusResponse:
        runtime = RuntimeOptions()
        return self.set_member_display_name_sync_status_with_options(request, runtime)

    async def set_member_display_name_sync_status_async(
        self,
        request: main_models.SetMemberDisplayNameSyncStatusRequest,
    ) -> main_models.SetMemberDisplayNameSyncStatusResponse:
        runtime = RuntimeOptions()
        return await self.set_member_display_name_sync_status_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_account_with_options(
        self,
        request: main_models.UpdateAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.new_account_type):
            query['NewAccountType'] = request.new_account_type
        if not DaraCore.is_null(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_account_with_options_async(
        self,
        request: main_models.UpdateAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.new_account_type):
            query['NewAccountType'] = request.new_account_type
        if not DaraCore.is_null(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_account(
        self,
        request: main_models.UpdateAccountRequest,
    ) -> main_models.UpdateAccountResponse:
        runtime = RuntimeOptions()
        return self.update_account_with_options(request, runtime)

    async def update_account_async(
        self,
        request: main_models.UpdateAccountRequest,
    ) -> main_models.UpdateAccountResponse:
        runtime = RuntimeOptions()
        return await self.update_account_with_options_async(request, runtime)

    def update_control_policy_with_options(
        self,
        request: main_models.UpdateControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_description):
            query['NewDescription'] = request.new_description
        if not DaraCore.is_null(request.new_policy_document):
            query['NewPolicyDocument'] = request.new_policy_document
        if not DaraCore.is_null(request.new_policy_name):
            query['NewPolicyName'] = request.new_policy_name
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateControlPolicy',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_control_policy_with_options_async(
        self,
        request: main_models.UpdateControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_description):
            query['NewDescription'] = request.new_description
        if not DaraCore.is_null(request.new_policy_document):
            query['NewPolicyDocument'] = request.new_policy_document
        if not DaraCore.is_null(request.new_policy_name):
            query['NewPolicyName'] = request.new_policy_name
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateControlPolicy',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_control_policy(
        self,
        request: main_models.UpdateControlPolicyRequest,
    ) -> main_models.UpdateControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.update_control_policy_with_options(request, runtime)

    async def update_control_policy_async(
        self,
        request: main_models.UpdateControlPolicyRequest,
    ) -> main_models.UpdateControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.update_control_policy_with_options_async(request, runtime)

    def update_folder_with_options(
        self,
        request: main_models.UpdateFolderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFolderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.folder_id):
            query['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.new_folder_name):
            query['NewFolderName'] = request.new_folder_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFolder',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_folder_with_options_async(
        self,
        request: main_models.UpdateFolderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFolderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.folder_id):
            query['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.new_folder_name):
            query['NewFolderName'] = request.new_folder_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFolder',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_folder(
        self,
        request: main_models.UpdateFolderRequest,
    ) -> main_models.UpdateFolderResponse:
        runtime = RuntimeOptions()
        return self.update_folder_with_options(request, runtime)

    async def update_folder_async(
        self,
        request: main_models.UpdateFolderRequest,
    ) -> main_models.UpdateFolderResponse:
        runtime = RuntimeOptions()
        return await self.update_folder_with_options_async(request, runtime)

    def update_message_contact_with_options(
        self,
        request: main_models.UpdateMessageContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMessageContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.email_address):
            query['EmailAddress'] = request.email_address
        if not DaraCore.is_null(request.message_types):
            query['MessageTypes'] = request.message_types
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMessageContact',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMessageContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_message_contact_with_options_async(
        self,
        request: main_models.UpdateMessageContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMessageContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.email_address):
            query['EmailAddress'] = request.email_address
        if not DaraCore.is_null(request.message_types):
            query['MessageTypes'] = request.message_types
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMessageContact',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMessageContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_message_contact(
        self,
        request: main_models.UpdateMessageContactRequest,
    ) -> main_models.UpdateMessageContactResponse:
        runtime = RuntimeOptions()
        return self.update_message_contact_with_options(request, runtime)

    async def update_message_contact_async(
        self,
        request: main_models.UpdateMessageContactRequest,
    ) -> main_models.UpdateMessageContactResponse:
        runtime = RuntimeOptions()
        return await self.update_message_contact_with_options_async(request, runtime)

    def update_payer_for_account_with_options(
        self,
        request: main_models.UpdatePayerForAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePayerForAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.payer_account_id):
            query['PayerAccountId'] = request.payer_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePayerForAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePayerForAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_payer_for_account_with_options_async(
        self,
        request: main_models.UpdatePayerForAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePayerForAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.payer_account_id):
            query['PayerAccountId'] = request.payer_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePayerForAccount',
            version = '2022-04-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePayerForAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_payer_for_account(
        self,
        request: main_models.UpdatePayerForAccountRequest,
    ) -> main_models.UpdatePayerForAccountResponse:
        runtime = RuntimeOptions()
        return self.update_payer_for_account_with_options(request, runtime)

    async def update_payer_for_account_async(
        self,
        request: main_models.UpdatePayerForAccountRequest,
    ) -> main_models.UpdatePayerForAccountResponse:
        runtime = RuntimeOptions()
        return await self.update_payer_for_account_with_options_async(request, runtime)
