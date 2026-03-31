# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ram20150501 import models as main_models
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
        self._endpoint = self.get_endpoint('ram', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_user_to_group_with_options(
        self,
        request: main_models.AddUserToGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserToGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserToGroup',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_to_group_with_options_async(
        self,
        request: main_models.AddUserToGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserToGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserToGroup',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserToGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_to_group(
        self,
        request: main_models.AddUserToGroupRequest,
    ) -> main_models.AddUserToGroupResponse:
        runtime = RuntimeOptions()
        return self.add_user_to_group_with_options(request, runtime)

    async def add_user_to_group_async(
        self,
        request: main_models.AddUserToGroupRequest,
    ) -> main_models.AddUserToGroupResponse:
        runtime = RuntimeOptions()
        return await self.add_user_to_group_with_options_async(request, runtime)

    def attach_policy_to_group_with_options(
        self,
        request: main_models.AttachPolicyToGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachPolicyToGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachPolicyToGroup',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachPolicyToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_policy_to_group_with_options_async(
        self,
        request: main_models.AttachPolicyToGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachPolicyToGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachPolicyToGroup',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachPolicyToGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_policy_to_group(
        self,
        request: main_models.AttachPolicyToGroupRequest,
    ) -> main_models.AttachPolicyToGroupResponse:
        runtime = RuntimeOptions()
        return self.attach_policy_to_group_with_options(request, runtime)

    async def attach_policy_to_group_async(
        self,
        request: main_models.AttachPolicyToGroupRequest,
    ) -> main_models.AttachPolicyToGroupResponse:
        runtime = RuntimeOptions()
        return await self.attach_policy_to_group_with_options_async(request, runtime)

    def attach_policy_to_role_with_options(
        self,
        request: main_models.AttachPolicyToRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachPolicyToRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachPolicyToRole',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachPolicyToRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_policy_to_role_with_options_async(
        self,
        request: main_models.AttachPolicyToRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachPolicyToRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachPolicyToRole',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachPolicyToRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_policy_to_role(
        self,
        request: main_models.AttachPolicyToRoleRequest,
    ) -> main_models.AttachPolicyToRoleResponse:
        runtime = RuntimeOptions()
        return self.attach_policy_to_role_with_options(request, runtime)

    async def attach_policy_to_role_async(
        self,
        request: main_models.AttachPolicyToRoleRequest,
    ) -> main_models.AttachPolicyToRoleResponse:
        runtime = RuntimeOptions()
        return await self.attach_policy_to_role_with_options_async(request, runtime)

    def attach_policy_to_user_with_options(
        self,
        request: main_models.AttachPolicyToUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachPolicyToUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachPolicyToUser',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachPolicyToUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_policy_to_user_with_options_async(
        self,
        request: main_models.AttachPolicyToUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachPolicyToUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachPolicyToUser',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachPolicyToUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_policy_to_user(
        self,
        request: main_models.AttachPolicyToUserRequest,
    ) -> main_models.AttachPolicyToUserResponse:
        runtime = RuntimeOptions()
        return self.attach_policy_to_user_with_options(request, runtime)

    async def attach_policy_to_user_async(
        self,
        request: main_models.AttachPolicyToUserRequest,
    ) -> main_models.AttachPolicyToUserResponse:
        runtime = RuntimeOptions()
        return await self.attach_policy_to_user_with_options_async(request, runtime)

    def bind_mfadevice_with_options(
        self,
        request: main_models.BindMFADeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindMFADeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authentication_code_1):
            query['AuthenticationCode1'] = request.authentication_code_1
        if not DaraCore.is_null(request.authentication_code_2):
            query['AuthenticationCode2'] = request.authentication_code_2
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindMFADevice',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_mfadevice_with_options_async(
        self,
        request: main_models.BindMFADeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindMFADeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authentication_code_1):
            query['AuthenticationCode1'] = request.authentication_code_1
        if not DaraCore.is_null(request.authentication_code_2):
            query['AuthenticationCode2'] = request.authentication_code_2
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindMFADevice',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindMFADeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_mfadevice(
        self,
        request: main_models.BindMFADeviceRequest,
    ) -> main_models.BindMFADeviceResponse:
        runtime = RuntimeOptions()
        return self.bind_mfadevice_with_options(request, runtime)

    async def bind_mfadevice_async(
        self,
        request: main_models.BindMFADeviceRequest,
    ) -> main_models.BindMFADeviceResponse:
        runtime = RuntimeOptions()
        return await self.bind_mfadevice_with_options_async(request, runtime)

    def change_password_with_options(
        self,
        request: main_models.ChangePasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangePasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_password):
            query['NewPassword'] = request.new_password
        if not DaraCore.is_null(request.old_password):
            query['OldPassword'] = request.old_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangePassword',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangePasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_password_with_options_async(
        self,
        request: main_models.ChangePasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangePasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_password):
            query['NewPassword'] = request.new_password
        if not DaraCore.is_null(request.old_password):
            query['OldPassword'] = request.old_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangePassword',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangePasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_password(
        self,
        request: main_models.ChangePasswordRequest,
    ) -> main_models.ChangePasswordResponse:
        runtime = RuntimeOptions()
        return self.change_password_with_options(request, runtime)

    async def change_password_async(
        self,
        request: main_models.ChangePasswordRequest,
    ) -> main_models.ChangePasswordResponse:
        runtime = RuntimeOptions()
        return await self.change_password_with_options_async(request, runtime)

    def clear_account_alias_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ClearAccountAliasResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ClearAccountAlias',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearAccountAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_account_alias_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ClearAccountAliasResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ClearAccountAlias',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearAccountAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_account_alias(self) -> main_models.ClearAccountAliasResponse:
        runtime = RuntimeOptions()
        return self.clear_account_alias_with_options(runtime)

    async def clear_account_alias_async(self) -> main_models.ClearAccountAliasResponse:
        runtime = RuntimeOptions()
        return await self.clear_account_alias_with_options_async(runtime)

    def create_access_key_with_options(
        self,
        request: main_models.CreateAccessKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessKey',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_key_with_options_async(
        self,
        request: main_models.CreateAccessKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessKey',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_key(
        self,
        request: main_models.CreateAccessKeyRequest,
    ) -> main_models.CreateAccessKeyResponse:
        runtime = RuntimeOptions()
        return self.create_access_key_with_options(request, runtime)

    async def create_access_key_async(
        self,
        request: main_models.CreateAccessKeyRequest,
    ) -> main_models.CreateAccessKeyResponse:
        runtime = RuntimeOptions()
        return await self.create_access_key_with_options_async(request, runtime)

    def create_group_with_options(
        self,
        request: main_models.CreateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comments):
            query['Comments'] = request.comments
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroup',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_with_options_async(
        self,
        request: main_models.CreateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comments):
            query['Comments'] = request.comments
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroup',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group(
        self,
        request: main_models.CreateGroupRequest,
    ) -> main_models.CreateGroupResponse:
        runtime = RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    async def create_group_async(
        self,
        request: main_models.CreateGroupRequest,
    ) -> main_models.CreateGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_group_with_options_async(request, runtime)

    def create_login_profile_with_options(
        self,
        request: main_models.CreateLoginProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoginProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mfabind_required):
            query['MFABindRequired'] = request.mfabind_required
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.password_reset_required):
            query['PasswordResetRequired'] = request.password_reset_required
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoginProfile',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLoginProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_login_profile_with_options_async(
        self,
        request: main_models.CreateLoginProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoginProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mfabind_required):
            query['MFABindRequired'] = request.mfabind_required
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.password_reset_required):
            query['PasswordResetRequired'] = request.password_reset_required
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoginProfile',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLoginProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_login_profile(
        self,
        request: main_models.CreateLoginProfileRequest,
    ) -> main_models.CreateLoginProfileResponse:
        runtime = RuntimeOptions()
        return self.create_login_profile_with_options(request, runtime)

    async def create_login_profile_async(
        self,
        request: main_models.CreateLoginProfileRequest,
    ) -> main_models.CreateLoginProfileResponse:
        runtime = RuntimeOptions()
        return await self.create_login_profile_with_options_async(request, runtime)

    def create_policy_with_options(
        self,
        tmp_req: main_models.CreatePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyResponse:
        tmp_req.validate()
        request = main_models.CreatePolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicy',
            version = '2015-05-01',
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
        tmp_req: main_models.CreatePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyResponse:
        tmp_req.validate()
        request = main_models.CreatePolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicy',
            version = '2015-05-01',
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
        if not DaraCore.is_null(request.rotate_strategy):
            query['RotateStrategy'] = request.rotate_strategy
        if not DaraCore.is_null(request.set_as_default):
            query['SetAsDefault'] = request.set_as_default
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicyVersion',
            version = '2015-05-01',
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
        if not DaraCore.is_null(request.rotate_strategy):
            query['RotateStrategy'] = request.rotate_strategy
        if not DaraCore.is_null(request.set_as_default):
            query['SetAsDefault'] = request.set_as_default
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicyVersion',
            version = '2015-05-01',
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

    def create_role_with_options(
        self,
        tmp_req: main_models.CreateRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRoleResponse:
        tmp_req.validate()
        request = main_models.CreateRoleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.assume_role_policy_document):
            query['AssumeRolePolicyDocument'] = request.assume_role_policy_document
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.max_session_duration):
            query['MaxSessionDuration'] = request.max_session_duration
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRole',
            version = '2015-05-01',
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
        tmp_req: main_models.CreateRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRoleResponse:
        tmp_req.validate()
        request = main_models.CreateRoleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.assume_role_policy_document):
            query['AssumeRolePolicyDocument'] = request.assume_role_policy_document
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.max_session_duration):
            query['MaxSessionDuration'] = request.max_session_duration
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRole',
            version = '2015-05-01',
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

    def create_user_with_options(
        self,
        request: main_models.CreateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comments):
            query['Comments'] = request.comments
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.mobile_phone):
            query['MobilePhone'] = request.mobile_phone
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: main_models.CreateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comments):
            query['Comments'] = request.comments
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.mobile_phone):
            query['MobilePhone'] = request.mobile_phone
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user(
        self,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def create_virtual_mfadevice_with_options(
        self,
        request: main_models.CreateVirtualMFADeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVirtualMFADeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.virtual_mfadevice_name):
            query['VirtualMFADeviceName'] = request.virtual_mfadevice_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVirtualMFADevice',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVirtualMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_virtual_mfadevice_with_options_async(
        self,
        request: main_models.CreateVirtualMFADeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVirtualMFADeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.virtual_mfadevice_name):
            query['VirtualMFADeviceName'] = request.virtual_mfadevice_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVirtualMFADevice',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVirtualMFADeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_virtual_mfadevice(
        self,
        request: main_models.CreateVirtualMFADeviceRequest,
    ) -> main_models.CreateVirtualMFADeviceResponse:
        runtime = RuntimeOptions()
        return self.create_virtual_mfadevice_with_options(request, runtime)

    async def create_virtual_mfadevice_async(
        self,
        request: main_models.CreateVirtualMFADeviceRequest,
    ) -> main_models.CreateVirtualMFADeviceResponse:
        runtime = RuntimeOptions()
        return await self.create_virtual_mfadevice_with_options_async(request, runtime)

    def decode_diagnostic_message_with_options(
        self,
        request: main_models.DecodeDiagnosticMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DecodeDiagnosticMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encoded_diagnostic_message):
            query['EncodedDiagnosticMessage'] = request.encoded_diagnostic_message
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DecodeDiagnosticMessage',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DecodeDiagnosticMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def decode_diagnostic_message_with_options_async(
        self,
        request: main_models.DecodeDiagnosticMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DecodeDiagnosticMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encoded_diagnostic_message):
            query['EncodedDiagnosticMessage'] = request.encoded_diagnostic_message
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DecodeDiagnosticMessage',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DecodeDiagnosticMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def decode_diagnostic_message(
        self,
        request: main_models.DecodeDiagnosticMessageRequest,
    ) -> main_models.DecodeDiagnosticMessageResponse:
        runtime = RuntimeOptions()
        return self.decode_diagnostic_message_with_options(request, runtime)

    async def decode_diagnostic_message_async(
        self,
        request: main_models.DecodeDiagnosticMessageRequest,
    ) -> main_models.DecodeDiagnosticMessageResponse:
        runtime = RuntimeOptions()
        return await self.decode_diagnostic_message_with_options_async(request, runtime)

    def delete_access_key_with_options(
        self,
        request: main_models.DeleteAccessKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessKey',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_key_with_options_async(
        self,
        request: main_models.DeleteAccessKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessKey',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_key(
        self,
        request: main_models.DeleteAccessKeyRequest,
    ) -> main_models.DeleteAccessKeyResponse:
        runtime = RuntimeOptions()
        return self.delete_access_key_with_options(request, runtime)

    async def delete_access_key_async(
        self,
        request: main_models.DeleteAccessKeyRequest,
    ) -> main_models.DeleteAccessKeyResponse:
        runtime = RuntimeOptions()
        return await self.delete_access_key_with_options_async(request, runtime)

    def delete_group_with_options(
        self,
        request: main_models.DeleteGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGroup',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        request: main_models.DeleteGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGroup',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group(
        self,
        request: main_models.DeleteGroupRequest,
    ) -> main_models.DeleteGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    async def delete_group_async(
        self,
        request: main_models.DeleteGroupRequest,
    ) -> main_models.DeleteGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_group_with_options_async(request, runtime)

    def delete_login_profile_with_options(
        self,
        request: main_models.DeleteLoginProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLoginProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLoginProfile',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLoginProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_login_profile_with_options_async(
        self,
        request: main_models.DeleteLoginProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLoginProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLoginProfile',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLoginProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_login_profile(
        self,
        request: main_models.DeleteLoginProfileRequest,
    ) -> main_models.DeleteLoginProfileResponse:
        runtime = RuntimeOptions()
        return self.delete_login_profile_with_options(request, runtime)

    async def delete_login_profile_async(
        self,
        request: main_models.DeleteLoginProfileRequest,
    ) -> main_models.DeleteLoginProfileResponse:
        runtime = RuntimeOptions()
        return await self.delete_login_profile_with_options_async(request, runtime)

    def delete_policy_with_options(
        self,
        request: main_models.DeletePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cascading_delete):
            query['CascadingDelete'] = request.cascading_delete
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicy',
            version = '2015-05-01',
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
        if not DaraCore.is_null(request.cascading_delete):
            query['CascadingDelete'] = request.cascading_delete
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicy',
            version = '2015-05-01',
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
            version = '2015-05-01',
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
            version = '2015-05-01',
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
            version = '2015-05-01',
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
            version = '2015-05-01',
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

    def delete_user_with_options(
        self,
        request: main_models.DeleteUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: main_models.DeleteUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user(
        self,
        request: main_models.DeleteUserRequest,
    ) -> main_models.DeleteUserResponse:
        runtime = RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: main_models.DeleteUserRequest,
    ) -> main_models.DeleteUserResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def delete_virtual_mfadevice_with_options(
        self,
        request: main_models.DeleteVirtualMFADeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVirtualMFADeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVirtualMFADevice',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVirtualMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_virtual_mfadevice_with_options_async(
        self,
        request: main_models.DeleteVirtualMFADeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVirtualMFADeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVirtualMFADevice',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVirtualMFADeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_virtual_mfadevice(
        self,
        request: main_models.DeleteVirtualMFADeviceRequest,
    ) -> main_models.DeleteVirtualMFADeviceResponse:
        runtime = RuntimeOptions()
        return self.delete_virtual_mfadevice_with_options(request, runtime)

    async def delete_virtual_mfadevice_async(
        self,
        request: main_models.DeleteVirtualMFADeviceRequest,
    ) -> main_models.DeleteVirtualMFADeviceResponse:
        runtime = RuntimeOptions()
        return await self.delete_virtual_mfadevice_with_options_async(request, runtime)

    def detach_policy_from_group_with_options(
        self,
        request: main_models.DetachPolicyFromGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachPolicyFromGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachPolicyFromGroup',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachPolicyFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_policy_from_group_with_options_async(
        self,
        request: main_models.DetachPolicyFromGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachPolicyFromGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachPolicyFromGroup',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachPolicyFromGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_policy_from_group(
        self,
        request: main_models.DetachPolicyFromGroupRequest,
    ) -> main_models.DetachPolicyFromGroupResponse:
        runtime = RuntimeOptions()
        return self.detach_policy_from_group_with_options(request, runtime)

    async def detach_policy_from_group_async(
        self,
        request: main_models.DetachPolicyFromGroupRequest,
    ) -> main_models.DetachPolicyFromGroupResponse:
        runtime = RuntimeOptions()
        return await self.detach_policy_from_group_with_options_async(request, runtime)

    def detach_policy_from_role_with_options(
        self,
        request: main_models.DetachPolicyFromRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachPolicyFromRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachPolicyFromRole',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachPolicyFromRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_policy_from_role_with_options_async(
        self,
        request: main_models.DetachPolicyFromRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachPolicyFromRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachPolicyFromRole',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachPolicyFromRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_policy_from_role(
        self,
        request: main_models.DetachPolicyFromRoleRequest,
    ) -> main_models.DetachPolicyFromRoleResponse:
        runtime = RuntimeOptions()
        return self.detach_policy_from_role_with_options(request, runtime)

    async def detach_policy_from_role_async(
        self,
        request: main_models.DetachPolicyFromRoleRequest,
    ) -> main_models.DetachPolicyFromRoleResponse:
        runtime = RuntimeOptions()
        return await self.detach_policy_from_role_with_options_async(request, runtime)

    def detach_policy_from_user_with_options(
        self,
        request: main_models.DetachPolicyFromUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachPolicyFromUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachPolicyFromUser',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachPolicyFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_policy_from_user_with_options_async(
        self,
        request: main_models.DetachPolicyFromUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachPolicyFromUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachPolicyFromUser',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachPolicyFromUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_policy_from_user(
        self,
        request: main_models.DetachPolicyFromUserRequest,
    ) -> main_models.DetachPolicyFromUserResponse:
        runtime = RuntimeOptions()
        return self.detach_policy_from_user_with_options(request, runtime)

    async def detach_policy_from_user_async(
        self,
        request: main_models.DetachPolicyFromUserRequest,
    ) -> main_models.DetachPolicyFromUserResponse:
        runtime = RuntimeOptions()
        return await self.detach_policy_from_user_with_options_async(request, runtime)

    def get_access_key_last_used_with_options(
        self,
        request: main_models.GetAccessKeyLastUsedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessKeyLastUsedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessKeyLastUsed',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessKeyLastUsedResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_key_last_used_with_options_async(
        self,
        request: main_models.GetAccessKeyLastUsedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessKeyLastUsedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessKeyLastUsed',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessKeyLastUsedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_key_last_used(
        self,
        request: main_models.GetAccessKeyLastUsedRequest,
    ) -> main_models.GetAccessKeyLastUsedResponse:
        runtime = RuntimeOptions()
        return self.get_access_key_last_used_with_options(request, runtime)

    async def get_access_key_last_used_async(
        self,
        request: main_models.GetAccessKeyLastUsedRequest,
    ) -> main_models.GetAccessKeyLastUsedResponse:
        runtime = RuntimeOptions()
        return await self.get_access_key_last_used_with_options_async(request, runtime)

    def get_account_alias_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountAliasResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetAccountAlias',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_alias_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountAliasResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetAccountAlias',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_alias(self) -> main_models.GetAccountAliasResponse:
        runtime = RuntimeOptions()
        return self.get_account_alias_with_options(runtime)

    async def get_account_alias_async(self) -> main_models.GetAccountAliasResponse:
        runtime = RuntimeOptions()
        return await self.get_account_alias_with_options_async(runtime)

    def get_group_with_options(
        self,
        request: main_models.GetGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGroup',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_group_with_options_async(
        self,
        request: main_models.GetGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGroup',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_group(
        self,
        request: main_models.GetGroupRequest,
    ) -> main_models.GetGroupResponse:
        runtime = RuntimeOptions()
        return self.get_group_with_options(request, runtime)

    async def get_group_async(
        self,
        request: main_models.GetGroupRequest,
    ) -> main_models.GetGroupResponse:
        runtime = RuntimeOptions()
        return await self.get_group_with_options_async(request, runtime)

    def get_login_profile_with_options(
        self,
        request: main_models.GetLoginProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLoginProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLoginProfile',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLoginProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_login_profile_with_options_async(
        self,
        request: main_models.GetLoginProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLoginProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLoginProfile',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLoginProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_login_profile(
        self,
        request: main_models.GetLoginProfileRequest,
    ) -> main_models.GetLoginProfileResponse:
        runtime = RuntimeOptions()
        return self.get_login_profile_with_options(request, runtime)

    async def get_login_profile_async(
        self,
        request: main_models.GetLoginProfileRequest,
    ) -> main_models.GetLoginProfileResponse:
        runtime = RuntimeOptions()
        return await self.get_login_profile_with_options_async(request, runtime)

    def get_password_policy_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetPasswordPolicyResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetPasswordPolicy',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPasswordPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_password_policy_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetPasswordPolicyResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetPasswordPolicy',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPasswordPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_password_policy(self) -> main_models.GetPasswordPolicyResponse:
        runtime = RuntimeOptions()
        return self.get_password_policy_with_options(runtime)

    async def get_password_policy_async(self) -> main_models.GetPasswordPolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_password_policy_with_options_async(runtime)

    def get_policy_with_options(
        self,
        request: main_models.GetPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyResponse:
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
            action = 'GetPolicy',
            version = '2015-05-01',
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
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPolicy',
            version = '2015-05-01',
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
            version = '2015-05-01',
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
            version = '2015-05-01',
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

    def get_role_with_options(
        self,
        request: main_models.GetRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRole',
            version = '2015-05-01',
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
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRole',
            version = '2015-05-01',
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

    def get_security_preference_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecurityPreferenceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetSecurityPreference',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecurityPreferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_security_preference_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecurityPreferenceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetSecurityPreference',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecurityPreferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_security_preference(self) -> main_models.GetSecurityPreferenceResponse:
        runtime = RuntimeOptions()
        return self.get_security_preference_with_options(runtime)

    async def get_security_preference_async(self) -> main_models.GetSecurityPreferenceResponse:
        runtime = RuntimeOptions()
        return await self.get_security_preference_with_options_async(runtime)

    def get_user_with_options(
        self,
        request: main_models.GetUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: main_models.GetUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: main_models.GetUserRequest,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: main_models.GetUserRequest,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def get_user_mfainfo_with_options(
        self,
        request: main_models.GetUserMFAInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserMFAInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserMFAInfo',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserMFAInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_mfainfo_with_options_async(
        self,
        request: main_models.GetUserMFAInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserMFAInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserMFAInfo',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserMFAInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_mfainfo(
        self,
        request: main_models.GetUserMFAInfoRequest,
    ) -> main_models.GetUserMFAInfoResponse:
        runtime = RuntimeOptions()
        return self.get_user_mfainfo_with_options(request, runtime)

    async def get_user_mfainfo_async(
        self,
        request: main_models.GetUserMFAInfoRequest,
    ) -> main_models.GetUserMFAInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_user_mfainfo_with_options_async(request, runtime)

    def list_access_keys_with_options(
        self,
        request: main_models.ListAccessKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccessKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccessKeys',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccessKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_access_keys_with_options_async(
        self,
        request: main_models.ListAccessKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccessKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccessKeys',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccessKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_access_keys(
        self,
        request: main_models.ListAccessKeysRequest,
    ) -> main_models.ListAccessKeysResponse:
        runtime = RuntimeOptions()
        return self.list_access_keys_with_options(request, runtime)

    async def list_access_keys_async(
        self,
        request: main_models.ListAccessKeysRequest,
    ) -> main_models.ListAccessKeysResponse:
        runtime = RuntimeOptions()
        return await self.list_access_keys_with_options_async(request, runtime)

    def list_entities_for_policy_with_options(
        self,
        request: main_models.ListEntitiesForPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEntitiesForPolicyResponse:
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
            action = 'ListEntitiesForPolicy',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEntitiesForPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_entities_for_policy_with_options_async(
        self,
        request: main_models.ListEntitiesForPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEntitiesForPolicyResponse:
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
            action = 'ListEntitiesForPolicy',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEntitiesForPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_entities_for_policy(
        self,
        request: main_models.ListEntitiesForPolicyRequest,
    ) -> main_models.ListEntitiesForPolicyResponse:
        runtime = RuntimeOptions()
        return self.list_entities_for_policy_with_options(request, runtime)

    async def list_entities_for_policy_async(
        self,
        request: main_models.ListEntitiesForPolicyRequest,
    ) -> main_models.ListEntitiesForPolicyResponse:
        runtime = RuntimeOptions()
        return await self.list_entities_for_policy_with_options_async(request, runtime)

    def list_groups_with_options(
        self,
        request: main_models.ListGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroups',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_with_options_async(
        self,
        request: main_models.ListGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroups',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups(
        self,
        request: main_models.ListGroupsRequest,
    ) -> main_models.ListGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_groups_with_options(request, runtime)

    async def list_groups_async(
        self,
        request: main_models.ListGroupsRequest,
    ) -> main_models.ListGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_groups_with_options_async(request, runtime)

    def list_groups_for_user_with_options(
        self,
        request: main_models.ListGroupsForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroupsForUser',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_for_user_with_options_async(
        self,
        request: main_models.ListGroupsForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroupsForUser',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups_for_user(
        self,
        request: main_models.ListGroupsForUserRequest,
    ) -> main_models.ListGroupsForUserResponse:
        runtime = RuntimeOptions()
        return self.list_groups_for_user_with_options(request, runtime)

    async def list_groups_for_user_async(
        self,
        request: main_models.ListGroupsForUserRequest,
    ) -> main_models.ListGroupsForUserResponse:
        runtime = RuntimeOptions()
        return await self.list_groups_for_user_with_options_async(request, runtime)

    def list_policies_with_options(
        self,
        tmp_req: main_models.ListPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesResponse:
        tmp_req.validate()
        request = main_models.ListPoliciesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.max_items):
            query['MaxItems'] = request.max_items
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicies',
            version = '2015-05-01',
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
        tmp_req: main_models.ListPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesResponse:
        tmp_req.validate()
        request = main_models.ListPoliciesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.max_items):
            query['MaxItems'] = request.max_items
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicies',
            version = '2015-05-01',
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

    def list_policies_for_group_with_options(
        self,
        request: main_models.ListPoliciesForGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesForGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPoliciesForGroup',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesForGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_for_group_with_options_async(
        self,
        request: main_models.ListPoliciesForGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesForGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPoliciesForGroup',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesForGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies_for_group(
        self,
        request: main_models.ListPoliciesForGroupRequest,
    ) -> main_models.ListPoliciesForGroupResponse:
        runtime = RuntimeOptions()
        return self.list_policies_for_group_with_options(request, runtime)

    async def list_policies_for_group_async(
        self,
        request: main_models.ListPoliciesForGroupRequest,
    ) -> main_models.ListPoliciesForGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_policies_for_group_with_options_async(request, runtime)

    def list_policies_for_role_with_options(
        self,
        request: main_models.ListPoliciesForRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesForRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPoliciesForRole',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesForRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_for_role_with_options_async(
        self,
        request: main_models.ListPoliciesForRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesForRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPoliciesForRole',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesForRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies_for_role(
        self,
        request: main_models.ListPoliciesForRoleRequest,
    ) -> main_models.ListPoliciesForRoleResponse:
        runtime = RuntimeOptions()
        return self.list_policies_for_role_with_options(request, runtime)

    async def list_policies_for_role_async(
        self,
        request: main_models.ListPoliciesForRoleRequest,
    ) -> main_models.ListPoliciesForRoleResponse:
        runtime = RuntimeOptions()
        return await self.list_policies_for_role_with_options_async(request, runtime)

    def list_policies_for_user_with_options(
        self,
        request: main_models.ListPoliciesForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPoliciesForUser',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_for_user_with_options_async(
        self,
        request: main_models.ListPoliciesForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPoliciesForUser',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies_for_user(
        self,
        request: main_models.ListPoliciesForUserRequest,
    ) -> main_models.ListPoliciesForUserResponse:
        runtime = RuntimeOptions()
        return self.list_policies_for_user_with_options(request, runtime)

    async def list_policies_for_user_async(
        self,
        request: main_models.ListPoliciesForUserRequest,
    ) -> main_models.ListPoliciesForUserResponse:
        runtime = RuntimeOptions()
        return await self.list_policies_for_user_with_options_async(request, runtime)

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
            version = '2015-05-01',
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
            version = '2015-05-01',
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

    def list_roles_with_options(
        self,
        tmp_req: main_models.ListRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRolesResponse:
        tmp_req.validate()
        request = main_models.ListRolesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.max_items):
            query['MaxItems'] = request.max_items
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRoles',
            version = '2015-05-01',
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
        tmp_req: main_models.ListRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRolesResponse:
        tmp_req.validate()
        request = main_models.ListRolesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.max_items):
            query['MaxItems'] = request.max_items
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRoles',
            version = '2015-05-01',
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

    def list_tag_resources_with_options(
        self,
        tmp_req: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_names):
            request.resource_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_names, 'ResourceNames', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_names_shrink):
            query['ResourceNames'] = request.resource_names_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2015-05-01',
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
        tmp_req: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_names):
            request.resource_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_names, 'ResourceNames', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_names_shrink):
            query['ResourceNames'] = request.resource_names_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2015-05-01',
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

    def list_users_with_options(
        self,
        request: main_models.ListUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: main_models.ListUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def list_users_for_group_with_options(
        self,
        request: main_models.ListUsersForGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersForGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsersForGroup',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersForGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_for_group_with_options_async(
        self,
        request: main_models.ListUsersForGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersForGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsersForGroup',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersForGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users_for_group(
        self,
        request: main_models.ListUsersForGroupRequest,
    ) -> main_models.ListUsersForGroupResponse:
        runtime = RuntimeOptions()
        return self.list_users_for_group_with_options(request, runtime)

    async def list_users_for_group_async(
        self,
        request: main_models.ListUsersForGroupRequest,
    ) -> main_models.ListUsersForGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_users_for_group_with_options_async(request, runtime)

    def list_virtual_mfadevices_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListVirtualMFADevicesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListVirtualMFADevices',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVirtualMFADevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_virtual_mfadevices_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListVirtualMFADevicesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListVirtualMFADevices',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVirtualMFADevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_virtual_mfadevices(self) -> main_models.ListVirtualMFADevicesResponse:
        runtime = RuntimeOptions()
        return self.list_virtual_mfadevices_with_options(runtime)

    async def list_virtual_mfadevices_async(self) -> main_models.ListVirtualMFADevicesResponse:
        runtime = RuntimeOptions()
        return await self.list_virtual_mfadevices_with_options_async(runtime)

    def remove_user_from_group_with_options(
        self,
        request: main_models.RemoveUserFromGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserFromGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUserFromGroup',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUserFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_user_from_group_with_options_async(
        self,
        request: main_models.RemoveUserFromGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserFromGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUserFromGroup',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUserFromGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_user_from_group(
        self,
        request: main_models.RemoveUserFromGroupRequest,
    ) -> main_models.RemoveUserFromGroupResponse:
        runtime = RuntimeOptions()
        return self.remove_user_from_group_with_options(request, runtime)

    async def remove_user_from_group_async(
        self,
        request: main_models.RemoveUserFromGroupRequest,
    ) -> main_models.RemoveUserFromGroupResponse:
        runtime = RuntimeOptions()
        return await self.remove_user_from_group_with_options_async(request, runtime)

    def set_account_alias_with_options(
        self,
        request: main_models.SetAccountAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAccountAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_alias):
            query['AccountAlias'] = request.account_alias
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAccountAlias',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAccountAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_account_alias_with_options_async(
        self,
        request: main_models.SetAccountAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAccountAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_alias):
            query['AccountAlias'] = request.account_alias
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAccountAlias',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAccountAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_account_alias(
        self,
        request: main_models.SetAccountAliasRequest,
    ) -> main_models.SetAccountAliasResponse:
        runtime = RuntimeOptions()
        return self.set_account_alias_with_options(request, runtime)

    async def set_account_alias_async(
        self,
        request: main_models.SetAccountAliasRequest,
    ) -> main_models.SetAccountAliasResponse:
        runtime = RuntimeOptions()
        return await self.set_account_alias_with_options_async(request, runtime)

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
            version = '2015-05-01',
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
            version = '2015-05-01',
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

    def set_password_policy_with_options(
        self,
        request: main_models.SetPasswordPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPasswordPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hard_expiry):
            query['HardExpiry'] = request.hard_expiry
        if not DaraCore.is_null(request.max_login_attemps):
            query['MaxLoginAttemps'] = request.max_login_attemps
        if not DaraCore.is_null(request.max_password_age):
            query['MaxPasswordAge'] = request.max_password_age
        if not DaraCore.is_null(request.minimum_password_length):
            query['MinimumPasswordLength'] = request.minimum_password_length
        if not DaraCore.is_null(request.password_reuse_prevention):
            query['PasswordReusePrevention'] = request.password_reuse_prevention
        if not DaraCore.is_null(request.require_lowercase_characters):
            query['RequireLowercaseCharacters'] = request.require_lowercase_characters
        if not DaraCore.is_null(request.require_numbers):
            query['RequireNumbers'] = request.require_numbers
        if not DaraCore.is_null(request.require_symbols):
            query['RequireSymbols'] = request.require_symbols
        if not DaraCore.is_null(request.require_uppercase_characters):
            query['RequireUppercaseCharacters'] = request.require_uppercase_characters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPasswordPolicy',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPasswordPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_password_policy_with_options_async(
        self,
        request: main_models.SetPasswordPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPasswordPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hard_expiry):
            query['HardExpiry'] = request.hard_expiry
        if not DaraCore.is_null(request.max_login_attemps):
            query['MaxLoginAttemps'] = request.max_login_attemps
        if not DaraCore.is_null(request.max_password_age):
            query['MaxPasswordAge'] = request.max_password_age
        if not DaraCore.is_null(request.minimum_password_length):
            query['MinimumPasswordLength'] = request.minimum_password_length
        if not DaraCore.is_null(request.password_reuse_prevention):
            query['PasswordReusePrevention'] = request.password_reuse_prevention
        if not DaraCore.is_null(request.require_lowercase_characters):
            query['RequireLowercaseCharacters'] = request.require_lowercase_characters
        if not DaraCore.is_null(request.require_numbers):
            query['RequireNumbers'] = request.require_numbers
        if not DaraCore.is_null(request.require_symbols):
            query['RequireSymbols'] = request.require_symbols
        if not DaraCore.is_null(request.require_uppercase_characters):
            query['RequireUppercaseCharacters'] = request.require_uppercase_characters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPasswordPolicy',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPasswordPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_password_policy(
        self,
        request: main_models.SetPasswordPolicyRequest,
    ) -> main_models.SetPasswordPolicyResponse:
        runtime = RuntimeOptions()
        return self.set_password_policy_with_options(request, runtime)

    async def set_password_policy_async(
        self,
        request: main_models.SetPasswordPolicyRequest,
    ) -> main_models.SetPasswordPolicyResponse:
        runtime = RuntimeOptions()
        return await self.set_password_policy_with_options_async(request, runtime)

    def set_security_preference_with_options(
        self,
        request: main_models.SetSecurityPreferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSecurityPreferenceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_user_to_change_password):
            query['AllowUserToChangePassword'] = request.allow_user_to_change_password
        if not DaraCore.is_null(request.allow_user_to_manage_access_keys):
            query['AllowUserToManageAccessKeys'] = request.allow_user_to_manage_access_keys
        if not DaraCore.is_null(request.allow_user_to_manage_mfadevices):
            query['AllowUserToManageMFADevices'] = request.allow_user_to_manage_mfadevices
        if not DaraCore.is_null(request.allow_user_to_manage_public_keys):
            query['AllowUserToManagePublicKeys'] = request.allow_user_to_manage_public_keys
        if not DaraCore.is_null(request.enable_save_mfaticket):
            query['EnableSaveMFATicket'] = request.enable_save_mfaticket
        if not DaraCore.is_null(request.login_network_masks):
            query['LoginNetworkMasks'] = request.login_network_masks
        if not DaraCore.is_null(request.login_session_duration):
            query['LoginSessionDuration'] = request.login_session_duration
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetSecurityPreference',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetSecurityPreferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_security_preference_with_options_async(
        self,
        request: main_models.SetSecurityPreferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSecurityPreferenceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_user_to_change_password):
            query['AllowUserToChangePassword'] = request.allow_user_to_change_password
        if not DaraCore.is_null(request.allow_user_to_manage_access_keys):
            query['AllowUserToManageAccessKeys'] = request.allow_user_to_manage_access_keys
        if not DaraCore.is_null(request.allow_user_to_manage_mfadevices):
            query['AllowUserToManageMFADevices'] = request.allow_user_to_manage_mfadevices
        if not DaraCore.is_null(request.allow_user_to_manage_public_keys):
            query['AllowUserToManagePublicKeys'] = request.allow_user_to_manage_public_keys
        if not DaraCore.is_null(request.enable_save_mfaticket):
            query['EnableSaveMFATicket'] = request.enable_save_mfaticket
        if not DaraCore.is_null(request.login_network_masks):
            query['LoginNetworkMasks'] = request.login_network_masks
        if not DaraCore.is_null(request.login_session_duration):
            query['LoginSessionDuration'] = request.login_session_duration
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetSecurityPreference',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetSecurityPreferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_security_preference(
        self,
        request: main_models.SetSecurityPreferenceRequest,
    ) -> main_models.SetSecurityPreferenceResponse:
        runtime = RuntimeOptions()
        return self.set_security_preference_with_options(request, runtime)

    async def set_security_preference_async(
        self,
        request: main_models.SetSecurityPreferenceRequest,
    ) -> main_models.SetSecurityPreferenceResponse:
        runtime = RuntimeOptions()
        return await self.set_security_preference_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        tmp_req: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        tmp_req.validate()
        request = main_models.TagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_names):
            request.resource_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_names, 'ResourceNames', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.resource_names_shrink):
            query['ResourceNames'] = request.resource_names_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2015-05-01',
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
        tmp_req: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        tmp_req.validate()
        request = main_models.TagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_names):
            request.resource_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_names, 'ResourceNames', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.resource_names_shrink):
            query['ResourceNames'] = request.resource_names_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2015-05-01',
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

    def unbind_mfadevice_with_options(
        self,
        request: main_models.UnbindMFADeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindMFADeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindMFADevice',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_mfadevice_with_options_async(
        self,
        request: main_models.UnbindMFADeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindMFADeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindMFADevice',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindMFADeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_mfadevice(
        self,
        request: main_models.UnbindMFADeviceRequest,
    ) -> main_models.UnbindMFADeviceResponse:
        runtime = RuntimeOptions()
        return self.unbind_mfadevice_with_options(request, runtime)

    async def unbind_mfadevice_async(
        self,
        request: main_models.UnbindMFADeviceRequest,
    ) -> main_models.UnbindMFADeviceResponse:
        runtime = RuntimeOptions()
        return await self.unbind_mfadevice_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        tmp_req: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        tmp_req.validate()
        request = main_models.UntagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_names):
            request.resource_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_names, 'ResourceNames', 'json')
        if not DaraCore.is_null(tmp_req.tag_keys):
            request.tag_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_names_shrink):
            query['ResourceNames'] = request.resource_names_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_keys_shrink):
            query['TagKeys'] = request.tag_keys_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2015-05-01',
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
        tmp_req: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        tmp_req.validate()
        request = main_models.UntagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_names):
            request.resource_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_names, 'ResourceNames', 'json')
        if not DaraCore.is_null(tmp_req.tag_keys):
            request.tag_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_names_shrink):
            query['ResourceNames'] = request.resource_names_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_keys_shrink):
            query['TagKeys'] = request.tag_keys_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2015-05-01',
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

    def update_access_key_with_options(
        self,
        request: main_models.UpdateAccessKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAccessKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccessKey',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAccessKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_access_key_with_options_async(
        self,
        request: main_models.UpdateAccessKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAccessKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccessKey',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAccessKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_access_key(
        self,
        request: main_models.UpdateAccessKeyRequest,
    ) -> main_models.UpdateAccessKeyResponse:
        runtime = RuntimeOptions()
        return self.update_access_key_with_options(request, runtime)

    async def update_access_key_async(
        self,
        request: main_models.UpdateAccessKeyRequest,
    ) -> main_models.UpdateAccessKeyResponse:
        runtime = RuntimeOptions()
        return await self.update_access_key_with_options_async(request, runtime)

    def update_group_with_options(
        self,
        request: main_models.UpdateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.new_comments):
            query['NewComments'] = request.new_comments
        if not DaraCore.is_null(request.new_group_name):
            query['NewGroupName'] = request.new_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGroup',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_group_with_options_async(
        self,
        request: main_models.UpdateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.new_comments):
            query['NewComments'] = request.new_comments
        if not DaraCore.is_null(request.new_group_name):
            query['NewGroupName'] = request.new_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGroup',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_group(
        self,
        request: main_models.UpdateGroupRequest,
    ) -> main_models.UpdateGroupResponse:
        runtime = RuntimeOptions()
        return self.update_group_with_options(request, runtime)

    async def update_group_async(
        self,
        request: main_models.UpdateGroupRequest,
    ) -> main_models.UpdateGroupResponse:
        runtime = RuntimeOptions()
        return await self.update_group_with_options_async(request, runtime)

    def update_login_profile_with_options(
        self,
        request: main_models.UpdateLoginProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLoginProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mfabind_required):
            query['MFABindRequired'] = request.mfabind_required
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.password_reset_required):
            query['PasswordResetRequired'] = request.password_reset_required
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoginProfile',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLoginProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_login_profile_with_options_async(
        self,
        request: main_models.UpdateLoginProfileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLoginProfileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mfabind_required):
            query['MFABindRequired'] = request.mfabind_required
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.password_reset_required):
            query['PasswordResetRequired'] = request.password_reset_required
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoginProfile',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLoginProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_login_profile(
        self,
        request: main_models.UpdateLoginProfileRequest,
    ) -> main_models.UpdateLoginProfileResponse:
        runtime = RuntimeOptions()
        return self.update_login_profile_with_options(request, runtime)

    async def update_login_profile_async(
        self,
        request: main_models.UpdateLoginProfileRequest,
    ) -> main_models.UpdateLoginProfileResponse:
        runtime = RuntimeOptions()
        return await self.update_login_profile_with_options_async(request, runtime)

    def update_policy_description_with_options(
        self,
        request: main_models.UpdatePolicyDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePolicyDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_description):
            query['NewDescription'] = request.new_description
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePolicyDescription',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePolicyDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_policy_description_with_options_async(
        self,
        request: main_models.UpdatePolicyDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePolicyDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_description):
            query['NewDescription'] = request.new_description
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePolicyDescription',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePolicyDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_policy_description(
        self,
        request: main_models.UpdatePolicyDescriptionRequest,
    ) -> main_models.UpdatePolicyDescriptionResponse:
        runtime = RuntimeOptions()
        return self.update_policy_description_with_options(request, runtime)

    async def update_policy_description_async(
        self,
        request: main_models.UpdatePolicyDescriptionRequest,
    ) -> main_models.UpdatePolicyDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.update_policy_description_with_options_async(request, runtime)

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
            version = '2015-05-01',
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
            version = '2015-05-01',
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

    def update_user_with_options(
        self,
        request: main_models.UpdateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_comments):
            query['NewComments'] = request.new_comments
        if not DaraCore.is_null(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not DaraCore.is_null(request.new_email):
            query['NewEmail'] = request.new_email
        if not DaraCore.is_null(request.new_mobile_phone):
            query['NewMobilePhone'] = request.new_mobile_phone
        if not DaraCore.is_null(request.new_user_name):
            query['NewUserName'] = request.new_user_name
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: main_models.UpdateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_comments):
            query['NewComments'] = request.new_comments
        if not DaraCore.is_null(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not DaraCore.is_null(request.new_email):
            query['NewEmail'] = request.new_email
        if not DaraCore.is_null(request.new_mobile_phone):
            query['NewMobilePhone'] = request.new_mobile_phone
        if not DaraCore.is_null(request.new_user_name):
            query['NewUserName'] = request.new_user_name
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2015-05-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)
