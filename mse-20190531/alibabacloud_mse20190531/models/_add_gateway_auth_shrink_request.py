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
        self.accept_language = accept_language
        self.auth_resource_config = auth_resource_config
        # The information about the resource to be authorized.
        self.auth_resource_list_shrink = auth_resource_list_shrink
        self.auth_resource_mode = auth_resource_mode
        # The application ID registered with the OIDC authentication service.
        self.client_id = client_id
        # The application secret registered with the OIDC authentication service.
        self.client_secret = client_secret
        # The domain name of the cookie. After the authentication is passed, the cookie is sent to the specified domain name to maintain the logon status. For example, if you set `Cookie-domain` to a.example.com, the cookie is sent to the domain name `a.example.com`. If you set `Cookie-domain` to .example.com, the cookie is sent to all subdomains of `example.com`.
        self.cookie_domain = cookie_domain
        # The information about the custom authentication service.
        self.external_auth_zjsonshrink = external_auth_zjsonshrink
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # Specifies whether to enable the whitelist feature.
        self.is_white = is_white
        # The iss value of JWT claims, which indicates the issuer. You must make sure that the value of this parameter is the same as the iss value in the payload of JWT claims.
        self.issuer = issuer
        # The JWT public key. The JSON format is supported.
        self.jwks = jwks
        # The URL that is used to log on to the IDaaS instance.
        self.login_url = login_url
        # The name.
        self.name = name
        # The redirect URL.
        self.redirect_url = redirect_url
        # The OIDC scope.
        self.scopes_list_shrink = scopes_list_shrink
        # The status.
        self.status = status
        # The sub value of JWT claims, which indicates the subject. You must make sure that the value of this parameter is the same as the sub value in the payload of JWT claims. If you do not set this parameter or leave it empty, the default value, which is the value of the Issuer parameter, is used.
        self.sub = sub
        # The name of the parameter that is required to verify a token. By default, a token is prefixed with Bearer and stored in the authorization header. Example: `Authorization: Bearer token`.
        self.token_name = token_name
        # The name prefix of the parameter that is required to verify a token. By default, a token is prefixed with Bearer and stored in the authorization header. Example: `Authorization: Bearer token`
        self.token_name_prefix = token_name_prefix
        # Specifies whether to enable pass-through.
        self.token_pass = token_pass
        # The position of the parameter that is required to verify a token. By default, a token is prefixed with Bearer and stored in the authorization header. Example: `Authorization: Bearer token`.
        self.token_position = token_position
        # The authentication type. JSON Web Token (JWT) authentication, OpenID Connect (OIDC) authentication, Identity as a Service (IDaaS) authentication, or custom authentication are supported.
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

