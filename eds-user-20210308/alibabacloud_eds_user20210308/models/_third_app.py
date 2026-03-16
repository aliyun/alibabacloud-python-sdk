# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class ThirdApp(DaraModel):
    def __init__(
        self,
        app_key: str = None,
        name: str = None,
        oidc_sso_config: main_models.ThirdAppOidcSsoConfig = None,
        secrets: List[main_models.ThirdAppSecrets] = None,
    ):
        self.app_key = app_key
        self.name = name
        self.oidc_sso_config = oidc_sso_config
        self.secrets = secrets

    def validate(self):
        if self.oidc_sso_config:
            self.oidc_sso_config.validate()
        if self.secrets:
            for v1 in self.secrets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.name is not None:
            result['Name'] = self.name

        if self.oidc_sso_config is not None:
            result['OidcSsoConfig'] = self.oidc_sso_config.to_map()

        result['Secrets'] = []
        if self.secrets is not None:
            for k1 in self.secrets:
                result['Secrets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OidcSsoConfig') is not None:
            temp_model = main_models.ThirdAppOidcSsoConfig()
            self.oidc_sso_config = temp_model.from_map(m.get('OidcSsoConfig'))

        self.secrets = []
        if m.get('Secrets') is not None:
            for k1 in m.get('Secrets'):
                temp_model = main_models.ThirdAppSecrets()
                self.secrets.append(temp_model.from_map(k1))

        return self

class ThirdAppSecrets(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        secret: str = None,
    ):
        self.enable = enable
        self.secret = secret

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.secret is not None:
            result['Secret'] = self.secret

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Secret') is not None:
            self.secret = m.get('Secret')

        return self

class ThirdAppOidcSsoConfig(DaraModel):
    def __init__(
        self,
        access_token_effective_time: int = None,
        code_effective_time: int = None,
        enable_auth_login: bool = None,
        endpoints: main_models.ThirdAppOidcSsoConfigEndpoints = None,
        grant_scopes: List[str] = None,
        grant_types: List[str] = None,
        id_token_algorithm_type: str = None,
        id_token_effective_time: int = None,
        redirect_uris: List[str] = None,
        refresh_token_effective: int = None,
    ):
        self.access_token_effective_time = access_token_effective_time
        self.code_effective_time = code_effective_time
        self.enable_auth_login = enable_auth_login
        self.endpoints = endpoints
        self.grant_scopes = grant_scopes
        self.grant_types = grant_types
        self.id_token_algorithm_type = id_token_algorithm_type
        self.id_token_effective_time = id_token_effective_time
        self.redirect_uris = redirect_uris
        self.refresh_token_effective = refresh_token_effective

    def validate(self):
        if self.endpoints:
            self.endpoints.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token_effective_time is not None:
            result['AccessTokenEffectiveTime'] = self.access_token_effective_time

        if self.code_effective_time is not None:
            result['CodeEffectiveTime'] = self.code_effective_time

        if self.enable_auth_login is not None:
            result['EnableAuthLogin'] = self.enable_auth_login

        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()

        if self.grant_scopes is not None:
            result['GrantScopes'] = self.grant_scopes

        if self.grant_types is not None:
            result['GrantTypes'] = self.grant_types

        if self.id_token_algorithm_type is not None:
            result['IdTokenAlgorithmType'] = self.id_token_algorithm_type

        if self.id_token_effective_time is not None:
            result['IdTokenEffectiveTime'] = self.id_token_effective_time

        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris

        if self.refresh_token_effective is not None:
            result['RefreshTokenEffective'] = self.refresh_token_effective

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTokenEffectiveTime') is not None:
            self.access_token_effective_time = m.get('AccessTokenEffectiveTime')

        if m.get('CodeEffectiveTime') is not None:
            self.code_effective_time = m.get('CodeEffectiveTime')

        if m.get('EnableAuthLogin') is not None:
            self.enable_auth_login = m.get('EnableAuthLogin')

        if m.get('Endpoints') is not None:
            temp_model = main_models.ThirdAppOidcSsoConfigEndpoints()
            self.endpoints = temp_model.from_map(m.get('Endpoints'))

        if m.get('GrantScopes') is not None:
            self.grant_scopes = m.get('GrantScopes')

        if m.get('GrantTypes') is not None:
            self.grant_types = m.get('GrantTypes')

        if m.get('IdTokenAlgorithmType') is not None:
            self.id_token_algorithm_type = m.get('IdTokenAlgorithmType')

        if m.get('IdTokenEffectiveTime') is not None:
            self.id_token_effective_time = m.get('IdTokenEffectiveTime')

        if m.get('RedirectUris') is not None:
            self.redirect_uris = m.get('RedirectUris')

        if m.get('RefreshTokenEffective') is not None:
            self.refresh_token_effective = m.get('RefreshTokenEffective')

        return self



class ThirdAppOidcSsoConfigEndpoints(DaraModel):
    def __init__(
        self,
        authorization_endpoint: str = None,
        discovery_endpoint: str = None,
        guest_authorization_endpoint: str = None,
        issuer: str = None,
        jwks_endpoint: str = None,
        logout_endpoint: str = None,
        revoke_endpoint: str = None,
        token_endpoint: str = None,
        userinfo_endpoint: str = None,
    ):
        self.authorization_endpoint = authorization_endpoint
        self.discovery_endpoint = discovery_endpoint
        self.guest_authorization_endpoint = guest_authorization_endpoint
        self.issuer = issuer
        self.jwks_endpoint = jwks_endpoint
        self.logout_endpoint = logout_endpoint
        self.revoke_endpoint = revoke_endpoint
        self.token_endpoint = token_endpoint
        self.userinfo_endpoint = userinfo_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_endpoint is not None:
            result['AuthorizationEndpoint'] = self.authorization_endpoint

        if self.discovery_endpoint is not None:
            result['DiscoveryEndpoint'] = self.discovery_endpoint

        if self.guest_authorization_endpoint is not None:
            result['GuestAuthorizationEndpoint'] = self.guest_authorization_endpoint

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.jwks_endpoint is not None:
            result['JwksEndpoint'] = self.jwks_endpoint

        if self.logout_endpoint is not None:
            result['LogoutEndpoint'] = self.logout_endpoint

        if self.revoke_endpoint is not None:
            result['RevokeEndpoint'] = self.revoke_endpoint

        if self.token_endpoint is not None:
            result['TokenEndpoint'] = self.token_endpoint

        if self.userinfo_endpoint is not None:
            result['UserinfoEndpoint'] = self.userinfo_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationEndpoint') is not None:
            self.authorization_endpoint = m.get('AuthorizationEndpoint')

        if m.get('DiscoveryEndpoint') is not None:
            self.discovery_endpoint = m.get('DiscoveryEndpoint')

        if m.get('GuestAuthorizationEndpoint') is not None:
            self.guest_authorization_endpoint = m.get('GuestAuthorizationEndpoint')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('JwksEndpoint') is not None:
            self.jwks_endpoint = m.get('JwksEndpoint')

        if m.get('LogoutEndpoint') is not None:
            self.logout_endpoint = m.get('LogoutEndpoint')

        if m.get('RevokeEndpoint') is not None:
            self.revoke_endpoint = m.get('RevokeEndpoint')

        if m.get('TokenEndpoint') is not None:
            self.token_endpoint = m.get('TokenEndpoint')

        if m.get('UserinfoEndpoint') is not None:
            self.userinfo_endpoint = m.get('UserinfoEndpoint')

        return self

