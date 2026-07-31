# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class CreateCredentialProviderRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        credential_provider_config: main_models.CreateCredentialProviderRequestCredentialProviderConfig = None,
        credential_provider_identifier: str = None,
        credential_provider_name: str = None,
        credential_provider_type: str = None,
        description: str = None,
        instance_id: str = None,
    ):
        # The idempotency token that ensures the idempotence of the request.
        # 
        # Generate a parameter value from your client to ensure uniqueness across different requests. ClientToken supports only ASCII characters and cannot exceed 64 characters in length. For more information, see References [How to ensure idempotence](https://www.alibabacloud.com/help/zh/ecs/developer-reference/how-to-ensure-idempotence).
        # 
        # This parameter is required.
        self.client_token = client_token
        # The configuration of the credential provider.
        self.credential_provider_config = credential_provider_config
        # The identifier of the credential provider.
        # 
        # > Allowed characters include uppercase and lowercase letters, digits, and the special characters `.-_`. The length cannot exceed 64 characters.
        # 
        # This parameter is required.
        self.credential_provider_identifier = credential_provider_identifier
        # The name of the credential provider.
        # 
        # > The length cannot exceed 64 characters.
        # 
        # This parameter is required.
        self.credential_provider_name = credential_provider_name
        # The type of the credential provider. Valid values:
        # 
        # - oauth: OAuth credential provider.
        # - jwt: JWT credential provider.
        # 
        # This parameter is required.
        self.credential_provider_type = credential_provider_type
        # The description.
        # 
        # > The length cannot exceed 128 characters.
        self.description = description
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        if self.credential_provider_config:
            self.credential_provider_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.credential_provider_config is not None:
            result['CredentialProviderConfig'] = self.credential_provider_config.to_map()

        if self.credential_provider_identifier is not None:
            result['CredentialProviderIdentifier'] = self.credential_provider_identifier

        if self.credential_provider_name is not None:
            result['CredentialProviderName'] = self.credential_provider_name

        if self.credential_provider_type is not None:
            result['CredentialProviderType'] = self.credential_provider_type

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CredentialProviderConfig') is not None:
            temp_model = main_models.CreateCredentialProviderRequestCredentialProviderConfig()
            self.credential_provider_config = temp_model.from_map(m.get('CredentialProviderConfig'))

        if m.get('CredentialProviderIdentifier') is not None:
            self.credential_provider_identifier = m.get('CredentialProviderIdentifier')

        if m.get('CredentialProviderName') is not None:
            self.credential_provider_name = m.get('CredentialProviderName')

        if m.get('CredentialProviderType') is not None:
            self.credential_provider_type = m.get('CredentialProviderType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class CreateCredentialProviderRequestCredentialProviderConfig(DaraModel):
    def __init__(
        self,
        jwt_provider_config: main_models.CreateCredentialProviderRequestCredentialProviderConfigJwtProviderConfig = None,
        oauth_provider_config: main_models.CreateCredentialProviderRequestCredentialProviderConfigOAuthProviderConfig = None,
    ):
        # The configuration of the JWT credential provider.
        self.jwt_provider_config = jwt_provider_config
        # The configuration of the OAuth credential provider.
        self.oauth_provider_config = oauth_provider_config

    def validate(self):
        if self.jwt_provider_config:
            self.jwt_provider_config.validate()
        if self.oauth_provider_config:
            self.oauth_provider_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.jwt_provider_config is not None:
            result['JwtProviderConfig'] = self.jwt_provider_config.to_map()

        if self.oauth_provider_config is not None:
            result['OAuthProviderConfig'] = self.oauth_provider_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtProviderConfig') is not None:
            temp_model = main_models.CreateCredentialProviderRequestCredentialProviderConfigJwtProviderConfig()
            self.jwt_provider_config = temp_model.from_map(m.get('JwtProviderConfig'))

        if m.get('OAuthProviderConfig') is not None:
            temp_model = main_models.CreateCredentialProviderRequestCredentialProviderConfigOAuthProviderConfig()
            self.oauth_provider_config = temp_model.from_map(m.get('OAuthProviderConfig'))

        return self

class CreateCredentialProviderRequestCredentialProviderConfigOAuthProviderConfig(DaraModel):
    def __init__(
        self,
        authorization_endpoint: str = None,
        authorization_flow: str = None,
        client_id: str = None,
        client_secret: str = None,
        discovery_url: str = None,
        issuer: str = None,
        pkce_challenge_method: str = None,
        pkce_enabled: bool = None,
        provider_vendor: str = None,
        scope: str = None,
        token_endpoint: str = None,
    ):
        # The endpoint address used to guide users through authorization. Conditionally required: required when AuthorizationFlow=user_federation and ProviderVendor=custom. For preset vendors, this can be automatically populated through DiscoveryUrl.
        self.authorization_endpoint = authorization_endpoint
        # The OAuth authorization flow type. Valid values: m2m: machine-to-machine (2LO, Client Credentials). user_federation: user federation (3LO, Authorization Code).
        self.authorization_flow = authorization_flow
        # The client_id in the OAuth protocol.
        # 
        # > The length cannot exceed 128 characters.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The client_secret in the OAuth protocol.
        # 
        # > The length cannot exceed 1024 characters.
        # 
        # This parameter is required.
        self.client_secret = client_secret
        # The Discovery document URL used to automatically retrieve OAuth endpoint configurations. Conditionally optional: used when AuthorizationFlow=user_federation. If DiscoveryUrl is not provided, you must manually configure fields such as TokenEndpoint and AuthorizationEndpoint.
        self.discovery_url = discovery_url
        self.issuer = issuer
        # The PKCE code_challenge generation method. Default value: s256.
        self.pkce_challenge_method = pkce_challenge_method
        # Specifies whether to use the PKCE extension to enhance security. We recommend that you always enable this feature.
        self.pkce_enabled = pkce_enabled
        # The preset vendor or custom configuration. Optional. Default value: custom.
        self.provider_vendor = provider_vendor
        # The scope in the OAuth protocol, which defines the permission range.
        # 
        # > The Scope configuration on the credential provider serves as the fallback value. If the scope parameter is not specified when calling the DeveloperAPI to obtain an OAuth Access Token, the Scope configuration on the credential provider is used for issuance.
        # 
        # >Notice: Separate multiple Scope values with spaces.
        # 
        # Restrictions for each individual Scope value:
        # 1. Allowed characters: lowercase letters, digits, and the special characters `|/:_-.`
        # 2. Must contain at least one lowercase letter or digit.
        # 3. Must start with the special character `.`, a lowercase letter, or a digit.
        # 4. The length cannot exceed 1024 characters.
        self.scope = scope
        # The token endpoint of the OAuth protocol.
        # 
        # > Must start with `http://` or `https://`, and the length cannot exceed 1024 characters.
        self.token_endpoint = token_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_endpoint is not None:
            result['AuthorizationEndpoint'] = self.authorization_endpoint

        if self.authorization_flow is not None:
            result['AuthorizationFlow'] = self.authorization_flow

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        if self.discovery_url is not None:
            result['DiscoveryUrl'] = self.discovery_url

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.pkce_challenge_method is not None:
            result['PkceChallengeMethod'] = self.pkce_challenge_method

        if self.pkce_enabled is not None:
            result['PkceEnabled'] = self.pkce_enabled

        if self.provider_vendor is not None:
            result['ProviderVendor'] = self.provider_vendor

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.token_endpoint is not None:
            result['TokenEndpoint'] = self.token_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationEndpoint') is not None:
            self.authorization_endpoint = m.get('AuthorizationEndpoint')

        if m.get('AuthorizationFlow') is not None:
            self.authorization_flow = m.get('AuthorizationFlow')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        if m.get('DiscoveryUrl') is not None:
            self.discovery_url = m.get('DiscoveryUrl')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('PkceChallengeMethod') is not None:
            self.pkce_challenge_method = m.get('PkceChallengeMethod')

        if m.get('PkceEnabled') is not None:
            self.pkce_enabled = m.get('PkceEnabled')

        if m.get('ProviderVendor') is not None:
            self.provider_vendor = m.get('ProviderVendor')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('TokenEndpoint') is not None:
            self.token_endpoint = m.get('TokenEndpoint')

        return self

class CreateCredentialProviderRequestCredentialProviderConfigJwtProviderConfig(DaraModel):
    def __init__(
        self,
        allowed_token_issuers: List[str] = None,
        derived_short_token_enabled: bool = None,
        expiration: int = None,
        expiration_cleanup_enabled: bool = None,
    ):
        # The list of allowed JWT issuers.
        # 
        # > The list length cannot exceed 200.
        self.allowed_token_issuers = allowed_token_issuers
        # Specifies whether to enable the JWT derived short token capability.
        self.derived_short_token_enabled = derived_short_token_enabled
        # The validity duration of the JWT. Unit: seconds.
        self.expiration = expiration
        # Specifies whether to enable JWT expiration cleanup.
        self.expiration_cleanup_enabled = expiration_cleanup_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_token_issuers is not None:
            result['AllowedTokenIssuers'] = self.allowed_token_issuers

        if self.derived_short_token_enabled is not None:
            result['DerivedShortTokenEnabled'] = self.derived_short_token_enabled

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.expiration_cleanup_enabled is not None:
            result['ExpirationCleanupEnabled'] = self.expiration_cleanup_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedTokenIssuers') is not None:
            self.allowed_token_issuers = m.get('AllowedTokenIssuers')

        if m.get('DerivedShortTokenEnabled') is not None:
            self.derived_short_token_enabled = m.get('DerivedShortTokenEnabled')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('ExpirationCleanupEnabled') is not None:
            self.expiration_cleanup_enabled = m.get('ExpirationCleanupEnabled')

        return self

