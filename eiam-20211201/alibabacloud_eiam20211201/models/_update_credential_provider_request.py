# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class UpdateCredentialProviderRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        credential_provider_config: main_models.UpdateCredentialProviderRequestCredentialProviderConfig = None,
        credential_provider_id: str = None,
        credential_provider_name: str = None,
        instance_id: str = None,
    ):
        # The idempotency token that ensures the idempotence of the request.
        # 
        # Generate a unique parameter value from your client to ensure uniqueness across different requests. ClientToken supports only ASCII characters and cannot exceed 64 characters. For more information, see References: [How to ensure idempotence](https://www.alibabacloud.com/help/zh/ecs/developer-reference/how-to-ensure-idempotence).
        # 
        # This parameter is required.
        self.client_token = client_token
        # The credential provider configuration.
        self.credential_provider_config = credential_provider_config
        # The credential provider ID.
        # 
        # This parameter is required.
        self.credential_provider_id = credential_provider_id
        # The credential provider name.
        # 
        # > The name cannot exceed 64 characters in length.
        self.credential_provider_name = credential_provider_name
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

        if self.credential_provider_id is not None:
            result['CredentialProviderId'] = self.credential_provider_id

        if self.credential_provider_name is not None:
            result['CredentialProviderName'] = self.credential_provider_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CredentialProviderConfig') is not None:
            temp_model = main_models.UpdateCredentialProviderRequestCredentialProviderConfig()
            self.credential_provider_config = temp_model.from_map(m.get('CredentialProviderConfig'))

        if m.get('CredentialProviderId') is not None:
            self.credential_provider_id = m.get('CredentialProviderId')

        if m.get('CredentialProviderName') is not None:
            self.credential_provider_name = m.get('CredentialProviderName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class UpdateCredentialProviderRequestCredentialProviderConfig(DaraModel):
    def __init__(
        self,
        jwt_provider_config: main_models.UpdateCredentialProviderRequestCredentialProviderConfigJwtProviderConfig = None,
        oauth_provider_config: main_models.UpdateCredentialProviderRequestCredentialProviderConfigOAuthProviderConfig = None,
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
            temp_model = main_models.UpdateCredentialProviderRequestCredentialProviderConfigJwtProviderConfig()
            self.jwt_provider_config = temp_model.from_map(m.get('JwtProviderConfig'))

        if m.get('OAuthProviderConfig') is not None:
            temp_model = main_models.UpdateCredentialProviderRequestCredentialProviderConfigOAuthProviderConfig()
            self.oauth_provider_config = temp_model.from_map(m.get('OAuthProviderConfig'))

        return self

class UpdateCredentialProviderRequestCredentialProviderConfigOAuthProviderConfig(DaraModel):
    def __init__(
        self,
        authorization_endpoint: str = None,
        authorization_flow: str = None,
        client_secret: str = None,
        discovery_url: str = None,
        issuer: str = None,
        pkce_challenge_method: str = None,
        pkce_enabled: bool = None,
        provider_vendor: str = None,
        scope: str = None,
        token_endpoint: str = None,
    ):
        # The authorization endpoint.
        self.authorization_endpoint = authorization_endpoint
        # The OAuth authorization flow type. Valid values:
        # - m2m: machine-to-machine.
        # - user_federation: user federation.
        self.authorization_flow = authorization_flow
        # The client_secret in the OAuth protocol.
        # 
        # > The value cannot exceed 1024 characters in length.
        self.client_secret = client_secret
        # The auto-discovery URL.
        self.discovery_url = discovery_url
        # The authorization server identifier URL.
        self.issuer = issuer
        # The PKCE challenge method. Valid values:
        # - S256.
        # - plain.
        self.pkce_challenge_method = pkce_challenge_method
        # Specifies whether PKCE is enabled.
        self.pkce_enabled = pkce_enabled
        # The vendor type. Valid values:
        # - custom: custom.
        # - dingtalk: DingTalk.
        # - feishu: Lark.
        # - github: GitHub.
        # - microsoft: Microsoft.
        # - google: Google.
        self.provider_vendor = provider_vendor
        # The scope in the OAuth protocol, which specifies the permission scope.
        # 
        # > The Scope configuration on the credential provider serves as the fallback value. If the scope parameter is not specified when calling the DeveloperAPI to obtain an OAuth Access Token, the Scope configuration on the credential provider is used for issuance.
        # 
        # >Notice: Separate multiple Scope values with spaces. To clear the Scope configuration, pass an empty string.
        # 
        # Restrictions on each individual Scope value:
        # 1. Allowed characters: lowercase letters, digits, and special characters `|/:_-.`
        # 2. Must contain at least one lowercase letter or digit.
        # 3. Must start with a special character `.`, a lowercase letter, or a digit.
        # 4. Cannot exceed 1024 characters in length.
        self.scope = scope
        # The token endpoint of the OAuth protocol.
        # 
        # > The value must start with `http://` or `https://` and cannot exceed 1024 characters in length.
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

class UpdateCredentialProviderRequestCredentialProviderConfigJwtProviderConfig(DaraModel):
    def __init__(
        self,
        allowed_token_issuers: List[str] = None,
        derived_short_token_enabled: bool = None,
        expiration: int = None,
        expiration_cleanup_enabled: bool = None,
    ):
        # The list of allowed JWT issuers.
        # 
        # > The list cannot contain more than 200 entries.
        # 
        # >Notice: To clear the issuer list, pass an empty list or an empty string when calling the API.
        self.allowed_token_issuers = allowed_token_issuers
        # Specifies whether the JWT derived short token feature is enabled.
        self.derived_short_token_enabled = derived_short_token_enabled
        # The validity period of the JWT, in seconds.
        self.expiration = expiration
        # Specifies whether JWT expiration cleanup is enabled.
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

