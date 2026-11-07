# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddGatewayAuthShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        auth_resource_config: str = None,
        auth_resource_list_shrink: str = None,
        auth_resource_mode: int = None,
        client_id: str = None,
        client_secret: str = None,
        cookie_domain: str = None,
        external_auth_zjsonshrink: str = None,
        gateway_unique_id: str = None,
        is_white: bool = None,
        issuer: str = None,
        jwks: str = None,
        login_url: str = None,
        name: str = None,
        redirect_url: str = None,
        scopes_list_shrink: str = None,
        status: bool = None,
        sub: str = None,
        token_name: str = None,
        token_name_prefix: str = None,
        token_pass: bool = None,
        token_position: str = None,
        type: str = None,
    ):
        # The language of the returned result. Valid values:
        # - zh: Chinese. This is the default value.
        # - en: English.
        self.accept_language = accept_language
        # The YAML configuration for the complex mode.
        self.auth_resource_config = auth_resource_config
        # The list of authorization rules for authentication. Multiple rule conditions use the OR operator, and multiple matching items within a rule condition use the AND operator.
        self.auth_resource_list_shrink = auth_resource_list_shrink
        # The authorization resource mode. Valid values:
        # - 0: simple mode.
        # - 1: complex mode.
        self.auth_resource_mode = auth_resource_mode
        # The application ID registered in the service. This parameter is used for OIDC and IDaaS.
        self.client_id = client_id
        # The application secret registered in the service. This parameter is used for OIDC and IDaaS.
        self.client_secret = client_secret
        # The domain name of the cookie. After authentication, the cookie is sent to the specified domain name to maintain the logon state.
        # 
        # For example, if you set the value to `Cookie-domain=a.example.com`, the cookie is sent to the `a.example.com` domain name. If you set the value to `Cookie-domain=.example.com`, the cookie is sent to all subdomains of `example.com`.
        self.cookie_domain = cookie_domain
        # The custom authentication information.
        self.external_auth_zjsonshrink = external_auth_zjsonshrink
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The authorization blacklist and whitelist mode. Valid values:
        # - true: whitelist mode. Hosts and paths in the list can be accessed without verification, while all others require verification.
        # - false: blacklist mode. Hosts and paths in the list require verification, while all others can be accessed directly.
        self.is_white = is_white
        # Used when the authentication type is JWT or OIDC:
        # - JWT: specifies the `iss` (issuer) claim of the JWT.
        # - OIDC: specifies the `iss` (issuer) claim of the OIDC token.
        self.issuer = issuer
        # The JWT public key. JSON format is supported.
        self.jwks = jwks
        # The URL of the user logon page for the IDaaS instance. This parameter is used for IDaaS.
        self.login_url = login_url
        # The name of the authentication.
        self.name = name
        # The redirect URL after successful authorization. This parameter is used for OIDC and IDaaS. The value must be the same as the redirect URL configured in OIDC or IDaaS.
        self.redirect_url = redirect_url
        # The OIDC authorization scopes. This parameter is used for OIDC.
        self.scopes_list_shrink = scopes_list_shrink
        # An unavailable parameter. You do not need to specify this parameter. By default, authentication is disabled after it is created.
        self.status = status
        # Used when the authentication type is JWT. Specifies the `sub` (subject) claim of the JWT. Make sure that the value of the `sub` field in the JWT payload is the same as the value configured here. If this parameter is not specified or is empty, the default value is the same as the value of the Issuer parameter.
        self.sub = sub
        # The location where the JWT token is stored.
        # 
        # By default, the token to be verified is placed in the Authorization header with the Bearer prefix, such as `Authorization: Bearer token`.
        self.token_name = token_name
        # The prefix of the JWT token.
        # 
        # By default, the token to be verified is placed in the Authorization header with the Bearer prefix, such as `Authorization: Bearer token`.
        self.token_name_prefix = token_name_prefix
        # Specifies whether to pass through the token.
        self.token_pass = token_pass
        # The position of the JWT token. Valid values:
        # - HEADER: transmitted in the HTTP header.
        # 
        # By default, the token to be verified is placed in the Authorization header with the Bearer prefix, such as Authorization: Bearer token.
        self.token_position = token_position
        # The authentication type. Valid values:
        # - JWT
        # - OIDC
        # - IDaaS
        # - ExternalAuthZ (custom authentication service)
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.auth_resource_config is not None:
            result['AuthResourceConfig'] = self.auth_resource_config

        if self.auth_resource_list_shrink is not None:
            result['AuthResourceList'] = self.auth_resource_list_shrink

        if self.auth_resource_mode is not None:
            result['AuthResourceMode'] = self.auth_resource_mode

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        if self.cookie_domain is not None:
            result['CookieDomain'] = self.cookie_domain

        if self.external_auth_zjsonshrink is not None:
            result['ExternalAuthZJSON'] = self.external_auth_zjsonshrink

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.is_white is not None:
            result['IsWhite'] = self.is_white

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.jwks is not None:
            result['Jwks'] = self.jwks

        if self.login_url is not None:
            result['LoginUrl'] = self.login_url

        if self.name is not None:
            result['Name'] = self.name

        if self.redirect_url is not None:
            result['RedirectUrl'] = self.redirect_url

        if self.scopes_list_shrink is not None:
            result['ScopesList'] = self.scopes_list_shrink

        if self.status is not None:
            result['Status'] = self.status

        if self.sub is not None:
            result['Sub'] = self.sub

        if self.token_name is not None:
            result['TokenName'] = self.token_name

        if self.token_name_prefix is not None:
            result['TokenNamePrefix'] = self.token_name_prefix

        if self.token_pass is not None:
            result['TokenPass'] = self.token_pass

        if self.token_position is not None:
            result['TokenPosition'] = self.token_position

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AuthResourceConfig') is not None:
            self.auth_resource_config = m.get('AuthResourceConfig')

        if m.get('AuthResourceList') is not None:
            self.auth_resource_list_shrink = m.get('AuthResourceList')

        if m.get('AuthResourceMode') is not None:
            self.auth_resource_mode = m.get('AuthResourceMode')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        if m.get('CookieDomain') is not None:
            self.cookie_domain = m.get('CookieDomain')

        if m.get('ExternalAuthZJSON') is not None:
            self.external_auth_zjsonshrink = m.get('ExternalAuthZJSON')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('IsWhite') is not None:
            self.is_white = m.get('IsWhite')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('Jwks') is not None:
            self.jwks = m.get('Jwks')

        if m.get('LoginUrl') is not None:
            self.login_url = m.get('LoginUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RedirectUrl') is not None:
            self.redirect_url = m.get('RedirectUrl')

        if m.get('ScopesList') is not None:
            self.scopes_list_shrink = m.get('ScopesList')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Sub') is not None:
            self.sub = m.get('Sub')

        if m.get('TokenName') is not None:
            self.token_name = m.get('TokenName')

        if m.get('TokenNamePrefix') is not None:
            self.token_name_prefix = m.get('TokenNamePrefix')

        if m.get('TokenPass') is not None:
            self.token_pass = m.get('TokenPass')

        if m.get('TokenPosition') is not None:
            self.token_position = m.get('TokenPosition')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

