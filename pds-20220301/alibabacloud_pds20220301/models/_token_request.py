# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TokenRequest(DaraModel):
    def __init__(
        self,
        assertion: str = None,
        client_id: str = None,
        client_secret: str = None,
        code: str = None,
        grant_type: str = None,
        redirect_uri: str = None,
        refresh_token: str = None,
    ):
        # The JWT assertion that is signed by using the JWT private key. The JWT assertion contains the information about the user to be authorized and the authorization parameters. For more information about the structure of the JWT assertion, see JWTPayload. This parameter is required if grant_type is set to urn:ietf:params:oauth:grant-type:jwt-bearer.
        self.assertion = assertion
        # The AppId of the application that is created in the Drive and Photo Service console.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The AppSecret of the application that is created in the Drive and Photo Service console. This parameter is required if the application is of the WebServer type.
        self.client_secret = client_secret
        # The authorization code in the redirect URI that is specified after the authorization process is complete. This parameter is required if grant_type is set to authorization_code.
        self.code = code
        # The method that is used to generate an access token. Valid values:
        # 
        # authorization_code: generates an access token by using the authorization code that is returned after the authorization process is complete.
        # 
        # refresh_token: generates an access token by using the refresh token that is returned after the authorization process is complete.
        # 
        # urn:ietf:params:oauth:grant-type:jwt-bearer: generates an access token by using a JWT assertion.
        # 
        # This parameter is required.
        self.grant_type = grant_type
        # The redirect URI that is specified when you initiate the authorization request. This parameter is required if grant_type is set to authorization_code.
        self.redirect_uri = redirect_uri
        # The refresh token that is used to refresh the access token. This parameter is required if grant_type is set to refresh_token.
        self.refresh_token = refresh_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assertion is not None:
            result['assertion'] = self.assertion

        if self.client_id is not None:
            result['client_id'] = self.client_id

        if self.client_secret is not None:
            result['client_secret'] = self.client_secret

        if self.code is not None:
            result['code'] = self.code

        if self.grant_type is not None:
            result['grant_type'] = self.grant_type

        if self.redirect_uri is not None:
            result['redirect_uri'] = self.redirect_uri

        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assertion') is not None:
            self.assertion = m.get('assertion')

        if m.get('client_id') is not None:
            self.client_id = m.get('client_id')

        if m.get('client_secret') is not None:
            self.client_secret = m.get('client_secret')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('grant_type') is not None:
            self.grant_type = m.get('grant_type')

        if m.get('redirect_uri') is not None:
            self.redirect_uri = m.get('redirect_uri')

        if m.get('refresh_token') is not None:
            self.refresh_token = m.get('refresh_token')

        return self

