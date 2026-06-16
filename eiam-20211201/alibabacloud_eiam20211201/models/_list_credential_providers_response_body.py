# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListCredentialProvidersResponseBody(DaraModel):
    def __init__(
        self,
        credential_providers: List[main_models.ListCredentialProvidersResponseBodyCredentialProviders] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # List of credential providers.
        self.credential_providers = credential_providers
        # Page size for paged queries.
        self.max_results = max_results
        # The query token returned by this call.
        self.next_token = next_token
        # Request ID.
        self.request_id = request_id
        # Total count.
        self.total_count = total_count

    def validate(self):
        if self.credential_providers:
            for v1 in self.credential_providers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CredentialProviders'] = []
        if self.credential_providers is not None:
            for k1 in self.credential_providers:
                result['CredentialProviders'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.credential_providers = []
        if m.get('CredentialProviders') is not None:
            for k1 in m.get('CredentialProviders'):
                temp_model = main_models.ListCredentialProvidersResponseBodyCredentialProviders()
                self.credential_providers.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCredentialProvidersResponseBodyCredentialProviders(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        credential_provider_config: main_models.ListCredentialProvidersResponseBodyCredentialProvidersCredentialProviderConfig = None,
        credential_provider_creation_type: str = None,
        credential_provider_id: str = None,
        credential_provider_identifier: str = None,
        credential_provider_name: str = None,
        credential_provider_type: str = None,
        description: str = None,
        instance_id: str = None,
        status: str = None,
        update_time: int = None,
    ):
        # Creation time of the credential provider, in Unix timestamp format (milliseconds).
        self.create_time = create_time
        # Credential provider configuration.
        self.credential_provider_config = credential_provider_config
        # Credential provider creation type. Valid values:
        # 
        # - system_init: System created.
        # 
        # - user_custom: User created.
        self.credential_provider_creation_type = credential_provider_creation_type
        # Credential provider ID.
        self.credential_provider_id = credential_provider_id
        # Credential provider identifier.
        self.credential_provider_identifier = credential_provider_identifier
        # Credential provider name.
        self.credential_provider_name = credential_provider_name
        # Credential provider type. Valid values:
        # 
        # - oauth: OAuth credential provider
        # 
        # - jwt: JWT credential provider
        self.credential_provider_type = credential_provider_type
        # Description.
        self.description = description
        # Instance ID.
        self.instance_id = instance_id
        # Credential provider status. Valid values:
        # 
        # - enabled: Enabled.
        # 
        # - disabled: Disabled.
        self.status = status
        # Update time of the credential provider, in Unix timestamp format (milliseconds).
        self.update_time = update_time

    def validate(self):
        if self.credential_provider_config:
            self.credential_provider_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.credential_provider_config is not None:
            result['CredentialProviderConfig'] = self.credential_provider_config.to_map()

        if self.credential_provider_creation_type is not None:
            result['CredentialProviderCreationType'] = self.credential_provider_creation_type

        if self.credential_provider_id is not None:
            result['CredentialProviderId'] = self.credential_provider_id

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

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CredentialProviderConfig') is not None:
            temp_model = main_models.ListCredentialProvidersResponseBodyCredentialProvidersCredentialProviderConfig()
            self.credential_provider_config = temp_model.from_map(m.get('CredentialProviderConfig'))

        if m.get('CredentialProviderCreationType') is not None:
            self.credential_provider_creation_type = m.get('CredentialProviderCreationType')

        if m.get('CredentialProviderId') is not None:
            self.credential_provider_id = m.get('CredentialProviderId')

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListCredentialProvidersResponseBodyCredentialProvidersCredentialProviderConfig(DaraModel):
    def __init__(
        self,
        jwt_provider_config: main_models.ListCredentialProvidersResponseBodyCredentialProvidersCredentialProviderConfigJwtProviderConfig = None,
        oauth_provider_config: main_models.ListCredentialProvidersResponseBodyCredentialProvidersCredentialProviderConfigOAuthProviderConfig = None,
        provider_credential_ids: List[str] = None,
    ):
        # Configuration for JWT credential providers.
        self.jwt_provider_config = jwt_provider_config
        # Configuration for OAuth credential providers.
        self.oauth_provider_config = oauth_provider_config
        # List of credential IDs for the sensitive configuration of the credential provider.
        # 
        # > The system securely stores sensitive credential provider configuration as credentials.
        self.provider_credential_ids = provider_credential_ids

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

        if self.provider_credential_ids is not None:
            result['ProviderCredentialIds'] = self.provider_credential_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtProviderConfig') is not None:
            temp_model = main_models.ListCredentialProvidersResponseBodyCredentialProvidersCredentialProviderConfigJwtProviderConfig()
            self.jwt_provider_config = temp_model.from_map(m.get('JwtProviderConfig'))

        if m.get('OAuthProviderConfig') is not None:
            temp_model = main_models.ListCredentialProvidersResponseBodyCredentialProvidersCredentialProviderConfigOAuthProviderConfig()
            self.oauth_provider_config = temp_model.from_map(m.get('OAuthProviderConfig'))

        if m.get('ProviderCredentialIds') is not None:
            self.provider_credential_ids = m.get('ProviderCredentialIds')

        return self

class ListCredentialProvidersResponseBodyCredentialProvidersCredentialProviderConfigOAuthProviderConfig(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        scope: str = None,
        token_endpoint: str = None,
    ):
        # The client_id in the OAuth protocol, also known as the client ID.
        self.client_id = client_id
        # The scope in the OAuth protocol, which defines permission scope.
        # 
        # > The Scope configuration for the OAuth credential provider acts as a fallback. If you do not specify the scope parameter when calling the DeveloperAPI to get an OAuth Access Token, the credential provider\\"s Scope configuration is used for issuance.
        # 
        # >Notice: 
        # 
        # Multiple Scope values are separated by spaces.
        self.scope = scope
        # The Token endpoint of the OAuth protocol.
        self.token_endpoint = token_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.token_endpoint is not None:
            result['TokenEndpoint'] = self.token_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('TokenEndpoint') is not None:
            self.token_endpoint = m.get('TokenEndpoint')

        return self

class ListCredentialProvidersResponseBodyCredentialProvidersCredentialProviderConfigJwtProviderConfig(DaraModel):
    def __init__(
        self,
        allowed_token_issuers: List[str] = None,
        derived_short_token_enabled: bool = None,
        expiration: int = None,
        expiration_cleanup_enabled: bool = None,
        issuer: str = None,
        jwks_endpoint: str = None,
    ):
        # List of allowed JWT issuers.
        self.allowed_token_issuers = allowed_token_issuers
        # Enable JWT derived short token capability.
        self.derived_short_token_enabled = derived_short_token_enabled
        # Validity period of the JWT, in seconds.
        self.expiration = expiration
        # Enable JWT expiration cleanup.
        self.expiration_cleanup_enabled = expiration_cleanup_enabled
        # JWT issuer.
        self.issuer = issuer
        # JWKs endpoint address.
        self.jwks_endpoint = jwks_endpoint

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

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.jwks_endpoint is not None:
            result['JwksEndpoint'] = self.jwks_endpoint

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

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('JwksEndpoint') is not None:
            self.jwks_endpoint = m.get('JwksEndpoint')

        return self

