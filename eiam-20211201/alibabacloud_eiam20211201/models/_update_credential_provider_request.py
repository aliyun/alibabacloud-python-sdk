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
        # 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。
        # 
        # This parameter is required.
        self.client_token = client_token
        # 认证令牌提供商的配置。
        self.credential_provider_config = credential_provider_config
        # 认证令牌提供商ID。
        # 
        # This parameter is required.
        self.credential_provider_id = credential_provider_id
        # 认证令牌提供商名称。
        self.credential_provider_name = credential_provider_name
        # IDaaS EIAM实例的ID。
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
        # JWT身份提供商配置。
        self.jwt_provider_config = jwt_provider_config
        # OAuth 2LO机用类型的提供商的配置。
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
        client_secret: str = None,
        scope: str = None,
        token_endpoint: str = None,
    ):
        # OAuth协议中的client_secret，客户端密钥。
        self.client_secret = client_secret
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
        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.token_endpoint is not None:
            result['TokenEndpoint'] = self.token_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

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
        # 签发出的JWT中的issuer字段的允许列表。
        self.allowed_token_issuers = allowed_token_issuers
        # 是否开启JWT派生短令牌能力。
        self.derived_short_token_enabled = derived_short_token_enabled
        # JWT的有效时长，单位秒。
        self.expiration = expiration
        # 是否开启JWT过期清理。
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

