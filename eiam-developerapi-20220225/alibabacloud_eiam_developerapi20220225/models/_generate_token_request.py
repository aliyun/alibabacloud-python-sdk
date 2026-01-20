# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateTokenRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
        code: str = None,
        code_verifier: str = None,
        device_code: str = None,
        exclusive_tag: str = None,
        grant_type: str = None,
        password: str = None,
        redirect_uri: str = None,
        refresh_token: str = None,
        scope: str = None,
        username: str = None,
    ):
        # The client ID.
        self.client_id = client_id
        # The client secret. This parameter is required if grant_type is set to client_credentials.
        self.client_secret = client_secret
        # The authorization code. This parameter is required if grant_type is set to authorization_code.
        self.code = code
        # The verification code.
        self.code_verifier = code_verifier
        # The device code. This parameter is required if grant_type is set to authorization_code.urn:ietf:params:oauth:grant-type:device_code.
        self.device_code = device_code
        # The excluded tags.
        self.exclusive_tag = exclusive_tag
        # The supported authorization types are as follows:
        # - client_credentials:Client credentials flow, requires client_id and client_secret.
        # - refresh_token:Refresh token flow.
        # - authorization_code:Authorization code flow.
        # - urn:ietf:params:oauth:grant-type:device_code:Device authorization flow.
        # - password:Password (Resource Owner Password Credentials) flow.
        # 
        # This parameter is required.
        self.grant_type = grant_type
        # The username. This parameter is required if grant_type is set to password. The password authentication type is not supported.
        self.password = password
        # The redirect URI. This parameter is required if grant_type is set to authorization_code. The value of this parameter must be the same as the redirect URI in the request to obtain the authorization code.
        self.redirect_uri = redirect_uri
        # The refreshed token. This parameter is required if grant_type is set to refresh_token.
        self.refresh_token = refresh_token
        # The authorization scope. Valid values:
        # 
        # *   openid
        # *   email
        # *   phone
        # *   profile
        self.scope = scope
        # The username. This parameter is required if grant_type is set to password. The password authentication type is not supported.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['client_id'] = self.client_id

        if self.client_secret is not None:
            result['client_secret'] = self.client_secret

        if self.code is not None:
            result['code'] = self.code

        if self.code_verifier is not None:
            result['code_verifier'] = self.code_verifier

        if self.device_code is not None:
            result['device_code'] = self.device_code

        if self.exclusive_tag is not None:
            result['exclusive_tag'] = self.exclusive_tag

        if self.grant_type is not None:
            result['grant_type'] = self.grant_type

        if self.password is not None:
            result['password'] = self.password

        if self.redirect_uri is not None:
            result['redirect_uri'] = self.redirect_uri

        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token

        if self.scope is not None:
            result['scope'] = self.scope

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('client_id') is not None:
            self.client_id = m.get('client_id')

        if m.get('client_secret') is not None:
            self.client_secret = m.get('client_secret')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('code_verifier') is not None:
            self.code_verifier = m.get('code_verifier')

        if m.get('device_code') is not None:
            self.device_code = m.get('device_code')

        if m.get('exclusive_tag') is not None:
            self.exclusive_tag = m.get('exclusive_tag')

        if m.get('grant_type') is not None:
            self.grant_type = m.get('grant_type')

        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('redirect_uri') is not None:
            self.redirect_uri = m.get('redirect_uri')

        if m.get('refresh_token') is not None:
            self.refresh_token = m.get('refresh_token')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

