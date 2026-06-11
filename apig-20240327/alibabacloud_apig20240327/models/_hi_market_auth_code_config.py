# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HiMarketAuthCodeConfig(DaraModel):
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
        # The URL of the identity provider\\"s authorization endpoint. Your application redirects users to this URL to sign in and grant consent.
        self.authorization_endpoint = authorization_endpoint
        # The unique identifier for your application. The identity provider assigns this ID when you register your application.
        self.client_id = client_id
        # The secret key for your application. This secret authenticates your application with the identity provider.
        self.client_secret = client_secret
        # The URL of the identity provider that issues the tokens. This URL uniquely identifies the provider.
        self.issuer = issuer
        # The URL of the identity provider\\"s JSON Web Key Set (JWKS) document. This document contains the public signing keys for token validation.
        self.jwk_set_uri = jwk_set_uri
        # The URL where the identity provider redirects the user after authorizing your application. This URL must be registered in your application settings with the identity provider.
        self.redirect_uri = redirect_uri
        # A space-separated list of requested permissions. For example: `openid profile`.
        self.scopes = scopes
        # The URL of the identity provider\\"s token endpoint. Your application uses this endpoint to exchange an authorization code for an access token.
        self.token_endpoint = token_endpoint
        # The URL of the identity provider\\"s user info endpoint. Your application can use this endpoint to retrieve the authenticated user\\"s profile information.
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

