# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_resourcemanager20200331 import models as main_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('resourcemanager', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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

    def attach_policy_with_options(
        self,
        request: main_models.AttachPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not DaraCore.is_null(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachPolicy',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_policy_with_options_async(
        self,
        request: main_models.AttachPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not DaraCore.is_null(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachPolicy',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_policy(
        self,
        request: main_models.AttachPolicyRequest,
    ) -> main_models.AttachPolicyResponse:
        runtime = RuntimeOptions()
        return self.attach_policy_with_options(request, runtime)

    async def attach_policy_async(
        self,
        request: main_models.AttachPolicyRequest,
    ) -> main_models.AttachPolicyResponse:
        runtime = RuntimeOptions()
        return await self.attach_policy_with_options_async(request, runtime)

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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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

    def cancel_create_cloud_account_with_options(
        self,
        request: main_models.CancelCreateCloudAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelCreateCloudAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelCreateCloudAccount',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelCreateCloudAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_create_cloud_account_with_options_async(
        self,
        request: main_models.CancelCreateCloudAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelCreateCloudAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelCreateCloudAccount',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelCreateCloudAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_create_cloud_account(
        self,
        request: main_models.CancelCreateCloudAccountRequest,
    ) -> main_models.CancelCreateCloudAccountResponse:
        runtime = RuntimeOptions()
        return self.cancel_create_cloud_account_with_options(request, runtime)

    async def cancel_create_cloud_account_async(
        self,
        request: main_models.CancelCreateCloudAccountRequest,
    ) -> main_models.CancelCreateCloudAccountResponse:
        runtime = RuntimeOptions()
        return await self.cancel_create_cloud_account_with_options_async(request, runtime)

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
            version = '2020-03-31',
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
            version = '2020-03-31',
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

    def cancel_promote_resource_account_with_options(
        self,
        request: main_models.CancelPromoteResourceAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelPromoteResourceAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelPromoteResourceAccount',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelPromoteResourceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_promote_resource_account_with_options_async(
        self,
        request: main_models.CancelPromoteResourceAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelPromoteResourceAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelPromoteResourceAccount',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelPromoteResourceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_promote_resource_account(
        self,
        request: main_models.CancelPromoteResourceAccountRequest,
    ) -> main_models.CancelPromoteResourceAccountResponse:
        runtime = RuntimeOptions()
        return self.cancel_promote_resource_account_with_options(request, runtime)

    async def cancel_promote_resource_account_async(
        self,
        request: main_models.CancelPromoteResourceAccountRequest,
    ) -> main_models.CancelPromoteResourceAccountResponse:
        runtime = RuntimeOptions()
        return await self.cancel_promote_resource_account_with_options_async(request, runtime)

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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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

    def create_auto_grouping_rule_with_options(
        self,
        request: main_models.CreateAutoGroupingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAutoGroupingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            query['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            query['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            query['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        if not DaraCore.is_null(request.exclude_resource_types_scope):
            query['ExcludeResourceTypesScope'] = request.exclude_resource_types_scope
        if not DaraCore.is_null(request.region_ids_scope):
            query['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            query['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            query['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.resource_types_scope):
            query['ResourceTypesScope'] = request.resource_types_scope
        if not DaraCore.is_null(request.rule_contents):
            query['RuleContents'] = request.rule_contents
        if not DaraCore.is_null(request.rule_desc):
            query['RuleDesc'] = request.rule_desc
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAutoGroupingRule',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAutoGroupingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_auto_grouping_rule_with_options_async(
        self,
        request: main_models.CreateAutoGroupingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAutoGroupingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            query['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            query['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            query['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        if not DaraCore.is_null(request.exclude_resource_types_scope):
            query['ExcludeResourceTypesScope'] = request.exclude_resource_types_scope
        if not DaraCore.is_null(request.region_ids_scope):
            query['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            query['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            query['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.resource_types_scope):
            query['ResourceTypesScope'] = request.resource_types_scope
        if not DaraCore.is_null(request.rule_contents):
            query['RuleContents'] = request.rule_contents
        if not DaraCore.is_null(request.rule_desc):
            query['RuleDesc'] = request.rule_desc
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAutoGroupingRule',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAutoGroupingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_auto_grouping_rule(
        self,
        request: main_models.CreateAutoGroupingRuleRequest,
    ) -> main_models.CreateAutoGroupingRuleResponse:
        runtime = RuntimeOptions()
        return self.create_auto_grouping_rule_with_options(request, runtime)

    async def create_auto_grouping_rule_async(
        self,
        request: main_models.CreateAutoGroupingRuleRequest,
    ) -> main_models.CreateAutoGroupingRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_auto_grouping_rule_with_options_async(request, runtime)

    def create_cloud_account_with_options(
        self,
        request: main_models.CreateCloudAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not DaraCore.is_null(request.payer_account_id):
            query['PayerAccountId'] = request.payer_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudAccount',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_account_with_options_async(
        self,
        request: main_models.CreateCloudAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not DaraCore.is_null(request.payer_account_id):
            query['PayerAccountId'] = request.payer_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudAccount',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_account(
        self,
        request: main_models.CreateCloudAccountRequest,
    ) -> main_models.CreateCloudAccountResponse:
        runtime = RuntimeOptions()
        return self.create_cloud_account_with_options(request, runtime)

    async def create_cloud_account_async(
        self,
        request: main_models.CreateCloudAccountRequest,
    ) -> main_models.CreateCloudAccountResponse:
        runtime = RuntimeOptions()
        return await self.create_cloud_account_with_options_async(request, runtime)

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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateControlPolicy',
            version = '2020-03-31',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateControlPolicy',
            version = '2020-03-31',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFolder',
            version = '2020-03-31',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFolder',
            version = '2020-03-31',
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

    def create_policy_with_options(
        self,
        request: main_models.CreatePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicy',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_with_options_async(
        self,
        request: main_models.CreatePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicy',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy(
        self,
        request: main_models.CreatePolicyRequest,
    ) -> main_models.CreatePolicyResponse:
        runtime = RuntimeOptions()
        return self.create_policy_with_options(request, runtime)

    async def create_policy_async(
        self,
        request: main_models.CreatePolicyRequest,
    ) -> main_models.CreatePolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_policy_with_options_async(request, runtime)

    def create_policy_version_with_options(
        self,
        request: main_models.CreatePolicyVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.set_as_default):
            query['SetAsDefault'] = request.set_as_default
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicyVersion',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_version_with_options_async(
        self,
        request: main_models.CreatePolicyVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.set_as_default):
            query['SetAsDefault'] = request.set_as_default
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicyVersion',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy_version(
        self,
        request: main_models.CreatePolicyVersionRequest,
    ) -> main_models.CreatePolicyVersionResponse:
        runtime = RuntimeOptions()
        return self.create_policy_version_with_options(request, runtime)

    async def create_policy_version_async(
        self,
        request: main_models.CreatePolicyVersionRequest,
    ) -> main_models.CreatePolicyVersionResponse:
        runtime = RuntimeOptions()
        return await self.create_policy_version_with_options_async(request, runtime)

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
            version = '2020-03-31',
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
            version = '2020-03-31',
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

    def create_resource_group_with_options(
        self,
        request: main_models.CreateResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceGroup',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_group_with_options_async(
        self,
        request: main_models.CreateResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceGroup',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_group(
        self,
        request: main_models.CreateResourceGroupRequest,
    ) -> main_models.CreateResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.create_resource_group_with_options(request, runtime)

    async def create_resource_group_async(
        self,
        request: main_models.CreateResourceGroupRequest,
    ) -> main_models.CreateResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_resource_group_with_options_async(request, runtime)

    def create_role_with_options(
        self,
        request: main_models.CreateRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assume_role_policy_document):
            query['AssumeRolePolicyDocument'] = request.assume_role_policy_document
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.max_session_duration):
            query['MaxSessionDuration'] = request.max_session_duration
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRole',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_role_with_options_async(
        self,
        request: main_models.CreateRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assume_role_policy_document):
            query['AssumeRolePolicyDocument'] = request.assume_role_policy_document
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.max_session_duration):
            query['MaxSessionDuration'] = request.max_session_duration
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRole',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_role(
        self,
        request: main_models.CreateRoleRequest,
    ) -> main_models.CreateRoleResponse:
        runtime = RuntimeOptions()
        return self.create_role_with_options(request, runtime)

    async def create_role_async(
        self,
        request: main_models.CreateRoleRequest,
    ) -> main_models.CreateRoleResponse:
        runtime = RuntimeOptions()
        return await self.create_role_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        request: main_models.CreateServiceLinkedRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceLinkedRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_suffix):
            query['CustomSuffix'] = request.custom_suffix
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceLinkedRole',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: main_models.CreateServiceLinkedRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceLinkedRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_suffix):
            query['CustomSuffix'] = request.custom_suffix
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceLinkedRole',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role(
        self,
        request: main_models.CreateServiceLinkedRoleRequest,
    ) -> main_models.CreateServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    async def create_service_linked_role_async(
        self,
        request: main_models.CreateServiceLinkedRoleRequest,
    ) -> main_models.CreateServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        return await self.create_service_linked_role_with_options_async(request, runtime)

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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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

    def delete_auto_grouping_rule_with_options(
        self,
        request: main_models.DeleteAutoGroupingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAutoGroupingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAutoGroupingRule',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAutoGroupingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_auto_grouping_rule_with_options_async(
        self,
        request: main_models.DeleteAutoGroupingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAutoGroupingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAutoGroupingRule',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAutoGroupingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_auto_grouping_rule(
        self,
        request: main_models.DeleteAutoGroupingRuleRequest,
    ) -> main_models.DeleteAutoGroupingRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_auto_grouping_rule_with_options(request, runtime)

    async def delete_auto_grouping_rule_async(
        self,
        request: main_models.DeleteAutoGroupingRuleRequest,
    ) -> main_models.DeleteAutoGroupingRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_auto_grouping_rule_with_options_async(request, runtime)

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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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

    def delete_policy_with_options(
        self,
        request: main_models.DeletePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicy',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_with_options_async(
        self,
        request: main_models.DeletePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicy',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy(
        self,
        request: main_models.DeletePolicyRequest,
    ) -> main_models.DeletePolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_policy_with_options(request, runtime)

    async def delete_policy_async(
        self,
        request: main_models.DeletePolicyRequest,
    ) -> main_models.DeletePolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_policy_with_options_async(request, runtime)

    def delete_policy_version_with_options(
        self,
        request: main_models.DeletePolicyVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicyVersion',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_version_with_options_async(
        self,
        request: main_models.DeletePolicyVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicyVersion',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy_version(
        self,
        request: main_models.DeletePolicyVersionRequest,
    ) -> main_models.DeletePolicyVersionResponse:
        runtime = RuntimeOptions()
        return self.delete_policy_version_with_options(request, runtime)

    async def delete_policy_version_async(
        self,
        request: main_models.DeletePolicyVersionRequest,
    ) -> main_models.DeletePolicyVersionResponse:
        runtime = RuntimeOptions()
        return await self.delete_policy_version_with_options_async(request, runtime)

    def delete_resource_group_with_options(
        self,
        request: main_models.DeleteResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceGroup',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_group_with_options_async(
        self,
        request: main_models.DeleteResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceGroup',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_group(
        self,
        request: main_models.DeleteResourceGroupRequest,
    ) -> main_models.DeleteResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_resource_group_with_options(request, runtime)

    async def delete_resource_group_async(
        self,
        request: main_models.DeleteResourceGroupRequest,
    ) -> main_models.DeleteResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_resource_group_with_options_async(request, runtime)

    def delete_role_with_options(
        self,
        request: main_models.DeleteRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRole',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_role_with_options_async(
        self,
        request: main_models.DeleteRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRole',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_role(
        self,
        request: main_models.DeleteRoleRequest,
    ) -> main_models.DeleteRoleResponse:
        runtime = RuntimeOptions()
        return self.delete_role_with_options(request, runtime)

    async def delete_role_async(
        self,
        request: main_models.DeleteRoleRequest,
    ) -> main_models.DeleteRoleResponse:
        runtime = RuntimeOptions()
        return await self.delete_role_with_options_async(request, runtime)

    def delete_service_linked_role_with_options(
        self,
        request: main_models.DeleteServiceLinkedRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceLinkedRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceLinkedRole',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_linked_role_with_options_async(
        self,
        request: main_models.DeleteServiceLinkedRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceLinkedRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceLinkedRole',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_linked_role(
        self,
        request: main_models.DeleteServiceLinkedRoleRequest,
    ) -> main_models.DeleteServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        return self.delete_service_linked_role_with_options(request, runtime)

    async def delete_service_linked_role_async(
        self,
        request: main_models.DeleteServiceLinkedRoleRequest,
    ) -> main_models.DeleteServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        return await self.delete_service_linked_role_with_options_async(request, runtime)

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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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

    def detach_policy_with_options(
        self,
        request: main_models.DetachPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not DaraCore.is_null(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachPolicy',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_policy_with_options_async(
        self,
        request: main_models.DetachPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not DaraCore.is_null(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachPolicy',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_policy(
        self,
        request: main_models.DetachPolicyRequest,
    ) -> main_models.DetachPolicyResponse:
        runtime = RuntimeOptions()
        return self.detach_policy_with_options(request, runtime)

    async def detach_policy_async(
        self,
        request: main_models.DetachPolicyRequest,
    ) -> main_models.DetachPolicyResponse:
        runtime = RuntimeOptions()
        return await self.detach_policy_with_options_async(request, runtime)

    def disable_associated_transfer_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAssociatedTransferResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DisableAssociatedTransfer',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableAssociatedTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_associated_transfer_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAssociatedTransferResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DisableAssociatedTransfer',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableAssociatedTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_associated_transfer(self) -> main_models.DisableAssociatedTransferResponse:
        runtime = RuntimeOptions()
        return self.disable_associated_transfer_with_options(runtime)

    async def disable_associated_transfer_async(self) -> main_models.DisableAssociatedTransferResponse:
        runtime = RuntimeOptions()
        return await self.disable_associated_transfer_with_options_async(runtime)

    def disable_auto_grouping_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAutoGroupingResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DisableAutoGrouping',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableAutoGroupingResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_auto_grouping_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAutoGroupingResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DisableAutoGrouping',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableAutoGroupingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_auto_grouping(self) -> main_models.DisableAutoGroupingResponse:
        runtime = RuntimeOptions()
        return self.disable_auto_grouping_with_options(runtime)

    async def disable_auto_grouping_async(self) -> main_models.DisableAutoGroupingResponse:
        runtime = RuntimeOptions()
        return await self.disable_auto_grouping_with_options_async(runtime)

    def disable_control_policy_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DisableControlPolicyResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DisableControlPolicy',
            version = '2020-03-31',
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
            version = '2020-03-31',
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

    def disable_resource_group_notification_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DisableResourceGroupNotificationResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DisableResourceGroupNotification',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableResourceGroupNotificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_resource_group_notification_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DisableResourceGroupNotificationResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DisableResourceGroupNotification',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableResourceGroupNotificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_resource_group_notification(self) -> main_models.DisableResourceGroupNotificationResponse:
        runtime = RuntimeOptions()
        return self.disable_resource_group_notification_with_options(runtime)

    async def disable_resource_group_notification_async(self) -> main_models.DisableResourceGroupNotificationResponse:
        runtime = RuntimeOptions()
        return await self.disable_resource_group_notification_with_options_async(runtime)

    def enable_associated_transfer_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.EnableAssociatedTransferResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'EnableAssociatedTransfer',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableAssociatedTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_associated_transfer_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.EnableAssociatedTransferResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'EnableAssociatedTransfer',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableAssociatedTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_associated_transfer(self) -> main_models.EnableAssociatedTransferResponse:
        runtime = RuntimeOptions()
        return self.enable_associated_transfer_with_options(runtime)

    async def enable_associated_transfer_async(self) -> main_models.EnableAssociatedTransferResponse:
        runtime = RuntimeOptions()
        return await self.enable_associated_transfer_with_options_async(runtime)

    def enable_auto_grouping_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.EnableAutoGroupingResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'EnableAutoGrouping',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableAutoGroupingResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_auto_grouping_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.EnableAutoGroupingResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'EnableAutoGrouping',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableAutoGroupingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_auto_grouping(self) -> main_models.EnableAutoGroupingResponse:
        runtime = RuntimeOptions()
        return self.enable_auto_grouping_with_options(runtime)

    async def enable_auto_grouping_async(self) -> main_models.EnableAutoGroupingResponse:
        runtime = RuntimeOptions()
        return await self.enable_auto_grouping_with_options_async(runtime)

    def enable_control_policy_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.EnableControlPolicyResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'EnableControlPolicy',
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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

    def enable_resource_group_notification_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.EnableResourceGroupNotificationResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'EnableResourceGroupNotification',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableResourceGroupNotificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_resource_group_notification_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.EnableResourceGroupNotificationResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'EnableResourceGroupNotification',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableResourceGroupNotificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_resource_group_notification(self) -> main_models.EnableResourceGroupNotificationResponse:
        runtime = RuntimeOptions()
        return self.enable_resource_group_notification_with_options(runtime)

    async def enable_resource_group_notification_async(self) -> main_models.EnableResourceGroupNotificationResponse:
        runtime = RuntimeOptions()
        return await self.enable_resource_group_notification_with_options_async(runtime)

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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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

    def get_auto_grouping_rule_with_options(
        self,
        request: main_models.GetAutoGroupingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoGroupingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutoGroupingRule',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoGroupingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_grouping_rule_with_options_async(
        self,
        request: main_models.GetAutoGroupingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoGroupingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutoGroupingRule',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoGroupingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_grouping_rule(
        self,
        request: main_models.GetAutoGroupingRuleRequest,
    ) -> main_models.GetAutoGroupingRuleResponse:
        runtime = RuntimeOptions()
        return self.get_auto_grouping_rule_with_options(request, runtime)

    async def get_auto_grouping_rule_async(
        self,
        request: main_models.GetAutoGroupingRuleRequest,
    ) -> main_models.GetAutoGroupingRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_auto_grouping_rule_with_options_async(request, runtime)

    def get_auto_grouping_status_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoGroupingStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetAutoGroupingStatus',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoGroupingStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_grouping_status_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoGroupingStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetAutoGroupingStatus',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoGroupingStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_grouping_status(self) -> main_models.GetAutoGroupingStatusResponse:
        runtime = RuntimeOptions()
        return self.get_auto_grouping_status_with_options(runtime)

    async def get_auto_grouping_status_async(self) -> main_models.GetAutoGroupingStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_auto_grouping_status_with_options_async(runtime)

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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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

    def get_policy_with_options(
        self,
        request: main_models.GetPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPolicy',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_with_options_async(
        self,
        request: main_models.GetPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPolicy',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy(
        self,
        request: main_models.GetPolicyRequest,
    ) -> main_models.GetPolicyResponse:
        runtime = RuntimeOptions()
        return self.get_policy_with_options(request, runtime)

    async def get_policy_async(
        self,
        request: main_models.GetPolicyRequest,
    ) -> main_models.GetPolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_policy_with_options_async(request, runtime)

    def get_policy_version_with_options(
        self,
        request: main_models.GetPolicyVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPolicyVersion',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_version_with_options_async(
        self,
        request: main_models.GetPolicyVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPolicyVersion',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy_version(
        self,
        request: main_models.GetPolicyVersionRequest,
    ) -> main_models.GetPolicyVersionResponse:
        runtime = RuntimeOptions()
        return self.get_policy_version_with_options(request, runtime)

    async def get_policy_version_async(
        self,
        request: main_models.GetPolicyVersionRequest,
    ) -> main_models.GetPolicyVersionResponse:
        runtime = RuntimeOptions()
        return await self.get_policy_version_with_options_async(request, runtime)

    def get_resource_directory_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceDirectoryResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetResourceDirectory',
            version = '2020-03-31',
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
            version = '2020-03-31',
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

    def get_resource_group_with_options(
        self,
        request: main_models.GetResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroup',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_with_options_async(
        self,
        request: main_models.GetResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroup',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group(
        self,
        request: main_models.GetResourceGroupRequest,
    ) -> main_models.GetResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.get_resource_group_with_options(request, runtime)

    async def get_resource_group_async(
        self,
        request: main_models.GetResourceGroupRequest,
    ) -> main_models.GetResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_group_with_options_async(request, runtime)

    def get_resource_group_admin_setting_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupAdminSettingResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetResourceGroupAdminSetting',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupAdminSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_admin_setting_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupAdminSettingResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetResourceGroupAdminSetting',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupAdminSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group_admin_setting(self) -> main_models.GetResourceGroupAdminSettingResponse:
        runtime = RuntimeOptions()
        return self.get_resource_group_admin_setting_with_options(runtime)

    async def get_resource_group_admin_setting_async(self) -> main_models.GetResourceGroupAdminSettingResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_group_admin_setting_with_options_async(runtime)

    def get_resource_group_notification_setting_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupNotificationSettingResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetResourceGroupNotificationSetting',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupNotificationSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_notification_setting_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupNotificationSettingResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetResourceGroupNotificationSetting',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupNotificationSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group_notification_setting(self) -> main_models.GetResourceGroupNotificationSettingResponse:
        runtime = RuntimeOptions()
        return self.get_resource_group_notification_setting_with_options(runtime)

    async def get_resource_group_notification_setting_async(self) -> main_models.GetResourceGroupNotificationSettingResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_group_notification_setting_with_options_async(runtime)

    def get_resource_group_resource_counts_with_options(
        self,
        request: main_models.GetResourceGroupResourceCountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupResourceCountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_by_key):
            query['GroupByKey'] = request.group_by_key
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroupResourceCounts',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupResourceCountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_resource_counts_with_options_async(
        self,
        request: main_models.GetResourceGroupResourceCountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupResourceCountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_by_key):
            query['GroupByKey'] = request.group_by_key
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroupResourceCounts',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupResourceCountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group_resource_counts(
        self,
        request: main_models.GetResourceGroupResourceCountsRequest,
    ) -> main_models.GetResourceGroupResourceCountsResponse:
        runtime = RuntimeOptions()
        return self.get_resource_group_resource_counts_with_options(request, runtime)

    async def get_resource_group_resource_counts_async(
        self,
        request: main_models.GetResourceGroupResourceCountsRequest,
    ) -> main_models.GetResourceGroupResourceCountsResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_group_resource_counts_with_options_async(request, runtime)

    def get_role_with_options(
        self,
        request: main_models.GetRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRole',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_role_with_options_async(
        self,
        request: main_models.GetRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRole',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_role(
        self,
        request: main_models.GetRoleRequest,
    ) -> main_models.GetRoleResponse:
        runtime = RuntimeOptions()
        return self.get_role_with_options(request, runtime)

    async def get_role_async(
        self,
        request: main_models.GetRoleRequest,
    ) -> main_models.GetRoleResponse:
        runtime = RuntimeOptions()
        return await self.get_role_with_options_async(request, runtime)

    def get_service_linked_role_deletion_status_with_options(
        self,
        request: main_models.GetServiceLinkedRoleDeletionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceLinkedRoleDeletionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deletion_task_id):
            query['DeletionTaskId'] = request.deletion_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceLinkedRoleDeletionStatus',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceLinkedRoleDeletionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_linked_role_deletion_status_with_options_async(
        self,
        request: main_models.GetServiceLinkedRoleDeletionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceLinkedRoleDeletionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deletion_task_id):
            query['DeletionTaskId'] = request.deletion_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceLinkedRoleDeletionStatus',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceLinkedRoleDeletionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_linked_role_deletion_status(
        self,
        request: main_models.GetServiceLinkedRoleDeletionStatusRequest,
    ) -> main_models.GetServiceLinkedRoleDeletionStatusResponse:
        runtime = RuntimeOptions()
        return self.get_service_linked_role_deletion_status_with_options(request, runtime)

    async def get_service_linked_role_deletion_status_async(
        self,
        request: main_models.GetServiceLinkedRoleDeletionStatusRequest,
    ) -> main_models.GetServiceLinkedRoleDeletionStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_service_linked_role_deletion_status_with_options_async(request, runtime)

    def init_resource_directory_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.InitResourceDirectoryResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'InitResourceDirectory',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_resource_directory_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.InitResourceDirectoryResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'InitResourceDirectory',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_resource_directory(self) -> main_models.InitResourceDirectoryResponse:
        runtime = RuntimeOptions()
        return self.init_resource_directory_with_options(runtime)

    async def init_resource_directory_async(self) -> main_models.InitResourceDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.init_resource_directory_with_options_async(runtime)

    def invite_account_to_resource_directory_with_options(
        self,
        request: main_models.InviteAccountToResourceDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InviteAccountToResourceDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccounts',
            version = '2020-03-31',
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
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccounts',
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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

    def list_associated_transfer_setting_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListAssociatedTransferSettingResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListAssociatedTransferSetting',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAssociatedTransferSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_associated_transfer_setting_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListAssociatedTransferSettingResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListAssociatedTransferSetting',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAssociatedTransferSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_associated_transfer_setting(self) -> main_models.ListAssociatedTransferSettingResponse:
        runtime = RuntimeOptions()
        return self.list_associated_transfer_setting_with_options(runtime)

    async def list_associated_transfer_setting_async(self) -> main_models.ListAssociatedTransferSettingResponse:
        runtime = RuntimeOptions()
        return await self.list_associated_transfer_setting_with_options_async(runtime)

    def list_auto_grouping_remediations_with_options(
        self,
        request: main_models.ListAutoGroupingRemediationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAutoGroupingRemediationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.earliest_remediation_time):
            query['EarliestRemediationTime'] = request.earliest_remediation_time
        if not DaraCore.is_null(request.latest_remediation_time):
            query['LatestRemediationTime'] = request.latest_remediation_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        if not DaraCore.is_null(request.target_resource_group_id):
            query['TargetResourceGroupId'] = request.target_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAutoGroupingRemediations',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAutoGroupingRemediationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_auto_grouping_remediations_with_options_async(
        self,
        request: main_models.ListAutoGroupingRemediationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAutoGroupingRemediationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.earliest_remediation_time):
            query['EarliestRemediationTime'] = request.earliest_remediation_time
        if not DaraCore.is_null(request.latest_remediation_time):
            query['LatestRemediationTime'] = request.latest_remediation_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        if not DaraCore.is_null(request.target_resource_group_id):
            query['TargetResourceGroupId'] = request.target_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAutoGroupingRemediations',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAutoGroupingRemediationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_auto_grouping_remediations(
        self,
        request: main_models.ListAutoGroupingRemediationsRequest,
    ) -> main_models.ListAutoGroupingRemediationsResponse:
        runtime = RuntimeOptions()
        return self.list_auto_grouping_remediations_with_options(request, runtime)

    async def list_auto_grouping_remediations_async(
        self,
        request: main_models.ListAutoGroupingRemediationsRequest,
    ) -> main_models.ListAutoGroupingRemediationsResponse:
        runtime = RuntimeOptions()
        return await self.list_auto_grouping_remediations_with_options_async(request, runtime)

    def list_auto_grouping_rules_with_options(
        self,
        request: main_models.ListAutoGroupingRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAutoGroupingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAutoGroupingRules',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAutoGroupingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_auto_grouping_rules_with_options_async(
        self,
        request: main_models.ListAutoGroupingRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAutoGroupingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAutoGroupingRules',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAutoGroupingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_auto_grouping_rules(
        self,
        request: main_models.ListAutoGroupingRulesRequest,
    ) -> main_models.ListAutoGroupingRulesResponse:
        runtime = RuntimeOptions()
        return self.list_auto_grouping_rules_with_options(request, runtime)

    async def list_auto_grouping_rules_async(
        self,
        request: main_models.ListAutoGroupingRulesRequest,
    ) -> main_models.ListAutoGroupingRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_auto_grouping_rules_with_options_async(request, runtime)

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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListControlPolicies',
            version = '2020-03-31',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListControlPolicies',
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDelegatedServicesForAccount',
            version = '2020-03-31',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDelegatedServicesForAccount',
            version = '2020-03-31',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFoldersForParent',
            version = '2020-03-31',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFoldersForParent',
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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

    def list_policies_with_options(
        self,
        request: main_models.ListPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesResponse:
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicies',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_with_options_async(
        self,
        request: main_models.ListPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesResponse:
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicies',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies(
        self,
        request: main_models.ListPoliciesRequest,
    ) -> main_models.ListPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_policies_with_options(request, runtime)

    async def list_policies_async(
        self,
        request: main_models.ListPoliciesRequest,
    ) -> main_models.ListPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_policies_with_options_async(request, runtime)

    def list_policy_attachments_with_options(
        self,
        request: main_models.ListPolicyAttachmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicyAttachmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not DaraCore.is_null(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicyAttachments',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPolicyAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policy_attachments_with_options_async(
        self,
        request: main_models.ListPolicyAttachmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicyAttachmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not DaraCore.is_null(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicyAttachments',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPolicyAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policy_attachments(
        self,
        request: main_models.ListPolicyAttachmentsRequest,
    ) -> main_models.ListPolicyAttachmentsResponse:
        runtime = RuntimeOptions()
        return self.list_policy_attachments_with_options(request, runtime)

    async def list_policy_attachments_async(
        self,
        request: main_models.ListPolicyAttachmentsRequest,
    ) -> main_models.ListPolicyAttachmentsResponse:
        runtime = RuntimeOptions()
        return await self.list_policy_attachments_with_options_async(request, runtime)

    def list_policy_versions_with_options(
        self,
        request: main_models.ListPolicyVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicyVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicyVersions',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPolicyVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policy_versions_with_options_async(
        self,
        request: main_models.ListPolicyVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicyVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicyVersions',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPolicyVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policy_versions(
        self,
        request: main_models.ListPolicyVersionsRequest,
    ) -> main_models.ListPolicyVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_policy_versions_with_options(request, runtime)

    async def list_policy_versions_async(
        self,
        request: main_models.ListPolicyVersionsRequest,
    ) -> main_models.ListPolicyVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_policy_versions_with_options_async(request, runtime)

    def list_resource_group_capability_with_options(
        self,
        request: main_models.ListResourceGroupCapabilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupCapabilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        if not DaraCore.is_null(request.support_resource_group_event):
            query['SupportResourceGroupEvent'] = request.support_resource_group_event
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroupCapability',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupCapabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_group_capability_with_options_async(
        self,
        request: main_models.ListResourceGroupCapabilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupCapabilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        if not DaraCore.is_null(request.support_resource_group_event):
            query['SupportResourceGroupEvent'] = request.support_resource_group_event
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroupCapability',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupCapabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_group_capability(
        self,
        request: main_models.ListResourceGroupCapabilityRequest,
    ) -> main_models.ListResourceGroupCapabilityResponse:
        runtime = RuntimeOptions()
        return self.list_resource_group_capability_with_options(request, runtime)

    async def list_resource_group_capability_async(
        self,
        request: main_models.ListResourceGroupCapabilityRequest,
    ) -> main_models.ListResourceGroupCapabilityResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_group_capability_with_options_async(request, runtime)

    def list_resource_groups_with_options(
        self,
        request: main_models.ListResourceGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroups',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_groups_with_options_async(
        self,
        request: main_models.ListResourceGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroups',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_groups(
        self,
        request: main_models.ListResourceGroupsRequest,
    ) -> main_models.ListResourceGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_resource_groups_with_options(request, runtime)

    async def list_resource_groups_async(
        self,
        request: main_models.ListResourceGroupsRequest,
    ) -> main_models.ListResourceGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_groups_with_options_async(request, runtime)

    def list_resource_groups_with_auth_details_with_options(
        self,
        request: main_models.ListResourceGroupsWithAuthDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupsWithAuthDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroupsWithAuthDetails',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupsWithAuthDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_groups_with_auth_details_with_options_async(
        self,
        request: main_models.ListResourceGroupsWithAuthDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupsWithAuthDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroupsWithAuthDetails',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupsWithAuthDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_groups_with_auth_details(
        self,
        request: main_models.ListResourceGroupsWithAuthDetailsRequest,
    ) -> main_models.ListResourceGroupsWithAuthDetailsResponse:
        runtime = RuntimeOptions()
        return self.list_resource_groups_with_auth_details_with_options(request, runtime)

    async def list_resource_groups_with_auth_details_async(
        self,
        request: main_models.ListResourceGroupsWithAuthDetailsRequest,
    ) -> main_models.ListResourceGroupsWithAuthDetailsResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_groups_with_auth_details_with_options_async(request, runtime)

    def list_resources_with_options(
        self,
        request: main_models.ListResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResources',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_with_options_async(
        self,
        request: main_models.ListResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.resource_types):
            query['ResourceTypes'] = request.resource_types
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResources',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources(
        self,
        request: main_models.ListResourcesRequest,
    ) -> main_models.ListResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_resources_with_options(request, runtime)

    async def list_resources_async(
        self,
        request: main_models.ListResourcesRequest,
    ) -> main_models.ListResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_resources_with_options_async(request, runtime)

    def list_roles_with_options(
        self,
        request: main_models.ListRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRoles',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: main_models.ListRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRoles',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_roles(
        self,
        request: main_models.ListRolesRequest,
    ) -> main_models.ListRolesResponse:
        runtime = RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    async def list_roles_async(
        self,
        request: main_models.ListRolesRequest,
    ) -> main_models.ListRolesResponse:
        runtime = RuntimeOptions()
        return await self.list_roles_with_options_async(request, runtime)

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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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

    def lookup_resource_group_events_with_options(
        self,
        request: main_models.LookupResourceGroupEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LookupResourceGroupEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_category):
            query['EventCategory'] = request.event_category
        if not DaraCore.is_null(request.lookup_attributes):
            query['LookupAttributes'] = request.lookup_attributes
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_display_name):
            query['ResourceGroupDisplayName'] = request.resource_group_display_name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LookupResourceGroupEvents',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LookupResourceGroupEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def lookup_resource_group_events_with_options_async(
        self,
        request: main_models.LookupResourceGroupEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LookupResourceGroupEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_category):
            query['EventCategory'] = request.event_category
        if not DaraCore.is_null(request.lookup_attributes):
            query['LookupAttributes'] = request.lookup_attributes
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_display_name):
            query['ResourceGroupDisplayName'] = request.resource_group_display_name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LookupResourceGroupEvents',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LookupResourceGroupEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lookup_resource_group_events(
        self,
        request: main_models.LookupResourceGroupEventsRequest,
    ) -> main_models.LookupResourceGroupEventsResponse:
        runtime = RuntimeOptions()
        return self.lookup_resource_group_events_with_options(request, runtime)

    async def lookup_resource_group_events_async(
        self,
        request: main_models.LookupResourceGroupEventsRequest,
    ) -> main_models.LookupResourceGroupEventsResponse:
        runtime = RuntimeOptions()
        return await self.lookup_resource_group_events_with_options_async(request, runtime)

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
            version = '2020-03-31',
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
            version = '2020-03-31',
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

    def move_resources_with_options(
        self,
        request: main_models.MoveResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResources',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resources_with_options_async(
        self,
        request: main_models.MoveResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResources',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resources(
        self,
        request: main_models.MoveResourcesRequest,
    ) -> main_models.MoveResourcesResponse:
        runtime = RuntimeOptions()
        return self.move_resources_with_options(request, runtime)

    async def move_resources_async(
        self,
        request: main_models.MoveResourcesRequest,
    ) -> main_models.MoveResourcesResponse:
        runtime = RuntimeOptions()
        return await self.move_resources_with_options_async(request, runtime)

    def promote_resource_account_with_options(
        self,
        request: main_models.PromoteResourceAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PromoteResourceAccountResponse:
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
            action = 'PromoteResourceAccount',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PromoteResourceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def promote_resource_account_with_options_async(
        self,
        request: main_models.PromoteResourceAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PromoteResourceAccountResponse:
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
            action = 'PromoteResourceAccount',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PromoteResourceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def promote_resource_account(
        self,
        request: main_models.PromoteResourceAccountRequest,
    ) -> main_models.PromoteResourceAccountResponse:
        runtime = RuntimeOptions()
        return self.promote_resource_account_with_options(request, runtime)

    async def promote_resource_account_async(
        self,
        request: main_models.PromoteResourceAccountRequest,
    ) -> main_models.PromoteResourceAccountResponse:
        runtime = RuntimeOptions()
        return await self.promote_resource_account_with_options_async(request, runtime)

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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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

    def resend_create_cloud_account_email_with_options(
        self,
        request: main_models.ResendCreateCloudAccountEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResendCreateCloudAccountEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResendCreateCloudAccountEmail',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResendCreateCloudAccountEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def resend_create_cloud_account_email_with_options_async(
        self,
        request: main_models.ResendCreateCloudAccountEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResendCreateCloudAccountEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResendCreateCloudAccountEmail',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResendCreateCloudAccountEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resend_create_cloud_account_email(
        self,
        request: main_models.ResendCreateCloudAccountEmailRequest,
    ) -> main_models.ResendCreateCloudAccountEmailResponse:
        runtime = RuntimeOptions()
        return self.resend_create_cloud_account_email_with_options(request, runtime)

    async def resend_create_cloud_account_email_async(
        self,
        request: main_models.ResendCreateCloudAccountEmailRequest,
    ) -> main_models.ResendCreateCloudAccountEmailResponse:
        runtime = RuntimeOptions()
        return await self.resend_create_cloud_account_email_with_options_async(request, runtime)

    def resend_promote_resource_account_email_with_options(
        self,
        request: main_models.ResendPromoteResourceAccountEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResendPromoteResourceAccountEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResendPromoteResourceAccountEmail',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResendPromoteResourceAccountEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def resend_promote_resource_account_email_with_options_async(
        self,
        request: main_models.ResendPromoteResourceAccountEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResendPromoteResourceAccountEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResendPromoteResourceAccountEmail',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResendPromoteResourceAccountEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resend_promote_resource_account_email(
        self,
        request: main_models.ResendPromoteResourceAccountEmailRequest,
    ) -> main_models.ResendPromoteResourceAccountEmailResponse:
        runtime = RuntimeOptions()
        return self.resend_promote_resource_account_email_with_options(request, runtime)

    async def resend_promote_resource_account_email_async(
        self,
        request: main_models.ResendPromoteResourceAccountEmailRequest,
    ) -> main_models.ResendPromoteResourceAccountEmailResponse:
        runtime = RuntimeOptions()
        return await self.resend_promote_resource_account_email_with_options_async(request, runtime)

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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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

    def set_default_policy_version_with_options(
        self,
        request: main_models.SetDefaultPolicyVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDefaultPolicyVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDefaultPolicyVersion',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDefaultPolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_default_policy_version_with_options_async(
        self,
        request: main_models.SetDefaultPolicyVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDefaultPolicyVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDefaultPolicyVersion',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDefaultPolicyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_default_policy_version(
        self,
        request: main_models.SetDefaultPolicyVersionRequest,
    ) -> main_models.SetDefaultPolicyVersionResponse:
        runtime = RuntimeOptions()
        return self.set_default_policy_version_with_options(request, runtime)

    async def set_default_policy_version_async(
        self,
        request: main_models.SetDefaultPolicyVersionRequest,
    ) -> main_models.SetDefaultPolicyVersionResponse:
        runtime = RuntimeOptions()
        return await self.set_default_policy_version_with_options_async(request, runtime)

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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
        if not DaraCore.is_null(request.new_account_type):
            query['NewAccountType'] = request.new_account_type
        if not DaraCore.is_null(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccount',
            version = '2020-03-31',
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
        if not DaraCore.is_null(request.new_account_type):
            query['NewAccountType'] = request.new_account_type
        if not DaraCore.is_null(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccount',
            version = '2020-03-31',
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

    def update_associated_transfer_setting_with_options(
        self,
        request: main_models.UpdateAssociatedTransferSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAssociatedTransferSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_existing_resources_transfer):
            query['EnableExistingResourcesTransfer'] = request.enable_existing_resources_transfer
        if not DaraCore.is_null(request.rule_settings):
            query['RuleSettings'] = request.rule_settings
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAssociatedTransferSetting',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAssociatedTransferSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_associated_transfer_setting_with_options_async(
        self,
        request: main_models.UpdateAssociatedTransferSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAssociatedTransferSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_existing_resources_transfer):
            query['EnableExistingResourcesTransfer'] = request.enable_existing_resources_transfer
        if not DaraCore.is_null(request.rule_settings):
            query['RuleSettings'] = request.rule_settings
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAssociatedTransferSetting',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAssociatedTransferSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_associated_transfer_setting(
        self,
        request: main_models.UpdateAssociatedTransferSettingRequest,
    ) -> main_models.UpdateAssociatedTransferSettingResponse:
        runtime = RuntimeOptions()
        return self.update_associated_transfer_setting_with_options(request, runtime)

    async def update_associated_transfer_setting_async(
        self,
        request: main_models.UpdateAssociatedTransferSettingRequest,
    ) -> main_models.UpdateAssociatedTransferSettingResponse:
        runtime = RuntimeOptions()
        return await self.update_associated_transfer_setting_with_options_async(request, runtime)

    def update_auto_grouping_config_with_options(
        self,
        request: main_models.UpdateAutoGroupingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAutoGroupingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_existing_resources_transfer):
            query['EnableExistingResourcesTransfer'] = request.enable_existing_resources_transfer
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAutoGroupingConfig',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAutoGroupingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_auto_grouping_config_with_options_async(
        self,
        request: main_models.UpdateAutoGroupingConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAutoGroupingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_existing_resources_transfer):
            query['EnableExistingResourcesTransfer'] = request.enable_existing_resources_transfer
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAutoGroupingConfig',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAutoGroupingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_auto_grouping_config(
        self,
        request: main_models.UpdateAutoGroupingConfigRequest,
    ) -> main_models.UpdateAutoGroupingConfigResponse:
        runtime = RuntimeOptions()
        return self.update_auto_grouping_config_with_options(request, runtime)

    async def update_auto_grouping_config_async(
        self,
        request: main_models.UpdateAutoGroupingConfigRequest,
    ) -> main_models.UpdateAutoGroupingConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_auto_grouping_config_with_options_async(request, runtime)

    def update_auto_grouping_rule_with_options(
        self,
        request: main_models.UpdateAutoGroupingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAutoGroupingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            query['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            query['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            query['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        if not DaraCore.is_null(request.exclude_resource_types_scope):
            query['ExcludeResourceTypesScope'] = request.exclude_resource_types_scope
        if not DaraCore.is_null(request.region_ids_scope):
            query['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            query['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            query['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.resource_types_scope):
            query['ResourceTypesScope'] = request.resource_types_scope
        if not DaraCore.is_null(request.rule_contents):
            query['RuleContents'] = request.rule_contents
        if not DaraCore.is_null(request.rule_desc):
            query['RuleDesc'] = request.rule_desc
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAutoGroupingRule',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAutoGroupingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_auto_grouping_rule_with_options_async(
        self,
        request: main_models.UpdateAutoGroupingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAutoGroupingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.exclude_region_ids_scope):
            query['ExcludeRegionIdsScope'] = request.exclude_region_ids_scope
        if not DaraCore.is_null(request.exclude_resource_group_ids_scope):
            query['ExcludeResourceGroupIdsScope'] = request.exclude_resource_group_ids_scope
        if not DaraCore.is_null(request.exclude_resource_ids_scope):
            query['ExcludeResourceIdsScope'] = request.exclude_resource_ids_scope
        if not DaraCore.is_null(request.exclude_resource_types_scope):
            query['ExcludeResourceTypesScope'] = request.exclude_resource_types_scope
        if not DaraCore.is_null(request.region_ids_scope):
            query['RegionIdsScope'] = request.region_ids_scope
        if not DaraCore.is_null(request.resource_group_ids_scope):
            query['ResourceGroupIdsScope'] = request.resource_group_ids_scope
        if not DaraCore.is_null(request.resource_ids_scope):
            query['ResourceIdsScope'] = request.resource_ids_scope
        if not DaraCore.is_null(request.resource_types_scope):
            query['ResourceTypesScope'] = request.resource_types_scope
        if not DaraCore.is_null(request.rule_contents):
            query['RuleContents'] = request.rule_contents
        if not DaraCore.is_null(request.rule_desc):
            query['RuleDesc'] = request.rule_desc
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAutoGroupingRule',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAutoGroupingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_auto_grouping_rule(
        self,
        request: main_models.UpdateAutoGroupingRuleRequest,
    ) -> main_models.UpdateAutoGroupingRuleResponse:
        runtime = RuntimeOptions()
        return self.update_auto_grouping_rule_with_options(request, runtime)

    async def update_auto_grouping_rule_async(
        self,
        request: main_models.UpdateAutoGroupingRuleRequest,
    ) -> main_models.UpdateAutoGroupingRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_auto_grouping_rule_with_options_async(request, runtime)

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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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
            version = '2020-03-31',
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

    def update_resource_group_with_options(
        self,
        request: main_models.UpdateResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceGroup',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_group_with_options_async(
        self,
        request: main_models.UpdateResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceGroup',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_group(
        self,
        request: main_models.UpdateResourceGroupRequest,
    ) -> main_models.UpdateResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.update_resource_group_with_options(request, runtime)

    async def update_resource_group_async(
        self,
        request: main_models.UpdateResourceGroupRequest,
    ) -> main_models.UpdateResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.update_resource_group_with_options_async(request, runtime)

    def update_resource_group_admin_setting_with_options(
        self,
        request: main_models.UpdateResourceGroupAdminSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceGroupAdminSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creator_as_admin):
            query['CreatorAsAdmin'] = request.creator_as_admin
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceGroupAdminSetting',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceGroupAdminSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_group_admin_setting_with_options_async(
        self,
        request: main_models.UpdateResourceGroupAdminSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceGroupAdminSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creator_as_admin):
            query['CreatorAsAdmin'] = request.creator_as_admin
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceGroupAdminSetting',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceGroupAdminSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_group_admin_setting(
        self,
        request: main_models.UpdateResourceGroupAdminSettingRequest,
    ) -> main_models.UpdateResourceGroupAdminSettingResponse:
        runtime = RuntimeOptions()
        return self.update_resource_group_admin_setting_with_options(request, runtime)

    async def update_resource_group_admin_setting_async(
        self,
        request: main_models.UpdateResourceGroupAdminSettingRequest,
    ) -> main_models.UpdateResourceGroupAdminSettingResponse:
        runtime = RuntimeOptions()
        return await self.update_resource_group_admin_setting_with_options_async(request, runtime)

    def update_role_with_options(
        self,
        request: main_models.UpdateRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_assume_role_policy_document):
            query['NewAssumeRolePolicyDocument'] = request.new_assume_role_policy_document
        if not DaraCore.is_null(request.new_description):
            query['NewDescription'] = request.new_description
        if not DaraCore.is_null(request.new_max_session_duration):
            query['NewMaxSessionDuration'] = request.new_max_session_duration
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRole',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_role_with_options_async(
        self,
        request: main_models.UpdateRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_assume_role_policy_document):
            query['NewAssumeRolePolicyDocument'] = request.new_assume_role_policy_document
        if not DaraCore.is_null(request.new_description):
            query['NewDescription'] = request.new_description
        if not DaraCore.is_null(request.new_max_session_duration):
            query['NewMaxSessionDuration'] = request.new_max_session_duration
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRole',
            version = '2020-03-31',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_role(
        self,
        request: main_models.UpdateRoleRequest,
    ) -> main_models.UpdateRoleResponse:
        runtime = RuntimeOptions()
        return self.update_role_with_options(request, runtime)

    async def update_role_async(
        self,
        request: main_models.UpdateRoleRequest,
    ) -> main_models.UpdateRoleResponse:
        runtime = RuntimeOptions()
        return await self.update_role_with_options_async(request, runtime)
