# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ims20190815 import models as ims_20190815_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_client_id_to_oidcprovider_with_options(
        self,
        request: ims_20190815_models.AddClientIdToOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.AddClientIdToOIDCProviderResponse:
        """
        @summary Adds a client ID to an OpenID Connect (OIDC) identity provider (IdP).
        
        @param request: AddClientIdToOIDCProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddClientIdToOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddClientIdToOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.AddClientIdToOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_client_id_to_oidcprovider_with_options_async(
        self,
        request: ims_20190815_models.AddClientIdToOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.AddClientIdToOIDCProviderResponse:
        """
        @summary Adds a client ID to an OpenID Connect (OIDC) identity provider (IdP).
        
        @param request: AddClientIdToOIDCProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddClientIdToOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddClientIdToOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.AddClientIdToOIDCProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_client_id_to_oidcprovider(
        self,
        request: ims_20190815_models.AddClientIdToOIDCProviderRequest,
    ) -> ims_20190815_models.AddClientIdToOIDCProviderResponse:
        """
        @summary Adds a client ID to an OpenID Connect (OIDC) identity provider (IdP).
        
        @param request: AddClientIdToOIDCProviderRequest
        @return: AddClientIdToOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_client_id_to_oidcprovider_with_options(request, runtime)

    async def add_client_id_to_oidcprovider_async(
        self,
        request: ims_20190815_models.AddClientIdToOIDCProviderRequest,
    ) -> ims_20190815_models.AddClientIdToOIDCProviderResponse:
        """
        @summary Adds a client ID to an OpenID Connect (OIDC) identity provider (IdP).
        
        @param request: AddClientIdToOIDCProviderRequest
        @return: AddClientIdToOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_client_id_to_oidcprovider_with_options_async(request, runtime)

    def add_fingerprint_to_oidcprovider_with_options(
        self,
        request: ims_20190815_models.AddFingerprintToOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.AddFingerprintToOIDCProviderResponse:
        """
        @summary Adds a fingerprint to an OpenID Connect (OIDC) identity provider (IdP).
        
        @description ###
        This topic provides an example on how to add the fingerprint `902ef2deeb3c5b13ea4c3d5193629309e231***` to the OIDC IdP named `TestOIDCProvider`.
        
        @param request: AddFingerprintToOIDCProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddFingerprintToOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fingerprint):
            query['Fingerprint'] = request.fingerprint
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFingerprintToOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.AddFingerprintToOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_fingerprint_to_oidcprovider_with_options_async(
        self,
        request: ims_20190815_models.AddFingerprintToOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.AddFingerprintToOIDCProviderResponse:
        """
        @summary Adds a fingerprint to an OpenID Connect (OIDC) identity provider (IdP).
        
        @description ###
        This topic provides an example on how to add the fingerprint `902ef2deeb3c5b13ea4c3d5193629309e231***` to the OIDC IdP named `TestOIDCProvider`.
        
        @param request: AddFingerprintToOIDCProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddFingerprintToOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fingerprint):
            query['Fingerprint'] = request.fingerprint
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFingerprintToOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.AddFingerprintToOIDCProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_fingerprint_to_oidcprovider(
        self,
        request: ims_20190815_models.AddFingerprintToOIDCProviderRequest,
    ) -> ims_20190815_models.AddFingerprintToOIDCProviderResponse:
        """
        @summary Adds a fingerprint to an OpenID Connect (OIDC) identity provider (IdP).
        
        @description ###
        This topic provides an example on how to add the fingerprint `902ef2deeb3c5b13ea4c3d5193629309e231***` to the OIDC IdP named `TestOIDCProvider`.
        
        @param request: AddFingerprintToOIDCProviderRequest
        @return: AddFingerprintToOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_fingerprint_to_oidcprovider_with_options(request, runtime)

    async def add_fingerprint_to_oidcprovider_async(
        self,
        request: ims_20190815_models.AddFingerprintToOIDCProviderRequest,
    ) -> ims_20190815_models.AddFingerprintToOIDCProviderResponse:
        """
        @summary Adds a fingerprint to an OpenID Connect (OIDC) identity provider (IdP).
        
        @description ###
        This topic provides an example on how to add the fingerprint `902ef2deeb3c5b13ea4c3d5193629309e231***` to the OIDC IdP named `TestOIDCProvider`.
        
        @param request: AddFingerprintToOIDCProviderRequest
        @return: AddFingerprintToOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_fingerprint_to_oidcprovider_with_options_async(request, runtime)

    def add_user_to_group_with_options(
        self,
        request: ims_20190815_models.AddUserToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.AddUserToGroupResponse:
        """
        @summary Adds a Resource Access Management (RAM) user to a RAM user group.
        
        @param request: AddUserToGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserToGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserToGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.AddUserToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_to_group_with_options_async(
        self,
        request: ims_20190815_models.AddUserToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.AddUserToGroupResponse:
        """
        @summary Adds a Resource Access Management (RAM) user to a RAM user group.
        
        @param request: AddUserToGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserToGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserToGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.AddUserToGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_to_group(
        self,
        request: ims_20190815_models.AddUserToGroupRequest,
    ) -> ims_20190815_models.AddUserToGroupResponse:
        """
        @summary Adds a Resource Access Management (RAM) user to a RAM user group.
        
        @param request: AddUserToGroupRequest
        @return: AddUserToGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_group_with_options(request, runtime)

    async def add_user_to_group_async(
        self,
        request: ims_20190815_models.AddUserToGroupRequest,
    ) -> ims_20190815_models.AddUserToGroupResponse:
        """
        @summary Adds a Resource Access Management (RAM) user to a RAM user group.
        
        @param request: AddUserToGroupRequest
        @return: AddUserToGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_user_to_group_with_options_async(request, runtime)

    def bind_mfadevice_with_options(
        self,
        request: ims_20190815_models.BindMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.BindMFADeviceResponse:
        """
        @summary Binds a multi-factor authentication (MFA) device to a Resource Access Management (RAM) user.
        
        @param request: BindMFADeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindMFADeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authentication_code_1):
            query['AuthenticationCode1'] = request.authentication_code_1
        if not UtilClient.is_unset(request.authentication_code_2):
            query['AuthenticationCode2'] = request.authentication_code_2
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindMFADevice',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.BindMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_mfadevice_with_options_async(
        self,
        request: ims_20190815_models.BindMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.BindMFADeviceResponse:
        """
        @summary Binds a multi-factor authentication (MFA) device to a Resource Access Management (RAM) user.
        
        @param request: BindMFADeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindMFADeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authentication_code_1):
            query['AuthenticationCode1'] = request.authentication_code_1
        if not UtilClient.is_unset(request.authentication_code_2):
            query['AuthenticationCode2'] = request.authentication_code_2
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindMFADevice',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.BindMFADeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_mfadevice(
        self,
        request: ims_20190815_models.BindMFADeviceRequest,
    ) -> ims_20190815_models.BindMFADeviceResponse:
        """
        @summary Binds a multi-factor authentication (MFA) device to a Resource Access Management (RAM) user.
        
        @param request: BindMFADeviceRequest
        @return: BindMFADeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_mfadevice_with_options(request, runtime)

    async def bind_mfadevice_async(
        self,
        request: ims_20190815_models.BindMFADeviceRequest,
    ) -> ims_20190815_models.BindMFADeviceResponse:
        """
        @summary Binds a multi-factor authentication (MFA) device to a Resource Access Management (RAM) user.
        
        @param request: BindMFADeviceRequest
        @return: BindMFADeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_mfadevice_with_options_async(request, runtime)

    def change_password_with_options(
        self,
        request: ims_20190815_models.ChangePasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ChangePasswordResponse:
        """
        @summary Changes the password that is used to log on to the console for a Resource Access Management (RAM) user.
        
        @description >  This operation is available only for RAM users. Before you call this operation, make sure that `AllowUserToChangePassword` in [SetSecurityPreference](https://help.aliyun.com/document_detail/43765.html) is set to `True`. The value True indicates that RAM users can manage their passwords.
        
        @param request: ChangePasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangePasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_password):
            query['NewPassword'] = request.new_password
        if not UtilClient.is_unset(request.old_password):
            query['OldPassword'] = request.old_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangePassword',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ChangePasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_password_with_options_async(
        self,
        request: ims_20190815_models.ChangePasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ChangePasswordResponse:
        """
        @summary Changes the password that is used to log on to the console for a Resource Access Management (RAM) user.
        
        @description >  This operation is available only for RAM users. Before you call this operation, make sure that `AllowUserToChangePassword` in [SetSecurityPreference](https://help.aliyun.com/document_detail/43765.html) is set to `True`. The value True indicates that RAM users can manage their passwords.
        
        @param request: ChangePasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangePasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_password):
            query['NewPassword'] = request.new_password
        if not UtilClient.is_unset(request.old_password):
            query['OldPassword'] = request.old_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangePassword',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ChangePasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_password(
        self,
        request: ims_20190815_models.ChangePasswordRequest,
    ) -> ims_20190815_models.ChangePasswordResponse:
        """
        @summary Changes the password that is used to log on to the console for a Resource Access Management (RAM) user.
        
        @description >  This operation is available only for RAM users. Before you call this operation, make sure that `AllowUserToChangePassword` in [SetSecurityPreference](https://help.aliyun.com/document_detail/43765.html) is set to `True`. The value True indicates that RAM users can manage their passwords.
        
        @param request: ChangePasswordRequest
        @return: ChangePasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_password_with_options(request, runtime)

    async def change_password_async(
        self,
        request: ims_20190815_models.ChangePasswordRequest,
    ) -> ims_20190815_models.ChangePasswordResponse:
        """
        @summary Changes the password that is used to log on to the console for a Resource Access Management (RAM) user.
        
        @description >  This operation is available only for RAM users. Before you call this operation, make sure that `AllowUserToChangePassword` in [SetSecurityPreference](https://help.aliyun.com/document_detail/43765.html) is set to `True`. The value True indicates that RAM users can manage their passwords.
        
        @param request: ChangePasswordRequest
        @return: ChangePasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_password_with_options_async(request, runtime)

    def create_access_key_with_options(
        self,
        request: ims_20190815_models.CreateAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateAccessKeyResponse:
        """
        @summary Creates an AccessKey pair for an Alibaba Cloud account or a Resource Access Management (RAM) user.
        
        @param request: CreateAccessKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccessKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessKey',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateAccessKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_key_with_options_async(
        self,
        request: ims_20190815_models.CreateAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateAccessKeyResponse:
        """
        @summary Creates an AccessKey pair for an Alibaba Cloud account or a Resource Access Management (RAM) user.
        
        @param request: CreateAccessKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccessKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessKey',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateAccessKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_key(
        self,
        request: ims_20190815_models.CreateAccessKeyRequest,
    ) -> ims_20190815_models.CreateAccessKeyResponse:
        """
        @summary Creates an AccessKey pair for an Alibaba Cloud account or a Resource Access Management (RAM) user.
        
        @param request: CreateAccessKeyRequest
        @return: CreateAccessKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_access_key_with_options(request, runtime)

    async def create_access_key_async(
        self,
        request: ims_20190815_models.CreateAccessKeyRequest,
    ) -> ims_20190815_models.CreateAccessKeyResponse:
        """
        @summary Creates an AccessKey pair for an Alibaba Cloud account or a Resource Access Management (RAM) user.
        
        @param request: CreateAccessKeyRequest
        @return: CreateAccessKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_access_key_with_options_async(request, runtime)

    def create_app_secret_with_options(
        self,
        request: ims_20190815_models.CreateAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateAppSecretResponse:
        """
        @summary Creates an application secret for an application.
        
        @param request: CreateAppSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppSecret',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateAppSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_secret_with_options_async(
        self,
        request: ims_20190815_models.CreateAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateAppSecretResponse:
        """
        @summary Creates an application secret for an application.
        
        @param request: CreateAppSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppSecret',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateAppSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_secret(
        self,
        request: ims_20190815_models.CreateAppSecretRequest,
    ) -> ims_20190815_models.CreateAppSecretResponse:
        """
        @summary Creates an application secret for an application.
        
        @param request: CreateAppSecretRequest
        @return: CreateAppSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_secret_with_options(request, runtime)

    async def create_app_secret_async(
        self,
        request: ims_20190815_models.CreateAppSecretRequest,
    ) -> ims_20190815_models.CreateAppSecretResponse:
        """
        @summary Creates an application secret for an application.
        
        @param request: CreateAppSecretRequest
        @return: CreateAppSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_secret_with_options_async(request, runtime)

    def create_application_with_options(
        self,
        request: ims_20190815_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateApplicationResponse:
        """
        @summary Creates an application.
        
        @param request: CreateApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token_validity):
            query['AccessTokenValidity'] = request.access_token_validity
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.is_multi_tenant):
            query['IsMultiTenant'] = request.is_multi_tenant
        if not UtilClient.is_unset(request.predefined_scopes):
            query['PredefinedScopes'] = request.predefined_scopes
        if not UtilClient.is_unset(request.protocol_version):
            query['ProtocolVersion'] = request.protocol_version
        if not UtilClient.is_unset(request.redirect_uris):
            query['RedirectUris'] = request.redirect_uris
        if not UtilClient.is_unset(request.refresh_token_validity):
            query['RefreshTokenValidity'] = request.refresh_token_validity
        if not UtilClient.is_unset(request.required_scopes):
            query['RequiredScopes'] = request.required_scopes
        if not UtilClient.is_unset(request.secret_required):
            query['SecretRequired'] = request.secret_required
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_with_options_async(
        self,
        request: ims_20190815_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateApplicationResponse:
        """
        @summary Creates an application.
        
        @param request: CreateApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token_validity):
            query['AccessTokenValidity'] = request.access_token_validity
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.is_multi_tenant):
            query['IsMultiTenant'] = request.is_multi_tenant
        if not UtilClient.is_unset(request.predefined_scopes):
            query['PredefinedScopes'] = request.predefined_scopes
        if not UtilClient.is_unset(request.protocol_version):
            query['ProtocolVersion'] = request.protocol_version
        if not UtilClient.is_unset(request.redirect_uris):
            query['RedirectUris'] = request.redirect_uris
        if not UtilClient.is_unset(request.refresh_token_validity):
            query['RefreshTokenValidity'] = request.refresh_token_validity
        if not UtilClient.is_unset(request.required_scopes):
            query['RequiredScopes'] = request.required_scopes
        if not UtilClient.is_unset(request.secret_required):
            query['SecretRequired'] = request.secret_required
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application(
        self,
        request: ims_20190815_models.CreateApplicationRequest,
    ) -> ims_20190815_models.CreateApplicationResponse:
        """
        @summary Creates an application.
        
        @param request: CreateApplicationRequest
        @return: CreateApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    async def create_application_async(
        self,
        request: ims_20190815_models.CreateApplicationRequest,
    ) -> ims_20190815_models.CreateApplicationResponse:
        """
        @summary Creates an application.
        
        @param request: CreateApplicationRequest
        @return: CreateApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_application_with_options_async(request, runtime)

    def create_group_with_options(
        self,
        request: ims_20190815_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateGroupResponse:
        """
        @summary Creates a Resource Access Management (RAM) user group.
        
        @param request: CreateGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comments):
            query['Comments'] = request.comments
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_with_options_async(
        self,
        request: ims_20190815_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateGroupResponse:
        """
        @summary Creates a Resource Access Management (RAM) user group.
        
        @param request: CreateGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comments):
            query['Comments'] = request.comments
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group(
        self,
        request: ims_20190815_models.CreateGroupRequest,
    ) -> ims_20190815_models.CreateGroupResponse:
        """
        @summary Creates a Resource Access Management (RAM) user group.
        
        @param request: CreateGroupRequest
        @return: CreateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    async def create_group_async(
        self,
        request: ims_20190815_models.CreateGroupRequest,
    ) -> ims_20190815_models.CreateGroupResponse:
        """
        @summary Creates a Resource Access Management (RAM) user group.
        
        @param request: CreateGroupRequest
        @return: CreateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_group_with_options_async(request, runtime)

    def create_login_profile_with_options(
        self,
        request: ims_20190815_models.CreateLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateLoginProfileResponse:
        """
        @summary Enables logon to the console for a Resource Access Management (RAM) user.
        
        @param request: CreateLoginProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoginProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mfabind_required):
            query['MFABindRequired'] = request.mfabind_required
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_reset_required):
            query['PasswordResetRequired'] = request.password_reset_required
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoginProfile',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateLoginProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_login_profile_with_options_async(
        self,
        request: ims_20190815_models.CreateLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateLoginProfileResponse:
        """
        @summary Enables logon to the console for a Resource Access Management (RAM) user.
        
        @param request: CreateLoginProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoginProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mfabind_required):
            query['MFABindRequired'] = request.mfabind_required
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_reset_required):
            query['PasswordResetRequired'] = request.password_reset_required
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoginProfile',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateLoginProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_login_profile(
        self,
        request: ims_20190815_models.CreateLoginProfileRequest,
    ) -> ims_20190815_models.CreateLoginProfileResponse:
        """
        @summary Enables logon to the console for a Resource Access Management (RAM) user.
        
        @param request: CreateLoginProfileRequest
        @return: CreateLoginProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_login_profile_with_options(request, runtime)

    async def create_login_profile_async(
        self,
        request: ims_20190815_models.CreateLoginProfileRequest,
    ) -> ims_20190815_models.CreateLoginProfileResponse:
        """
        @summary Enables logon to the console for a Resource Access Management (RAM) user.
        
        @param request: CreateLoginProfileRequest
        @return: CreateLoginProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_login_profile_with_options_async(request, runtime)

    def create_oidcprovider_with_options(
        self,
        request: ims_20190815_models.CreateOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateOIDCProviderResponse:
        """
        @summary Creates an OpenID Connect (OIDC) identity provider (IdP) to configure a trust relationship between Alibaba Cloud and an external IdP. This topic provides an example on how to create an IdP named TestOIDCProvider to configure a trust relationship between the external IdP Okta and Alibaba Cloud.
        
        @description ### [](#)Prerequisites
        Before you call this operation, make sure that the information such as the URL of the issuer, the fingerprints of HTTPS certificate authority (CA) certificates, and the client IDs are obtained from an external IdP, such as Google Workspace or Okta.
        ### [](#)Limits
        You can create a maximum of 100 OIDC IdPs in an Alibaba Cloud account.
        You can add a maximum of 50 client IDs to an OIDC IdP.
        You can add a maximum of five fingerprints to an OIDC IdP.
        ### [](#)Operation description
        This topic provides an example on how to create an IdP named `TestOIDCProvider` to configure a trust relationship between the external IdP and Alibaba Cloud.
        
        @param request: CreateOIDCProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ids):
            query['ClientIds'] = request.client_ids
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.fingerprints):
            query['Fingerprints'] = request.fingerprints
        if not UtilClient.is_unset(request.issuance_limit_time):
            query['IssuanceLimitTime'] = request.issuance_limit_time
        if not UtilClient.is_unset(request.issuer_url):
            query['IssuerUrl'] = request.issuer_url
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_oidcprovider_with_options_async(
        self,
        request: ims_20190815_models.CreateOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateOIDCProviderResponse:
        """
        @summary Creates an OpenID Connect (OIDC) identity provider (IdP) to configure a trust relationship between Alibaba Cloud and an external IdP. This topic provides an example on how to create an IdP named TestOIDCProvider to configure a trust relationship between the external IdP Okta and Alibaba Cloud.
        
        @description ### [](#)Prerequisites
        Before you call this operation, make sure that the information such as the URL of the issuer, the fingerprints of HTTPS certificate authority (CA) certificates, and the client IDs are obtained from an external IdP, such as Google Workspace or Okta.
        ### [](#)Limits
        You can create a maximum of 100 OIDC IdPs in an Alibaba Cloud account.
        You can add a maximum of 50 client IDs to an OIDC IdP.
        You can add a maximum of five fingerprints to an OIDC IdP.
        ### [](#)Operation description
        This topic provides an example on how to create an IdP named `TestOIDCProvider` to configure a trust relationship between the external IdP and Alibaba Cloud.
        
        @param request: CreateOIDCProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ids):
            query['ClientIds'] = request.client_ids
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.fingerprints):
            query['Fingerprints'] = request.fingerprints
        if not UtilClient.is_unset(request.issuance_limit_time):
            query['IssuanceLimitTime'] = request.issuance_limit_time
        if not UtilClient.is_unset(request.issuer_url):
            query['IssuerUrl'] = request.issuer_url
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateOIDCProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_oidcprovider(
        self,
        request: ims_20190815_models.CreateOIDCProviderRequest,
    ) -> ims_20190815_models.CreateOIDCProviderResponse:
        """
        @summary Creates an OpenID Connect (OIDC) identity provider (IdP) to configure a trust relationship between Alibaba Cloud and an external IdP. This topic provides an example on how to create an IdP named TestOIDCProvider to configure a trust relationship between the external IdP Okta and Alibaba Cloud.
        
        @description ### [](#)Prerequisites
        Before you call this operation, make sure that the information such as the URL of the issuer, the fingerprints of HTTPS certificate authority (CA) certificates, and the client IDs are obtained from an external IdP, such as Google Workspace or Okta.
        ### [](#)Limits
        You can create a maximum of 100 OIDC IdPs in an Alibaba Cloud account.
        You can add a maximum of 50 client IDs to an OIDC IdP.
        You can add a maximum of five fingerprints to an OIDC IdP.
        ### [](#)Operation description
        This topic provides an example on how to create an IdP named `TestOIDCProvider` to configure a trust relationship between the external IdP and Alibaba Cloud.
        
        @param request: CreateOIDCProviderRequest
        @return: CreateOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_oidcprovider_with_options(request, runtime)

    async def create_oidcprovider_async(
        self,
        request: ims_20190815_models.CreateOIDCProviderRequest,
    ) -> ims_20190815_models.CreateOIDCProviderResponse:
        """
        @summary Creates an OpenID Connect (OIDC) identity provider (IdP) to configure a trust relationship between Alibaba Cloud and an external IdP. This topic provides an example on how to create an IdP named TestOIDCProvider to configure a trust relationship between the external IdP Okta and Alibaba Cloud.
        
        @description ### [](#)Prerequisites
        Before you call this operation, make sure that the information such as the URL of the issuer, the fingerprints of HTTPS certificate authority (CA) certificates, and the client IDs are obtained from an external IdP, such as Google Workspace or Okta.
        ### [](#)Limits
        You can create a maximum of 100 OIDC IdPs in an Alibaba Cloud account.
        You can add a maximum of 50 client IDs to an OIDC IdP.
        You can add a maximum of five fingerprints to an OIDC IdP.
        ### [](#)Operation description
        This topic provides an example on how to create an IdP named `TestOIDCProvider` to configure a trust relationship between the external IdP and Alibaba Cloud.
        
        @param request: CreateOIDCProviderRequest
        @return: CreateOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_oidcprovider_with_options_async(request, runtime)

    def create_samlprovider_with_options(
        self,
        request: ims_20190815_models.CreateSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateSAMLProviderResponse:
        """
        @summary Creates an identity provider (IdP) for role-based single sign-on (SSO).
        
        @param request: CreateSAMLProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSAMLProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.encoded_samlmetadata_document):
            query['EncodedSAMLMetadataDocument'] = request.encoded_samlmetadata_document
        if not UtilClient.is_unset(request.samlprovider_name):
            query['SAMLProviderName'] = request.samlprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSAMLProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateSAMLProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_samlprovider_with_options_async(
        self,
        request: ims_20190815_models.CreateSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateSAMLProviderResponse:
        """
        @summary Creates an identity provider (IdP) for role-based single sign-on (SSO).
        
        @param request: CreateSAMLProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSAMLProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.encoded_samlmetadata_document):
            query['EncodedSAMLMetadataDocument'] = request.encoded_samlmetadata_document
        if not UtilClient.is_unset(request.samlprovider_name):
            query['SAMLProviderName'] = request.samlprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSAMLProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateSAMLProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_samlprovider(
        self,
        request: ims_20190815_models.CreateSAMLProviderRequest,
    ) -> ims_20190815_models.CreateSAMLProviderResponse:
        """
        @summary Creates an identity provider (IdP) for role-based single sign-on (SSO).
        
        @param request: CreateSAMLProviderRequest
        @return: CreateSAMLProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_samlprovider_with_options(request, runtime)

    async def create_samlprovider_async(
        self,
        request: ims_20190815_models.CreateSAMLProviderRequest,
    ) -> ims_20190815_models.CreateSAMLProviderResponse:
        """
        @summary Creates an identity provider (IdP) for role-based single sign-on (SSO).
        
        @param request: CreateSAMLProviderRequest
        @return: CreateSAMLProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_samlprovider_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: ims_20190815_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateUserResponse:
        """
        @summary Creates a RAM user.
        
        @description This topic provides an example on how to create a RAM user named `test`.
        
        @param request: CreateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comments):
            query['Comments'] = request.comments
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.mobile_phone):
            query['MobilePhone'] = request.mobile_phone
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: ims_20190815_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateUserResponse:
        """
        @summary Creates a RAM user.
        
        @description This topic provides an example on how to create a RAM user named `test`.
        
        @param request: CreateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comments):
            query['Comments'] = request.comments
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.mobile_phone):
            query['MobilePhone'] = request.mobile_phone
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user(
        self,
        request: ims_20190815_models.CreateUserRequest,
    ) -> ims_20190815_models.CreateUserResponse:
        """
        @summary Creates a RAM user.
        
        @description This topic provides an example on how to create a RAM user named `test`.
        
        @param request: CreateUserRequest
        @return: CreateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: ims_20190815_models.CreateUserRequest,
    ) -> ims_20190815_models.CreateUserResponse:
        """
        @summary Creates a RAM user.
        
        @description This topic provides an example on how to create a RAM user named `test`.
        
        @param request: CreateUserRequest
        @return: CreateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def create_virtual_mfadevice_with_options(
        self,
        request: ims_20190815_models.CreateVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateVirtualMFADeviceResponse:
        """
        @summary Creates a virtual multi-factor authentication (MFA) device.
        
        @param request: CreateVirtualMFADeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVirtualMFADeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.virtual_mfadevice_name):
            query['VirtualMFADeviceName'] = request.virtual_mfadevice_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVirtualMFADevice',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateVirtualMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_virtual_mfadevice_with_options_async(
        self,
        request: ims_20190815_models.CreateVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.CreateVirtualMFADeviceResponse:
        """
        @summary Creates a virtual multi-factor authentication (MFA) device.
        
        @param request: CreateVirtualMFADeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVirtualMFADeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.virtual_mfadevice_name):
            query['VirtualMFADeviceName'] = request.virtual_mfadevice_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVirtualMFADevice',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateVirtualMFADeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_virtual_mfadevice(
        self,
        request: ims_20190815_models.CreateVirtualMFADeviceRequest,
    ) -> ims_20190815_models.CreateVirtualMFADeviceResponse:
        """
        @summary Creates a virtual multi-factor authentication (MFA) device.
        
        @param request: CreateVirtualMFADeviceRequest
        @return: CreateVirtualMFADeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_mfadevice_with_options(request, runtime)

    async def create_virtual_mfadevice_async(
        self,
        request: ims_20190815_models.CreateVirtualMFADeviceRequest,
    ) -> ims_20190815_models.CreateVirtualMFADeviceResponse:
        """
        @summary Creates a virtual multi-factor authentication (MFA) device.
        
        @param request: CreateVirtualMFADeviceRequest
        @return: CreateVirtualMFADeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_virtual_mfadevice_with_options_async(request, runtime)

    def delete_access_key_with_options(
        self,
        request: ims_20190815_models.DeleteAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteAccessKeyResponse:
        """
        @summary Deletes an AccessKey pair for an Alibaba Cloud account or a Resource Access Management (RAM) user.
        
        @param request: DeleteAccessKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccessKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessKey',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteAccessKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_key_with_options_async(
        self,
        request: ims_20190815_models.DeleteAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteAccessKeyResponse:
        """
        @summary Deletes an AccessKey pair for an Alibaba Cloud account or a Resource Access Management (RAM) user.
        
        @param request: DeleteAccessKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccessKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessKey',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteAccessKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_key(
        self,
        request: ims_20190815_models.DeleteAccessKeyRequest,
    ) -> ims_20190815_models.DeleteAccessKeyResponse:
        """
        @summary Deletes an AccessKey pair for an Alibaba Cloud account or a Resource Access Management (RAM) user.
        
        @param request: DeleteAccessKeyRequest
        @return: DeleteAccessKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_access_key_with_options(request, runtime)

    async def delete_access_key_async(
        self,
        request: ims_20190815_models.DeleteAccessKeyRequest,
    ) -> ims_20190815_models.DeleteAccessKeyResponse:
        """
        @summary Deletes an AccessKey pair for an Alibaba Cloud account or a Resource Access Management (RAM) user.
        
        @param request: DeleteAccessKeyRequest
        @return: DeleteAccessKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_access_key_with_options_async(request, runtime)

    def delete_access_key_in_recycle_bin_with_options(
        self,
        request: ims_20190815_models.DeleteAccessKeyInRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteAccessKeyInRecycleBinResponse:
        """
        @summary Deletes a specific AccessKey pair that belongs to a Resource Access Management (RAM) user from the recycle bin.
        
        @param request: DeleteAccessKeyInRecycleBinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccessKeyInRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessKeyInRecycleBin',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteAccessKeyInRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_key_in_recycle_bin_with_options_async(
        self,
        request: ims_20190815_models.DeleteAccessKeyInRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteAccessKeyInRecycleBinResponse:
        """
        @summary Deletes a specific AccessKey pair that belongs to a Resource Access Management (RAM) user from the recycle bin.
        
        @param request: DeleteAccessKeyInRecycleBinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccessKeyInRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessKeyInRecycleBin',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteAccessKeyInRecycleBinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_key_in_recycle_bin(
        self,
        request: ims_20190815_models.DeleteAccessKeyInRecycleBinRequest,
    ) -> ims_20190815_models.DeleteAccessKeyInRecycleBinResponse:
        """
        @summary Deletes a specific AccessKey pair that belongs to a Resource Access Management (RAM) user from the recycle bin.
        
        @param request: DeleteAccessKeyInRecycleBinRequest
        @return: DeleteAccessKeyInRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_access_key_in_recycle_bin_with_options(request, runtime)

    async def delete_access_key_in_recycle_bin_async(
        self,
        request: ims_20190815_models.DeleteAccessKeyInRecycleBinRequest,
    ) -> ims_20190815_models.DeleteAccessKeyInRecycleBinResponse:
        """
        @summary Deletes a specific AccessKey pair that belongs to a Resource Access Management (RAM) user from the recycle bin.
        
        @param request: DeleteAccessKeyInRecycleBinRequest
        @return: DeleteAccessKeyInRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_access_key_in_recycle_bin_with_options_async(request, runtime)

    def delete_app_secret_with_options(
        self,
        request: ims_20190815_models.DeleteAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteAppSecretResponse:
        """
        @summary Deletes the application secret of an application.
        
        @param request: DeleteAppSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_secret_id):
            query['AppSecretId'] = request.app_secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppSecret',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteAppSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_secret_with_options_async(
        self,
        request: ims_20190815_models.DeleteAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteAppSecretResponse:
        """
        @summary Deletes the application secret of an application.
        
        @param request: DeleteAppSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_secret_id):
            query['AppSecretId'] = request.app_secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppSecret',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteAppSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_secret(
        self,
        request: ims_20190815_models.DeleteAppSecretRequest,
    ) -> ims_20190815_models.DeleteAppSecretResponse:
        """
        @summary Deletes the application secret of an application.
        
        @param request: DeleteAppSecretRequest
        @return: DeleteAppSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_app_secret_with_options(request, runtime)

    async def delete_app_secret_async(
        self,
        request: ims_20190815_models.DeleteAppSecretRequest,
    ) -> ims_20190815_models.DeleteAppSecretResponse:
        """
        @summary Deletes the application secret of an application.
        
        @param request: DeleteAppSecretRequest
        @return: DeleteAppSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_secret_with_options_async(request, runtime)

    def delete_application_with_options(
        self,
        request: ims_20190815_models.DeleteApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteApplicationResponse:
        """
        @summary Deletes an application.
        
        @param request: DeleteApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_with_options_async(
        self,
        request: ims_20190815_models.DeleteApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteApplicationResponse:
        """
        @summary Deletes an application.
        
        @param request: DeleteApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application(
        self,
        request: ims_20190815_models.DeleteApplicationRequest,
    ) -> ims_20190815_models.DeleteApplicationResponse:
        """
        @summary Deletes an application.
        
        @param request: DeleteApplicationRequest
        @return: DeleteApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_application_with_options(request, runtime)

    async def delete_application_async(
        self,
        request: ims_20190815_models.DeleteApplicationRequest,
    ) -> ims_20190815_models.DeleteApplicationResponse:
        """
        @summary Deletes an application.
        
        @param request: DeleteApplicationRequest
        @return: DeleteApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_application_with_options_async(request, runtime)

    def delete_group_with_options(
        self,
        request: ims_20190815_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteGroupResponse:
        """
        @summary Deletes a Resource Access Management (RAM) user group.
        
        @description Before you delete a RAM user group, make sure that no policies are attached to the group and no RAM users are included in the group.
        
        @param request: DeleteGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        request: ims_20190815_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteGroupResponse:
        """
        @summary Deletes a Resource Access Management (RAM) user group.
        
        @description Before you delete a RAM user group, make sure that no policies are attached to the group and no RAM users are included in the group.
        
        @param request: DeleteGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group(
        self,
        request: ims_20190815_models.DeleteGroupRequest,
    ) -> ims_20190815_models.DeleteGroupResponse:
        """
        @summary Deletes a Resource Access Management (RAM) user group.
        
        @description Before you delete a RAM user group, make sure that no policies are attached to the group and no RAM users are included in the group.
        
        @param request: DeleteGroupRequest
        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    async def delete_group_async(
        self,
        request: ims_20190815_models.DeleteGroupRequest,
    ) -> ims_20190815_models.DeleteGroupResponse:
        """
        @summary Deletes a Resource Access Management (RAM) user group.
        
        @description Before you delete a RAM user group, make sure that no policies are attached to the group and no RAM users are included in the group.
        
        @param request: DeleteGroupRequest
        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_group_with_options_async(request, runtime)

    def delete_login_profile_with_options(
        self,
        request: ims_20190815_models.DeleteLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteLoginProfileResponse:
        """
        @summary Disables logon to the console for a Resource Access Management (RAM) user.
        
        @param request: DeleteLoginProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLoginProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLoginProfile',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteLoginProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_login_profile_with_options_async(
        self,
        request: ims_20190815_models.DeleteLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteLoginProfileResponse:
        """
        @summary Disables logon to the console for a Resource Access Management (RAM) user.
        
        @param request: DeleteLoginProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLoginProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLoginProfile',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteLoginProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_login_profile(
        self,
        request: ims_20190815_models.DeleteLoginProfileRequest,
    ) -> ims_20190815_models.DeleteLoginProfileResponse:
        """
        @summary Disables logon to the console for a Resource Access Management (RAM) user.
        
        @param request: DeleteLoginProfileRequest
        @return: DeleteLoginProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_login_profile_with_options(request, runtime)

    async def delete_login_profile_async(
        self,
        request: ims_20190815_models.DeleteLoginProfileRequest,
    ) -> ims_20190815_models.DeleteLoginProfileResponse:
        """
        @summary Disables logon to the console for a Resource Access Management (RAM) user.
        
        @param request: DeleteLoginProfileRequest
        @return: DeleteLoginProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_login_profile_with_options_async(request, runtime)

    def delete_oidcprovider_with_options(
        self,
        request: ims_20190815_models.DeleteOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteOIDCProviderResponse:
        """
        @summary Deletes an OpenID Connect (OIDC) identity provider (IdP).
        
        @description ###
        This topic provides an example on how to remove the OIDC IdP named `TestOIDCProvider`.
        
        @param request: DeleteOIDCProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_oidcprovider_with_options_async(
        self,
        request: ims_20190815_models.DeleteOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteOIDCProviderResponse:
        """
        @summary Deletes an OpenID Connect (OIDC) identity provider (IdP).
        
        @description ###
        This topic provides an example on how to remove the OIDC IdP named `TestOIDCProvider`.
        
        @param request: DeleteOIDCProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteOIDCProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_oidcprovider(
        self,
        request: ims_20190815_models.DeleteOIDCProviderRequest,
    ) -> ims_20190815_models.DeleteOIDCProviderResponse:
        """
        @summary Deletes an OpenID Connect (OIDC) identity provider (IdP).
        
        @description ###
        This topic provides an example on how to remove the OIDC IdP named `TestOIDCProvider`.
        
        @param request: DeleteOIDCProviderRequest
        @return: DeleteOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_oidcprovider_with_options(request, runtime)

    async def delete_oidcprovider_async(
        self,
        request: ims_20190815_models.DeleteOIDCProviderRequest,
    ) -> ims_20190815_models.DeleteOIDCProviderResponse:
        """
        @summary Deletes an OpenID Connect (OIDC) identity provider (IdP).
        
        @description ###
        This topic provides an example on how to remove the OIDC IdP named `TestOIDCProvider`.
        
        @param request: DeleteOIDCProviderRequest
        @return: DeleteOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_oidcprovider_with_options_async(request, runtime)

    def delete_passkey_with_options(
        self,
        request: ims_20190815_models.DeletePasskeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeletePasskeyResponse:
        """
        @summary Deletes a passkey for a Resource Access Management (RAM) user.
        
        @param request: DeletePasskeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePasskeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.passkey_id):
            query['PasskeyId'] = request.passkey_id
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePasskey',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeletePasskeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_passkey_with_options_async(
        self,
        request: ims_20190815_models.DeletePasskeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeletePasskeyResponse:
        """
        @summary Deletes a passkey for a Resource Access Management (RAM) user.
        
        @param request: DeletePasskeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePasskeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.passkey_id):
            query['PasskeyId'] = request.passkey_id
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePasskey',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeletePasskeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_passkey(
        self,
        request: ims_20190815_models.DeletePasskeyRequest,
    ) -> ims_20190815_models.DeletePasskeyResponse:
        """
        @summary Deletes a passkey for a Resource Access Management (RAM) user.
        
        @param request: DeletePasskeyRequest
        @return: DeletePasskeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_passkey_with_options(request, runtime)

    async def delete_passkey_async(
        self,
        request: ims_20190815_models.DeletePasskeyRequest,
    ) -> ims_20190815_models.DeletePasskeyResponse:
        """
        @summary Deletes a passkey for a Resource Access Management (RAM) user.
        
        @param request: DeletePasskeyRequest
        @return: DeletePasskeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_passkey_with_options_async(request, runtime)

    def delete_samlprovider_with_options(
        self,
        request: ims_20190815_models.DeleteSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteSAMLProviderResponse:
        """
        @summary Deletes an identity provider (IdP) for role-based single sign-on (SSO).
        
        @param request: DeleteSAMLProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSAMLProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.samlprovider_name):
            query['SAMLProviderName'] = request.samlprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSAMLProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteSAMLProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_samlprovider_with_options_async(
        self,
        request: ims_20190815_models.DeleteSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteSAMLProviderResponse:
        """
        @summary Deletes an identity provider (IdP) for role-based single sign-on (SSO).
        
        @param request: DeleteSAMLProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSAMLProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.samlprovider_name):
            query['SAMLProviderName'] = request.samlprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSAMLProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteSAMLProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_samlprovider(
        self,
        request: ims_20190815_models.DeleteSAMLProviderRequest,
    ) -> ims_20190815_models.DeleteSAMLProviderResponse:
        """
        @summary Deletes an identity provider (IdP) for role-based single sign-on (SSO).
        
        @param request: DeleteSAMLProviderRequest
        @return: DeleteSAMLProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_samlprovider_with_options(request, runtime)

    async def delete_samlprovider_async(
        self,
        request: ims_20190815_models.DeleteSAMLProviderRequest,
    ) -> ims_20190815_models.DeleteSAMLProviderResponse:
        """
        @summary Deletes an identity provider (IdP) for role-based single sign-on (SSO).
        
        @param request: DeleteSAMLProviderRequest
        @return: DeleteSAMLProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_samlprovider_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: ims_20190815_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteUserResponse:
        """
        @summary Deletes a Resource Access Management (RAM) user.
        
        @param request: DeleteUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: ims_20190815_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteUserResponse:
        """
        @summary Deletes a Resource Access Management (RAM) user.
        
        @param request: DeleteUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user(
        self,
        request: ims_20190815_models.DeleteUserRequest,
    ) -> ims_20190815_models.DeleteUserResponse:
        """
        @summary Deletes a Resource Access Management (RAM) user.
        
        @param request: DeleteUserRequest
        @return: DeleteUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: ims_20190815_models.DeleteUserRequest,
    ) -> ims_20190815_models.DeleteUserResponse:
        """
        @summary Deletes a Resource Access Management (RAM) user.
        
        @param request: DeleteUserRequest
        @return: DeleteUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def delete_user_in_recycle_bin_with_options(
        self,
        request: ims_20190815_models.DeleteUserInRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteUserInRecycleBinResponse:
        """
        @summary Deletes a specific Resource Access Management (RAM) user from the recycle bin.
        
        @param request: DeleteUserInRecycleBinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserInRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserInRecycleBin',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteUserInRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_in_recycle_bin_with_options_async(
        self,
        request: ims_20190815_models.DeleteUserInRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteUserInRecycleBinResponse:
        """
        @summary Deletes a specific Resource Access Management (RAM) user from the recycle bin.
        
        @param request: DeleteUserInRecycleBinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserInRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserInRecycleBin',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteUserInRecycleBinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_in_recycle_bin(
        self,
        request: ims_20190815_models.DeleteUserInRecycleBinRequest,
    ) -> ims_20190815_models.DeleteUserInRecycleBinResponse:
        """
        @summary Deletes a specific Resource Access Management (RAM) user from the recycle bin.
        
        @param request: DeleteUserInRecycleBinRequest
        @return: DeleteUserInRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_in_recycle_bin_with_options(request, runtime)

    async def delete_user_in_recycle_bin_async(
        self,
        request: ims_20190815_models.DeleteUserInRecycleBinRequest,
    ) -> ims_20190815_models.DeleteUserInRecycleBinResponse:
        """
        @summary Deletes a specific Resource Access Management (RAM) user from the recycle bin.
        
        @param request: DeleteUserInRecycleBinRequest
        @return: DeleteUserInRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_in_recycle_bin_with_options_async(request, runtime)

    def delete_virtual_mfadevice_with_options(
        self,
        request: ims_20190815_models.DeleteVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteVirtualMFADeviceResponse:
        """
        @summary Deletes a multi-factor authentication (MFA) device.
        
        @param request: DeleteVirtualMFADeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVirtualMFADeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVirtualMFADevice',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteVirtualMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_virtual_mfadevice_with_options_async(
        self,
        request: ims_20190815_models.DeleteVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeleteVirtualMFADeviceResponse:
        """
        @summary Deletes a multi-factor authentication (MFA) device.
        
        @param request: DeleteVirtualMFADeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVirtualMFADeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVirtualMFADevice',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteVirtualMFADeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_virtual_mfadevice(
        self,
        request: ims_20190815_models.DeleteVirtualMFADeviceRequest,
    ) -> ims_20190815_models.DeleteVirtualMFADeviceResponse:
        """
        @summary Deletes a multi-factor authentication (MFA) device.
        
        @param request: DeleteVirtualMFADeviceRequest
        @return: DeleteVirtualMFADeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_mfadevice_with_options(request, runtime)

    async def delete_virtual_mfadevice_async(
        self,
        request: ims_20190815_models.DeleteVirtualMFADeviceRequest,
    ) -> ims_20190815_models.DeleteVirtualMFADeviceResponse:
        """
        @summary Deletes a multi-factor authentication (MFA) device.
        
        @param request: DeleteVirtualMFADeviceRequest
        @return: DeleteVirtualMFADeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_virtual_mfadevice_with_options_async(request, runtime)

    def deprovision_application_with_options(
        self,
        request: ims_20190815_models.DeprovisionApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeprovisionApplicationResponse:
        """
        @summary Uninstalls an external application or an internal application of the ServerApp type.
        
        @description If you want to call this operation to uninstall an internal application, the type of the internal application must be *ServerApp**. Otherwise, an error occurs when you call this operation.
        >  For *internal applications**, only internal applications of the ServerApp type need to be **installed or provisioned**. Therefore, only internal applications of the ServerApp type **can be uninstalled**. Internal applications of the WebApp and NativeApp types **do not need to and cannot be uninstalled**.
        
        @param request: DeprovisionApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeprovisionApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeprovisionApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeprovisionApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def deprovision_application_with_options_async(
        self,
        request: ims_20190815_models.DeprovisionApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeprovisionApplicationResponse:
        """
        @summary Uninstalls an external application or an internal application of the ServerApp type.
        
        @description If you want to call this operation to uninstall an internal application, the type of the internal application must be *ServerApp**. Otherwise, an error occurs when you call this operation.
        >  For *internal applications**, only internal applications of the ServerApp type need to be **installed or provisioned**. Therefore, only internal applications of the ServerApp type **can be uninstalled**. Internal applications of the WebApp and NativeApp types **do not need to and cannot be uninstalled**.
        
        @param request: DeprovisionApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeprovisionApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeprovisionApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeprovisionApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deprovision_application(
        self,
        request: ims_20190815_models.DeprovisionApplicationRequest,
    ) -> ims_20190815_models.DeprovisionApplicationResponse:
        """
        @summary Uninstalls an external application or an internal application of the ServerApp type.
        
        @description If you want to call this operation to uninstall an internal application, the type of the internal application must be *ServerApp**. Otherwise, an error occurs when you call this operation.
        >  For *internal applications**, only internal applications of the ServerApp type need to be **installed or provisioned**. Therefore, only internal applications of the ServerApp type **can be uninstalled**. Internal applications of the WebApp and NativeApp types **do not need to and cannot be uninstalled**.
        
        @param request: DeprovisionApplicationRequest
        @return: DeprovisionApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deprovision_application_with_options(request, runtime)

    async def deprovision_application_async(
        self,
        request: ims_20190815_models.DeprovisionApplicationRequest,
    ) -> ims_20190815_models.DeprovisionApplicationResponse:
        """
        @summary Uninstalls an external application or an internal application of the ServerApp type.
        
        @description If you want to call this operation to uninstall an internal application, the type of the internal application must be *ServerApp**. Otherwise, an error occurs when you call this operation.
        >  For *internal applications**, only internal applications of the ServerApp type need to be **installed or provisioned**. Therefore, only internal applications of the ServerApp type **can be uninstalled**. Internal applications of the WebApp and NativeApp types **do not need to and cannot be uninstalled**.
        
        @param request: DeprovisionApplicationRequest
        @return: DeprovisionApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.deprovision_application_with_options_async(request, runtime)

    def deprovision_external_application_with_options(
        self,
        request: ims_20190815_models.DeprovisionExternalApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeprovisionExternalApplicationResponse:
        """
        @summary Deletes an installed external application.
        
        @param request: DeprovisionExternalApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeprovisionExternalApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeprovisionExternalApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeprovisionExternalApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def deprovision_external_application_with_options_async(
        self,
        request: ims_20190815_models.DeprovisionExternalApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DeprovisionExternalApplicationResponse:
        """
        @summary Deletes an installed external application.
        
        @param request: DeprovisionExternalApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeprovisionExternalApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeprovisionExternalApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeprovisionExternalApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deprovision_external_application(
        self,
        request: ims_20190815_models.DeprovisionExternalApplicationRequest,
    ) -> ims_20190815_models.DeprovisionExternalApplicationResponse:
        """
        @summary Deletes an installed external application.
        
        @param request: DeprovisionExternalApplicationRequest
        @return: DeprovisionExternalApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deprovision_external_application_with_options(request, runtime)

    async def deprovision_external_application_async(
        self,
        request: ims_20190815_models.DeprovisionExternalApplicationRequest,
    ) -> ims_20190815_models.DeprovisionExternalApplicationResponse:
        """
        @summary Deletes an installed external application.
        
        @param request: DeprovisionExternalApplicationRequest
        @return: DeprovisionExternalApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.deprovision_external_application_with_options_async(request, runtime)

    def disable_virtual_mfawith_options(
        self,
        request: ims_20190815_models.DisableVirtualMFARequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DisableVirtualMFAResponse:
        """
        @summary Unbinds and deletes a multi-factor authentication (MFA) device from a Resource Access Management (RAM) user.
        
        @param request: DisableVirtualMFARequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableVirtualMFAResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableVirtualMFA',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DisableVirtualMFAResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_virtual_mfawith_options_async(
        self,
        request: ims_20190815_models.DisableVirtualMFARequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.DisableVirtualMFAResponse:
        """
        @summary Unbinds and deletes a multi-factor authentication (MFA) device from a Resource Access Management (RAM) user.
        
        @param request: DisableVirtualMFARequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableVirtualMFAResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableVirtualMFA',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DisableVirtualMFAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_virtual_mfa(
        self,
        request: ims_20190815_models.DisableVirtualMFARequest,
    ) -> ims_20190815_models.DisableVirtualMFAResponse:
        """
        @summary Unbinds and deletes a multi-factor authentication (MFA) device from a Resource Access Management (RAM) user.
        
        @param request: DisableVirtualMFARequest
        @return: DisableVirtualMFAResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_virtual_mfawith_options(request, runtime)

    async def disable_virtual_mfa_async(
        self,
        request: ims_20190815_models.DisableVirtualMFARequest,
    ) -> ims_20190815_models.DisableVirtualMFAResponse:
        """
        @summary Unbinds and deletes a multi-factor authentication (MFA) device from a Resource Access Management (RAM) user.
        
        @param request: DisableVirtualMFARequest
        @return: DisableVirtualMFAResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_virtual_mfawith_options_async(request, runtime)

    def generate_credential_report_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GenerateCredentialReportResponse:
        """
        @summary Generates the user credential report of an Alibaba Cloud account.
        
        @param request: GenerateCredentialReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateCredentialReportResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GenerateCredentialReport',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GenerateCredentialReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_credential_report_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GenerateCredentialReportResponse:
        """
        @summary Generates the user credential report of an Alibaba Cloud account.
        
        @param request: GenerateCredentialReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateCredentialReportResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GenerateCredentialReport',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GenerateCredentialReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_credential_report(self) -> ims_20190815_models.GenerateCredentialReportResponse:
        """
        @summary Generates the user credential report of an Alibaba Cloud account.
        
        @return: GenerateCredentialReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_credential_report_with_options(runtime)

    async def generate_credential_report_async(self) -> ims_20190815_models.GenerateCredentialReportResponse:
        """
        @summary Generates the user credential report of an Alibaba Cloud account.
        
        @return: GenerateCredentialReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_credential_report_with_options_async(runtime)

    def generate_governance_report_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GenerateGovernanceReportResponse:
        """
        @summary Generates a check report for Cloud Governance.
        
        @param request: GenerateGovernanceReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateGovernanceReportResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GenerateGovernanceReport',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GenerateGovernanceReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_governance_report_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GenerateGovernanceReportResponse:
        """
        @summary Generates a check report for Cloud Governance.
        
        @param request: GenerateGovernanceReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateGovernanceReportResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GenerateGovernanceReport',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GenerateGovernanceReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_governance_report(self) -> ims_20190815_models.GenerateGovernanceReportResponse:
        """
        @summary Generates a check report for Cloud Governance.
        
        @return: GenerateGovernanceReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_governance_report_with_options(runtime)

    async def generate_governance_report_async(self) -> ims_20190815_models.GenerateGovernanceReportResponse:
        """
        @summary Generates a check report for Cloud Governance.
        
        @return: GenerateGovernanceReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_governance_report_with_options_async(runtime)

    def get_access_key_info_in_recycle_bin_with_options(
        self,
        request: ims_20190815_models.GetAccessKeyInfoInRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccessKeyInfoInRecycleBinResponse:
        """
        @summary Queries information about a specific AccessKey pair of a Resource Access Management (RAM) user in the recycle bin.
        
        @param request: GetAccessKeyInfoInRecycleBinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccessKeyInfoInRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyInfoInRecycleBin',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAccessKeyInfoInRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_key_info_in_recycle_bin_with_options_async(
        self,
        request: ims_20190815_models.GetAccessKeyInfoInRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccessKeyInfoInRecycleBinResponse:
        """
        @summary Queries information about a specific AccessKey pair of a Resource Access Management (RAM) user in the recycle bin.
        
        @param request: GetAccessKeyInfoInRecycleBinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccessKeyInfoInRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyInfoInRecycleBin',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAccessKeyInfoInRecycleBinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_key_info_in_recycle_bin(
        self,
        request: ims_20190815_models.GetAccessKeyInfoInRecycleBinRequest,
    ) -> ims_20190815_models.GetAccessKeyInfoInRecycleBinResponse:
        """
        @summary Queries information about a specific AccessKey pair of a Resource Access Management (RAM) user in the recycle bin.
        
        @param request: GetAccessKeyInfoInRecycleBinRequest
        @return: GetAccessKeyInfoInRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_access_key_info_in_recycle_bin_with_options(request, runtime)

    async def get_access_key_info_in_recycle_bin_async(
        self,
        request: ims_20190815_models.GetAccessKeyInfoInRecycleBinRequest,
    ) -> ims_20190815_models.GetAccessKeyInfoInRecycleBinResponse:
        """
        @summary Queries information about a specific AccessKey pair of a Resource Access Management (RAM) user in the recycle bin.
        
        @param request: GetAccessKeyInfoInRecycleBinRequest
        @return: GetAccessKeyInfoInRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_access_key_info_in_recycle_bin_with_options_async(request, runtime)

    def get_access_key_last_used_with_options(
        self,
        request: ims_20190815_models.GetAccessKeyLastUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccessKeyLastUsedResponse:
        """
        @summary Queries the time when an AccessKey pair was used for the last time.
        
        @param request: GetAccessKeyLastUsedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccessKeyLastUsedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsed',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAccessKeyLastUsedResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_key_last_used_with_options_async(
        self,
        request: ims_20190815_models.GetAccessKeyLastUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccessKeyLastUsedResponse:
        """
        @summary Queries the time when an AccessKey pair was used for the last time.
        
        @param request: GetAccessKeyLastUsedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccessKeyLastUsedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsed',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAccessKeyLastUsedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_key_last_used(
        self,
        request: ims_20190815_models.GetAccessKeyLastUsedRequest,
    ) -> ims_20190815_models.GetAccessKeyLastUsedResponse:
        """
        @summary Queries the time when an AccessKey pair was used for the last time.
        
        @param request: GetAccessKeyLastUsedRequest
        @return: GetAccessKeyLastUsedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_access_key_last_used_with_options(request, runtime)

    async def get_access_key_last_used_async(
        self,
        request: ims_20190815_models.GetAccessKeyLastUsedRequest,
    ) -> ims_20190815_models.GetAccessKeyLastUsedResponse:
        """
        @summary Queries the time when an AccessKey pair was used for the last time.
        
        @param request: GetAccessKeyLastUsedRequest
        @return: GetAccessKeyLastUsedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_access_key_last_used_with_options_async(request, runtime)

    def get_account_mfainfo_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccountMFAInfoResponse:
        """
        @summary Queries information about the multi-factor authentication (MFA) devices of an Alibaba Cloud account.
        
        @param request: GetAccountMFAInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccountMFAInfoResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAccountMFAInfo',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAccountMFAInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_mfainfo_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccountMFAInfoResponse:
        """
        @summary Queries information about the multi-factor authentication (MFA) devices of an Alibaba Cloud account.
        
        @param request: GetAccountMFAInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccountMFAInfoResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAccountMFAInfo',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAccountMFAInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_mfainfo(self) -> ims_20190815_models.GetAccountMFAInfoResponse:
        """
        @summary Queries information about the multi-factor authentication (MFA) devices of an Alibaba Cloud account.
        
        @return: GetAccountMFAInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_account_mfainfo_with_options(runtime)

    async def get_account_mfainfo_async(self) -> ims_20190815_models.GetAccountMFAInfoResponse:
        """
        @summary Queries information about the multi-factor authentication (MFA) devices of an Alibaba Cloud account.
        
        @return: GetAccountMFAInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_account_mfainfo_with_options_async(runtime)

    def get_account_security_practice_report_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccountSecurityPracticeReportResponse:
        """
        @summary Queries the security report of an Alibaba Cloud account.
        
        @param request: GetAccountSecurityPracticeReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccountSecurityPracticeReportResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAccountSecurityPracticeReport',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAccountSecurityPracticeReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_security_practice_report_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccountSecurityPracticeReportResponse:
        """
        @summary Queries the security report of an Alibaba Cloud account.
        
        @param request: GetAccountSecurityPracticeReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccountSecurityPracticeReportResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAccountSecurityPracticeReport',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAccountSecurityPracticeReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_security_practice_report(self) -> ims_20190815_models.GetAccountSecurityPracticeReportResponse:
        """
        @summary Queries the security report of an Alibaba Cloud account.
        
        @return: GetAccountSecurityPracticeReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_account_security_practice_report_with_options(runtime)

    async def get_account_security_practice_report_async(self) -> ims_20190815_models.GetAccountSecurityPracticeReportResponse:
        """
        @summary Queries the security report of an Alibaba Cloud account.
        
        @return: GetAccountSecurityPracticeReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_account_security_practice_report_with_options_async(runtime)

    def get_account_summary_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccountSummaryResponse:
        """
        @summary Queries the overview information about an Alibaba Cloud account.
        
        @param request: GetAccountSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccountSummaryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAccountSummary',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAccountSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_summary_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAccountSummaryResponse:
        """
        @summary Queries the overview information about an Alibaba Cloud account.
        
        @param request: GetAccountSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccountSummaryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAccountSummary',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAccountSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_summary(self) -> ims_20190815_models.GetAccountSummaryResponse:
        """
        @summary Queries the overview information about an Alibaba Cloud account.
        
        @return: GetAccountSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_account_summary_with_options(runtime)

    async def get_account_summary_async(self) -> ims_20190815_models.GetAccountSummaryResponse:
        """
        @summary Queries the overview information about an Alibaba Cloud account.
        
        @return: GetAccountSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_account_summary_with_options_async(runtime)

    def get_app_secret_with_options(
        self,
        request: ims_20190815_models.GetAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAppSecretResponse:
        """
        @summary Queries the details of an application secret.
        
        @param request: GetAppSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_secret_id):
            query['AppSecretId'] = request.app_secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppSecret',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAppSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_secret_with_options_async(
        self,
        request: ims_20190815_models.GetAppSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetAppSecretResponse:
        """
        @summary Queries the details of an application secret.
        
        @param request: GetAppSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_secret_id):
            query['AppSecretId'] = request.app_secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppSecret',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAppSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_secret(
        self,
        request: ims_20190815_models.GetAppSecretRequest,
    ) -> ims_20190815_models.GetAppSecretResponse:
        """
        @summary Queries the details of an application secret.
        
        @param request: GetAppSecretRequest
        @return: GetAppSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_app_secret_with_options(request, runtime)

    async def get_app_secret_async(
        self,
        request: ims_20190815_models.GetAppSecretRequest,
    ) -> ims_20190815_models.GetAppSecretResponse:
        """
        @summary Queries the details of an application secret.
        
        @param request: GetAppSecretRequest
        @return: GetAppSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_app_secret_with_options_async(request, runtime)

    def get_application_with_options(
        self,
        request: ims_20190815_models.GetApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetApplicationResponse:
        """
        @summary Queries the configuration information about an application.
        
        @description This topic provides an example on how to query the configurations of an application named `472457090344041***`.
        
        @param request: GetApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_with_options_async(
        self,
        request: ims_20190815_models.GetApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetApplicationResponse:
        """
        @summary Queries the configuration information about an application.
        
        @description This topic provides an example on how to query the configurations of an application named `472457090344041***`.
        
        @param request: GetApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application(
        self,
        request: ims_20190815_models.GetApplicationRequest,
    ) -> ims_20190815_models.GetApplicationResponse:
        """
        @summary Queries the configuration information about an application.
        
        @description This topic provides an example on how to query the configurations of an application named `472457090344041***`.
        
        @param request: GetApplicationRequest
        @return: GetApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_application_with_options(request, runtime)

    async def get_application_async(
        self,
        request: ims_20190815_models.GetApplicationRequest,
    ) -> ims_20190815_models.GetApplicationResponse:
        """
        @summary Queries the configuration information about an application.
        
        @description This topic provides an example on how to query the configurations of an application named `472457090344041***`.
        
        @param request: GetApplicationRequest
        @return: GetApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_application_with_options_async(request, runtime)

    def get_application_provision_info_with_options(
        self,
        request: ims_20190815_models.GetApplicationProvisionInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetApplicationProvisionInfoResponse:
        """
        @summary Queries installation information about a specified installed application.
        
        @param request: GetApplicationProvisionInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationProvisionInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationProvisionInfo',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetApplicationProvisionInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_provision_info_with_options_async(
        self,
        request: ims_20190815_models.GetApplicationProvisionInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetApplicationProvisionInfoResponse:
        """
        @summary Queries installation information about a specified installed application.
        
        @param request: GetApplicationProvisionInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationProvisionInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationProvisionInfo',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetApplicationProvisionInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_provision_info(
        self,
        request: ims_20190815_models.GetApplicationProvisionInfoRequest,
    ) -> ims_20190815_models.GetApplicationProvisionInfoResponse:
        """
        @summary Queries installation information about a specified installed application.
        
        @param request: GetApplicationProvisionInfoRequest
        @return: GetApplicationProvisionInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_application_provision_info_with_options(request, runtime)

    async def get_application_provision_info_async(
        self,
        request: ims_20190815_models.GetApplicationProvisionInfoRequest,
    ) -> ims_20190815_models.GetApplicationProvisionInfoResponse:
        """
        @summary Queries installation information about a specified installed application.
        
        @param request: GetApplicationProvisionInfoRequest
        @return: GetApplicationProvisionInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_application_provision_info_with_options_async(request, runtime)

    def get_credential_report_with_options(
        self,
        request: ims_20190815_models.GetCredentialReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetCredentialReportResponse:
        """
        @summary Queries the user credential reports of an Alibaba Cloud account.
        
        @param request: GetCredentialReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCredentialReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCredentialReport',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetCredentialReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_credential_report_with_options_async(
        self,
        request: ims_20190815_models.GetCredentialReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetCredentialReportResponse:
        """
        @summary Queries the user credential reports of an Alibaba Cloud account.
        
        @param request: GetCredentialReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCredentialReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCredentialReport',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetCredentialReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_credential_report(
        self,
        request: ims_20190815_models.GetCredentialReportRequest,
    ) -> ims_20190815_models.GetCredentialReportResponse:
        """
        @summary Queries the user credential reports of an Alibaba Cloud account.
        
        @param request: GetCredentialReportRequest
        @return: GetCredentialReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_credential_report_with_options(request, runtime)

    async def get_credential_report_async(
        self,
        request: ims_20190815_models.GetCredentialReportRequest,
    ) -> ims_20190815_models.GetCredentialReportResponse:
        """
        @summary Queries the user credential reports of an Alibaba Cloud account.
        
        @param request: GetCredentialReportRequest
        @return: GetCredentialReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_credential_report_with_options_async(request, runtime)

    def get_default_domain_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetDefaultDomainResponse:
        """
        @summary Queries the default domain name of an Alibaba Cloud account.
        
        @param request: GetDefaultDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDefaultDomainResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetDefaultDomain',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetDefaultDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_default_domain_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetDefaultDomainResponse:
        """
        @summary Queries the default domain name of an Alibaba Cloud account.
        
        @param request: GetDefaultDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDefaultDomainResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetDefaultDomain',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetDefaultDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_default_domain(self) -> ims_20190815_models.GetDefaultDomainResponse:
        """
        @summary Queries the default domain name of an Alibaba Cloud account.
        
        @return: GetDefaultDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_default_domain_with_options(runtime)

    async def get_default_domain_async(self) -> ims_20190815_models.GetDefaultDomainResponse:
        """
        @summary Queries the default domain name of an Alibaba Cloud account.
        
        @return: GetDefaultDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_default_domain_with_options_async(runtime)

    def get_external_application_with_options(
        self,
        request: ims_20190815_models.GetExternalApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetExternalApplicationResponse:
        """
        @summary Queries information about an installed external application.
        
        @param request: GetExternalApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExternalApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExternalApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetExternalApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_external_application_with_options_async(
        self,
        request: ims_20190815_models.GetExternalApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetExternalApplicationResponse:
        """
        @summary Queries information about an installed external application.
        
        @param request: GetExternalApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExternalApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExternalApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetExternalApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_external_application(
        self,
        request: ims_20190815_models.GetExternalApplicationRequest,
    ) -> ims_20190815_models.GetExternalApplicationResponse:
        """
        @summary Queries information about an installed external application.
        
        @param request: GetExternalApplicationRequest
        @return: GetExternalApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_external_application_with_options(request, runtime)

    async def get_external_application_async(
        self,
        request: ims_20190815_models.GetExternalApplicationRequest,
    ) -> ims_20190815_models.GetExternalApplicationResponse:
        """
        @summary Queries information about an installed external application.
        
        @param request: GetExternalApplicationRequest
        @return: GetExternalApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_external_application_with_options_async(request, runtime)

    def get_governance_item_report_with_options(
        self,
        request: ims_20190815_models.GetGovernanceItemReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetGovernanceItemReportResponse:
        """
        @summary 查询用户的单项ram治理报告
        
        @param request: GetGovernanceItemReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGovernanceItemReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.governance_item_type):
            query['GovernanceItemType'] = request.governance_item_type
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGovernanceItemReport',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetGovernanceItemReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_governance_item_report_with_options_async(
        self,
        request: ims_20190815_models.GetGovernanceItemReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetGovernanceItemReportResponse:
        """
        @summary 查询用户的单项ram治理报告
        
        @param request: GetGovernanceItemReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGovernanceItemReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.governance_item_type):
            query['GovernanceItemType'] = request.governance_item_type
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGovernanceItemReport',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetGovernanceItemReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_governance_item_report(
        self,
        request: ims_20190815_models.GetGovernanceItemReportRequest,
    ) -> ims_20190815_models.GetGovernanceItemReportResponse:
        """
        @summary 查询用户的单项ram治理报告
        
        @param request: GetGovernanceItemReportRequest
        @return: GetGovernanceItemReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_governance_item_report_with_options(request, runtime)

    async def get_governance_item_report_async(
        self,
        request: ims_20190815_models.GetGovernanceItemReportRequest,
    ) -> ims_20190815_models.GetGovernanceItemReportResponse:
        """
        @summary 查询用户的单项ram治理报告
        
        @param request: GetGovernanceItemReportRequest
        @return: GetGovernanceItemReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_governance_item_report_with_options_async(request, runtime)

    def get_governance_report_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetGovernanceReportStatusResponse:
        """
        @summary 查询成熟度报告状态
        
        @param request: GetGovernanceReportStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGovernanceReportStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetGovernanceReportStatus',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetGovernanceReportStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_governance_report_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetGovernanceReportStatusResponse:
        """
        @summary 查询成熟度报告状态
        
        @param request: GetGovernanceReportStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGovernanceReportStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetGovernanceReportStatus',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetGovernanceReportStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_governance_report_status(self) -> ims_20190815_models.GetGovernanceReportStatusResponse:
        """
        @summary 查询成熟度报告状态
        
        @return: GetGovernanceReportStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_governance_report_status_with_options(runtime)

    async def get_governance_report_status_async(self) -> ims_20190815_models.GetGovernanceReportStatusResponse:
        """
        @summary 查询成熟度报告状态
        
        @return: GetGovernanceReportStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_governance_report_status_with_options_async(runtime)

    def get_group_with_options(
        self,
        request: ims_20190815_models.GetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetGroupResponse:
        """
        @summary Queries the information about a Resource Access Management (RAM) user group.
        
        @param request: GetGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_group_with_options_async(
        self,
        request: ims_20190815_models.GetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetGroupResponse:
        """
        @summary Queries the information about a Resource Access Management (RAM) user group.
        
        @param request: GetGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_group(
        self,
        request: ims_20190815_models.GetGroupRequest,
    ) -> ims_20190815_models.GetGroupResponse:
        """
        @summary Queries the information about a Resource Access Management (RAM) user group.
        
        @param request: GetGroupRequest
        @return: GetGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_group_with_options(request, runtime)

    async def get_group_async(
        self,
        request: ims_20190815_models.GetGroupRequest,
    ) -> ims_20190815_models.GetGroupResponse:
        """
        @summary Queries the information about a Resource Access Management (RAM) user group.
        
        @param request: GetGroupRequest
        @return: GetGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_group_with_options_async(request, runtime)

    def get_login_profile_with_options(
        self,
        request: ims_20190815_models.GetLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetLoginProfileResponse:
        """
        @summary Queries the logon configurations of a Resource Access Management (RAM) user.
        
        @param request: GetLoginProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLoginProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLoginProfile',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetLoginProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_login_profile_with_options_async(
        self,
        request: ims_20190815_models.GetLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetLoginProfileResponse:
        """
        @summary Queries the logon configurations of a Resource Access Management (RAM) user.
        
        @param request: GetLoginProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLoginProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLoginProfile',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetLoginProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_login_profile(
        self,
        request: ims_20190815_models.GetLoginProfileRequest,
    ) -> ims_20190815_models.GetLoginProfileResponse:
        """
        @summary Queries the logon configurations of a Resource Access Management (RAM) user.
        
        @param request: GetLoginProfileRequest
        @return: GetLoginProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_login_profile_with_options(request, runtime)

    async def get_login_profile_async(
        self,
        request: ims_20190815_models.GetLoginProfileRequest,
    ) -> ims_20190815_models.GetLoginProfileResponse:
        """
        @summary Queries the logon configurations of a Resource Access Management (RAM) user.
        
        @param request: GetLoginProfileRequest
        @return: GetLoginProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_login_profile_with_options_async(request, runtime)

    def get_oidcprovider_with_options(
        self,
        request: ims_20190815_models.GetOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetOIDCProviderResponse:
        """
        @summary Queries the information about an OIDC IdP.
        
        @description ###
        This topic provides an example on how to query the information about an OpenID Connect (OIDC) identity provider (IdP) named `TestOIDCProvider`.
        
        @param request: GetOIDCProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oidcprovider_with_options_async(
        self,
        request: ims_20190815_models.GetOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetOIDCProviderResponse:
        """
        @summary Queries the information about an OIDC IdP.
        
        @description ###
        This topic provides an example on how to query the information about an OpenID Connect (OIDC) identity provider (IdP) named `TestOIDCProvider`.
        
        @param request: GetOIDCProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetOIDCProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oidcprovider(
        self,
        request: ims_20190815_models.GetOIDCProviderRequest,
    ) -> ims_20190815_models.GetOIDCProviderResponse:
        """
        @summary Queries the information about an OIDC IdP.
        
        @description ###
        This topic provides an example on how to query the information about an OpenID Connect (OIDC) identity provider (IdP) named `TestOIDCProvider`.
        
        @param request: GetOIDCProviderRequest
        @return: GetOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_oidcprovider_with_options(request, runtime)

    async def get_oidcprovider_async(
        self,
        request: ims_20190815_models.GetOIDCProviderRequest,
    ) -> ims_20190815_models.GetOIDCProviderResponse:
        """
        @summary Queries the information about an OIDC IdP.
        
        @description ###
        This topic provides an example on how to query the information about an OpenID Connect (OIDC) identity provider (IdP) named `TestOIDCProvider`.
        
        @param request: GetOIDCProviderRequest
        @return: GetOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_oidcprovider_with_options_async(request, runtime)

    def get_password_policy_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetPasswordPolicyResponse:
        """
        @summary Queries the details of the password policy for RAM users.
        
        @param request: GetPasswordPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPasswordPolicyResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetPasswordPolicy',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetPasswordPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_password_policy_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetPasswordPolicyResponse:
        """
        @summary Queries the details of the password policy for RAM users.
        
        @param request: GetPasswordPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPasswordPolicyResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetPasswordPolicy',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetPasswordPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_password_policy(self) -> ims_20190815_models.GetPasswordPolicyResponse:
        """
        @summary Queries the details of the password policy for RAM users.
        
        @return: GetPasswordPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_password_policy_with_options(runtime)

    async def get_password_policy_async(self) -> ims_20190815_models.GetPasswordPolicyResponse:
        """
        @summary Queries the details of the password policy for RAM users.
        
        @return: GetPasswordPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_password_policy_with_options_async(runtime)

    def get_samlprovider_with_options(
        self,
        request: ims_20190815_models.GetSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetSAMLProviderResponse:
        """
        @summary Queries the information about an identity provider (IdP) for role-based single sign-on (SSO).
        
        @param request: GetSAMLProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSAMLProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.samlprovider_name):
            query['SAMLProviderName'] = request.samlprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSAMLProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetSAMLProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_samlprovider_with_options_async(
        self,
        request: ims_20190815_models.GetSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetSAMLProviderResponse:
        """
        @summary Queries the information about an identity provider (IdP) for role-based single sign-on (SSO).
        
        @param request: GetSAMLProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSAMLProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.samlprovider_name):
            query['SAMLProviderName'] = request.samlprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSAMLProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetSAMLProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_samlprovider(
        self,
        request: ims_20190815_models.GetSAMLProviderRequest,
    ) -> ims_20190815_models.GetSAMLProviderResponse:
        """
        @summary Queries the information about an identity provider (IdP) for role-based single sign-on (SSO).
        
        @param request: GetSAMLProviderRequest
        @return: GetSAMLProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_samlprovider_with_options(request, runtime)

    async def get_samlprovider_async(
        self,
        request: ims_20190815_models.GetSAMLProviderRequest,
    ) -> ims_20190815_models.GetSAMLProviderResponse:
        """
        @summary Queries the information about an identity provider (IdP) for role-based single sign-on (SSO).
        
        @param request: GetSAMLProviderRequest
        @return: GetSAMLProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_samlprovider_with_options_async(request, runtime)

    def get_security_preference_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetSecurityPreferenceResponse:
        """
        @summary Queries the security preferences for RAM users.
        
        @param request: GetSecurityPreferenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSecurityPreferenceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetSecurityPreference',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetSecurityPreferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_security_preference_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetSecurityPreferenceResponse:
        """
        @summary Queries the security preferences for RAM users.
        
        @param request: GetSecurityPreferenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSecurityPreferenceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetSecurityPreference',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetSecurityPreferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_security_preference(self) -> ims_20190815_models.GetSecurityPreferenceResponse:
        """
        @summary Queries the security preferences for RAM users.
        
        @return: GetSecurityPreferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_security_preference_with_options(runtime)

    async def get_security_preference_async(self) -> ims_20190815_models.GetSecurityPreferenceResponse:
        """
        @summary Queries the security preferences for RAM users.
        
        @return: GetSecurityPreferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_security_preference_with_options_async(runtime)

    def get_user_with_options(
        self,
        request: ims_20190815_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetUserResponse:
        """
        @summary Queries the information about a RAM user.
        
        @param request: GetUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: ims_20190815_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetUserResponse:
        """
        @summary Queries the information about a RAM user.
        
        @param request: GetUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: ims_20190815_models.GetUserRequest,
    ) -> ims_20190815_models.GetUserResponse:
        """
        @summary Queries the information about a RAM user.
        
        @param request: GetUserRequest
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: ims_20190815_models.GetUserRequest,
    ) -> ims_20190815_models.GetUserResponse:
        """
        @summary Queries the information about a RAM user.
        
        @param request: GetUserRequest
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def get_user_in_recycle_bin_with_options(
        self,
        request: ims_20190815_models.GetUserInRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetUserInRecycleBinResponse:
        """
        @summary Queries information about a specific Resource Access Management (RAM) user in the recycle bin.
        
        @param request: GetUserInRecycleBinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserInRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserInRecycleBin',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetUserInRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_in_recycle_bin_with_options_async(
        self,
        request: ims_20190815_models.GetUserInRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetUserInRecycleBinResponse:
        """
        @summary Queries information about a specific Resource Access Management (RAM) user in the recycle bin.
        
        @param request: GetUserInRecycleBinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserInRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserInRecycleBin',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetUserInRecycleBinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_in_recycle_bin(
        self,
        request: ims_20190815_models.GetUserInRecycleBinRequest,
    ) -> ims_20190815_models.GetUserInRecycleBinResponse:
        """
        @summary Queries information about a specific Resource Access Management (RAM) user in the recycle bin.
        
        @param request: GetUserInRecycleBinRequest
        @return: GetUserInRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_in_recycle_bin_with_options(request, runtime)

    async def get_user_in_recycle_bin_async(
        self,
        request: ims_20190815_models.GetUserInRecycleBinRequest,
    ) -> ims_20190815_models.GetUserInRecycleBinResponse:
        """
        @summary Queries information about a specific Resource Access Management (RAM) user in the recycle bin.
        
        @param request: GetUserInRecycleBinRequest
        @return: GetUserInRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_in_recycle_bin_with_options_async(request, runtime)

    def get_user_mfainfo_with_options(
        self,
        request: ims_20190815_models.GetUserMFAInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetUserMFAInfoResponse:
        """
        @summary Queries information about the multi-factor authentication (MFA) device that is bound to a Resource Access Management (RAM) user.
        
        @param request: GetUserMFAInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserMFAInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserMFAInfo',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetUserMFAInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_mfainfo_with_options_async(
        self,
        request: ims_20190815_models.GetUserMFAInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetUserMFAInfoResponse:
        """
        @summary Queries information about the multi-factor authentication (MFA) device that is bound to a Resource Access Management (RAM) user.
        
        @param request: GetUserMFAInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserMFAInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserMFAInfo',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetUserMFAInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_mfainfo(
        self,
        request: ims_20190815_models.GetUserMFAInfoRequest,
    ) -> ims_20190815_models.GetUserMFAInfoResponse:
        """
        @summary Queries information about the multi-factor authentication (MFA) device that is bound to a Resource Access Management (RAM) user.
        
        @param request: GetUserMFAInfoRequest
        @return: GetUserMFAInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_mfainfo_with_options(request, runtime)

    async def get_user_mfainfo_async(
        self,
        request: ims_20190815_models.GetUserMFAInfoRequest,
    ) -> ims_20190815_models.GetUserMFAInfoResponse:
        """
        @summary Queries information about the multi-factor authentication (MFA) device that is bound to a Resource Access Management (RAM) user.
        
        @param request: GetUserMFAInfoRequest
        @return: GetUserMFAInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_mfainfo_with_options_async(request, runtime)

    def get_user_sso_settings_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetUserSsoSettingsResponse:
        """
        @summary Queries the configurations of user-based single sign-on (SSO).
        
        @param request: GetUserSsoSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserSsoSettingsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetUserSsoSettings',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetUserSsoSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_sso_settings_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetUserSsoSettingsResponse:
        """
        @summary Queries the configurations of user-based single sign-on (SSO).
        
        @param request: GetUserSsoSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserSsoSettingsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetUserSsoSettings',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetUserSsoSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_sso_settings(self) -> ims_20190815_models.GetUserSsoSettingsResponse:
        """
        @summary Queries the configurations of user-based single sign-on (SSO).
        
        @return: GetUserSsoSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_sso_settings_with_options(runtime)

    async def get_user_sso_settings_async(self) -> ims_20190815_models.GetUserSsoSettingsResponse:
        """
        @summary Queries the configurations of user-based single sign-on (SSO).
        
        @return: GetUserSsoSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_sso_settings_with_options_async(runtime)

    def get_verification_info_with_options(
        self,
        request: ims_20190815_models.GetVerificationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetVerificationInfoResponse:
        """
        @summary Queries the status of the mobile phone or email that is bound to a Resource Access Management (RAM) user.
        
        @param request: GetVerificationInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVerificationInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVerificationInfo',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetVerificationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_verification_info_with_options_async(
        self,
        request: ims_20190815_models.GetVerificationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.GetVerificationInfoResponse:
        """
        @summary Queries the status of the mobile phone or email that is bound to a Resource Access Management (RAM) user.
        
        @param request: GetVerificationInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVerificationInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVerificationInfo',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetVerificationInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_verification_info(
        self,
        request: ims_20190815_models.GetVerificationInfoRequest,
    ) -> ims_20190815_models.GetVerificationInfoResponse:
        """
        @summary Queries the status of the mobile phone or email that is bound to a Resource Access Management (RAM) user.
        
        @param request: GetVerificationInfoRequest
        @return: GetVerificationInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_verification_info_with_options(request, runtime)

    async def get_verification_info_async(
        self,
        request: ims_20190815_models.GetVerificationInfoRequest,
    ) -> ims_20190815_models.GetVerificationInfoResponse:
        """
        @summary Queries the status of the mobile phone or email that is bound to a Resource Access Management (RAM) user.
        
        @param request: GetVerificationInfoRequest
        @return: GetVerificationInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_verification_info_with_options_async(request, runtime)

    def list_access_keys_with_options(
        self,
        request: ims_20190815_models.ListAccessKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListAccessKeysResponse:
        """
        @summary Queries the AccessKey pairs of an Alibaba Cloud account or a Resource Access Management (RAM) user.
        
        @param request: ListAccessKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccessKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessKeys',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListAccessKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_access_keys_with_options_async(
        self,
        request: ims_20190815_models.ListAccessKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListAccessKeysResponse:
        """
        @summary Queries the AccessKey pairs of an Alibaba Cloud account or a Resource Access Management (RAM) user.
        
        @param request: ListAccessKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccessKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessKeys',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListAccessKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_access_keys(
        self,
        request: ims_20190815_models.ListAccessKeysRequest,
    ) -> ims_20190815_models.ListAccessKeysResponse:
        """
        @summary Queries the AccessKey pairs of an Alibaba Cloud account or a Resource Access Management (RAM) user.
        
        @param request: ListAccessKeysRequest
        @return: ListAccessKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_access_keys_with_options(request, runtime)

    async def list_access_keys_async(
        self,
        request: ims_20190815_models.ListAccessKeysRequest,
    ) -> ims_20190815_models.ListAccessKeysResponse:
        """
        @summary Queries the AccessKey pairs of an Alibaba Cloud account or a Resource Access Management (RAM) user.
        
        @param request: ListAccessKeysRequest
        @return: ListAccessKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_access_keys_with_options_async(request, runtime)

    def list_access_keys_in_recycle_bin_with_options(
        self,
        request: ims_20190815_models.ListAccessKeysInRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListAccessKeysInRecycleBinResponse:
        """
        @summary Queries the AccessKey pairs of a specific Resource Access Management (RAM) user in the recycle bin.
        
        @param request: ListAccessKeysInRecycleBinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccessKeysInRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessKeysInRecycleBin',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListAccessKeysInRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_access_keys_in_recycle_bin_with_options_async(
        self,
        request: ims_20190815_models.ListAccessKeysInRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListAccessKeysInRecycleBinResponse:
        """
        @summary Queries the AccessKey pairs of a specific Resource Access Management (RAM) user in the recycle bin.
        
        @param request: ListAccessKeysInRecycleBinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccessKeysInRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessKeysInRecycleBin',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListAccessKeysInRecycleBinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_access_keys_in_recycle_bin(
        self,
        request: ims_20190815_models.ListAccessKeysInRecycleBinRequest,
    ) -> ims_20190815_models.ListAccessKeysInRecycleBinResponse:
        """
        @summary Queries the AccessKey pairs of a specific Resource Access Management (RAM) user in the recycle bin.
        
        @param request: ListAccessKeysInRecycleBinRequest
        @return: ListAccessKeysInRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_access_keys_in_recycle_bin_with_options(request, runtime)

    async def list_access_keys_in_recycle_bin_async(
        self,
        request: ims_20190815_models.ListAccessKeysInRecycleBinRequest,
    ) -> ims_20190815_models.ListAccessKeysInRecycleBinResponse:
        """
        @summary Queries the AccessKey pairs of a specific Resource Access Management (RAM) user in the recycle bin.
        
        @param request: ListAccessKeysInRecycleBinRequest
        @return: ListAccessKeysInRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_access_keys_in_recycle_bin_with_options_async(request, runtime)

    def list_app_secret_ids_with_options(
        self,
        request: ims_20190815_models.ListAppSecretIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListAppSecretIdsResponse:
        """
        @summary Queries the secret IDs of an application.
        
        @param request: ListAppSecretIdsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppSecretIdsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppSecretIds',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListAppSecretIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_secret_ids_with_options_async(
        self,
        request: ims_20190815_models.ListAppSecretIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListAppSecretIdsResponse:
        """
        @summary Queries the secret IDs of an application.
        
        @param request: ListAppSecretIdsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppSecretIdsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppSecretIds',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListAppSecretIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_secret_ids(
        self,
        request: ims_20190815_models.ListAppSecretIdsRequest,
    ) -> ims_20190815_models.ListAppSecretIdsResponse:
        """
        @summary Queries the secret IDs of an application.
        
        @param request: ListAppSecretIdsRequest
        @return: ListAppSecretIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_app_secret_ids_with_options(request, runtime)

    async def list_app_secret_ids_async(
        self,
        request: ims_20190815_models.ListAppSecretIdsRequest,
    ) -> ims_20190815_models.ListAppSecretIdsResponse:
        """
        @summary Queries the secret IDs of an application.
        
        @param request: ListAppSecretIdsRequest
        @return: ListAppSecretIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_app_secret_ids_with_options_async(request, runtime)

    def list_application_provision_infos_with_options(
        self,
        request: ims_20190815_models.ListApplicationProvisionInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListApplicationProvisionInfosResponse:
        """
        @summary Queries installation information about all installed applications.
        
        @param request: ListApplicationProvisionInfosRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationProvisionInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationProvisionInfos',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListApplicationProvisionInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_provision_infos_with_options_async(
        self,
        request: ims_20190815_models.ListApplicationProvisionInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListApplicationProvisionInfosResponse:
        """
        @summary Queries installation information about all installed applications.
        
        @param request: ListApplicationProvisionInfosRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationProvisionInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationProvisionInfos',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListApplicationProvisionInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_provision_infos(
        self,
        request: ims_20190815_models.ListApplicationProvisionInfosRequest,
    ) -> ims_20190815_models.ListApplicationProvisionInfosResponse:
        """
        @summary Queries installation information about all installed applications.
        
        @param request: ListApplicationProvisionInfosRequest
        @return: ListApplicationProvisionInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_application_provision_infos_with_options(request, runtime)

    async def list_application_provision_infos_async(
        self,
        request: ims_20190815_models.ListApplicationProvisionInfosRequest,
    ) -> ims_20190815_models.ListApplicationProvisionInfosResponse:
        """
        @summary Queries installation information about all installed applications.
        
        @param request: ListApplicationProvisionInfosRequest
        @return: ListApplicationProvisionInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_application_provision_infos_with_options_async(request, runtime)

    def list_applications_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListApplicationsResponse:
        """
        @summary Lists the created applications.
        
        @description This topic provides an example on how to query the applications within the current account. The returned result shows that only one application named `myapp` belongs to the current account.
        
        @param request: ListApplicationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListApplications',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListApplicationsResponse:
        """
        @summary Lists the created applications.
        
        @description This topic provides an example on how to query the applications within the current account. The returned result shows that only one application named `myapp` belongs to the current account.
        
        @param request: ListApplicationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListApplications',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications(self) -> ims_20190815_models.ListApplicationsResponse:
        """
        @summary Lists the created applications.
        
        @description This topic provides an example on how to query the applications within the current account. The returned result shows that only one application named `myapp` belongs to the current account.
        
        @return: ListApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_applications_with_options(runtime)

    async def list_applications_async(self) -> ims_20190815_models.ListApplicationsResponse:
        """
        @summary Lists the created applications.
        
        @description This topic provides an example on how to query the applications within the current account. The returned result shows that only one application named `myapp` belongs to the current account.
        
        @return: ListApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_applications_with_options_async(runtime)

    def list_external_applications_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListExternalApplicationsResponse:
        """
        @summary Queries information about all installed external applications.
        
        @param request: ListExternalApplicationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExternalApplicationsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListExternalApplications',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListExternalApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_external_applications_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListExternalApplicationsResponse:
        """
        @summary Queries information about all installed external applications.
        
        @param request: ListExternalApplicationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExternalApplicationsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListExternalApplications',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListExternalApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_external_applications(self) -> ims_20190815_models.ListExternalApplicationsResponse:
        """
        @summary Queries information about all installed external applications.
        
        @return: ListExternalApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_external_applications_with_options(runtime)

    async def list_external_applications_async(self) -> ims_20190815_models.ListExternalApplicationsResponse:
        """
        @summary Queries information about all installed external applications.
        
        @return: ListExternalApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_external_applications_with_options_async(runtime)

    def list_groups_with_options(
        self,
        request: ims_20190815_models.ListGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListGroupsResponse:
        """
        @summary Queries Resource Access Management (RAM) user groups.
        
        @param request: ListGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_with_options_async(
        self,
        request: ims_20190815_models.ListGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListGroupsResponse:
        """
        @summary Queries Resource Access Management (RAM) user groups.
        
        @param request: ListGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups(
        self,
        request: ims_20190815_models.ListGroupsRequest,
    ) -> ims_20190815_models.ListGroupsResponse:
        """
        @summary Queries Resource Access Management (RAM) user groups.
        
        @param request: ListGroupsRequest
        @return: ListGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_groups_with_options(request, runtime)

    async def list_groups_async(
        self,
        request: ims_20190815_models.ListGroupsRequest,
    ) -> ims_20190815_models.ListGroupsResponse:
        """
        @summary Queries Resource Access Management (RAM) user groups.
        
        @param request: ListGroupsRequest
        @return: ListGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_groups_with_options_async(request, runtime)

    def list_groups_for_user_with_options(
        self,
        request: ims_20190815_models.ListGroupsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListGroupsForUserResponse:
        """
        @summary Queries the Resource Access Management (RAM) user groups to which a RAM user belongs.
        
        @param request: ListGroupsForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsForUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupsForUser',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListGroupsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_for_user_with_options_async(
        self,
        request: ims_20190815_models.ListGroupsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListGroupsForUserResponse:
        """
        @summary Queries the Resource Access Management (RAM) user groups to which a RAM user belongs.
        
        @param request: ListGroupsForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsForUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupsForUser',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListGroupsForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups_for_user(
        self,
        request: ims_20190815_models.ListGroupsForUserRequest,
    ) -> ims_20190815_models.ListGroupsForUserResponse:
        """
        @summary Queries the Resource Access Management (RAM) user groups to which a RAM user belongs.
        
        @param request: ListGroupsForUserRequest
        @return: ListGroupsForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_groups_for_user_with_options(request, runtime)

    async def list_groups_for_user_async(
        self,
        request: ims_20190815_models.ListGroupsForUserRequest,
    ) -> ims_20190815_models.ListGroupsForUserResponse:
        """
        @summary Queries the Resource Access Management (RAM) user groups to which a RAM user belongs.
        
        @param request: ListGroupsForUserRequest
        @return: ListGroupsForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_groups_for_user_with_options_async(request, runtime)

    def list_oidcproviders_with_options(
        self,
        request: ims_20190815_models.ListOIDCProvidersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListOIDCProvidersResponse:
        """
        @summary Queries OIDC IdPs.
        
        @description ###
        This topic provides an example on how to query all OpenID Connect (OIDC) identity providers (IdPs) within your Alibaba Cloud account. The response shows that your Alibaba Cloud account has only one OIDC IdP named `TestOIDCProvider`.
        
        @param request: ListOIDCProvidersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOIDCProvidersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOIDCProviders',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListOIDCProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_oidcproviders_with_options_async(
        self,
        request: ims_20190815_models.ListOIDCProvidersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListOIDCProvidersResponse:
        """
        @summary Queries OIDC IdPs.
        
        @description ###
        This topic provides an example on how to query all OpenID Connect (OIDC) identity providers (IdPs) within your Alibaba Cloud account. The response shows that your Alibaba Cloud account has only one OIDC IdP named `TestOIDCProvider`.
        
        @param request: ListOIDCProvidersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOIDCProvidersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOIDCProviders',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListOIDCProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_oidcproviders(
        self,
        request: ims_20190815_models.ListOIDCProvidersRequest,
    ) -> ims_20190815_models.ListOIDCProvidersResponse:
        """
        @summary Queries OIDC IdPs.
        
        @description ###
        This topic provides an example on how to query all OpenID Connect (OIDC) identity providers (IdPs) within your Alibaba Cloud account. The response shows that your Alibaba Cloud account has only one OIDC IdP named `TestOIDCProvider`.
        
        @param request: ListOIDCProvidersRequest
        @return: ListOIDCProvidersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_oidcproviders_with_options(request, runtime)

    async def list_oidcproviders_async(
        self,
        request: ims_20190815_models.ListOIDCProvidersRequest,
    ) -> ims_20190815_models.ListOIDCProvidersResponse:
        """
        @summary Queries OIDC IdPs.
        
        @description ###
        This topic provides an example on how to query all OpenID Connect (OIDC) identity providers (IdPs) within your Alibaba Cloud account. The response shows that your Alibaba Cloud account has only one OIDC IdP named `TestOIDCProvider`.
        
        @param request: ListOIDCProvidersRequest
        @return: ListOIDCProvidersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_oidcproviders_with_options_async(request, runtime)

    def list_passkeys_with_options(
        self,
        request: ims_20190815_models.ListPasskeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListPasskeysResponse:
        """
        @summary Queries the information about the passkeys that are bound to a Resource Access Management (RAM) user.
        
        @param request: ListPasskeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPasskeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPasskeys',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListPasskeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_passkeys_with_options_async(
        self,
        request: ims_20190815_models.ListPasskeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListPasskeysResponse:
        """
        @summary Queries the information about the passkeys that are bound to a Resource Access Management (RAM) user.
        
        @param request: ListPasskeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPasskeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPasskeys',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListPasskeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_passkeys(
        self,
        request: ims_20190815_models.ListPasskeysRequest,
    ) -> ims_20190815_models.ListPasskeysResponse:
        """
        @summary Queries the information about the passkeys that are bound to a Resource Access Management (RAM) user.
        
        @param request: ListPasskeysRequest
        @return: ListPasskeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_passkeys_with_options(request, runtime)

    async def list_passkeys_async(
        self,
        request: ims_20190815_models.ListPasskeysRequest,
    ) -> ims_20190815_models.ListPasskeysResponse:
        """
        @summary Queries the information about the passkeys that are bound to a Resource Access Management (RAM) user.
        
        @param request: ListPasskeysRequest
        @return: ListPasskeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_passkeys_with_options_async(request, runtime)

    def list_predefined_scopes_with_options(
        self,
        request: ims_20190815_models.ListPredefinedScopesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListPredefinedScopesResponse:
        """
        @summary Queries predefined application permissions.
        
        @param request: ListPredefinedScopesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPredefinedScopesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPredefinedScopes',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListPredefinedScopesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_predefined_scopes_with_options_async(
        self,
        request: ims_20190815_models.ListPredefinedScopesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListPredefinedScopesResponse:
        """
        @summary Queries predefined application permissions.
        
        @param request: ListPredefinedScopesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPredefinedScopesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPredefinedScopes',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListPredefinedScopesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_predefined_scopes(
        self,
        request: ims_20190815_models.ListPredefinedScopesRequest,
    ) -> ims_20190815_models.ListPredefinedScopesResponse:
        """
        @summary Queries predefined application permissions.
        
        @param request: ListPredefinedScopesRequest
        @return: ListPredefinedScopesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_predefined_scopes_with_options(request, runtime)

    async def list_predefined_scopes_async(
        self,
        request: ims_20190815_models.ListPredefinedScopesRequest,
    ) -> ims_20190815_models.ListPredefinedScopesResponse:
        """
        @summary Queries predefined application permissions.
        
        @param request: ListPredefinedScopesRequest
        @return: ListPredefinedScopesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_predefined_scopes_with_options_async(request, runtime)

    def list_recent_governance_metrics_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListRecentGovernanceMetricsResponse:
        """
        @summary Queries all metric values in the most recent governance check.
        
        @param request: ListRecentGovernanceMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRecentGovernanceMetricsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRecentGovernanceMetrics',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListRecentGovernanceMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recent_governance_metrics_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListRecentGovernanceMetricsResponse:
        """
        @summary Queries all metric values in the most recent governance check.
        
        @param request: ListRecentGovernanceMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRecentGovernanceMetricsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRecentGovernanceMetrics',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListRecentGovernanceMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recent_governance_metrics(self) -> ims_20190815_models.ListRecentGovernanceMetricsResponse:
        """
        @summary Queries all metric values in the most recent governance check.
        
        @return: ListRecentGovernanceMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_recent_governance_metrics_with_options(runtime)

    async def list_recent_governance_metrics_async(self) -> ims_20190815_models.ListRecentGovernanceMetricsResponse:
        """
        @summary Queries all metric values in the most recent governance check.
        
        @return: ListRecentGovernanceMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_recent_governance_metrics_with_options_async(runtime)

    def list_samlproviders_with_options(
        self,
        request: ims_20190815_models.ListSAMLProvidersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListSAMLProvidersResponse:
        """
        @summary Queries information about identity providers (IdPs) for role-based single sign-on (SSO).
        
        @param request: ListSAMLProvidersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSAMLProvidersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSAMLProviders',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListSAMLProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_samlproviders_with_options_async(
        self,
        request: ims_20190815_models.ListSAMLProvidersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListSAMLProvidersResponse:
        """
        @summary Queries information about identity providers (IdPs) for role-based single sign-on (SSO).
        
        @param request: ListSAMLProvidersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSAMLProvidersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSAMLProviders',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListSAMLProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_samlproviders(
        self,
        request: ims_20190815_models.ListSAMLProvidersRequest,
    ) -> ims_20190815_models.ListSAMLProvidersResponse:
        """
        @summary Queries information about identity providers (IdPs) for role-based single sign-on (SSO).
        
        @param request: ListSAMLProvidersRequest
        @return: ListSAMLProvidersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_samlproviders_with_options(request, runtime)

    async def list_samlproviders_async(
        self,
        request: ims_20190815_models.ListSAMLProvidersRequest,
    ) -> ims_20190815_models.ListSAMLProvidersResponse:
        """
        @summary Queries information about identity providers (IdPs) for role-based single sign-on (SSO).
        
        @param request: ListSAMLProvidersRequest
        @return: ListSAMLProvidersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_samlproviders_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ims_20190815_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added resources.
        
        @description ###
        You must specify at least one of the following parameters or parameter pairs in a request to determine a query object:
        `ResourceId.N`
        `Tag.N.Key`
        `Tag.N.Key` and `Tag.N.Value`
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_principal_name):
            query['ResourcePrincipalName'] = request.resource_principal_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ims_20190815_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added resources.
        
        @description ###
        You must specify at least one of the following parameters or parameter pairs in a request to determine a query object:
        `ResourceId.N`
        `Tag.N.Key`
        `Tag.N.Key` and `Tag.N.Value`
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_principal_name):
            query['ResourcePrincipalName'] = request.resource_principal_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: ims_20190815_models.ListTagResourcesRequest,
    ) -> ims_20190815_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added resources.
        
        @description ###
        You must specify at least one of the following parameters or parameter pairs in a request to determine a query object:
        `ResourceId.N`
        `Tag.N.Key`
        `Tag.N.Key` and `Tag.N.Value`
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ims_20190815_models.ListTagResourcesRequest,
    ) -> ims_20190815_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added resources.
        
        @description ###
        You must specify at least one of the following parameters or parameter pairs in a request to determine a query object:
        `ResourceId.N`
        `Tag.N.Key`
        `Tag.N.Key` and `Tag.N.Value`
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_user_basic_infos_with_options(
        self,
        request: ims_20190815_models.ListUserBasicInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListUserBasicInfosResponse:
        """
        @summary Queries the basic information about all Resource Access Management (RAM) users.
        
        @description You can call the following API operations to query information about all RAM users:
        ListUsers: queries the details of all RAM users.
        ListUserBasicInfos: queries the basic information about all RAM users. The basic information includes only the logon names (`UserPrincipalName`), display names (`DisplayName`), and user IDs (`UserId`).
        
        @param request: ListUserBasicInfosRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserBasicInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserBasicInfos',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListUserBasicInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_basic_infos_with_options_async(
        self,
        request: ims_20190815_models.ListUserBasicInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListUserBasicInfosResponse:
        """
        @summary Queries the basic information about all Resource Access Management (RAM) users.
        
        @description You can call the following API operations to query information about all RAM users:
        ListUsers: queries the details of all RAM users.
        ListUserBasicInfos: queries the basic information about all RAM users. The basic information includes only the logon names (`UserPrincipalName`), display names (`DisplayName`), and user IDs (`UserId`).
        
        @param request: ListUserBasicInfosRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserBasicInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserBasicInfos',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListUserBasicInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_basic_infos(
        self,
        request: ims_20190815_models.ListUserBasicInfosRequest,
    ) -> ims_20190815_models.ListUserBasicInfosResponse:
        """
        @summary Queries the basic information about all Resource Access Management (RAM) users.
        
        @description You can call the following API operations to query information about all RAM users:
        ListUsers: queries the details of all RAM users.
        ListUserBasicInfos: queries the basic information about all RAM users. The basic information includes only the logon names (`UserPrincipalName`), display names (`DisplayName`), and user IDs (`UserId`).
        
        @param request: ListUserBasicInfosRequest
        @return: ListUserBasicInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_basic_infos_with_options(request, runtime)

    async def list_user_basic_infos_async(
        self,
        request: ims_20190815_models.ListUserBasicInfosRequest,
    ) -> ims_20190815_models.ListUserBasicInfosResponse:
        """
        @summary Queries the basic information about all Resource Access Management (RAM) users.
        
        @description You can call the following API operations to query information about all RAM users:
        ListUsers: queries the details of all RAM users.
        ListUserBasicInfos: queries the basic information about all RAM users. The basic information includes only the logon names (`UserPrincipalName`), display names (`DisplayName`), and user IDs (`UserId`).
        
        @param request: ListUserBasicInfosRequest
        @return: ListUserBasicInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_basic_infos_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: ims_20190815_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListUsersResponse:
        """
        @summary Queries information about all Resource Access Management (RAM) users.
        
        @description ### [](#)
        You can call the following API operations to query the details of all RAM users:
        ListUsers: queries the details of all RAM users.
        ListUserBasicInfos: queries the basic information about all RAM users. The basic information includes only the logon names (`UserPrincipalName`), display names (`DisplayName`), and user IDs (`UserId`).
        
        @param request: ListUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: ims_20190815_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListUsersResponse:
        """
        @summary Queries information about all Resource Access Management (RAM) users.
        
        @description ### [](#)
        You can call the following API operations to query the details of all RAM users:
        ListUsers: queries the details of all RAM users.
        ListUserBasicInfos: queries the basic information about all RAM users. The basic information includes only the logon names (`UserPrincipalName`), display names (`DisplayName`), and user IDs (`UserId`).
        
        @param request: ListUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: ims_20190815_models.ListUsersRequest,
    ) -> ims_20190815_models.ListUsersResponse:
        """
        @summary Queries information about all Resource Access Management (RAM) users.
        
        @description ### [](#)
        You can call the following API operations to query the details of all RAM users:
        ListUsers: queries the details of all RAM users.
        ListUserBasicInfos: queries the basic information about all RAM users. The basic information includes only the logon names (`UserPrincipalName`), display names (`DisplayName`), and user IDs (`UserId`).
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: ims_20190815_models.ListUsersRequest,
    ) -> ims_20190815_models.ListUsersResponse:
        """
        @summary Queries information about all Resource Access Management (RAM) users.
        
        @description ### [](#)
        You can call the following API operations to query the details of all RAM users:
        ListUsers: queries the details of all RAM users.
        ListUserBasicInfos: queries the basic information about all RAM users. The basic information includes only the logon names (`UserPrincipalName`), display names (`DisplayName`), and user IDs (`UserId`).
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def list_users_for_group_with_options(
        self,
        request: ims_20190815_models.ListUsersForGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListUsersForGroupResponse:
        """
        @summary Queries Resource Access Management (RAM) users in a RAM user group.
        
        @param request: ListUsersForGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersForGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsersForGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListUsersForGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_for_group_with_options_async(
        self,
        request: ims_20190815_models.ListUsersForGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListUsersForGroupResponse:
        """
        @summary Queries Resource Access Management (RAM) users in a RAM user group.
        
        @param request: ListUsersForGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersForGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsersForGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListUsersForGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users_for_group(
        self,
        request: ims_20190815_models.ListUsersForGroupRequest,
    ) -> ims_20190815_models.ListUsersForGroupResponse:
        """
        @summary Queries Resource Access Management (RAM) users in a RAM user group.
        
        @param request: ListUsersForGroupRequest
        @return: ListUsersForGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_users_for_group_with_options(request, runtime)

    async def list_users_for_group_async(
        self,
        request: ims_20190815_models.ListUsersForGroupRequest,
    ) -> ims_20190815_models.ListUsersForGroupResponse:
        """
        @summary Queries Resource Access Management (RAM) users in a RAM user group.
        
        @param request: ListUsersForGroupRequest
        @return: ListUsersForGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_users_for_group_with_options_async(request, runtime)

    def list_users_in_recycle_bin_with_options(
        self,
        request: ims_20190815_models.ListUsersInRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListUsersInRecycleBinResponse:
        """
        @summary Queries the basic information about all Resource Access Management (RAM) users in the recycle bin.
        
        @param request: ListUsersInRecycleBinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersInRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsersInRecycleBin',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListUsersInRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_in_recycle_bin_with_options_async(
        self,
        request: ims_20190815_models.ListUsersInRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListUsersInRecycleBinResponse:
        """
        @summary Queries the basic information about all Resource Access Management (RAM) users in the recycle bin.
        
        @param request: ListUsersInRecycleBinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersInRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsersInRecycleBin',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListUsersInRecycleBinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users_in_recycle_bin(
        self,
        request: ims_20190815_models.ListUsersInRecycleBinRequest,
    ) -> ims_20190815_models.ListUsersInRecycleBinResponse:
        """
        @summary Queries the basic information about all Resource Access Management (RAM) users in the recycle bin.
        
        @param request: ListUsersInRecycleBinRequest
        @return: ListUsersInRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_users_in_recycle_bin_with_options(request, runtime)

    async def list_users_in_recycle_bin_async(
        self,
        request: ims_20190815_models.ListUsersInRecycleBinRequest,
    ) -> ims_20190815_models.ListUsersInRecycleBinResponse:
        """
        @summary Queries the basic information about all Resource Access Management (RAM) users in the recycle bin.
        
        @param request: ListUsersInRecycleBinRequest
        @return: ListUsersInRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_users_in_recycle_bin_with_options_async(request, runtime)

    def list_virtual_mfadevices_with_options(
        self,
        request: ims_20190815_models.ListVirtualMFADevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListVirtualMFADevicesResponse:
        """
        @summary Queries multi-factor authentication (MFA) devices.
        
        @param request: ListVirtualMFADevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVirtualMFADevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVirtualMFADevices',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListVirtualMFADevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_virtual_mfadevices_with_options_async(
        self,
        request: ims_20190815_models.ListVirtualMFADevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ListVirtualMFADevicesResponse:
        """
        @summary Queries multi-factor authentication (MFA) devices.
        
        @param request: ListVirtualMFADevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVirtualMFADevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVirtualMFADevices',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListVirtualMFADevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_virtual_mfadevices(
        self,
        request: ims_20190815_models.ListVirtualMFADevicesRequest,
    ) -> ims_20190815_models.ListVirtualMFADevicesResponse:
        """
        @summary Queries multi-factor authentication (MFA) devices.
        
        @param request: ListVirtualMFADevicesRequest
        @return: ListVirtualMFADevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_virtual_mfadevices_with_options(request, runtime)

    async def list_virtual_mfadevices_async(
        self,
        request: ims_20190815_models.ListVirtualMFADevicesRequest,
    ) -> ims_20190815_models.ListVirtualMFADevicesResponse:
        """
        @summary Queries multi-factor authentication (MFA) devices.
        
        @param request: ListVirtualMFADevicesRequest
        @return: ListVirtualMFADevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_virtual_mfadevices_with_options_async(request, runtime)

    def provision_application_with_options(
        self,
        request: ims_20190815_models.ProvisionApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ProvisionApplicationResponse:
        """
        @summary Installs an application.
        
        @param request: ProvisionApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ProvisionApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scopes):
            query['Scopes'] = request.scopes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProvisionApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ProvisionApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def provision_application_with_options_async(
        self,
        request: ims_20190815_models.ProvisionApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ProvisionApplicationResponse:
        """
        @summary Installs an application.
        
        @param request: ProvisionApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ProvisionApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scopes):
            query['Scopes'] = request.scopes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProvisionApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ProvisionApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def provision_application(
        self,
        request: ims_20190815_models.ProvisionApplicationRequest,
    ) -> ims_20190815_models.ProvisionApplicationResponse:
        """
        @summary Installs an application.
        
        @param request: ProvisionApplicationRequest
        @return: ProvisionApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.provision_application_with_options(request, runtime)

    async def provision_application_async(
        self,
        request: ims_20190815_models.ProvisionApplicationRequest,
    ) -> ims_20190815_models.ProvisionApplicationResponse:
        """
        @summary Installs an application.
        
        @param request: ProvisionApplicationRequest
        @return: ProvisionApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.provision_application_with_options_async(request, runtime)

    def provision_external_application_with_options(
        self,
        request: ims_20190815_models.ProvisionExternalApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ProvisionExternalApplicationResponse:
        """
        @summary Installs an external application.
        
        @param request: ProvisionExternalApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ProvisionExternalApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scopes):
            query['Scopes'] = request.scopes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProvisionExternalApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ProvisionExternalApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def provision_external_application_with_options_async(
        self,
        request: ims_20190815_models.ProvisionExternalApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.ProvisionExternalApplicationResponse:
        """
        @summary Installs an external application.
        
        @param request: ProvisionExternalApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ProvisionExternalApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scopes):
            query['Scopes'] = request.scopes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProvisionExternalApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ProvisionExternalApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def provision_external_application(
        self,
        request: ims_20190815_models.ProvisionExternalApplicationRequest,
    ) -> ims_20190815_models.ProvisionExternalApplicationResponse:
        """
        @summary Installs an external application.
        
        @param request: ProvisionExternalApplicationRequest
        @return: ProvisionExternalApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.provision_external_application_with_options(request, runtime)

    async def provision_external_application_async(
        self,
        request: ims_20190815_models.ProvisionExternalApplicationRequest,
    ) -> ims_20190815_models.ProvisionExternalApplicationResponse:
        """
        @summary Installs an external application.
        
        @param request: ProvisionExternalApplicationRequest
        @return: ProvisionExternalApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.provision_external_application_with_options_async(request, runtime)

    def remove_client_id_from_oidcprovider_with_options(
        self,
        request: ims_20190815_models.RemoveClientIdFromOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.RemoveClientIdFromOIDCProviderResponse:
        """
        @summary Removes a client ID from an OpenID Connect (OIDC) identity provider (IdP).
        
        @description ###
        This topic provides an example on how to remove the client ID `498469743454717***` from the OIDC IdP named `TestOIDCProvider`.
        
        @param request: RemoveClientIdFromOIDCProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveClientIdFromOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveClientIdFromOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.RemoveClientIdFromOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_client_id_from_oidcprovider_with_options_async(
        self,
        request: ims_20190815_models.RemoveClientIdFromOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.RemoveClientIdFromOIDCProviderResponse:
        """
        @summary Removes a client ID from an OpenID Connect (OIDC) identity provider (IdP).
        
        @description ###
        This topic provides an example on how to remove the client ID `498469743454717***` from the OIDC IdP named `TestOIDCProvider`.
        
        @param request: RemoveClientIdFromOIDCProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveClientIdFromOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveClientIdFromOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.RemoveClientIdFromOIDCProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_client_id_from_oidcprovider(
        self,
        request: ims_20190815_models.RemoveClientIdFromOIDCProviderRequest,
    ) -> ims_20190815_models.RemoveClientIdFromOIDCProviderResponse:
        """
        @summary Removes a client ID from an OpenID Connect (OIDC) identity provider (IdP).
        
        @description ###
        This topic provides an example on how to remove the client ID `498469743454717***` from the OIDC IdP named `TestOIDCProvider`.
        
        @param request: RemoveClientIdFromOIDCProviderRequest
        @return: RemoveClientIdFromOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_client_id_from_oidcprovider_with_options(request, runtime)

    async def remove_client_id_from_oidcprovider_async(
        self,
        request: ims_20190815_models.RemoveClientIdFromOIDCProviderRequest,
    ) -> ims_20190815_models.RemoveClientIdFromOIDCProviderResponse:
        """
        @summary Removes a client ID from an OpenID Connect (OIDC) identity provider (IdP).
        
        @description ###
        This topic provides an example on how to remove the client ID `498469743454717***` from the OIDC IdP named `TestOIDCProvider`.
        
        @param request: RemoveClientIdFromOIDCProviderRequest
        @return: RemoveClientIdFromOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_client_id_from_oidcprovider_with_options_async(request, runtime)

    def remove_fingerprint_from_oidcprovider_with_options(
        self,
        request: ims_20190815_models.RemoveFingerprintFromOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.RemoveFingerprintFromOIDCProviderResponse:
        """
        @summary Removes a fingerprint from an OpenID Connect (OIDC) identity provider (IdP).
        
        @description ###
        This topic provides an example on how to remove the fingerprint `6938fd4d98bab03faadb97b34396831e3780***` from the OIDC IdP named `TestOIDCProvider`.
        
        @param request: RemoveFingerprintFromOIDCProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveFingerprintFromOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fingerprint):
            query['Fingerprint'] = request.fingerprint
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveFingerprintFromOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.RemoveFingerprintFromOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_fingerprint_from_oidcprovider_with_options_async(
        self,
        request: ims_20190815_models.RemoveFingerprintFromOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.RemoveFingerprintFromOIDCProviderResponse:
        """
        @summary Removes a fingerprint from an OpenID Connect (OIDC) identity provider (IdP).
        
        @description ###
        This topic provides an example on how to remove the fingerprint `6938fd4d98bab03faadb97b34396831e3780***` from the OIDC IdP named `TestOIDCProvider`.
        
        @param request: RemoveFingerprintFromOIDCProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveFingerprintFromOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fingerprint):
            query['Fingerprint'] = request.fingerprint
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveFingerprintFromOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.RemoveFingerprintFromOIDCProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_fingerprint_from_oidcprovider(
        self,
        request: ims_20190815_models.RemoveFingerprintFromOIDCProviderRequest,
    ) -> ims_20190815_models.RemoveFingerprintFromOIDCProviderResponse:
        """
        @summary Removes a fingerprint from an OpenID Connect (OIDC) identity provider (IdP).
        
        @description ###
        This topic provides an example on how to remove the fingerprint `6938fd4d98bab03faadb97b34396831e3780***` from the OIDC IdP named `TestOIDCProvider`.
        
        @param request: RemoveFingerprintFromOIDCProviderRequest
        @return: RemoveFingerprintFromOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_fingerprint_from_oidcprovider_with_options(request, runtime)

    async def remove_fingerprint_from_oidcprovider_async(
        self,
        request: ims_20190815_models.RemoveFingerprintFromOIDCProviderRequest,
    ) -> ims_20190815_models.RemoveFingerprintFromOIDCProviderResponse:
        """
        @summary Removes a fingerprint from an OpenID Connect (OIDC) identity provider (IdP).
        
        @description ###
        This topic provides an example on how to remove the fingerprint `6938fd4d98bab03faadb97b34396831e3780***` from the OIDC IdP named `TestOIDCProvider`.
        
        @param request: RemoveFingerprintFromOIDCProviderRequest
        @return: RemoveFingerprintFromOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_fingerprint_from_oidcprovider_with_options_async(request, runtime)

    def remove_user_from_group_with_options(
        self,
        request: ims_20190815_models.RemoveUserFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.RemoveUserFromGroupResponse:
        """
        @summary Removes a Resource Access Management (RAM) user from a RAM user group.
        
        @param request: RemoveUserFromGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUserFromGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUserFromGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.RemoveUserFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_user_from_group_with_options_async(
        self,
        request: ims_20190815_models.RemoveUserFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.RemoveUserFromGroupResponse:
        """
        @summary Removes a Resource Access Management (RAM) user from a RAM user group.
        
        @param request: RemoveUserFromGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUserFromGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUserFromGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.RemoveUserFromGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_user_from_group(
        self,
        request: ims_20190815_models.RemoveUserFromGroupRequest,
    ) -> ims_20190815_models.RemoveUserFromGroupResponse:
        """
        @summary Removes a Resource Access Management (RAM) user from a RAM user group.
        
        @param request: RemoveUserFromGroupRequest
        @return: RemoveUserFromGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_user_from_group_with_options(request, runtime)

    async def remove_user_from_group_async(
        self,
        request: ims_20190815_models.RemoveUserFromGroupRequest,
    ) -> ims_20190815_models.RemoveUserFromGroupResponse:
        """
        @summary Removes a Resource Access Management (RAM) user from a RAM user group.
        
        @param request: RemoveUserFromGroupRequest
        @return: RemoveUserFromGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_user_from_group_with_options_async(request, runtime)

    def restore_access_key_from_recycle_bin_with_options(
        self,
        request: ims_20190815_models.RestoreAccessKeyFromRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.RestoreAccessKeyFromRecycleBinResponse:
        """
        @summary Restores a specific AccessKey pair that belongs to a Resource Access Management (RAM) user from the recycle bin.
        
        @param request: RestoreAccessKeyFromRecycleBinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestoreAccessKeyFromRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreAccessKeyFromRecycleBin',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.RestoreAccessKeyFromRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_access_key_from_recycle_bin_with_options_async(
        self,
        request: ims_20190815_models.RestoreAccessKeyFromRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.RestoreAccessKeyFromRecycleBinResponse:
        """
        @summary Restores a specific AccessKey pair that belongs to a Resource Access Management (RAM) user from the recycle bin.
        
        @param request: RestoreAccessKeyFromRecycleBinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestoreAccessKeyFromRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreAccessKeyFromRecycleBin',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.RestoreAccessKeyFromRecycleBinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restore_access_key_from_recycle_bin(
        self,
        request: ims_20190815_models.RestoreAccessKeyFromRecycleBinRequest,
    ) -> ims_20190815_models.RestoreAccessKeyFromRecycleBinResponse:
        """
        @summary Restores a specific AccessKey pair that belongs to a Resource Access Management (RAM) user from the recycle bin.
        
        @param request: RestoreAccessKeyFromRecycleBinRequest
        @return: RestoreAccessKeyFromRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restore_access_key_from_recycle_bin_with_options(request, runtime)

    async def restore_access_key_from_recycle_bin_async(
        self,
        request: ims_20190815_models.RestoreAccessKeyFromRecycleBinRequest,
    ) -> ims_20190815_models.RestoreAccessKeyFromRecycleBinResponse:
        """
        @summary Restores a specific AccessKey pair that belongs to a Resource Access Management (RAM) user from the recycle bin.
        
        @param request: RestoreAccessKeyFromRecycleBinRequest
        @return: RestoreAccessKeyFromRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restore_access_key_from_recycle_bin_with_options_async(request, runtime)

    def restore_user_from_recycle_bin_with_options(
        self,
        request: ims_20190815_models.RestoreUserFromRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.RestoreUserFromRecycleBinResponse:
        """
        @summary Restores a specific Resource Access Management (RAM) user from the recycle bin.
        
        @param request: RestoreUserFromRecycleBinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestoreUserFromRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreUserFromRecycleBin',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.RestoreUserFromRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_user_from_recycle_bin_with_options_async(
        self,
        request: ims_20190815_models.RestoreUserFromRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.RestoreUserFromRecycleBinResponse:
        """
        @summary Restores a specific Resource Access Management (RAM) user from the recycle bin.
        
        @param request: RestoreUserFromRecycleBinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestoreUserFromRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreUserFromRecycleBin',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.RestoreUserFromRecycleBinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restore_user_from_recycle_bin(
        self,
        request: ims_20190815_models.RestoreUserFromRecycleBinRequest,
    ) -> ims_20190815_models.RestoreUserFromRecycleBinResponse:
        """
        @summary Restores a specific Resource Access Management (RAM) user from the recycle bin.
        
        @param request: RestoreUserFromRecycleBinRequest
        @return: RestoreUserFromRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restore_user_from_recycle_bin_with_options(request, runtime)

    async def restore_user_from_recycle_bin_async(
        self,
        request: ims_20190815_models.RestoreUserFromRecycleBinRequest,
    ) -> ims_20190815_models.RestoreUserFromRecycleBinResponse:
        """
        @summary Restores a specific Resource Access Management (RAM) user from the recycle bin.
        
        @param request: RestoreUserFromRecycleBinRequest
        @return: RestoreUserFromRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restore_user_from_recycle_bin_with_options_async(request, runtime)

    def set_default_domain_with_options(
        self,
        request: ims_20190815_models.SetDefaultDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetDefaultDomainResponse:
        """
        @summary Configures the default domain name for an Alibaba Cloud account.
        
        @param request: SetDefaultDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDefaultDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_domain_name):
            query['DefaultDomainName'] = request.default_domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultDomain',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.SetDefaultDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_default_domain_with_options_async(
        self,
        request: ims_20190815_models.SetDefaultDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetDefaultDomainResponse:
        """
        @summary Configures the default domain name for an Alibaba Cloud account.
        
        @param request: SetDefaultDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDefaultDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_domain_name):
            query['DefaultDomainName'] = request.default_domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultDomain',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.SetDefaultDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_default_domain(
        self,
        request: ims_20190815_models.SetDefaultDomainRequest,
    ) -> ims_20190815_models.SetDefaultDomainResponse:
        """
        @summary Configures the default domain name for an Alibaba Cloud account.
        
        @param request: SetDefaultDomainRequest
        @return: SetDefaultDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_default_domain_with_options(request, runtime)

    async def set_default_domain_async(
        self,
        request: ims_20190815_models.SetDefaultDomainRequest,
    ) -> ims_20190815_models.SetDefaultDomainResponse:
        """
        @summary Configures the default domain name for an Alibaba Cloud account.
        
        @param request: SetDefaultDomainRequest
        @return: SetDefaultDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_default_domain_with_options_async(request, runtime)

    def set_password_policy_with_options(
        self,
        request: ims_20190815_models.SetPasswordPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetPasswordPolicyResponse:
        """
        @summary Configures the password policy for Resource Access Management (RAM) users.
        
        @param request: SetPasswordPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPasswordPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hard_expire):
            query['HardExpire'] = request.hard_expire
        if not UtilClient.is_unset(request.max_login_attemps):
            query['MaxLoginAttemps'] = request.max_login_attemps
        if not UtilClient.is_unset(request.max_password_age):
            query['MaxPasswordAge'] = request.max_password_age
        if not UtilClient.is_unset(request.minimum_password_different_character):
            query['MinimumPasswordDifferentCharacter'] = request.minimum_password_different_character
        if not UtilClient.is_unset(request.minimum_password_length):
            query['MinimumPasswordLength'] = request.minimum_password_length
        if not UtilClient.is_unset(request.password_not_contain_user_name):
            query['PasswordNotContainUserName'] = request.password_not_contain_user_name
        if not UtilClient.is_unset(request.password_reuse_prevention):
            query['PasswordReusePrevention'] = request.password_reuse_prevention
        if not UtilClient.is_unset(request.require_lowercase_characters):
            query['RequireLowercaseCharacters'] = request.require_lowercase_characters
        if not UtilClient.is_unset(request.require_numbers):
            query['RequireNumbers'] = request.require_numbers
        if not UtilClient.is_unset(request.require_symbols):
            query['RequireSymbols'] = request.require_symbols
        if not UtilClient.is_unset(request.require_uppercase_characters):
            query['RequireUppercaseCharacters'] = request.require_uppercase_characters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPasswordPolicy',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.SetPasswordPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_password_policy_with_options_async(
        self,
        request: ims_20190815_models.SetPasswordPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetPasswordPolicyResponse:
        """
        @summary Configures the password policy for Resource Access Management (RAM) users.
        
        @param request: SetPasswordPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPasswordPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hard_expire):
            query['HardExpire'] = request.hard_expire
        if not UtilClient.is_unset(request.max_login_attemps):
            query['MaxLoginAttemps'] = request.max_login_attemps
        if not UtilClient.is_unset(request.max_password_age):
            query['MaxPasswordAge'] = request.max_password_age
        if not UtilClient.is_unset(request.minimum_password_different_character):
            query['MinimumPasswordDifferentCharacter'] = request.minimum_password_different_character
        if not UtilClient.is_unset(request.minimum_password_length):
            query['MinimumPasswordLength'] = request.minimum_password_length
        if not UtilClient.is_unset(request.password_not_contain_user_name):
            query['PasswordNotContainUserName'] = request.password_not_contain_user_name
        if not UtilClient.is_unset(request.password_reuse_prevention):
            query['PasswordReusePrevention'] = request.password_reuse_prevention
        if not UtilClient.is_unset(request.require_lowercase_characters):
            query['RequireLowercaseCharacters'] = request.require_lowercase_characters
        if not UtilClient.is_unset(request.require_numbers):
            query['RequireNumbers'] = request.require_numbers
        if not UtilClient.is_unset(request.require_symbols):
            query['RequireSymbols'] = request.require_symbols
        if not UtilClient.is_unset(request.require_uppercase_characters):
            query['RequireUppercaseCharacters'] = request.require_uppercase_characters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPasswordPolicy',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.SetPasswordPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_password_policy(
        self,
        request: ims_20190815_models.SetPasswordPolicyRequest,
    ) -> ims_20190815_models.SetPasswordPolicyResponse:
        """
        @summary Configures the password policy for Resource Access Management (RAM) users.
        
        @param request: SetPasswordPolicyRequest
        @return: SetPasswordPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_password_policy_with_options(request, runtime)

    async def set_password_policy_async(
        self,
        request: ims_20190815_models.SetPasswordPolicyRequest,
    ) -> ims_20190815_models.SetPasswordPolicyResponse:
        """
        @summary Configures the password policy for Resource Access Management (RAM) users.
        
        @param request: SetPasswordPolicyRequest
        @return: SetPasswordPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_password_policy_with_options_async(request, runtime)

    def set_security_preference_with_options(
        self,
        tmp_req: ims_20190815_models.SetSecurityPreferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetSecurityPreferenceResponse:
        """
        @summary Configures security preferences for a RAM user.
        
        @description ###
        This topic provides an example on how to enable multi-factor authentication (MFA) only for RAM users who initiated unusual logons.
        
        @param tmp_req: SetSecurityPreferenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSecurityPreferenceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ims_20190815_models.SetSecurityPreferenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.verification_types):
            request.verification_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.verification_types, 'VerificationTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.allow_user_to_change_password):
            query['AllowUserToChangePassword'] = request.allow_user_to_change_password
        if not UtilClient.is_unset(request.allow_user_to_login_with_passkey):
            query['AllowUserToLoginWithPasskey'] = request.allow_user_to_login_with_passkey
        if not UtilClient.is_unset(request.allow_user_to_manage_access_keys):
            query['AllowUserToManageAccessKeys'] = request.allow_user_to_manage_access_keys
        if not UtilClient.is_unset(request.allow_user_to_manage_mfadevices):
            query['AllowUserToManageMFADevices'] = request.allow_user_to_manage_mfadevices
        if not UtilClient.is_unset(request.allow_user_to_manage_personal_ding_talk):
            query['AllowUserToManagePersonalDingTalk'] = request.allow_user_to_manage_personal_ding_talk
        if not UtilClient.is_unset(request.enable_save_mfaticket):
            query['EnableSaveMFATicket'] = request.enable_save_mfaticket
        if not UtilClient.is_unset(request.login_network_masks):
            query['LoginNetworkMasks'] = request.login_network_masks
        if not UtilClient.is_unset(request.login_session_duration):
            query['LoginSessionDuration'] = request.login_session_duration
        if not UtilClient.is_unset(request.mfaoperation_for_login):
            query['MFAOperationForLogin'] = request.mfaoperation_for_login
        if not UtilClient.is_unset(request.operation_for_risk_login):
            query['OperationForRiskLogin'] = request.operation_for_risk_login
        if not UtilClient.is_unset(request.verification_types_shrink):
            query['VerificationTypes'] = request.verification_types_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSecurityPreference',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.SetSecurityPreferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_security_preference_with_options_async(
        self,
        tmp_req: ims_20190815_models.SetSecurityPreferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetSecurityPreferenceResponse:
        """
        @summary Configures security preferences for a RAM user.
        
        @description ###
        This topic provides an example on how to enable multi-factor authentication (MFA) only for RAM users who initiated unusual logons.
        
        @param tmp_req: SetSecurityPreferenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSecurityPreferenceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ims_20190815_models.SetSecurityPreferenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.verification_types):
            request.verification_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.verification_types, 'VerificationTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.allow_user_to_change_password):
            query['AllowUserToChangePassword'] = request.allow_user_to_change_password
        if not UtilClient.is_unset(request.allow_user_to_login_with_passkey):
            query['AllowUserToLoginWithPasskey'] = request.allow_user_to_login_with_passkey
        if not UtilClient.is_unset(request.allow_user_to_manage_access_keys):
            query['AllowUserToManageAccessKeys'] = request.allow_user_to_manage_access_keys
        if not UtilClient.is_unset(request.allow_user_to_manage_mfadevices):
            query['AllowUserToManageMFADevices'] = request.allow_user_to_manage_mfadevices
        if not UtilClient.is_unset(request.allow_user_to_manage_personal_ding_talk):
            query['AllowUserToManagePersonalDingTalk'] = request.allow_user_to_manage_personal_ding_talk
        if not UtilClient.is_unset(request.enable_save_mfaticket):
            query['EnableSaveMFATicket'] = request.enable_save_mfaticket
        if not UtilClient.is_unset(request.login_network_masks):
            query['LoginNetworkMasks'] = request.login_network_masks
        if not UtilClient.is_unset(request.login_session_duration):
            query['LoginSessionDuration'] = request.login_session_duration
        if not UtilClient.is_unset(request.mfaoperation_for_login):
            query['MFAOperationForLogin'] = request.mfaoperation_for_login
        if not UtilClient.is_unset(request.operation_for_risk_login):
            query['OperationForRiskLogin'] = request.operation_for_risk_login
        if not UtilClient.is_unset(request.verification_types_shrink):
            query['VerificationTypes'] = request.verification_types_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSecurityPreference',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.SetSecurityPreferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_security_preference(
        self,
        request: ims_20190815_models.SetSecurityPreferenceRequest,
    ) -> ims_20190815_models.SetSecurityPreferenceResponse:
        """
        @summary Configures security preferences for a RAM user.
        
        @description ###
        This topic provides an example on how to enable multi-factor authentication (MFA) only for RAM users who initiated unusual logons.
        
        @param request: SetSecurityPreferenceRequest
        @return: SetSecurityPreferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_security_preference_with_options(request, runtime)

    async def set_security_preference_async(
        self,
        request: ims_20190815_models.SetSecurityPreferenceRequest,
    ) -> ims_20190815_models.SetSecurityPreferenceResponse:
        """
        @summary Configures security preferences for a RAM user.
        
        @description ###
        This topic provides an example on how to enable multi-factor authentication (MFA) only for RAM users who initiated unusual logons.
        
        @param request: SetSecurityPreferenceRequest
        @return: SetSecurityPreferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_security_preference_with_options_async(request, runtime)

    def set_user_sso_settings_with_options(
        self,
        request: ims_20190815_models.SetUserSsoSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetUserSsoSettingsResponse:
        """
        @summary Configures information about user-based single sign-on (SSO).
        
        @param request: SetUserSsoSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetUserSsoSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auxiliary_domain):
            query['AuxiliaryDomain'] = request.auxiliary_domain
        if not UtilClient.is_unset(request.metadata_document):
            query['MetadataDocument'] = request.metadata_document
        if not UtilClient.is_unset(request.sso_enabled):
            query['SsoEnabled'] = request.sso_enabled
        if not UtilClient.is_unset(request.sso_login_with_domain):
            query['SsoLoginWithDomain'] = request.sso_login_with_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetUserSsoSettings',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.SetUserSsoSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_user_sso_settings_with_options_async(
        self,
        request: ims_20190815_models.SetUserSsoSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetUserSsoSettingsResponse:
        """
        @summary Configures information about user-based single sign-on (SSO).
        
        @param request: SetUserSsoSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetUserSsoSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auxiliary_domain):
            query['AuxiliaryDomain'] = request.auxiliary_domain
        if not UtilClient.is_unset(request.metadata_document):
            query['MetadataDocument'] = request.metadata_document
        if not UtilClient.is_unset(request.sso_enabled):
            query['SsoEnabled'] = request.sso_enabled
        if not UtilClient.is_unset(request.sso_login_with_domain):
            query['SsoLoginWithDomain'] = request.sso_login_with_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetUserSsoSettings',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.SetUserSsoSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_user_sso_settings(
        self,
        request: ims_20190815_models.SetUserSsoSettingsRequest,
    ) -> ims_20190815_models.SetUserSsoSettingsResponse:
        """
        @summary Configures information about user-based single sign-on (SSO).
        
        @param request: SetUserSsoSettingsRequest
        @return: SetUserSsoSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_user_sso_settings_with_options(request, runtime)

    async def set_user_sso_settings_async(
        self,
        request: ims_20190815_models.SetUserSsoSettingsRequest,
    ) -> ims_20190815_models.SetUserSsoSettingsResponse:
        """
        @summary Configures information about user-based single sign-on (SSO).
        
        @param request: SetUserSsoSettingsRequest
        @return: SetUserSsoSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_user_sso_settings_with_options_async(request, runtime)

    def set_verification_info_with_options(
        self,
        request: ims_20190815_models.SetVerificationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetVerificationInfoResponse:
        """
        @summary Binds a mobile phone or email to a Resource Access Management (RAM) user.
        
        @param request: SetVerificationInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetVerificationInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.mobile_phone):
            query['MobilePhone'] = request.mobile_phone
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        if not UtilClient.is_unset(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetVerificationInfo',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.SetVerificationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_verification_info_with_options_async(
        self,
        request: ims_20190815_models.SetVerificationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.SetVerificationInfoResponse:
        """
        @summary Binds a mobile phone or email to a Resource Access Management (RAM) user.
        
        @param request: SetVerificationInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetVerificationInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.mobile_phone):
            query['MobilePhone'] = request.mobile_phone
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        if not UtilClient.is_unset(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetVerificationInfo',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.SetVerificationInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_verification_info(
        self,
        request: ims_20190815_models.SetVerificationInfoRequest,
    ) -> ims_20190815_models.SetVerificationInfoResponse:
        """
        @summary Binds a mobile phone or email to a Resource Access Management (RAM) user.
        
        @param request: SetVerificationInfoRequest
        @return: SetVerificationInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_verification_info_with_options(request, runtime)

    async def set_verification_info_async(
        self,
        request: ims_20190815_models.SetVerificationInfoRequest,
    ) -> ims_20190815_models.SetVerificationInfoResponse:
        """
        @summary Binds a mobile phone or email to a Resource Access Management (RAM) user.
        
        @param request: SetVerificationInfoRequest
        @return: SetVerificationInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_verification_info_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ims_20190815_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_principal_name):
            query['ResourcePrincipalName'] = request.resource_principal_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ims_20190815_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_principal_name):
            query['ResourcePrincipalName'] = request.resource_principal_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: ims_20190815_models.TagResourcesRequest,
    ) -> ims_20190815_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ims_20190815_models.TagResourcesRequest,
    ) -> ims_20190815_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def unbind_mfadevice_with_options(
        self,
        request: ims_20190815_models.UnbindMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UnbindMFADeviceResponse:
        """
        @summary Unbinds a multi-factor authentication (MFA) device from a Resource Access Management (RAM) user.
        
        @param request: UnbindMFADeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindMFADeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindMFADevice',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UnbindMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_mfadevice_with_options_async(
        self,
        request: ims_20190815_models.UnbindMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UnbindMFADeviceResponse:
        """
        @summary Unbinds a multi-factor authentication (MFA) device from a Resource Access Management (RAM) user.
        
        @param request: UnbindMFADeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindMFADeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindMFADevice',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UnbindMFADeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_mfadevice(
        self,
        request: ims_20190815_models.UnbindMFADeviceRequest,
    ) -> ims_20190815_models.UnbindMFADeviceResponse:
        """
        @summary Unbinds a multi-factor authentication (MFA) device from a Resource Access Management (RAM) user.
        
        @param request: UnbindMFADeviceRequest
        @return: UnbindMFADeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_mfadevice_with_options(request, runtime)

    async def unbind_mfadevice_async(
        self,
        request: ims_20190815_models.UnbindMFADeviceRequest,
    ) -> ims_20190815_models.UnbindMFADeviceResponse:
        """
        @summary Unbinds a multi-factor authentication (MFA) device from a Resource Access Management (RAM) user.
        
        @param request: UnbindMFADeviceRequest
        @return: UnbindMFADeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_mfadevice_with_options_async(request, runtime)

    def unbind_verification_with_options(
        self,
        request: ims_20190815_models.UnbindVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UnbindVerificationResponse:
        """
        @summary Unbinds a mobile phone or email from a Resource Access Management (RAM) user.
        
        @param request: UnbindVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.mobile_phone):
            query['MobilePhone'] = request.mobile_phone
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        if not UtilClient.is_unset(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindVerification',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UnbindVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_verification_with_options_async(
        self,
        request: ims_20190815_models.UnbindVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UnbindVerificationResponse:
        """
        @summary Unbinds a mobile phone or email from a Resource Access Management (RAM) user.
        
        @param request: UnbindVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.mobile_phone):
            query['MobilePhone'] = request.mobile_phone
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        if not UtilClient.is_unset(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindVerification',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UnbindVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_verification(
        self,
        request: ims_20190815_models.UnbindVerificationRequest,
    ) -> ims_20190815_models.UnbindVerificationResponse:
        """
        @summary Unbinds a mobile phone or email from a Resource Access Management (RAM) user.
        
        @param request: UnbindVerificationRequest
        @return: UnbindVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_verification_with_options(request, runtime)

    async def unbind_verification_async(
        self,
        request: ims_20190815_models.UnbindVerificationRequest,
    ) -> ims_20190815_models.UnbindVerificationResponse:
        """
        @summary Unbinds a mobile phone or email from a Resource Access Management (RAM) user.
        
        @param request: UnbindVerificationRequest
        @return: UnbindVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_verification_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ims_20190815_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UntagResourcesResponse:
        """
        @summary Removes tags from a resource.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_principal_name):
            query['ResourcePrincipalName'] = request.resource_principal_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ims_20190815_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UntagResourcesResponse:
        """
        @summary Removes tags from a resource.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_principal_name):
            query['ResourcePrincipalName'] = request.resource_principal_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: ims_20190815_models.UntagResourcesRequest,
    ) -> ims_20190815_models.UntagResourcesResponse:
        """
        @summary Removes tags from a resource.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ims_20190815_models.UntagResourcesRequest,
    ) -> ims_20190815_models.UntagResourcesResponse:
        """
        @summary Removes tags from a resource.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_access_key_with_options(
        self,
        request: ims_20190815_models.UpdateAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateAccessKeyResponse:
        """
        @summary Modifies the status of an AccessKey pair for an Alibaba Cloud account or a Resource Access Management (RAM) user.
        
        @param request: UpdateAccessKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAccessKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccessKey',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateAccessKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_access_key_with_options_async(
        self,
        request: ims_20190815_models.UpdateAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateAccessKeyResponse:
        """
        @summary Modifies the status of an AccessKey pair for an Alibaba Cloud account or a Resource Access Management (RAM) user.
        
        @param request: UpdateAccessKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAccessKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccessKey',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateAccessKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_access_key(
        self,
        request: ims_20190815_models.UpdateAccessKeyRequest,
    ) -> ims_20190815_models.UpdateAccessKeyResponse:
        """
        @summary Modifies the status of an AccessKey pair for an Alibaba Cloud account or a Resource Access Management (RAM) user.
        
        @param request: UpdateAccessKeyRequest
        @return: UpdateAccessKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_access_key_with_options(request, runtime)

    async def update_access_key_async(
        self,
        request: ims_20190815_models.UpdateAccessKeyRequest,
    ) -> ims_20190815_models.UpdateAccessKeyResponse:
        """
        @summary Modifies the status of an AccessKey pair for an Alibaba Cloud account or a Resource Access Management (RAM) user.
        
        @param request: UpdateAccessKeyRequest
        @return: UpdateAccessKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_access_key_with_options_async(request, runtime)

    def update_application_with_options(
        self,
        request: ims_20190815_models.UpdateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateApplicationResponse:
        """
        @summary Modifies the information about a specified application.
        
        @param request: UpdateApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.new_access_token_validity):
            query['NewAccessTokenValidity'] = request.new_access_token_validity
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not UtilClient.is_unset(request.new_is_multi_tenant):
            query['NewIsMultiTenant'] = request.new_is_multi_tenant
        if not UtilClient.is_unset(request.new_predefined_scopes):
            query['NewPredefinedScopes'] = request.new_predefined_scopes
        if not UtilClient.is_unset(request.new_redirect_uris):
            query['NewRedirectUris'] = request.new_redirect_uris
        if not UtilClient.is_unset(request.new_refresh_token_validity):
            query['NewRefreshTokenValidity'] = request.new_refresh_token_validity
        if not UtilClient.is_unset(request.new_required_scopes):
            query['NewRequiredScopes'] = request.new_required_scopes
        if not UtilClient.is_unset(request.new_secret_required):
            query['NewSecretRequired'] = request.new_secret_required
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_with_options_async(
        self,
        request: ims_20190815_models.UpdateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateApplicationResponse:
        """
        @summary Modifies the information about a specified application.
        
        @param request: UpdateApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.new_access_token_validity):
            query['NewAccessTokenValidity'] = request.new_access_token_validity
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not UtilClient.is_unset(request.new_is_multi_tenant):
            query['NewIsMultiTenant'] = request.new_is_multi_tenant
        if not UtilClient.is_unset(request.new_predefined_scopes):
            query['NewPredefinedScopes'] = request.new_predefined_scopes
        if not UtilClient.is_unset(request.new_redirect_uris):
            query['NewRedirectUris'] = request.new_redirect_uris
        if not UtilClient.is_unset(request.new_refresh_token_validity):
            query['NewRefreshTokenValidity'] = request.new_refresh_token_validity
        if not UtilClient.is_unset(request.new_required_scopes):
            query['NewRequiredScopes'] = request.new_required_scopes
        if not UtilClient.is_unset(request.new_secret_required):
            query['NewSecretRequired'] = request.new_secret_required
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application(
        self,
        request: ims_20190815_models.UpdateApplicationRequest,
    ) -> ims_20190815_models.UpdateApplicationResponse:
        """
        @summary Modifies the information about a specified application.
        
        @param request: UpdateApplicationRequest
        @return: UpdateApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_application_with_options(request, runtime)

    async def update_application_async(
        self,
        request: ims_20190815_models.UpdateApplicationRequest,
    ) -> ims_20190815_models.UpdateApplicationResponse:
        """
        @summary Modifies the information about a specified application.
        
        @param request: UpdateApplicationRequest
        @return: UpdateApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_application_with_options_async(request, runtime)

    def update_group_with_options(
        self,
        request: ims_20190815_models.UpdateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateGroupResponse:
        """
        @summary Modifies information about a Resource Access Management (RAM) user group.
        
        @param request: UpdateGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.new_comments):
            query['NewComments'] = request.new_comments
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not UtilClient.is_unset(request.new_group_name):
            query['NewGroupName'] = request.new_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_group_with_options_async(
        self,
        request: ims_20190815_models.UpdateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateGroupResponse:
        """
        @summary Modifies information about a Resource Access Management (RAM) user group.
        
        @param request: UpdateGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.new_comments):
            query['NewComments'] = request.new_comments
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not UtilClient.is_unset(request.new_group_name):
            query['NewGroupName'] = request.new_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_group(
        self,
        request: ims_20190815_models.UpdateGroupRequest,
    ) -> ims_20190815_models.UpdateGroupResponse:
        """
        @summary Modifies information about a Resource Access Management (RAM) user group.
        
        @param request: UpdateGroupRequest
        @return: UpdateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_group_with_options(request, runtime)

    async def update_group_async(
        self,
        request: ims_20190815_models.UpdateGroupRequest,
    ) -> ims_20190815_models.UpdateGroupResponse:
        """
        @summary Modifies information about a Resource Access Management (RAM) user group.
        
        @param request: UpdateGroupRequest
        @return: UpdateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_group_with_options_async(request, runtime)

    def update_login_profile_with_options(
        self,
        request: ims_20190815_models.UpdateLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateLoginProfileResponse:
        """
        @summary Modifies the console logon configurations of a Resource Access Management (RAM) user.
        
        @param request: UpdateLoginProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoginProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mfabind_required):
            query['MFABindRequired'] = request.mfabind_required
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_reset_required):
            query['PasswordResetRequired'] = request.password_reset_required
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLoginProfile',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateLoginProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_login_profile_with_options_async(
        self,
        request: ims_20190815_models.UpdateLoginProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateLoginProfileResponse:
        """
        @summary Modifies the console logon configurations of a Resource Access Management (RAM) user.
        
        @param request: UpdateLoginProfileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoginProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mfabind_required):
            query['MFABindRequired'] = request.mfabind_required
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_reset_required):
            query['PasswordResetRequired'] = request.password_reset_required
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLoginProfile',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateLoginProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_login_profile(
        self,
        request: ims_20190815_models.UpdateLoginProfileRequest,
    ) -> ims_20190815_models.UpdateLoginProfileResponse:
        """
        @summary Modifies the console logon configurations of a Resource Access Management (RAM) user.
        
        @param request: UpdateLoginProfileRequest
        @return: UpdateLoginProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_login_profile_with_options(request, runtime)

    async def update_login_profile_async(
        self,
        request: ims_20190815_models.UpdateLoginProfileRequest,
    ) -> ims_20190815_models.UpdateLoginProfileResponse:
        """
        @summary Modifies the console logon configurations of a Resource Access Management (RAM) user.
        
        @param request: UpdateLoginProfileRequest
        @return: UpdateLoginProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_login_profile_with_options_async(request, runtime)

    def update_oidcprovider_with_options(
        self,
        request: ims_20190815_models.UpdateOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateOIDCProviderResponse:
        """
        @summary Modifies the description and client IDs of an OpenID Connect (OIDC) identity provider (IdP).
        
        @description ###
        This topic provides an example on how to change the description of the OIDC IdP named `TestOIDCProvider` to `This is a new OIDC Provider.`
        
        @param request: UpdateOIDCProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ids):
            query['ClientIds'] = request.client_ids
        if not UtilClient.is_unset(request.issuance_limit_time):
            query['IssuanceLimitTime'] = request.issuance_limit_time
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_oidcprovider_with_options_async(
        self,
        request: ims_20190815_models.UpdateOIDCProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateOIDCProviderResponse:
        """
        @summary Modifies the description and client IDs of an OpenID Connect (OIDC) identity provider (IdP).
        
        @description ###
        This topic provides an example on how to change the description of the OIDC IdP named `TestOIDCProvider` to `This is a new OIDC Provider.`
        
        @param request: UpdateOIDCProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ids):
            query['ClientIds'] = request.client_ids
        if not UtilClient.is_unset(request.issuance_limit_time):
            query['IssuanceLimitTime'] = request.issuance_limit_time
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateOIDCProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_oidcprovider(
        self,
        request: ims_20190815_models.UpdateOIDCProviderRequest,
    ) -> ims_20190815_models.UpdateOIDCProviderResponse:
        """
        @summary Modifies the description and client IDs of an OpenID Connect (OIDC) identity provider (IdP).
        
        @description ###
        This topic provides an example on how to change the description of the OIDC IdP named `TestOIDCProvider` to `This is a new OIDC Provider.`
        
        @param request: UpdateOIDCProviderRequest
        @return: UpdateOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_oidcprovider_with_options(request, runtime)

    async def update_oidcprovider_async(
        self,
        request: ims_20190815_models.UpdateOIDCProviderRequest,
    ) -> ims_20190815_models.UpdateOIDCProviderResponse:
        """
        @summary Modifies the description and client IDs of an OpenID Connect (OIDC) identity provider (IdP).
        
        @description ###
        This topic provides an example on how to change the description of the OIDC IdP named `TestOIDCProvider` to `This is a new OIDC Provider.`
        
        @param request: UpdateOIDCProviderRequest
        @return: UpdateOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_oidcprovider_with_options_async(request, runtime)

    def update_passkey_with_options(
        self,
        request: ims_20190815_models.UpdatePasskeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdatePasskeyResponse:
        """
        @summary Updates the name of a passkey.
        
        @param request: UpdatePasskeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePasskeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.passkey_id):
            query['PasskeyId'] = request.passkey_id
        if not UtilClient.is_unset(request.passkey_name):
            query['PasskeyName'] = request.passkey_name
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePasskey',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdatePasskeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_passkey_with_options_async(
        self,
        request: ims_20190815_models.UpdatePasskeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdatePasskeyResponse:
        """
        @summary Updates the name of a passkey.
        
        @param request: UpdatePasskeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePasskeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.passkey_id):
            query['PasskeyId'] = request.passkey_id
        if not UtilClient.is_unset(request.passkey_name):
            query['PasskeyName'] = request.passkey_name
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePasskey',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdatePasskeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_passkey(
        self,
        request: ims_20190815_models.UpdatePasskeyRequest,
    ) -> ims_20190815_models.UpdatePasskeyResponse:
        """
        @summary Updates the name of a passkey.
        
        @param request: UpdatePasskeyRequest
        @return: UpdatePasskeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_passkey_with_options(request, runtime)

    async def update_passkey_async(
        self,
        request: ims_20190815_models.UpdatePasskeyRequest,
    ) -> ims_20190815_models.UpdatePasskeyResponse:
        """
        @summary Updates the name of a passkey.
        
        @param request: UpdatePasskeyRequest
        @return: UpdatePasskeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_passkey_with_options_async(request, runtime)

    def update_samlprovider_with_options(
        self,
        request: ims_20190815_models.UpdateSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateSAMLProviderResponse:
        """
        @summary Modifies information about an identity provider (IdP) for role-based single sign-on (SSO).
        
        @description This topic provides an example on how to change the description of an IdP named `test-provider` to `This is a new provider.`
        
        @param request: UpdateSAMLProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSAMLProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_encoded_samlmetadata_document):
            query['NewEncodedSAMLMetadataDocument'] = request.new_encoded_samlmetadata_document
        if not UtilClient.is_unset(request.samlprovider_name):
            query['SAMLProviderName'] = request.samlprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSAMLProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateSAMLProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_samlprovider_with_options_async(
        self,
        request: ims_20190815_models.UpdateSAMLProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateSAMLProviderResponse:
        """
        @summary Modifies information about an identity provider (IdP) for role-based single sign-on (SSO).
        
        @description This topic provides an example on how to change the description of an IdP named `test-provider` to `This is a new provider.`
        
        @param request: UpdateSAMLProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSAMLProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_encoded_samlmetadata_document):
            query['NewEncodedSAMLMetadataDocument'] = request.new_encoded_samlmetadata_document
        if not UtilClient.is_unset(request.samlprovider_name):
            query['SAMLProviderName'] = request.samlprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSAMLProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateSAMLProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_samlprovider(
        self,
        request: ims_20190815_models.UpdateSAMLProviderRequest,
    ) -> ims_20190815_models.UpdateSAMLProviderResponse:
        """
        @summary Modifies information about an identity provider (IdP) for role-based single sign-on (SSO).
        
        @description This topic provides an example on how to change the description of an IdP named `test-provider` to `This is a new provider.`
        
        @param request: UpdateSAMLProviderRequest
        @return: UpdateSAMLProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_samlprovider_with_options(request, runtime)

    async def update_samlprovider_async(
        self,
        request: ims_20190815_models.UpdateSAMLProviderRequest,
    ) -> ims_20190815_models.UpdateSAMLProviderResponse:
        """
        @summary Modifies information about an identity provider (IdP) for role-based single sign-on (SSO).
        
        @description This topic provides an example on how to change the description of an IdP named `test-provider` to `This is a new provider.`
        
        @param request: UpdateSAMLProviderRequest
        @return: UpdateSAMLProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_samlprovider_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: ims_20190815_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateUserResponse:
        """
        @summary Modifies the information about a RAM user.
        
        @description This topic provides an example to show how to modify the name of a RAM user from `test@example.onaliyun.com` to `new@example.onaliyun.com`.
        
        @param request: UpdateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_comments):
            query['NewComments'] = request.new_comments
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not UtilClient.is_unset(request.new_email):
            query['NewEmail'] = request.new_email
        if not UtilClient.is_unset(request.new_mobile_phone):
            query['NewMobilePhone'] = request.new_mobile_phone
        if not UtilClient.is_unset(request.new_user_principal_name):
            query['NewUserPrincipalName'] = request.new_user_principal_name
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: ims_20190815_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ims_20190815_models.UpdateUserResponse:
        """
        @summary Modifies the information about a RAM user.
        
        @description This topic provides an example to show how to modify the name of a RAM user from `test@example.onaliyun.com` to `new@example.onaliyun.com`.
        
        @param request: UpdateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_comments):
            query['NewComments'] = request.new_comments
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not UtilClient.is_unset(request.new_email):
            query['NewEmail'] = request.new_email
        if not UtilClient.is_unset(request.new_mobile_phone):
            query['NewMobilePhone'] = request.new_mobile_phone
        if not UtilClient.is_unset(request.new_user_principal_name):
            query['NewUserPrincipalName'] = request.new_user_principal_name
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        request: ims_20190815_models.UpdateUserRequest,
    ) -> ims_20190815_models.UpdateUserResponse:
        """
        @summary Modifies the information about a RAM user.
        
        @description This topic provides an example to show how to modify the name of a RAM user from `test@example.onaliyun.com` to `new@example.onaliyun.com`.
        
        @param request: UpdateUserRequest
        @return: UpdateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: ims_20190815_models.UpdateUserRequest,
    ) -> ims_20190815_models.UpdateUserResponse:
        """
        @summary Modifies the information about a RAM user.
        
        @description This topic provides an example to show how to modify the name of a RAM user from `test@example.onaliyun.com` to `new@example.onaliyun.com`.
        
        @param request: UpdateUserRequest
        @return: UpdateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)
