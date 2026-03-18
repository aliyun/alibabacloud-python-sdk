# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetCredentialProviderResponseBody(DaraModel):
    def __init__(
        self,
        credential_provider: main_models.GetCredentialProviderResponseBodyCredentialProvider = None,
        request_id: str = None,
    ):
        self.credential_provider = credential_provider
        self.request_id = request_id

    def validate(self):
        if self.credential_provider:
            self.credential_provider.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_provider is not None:
            result['CredentialProvider'] = self.credential_provider.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialProvider') is not None:
            temp_model = main_models.GetCredentialProviderResponseBodyCredentialProvider()
            self.credential_provider = temp_model.from_map(m.get('CredentialProvider'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCredentialProviderResponseBodyCredentialProvider(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        credential_provider_config: main_models.GetCredentialProviderResponseBodyCredentialProviderCredentialProviderConfig = None,
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
        # 认证令牌提供商的创建时间，Unix时间戳。
        self.create_time = create_time
        # 认证令牌提供商的配置。
        self.credential_provider_config = credential_provider_config
        # 认证令牌提供商的创建类型。
        self.credential_provider_creation_type = credential_provider_creation_type
        # 认证令牌提供商ID。
        self.credential_provider_id = credential_provider_id
        # 认证令牌提供商的业务标识。
        self.credential_provider_identifier = credential_provider_identifier
        # 认证令牌提供商名称。
        self.credential_provider_name = credential_provider_name
        # 认证令牌提供商的类型。
        self.credential_provider_type = credential_provider_type
        # 描述。
        self.description = description
        # EIAM实例ID。
        self.instance_id = instance_id
        # 认证令牌提供商的状态。
        self.status = status
        # 认证令牌提供商的更新时间，Unix时间戳。
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
            temp_model = main_models.GetCredentialProviderResponseBodyCredentialProviderCredentialProviderConfig()
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

class GetCredentialProviderResponseBodyCredentialProviderCredentialProviderConfig(DaraModel):
    def __init__(
        self,
        jwt_provider_config: main_models.GetCredentialProviderResponseBodyCredentialProviderCredentialProviderConfigJwtProviderConfig = None,
        oauth_provider_config: main_models.GetCredentialProviderResponseBodyCredentialProviderCredentialProviderConfigOAuthProviderConfig = None,
        provider_credential_ids: List[str] = None,
    ):
        # JWT身份提供商配置。
        self.jwt_provider_config = jwt_provider_config
        # OAuth 2LO机用类型的提供商的配置。
        self.oauth_provider_config = oauth_provider_config
        # 认证令牌提供商的敏感配置对应的凭据ID列表。
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
            temp_model = main_models.GetCredentialProviderResponseBodyCredentialProviderCredentialProviderConfigJwtProviderConfig()
            self.jwt_provider_config = temp_model.from_map(m.get('JwtProviderConfig'))

        if m.get('OAuthProviderConfig') is not None:
            temp_model = main_models.GetCredentialProviderResponseBodyCredentialProviderCredentialProviderConfigOAuthProviderConfig()
            self.oauth_provider_config = temp_model.from_map(m.get('OAuthProviderConfig'))

        if m.get('ProviderCredentialIds') is not None:
            self.provider_credential_ids = m.get('ProviderCredentialIds')

        return self

class GetCredentialProviderResponseBodyCredentialProviderCredentialProviderConfigOAuthProviderConfig(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        scope: str = None,
        token_endpoint: str = None,
    ):
        # OAuth协议中的client_id，客户端ID。
        self.client_id = client_id
        # OAuth协议中的scope，权限范围。
        self.scope = scope
        # OAuth协议的Token端点。
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

class GetCredentialProviderResponseBodyCredentialProviderCredentialProviderConfigJwtProviderConfig(DaraModel):
    def __init__(
        self,
        allowed_token_issuers: List[str] = None,
        derived_short_token_enabled: bool = None,
        expiration: int = None,
        expiration_cleanup_enabled: bool = None,
        issuer: str = None,
        jwks_endpoint: str = None,
    ):
        # 签发出的JWT中的issuer字段的允许列表。
        self.allowed_token_issuers = allowed_token_issuers
        # 是否开启JWT派生短令牌能力。
        self.derived_short_token_enabled = derived_short_token_enabled
        # JWT的有效时长，单位秒。
        self.expiration = expiration
        # 是否开启JWT过期清理。
        self.expiration_cleanup_enabled = expiration_cleanup_enabled
        # JWT issuer。
        self.issuer = issuer
        # JWKs端点地址。
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

