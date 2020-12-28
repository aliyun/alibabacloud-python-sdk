# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ram20150501 import models as ram_20150501_models
from alibabacloud_tea_util import models as util_models


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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.AddUserToGroupResponse().from_map(
            self.do_rpcrequest('AddUserToGroup', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_user_to_group_with_options_async(
        self,
        request: ram_20150501_models.AddUserToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.AddUserToGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.AddUserToGroupResponse().from_map(
            await self.do_rpcrequest_async('AddUserToGroup', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.AttachPolicyToGroupResponse().from_map(
            self.do_rpcrequest('AttachPolicyToGroup', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_policy_to_group_with_options_async(
        self,
        request: ram_20150501_models.AttachPolicyToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.AttachPolicyToGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.AttachPolicyToGroupResponse().from_map(
            await self.do_rpcrequest_async('AttachPolicyToGroup', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.AttachPolicyToRoleResponse().from_map(
            self.do_rpcrequest('AttachPolicyToRole', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_policy_to_role_with_options_async(
        self,
        request: ram_20150501_models.AttachPolicyToRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.AttachPolicyToRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.AttachPolicyToRoleResponse().from_map(
            await self.do_rpcrequest_async('AttachPolicyToRole', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.AttachPolicyToUserResponse().from_map(
            self.do_rpcrequest('AttachPolicyToUser', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_policy_to_user_with_options_async(
        self,
        request: ram_20150501_models.AttachPolicyToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.AttachPolicyToUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.AttachPolicyToUserResponse().from_map(
            await self.do_rpcrequest_async('AttachPolicyToUser', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.BindMFADeviceResponse().from_map(
            self.do_rpcrequest('BindMFADevice', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_mfadevice_with_options_async(
        self,
        request: ram_20150501_models.BindMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.BindMFADeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.BindMFADeviceResponse().from_map(
            await self.do_rpcrequest_async('BindMFADevice', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ChangePasswordResponse().from_map(
            self.do_rpcrequest('ChangePassword', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def change_password_with_options_async(
        self,
        request: ram_20150501_models.ChangePasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ChangePasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ChangePasswordResponse().from_map(
            await self.do_rpcrequest_async('ChangePassword', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return ram_20150501_models.ClearAccountAliasResponse().from_map(
            self.do_rpcrequest('ClearAccountAlias', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clear_account_alias_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ClearAccountAliasResponse:
        req = open_api_models.OpenApiRequest()
        return ram_20150501_models.ClearAccountAliasResponse().from_map(
            await self.do_rpcrequest_async('ClearAccountAlias', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.CreateAccessKeyResponse().from_map(
            self.do_rpcrequest('CreateAccessKey', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_access_key_with_options_async(
        self,
        request: ram_20150501_models.CreateAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreateAccessKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.CreateAccessKeyResponse().from_map(
            await self.do_rpcrequest_async('CreateAccessKey', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.CreateGroupResponse().from_map(
            self.do_rpcrequest('CreateGroup', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_group_with_options_async(
        self,
        request: ram_20150501_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.CreateGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateGroup', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.CreateLoginProfileResponse().from_map(
            self.do_rpcrequest('CreateLoginProfile', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_login_profile_with_options_async(
        self,
        request: ram_20150501_models.CreateLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreateLoginProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.CreateLoginProfileResponse().from_map(
            await self.do_rpcrequest_async('CreateLoginProfile', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.CreatePolicyResponse().from_map(
            self.do_rpcrequest('CreatePolicy', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_policy_with_options_async(
        self,
        request: ram_20150501_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreatePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.CreatePolicyResponse().from_map(
            await self.do_rpcrequest_async('CreatePolicy', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.CreatePolicyVersionResponse().from_map(
            self.do_rpcrequest('CreatePolicyVersion', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_policy_version_with_options_async(
        self,
        request: ram_20150501_models.CreatePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreatePolicyVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.CreatePolicyVersionResponse().from_map(
            await self.do_rpcrequest_async('CreatePolicyVersion', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.CreateRoleResponse().from_map(
            self.do_rpcrequest('CreateRole', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_role_with_options_async(
        self,
        request: ram_20150501_models.CreateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreateRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.CreateRoleResponse().from_map(
            await self.do_rpcrequest_async('CreateRole', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.CreateUserResponse().from_map(
            self.do_rpcrequest('CreateUser', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: ram_20150501_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.CreateUserResponse().from_map(
            await self.do_rpcrequest_async('CreateUser', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.CreateVirtualMFADeviceResponse().from_map(
            self.do_rpcrequest('CreateVirtualMFADevice', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_virtual_mfadevice_with_options_async(
        self,
        request: ram_20150501_models.CreateVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.CreateVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.CreateVirtualMFADeviceResponse().from_map(
            await self.do_rpcrequest_async('CreateVirtualMFADevice', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DeleteAccessKeyResponse().from_map(
            self.do_rpcrequest('DeleteAccessKey', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_access_key_with_options_async(
        self,
        request: ram_20150501_models.DeleteAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeleteAccessKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DeleteAccessKeyResponse().from_map(
            await self.do_rpcrequest_async('DeleteAccessKey', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DeleteGroupResponse().from_map(
            self.do_rpcrequest('DeleteGroup', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        request: ram_20150501_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeleteGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DeleteGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteGroup', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DeleteLoginProfileResponse().from_map(
            self.do_rpcrequest('DeleteLoginProfile', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_login_profile_with_options_async(
        self,
        request: ram_20150501_models.DeleteLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeleteLoginProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DeleteLoginProfileResponse().from_map(
            await self.do_rpcrequest_async('DeleteLoginProfile', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DeletePolicyResponse().from_map(
            self.do_rpcrequest('DeletePolicy', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_policy_with_options_async(
        self,
        request: ram_20150501_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeletePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DeletePolicyResponse().from_map(
            await self.do_rpcrequest_async('DeletePolicy', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DeletePolicyVersionResponse().from_map(
            self.do_rpcrequest('DeletePolicyVersion', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_policy_version_with_options_async(
        self,
        request: ram_20150501_models.DeletePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeletePolicyVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DeletePolicyVersionResponse().from_map(
            await self.do_rpcrequest_async('DeletePolicyVersion', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DeleteRoleResponse().from_map(
            self.do_rpcrequest('DeleteRole', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_role_with_options_async(
        self,
        request: ram_20150501_models.DeleteRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeleteRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DeleteRoleResponse().from_map(
            await self.do_rpcrequest_async('DeleteRole', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DeleteUserResponse().from_map(
            self.do_rpcrequest('DeleteUser', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: ram_20150501_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DeleteUserResponse().from_map(
            await self.do_rpcrequest_async('DeleteUser', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DeleteVirtualMFADeviceResponse().from_map(
            self.do_rpcrequest('DeleteVirtualMFADevice', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_virtual_mfadevice_with_options_async(
        self,
        request: ram_20150501_models.DeleteVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DeleteVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DeleteVirtualMFADeviceResponse().from_map(
            await self.do_rpcrequest_async('DeleteVirtualMFADevice', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DetachPolicyFromGroupResponse().from_map(
            self.do_rpcrequest('DetachPolicyFromGroup', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_policy_from_group_with_options_async(
        self,
        request: ram_20150501_models.DetachPolicyFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DetachPolicyFromGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DetachPolicyFromGroupResponse().from_map(
            await self.do_rpcrequest_async('DetachPolicyFromGroup', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DetachPolicyFromRoleResponse().from_map(
            self.do_rpcrequest('DetachPolicyFromRole', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_policy_from_role_with_options_async(
        self,
        request: ram_20150501_models.DetachPolicyFromRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DetachPolicyFromRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DetachPolicyFromRoleResponse().from_map(
            await self.do_rpcrequest_async('DetachPolicyFromRole', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DetachPolicyFromUserResponse().from_map(
            self.do_rpcrequest('DetachPolicyFromUser', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_policy_from_user_with_options_async(
        self,
        request: ram_20150501_models.DetachPolicyFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.DetachPolicyFromUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.DetachPolicyFromUserResponse().from_map(
            await self.do_rpcrequest_async('DetachPolicyFromUser', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.GetAccessKeyLastUsedResponse().from_map(
            self.do_rpcrequest('GetAccessKeyLastUsed', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_access_key_last_used_with_options_async(
        self,
        request: ram_20150501_models.GetAccessKeyLastUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetAccessKeyLastUsedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.GetAccessKeyLastUsedResponse().from_map(
            await self.do_rpcrequest_async('GetAccessKeyLastUsed', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return ram_20150501_models.GetAccountAliasResponse().from_map(
            self.do_rpcrequest('GetAccountAlias', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_account_alias_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetAccountAliasResponse:
        req = open_api_models.OpenApiRequest()
        return ram_20150501_models.GetAccountAliasResponse().from_map(
            await self.do_rpcrequest_async('GetAccountAlias', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.GetGroupResponse().from_map(
            self.do_rpcrequest('GetGroup', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_group_with_options_async(
        self,
        request: ram_20150501_models.GetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.GetGroupResponse().from_map(
            await self.do_rpcrequest_async('GetGroup', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.GetLoginProfileResponse().from_map(
            self.do_rpcrequest('GetLoginProfile', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_login_profile_with_options_async(
        self,
        request: ram_20150501_models.GetLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetLoginProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.GetLoginProfileResponse().from_map(
            await self.do_rpcrequest_async('GetLoginProfile', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return ram_20150501_models.GetPasswordPolicyResponse().from_map(
            self.do_rpcrequest('GetPasswordPolicy', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_password_policy_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetPasswordPolicyResponse:
        req = open_api_models.OpenApiRequest()
        return ram_20150501_models.GetPasswordPolicyResponse().from_map(
            await self.do_rpcrequest_async('GetPasswordPolicy', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.GetPolicyResponse().from_map(
            self.do_rpcrequest('GetPolicy', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_policy_with_options_async(
        self,
        request: ram_20150501_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.GetPolicyResponse().from_map(
            await self.do_rpcrequest_async('GetPolicy', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.GetPolicyVersionResponse().from_map(
            self.do_rpcrequest('GetPolicyVersion', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_policy_version_with_options_async(
        self,
        request: ram_20150501_models.GetPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetPolicyVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.GetPolicyVersionResponse().from_map(
            await self.do_rpcrequest_async('GetPolicyVersion', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.GetRoleResponse().from_map(
            self.do_rpcrequest('GetRole', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_role_with_options_async(
        self,
        request: ram_20150501_models.GetRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.GetRoleResponse().from_map(
            await self.do_rpcrequest_async('GetRole', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return ram_20150501_models.GetSecurityPreferenceResponse().from_map(
            self.do_rpcrequest('GetSecurityPreference', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_security_preference_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetSecurityPreferenceResponse:
        req = open_api_models.OpenApiRequest()
        return ram_20150501_models.GetSecurityPreferenceResponse().from_map(
            await self.do_rpcrequest_async('GetSecurityPreference', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.GetUserResponse().from_map(
            self.do_rpcrequest('GetUser', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: ram_20150501_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.GetUserResponse().from_map(
            await self.do_rpcrequest_async('GetUser', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.GetUserMFAInfoResponse().from_map(
            self.do_rpcrequest('GetUserMFAInfo', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_mfainfo_with_options_async(
        self,
        request: ram_20150501_models.GetUserMFAInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.GetUserMFAInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.GetUserMFAInfoResponse().from_map(
            await self.do_rpcrequest_async('GetUserMFAInfo', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListAccessKeysResponse().from_map(
            self.do_rpcrequest('ListAccessKeys', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_access_keys_with_options_async(
        self,
        request: ram_20150501_models.ListAccessKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListAccessKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListAccessKeysResponse().from_map(
            await self.do_rpcrequest_async('ListAccessKeys', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListEntitiesForPolicyResponse().from_map(
            self.do_rpcrequest('ListEntitiesForPolicy', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_entities_for_policy_with_options_async(
        self,
        request: ram_20150501_models.ListEntitiesForPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListEntitiesForPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListEntitiesForPolicyResponse().from_map(
            await self.do_rpcrequest_async('ListEntitiesForPolicy', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListGroupsResponse().from_map(
            self.do_rpcrequest('ListGroups', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_groups_with_options_async(
        self,
        request: ram_20150501_models.ListGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListGroupsResponse().from_map(
            await self.do_rpcrequest_async('ListGroups', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListGroupsForUserResponse().from_map(
            self.do_rpcrequest('ListGroupsForUser', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_groups_for_user_with_options_async(
        self,
        request: ram_20150501_models.ListGroupsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListGroupsForUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListGroupsForUserResponse().from_map(
            await self.do_rpcrequest_async('ListGroupsForUser', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListPoliciesResponse().from_map(
            self.do_rpcrequest('ListPolicies', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_policies_with_options_async(
        self,
        request: ram_20150501_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListPoliciesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListPoliciesResponse().from_map(
            await self.do_rpcrequest_async('ListPolicies', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListPoliciesForGroupResponse().from_map(
            self.do_rpcrequest('ListPoliciesForGroup', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_policies_for_group_with_options_async(
        self,
        request: ram_20150501_models.ListPoliciesForGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListPoliciesForGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListPoliciesForGroupResponse().from_map(
            await self.do_rpcrequest_async('ListPoliciesForGroup', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListPoliciesForRoleResponse().from_map(
            self.do_rpcrequest('ListPoliciesForRole', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_policies_for_role_with_options_async(
        self,
        request: ram_20150501_models.ListPoliciesForRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListPoliciesForRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListPoliciesForRoleResponse().from_map(
            await self.do_rpcrequest_async('ListPoliciesForRole', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListPoliciesForUserResponse().from_map(
            self.do_rpcrequest('ListPoliciesForUser', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_policies_for_user_with_options_async(
        self,
        request: ram_20150501_models.ListPoliciesForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListPoliciesForUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListPoliciesForUserResponse().from_map(
            await self.do_rpcrequest_async('ListPoliciesForUser', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListPolicyVersionsResponse().from_map(
            self.do_rpcrequest('ListPolicyVersions', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_policy_versions_with_options_async(
        self,
        request: ram_20150501_models.ListPolicyVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListPolicyVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListPolicyVersionsResponse().from_map(
            await self.do_rpcrequest_async('ListPolicyVersions', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListRolesResponse().from_map(
            self.do_rpcrequest('ListRoles', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: ram_20150501_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListRolesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListRolesResponse().from_map(
            await self.do_rpcrequest_async('ListRoles', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListUsersResponse().from_map(
            self.do_rpcrequest('ListUsers', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: ram_20150501_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListUsersResponse().from_map(
            await self.do_rpcrequest_async('ListUsers', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListUsersForGroupResponse().from_map(
            self.do_rpcrequest('ListUsersForGroup', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_users_for_group_with_options_async(
        self,
        request: ram_20150501_models.ListUsersForGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListUsersForGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.ListUsersForGroupResponse().from_map(
            await self.do_rpcrequest_async('ListUsersForGroup', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return ram_20150501_models.ListVirtualMFADevicesResponse().from_map(
            self.do_rpcrequest('ListVirtualMFADevices', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_virtual_mfadevices_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.ListVirtualMFADevicesResponse:
        req = open_api_models.OpenApiRequest()
        return ram_20150501_models.ListVirtualMFADevicesResponse().from_map(
            await self.do_rpcrequest_async('ListVirtualMFADevices', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.RemoveUserFromGroupResponse().from_map(
            self.do_rpcrequest('RemoveUserFromGroup', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_user_from_group_with_options_async(
        self,
        request: ram_20150501_models.RemoveUserFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.RemoveUserFromGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.RemoveUserFromGroupResponse().from_map(
            await self.do_rpcrequest_async('RemoveUserFromGroup', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.SetAccountAliasResponse().from_map(
            self.do_rpcrequest('SetAccountAlias', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_account_alias_with_options_async(
        self,
        request: ram_20150501_models.SetAccountAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.SetAccountAliasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.SetAccountAliasResponse().from_map(
            await self.do_rpcrequest_async('SetAccountAlias', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.SetDefaultPolicyVersionResponse().from_map(
            self.do_rpcrequest('SetDefaultPolicyVersion', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_default_policy_version_with_options_async(
        self,
        request: ram_20150501_models.SetDefaultPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.SetDefaultPolicyVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.SetDefaultPolicyVersionResponse().from_map(
            await self.do_rpcrequest_async('SetDefaultPolicyVersion', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.SetPasswordPolicyResponse().from_map(
            self.do_rpcrequest('SetPasswordPolicy', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_password_policy_with_options_async(
        self,
        request: ram_20150501_models.SetPasswordPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.SetPasswordPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.SetPasswordPolicyResponse().from_map(
            await self.do_rpcrequest_async('SetPasswordPolicy', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.SetSecurityPreferenceResponse().from_map(
            self.do_rpcrequest('SetSecurityPreference', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_security_preference_with_options_async(
        self,
        request: ram_20150501_models.SetSecurityPreferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.SetSecurityPreferenceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.SetSecurityPreferenceResponse().from_map(
            await self.do_rpcrequest_async('SetSecurityPreference', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.UnbindMFADeviceResponse().from_map(
            self.do_rpcrequest('UnbindMFADevice', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_mfadevice_with_options_async(
        self,
        request: ram_20150501_models.UnbindMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.UnbindMFADeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.UnbindMFADeviceResponse().from_map(
            await self.do_rpcrequest_async('UnbindMFADevice', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.UpdateAccessKeyResponse().from_map(
            self.do_rpcrequest('UpdateAccessKey', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_access_key_with_options_async(
        self,
        request: ram_20150501_models.UpdateAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.UpdateAccessKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.UpdateAccessKeyResponse().from_map(
            await self.do_rpcrequest_async('UpdateAccessKey', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.UpdateGroupResponse().from_map(
            self.do_rpcrequest('UpdateGroup', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_group_with_options_async(
        self,
        request: ram_20150501_models.UpdateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.UpdateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.UpdateGroupResponse().from_map(
            await self.do_rpcrequest_async('UpdateGroup', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.UpdateLoginProfileResponse().from_map(
            self.do_rpcrequest('UpdateLoginProfile', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_login_profile_with_options_async(
        self,
        request: ram_20150501_models.UpdateLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.UpdateLoginProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.UpdateLoginProfileResponse().from_map(
            await self.do_rpcrequest_async('UpdateLoginProfile', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.UpdateRoleResponse().from_map(
            self.do_rpcrequest('UpdateRole', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_role_with_options_async(
        self,
        request: ram_20150501_models.UpdateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.UpdateRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.UpdateRoleResponse().from_map(
            await self.do_rpcrequest_async('UpdateRole', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.UpdateUserResponse().from_map(
            self.do_rpcrequest('UpdateUser', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: ram_20150501_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ram_20150501_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ram_20150501_models.UpdateUserResponse().from_map(
            await self.do_rpcrequest_async('UpdateUser', '2015-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
