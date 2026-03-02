# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ims20190815 import models as main_models
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
        self._endpoint = self.get_endpoint('ims', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_client_id_to_oidcprovider_with_options(
        self,
        request: main_models.AddClientIdToOIDCProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddClientIdToOIDCProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddClientIdToOIDCProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddClientIdToOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_client_id_to_oidcprovider_with_options_async(
        self,
        request: main_models.AddClientIdToOIDCProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddClientIdToOIDCProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddClientIdToOIDCProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddClientIdToOIDCProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_client_id_to_oidcprovider(
        self,
        request: main_models.AddClientIdToOIDCProviderRequest,
    ) -> main_models.AddClientIdToOIDCProviderResponse:
        runtime = RuntimeOptions()
        return self.add_client_id_to_oidcprovider_with_options(request, runtime)

    async def add_client_id_to_oidcprovider_async(
        self,
        request: main_models.AddClientIdToOIDCProviderRequest,
    ) -> main_models.AddClientIdToOIDCProviderResponse:
        runtime = RuntimeOptions()
        return await self.add_client_id_to_oidcprovider_with_options_async(request, runtime)

    def add_fingerprint_to_oidcprovider_with_options(
        self,
        request: main_models.AddFingerprintToOIDCProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFingerprintToOIDCProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fingerprint):
            query['Fingerprint'] = request.fingerprint
        if not DaraCore.is_null(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddFingerprintToOIDCProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFingerprintToOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_fingerprint_to_oidcprovider_with_options_async(
        self,
        request: main_models.AddFingerprintToOIDCProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFingerprintToOIDCProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fingerprint):
            query['Fingerprint'] = request.fingerprint
        if not DaraCore.is_null(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddFingerprintToOIDCProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFingerprintToOIDCProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_fingerprint_to_oidcprovider(
        self,
        request: main_models.AddFingerprintToOIDCProviderRequest,
    ) -> main_models.AddFingerprintToOIDCProviderResponse:
        runtime = RuntimeOptions()
        return self.add_fingerprint_to_oidcprovider_with_options(request, runtime)

    async def add_fingerprint_to_oidcprovider_async(
        self,
        request: main_models.AddFingerprintToOIDCProviderRequest,
    ) -> main_models.AddFingerprintToOIDCProviderResponse:
        runtime = RuntimeOptions()
        return await self.add_fingerprint_to_oidcprovider_with_options_async(request, runtime)

    def add_user_to_group_with_options(
        self,
        request: main_models.AddUserToGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserToGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserToGroup',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserToGroup',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindMFADevice',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindMFADevice',
            version = '2019-08-15',
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
            version = '2019-08-15',
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
            version = '2019-08-15',
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

    def create_access_key_with_options(
        self,
        request: main_models.CreateAccessKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessKey',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessKey',
            version = '2019-08-15',
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

    def create_app_secret_with_options(
        self,
        request: main_models.CreateAppSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppSecret',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_secret_with_options_async(
        self,
        request: main_models.CreateAppSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppSecret',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_secret(
        self,
        request: main_models.CreateAppSecretRequest,
    ) -> main_models.CreateAppSecretResponse:
        runtime = RuntimeOptions()
        return self.create_app_secret_with_options(request, runtime)

    async def create_app_secret_async(
        self,
        request: main_models.CreateAppSecretRequest,
    ) -> main_models.CreateAppSecretResponse:
        runtime = RuntimeOptions()
        return await self.create_app_secret_with_options_async(request, runtime)

    def create_application_with_options(
        self,
        request: main_models.CreateApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_token_validity):
            query['AccessTokenValidity'] = request.access_token_validity
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.is_multi_tenant):
            query['IsMultiTenant'] = request.is_multi_tenant
        if not DaraCore.is_null(request.predefined_scopes):
            query['PredefinedScopes'] = request.predefined_scopes
        if not DaraCore.is_null(request.protocol_version):
            query['ProtocolVersion'] = request.protocol_version
        if not DaraCore.is_null(request.redirect_uris):
            query['RedirectUris'] = request.redirect_uris
        if not DaraCore.is_null(request.refresh_token_validity):
            query['RefreshTokenValidity'] = request.refresh_token_validity
        if not DaraCore.is_null(request.required_scopes):
            query['RequiredScopes'] = request.required_scopes
        if not DaraCore.is_null(request.secret_required):
            query['SecretRequired'] = request.secret_required
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplication',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_with_options_async(
        self,
        request: main_models.CreateApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_token_validity):
            query['AccessTokenValidity'] = request.access_token_validity
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.is_multi_tenant):
            query['IsMultiTenant'] = request.is_multi_tenant
        if not DaraCore.is_null(request.predefined_scopes):
            query['PredefinedScopes'] = request.predefined_scopes
        if not DaraCore.is_null(request.protocol_version):
            query['ProtocolVersion'] = request.protocol_version
        if not DaraCore.is_null(request.redirect_uris):
            query['RedirectUris'] = request.redirect_uris
        if not DaraCore.is_null(request.refresh_token_validity):
            query['RefreshTokenValidity'] = request.refresh_token_validity
        if not DaraCore.is_null(request.required_scopes):
            query['RequiredScopes'] = request.required_scopes
        if not DaraCore.is_null(request.secret_required):
            query['SecretRequired'] = request.secret_required
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplication',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application(
        self,
        request: main_models.CreateApplicationRequest,
    ) -> main_models.CreateApplicationResponse:
        runtime = RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    async def create_application_async(
        self,
        request: main_models.CreateApplicationRequest,
    ) -> main_models.CreateApplicationResponse:
        runtime = RuntimeOptions()
        return await self.create_application_with_options_async(request, runtime)

    def create_group_with_options(
        self,
        request: main_models.CreateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comments):
            query['Comments'] = request.comments
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroup',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroup',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoginProfile',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoginProfile',
            version = '2019-08-15',
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

    def create_oidcprovider_with_options(
        self,
        request: main_models.CreateOIDCProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOIDCProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_ids):
            query['ClientIds'] = request.client_ids
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.fingerprints):
            query['Fingerprints'] = request.fingerprints
        if not DaraCore.is_null(request.issuance_limit_time):
            query['IssuanceLimitTime'] = request.issuance_limit_time
        if not DaraCore.is_null(request.issuer_url):
            query['IssuerUrl'] = request.issuer_url
        if not DaraCore.is_null(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOIDCProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_oidcprovider_with_options_async(
        self,
        request: main_models.CreateOIDCProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOIDCProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_ids):
            query['ClientIds'] = request.client_ids
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.fingerprints):
            query['Fingerprints'] = request.fingerprints
        if not DaraCore.is_null(request.issuance_limit_time):
            query['IssuanceLimitTime'] = request.issuance_limit_time
        if not DaraCore.is_null(request.issuer_url):
            query['IssuerUrl'] = request.issuer_url
        if not DaraCore.is_null(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOIDCProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOIDCProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_oidcprovider(
        self,
        request: main_models.CreateOIDCProviderRequest,
    ) -> main_models.CreateOIDCProviderResponse:
        runtime = RuntimeOptions()
        return self.create_oidcprovider_with_options(request, runtime)

    async def create_oidcprovider_async(
        self,
        request: main_models.CreateOIDCProviderRequest,
    ) -> main_models.CreateOIDCProviderResponse:
        runtime = RuntimeOptions()
        return await self.create_oidcprovider_with_options_async(request, runtime)

    def create_samlprovider_with_options(
        self,
        request: main_models.CreateSAMLProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSAMLProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authn_sign_algo):
            query['AuthnSignAlgo'] = request.authn_sign_algo
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.encoded_samlmetadata_document):
            query['EncodedSAMLMetadataDocument'] = request.encoded_samlmetadata_document
        if not DaraCore.is_null(request.samlprovider_name):
            query['SAMLProviderName'] = request.samlprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSAMLProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSAMLProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_samlprovider_with_options_async(
        self,
        request: main_models.CreateSAMLProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSAMLProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authn_sign_algo):
            query['AuthnSignAlgo'] = request.authn_sign_algo
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.encoded_samlmetadata_document):
            query['EncodedSAMLMetadataDocument'] = request.encoded_samlmetadata_document
        if not DaraCore.is_null(request.samlprovider_name):
            query['SAMLProviderName'] = request.samlprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSAMLProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSAMLProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_samlprovider(
        self,
        request: main_models.CreateSAMLProviderRequest,
    ) -> main_models.CreateSAMLProviderResponse:
        runtime = RuntimeOptions()
        return self.create_samlprovider_with_options(request, runtime)

    async def create_samlprovider_async(
        self,
        request: main_models.CreateSAMLProviderRequest,
    ) -> main_models.CreateSAMLProviderResponse:
        runtime = RuntimeOptions()
        return await self.create_samlprovider_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2019-08-15',
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
            version = '2019-08-15',
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
            version = '2019-08-15',
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

    def delete_access_key_with_options(
        self,
        request: main_models.DeleteAccessKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessKey',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessKey',
            version = '2019-08-15',
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

    def delete_access_key_in_recycle_bin_with_options(
        self,
        request: main_models.DeleteAccessKeyInRecycleBinRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessKeyInRecycleBinResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessKeyInRecycleBin',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessKeyInRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_key_in_recycle_bin_with_options_async(
        self,
        request: main_models.DeleteAccessKeyInRecycleBinRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessKeyInRecycleBinResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessKeyInRecycleBin',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessKeyInRecycleBinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_key_in_recycle_bin(
        self,
        request: main_models.DeleteAccessKeyInRecycleBinRequest,
    ) -> main_models.DeleteAccessKeyInRecycleBinResponse:
        runtime = RuntimeOptions()
        return self.delete_access_key_in_recycle_bin_with_options(request, runtime)

    async def delete_access_key_in_recycle_bin_async(
        self,
        request: main_models.DeleteAccessKeyInRecycleBinRequest,
    ) -> main_models.DeleteAccessKeyInRecycleBinResponse:
        runtime = RuntimeOptions()
        return await self.delete_access_key_in_recycle_bin_with_options_async(request, runtime)

    def delete_app_secret_with_options(
        self,
        request: main_models.DeleteAppSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_secret_id):
            query['AppSecretId'] = request.app_secret_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppSecret',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_secret_with_options_async(
        self,
        request: main_models.DeleteAppSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_secret_id):
            query['AppSecretId'] = request.app_secret_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppSecret',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_secret(
        self,
        request: main_models.DeleteAppSecretRequest,
    ) -> main_models.DeleteAppSecretResponse:
        runtime = RuntimeOptions()
        return self.delete_app_secret_with_options(request, runtime)

    async def delete_app_secret_async(
        self,
        request: main_models.DeleteAppSecretRequest,
    ) -> main_models.DeleteAppSecretResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_secret_with_options_async(request, runtime)

    def delete_application_with_options(
        self,
        request: main_models.DeleteApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplication',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_with_options_async(
        self,
        request: main_models.DeleteApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplication',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application(
        self,
        request: main_models.DeleteApplicationRequest,
    ) -> main_models.DeleteApplicationResponse:
        runtime = RuntimeOptions()
        return self.delete_application_with_options(request, runtime)

    async def delete_application_async(
        self,
        request: main_models.DeleteApplicationRequest,
    ) -> main_models.DeleteApplicationResponse:
        runtime = RuntimeOptions()
        return await self.delete_application_with_options_async(request, runtime)

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
            version = '2019-08-15',
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
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLoginProfile',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLoginProfile',
            version = '2019-08-15',
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

    def delete_oidcprovider_with_options(
        self,
        request: main_models.DeleteOIDCProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOIDCProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOIDCProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_oidcprovider_with_options_async(
        self,
        request: main_models.DeleteOIDCProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOIDCProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOIDCProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOIDCProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_oidcprovider(
        self,
        request: main_models.DeleteOIDCProviderRequest,
    ) -> main_models.DeleteOIDCProviderResponse:
        runtime = RuntimeOptions()
        return self.delete_oidcprovider_with_options(request, runtime)

    async def delete_oidcprovider_async(
        self,
        request: main_models.DeleteOIDCProviderRequest,
    ) -> main_models.DeleteOIDCProviderResponse:
        runtime = RuntimeOptions()
        return await self.delete_oidcprovider_with_options_async(request, runtime)

    def delete_passkey_with_options(
        self,
        request: main_models.DeletePasskeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePasskeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.passkey_id):
            query['PasskeyId'] = request.passkey_id
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePasskey',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePasskeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_passkey_with_options_async(
        self,
        request: main_models.DeletePasskeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePasskeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.passkey_id):
            query['PasskeyId'] = request.passkey_id
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePasskey',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePasskeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_passkey(
        self,
        request: main_models.DeletePasskeyRequest,
    ) -> main_models.DeletePasskeyResponse:
        runtime = RuntimeOptions()
        return self.delete_passkey_with_options(request, runtime)

    async def delete_passkey_async(
        self,
        request: main_models.DeletePasskeyRequest,
    ) -> main_models.DeletePasskeyResponse:
        runtime = RuntimeOptions()
        return await self.delete_passkey_with_options_async(request, runtime)

    def delete_samlprovider_with_options(
        self,
        request: main_models.DeleteSAMLProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSAMLProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.samlprovider_name):
            query['SAMLProviderName'] = request.samlprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSAMLProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSAMLProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_samlprovider_with_options_async(
        self,
        request: main_models.DeleteSAMLProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSAMLProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.samlprovider_name):
            query['SAMLProviderName'] = request.samlprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSAMLProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSAMLProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_samlprovider(
        self,
        request: main_models.DeleteSAMLProviderRequest,
    ) -> main_models.DeleteSAMLProviderResponse:
        runtime = RuntimeOptions()
        return self.delete_samlprovider_with_options(request, runtime)

    async def delete_samlprovider_async(
        self,
        request: main_models.DeleteSAMLProviderRequest,
    ) -> main_models.DeleteSAMLProviderResponse:
        runtime = RuntimeOptions()
        return await self.delete_samlprovider_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: main_models.DeleteUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2019-08-15',
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

    def delete_user_in_recycle_bin_with_options(
        self,
        request: main_models.DeleteUserInRecycleBinRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserInRecycleBinResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserInRecycleBin',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserInRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_in_recycle_bin_with_options_async(
        self,
        request: main_models.DeleteUserInRecycleBinRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserInRecycleBinResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserInRecycleBin',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserInRecycleBinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_in_recycle_bin(
        self,
        request: main_models.DeleteUserInRecycleBinRequest,
    ) -> main_models.DeleteUserInRecycleBinResponse:
        runtime = RuntimeOptions()
        return self.delete_user_in_recycle_bin_with_options(request, runtime)

    async def delete_user_in_recycle_bin_async(
        self,
        request: main_models.DeleteUserInRecycleBinRequest,
    ) -> main_models.DeleteUserInRecycleBinResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_in_recycle_bin_with_options_async(request, runtime)

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
            version = '2019-08-15',
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
            version = '2019-08-15',
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

    def deprovision_application_with_options(
        self,
        request: main_models.DeprovisionApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeprovisionApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeprovisionApplication',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeprovisionApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def deprovision_application_with_options_async(
        self,
        request: main_models.DeprovisionApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeprovisionApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeprovisionApplication',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeprovisionApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deprovision_application(
        self,
        request: main_models.DeprovisionApplicationRequest,
    ) -> main_models.DeprovisionApplicationResponse:
        runtime = RuntimeOptions()
        return self.deprovision_application_with_options(request, runtime)

    async def deprovision_application_async(
        self,
        request: main_models.DeprovisionApplicationRequest,
    ) -> main_models.DeprovisionApplicationResponse:
        runtime = RuntimeOptions()
        return await self.deprovision_application_with_options_async(request, runtime)

    def deprovision_external_application_with_options(
        self,
        request: main_models.DeprovisionExternalApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeprovisionExternalApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeprovisionExternalApplication',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeprovisionExternalApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def deprovision_external_application_with_options_async(
        self,
        request: main_models.DeprovisionExternalApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeprovisionExternalApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeprovisionExternalApplication',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeprovisionExternalApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deprovision_external_application(
        self,
        request: main_models.DeprovisionExternalApplicationRequest,
    ) -> main_models.DeprovisionExternalApplicationResponse:
        runtime = RuntimeOptions()
        return self.deprovision_external_application_with_options(request, runtime)

    async def deprovision_external_application_async(
        self,
        request: main_models.DeprovisionExternalApplicationRequest,
    ) -> main_models.DeprovisionExternalApplicationResponse:
        runtime = RuntimeOptions()
        return await self.deprovision_external_application_with_options_async(request, runtime)

    def disable_virtual_mfawith_options(
        self,
        request: main_models.DisableVirtualMFARequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableVirtualMFAResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableVirtualMFA',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableVirtualMFAResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_virtual_mfawith_options_async(
        self,
        request: main_models.DisableVirtualMFARequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableVirtualMFAResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableVirtualMFA',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableVirtualMFAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_virtual_mfa(
        self,
        request: main_models.DisableVirtualMFARequest,
    ) -> main_models.DisableVirtualMFAResponse:
        runtime = RuntimeOptions()
        return self.disable_virtual_mfawith_options(request, runtime)

    async def disable_virtual_mfa_async(
        self,
        request: main_models.DisableVirtualMFARequest,
    ) -> main_models.DisableVirtualMFAResponse:
        runtime = RuntimeOptions()
        return await self.disable_virtual_mfawith_options_async(request, runtime)

    def generate_credential_report_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateCredentialReportResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GenerateCredentialReport',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateCredentialReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_credential_report_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateCredentialReportResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GenerateCredentialReport',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateCredentialReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_credential_report(self) -> main_models.GenerateCredentialReportResponse:
        runtime = RuntimeOptions()
        return self.generate_credential_report_with_options(runtime)

    async def generate_credential_report_async(self) -> main_models.GenerateCredentialReportResponse:
        runtime = RuntimeOptions()
        return await self.generate_credential_report_with_options_async(runtime)

    def generate_governance_report_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateGovernanceReportResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GenerateGovernanceReport',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateGovernanceReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_governance_report_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateGovernanceReportResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GenerateGovernanceReport',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateGovernanceReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_governance_report(self) -> main_models.GenerateGovernanceReportResponse:
        runtime = RuntimeOptions()
        return self.generate_governance_report_with_options(runtime)

    async def generate_governance_report_async(self) -> main_models.GenerateGovernanceReportResponse:
        runtime = RuntimeOptions()
        return await self.generate_governance_report_with_options_async(runtime)

    def get_access_key_info_in_recycle_bin_with_options(
        self,
        request: main_models.GetAccessKeyInfoInRecycleBinRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessKeyInfoInRecycleBinResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessKeyInfoInRecycleBin',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessKeyInfoInRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_key_info_in_recycle_bin_with_options_async(
        self,
        request: main_models.GetAccessKeyInfoInRecycleBinRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessKeyInfoInRecycleBinResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessKeyInfoInRecycleBin',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessKeyInfoInRecycleBinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_key_info_in_recycle_bin(
        self,
        request: main_models.GetAccessKeyInfoInRecycleBinRequest,
    ) -> main_models.GetAccessKeyInfoInRecycleBinResponse:
        runtime = RuntimeOptions()
        return self.get_access_key_info_in_recycle_bin_with_options(request, runtime)

    async def get_access_key_info_in_recycle_bin_async(
        self,
        request: main_models.GetAccessKeyInfoInRecycleBinRequest,
    ) -> main_models.GetAccessKeyInfoInRecycleBinResponse:
        runtime = RuntimeOptions()
        return await self.get_access_key_info_in_recycle_bin_with_options_async(request, runtime)

    def get_access_key_last_used_with_options(
        self,
        request: main_models.GetAccessKeyLastUsedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessKeyLastUsedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessKeyLastUsed',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessKeyLastUsed',
            version = '2019-08-15',
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

    def get_account_mfainfo_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountMFAInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetAccountMFAInfo',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountMFAInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_mfainfo_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountMFAInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetAccountMFAInfo',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountMFAInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_mfainfo(self) -> main_models.GetAccountMFAInfoResponse:
        runtime = RuntimeOptions()
        return self.get_account_mfainfo_with_options(runtime)

    async def get_account_mfainfo_async(self) -> main_models.GetAccountMFAInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_account_mfainfo_with_options_async(runtime)

    def get_account_security_practice_report_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountSecurityPracticeReportResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetAccountSecurityPracticeReport',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountSecurityPracticeReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_security_practice_report_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountSecurityPracticeReportResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetAccountSecurityPracticeReport',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountSecurityPracticeReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_security_practice_report(self) -> main_models.GetAccountSecurityPracticeReportResponse:
        runtime = RuntimeOptions()
        return self.get_account_security_practice_report_with_options(runtime)

    async def get_account_security_practice_report_async(self) -> main_models.GetAccountSecurityPracticeReportResponse:
        runtime = RuntimeOptions()
        return await self.get_account_security_practice_report_with_options_async(runtime)

    def get_account_summary_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountSummaryResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetAccountSummary',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_summary_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountSummaryResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetAccountSummary',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_summary(self) -> main_models.GetAccountSummaryResponse:
        runtime = RuntimeOptions()
        return self.get_account_summary_with_options(runtime)

    async def get_account_summary_async(self) -> main_models.GetAccountSummaryResponse:
        runtime = RuntimeOptions()
        return await self.get_account_summary_with_options_async(runtime)

    def get_app_secret_with_options(
        self,
        request: main_models.GetAppSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_secret_id):
            query['AppSecretId'] = request.app_secret_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppSecret',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_secret_with_options_async(
        self,
        request: main_models.GetAppSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_secret_id):
            query['AppSecretId'] = request.app_secret_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppSecret',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_secret(
        self,
        request: main_models.GetAppSecretRequest,
    ) -> main_models.GetAppSecretResponse:
        runtime = RuntimeOptions()
        return self.get_app_secret_with_options(request, runtime)

    async def get_app_secret_async(
        self,
        request: main_models.GetAppSecretRequest,
    ) -> main_models.GetAppSecretResponse:
        runtime = RuntimeOptions()
        return await self.get_app_secret_with_options_async(request, runtime)

    def get_application_with_options(
        self,
        request: main_models.GetApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplication',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_with_options_async(
        self,
        request: main_models.GetApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplication',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application(
        self,
        request: main_models.GetApplicationRequest,
    ) -> main_models.GetApplicationResponse:
        runtime = RuntimeOptions()
        return self.get_application_with_options(request, runtime)

    async def get_application_async(
        self,
        request: main_models.GetApplicationRequest,
    ) -> main_models.GetApplicationResponse:
        runtime = RuntimeOptions()
        return await self.get_application_with_options_async(request, runtime)

    def get_application_provision_info_with_options(
        self,
        request: main_models.GetApplicationProvisionInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationProvisionInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationProvisionInfo',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationProvisionInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_provision_info_with_options_async(
        self,
        request: main_models.GetApplicationProvisionInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationProvisionInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationProvisionInfo',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationProvisionInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_provision_info(
        self,
        request: main_models.GetApplicationProvisionInfoRequest,
    ) -> main_models.GetApplicationProvisionInfoResponse:
        runtime = RuntimeOptions()
        return self.get_application_provision_info_with_options(request, runtime)

    async def get_application_provision_info_async(
        self,
        request: main_models.GetApplicationProvisionInfoRequest,
    ) -> main_models.GetApplicationProvisionInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_application_provision_info_with_options_async(request, runtime)

    def get_credential_report_with_options(
        self,
        request: main_models.GetCredentialReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCredentialReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_items):
            query['MaxItems'] = request.max_items
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCredentialReport',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCredentialReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_credential_report_with_options_async(
        self,
        request: main_models.GetCredentialReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCredentialReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_items):
            query['MaxItems'] = request.max_items
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCredentialReport',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCredentialReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_credential_report(
        self,
        request: main_models.GetCredentialReportRequest,
    ) -> main_models.GetCredentialReportResponse:
        runtime = RuntimeOptions()
        return self.get_credential_report_with_options(request, runtime)

    async def get_credential_report_async(
        self,
        request: main_models.GetCredentialReportRequest,
    ) -> main_models.GetCredentialReportResponse:
        runtime = RuntimeOptions()
        return await self.get_credential_report_with_options_async(request, runtime)

    def get_default_domain_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetDefaultDomainResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetDefaultDomain',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDefaultDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_default_domain_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetDefaultDomainResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetDefaultDomain',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDefaultDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_default_domain(self) -> main_models.GetDefaultDomainResponse:
        runtime = RuntimeOptions()
        return self.get_default_domain_with_options(runtime)

    async def get_default_domain_async(self) -> main_models.GetDefaultDomainResponse:
        runtime = RuntimeOptions()
        return await self.get_default_domain_with_options_async(runtime)

    def get_external_application_with_options(
        self,
        request: main_models.GetExternalApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExternalApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExternalApplication',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExternalApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_external_application_with_options_async(
        self,
        request: main_models.GetExternalApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExternalApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExternalApplication',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExternalApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_external_application(
        self,
        request: main_models.GetExternalApplicationRequest,
    ) -> main_models.GetExternalApplicationResponse:
        runtime = RuntimeOptions()
        return self.get_external_application_with_options(request, runtime)

    async def get_external_application_async(
        self,
        request: main_models.GetExternalApplicationRequest,
    ) -> main_models.GetExternalApplicationResponse:
        runtime = RuntimeOptions()
        return await self.get_external_application_with_options_async(request, runtime)

    def get_governance_item_report_with_options(
        self,
        request: main_models.GetGovernanceItemReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGovernanceItemReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.governance_item_type):
            query['GovernanceItemType'] = request.governance_item_type
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGovernanceItemReport',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGovernanceItemReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_governance_item_report_with_options_async(
        self,
        request: main_models.GetGovernanceItemReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGovernanceItemReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.governance_item_type):
            query['GovernanceItemType'] = request.governance_item_type
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGovernanceItemReport',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGovernanceItemReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_governance_item_report(
        self,
        request: main_models.GetGovernanceItemReportRequest,
    ) -> main_models.GetGovernanceItemReportResponse:
        runtime = RuntimeOptions()
        return self.get_governance_item_report_with_options(request, runtime)

    async def get_governance_item_report_async(
        self,
        request: main_models.GetGovernanceItemReportRequest,
    ) -> main_models.GetGovernanceItemReportResponse:
        runtime = RuntimeOptions()
        return await self.get_governance_item_report_with_options_async(request, runtime)

    def get_governance_report_status_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetGovernanceReportStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetGovernanceReportStatus',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGovernanceReportStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_governance_report_status_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetGovernanceReportStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetGovernanceReportStatus',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGovernanceReportStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_governance_report_status(self) -> main_models.GetGovernanceReportStatusResponse:
        runtime = RuntimeOptions()
        return self.get_governance_report_status_with_options(runtime)

    async def get_governance_report_status_async(self) -> main_models.GetGovernanceReportStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_governance_report_status_with_options_async(runtime)

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
            version = '2019-08-15',
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
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLoginProfile',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLoginProfile',
            version = '2019-08-15',
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

    def get_oidcprovider_with_options(
        self,
        request: main_models.GetOIDCProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOIDCProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOIDCProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oidcprovider_with_options_async(
        self,
        request: main_models.GetOIDCProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOIDCProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOIDCProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOIDCProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oidcprovider(
        self,
        request: main_models.GetOIDCProviderRequest,
    ) -> main_models.GetOIDCProviderResponse:
        runtime = RuntimeOptions()
        return self.get_oidcprovider_with_options(request, runtime)

    async def get_oidcprovider_async(
        self,
        request: main_models.GetOIDCProviderRequest,
    ) -> main_models.GetOIDCProviderResponse:
        runtime = RuntimeOptions()
        return await self.get_oidcprovider_with_options_async(request, runtime)

    def get_password_policy_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetPasswordPolicyResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetPasswordPolicy',
            version = '2019-08-15',
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
            version = '2019-08-15',
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

    def get_samlprovider_with_options(
        self,
        request: main_models.GetSAMLProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSAMLProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.samlprovider_name):
            query['SAMLProviderName'] = request.samlprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSAMLProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSAMLProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_samlprovider_with_options_async(
        self,
        request: main_models.GetSAMLProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSAMLProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.samlprovider_name):
            query['SAMLProviderName'] = request.samlprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSAMLProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSAMLProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_samlprovider(
        self,
        request: main_models.GetSAMLProviderRequest,
    ) -> main_models.GetSAMLProviderResponse:
        runtime = RuntimeOptions()
        return self.get_samlprovider_with_options(request, runtime)

    async def get_samlprovider_async(
        self,
        request: main_models.GetSAMLProviderRequest,
    ) -> main_models.GetSAMLProviderResponse:
        runtime = RuntimeOptions()
        return await self.get_samlprovider_with_options_async(request, runtime)

    def get_security_preference_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecurityPreferenceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetSecurityPreference',
            version = '2019-08-15',
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
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2019-08-15',
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

    def get_user_in_recycle_bin_with_options(
        self,
        request: main_models.GetUserInRecycleBinRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserInRecycleBinResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserInRecycleBin',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserInRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_in_recycle_bin_with_options_async(
        self,
        request: main_models.GetUserInRecycleBinRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserInRecycleBinResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserInRecycleBin',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserInRecycleBinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_in_recycle_bin(
        self,
        request: main_models.GetUserInRecycleBinRequest,
    ) -> main_models.GetUserInRecycleBinResponse:
        runtime = RuntimeOptions()
        return self.get_user_in_recycle_bin_with_options(request, runtime)

    async def get_user_in_recycle_bin_async(
        self,
        request: main_models.GetUserInRecycleBinRequest,
    ) -> main_models.GetUserInRecycleBinResponse:
        runtime = RuntimeOptions()
        return await self.get_user_in_recycle_bin_with_options_async(request, runtime)

    def get_user_mfainfo_with_options(
        self,
        request: main_models.GetUserMFAInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserMFAInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserMFAInfo',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserMFAInfo',
            version = '2019-08-15',
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

    def get_user_sso_settings_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserSsoSettingsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetUserSsoSettings',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserSsoSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_sso_settings_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserSsoSettingsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetUserSsoSettings',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserSsoSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_sso_settings(self) -> main_models.GetUserSsoSettingsResponse:
        runtime = RuntimeOptions()
        return self.get_user_sso_settings_with_options(runtime)

    async def get_user_sso_settings_async(self) -> main_models.GetUserSsoSettingsResponse:
        runtime = RuntimeOptions()
        return await self.get_user_sso_settings_with_options_async(runtime)

    def get_verification_info_with_options(
        self,
        request: main_models.GetVerificationInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVerificationInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVerificationInfo',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVerificationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_verification_info_with_options_async(
        self,
        request: main_models.GetVerificationInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVerificationInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVerificationInfo',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVerificationInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_verification_info(
        self,
        request: main_models.GetVerificationInfoRequest,
    ) -> main_models.GetVerificationInfoResponse:
        runtime = RuntimeOptions()
        return self.get_verification_info_with_options(request, runtime)

    async def get_verification_info_async(
        self,
        request: main_models.GetVerificationInfoRequest,
    ) -> main_models.GetVerificationInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_verification_info_with_options_async(request, runtime)

    def list_access_keys_with_options(
        self,
        request: main_models.ListAccessKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccessKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccessKeys',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccessKeys',
            version = '2019-08-15',
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

    def list_access_keys_in_recycle_bin_with_options(
        self,
        request: main_models.ListAccessKeysInRecycleBinRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccessKeysInRecycleBinResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccessKeysInRecycleBin',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccessKeysInRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_access_keys_in_recycle_bin_with_options_async(
        self,
        request: main_models.ListAccessKeysInRecycleBinRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccessKeysInRecycleBinResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccessKeysInRecycleBin',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccessKeysInRecycleBinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_access_keys_in_recycle_bin(
        self,
        request: main_models.ListAccessKeysInRecycleBinRequest,
    ) -> main_models.ListAccessKeysInRecycleBinResponse:
        runtime = RuntimeOptions()
        return self.list_access_keys_in_recycle_bin_with_options(request, runtime)

    async def list_access_keys_in_recycle_bin_async(
        self,
        request: main_models.ListAccessKeysInRecycleBinRequest,
    ) -> main_models.ListAccessKeysInRecycleBinResponse:
        runtime = RuntimeOptions()
        return await self.list_access_keys_in_recycle_bin_with_options_async(request, runtime)

    def list_app_secret_ids_with_options(
        self,
        request: main_models.ListAppSecretIdsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppSecretIdsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppSecretIds',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppSecretIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_secret_ids_with_options_async(
        self,
        request: main_models.ListAppSecretIdsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppSecretIdsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppSecretIds',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppSecretIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_secret_ids(
        self,
        request: main_models.ListAppSecretIdsRequest,
    ) -> main_models.ListAppSecretIdsResponse:
        runtime = RuntimeOptions()
        return self.list_app_secret_ids_with_options(request, runtime)

    async def list_app_secret_ids_async(
        self,
        request: main_models.ListAppSecretIdsRequest,
    ) -> main_models.ListAppSecretIdsResponse:
        runtime = RuntimeOptions()
        return await self.list_app_secret_ids_with_options_async(request, runtime)

    def list_application_provision_infos_with_options(
        self,
        request: main_models.ListApplicationProvisionInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationProvisionInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationProvisionInfos',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationProvisionInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_provision_infos_with_options_async(
        self,
        request: main_models.ListApplicationProvisionInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationProvisionInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationProvisionInfos',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationProvisionInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_provision_infos(
        self,
        request: main_models.ListApplicationProvisionInfosRequest,
    ) -> main_models.ListApplicationProvisionInfosResponse:
        runtime = RuntimeOptions()
        return self.list_application_provision_infos_with_options(request, runtime)

    async def list_application_provision_infos_async(
        self,
        request: main_models.ListApplicationProvisionInfosRequest,
    ) -> main_models.ListApplicationProvisionInfosResponse:
        runtime = RuntimeOptions()
        return await self.list_application_provision_infos_with_options_async(request, runtime)

    def list_applications_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListApplications',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListApplications',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications(self) -> main_models.ListApplicationsResponse:
        runtime = RuntimeOptions()
        return self.list_applications_with_options(runtime)

    async def list_applications_async(self) -> main_models.ListApplicationsResponse:
        runtime = RuntimeOptions()
        return await self.list_applications_with_options_async(runtime)

    def list_external_applications_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListExternalApplicationsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListExternalApplications',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExternalApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_external_applications_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListExternalApplicationsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListExternalApplications',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExternalApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_external_applications(self) -> main_models.ListExternalApplicationsResponse:
        runtime = RuntimeOptions()
        return self.list_external_applications_with_options(runtime)

    async def list_external_applications_async(self) -> main_models.ListExternalApplicationsResponse:
        runtime = RuntimeOptions()
        return await self.list_external_applications_with_options_async(runtime)

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
            version = '2019-08-15',
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
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroupsForUser',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroupsForUser',
            version = '2019-08-15',
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

    def list_oidcproviders_with_options(
        self,
        request: main_models.ListOIDCProvidersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOIDCProvidersResponse:
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
            action = 'ListOIDCProviders',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOIDCProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_oidcproviders_with_options_async(
        self,
        request: main_models.ListOIDCProvidersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOIDCProvidersResponse:
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
            action = 'ListOIDCProviders',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOIDCProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_oidcproviders(
        self,
        request: main_models.ListOIDCProvidersRequest,
    ) -> main_models.ListOIDCProvidersResponse:
        runtime = RuntimeOptions()
        return self.list_oidcproviders_with_options(request, runtime)

    async def list_oidcproviders_async(
        self,
        request: main_models.ListOIDCProvidersRequest,
    ) -> main_models.ListOIDCProvidersResponse:
        runtime = RuntimeOptions()
        return await self.list_oidcproviders_with_options_async(request, runtime)

    def list_passkeys_with_options(
        self,
        request: main_models.ListPasskeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPasskeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPasskeys',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPasskeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_passkeys_with_options_async(
        self,
        request: main_models.ListPasskeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPasskeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPasskeys',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPasskeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_passkeys(
        self,
        request: main_models.ListPasskeysRequest,
    ) -> main_models.ListPasskeysResponse:
        runtime = RuntimeOptions()
        return self.list_passkeys_with_options(request, runtime)

    async def list_passkeys_async(
        self,
        request: main_models.ListPasskeysRequest,
    ) -> main_models.ListPasskeysResponse:
        runtime = RuntimeOptions()
        return await self.list_passkeys_with_options_async(request, runtime)

    def list_predefined_scopes_with_options(
        self,
        request: main_models.ListPredefinedScopesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPredefinedScopesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPredefinedScopes',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPredefinedScopesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_predefined_scopes_with_options_async(
        self,
        request: main_models.ListPredefinedScopesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPredefinedScopesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPredefinedScopes',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPredefinedScopesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_predefined_scopes(
        self,
        request: main_models.ListPredefinedScopesRequest,
    ) -> main_models.ListPredefinedScopesResponse:
        runtime = RuntimeOptions()
        return self.list_predefined_scopes_with_options(request, runtime)

    async def list_predefined_scopes_async(
        self,
        request: main_models.ListPredefinedScopesRequest,
    ) -> main_models.ListPredefinedScopesResponse:
        runtime = RuntimeOptions()
        return await self.list_predefined_scopes_with_options_async(request, runtime)

    def list_recent_governance_metrics_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListRecentGovernanceMetricsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListRecentGovernanceMetrics',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecentGovernanceMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recent_governance_metrics_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListRecentGovernanceMetricsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListRecentGovernanceMetrics',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecentGovernanceMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recent_governance_metrics(self) -> main_models.ListRecentGovernanceMetricsResponse:
        runtime = RuntimeOptions()
        return self.list_recent_governance_metrics_with_options(runtime)

    async def list_recent_governance_metrics_async(self) -> main_models.ListRecentGovernanceMetricsResponse:
        runtime = RuntimeOptions()
        return await self.list_recent_governance_metrics_with_options_async(runtime)

    def list_samlproviders_with_options(
        self,
        request: main_models.ListSAMLProvidersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSAMLProvidersResponse:
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
            action = 'ListSAMLProviders',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSAMLProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_samlproviders_with_options_async(
        self,
        request: main_models.ListSAMLProvidersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSAMLProvidersResponse:
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
            action = 'ListSAMLProviders',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSAMLProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_samlproviders(
        self,
        request: main_models.ListSAMLProvidersRequest,
    ) -> main_models.ListSAMLProvidersResponse:
        runtime = RuntimeOptions()
        return self.list_samlproviders_with_options(request, runtime)

    async def list_samlproviders_async(
        self,
        request: main_models.ListSAMLProvidersRequest,
    ) -> main_models.ListSAMLProvidersResponse:
        runtime = RuntimeOptions()
        return await self.list_samlproviders_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_principal_name):
            query['ResourcePrincipalName'] = request.resource_principal_name
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_principal_name):
            query['ResourcePrincipalName'] = request.resource_principal_name
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-08-15',
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

    def list_user_basic_infos_with_options(
        self,
        request: main_models.ListUserBasicInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserBasicInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.max_items):
            query['MaxItems'] = request.max_items
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserBasicInfos',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserBasicInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_basic_infos_with_options_async(
        self,
        request: main_models.ListUserBasicInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserBasicInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.max_items):
            query['MaxItems'] = request.max_items
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserBasicInfos',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserBasicInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_basic_infos(
        self,
        request: main_models.ListUserBasicInfosRequest,
    ) -> main_models.ListUserBasicInfosResponse:
        runtime = RuntimeOptions()
        return self.list_user_basic_infos_with_options(request, runtime)

    async def list_user_basic_infos_async(
        self,
        request: main_models.ListUserBasicInfosRequest,
    ) -> main_models.ListUserBasicInfosResponse:
        runtime = RuntimeOptions()
        return await self.list_user_basic_infos_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2019-08-15',
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
            version = '2019-08-15',
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
            version = '2019-08-15',
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

    def list_users_in_recycle_bin_with_options(
        self,
        request: main_models.ListUsersInRecycleBinRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersInRecycleBinResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsersInRecycleBin',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersInRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_in_recycle_bin_with_options_async(
        self,
        request: main_models.ListUsersInRecycleBinRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersInRecycleBinResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsersInRecycleBin',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersInRecycleBinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users_in_recycle_bin(
        self,
        request: main_models.ListUsersInRecycleBinRequest,
    ) -> main_models.ListUsersInRecycleBinResponse:
        runtime = RuntimeOptions()
        return self.list_users_in_recycle_bin_with_options(request, runtime)

    async def list_users_in_recycle_bin_async(
        self,
        request: main_models.ListUsersInRecycleBinRequest,
    ) -> main_models.ListUsersInRecycleBinResponse:
        runtime = RuntimeOptions()
        return await self.list_users_in_recycle_bin_with_options_async(request, runtime)

    def list_virtual_mfadevices_with_options(
        self,
        request: main_models.ListVirtualMFADevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVirtualMFADevicesResponse:
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
            action = 'ListVirtualMFADevices',
            version = '2019-08-15',
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
        request: main_models.ListVirtualMFADevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVirtualMFADevicesResponse:
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
            action = 'ListVirtualMFADevices',
            version = '2019-08-15',
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

    def list_virtual_mfadevices(
        self,
        request: main_models.ListVirtualMFADevicesRequest,
    ) -> main_models.ListVirtualMFADevicesResponse:
        runtime = RuntimeOptions()
        return self.list_virtual_mfadevices_with_options(request, runtime)

    async def list_virtual_mfadevices_async(
        self,
        request: main_models.ListVirtualMFADevicesRequest,
    ) -> main_models.ListVirtualMFADevicesResponse:
        runtime = RuntimeOptions()
        return await self.list_virtual_mfadevices_with_options_async(request, runtime)

    def provision_application_with_options(
        self,
        request: main_models.ProvisionApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ProvisionApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scopes):
            query['Scopes'] = request.scopes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ProvisionApplication',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ProvisionApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def provision_application_with_options_async(
        self,
        request: main_models.ProvisionApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ProvisionApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scopes):
            query['Scopes'] = request.scopes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ProvisionApplication',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ProvisionApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def provision_application(
        self,
        request: main_models.ProvisionApplicationRequest,
    ) -> main_models.ProvisionApplicationResponse:
        runtime = RuntimeOptions()
        return self.provision_application_with_options(request, runtime)

    async def provision_application_async(
        self,
        request: main_models.ProvisionApplicationRequest,
    ) -> main_models.ProvisionApplicationResponse:
        runtime = RuntimeOptions()
        return await self.provision_application_with_options_async(request, runtime)

    def provision_external_application_with_options(
        self,
        request: main_models.ProvisionExternalApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ProvisionExternalApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scopes):
            query['Scopes'] = request.scopes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ProvisionExternalApplication',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ProvisionExternalApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def provision_external_application_with_options_async(
        self,
        request: main_models.ProvisionExternalApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ProvisionExternalApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scopes):
            query['Scopes'] = request.scopes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ProvisionExternalApplication',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ProvisionExternalApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def provision_external_application(
        self,
        request: main_models.ProvisionExternalApplicationRequest,
    ) -> main_models.ProvisionExternalApplicationResponse:
        runtime = RuntimeOptions()
        return self.provision_external_application_with_options(request, runtime)

    async def provision_external_application_async(
        self,
        request: main_models.ProvisionExternalApplicationRequest,
    ) -> main_models.ProvisionExternalApplicationResponse:
        runtime = RuntimeOptions()
        return await self.provision_external_application_with_options_async(request, runtime)

    def remove_client_id_from_oidcprovider_with_options(
        self,
        request: main_models.RemoveClientIdFromOIDCProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveClientIdFromOIDCProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveClientIdFromOIDCProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveClientIdFromOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_client_id_from_oidcprovider_with_options_async(
        self,
        request: main_models.RemoveClientIdFromOIDCProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveClientIdFromOIDCProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveClientIdFromOIDCProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveClientIdFromOIDCProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_client_id_from_oidcprovider(
        self,
        request: main_models.RemoveClientIdFromOIDCProviderRequest,
    ) -> main_models.RemoveClientIdFromOIDCProviderResponse:
        runtime = RuntimeOptions()
        return self.remove_client_id_from_oidcprovider_with_options(request, runtime)

    async def remove_client_id_from_oidcprovider_async(
        self,
        request: main_models.RemoveClientIdFromOIDCProviderRequest,
    ) -> main_models.RemoveClientIdFromOIDCProviderResponse:
        runtime = RuntimeOptions()
        return await self.remove_client_id_from_oidcprovider_with_options_async(request, runtime)

    def remove_fingerprint_from_oidcprovider_with_options(
        self,
        request: main_models.RemoveFingerprintFromOIDCProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveFingerprintFromOIDCProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fingerprint):
            query['Fingerprint'] = request.fingerprint
        if not DaraCore.is_null(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveFingerprintFromOIDCProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveFingerprintFromOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_fingerprint_from_oidcprovider_with_options_async(
        self,
        request: main_models.RemoveFingerprintFromOIDCProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveFingerprintFromOIDCProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fingerprint):
            query['Fingerprint'] = request.fingerprint
        if not DaraCore.is_null(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveFingerprintFromOIDCProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveFingerprintFromOIDCProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_fingerprint_from_oidcprovider(
        self,
        request: main_models.RemoveFingerprintFromOIDCProviderRequest,
    ) -> main_models.RemoveFingerprintFromOIDCProviderResponse:
        runtime = RuntimeOptions()
        return self.remove_fingerprint_from_oidcprovider_with_options(request, runtime)

    async def remove_fingerprint_from_oidcprovider_async(
        self,
        request: main_models.RemoveFingerprintFromOIDCProviderRequest,
    ) -> main_models.RemoveFingerprintFromOIDCProviderResponse:
        runtime = RuntimeOptions()
        return await self.remove_fingerprint_from_oidcprovider_with_options_async(request, runtime)

    def remove_user_from_group_with_options(
        self,
        request: main_models.RemoveUserFromGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserFromGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUserFromGroup',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUserFromGroup',
            version = '2019-08-15',
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

    def restore_access_key_from_recycle_bin_with_options(
        self,
        request: main_models.RestoreAccessKeyFromRecycleBinRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestoreAccessKeyFromRecycleBinResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestoreAccessKeyFromRecycleBin',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestoreAccessKeyFromRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_access_key_from_recycle_bin_with_options_async(
        self,
        request: main_models.RestoreAccessKeyFromRecycleBinRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestoreAccessKeyFromRecycleBinResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestoreAccessKeyFromRecycleBin',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestoreAccessKeyFromRecycleBinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restore_access_key_from_recycle_bin(
        self,
        request: main_models.RestoreAccessKeyFromRecycleBinRequest,
    ) -> main_models.RestoreAccessKeyFromRecycleBinResponse:
        runtime = RuntimeOptions()
        return self.restore_access_key_from_recycle_bin_with_options(request, runtime)

    async def restore_access_key_from_recycle_bin_async(
        self,
        request: main_models.RestoreAccessKeyFromRecycleBinRequest,
    ) -> main_models.RestoreAccessKeyFromRecycleBinResponse:
        runtime = RuntimeOptions()
        return await self.restore_access_key_from_recycle_bin_with_options_async(request, runtime)

    def restore_user_from_recycle_bin_with_options(
        self,
        request: main_models.RestoreUserFromRecycleBinRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestoreUserFromRecycleBinResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestoreUserFromRecycleBin',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestoreUserFromRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_user_from_recycle_bin_with_options_async(
        self,
        request: main_models.RestoreUserFromRecycleBinRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestoreUserFromRecycleBinResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestoreUserFromRecycleBin',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestoreUserFromRecycleBinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restore_user_from_recycle_bin(
        self,
        request: main_models.RestoreUserFromRecycleBinRequest,
    ) -> main_models.RestoreUserFromRecycleBinResponse:
        runtime = RuntimeOptions()
        return self.restore_user_from_recycle_bin_with_options(request, runtime)

    async def restore_user_from_recycle_bin_async(
        self,
        request: main_models.RestoreUserFromRecycleBinRequest,
    ) -> main_models.RestoreUserFromRecycleBinResponse:
        runtime = RuntimeOptions()
        return await self.restore_user_from_recycle_bin_with_options_async(request, runtime)

    def set_default_domain_with_options(
        self,
        request: main_models.SetDefaultDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDefaultDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_domain_name):
            query['DefaultDomainName'] = request.default_domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDefaultDomain',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDefaultDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_default_domain_with_options_async(
        self,
        request: main_models.SetDefaultDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDefaultDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_domain_name):
            query['DefaultDomainName'] = request.default_domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDefaultDomain',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDefaultDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_default_domain(
        self,
        request: main_models.SetDefaultDomainRequest,
    ) -> main_models.SetDefaultDomainResponse:
        runtime = RuntimeOptions()
        return self.set_default_domain_with_options(request, runtime)

    async def set_default_domain_async(
        self,
        request: main_models.SetDefaultDomainRequest,
    ) -> main_models.SetDefaultDomainResponse:
        runtime = RuntimeOptions()
        return await self.set_default_domain_with_options_async(request, runtime)

    def set_password_policy_with_options(
        self,
        request: main_models.SetPasswordPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPasswordPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hard_expire):
            query['HardExpire'] = request.hard_expire
        if not DaraCore.is_null(request.initial_password_age):
            query['InitialPasswordAge'] = request.initial_password_age
        if not DaraCore.is_null(request.intercept_risk_password_on_api):
            query['InterceptRiskPasswordOnApi'] = request.intercept_risk_password_on_api
        if not DaraCore.is_null(request.max_login_attemps):
            query['MaxLoginAttemps'] = request.max_login_attemps
        if not DaraCore.is_null(request.max_password_age):
            query['MaxPasswordAge'] = request.max_password_age
        if not DaraCore.is_null(request.minimum_password_different_character):
            query['MinimumPasswordDifferentCharacter'] = request.minimum_password_different_character
        if not DaraCore.is_null(request.minimum_password_length):
            query['MinimumPasswordLength'] = request.minimum_password_length
        if not DaraCore.is_null(request.password_not_contain_user_name):
            query['PasswordNotContainUserName'] = request.password_not_contain_user_name
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
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.hard_expire):
            query['HardExpire'] = request.hard_expire
        if not DaraCore.is_null(request.initial_password_age):
            query['InitialPasswordAge'] = request.initial_password_age
        if not DaraCore.is_null(request.intercept_risk_password_on_api):
            query['InterceptRiskPasswordOnApi'] = request.intercept_risk_password_on_api
        if not DaraCore.is_null(request.max_login_attemps):
            query['MaxLoginAttemps'] = request.max_login_attemps
        if not DaraCore.is_null(request.max_password_age):
            query['MaxPasswordAge'] = request.max_password_age
        if not DaraCore.is_null(request.minimum_password_different_character):
            query['MinimumPasswordDifferentCharacter'] = request.minimum_password_different_character
        if not DaraCore.is_null(request.minimum_password_length):
            query['MinimumPasswordLength'] = request.minimum_password_length
        if not DaraCore.is_null(request.password_not_contain_user_name):
            query['PasswordNotContainUserName'] = request.password_not_contain_user_name
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
            version = '2019-08-15',
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
        tmp_req: main_models.SetSecurityPreferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSecurityPreferenceResponse:
        tmp_req.validate()
        request = main_models.SetSecurityPreferenceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.verification_types):
            request.verification_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.verification_types, 'VerificationTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.allow_user_to_change_password):
            query['AllowUserToChangePassword'] = request.allow_user_to_change_password
        if not DaraCore.is_null(request.allow_user_to_login_with_passkey):
            query['AllowUserToLoginWithPasskey'] = request.allow_user_to_login_with_passkey
        if not DaraCore.is_null(request.allow_user_to_manage_access_keys):
            query['AllowUserToManageAccessKeys'] = request.allow_user_to_manage_access_keys
        if not DaraCore.is_null(request.allow_user_to_manage_mfadevices):
            query['AllowUserToManageMFADevices'] = request.allow_user_to_manage_mfadevices
        if not DaraCore.is_null(request.allow_user_to_manage_personal_ding_talk):
            query['AllowUserToManagePersonalDingTalk'] = request.allow_user_to_manage_personal_ding_talk
        if not DaraCore.is_null(request.enable_save_mfaticket):
            query['EnableSaveMFATicket'] = request.enable_save_mfaticket
        if not DaraCore.is_null(request.login_network_masks):
            query['LoginNetworkMasks'] = request.login_network_masks
        if not DaraCore.is_null(request.login_session_duration):
            query['LoginSessionDuration'] = request.login_session_duration
        if not DaraCore.is_null(request.mfaoperation_for_login):
            query['MFAOperationForLogin'] = request.mfaoperation_for_login
        if not DaraCore.is_null(request.max_idle_days_for_access_keys):
            query['MaxIdleDaysForAccessKeys'] = request.max_idle_days_for_access_keys
        if not DaraCore.is_null(request.max_idle_days_for_users):
            query['MaxIdleDaysForUsers'] = request.max_idle_days_for_users
        if not DaraCore.is_null(request.operation_for_risk_login):
            query['OperationForRiskLogin'] = request.operation_for_risk_login
        if not DaraCore.is_null(request.verification_types_shrink):
            query['VerificationTypes'] = request.verification_types_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetSecurityPreference',
            version = '2019-08-15',
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
        tmp_req: main_models.SetSecurityPreferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSecurityPreferenceResponse:
        tmp_req.validate()
        request = main_models.SetSecurityPreferenceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.verification_types):
            request.verification_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.verification_types, 'VerificationTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.allow_user_to_change_password):
            query['AllowUserToChangePassword'] = request.allow_user_to_change_password
        if not DaraCore.is_null(request.allow_user_to_login_with_passkey):
            query['AllowUserToLoginWithPasskey'] = request.allow_user_to_login_with_passkey
        if not DaraCore.is_null(request.allow_user_to_manage_access_keys):
            query['AllowUserToManageAccessKeys'] = request.allow_user_to_manage_access_keys
        if not DaraCore.is_null(request.allow_user_to_manage_mfadevices):
            query['AllowUserToManageMFADevices'] = request.allow_user_to_manage_mfadevices
        if not DaraCore.is_null(request.allow_user_to_manage_personal_ding_talk):
            query['AllowUserToManagePersonalDingTalk'] = request.allow_user_to_manage_personal_ding_talk
        if not DaraCore.is_null(request.enable_save_mfaticket):
            query['EnableSaveMFATicket'] = request.enable_save_mfaticket
        if not DaraCore.is_null(request.login_network_masks):
            query['LoginNetworkMasks'] = request.login_network_masks
        if not DaraCore.is_null(request.login_session_duration):
            query['LoginSessionDuration'] = request.login_session_duration
        if not DaraCore.is_null(request.mfaoperation_for_login):
            query['MFAOperationForLogin'] = request.mfaoperation_for_login
        if not DaraCore.is_null(request.max_idle_days_for_access_keys):
            query['MaxIdleDaysForAccessKeys'] = request.max_idle_days_for_access_keys
        if not DaraCore.is_null(request.max_idle_days_for_users):
            query['MaxIdleDaysForUsers'] = request.max_idle_days_for_users
        if not DaraCore.is_null(request.operation_for_risk_login):
            query['OperationForRiskLogin'] = request.operation_for_risk_login
        if not DaraCore.is_null(request.verification_types_shrink):
            query['VerificationTypes'] = request.verification_types_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetSecurityPreference',
            version = '2019-08-15',
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

    def set_user_sso_settings_with_options(
        self,
        request: main_models.SetUserSsoSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetUserSsoSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authn_sign_algo):
            query['AuthnSignAlgo'] = request.authn_sign_algo
        if not DaraCore.is_null(request.auxiliary_domain):
            query['AuxiliaryDomain'] = request.auxiliary_domain
        if not DaraCore.is_null(request.metadata_document):
            query['MetadataDocument'] = request.metadata_document
        if not DaraCore.is_null(request.sso_enabled):
            query['SsoEnabled'] = request.sso_enabled
        if not DaraCore.is_null(request.sso_login_with_domain):
            query['SsoLoginWithDomain'] = request.sso_login_with_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetUserSsoSettings',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetUserSsoSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_user_sso_settings_with_options_async(
        self,
        request: main_models.SetUserSsoSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetUserSsoSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authn_sign_algo):
            query['AuthnSignAlgo'] = request.authn_sign_algo
        if not DaraCore.is_null(request.auxiliary_domain):
            query['AuxiliaryDomain'] = request.auxiliary_domain
        if not DaraCore.is_null(request.metadata_document):
            query['MetadataDocument'] = request.metadata_document
        if not DaraCore.is_null(request.sso_enabled):
            query['SsoEnabled'] = request.sso_enabled
        if not DaraCore.is_null(request.sso_login_with_domain):
            query['SsoLoginWithDomain'] = request.sso_login_with_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetUserSsoSettings',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetUserSsoSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_user_sso_settings(
        self,
        request: main_models.SetUserSsoSettingsRequest,
    ) -> main_models.SetUserSsoSettingsResponse:
        runtime = RuntimeOptions()
        return self.set_user_sso_settings_with_options(request, runtime)

    async def set_user_sso_settings_async(
        self,
        request: main_models.SetUserSsoSettingsRequest,
    ) -> main_models.SetUserSsoSettingsResponse:
        runtime = RuntimeOptions()
        return await self.set_user_sso_settings_with_options_async(request, runtime)

    def set_verification_info_with_options(
        self,
        request: main_models.SetVerificationInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetVerificationInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.mobile_phone):
            query['MobilePhone'] = request.mobile_phone
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        if not DaraCore.is_null(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetVerificationInfo',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetVerificationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_verification_info_with_options_async(
        self,
        request: main_models.SetVerificationInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetVerificationInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.mobile_phone):
            query['MobilePhone'] = request.mobile_phone
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        if not DaraCore.is_null(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetVerificationInfo',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetVerificationInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_verification_info(
        self,
        request: main_models.SetVerificationInfoRequest,
    ) -> main_models.SetVerificationInfoResponse:
        runtime = RuntimeOptions()
        return self.set_verification_info_with_options(request, runtime)

    async def set_verification_info_async(
        self,
        request: main_models.SetVerificationInfoRequest,
    ) -> main_models.SetVerificationInfoResponse:
        runtime = RuntimeOptions()
        return await self.set_verification_info_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_principal_name):
            query['ResourcePrincipalName'] = request.resource_principal_name
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.resource_principal_name):
            query['ResourcePrincipalName'] = request.resource_principal_name
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindMFADevice',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindMFADevice',
            version = '2019-08-15',
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

    def unbind_verification_with_options(
        self,
        request: main_models.UnbindVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.mobile_phone):
            query['MobilePhone'] = request.mobile_phone
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        if not DaraCore.is_null(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindVerification',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_verification_with_options_async(
        self,
        request: main_models.UnbindVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.mobile_phone):
            query['MobilePhone'] = request.mobile_phone
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        if not DaraCore.is_null(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindVerification',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_verification(
        self,
        request: main_models.UnbindVerificationRequest,
    ) -> main_models.UnbindVerificationResponse:
        runtime = RuntimeOptions()
        return self.unbind_verification_with_options(request, runtime)

    async def unbind_verification_async(
        self,
        request: main_models.UnbindVerificationRequest,
    ) -> main_models.UnbindVerificationResponse:
        runtime = RuntimeOptions()
        return await self.unbind_verification_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.resource_principal_name):
            query['ResourcePrincipalName'] = request.resource_principal_name
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.resource_principal_name):
            query['ResourcePrincipalName'] = request.resource_principal_name
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccessKey',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccessKey',
            version = '2019-08-15',
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

    def update_application_with_options(
        self,
        request: main_models.UpdateApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.new_access_token_validity):
            query['NewAccessTokenValidity'] = request.new_access_token_validity
        if not DaraCore.is_null(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not DaraCore.is_null(request.new_is_multi_tenant):
            query['NewIsMultiTenant'] = request.new_is_multi_tenant
        if not DaraCore.is_null(request.new_predefined_scopes):
            query['NewPredefinedScopes'] = request.new_predefined_scopes
        if not DaraCore.is_null(request.new_redirect_uris):
            query['NewRedirectUris'] = request.new_redirect_uris
        if not DaraCore.is_null(request.new_refresh_token_validity):
            query['NewRefreshTokenValidity'] = request.new_refresh_token_validity
        if not DaraCore.is_null(request.new_required_scopes):
            query['NewRequiredScopes'] = request.new_required_scopes
        if not DaraCore.is_null(request.new_secret_required):
            query['NewSecretRequired'] = request.new_secret_required
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplication',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_with_options_async(
        self,
        request: main_models.UpdateApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.new_access_token_validity):
            query['NewAccessTokenValidity'] = request.new_access_token_validity
        if not DaraCore.is_null(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not DaraCore.is_null(request.new_is_multi_tenant):
            query['NewIsMultiTenant'] = request.new_is_multi_tenant
        if not DaraCore.is_null(request.new_predefined_scopes):
            query['NewPredefinedScopes'] = request.new_predefined_scopes
        if not DaraCore.is_null(request.new_redirect_uris):
            query['NewRedirectUris'] = request.new_redirect_uris
        if not DaraCore.is_null(request.new_refresh_token_validity):
            query['NewRefreshTokenValidity'] = request.new_refresh_token_validity
        if not DaraCore.is_null(request.new_required_scopes):
            query['NewRequiredScopes'] = request.new_required_scopes
        if not DaraCore.is_null(request.new_secret_required):
            query['NewSecretRequired'] = request.new_secret_required
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplication',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application(
        self,
        request: main_models.UpdateApplicationRequest,
    ) -> main_models.UpdateApplicationResponse:
        runtime = RuntimeOptions()
        return self.update_application_with_options(request, runtime)

    async def update_application_async(
        self,
        request: main_models.UpdateApplicationRequest,
    ) -> main_models.UpdateApplicationResponse:
        runtime = RuntimeOptions()
        return await self.update_application_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not DaraCore.is_null(request.new_group_name):
            query['NewGroupName'] = request.new_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGroup',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not DaraCore.is_null(request.new_group_name):
            query['NewGroupName'] = request.new_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGroup',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoginProfile',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoginProfile',
            version = '2019-08-15',
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

    def update_oidcprovider_with_options(
        self,
        request: main_models.UpdateOIDCProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOIDCProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_ids):
            query['ClientIds'] = request.client_ids
        if not DaraCore.is_null(request.issuance_limit_time):
            query['IssuanceLimitTime'] = request.issuance_limit_time
        if not DaraCore.is_null(request.new_description):
            query['NewDescription'] = request.new_description
        if not DaraCore.is_null(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOIDCProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_oidcprovider_with_options_async(
        self,
        request: main_models.UpdateOIDCProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOIDCProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_ids):
            query['ClientIds'] = request.client_ids
        if not DaraCore.is_null(request.issuance_limit_time):
            query['IssuanceLimitTime'] = request.issuance_limit_time
        if not DaraCore.is_null(request.new_description):
            query['NewDescription'] = request.new_description
        if not DaraCore.is_null(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOIDCProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOIDCProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_oidcprovider(
        self,
        request: main_models.UpdateOIDCProviderRequest,
    ) -> main_models.UpdateOIDCProviderResponse:
        runtime = RuntimeOptions()
        return self.update_oidcprovider_with_options(request, runtime)

    async def update_oidcprovider_async(
        self,
        request: main_models.UpdateOIDCProviderRequest,
    ) -> main_models.UpdateOIDCProviderResponse:
        runtime = RuntimeOptions()
        return await self.update_oidcprovider_with_options_async(request, runtime)

    def update_passkey_with_options(
        self,
        request: main_models.UpdatePasskeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePasskeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.passkey_id):
            query['PasskeyId'] = request.passkey_id
        if not DaraCore.is_null(request.passkey_name):
            query['PasskeyName'] = request.passkey_name
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePasskey',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePasskeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_passkey_with_options_async(
        self,
        request: main_models.UpdatePasskeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePasskeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.passkey_id):
            query['PasskeyId'] = request.passkey_id
        if not DaraCore.is_null(request.passkey_name):
            query['PasskeyName'] = request.passkey_name
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePasskey',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePasskeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_passkey(
        self,
        request: main_models.UpdatePasskeyRequest,
    ) -> main_models.UpdatePasskeyResponse:
        runtime = RuntimeOptions()
        return self.update_passkey_with_options(request, runtime)

    async def update_passkey_async(
        self,
        request: main_models.UpdatePasskeyRequest,
    ) -> main_models.UpdatePasskeyResponse:
        runtime = RuntimeOptions()
        return await self.update_passkey_with_options_async(request, runtime)

    def update_samlprovider_with_options(
        self,
        request: main_models.UpdateSAMLProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSAMLProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authn_sign_algo):
            query['AuthnSignAlgo'] = request.authn_sign_algo
        if not DaraCore.is_null(request.new_description):
            query['NewDescription'] = request.new_description
        if not DaraCore.is_null(request.new_encoded_samlmetadata_document):
            query['NewEncodedSAMLMetadataDocument'] = request.new_encoded_samlmetadata_document
        if not DaraCore.is_null(request.samlprovider_name):
            query['SAMLProviderName'] = request.samlprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSAMLProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSAMLProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_samlprovider_with_options_async(
        self,
        request: main_models.UpdateSAMLProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSAMLProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authn_sign_algo):
            query['AuthnSignAlgo'] = request.authn_sign_algo
        if not DaraCore.is_null(request.new_description):
            query['NewDescription'] = request.new_description
        if not DaraCore.is_null(request.new_encoded_samlmetadata_document):
            query['NewEncodedSAMLMetadataDocument'] = request.new_encoded_samlmetadata_document
        if not DaraCore.is_null(request.samlprovider_name):
            query['SAMLProviderName'] = request.samlprovider_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSAMLProvider',
            version = '2019-08-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSAMLProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_samlprovider(
        self,
        request: main_models.UpdateSAMLProviderRequest,
    ) -> main_models.UpdateSAMLProviderResponse:
        runtime = RuntimeOptions()
        return self.update_samlprovider_with_options(request, runtime)

    async def update_samlprovider_async(
        self,
        request: main_models.UpdateSAMLProviderRequest,
    ) -> main_models.UpdateSAMLProviderResponse:
        runtime = RuntimeOptions()
        return await self.update_samlprovider_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.new_user_principal_name):
            query['NewUserPrincipalName'] = request.new_user_principal_name
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2019-08-15',
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
        if not DaraCore.is_null(request.new_user_principal_name):
            query['NewUserPrincipalName'] = request.new_user_principal_name
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2019-08-15',
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
