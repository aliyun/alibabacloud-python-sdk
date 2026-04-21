# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HiMarketOidcConfig(DaraModel):
    def __init__(
        self,
        auth_code_config: main_models.HiMarketOidcConfigAuthCodeConfig = None,
        enabled: bool = None,
        grant_type: str = None,
        identity_mapping: main_models.HiMarketOidcConfigIdentityMapping = None,
        logo_url: str = None,
        name: str = None,
        provider: str = None,
    ):
        self.auth_code_config = auth_code_config
        self.enabled = enabled
        self.grant_type = grant_type
        self.identity_mapping = identity_mapping
        self.logo_url = logo_url
        self.name = name
        self.provider = provider

    def validate(self):
        if self.auth_code_config:
            self.auth_code_config.validate()
        if self.identity_mapping:
            self.identity_mapping.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_code_config is not None:
            result['authCodeConfig'] = self.auth_code_config.to_map()

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.grant_type is not None:
            result['grantType'] = self.grant_type

        if self.identity_mapping is not None:
            result['identityMapping'] = self.identity_mapping.to_map()

        if self.logo_url is not None:
            result['logoUrl'] = self.logo_url

        if self.name is not None:
            result['name'] = self.name

        if self.provider is not None:
            result['provider'] = self.provider

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authCodeConfig') is not None:
            temp_model = main_models.HiMarketOidcConfigAuthCodeConfig()
            self.auth_code_config = temp_model.from_map(m.get('authCodeConfig'))

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('grantType') is not None:
            self.grant_type = m.get('grantType')

        if m.get('identityMapping') is not None:
            temp_model = main_models.HiMarketOidcConfigIdentityMapping()
            self.identity_mapping = temp_model.from_map(m.get('identityMapping'))

        if m.get('logoUrl') is not None:
            self.logo_url = m.get('logoUrl')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        return self

class HiMarketOidcConfigIdentityMapping(DaraModel):
    def __init__(
        self,
        custom_fields: Dict[str, str] = None,
        email_field: str = None,
        user_id_field: str = None,
        user_name_field: str = None,
    ):
        self.custom_fields = custom_fields
        self.email_field = email_field
        self.user_id_field = user_id_field
        self.user_name_field = user_name_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_fields is not None:
            result['customFields'] = self.custom_fields

        if self.email_field is not None:
            result['emailField'] = self.email_field

        if self.user_id_field is not None:
            result['userIdField'] = self.user_id_field

        if self.user_name_field is not None:
            result['userNameField'] = self.user_name_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customFields') is not None:
            self.custom_fields = m.get('customFields')

        if m.get('emailField') is not None:
            self.email_field = m.get('emailField')

        if m.get('userIdField') is not None:
            self.user_id_field = m.get('userIdField')

        if m.get('userNameField') is not None:
            self.user_name_field = m.get('userNameField')

        return self

class HiMarketOidcConfigAuthCodeConfig(DaraModel):
    def __init__(
        self,
        authorization_endpoint: str = None,
        client_id: str = None,
        client_secret: str = None,
        issuer: str = None,
        jwk_set_uri: str = None,
        redirect_uri: str = None,
        scopes: str = None,
        token_endpoint: str = None,
        user_info_endpoint: str = None,
    ):
        self.authorization_endpoint = authorization_endpoint
        self.client_id = client_id
        self.client_secret = client_secret
        self.issuer = issuer
        self.jwk_set_uri = jwk_set_uri
        self.redirect_uri = redirect_uri
        self.scopes = scopes
        self.token_endpoint = token_endpoint
        self.user_info_endpoint = user_info_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_endpoint is not None:
            result['authorizationEndpoint'] = self.authorization_endpoint

        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.client_secret is not None:
            result['clientSecret'] = self.client_secret

        if self.issuer is not None:
            result['issuer'] = self.issuer

        if self.jwk_set_uri is not None:
            result['jwkSetUri'] = self.jwk_set_uri

        if self.redirect_uri is not None:
            result['redirectUri'] = self.redirect_uri

        if self.scopes is not None:
            result['scopes'] = self.scopes

        if self.token_endpoint is not None:
            result['tokenEndpoint'] = self.token_endpoint

        if self.user_info_endpoint is not None:
            result['userInfoEndpoint'] = self.user_info_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authorizationEndpoint') is not None:
            self.authorization_endpoint = m.get('authorizationEndpoint')

        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('clientSecret') is not None:
            self.client_secret = m.get('clientSecret')

        if m.get('issuer') is not None:
            self.issuer = m.get('issuer')

        if m.get('jwkSetUri') is not None:
            self.jwk_set_uri = m.get('jwkSetUri')

        if m.get('redirectUri') is not None:
            self.redirect_uri = m.get('redirectUri')

        if m.get('scopes') is not None:
            self.scopes = m.get('scopes')

        if m.get('tokenEndpoint') is not None:
            self.token_endpoint = m.get('tokenEndpoint')

        if m.get('userInfoEndpoint') is not None:
            self.user_info_endpoint = m.get('userInfoEndpoint')

        return self

