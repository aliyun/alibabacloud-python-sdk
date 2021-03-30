# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ram20150501 import models as ram_20150501_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_user_to_group_with_options(
        self,
        request: ram_20150501_models.AddUserToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.AddUserToGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddUserToGroup',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.AddUserToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_to_group_with_options_async(
        self,
        request: ram_20150501_models.AddUserToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.AddUserToGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddUserToGroup',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.AddUserToGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_to_group(
        self,
        request: ram_20150501_models.AddUserToGroupRequest,
    ) -> ram_20150501_models.AddUserToGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_group_with_options(request, runtime)

    async def add_user_to_group_async(
        self,
        request: ram_20150501_models.AddUserToGroupRequest,
    ) -> ram_20150501_models.AddUserToGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_user_to_group_with_options_async(request, runtime)

    def attach_policy_to_group_with_options(
        self,
        request: ram_20150501_models.AttachPolicyToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.AttachPolicyToGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['PolicyName'] = request.policy_name
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AttachPolicyToGroup',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.AttachPolicyToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_policy_to_group_with_options_async(
        self,
        request: ram_20150501_models.AttachPolicyToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.AttachPolicyToGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['PolicyName'] = request.policy_name
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AttachPolicyToGroup',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.AttachPolicyToGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_policy_to_group(
        self,
        request: ram_20150501_models.AttachPolicyToGroupRequest,
    ) -> ram_20150501_models.AttachPolicyToGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_policy_to_group_with_options(request, runtime)

    async def attach_policy_to_group_async(
        self,
        request: ram_20150501_models.AttachPolicyToGroupRequest,
    ) -> ram_20150501_models.AttachPolicyToGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_policy_to_group_with_options_async(request, runtime)

    def attach_policy_to_role_with_options(
        self,
        request: ram_20150501_models.AttachPolicyToRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.AttachPolicyToRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['PolicyName'] = request.policy_name
        query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AttachPolicyToRole',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.AttachPolicyToRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_policy_to_role_with_options_async(
        self,
        request: ram_20150501_models.AttachPolicyToRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.AttachPolicyToRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['PolicyName'] = request.policy_name
        query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AttachPolicyToRole',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.AttachPolicyToRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_policy_to_role(
        self,
        request: ram_20150501_models.AttachPolicyToRoleRequest,
    ) -> ram_20150501_models.AttachPolicyToRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_policy_to_role_with_options(request, runtime)

    async def attach_policy_to_role_async(
        self,
        request: ram_20150501_models.AttachPolicyToRoleRequest,
    ) -> ram_20150501_models.AttachPolicyToRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_policy_to_role_with_options_async(request, runtime)

    def attach_policy_to_user_with_options(
        self,
        request: ram_20150501_models.AttachPolicyToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.AttachPolicyToUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['PolicyName'] = request.policy_name
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AttachPolicyToUser',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.AttachPolicyToUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_policy_to_user_with_options_async(
        self,
        request: ram_20150501_models.AttachPolicyToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.AttachPolicyToUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['PolicyName'] = request.policy_name
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AttachPolicyToUser',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.AttachPolicyToUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_policy_to_user(
        self,
        request: ram_20150501_models.AttachPolicyToUserRequest,
    ) -> ram_20150501_models.AttachPolicyToUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_policy_to_user_with_options(request, runtime)

    async def attach_policy_to_user_async(
        self,
        request: ram_20150501_models.AttachPolicyToUserRequest,
    ) -> ram_20150501_models.AttachPolicyToUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_policy_to_user_with_options_async(request, runtime)

    def bind_mfadevice_with_options(
        self,
        request: ram_20150501_models.BindMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.BindMFADeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SerialNumber'] = request.serial_number
        query['UserName'] = request.user_name
        query['AuthenticationCode1'] = request.authentication_code_1
        query['AuthenticationCode2'] = request.authentication_code_2
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BindMFADevice',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.BindMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_mfadevice_with_options_async(
        self,
        request: ram_20150501_models.BindMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.BindMFADeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SerialNumber'] = request.serial_number
        query['UserName'] = request.user_name
        query['AuthenticationCode1'] = request.authentication_code_1
        query['AuthenticationCode2'] = request.authentication_code_2
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BindMFADevice',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.BindMFADeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_mfadevice(
        self,
        request: ram_20150501_models.BindMFADeviceRequest,
    ) -> ram_20150501_models.BindMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_mfadevice_with_options(request, runtime)

    async def bind_mfadevice_async(
        self,
        request: ram_20150501_models.BindMFADeviceRequest,
    ) -> ram_20150501_models.BindMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_mfadevice_with_options_async(request, runtime)

    def change_password_with_options(
        self,
        request: ram_20150501_models.ChangePasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ChangePasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OldPassword'] = request.old_password
        query['NewPassword'] = request.new_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ChangePassword',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ChangePasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_password_with_options_async(
        self,
        request: ram_20150501_models.ChangePasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ChangePasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OldPassword'] = request.old_password
        query['NewPassword'] = request.new_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ChangePassword',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ChangePasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_password(
        self,
        request: ram_20150501_models.ChangePasswordRequest,
    ) -> ram_20150501_models.ChangePasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_password_with_options(request, runtime)

    async def change_password_async(
        self,
        request: ram_20150501_models.ChangePasswordRequest,
    ) -> ram_20150501_models.ChangePasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_password_with_options_async(request, runtime)

    def clear_account_alias_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ClearAccountAliasResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ClearAccountAlias',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ClearAccountAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_account_alias_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ClearAccountAliasResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ClearAccountAlias',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ClearAccountAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_account_alias(self) -> ram_20150501_models.ClearAccountAliasResponse:
        runtime = util_models.RuntimeOptions()
        return self.clear_account_alias_with_options(runtime)

    async def clear_account_alias_async(self) -> ram_20150501_models.ClearAccountAliasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clear_account_alias_with_options_async(runtime)

    def create_access_key_with_options(
        self,
        request: ram_20150501_models.CreateAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreateAccessKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccessKey',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.CreateAccessKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_key_with_options_async(
        self,
        request: ram_20150501_models.CreateAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreateAccessKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccessKey',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.CreateAccessKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_key(
        self,
        request: ram_20150501_models.CreateAccessKeyRequest,
    ) -> ram_20150501_models.CreateAccessKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_access_key_with_options(request, runtime)

    async def create_access_key_async(
        self,
        request: ram_20150501_models.CreateAccessKeyRequest,
    ) -> ram_20150501_models.CreateAccessKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_access_key_with_options_async(request, runtime)

    def create_group_with_options(
        self,
        request: ram_20150501_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreateGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupName'] = request.group_name
        query['Comments'] = request.comments
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.CreateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_with_options_async(
        self,
        request: ram_20150501_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreateGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupName'] = request.group_name
        query['Comments'] = request.comments
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.CreateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group(
        self,
        request: ram_20150501_models.CreateGroupRequest,
    ) -> ram_20150501_models.CreateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    async def create_group_async(
        self,
        request: ram_20150501_models.CreateGroupRequest,
    ) -> ram_20150501_models.CreateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_group_with_options_async(request, runtime)

    def create_login_profile_with_options(
        self,
        request: ram_20150501_models.CreateLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreateLoginProfileResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        query['Password'] = request.password
        query['PasswordResetRequired'] = request.password_reset_required
        query['MFABindRequired'] = request.mfabind_required
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateLoginProfile',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.CreateLoginProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_login_profile_with_options_async(
        self,
        request: ram_20150501_models.CreateLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreateLoginProfileResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        query['Password'] = request.password
        query['PasswordResetRequired'] = request.password_reset_required
        query['MFABindRequired'] = request.mfabind_required
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateLoginProfile',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.CreateLoginProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_login_profile(
        self,
        request: ram_20150501_models.CreateLoginProfileRequest,
    ) -> ram_20150501_models.CreateLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_login_profile_with_options(request, runtime)

    async def create_login_profile_async(
        self,
        request: ram_20150501_models.CreateLoginProfileRequest,
    ) -> ram_20150501_models.CreateLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_login_profile_with_options_async(request, runtime)

    def create_policy_with_options(
        self,
        request: ram_20150501_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreatePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyName'] = request.policy_name
        query['Description'] = request.description
        query['PolicyDocument'] = request.policy_document
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreatePolicy',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.CreatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_with_options_async(
        self,
        request: ram_20150501_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreatePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyName'] = request.policy_name
        query['Description'] = request.description
        query['PolicyDocument'] = request.policy_document
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreatePolicy',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.CreatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy(
        self,
        request: ram_20150501_models.CreatePolicyRequest,
    ) -> ram_20150501_models.CreatePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_policy_with_options(request, runtime)

    async def create_policy_async(
        self,
        request: ram_20150501_models.CreatePolicyRequest,
    ) -> ram_20150501_models.CreatePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_with_options_async(request, runtime)

    def create_policy_version_with_options(
        self,
        request: ram_20150501_models.CreatePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreatePolicyVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyName'] = request.policy_name
        query['PolicyDocument'] = request.policy_document
        query['SetAsDefault'] = request.set_as_default
        query['RotateStrategy'] = request.rotate_strategy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreatePolicyVersion',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.CreatePolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_version_with_options_async(
        self,
        request: ram_20150501_models.CreatePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreatePolicyVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyName'] = request.policy_name
        query['PolicyDocument'] = request.policy_document
        query['SetAsDefault'] = request.set_as_default
        query['RotateStrategy'] = request.rotate_strategy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreatePolicyVersion',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.CreatePolicyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy_version(
        self,
        request: ram_20150501_models.CreatePolicyVersionRequest,
    ) -> ram_20150501_models.CreatePolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_policy_version_with_options(request, runtime)

    async def create_policy_version_async(
        self,
        request: ram_20150501_models.CreatePolicyVersionRequest,
    ) -> ram_20150501_models.CreatePolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_version_with_options_async(request, runtime)

    def create_role_with_options(
        self,
        request: ram_20150501_models.CreateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreateRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RoleName'] = request.role_name
        query['Description'] = request.description
        query['AssumeRolePolicyDocument'] = request.assume_role_policy_document
        query['MaxSessionDuration'] = request.max_session_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRole',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.CreateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_role_with_options_async(
        self,
        request: ram_20150501_models.CreateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreateRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RoleName'] = request.role_name
        query['Description'] = request.description
        query['AssumeRolePolicyDocument'] = request.assume_role_policy_document
        query['MaxSessionDuration'] = request.max_session_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRole',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.CreateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_role(
        self,
        request: ram_20150501_models.CreateRoleRequest,
    ) -> ram_20150501_models.CreateRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_role_with_options(request, runtime)

    async def create_role_async(
        self,
        request: ram_20150501_models.CreateRoleRequest,
    ) -> ram_20150501_models.CreateRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_role_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: ram_20150501_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        query['DisplayName'] = request.display_name
        query['MobilePhone'] = request.mobile_phone
        query['Email'] = request.email
        query['Comments'] = request.comments
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: ram_20150501_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        query['DisplayName'] = request.display_name
        query['MobilePhone'] = request.mobile_phone
        query['Email'] = request.email
        query['Comments'] = request.comments
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user(
        self,
        request: ram_20150501_models.CreateUserRequest,
    ) -> ram_20150501_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: ram_20150501_models.CreateUserRequest,
    ) -> ram_20150501_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def create_virtual_mfadevice_with_options(
        self,
        request: ram_20150501_models.CreateVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreateVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['VirtualMFADeviceName'] = request.virtual_mfadevice_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateVirtualMFADevice',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.CreateVirtualMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_virtual_mfadevice_with_options_async(
        self,
        request: ram_20150501_models.CreateVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreateVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['VirtualMFADeviceName'] = request.virtual_mfadevice_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateVirtualMFADevice',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.CreateVirtualMFADeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_virtual_mfadevice(
        self,
        request: ram_20150501_models.CreateVirtualMFADeviceRequest,
    ) -> ram_20150501_models.CreateVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_mfadevice_with_options(request, runtime)

    async def create_virtual_mfadevice_async(
        self,
        request: ram_20150501_models.CreateVirtualMFADeviceRequest,
    ) -> ram_20150501_models.CreateVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_virtual_mfadevice_with_options_async(request, runtime)

    def delete_access_key_with_options(
        self,
        request: ram_20150501_models.DeleteAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeleteAccessKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        query['UserAccessKeyId'] = request.user_access_key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAccessKey',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DeleteAccessKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_key_with_options_async(
        self,
        request: ram_20150501_models.DeleteAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeleteAccessKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        query['UserAccessKeyId'] = request.user_access_key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAccessKey',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DeleteAccessKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_key(
        self,
        request: ram_20150501_models.DeleteAccessKeyRequest,
    ) -> ram_20150501_models.DeleteAccessKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_access_key_with_options(request, runtime)

    async def delete_access_key_async(
        self,
        request: ram_20150501_models.DeleteAccessKeyRequest,
    ) -> ram_20150501_models.DeleteAccessKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_access_key_with_options_async(request, runtime)

    def delete_group_with_options(
        self,
        request: ram_20150501_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeleteGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DeleteGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        request: ram_20150501_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeleteGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DeleteGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group(
        self,
        request: ram_20150501_models.DeleteGroupRequest,
    ) -> ram_20150501_models.DeleteGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    async def delete_group_async(
        self,
        request: ram_20150501_models.DeleteGroupRequest,
    ) -> ram_20150501_models.DeleteGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_group_with_options_async(request, runtime)

    def delete_login_profile_with_options(
        self,
        request: ram_20150501_models.DeleteLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeleteLoginProfileResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteLoginProfile',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DeleteLoginProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_login_profile_with_options_async(
        self,
        request: ram_20150501_models.DeleteLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeleteLoginProfileResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteLoginProfile',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DeleteLoginProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_login_profile(
        self,
        request: ram_20150501_models.DeleteLoginProfileRequest,
    ) -> ram_20150501_models.DeleteLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_login_profile_with_options(request, runtime)

    async def delete_login_profile_async(
        self,
        request: ram_20150501_models.DeleteLoginProfileRequest,
    ) -> ram_20150501_models.DeleteLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_login_profile_with_options_async(request, runtime)

    def delete_policy_with_options(
        self,
        request: ram_20150501_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeletePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeletePolicy',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DeletePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_with_options_async(
        self,
        request: ram_20150501_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeletePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeletePolicy',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DeletePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy(
        self,
        request: ram_20150501_models.DeletePolicyRequest,
    ) -> ram_20150501_models.DeletePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_with_options(request, runtime)

    async def delete_policy_async(
        self,
        request: ram_20150501_models.DeletePolicyRequest,
    ) -> ram_20150501_models.DeletePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_with_options_async(request, runtime)

    def delete_policy_version_with_options(
        self,
        request: ram_20150501_models.DeletePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeletePolicyVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyName'] = request.policy_name
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeletePolicyVersion',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DeletePolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_version_with_options_async(
        self,
        request: ram_20150501_models.DeletePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeletePolicyVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyName'] = request.policy_name
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeletePolicyVersion',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DeletePolicyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy_version(
        self,
        request: ram_20150501_models.DeletePolicyVersionRequest,
    ) -> ram_20150501_models.DeletePolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_version_with_options(request, runtime)

    async def delete_policy_version_async(
        self,
        request: ram_20150501_models.DeletePolicyVersionRequest,
    ) -> ram_20150501_models.DeletePolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_version_with_options_async(request, runtime)

    def delete_role_with_options(
        self,
        request: ram_20150501_models.DeleteRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeleteRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteRole',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DeleteRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_role_with_options_async(
        self,
        request: ram_20150501_models.DeleteRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeleteRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteRole',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DeleteRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_role(
        self,
        request: ram_20150501_models.DeleteRoleRequest,
    ) -> ram_20150501_models.DeleteRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_role_with_options(request, runtime)

    async def delete_role_async(
        self,
        request: ram_20150501_models.DeleteRoleRequest,
    ) -> ram_20150501_models.DeleteRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_role_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: ram_20150501_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: ram_20150501_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user(
        self,
        request: ram_20150501_models.DeleteUserRequest,
    ) -> ram_20150501_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: ram_20150501_models.DeleteUserRequest,
    ) -> ram_20150501_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def delete_virtual_mfadevice_with_options(
        self,
        request: ram_20150501_models.DeleteVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeleteVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteVirtualMFADevice',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DeleteVirtualMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_virtual_mfadevice_with_options_async(
        self,
        request: ram_20150501_models.DeleteVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeleteVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteVirtualMFADevice',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DeleteVirtualMFADeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_virtual_mfadevice(
        self,
        request: ram_20150501_models.DeleteVirtualMFADeviceRequest,
    ) -> ram_20150501_models.DeleteVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_mfadevice_with_options(request, runtime)

    async def delete_virtual_mfadevice_async(
        self,
        request: ram_20150501_models.DeleteVirtualMFADeviceRequest,
    ) -> ram_20150501_models.DeleteVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_virtual_mfadevice_with_options_async(request, runtime)

    def detach_policy_from_group_with_options(
        self,
        request: ram_20150501_models.DetachPolicyFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DetachPolicyFromGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['PolicyName'] = request.policy_name
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetachPolicyFromGroup',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DetachPolicyFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_policy_from_group_with_options_async(
        self,
        request: ram_20150501_models.DetachPolicyFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DetachPolicyFromGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['PolicyName'] = request.policy_name
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetachPolicyFromGroup',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DetachPolicyFromGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_policy_from_group(
        self,
        request: ram_20150501_models.DetachPolicyFromGroupRequest,
    ) -> ram_20150501_models.DetachPolicyFromGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_policy_from_group_with_options(request, runtime)

    async def detach_policy_from_group_async(
        self,
        request: ram_20150501_models.DetachPolicyFromGroupRequest,
    ) -> ram_20150501_models.DetachPolicyFromGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_policy_from_group_with_options_async(request, runtime)

    def detach_policy_from_role_with_options(
        self,
        request: ram_20150501_models.DetachPolicyFromRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DetachPolicyFromRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['PolicyName'] = request.policy_name
        query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetachPolicyFromRole',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DetachPolicyFromRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_policy_from_role_with_options_async(
        self,
        request: ram_20150501_models.DetachPolicyFromRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DetachPolicyFromRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['PolicyName'] = request.policy_name
        query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetachPolicyFromRole',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DetachPolicyFromRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_policy_from_role(
        self,
        request: ram_20150501_models.DetachPolicyFromRoleRequest,
    ) -> ram_20150501_models.DetachPolicyFromRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_policy_from_role_with_options(request, runtime)

    async def detach_policy_from_role_async(
        self,
        request: ram_20150501_models.DetachPolicyFromRoleRequest,
    ) -> ram_20150501_models.DetachPolicyFromRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_policy_from_role_with_options_async(request, runtime)

    def detach_policy_from_user_with_options(
        self,
        request: ram_20150501_models.DetachPolicyFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DetachPolicyFromUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['PolicyName'] = request.policy_name
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetachPolicyFromUser',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DetachPolicyFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_policy_from_user_with_options_async(
        self,
        request: ram_20150501_models.DetachPolicyFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DetachPolicyFromUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['PolicyName'] = request.policy_name
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetachPolicyFromUser',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.DetachPolicyFromUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_policy_from_user(
        self,
        request: ram_20150501_models.DetachPolicyFromUserRequest,
    ) -> ram_20150501_models.DetachPolicyFromUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_policy_from_user_with_options(request, runtime)

    async def detach_policy_from_user_async(
        self,
        request: ram_20150501_models.DetachPolicyFromUserRequest,
    ) -> ram_20150501_models.DetachPolicyFromUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_policy_from_user_with_options_async(request, runtime)

    def get_access_key_last_used_with_options(
        self,
        request: ram_20150501_models.GetAccessKeyLastUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetAccessKeyLastUsedResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        query['UserAccessKeyId'] = request.user_access_key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsed',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetAccessKeyLastUsedResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_key_last_used_with_options_async(
        self,
        request: ram_20150501_models.GetAccessKeyLastUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetAccessKeyLastUsedResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        query['UserAccessKeyId'] = request.user_access_key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsed',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetAccessKeyLastUsedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_key_last_used(
        self,
        request: ram_20150501_models.GetAccessKeyLastUsedRequest,
    ) -> ram_20150501_models.GetAccessKeyLastUsedResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_access_key_last_used_with_options(request, runtime)

    async def get_access_key_last_used_async(
        self,
        request: ram_20150501_models.GetAccessKeyLastUsedRequest,
    ) -> ram_20150501_models.GetAccessKeyLastUsedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_access_key_last_used_with_options_async(request, runtime)

    def get_account_alias_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetAccountAliasResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAccountAlias',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetAccountAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_alias_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetAccountAliasResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAccountAlias',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetAccountAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_alias(self) -> ram_20150501_models.GetAccountAliasResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_account_alias_with_options(runtime)

    async def get_account_alias_async(self) -> ram_20150501_models.GetAccountAliasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_account_alias_with_options_async(runtime)

    def get_group_with_options(
        self,
        request: ram_20150501_models.GetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_group_with_options_async(
        self,
        request: ram_20150501_models.GetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_group(
        self,
        request: ram_20150501_models.GetGroupRequest,
    ) -> ram_20150501_models.GetGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_group_with_options(request, runtime)

    async def get_group_async(
        self,
        request: ram_20150501_models.GetGroupRequest,
    ) -> ram_20150501_models.GetGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_group_with_options_async(request, runtime)

    def get_login_profile_with_options(
        self,
        request: ram_20150501_models.GetLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetLoginProfileResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetLoginProfile',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetLoginProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_login_profile_with_options_async(
        self,
        request: ram_20150501_models.GetLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetLoginProfileResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetLoginProfile',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetLoginProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_login_profile(
        self,
        request: ram_20150501_models.GetLoginProfileRequest,
    ) -> ram_20150501_models.GetLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_login_profile_with_options(request, runtime)

    async def get_login_profile_async(
        self,
        request: ram_20150501_models.GetLoginProfileRequest,
    ) -> ram_20150501_models.GetLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_login_profile_with_options_async(request, runtime)

    def get_password_policy_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetPasswordPolicyResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetPasswordPolicy',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetPasswordPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_password_policy_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetPasswordPolicyResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetPasswordPolicy',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetPasswordPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_password_policy(self) -> ram_20150501_models.GetPasswordPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_password_policy_with_options(runtime)

    async def get_password_policy_async(self) -> ram_20150501_models.GetPasswordPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_password_policy_with_options_async(runtime)

    def get_policy_with_options(
        self,
        request: ram_20150501_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetPolicy',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_with_options_async(
        self,
        request: ram_20150501_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetPolicy',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy(
        self,
        request: ram_20150501_models.GetPolicyRequest,
    ) -> ram_20150501_models.GetPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_policy_with_options(request, runtime)

    async def get_policy_async(
        self,
        request: ram_20150501_models.GetPolicyRequest,
    ) -> ram_20150501_models.GetPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_with_options_async(request, runtime)

    def get_policy_version_with_options(
        self,
        request: ram_20150501_models.GetPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetPolicyVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['PolicyName'] = request.policy_name
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetPolicyVersion',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetPolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_version_with_options_async(
        self,
        request: ram_20150501_models.GetPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetPolicyVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['PolicyName'] = request.policy_name
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetPolicyVersion',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetPolicyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy_version(
        self,
        request: ram_20150501_models.GetPolicyVersionRequest,
    ) -> ram_20150501_models.GetPolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_policy_version_with_options(request, runtime)

    async def get_policy_version_async(
        self,
        request: ram_20150501_models.GetPolicyVersionRequest,
    ) -> ram_20150501_models.GetPolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_version_with_options_async(request, runtime)

    def get_role_with_options(
        self,
        request: ram_20150501_models.GetRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetRole',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_role_with_options_async(
        self,
        request: ram_20150501_models.GetRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetRole',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_role(
        self,
        request: ram_20150501_models.GetRoleRequest,
    ) -> ram_20150501_models.GetRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_role_with_options(request, runtime)

    async def get_role_async(
        self,
        request: ram_20150501_models.GetRoleRequest,
    ) -> ram_20150501_models.GetRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_role_with_options_async(request, runtime)

    def get_security_preference_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetSecurityPreferenceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetSecurityPreference',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetSecurityPreferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_security_preference_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetSecurityPreferenceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetSecurityPreference',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetSecurityPreferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_security_preference(self) -> ram_20150501_models.GetSecurityPreferenceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_security_preference_with_options(runtime)

    async def get_security_preference_async(self) -> ram_20150501_models.GetSecurityPreferenceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_security_preference_with_options_async(runtime)

    def get_user_with_options(
        self,
        request: ram_20150501_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: ram_20150501_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: ram_20150501_models.GetUserRequest,
    ) -> ram_20150501_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: ram_20150501_models.GetUserRequest,
    ) -> ram_20150501_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def get_user_mfainfo_with_options(
        self,
        request: ram_20150501_models.GetUserMFAInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetUserMFAInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetUserMFAInfo',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetUserMFAInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_mfainfo_with_options_async(
        self,
        request: ram_20150501_models.GetUserMFAInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetUserMFAInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetUserMFAInfo',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.GetUserMFAInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_mfainfo(
        self,
        request: ram_20150501_models.GetUserMFAInfoRequest,
    ) -> ram_20150501_models.GetUserMFAInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_mfainfo_with_options(request, runtime)

    async def get_user_mfainfo_async(
        self,
        request: ram_20150501_models.GetUserMFAInfoRequest,
    ) -> ram_20150501_models.GetUserMFAInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_mfainfo_with_options_async(request, runtime)

    def list_access_keys_with_options(
        self,
        request: ram_20150501_models.ListAccessKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListAccessKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAccessKeys',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListAccessKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_access_keys_with_options_async(
        self,
        request: ram_20150501_models.ListAccessKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListAccessKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAccessKeys',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListAccessKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_access_keys(
        self,
        request: ram_20150501_models.ListAccessKeysRequest,
    ) -> ram_20150501_models.ListAccessKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_access_keys_with_options(request, runtime)

    async def list_access_keys_async(
        self,
        request: ram_20150501_models.ListAccessKeysRequest,
    ) -> ram_20150501_models.ListAccessKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_access_keys_with_options_async(request, runtime)

    def list_entities_for_policy_with_options(
        self,
        request: ram_20150501_models.ListEntitiesForPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListEntitiesForPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListEntitiesForPolicy',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListEntitiesForPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_entities_for_policy_with_options_async(
        self,
        request: ram_20150501_models.ListEntitiesForPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListEntitiesForPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListEntitiesForPolicy',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListEntitiesForPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_entities_for_policy(
        self,
        request: ram_20150501_models.ListEntitiesForPolicyRequest,
    ) -> ram_20150501_models.ListEntitiesForPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_entities_for_policy_with_options(request, runtime)

    async def list_entities_for_policy_async(
        self,
        request: ram_20150501_models.ListEntitiesForPolicyRequest,
    ) -> ram_20150501_models.ListEntitiesForPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_entities_for_policy_with_options_async(request, runtime)

    def list_groups_with_options(
        self,
        request: ram_20150501_models.ListGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Marker'] = request.marker
        query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_with_options_async(
        self,
        request: ram_20150501_models.ListGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Marker'] = request.marker
        query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups(
        self,
        request: ram_20150501_models.ListGroupsRequest,
    ) -> ram_20150501_models.ListGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_groups_with_options(request, runtime)

    async def list_groups_async(
        self,
        request: ram_20150501_models.ListGroupsRequest,
    ) -> ram_20150501_models.ListGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_groups_with_options_async(request, runtime)

    def list_groups_for_user_with_options(
        self,
        request: ram_20150501_models.ListGroupsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListGroupsForUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListGroupsForUser',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListGroupsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_for_user_with_options_async(
        self,
        request: ram_20150501_models.ListGroupsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListGroupsForUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListGroupsForUser',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListGroupsForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups_for_user(
        self,
        request: ram_20150501_models.ListGroupsForUserRequest,
    ) -> ram_20150501_models.ListGroupsForUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_groups_for_user_with_options(request, runtime)

    async def list_groups_for_user_async(
        self,
        request: ram_20150501_models.ListGroupsForUserRequest,
    ) -> ram_20150501_models.ListGroupsForUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_groups_for_user_with_options_async(request, runtime)

    def list_policies_with_options(
        self,
        request: ram_20150501_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['Marker'] = request.marker
        query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListPolicies',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_with_options_async(
        self,
        request: ram_20150501_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['Marker'] = request.marker
        query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListPolicies',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies(
        self,
        request: ram_20150501_models.ListPoliciesRequest,
    ) -> ram_20150501_models.ListPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_policies_with_options(request, runtime)

    async def list_policies_async(
        self,
        request: ram_20150501_models.ListPoliciesRequest,
    ) -> ram_20150501_models.ListPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_policies_with_options_async(request, runtime)

    def list_policies_for_group_with_options(
        self,
        request: ram_20150501_models.ListPoliciesForGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListPoliciesForGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListPoliciesForGroup',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListPoliciesForGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_for_group_with_options_async(
        self,
        request: ram_20150501_models.ListPoliciesForGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListPoliciesForGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListPoliciesForGroup',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListPoliciesForGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies_for_group(
        self,
        request: ram_20150501_models.ListPoliciesForGroupRequest,
    ) -> ram_20150501_models.ListPoliciesForGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_policies_for_group_with_options(request, runtime)

    async def list_policies_for_group_async(
        self,
        request: ram_20150501_models.ListPoliciesForGroupRequest,
    ) -> ram_20150501_models.ListPoliciesForGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_policies_for_group_with_options_async(request, runtime)

    def list_policies_for_role_with_options(
        self,
        request: ram_20150501_models.ListPoliciesForRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListPoliciesForRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListPoliciesForRole',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListPoliciesForRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_for_role_with_options_async(
        self,
        request: ram_20150501_models.ListPoliciesForRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListPoliciesForRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListPoliciesForRole',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListPoliciesForRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies_for_role(
        self,
        request: ram_20150501_models.ListPoliciesForRoleRequest,
    ) -> ram_20150501_models.ListPoliciesForRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_policies_for_role_with_options(request, runtime)

    async def list_policies_for_role_async(
        self,
        request: ram_20150501_models.ListPoliciesForRoleRequest,
    ) -> ram_20150501_models.ListPoliciesForRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_policies_for_role_with_options_async(request, runtime)

    def list_policies_for_user_with_options(
        self,
        request: ram_20150501_models.ListPoliciesForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListPoliciesForUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListPoliciesForUser',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListPoliciesForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_for_user_with_options_async(
        self,
        request: ram_20150501_models.ListPoliciesForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListPoliciesForUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListPoliciesForUser',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListPoliciesForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies_for_user(
        self,
        request: ram_20150501_models.ListPoliciesForUserRequest,
    ) -> ram_20150501_models.ListPoliciesForUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_policies_for_user_with_options(request, runtime)

    async def list_policies_for_user_async(
        self,
        request: ram_20150501_models.ListPoliciesForUserRequest,
    ) -> ram_20150501_models.ListPoliciesForUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_policies_for_user_with_options_async(request, runtime)

    def list_policy_versions_with_options(
        self,
        request: ram_20150501_models.ListPolicyVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListPolicyVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListPolicyVersions',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListPolicyVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policy_versions_with_options_async(
        self,
        request: ram_20150501_models.ListPolicyVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListPolicyVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyType'] = request.policy_type
        query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListPolicyVersions',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListPolicyVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policy_versions(
        self,
        request: ram_20150501_models.ListPolicyVersionsRequest,
    ) -> ram_20150501_models.ListPolicyVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_policy_versions_with_options(request, runtime)

    async def list_policy_versions_async(
        self,
        request: ram_20150501_models.ListPolicyVersionsRequest,
    ) -> ram_20150501_models.ListPolicyVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_policy_versions_with_options_async(request, runtime)

    def list_roles_with_options(
        self,
        request: ram_20150501_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Marker'] = request.marker
        query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: ram_20150501_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Marker'] = request.marker
        query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_roles(
        self,
        request: ram_20150501_models.ListRolesRequest,
    ) -> ram_20150501_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    async def list_roles_async(
        self,
        request: ram_20150501_models.ListRolesRequest,
    ) -> ram_20150501_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_roles_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: ram_20150501_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Marker'] = request.marker
        query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: ram_20150501_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Marker'] = request.marker
        query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: ram_20150501_models.ListUsersRequest,
    ) -> ram_20150501_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: ram_20150501_models.ListUsersRequest,
    ) -> ram_20150501_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def list_users_for_group_with_options(
        self,
        request: ram_20150501_models.ListUsersForGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListUsersForGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupName'] = request.group_name
        query['Marker'] = request.marker
        query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListUsersForGroup',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListUsersForGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_for_group_with_options_async(
        self,
        request: ram_20150501_models.ListUsersForGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListUsersForGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupName'] = request.group_name
        query['Marker'] = request.marker
        query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListUsersForGroup',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListUsersForGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users_for_group(
        self,
        request: ram_20150501_models.ListUsersForGroupRequest,
    ) -> ram_20150501_models.ListUsersForGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_for_group_with_options(request, runtime)

    async def list_users_for_group_async(
        self,
        request: ram_20150501_models.ListUsersForGroupRequest,
    ) -> ram_20150501_models.ListUsersForGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_for_group_with_options_async(request, runtime)

    def list_virtual_mfadevices_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListVirtualMFADevicesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListVirtualMFADevices',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListVirtualMFADevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_virtual_mfadevices_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListVirtualMFADevicesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListVirtualMFADevices',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.ListVirtualMFADevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_virtual_mfadevices(self) -> ram_20150501_models.ListVirtualMFADevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_virtual_mfadevices_with_options(runtime)

    async def list_virtual_mfadevices_async(self) -> ram_20150501_models.ListVirtualMFADevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_virtual_mfadevices_with_options_async(runtime)

    def remove_user_from_group_with_options(
        self,
        request: ram_20150501_models.RemoveUserFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.RemoveUserFromGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveUserFromGroup',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.RemoveUserFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_user_from_group_with_options_async(
        self,
        request: ram_20150501_models.RemoveUserFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.RemoveUserFromGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveUserFromGroup',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.RemoveUserFromGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_user_from_group(
        self,
        request: ram_20150501_models.RemoveUserFromGroupRequest,
    ) -> ram_20150501_models.RemoveUserFromGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_user_from_group_with_options(request, runtime)

    async def remove_user_from_group_async(
        self,
        request: ram_20150501_models.RemoveUserFromGroupRequest,
    ) -> ram_20150501_models.RemoveUserFromGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_user_from_group_with_options_async(request, runtime)

    def set_account_alias_with_options(
        self,
        request: ram_20150501_models.SetAccountAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.SetAccountAliasResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountAlias'] = request.account_alias
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetAccountAlias',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.SetAccountAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_account_alias_with_options_async(
        self,
        request: ram_20150501_models.SetAccountAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.SetAccountAliasResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountAlias'] = request.account_alias
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetAccountAlias',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.SetAccountAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_account_alias(
        self,
        request: ram_20150501_models.SetAccountAliasRequest,
    ) -> ram_20150501_models.SetAccountAliasResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_account_alias_with_options(request, runtime)

    async def set_account_alias_async(
        self,
        request: ram_20150501_models.SetAccountAliasRequest,
    ) -> ram_20150501_models.SetAccountAliasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_account_alias_with_options_async(request, runtime)

    def set_default_policy_version_with_options(
        self,
        request: ram_20150501_models.SetDefaultPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.SetDefaultPolicyVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyName'] = request.policy_name
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDefaultPolicyVersion',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.SetDefaultPolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_default_policy_version_with_options_async(
        self,
        request: ram_20150501_models.SetDefaultPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.SetDefaultPolicyVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PolicyName'] = request.policy_name
        query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDefaultPolicyVersion',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.SetDefaultPolicyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_default_policy_version(
        self,
        request: ram_20150501_models.SetDefaultPolicyVersionRequest,
    ) -> ram_20150501_models.SetDefaultPolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_default_policy_version_with_options(request, runtime)

    async def set_default_policy_version_async(
        self,
        request: ram_20150501_models.SetDefaultPolicyVersionRequest,
    ) -> ram_20150501_models.SetDefaultPolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_default_policy_version_with_options_async(request, runtime)

    def set_password_policy_with_options(
        self,
        request: ram_20150501_models.SetPasswordPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.SetPasswordPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MinimumPasswordLength'] = request.minimum_password_length
        query['RequireLowercaseCharacters'] = request.require_lowercase_characters
        query['RequireUppercaseCharacters'] = request.require_uppercase_characters
        query['RequireNumbers'] = request.require_numbers
        query['RequireSymbols'] = request.require_symbols
        query['HardExpiry'] = request.hard_expiry
        query['MaxPasswordAge'] = request.max_password_age
        query['PasswordReusePrevention'] = request.password_reuse_prevention
        query['MaxLoginAttemps'] = request.max_login_attemps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetPasswordPolicy',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.SetPasswordPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_password_policy_with_options_async(
        self,
        request: ram_20150501_models.SetPasswordPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.SetPasswordPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MinimumPasswordLength'] = request.minimum_password_length
        query['RequireLowercaseCharacters'] = request.require_lowercase_characters
        query['RequireUppercaseCharacters'] = request.require_uppercase_characters
        query['RequireNumbers'] = request.require_numbers
        query['RequireSymbols'] = request.require_symbols
        query['HardExpiry'] = request.hard_expiry
        query['MaxPasswordAge'] = request.max_password_age
        query['PasswordReusePrevention'] = request.password_reuse_prevention
        query['MaxLoginAttemps'] = request.max_login_attemps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetPasswordPolicy',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.SetPasswordPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_password_policy(
        self,
        request: ram_20150501_models.SetPasswordPolicyRequest,
    ) -> ram_20150501_models.SetPasswordPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_password_policy_with_options(request, runtime)

    async def set_password_policy_async(
        self,
        request: ram_20150501_models.SetPasswordPolicyRequest,
    ) -> ram_20150501_models.SetPasswordPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_password_policy_with_options_async(request, runtime)

    def set_security_preference_with_options(
        self,
        request: ram_20150501_models.SetSecurityPreferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.SetSecurityPreferenceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EnableSaveMFATicket'] = request.enable_save_mfaticket
        query['AllowUserToChangePassword'] = request.allow_user_to_change_password
        query['AllowUserToManageAccessKeys'] = request.allow_user_to_manage_access_keys
        query['AllowUserToManagePublicKeys'] = request.allow_user_to_manage_public_keys
        query['AllowUserToManageMFADevices'] = request.allow_user_to_manage_mfadevices
        query['LoginSessionDuration'] = request.login_session_duration
        query['LoginNetworkMasks'] = request.login_network_masks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetSecurityPreference',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.SetSecurityPreferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_security_preference_with_options_async(
        self,
        request: ram_20150501_models.SetSecurityPreferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.SetSecurityPreferenceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EnableSaveMFATicket'] = request.enable_save_mfaticket
        query['AllowUserToChangePassword'] = request.allow_user_to_change_password
        query['AllowUserToManageAccessKeys'] = request.allow_user_to_manage_access_keys
        query['AllowUserToManagePublicKeys'] = request.allow_user_to_manage_public_keys
        query['AllowUserToManageMFADevices'] = request.allow_user_to_manage_mfadevices
        query['LoginSessionDuration'] = request.login_session_duration
        query['LoginNetworkMasks'] = request.login_network_masks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetSecurityPreference',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.SetSecurityPreferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_security_preference(
        self,
        request: ram_20150501_models.SetSecurityPreferenceRequest,
    ) -> ram_20150501_models.SetSecurityPreferenceResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_security_preference_with_options(request, runtime)

    async def set_security_preference_async(
        self,
        request: ram_20150501_models.SetSecurityPreferenceRequest,
    ) -> ram_20150501_models.SetSecurityPreferenceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_security_preference_with_options_async(request, runtime)

    def unbind_mfadevice_with_options(
        self,
        request: ram_20150501_models.UnbindMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.UnbindMFADeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnbindMFADevice',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.UnbindMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_mfadevice_with_options_async(
        self,
        request: ram_20150501_models.UnbindMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.UnbindMFADeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnbindMFADevice',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.UnbindMFADeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_mfadevice(
        self,
        request: ram_20150501_models.UnbindMFADeviceRequest,
    ) -> ram_20150501_models.UnbindMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_mfadevice_with_options(request, runtime)

    async def unbind_mfadevice_async(
        self,
        request: ram_20150501_models.UnbindMFADeviceRequest,
    ) -> ram_20150501_models.UnbindMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_mfadevice_with_options_async(request, runtime)

    def update_access_key_with_options(
        self,
        request: ram_20150501_models.UpdateAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.UpdateAccessKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        query['UserAccessKeyId'] = request.user_access_key_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAccessKey',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.UpdateAccessKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_access_key_with_options_async(
        self,
        request: ram_20150501_models.UpdateAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.UpdateAccessKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        query['UserAccessKeyId'] = request.user_access_key_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAccessKey',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.UpdateAccessKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_access_key(
        self,
        request: ram_20150501_models.UpdateAccessKeyRequest,
    ) -> ram_20150501_models.UpdateAccessKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_access_key_with_options(request, runtime)

    async def update_access_key_async(
        self,
        request: ram_20150501_models.UpdateAccessKeyRequest,
    ) -> ram_20150501_models.UpdateAccessKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_access_key_with_options_async(request, runtime)

    def update_group_with_options(
        self,
        request: ram_20150501_models.UpdateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.UpdateGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupName'] = request.group_name
        query['NewGroupName'] = request.new_group_name
        query['NewComments'] = request.new_comments
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.UpdateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_group_with_options_async(
        self,
        request: ram_20150501_models.UpdateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.UpdateGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupName'] = request.group_name
        query['NewGroupName'] = request.new_group_name
        query['NewComments'] = request.new_comments
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.UpdateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_group(
        self,
        request: ram_20150501_models.UpdateGroupRequest,
    ) -> ram_20150501_models.UpdateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_group_with_options(request, runtime)

    async def update_group_async(
        self,
        request: ram_20150501_models.UpdateGroupRequest,
    ) -> ram_20150501_models.UpdateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_group_with_options_async(request, runtime)

    def update_login_profile_with_options(
        self,
        request: ram_20150501_models.UpdateLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.UpdateLoginProfileResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        query['Password'] = request.password
        query['PasswordResetRequired'] = request.password_reset_required
        query['MFABindRequired'] = request.mfabind_required
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateLoginProfile',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.UpdateLoginProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_login_profile_with_options_async(
        self,
        request: ram_20150501_models.UpdateLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.UpdateLoginProfileResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        query['Password'] = request.password
        query['PasswordResetRequired'] = request.password_reset_required
        query['MFABindRequired'] = request.mfabind_required
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateLoginProfile',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.UpdateLoginProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_login_profile(
        self,
        request: ram_20150501_models.UpdateLoginProfileRequest,
    ) -> ram_20150501_models.UpdateLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_login_profile_with_options(request, runtime)

    async def update_login_profile_async(
        self,
        request: ram_20150501_models.UpdateLoginProfileRequest,
    ) -> ram_20150501_models.UpdateLoginProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_login_profile_with_options_async(request, runtime)

    def update_role_with_options(
        self,
        request: ram_20150501_models.UpdateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.UpdateRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RoleName'] = request.role_name
        query['NewAssumeRolePolicyDocument'] = request.new_assume_role_policy_document
        query['NewMaxSessionDuration'] = request.new_max_session_duration
        query['NewDescription'] = request.new_description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateRole',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.UpdateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_role_with_options_async(
        self,
        request: ram_20150501_models.UpdateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.UpdateRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RoleName'] = request.role_name
        query['NewAssumeRolePolicyDocument'] = request.new_assume_role_policy_document
        query['NewMaxSessionDuration'] = request.new_max_session_duration
        query['NewDescription'] = request.new_description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateRole',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.UpdateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_role(
        self,
        request: ram_20150501_models.UpdateRoleRequest,
    ) -> ram_20150501_models.UpdateRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_role_with_options(request, runtime)

    async def update_role_async(
        self,
        request: ram_20150501_models.UpdateRoleRequest,
    ) -> ram_20150501_models.UpdateRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_role_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: ram_20150501_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        query['NewUserName'] = request.new_user_name
        query['NewDisplayName'] = request.new_display_name
        query['NewMobilePhone'] = request.new_mobile_phone
        query['NewEmail'] = request.new_email
        query['NewComments'] = request.new_comments
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: ram_20150501_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['UserName'] = request.user_name
        query['NewUserName'] = request.new_user_name
        query['NewDisplayName'] = request.new_display_name
        query['NewMobilePhone'] = request.new_mobile_phone
        query['NewEmail'] = request.new_email
        query['NewComments'] = request.new_comments
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2015-05-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ram_20150501_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        request: ram_20150501_models.UpdateUserRequest,
    ) -> ram_20150501_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: ram_20150501_models.UpdateUserRequest,
    ) -> ram_20150501_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)
