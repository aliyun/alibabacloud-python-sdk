# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GenerateOauthTokenResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        token_response: main_models.GenerateOauthTokenResponseBodyTokenResponse = None,
    ):
        self.request_id = request_id
        self.token_response = token_response

    def validate(self):
        if self.token_response:
            self.token_response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.token_response is not None:
            result['TokenResponse'] = self.token_response.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TokenResponse') is not None:
            temp_model = main_models.GenerateOauthTokenResponseBodyTokenResponse()
            self.token_response = temp_model.from_map(m.get('TokenResponse'))

        return self

class GenerateOauthTokenResponseBodyTokenResponse(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        expires_at: int = None,
        expires_in: int = None,
        token_type: str = None,
    ):
        # Access Token。
        self.access_token = access_token
        self.expires_at = expires_at
        self.expires_in = expires_in
        self.token_type = token_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token is not None:
            result['AccessToken'] = self.access_token

        if self.expires_at is not None:
            result['ExpiresAt'] = self.expires_at

        if self.expires_in is not None:
            result['ExpiresIn'] = self.expires_in

        if self.token_type is not None:
            result['TokenType'] = self.token_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')

        if m.get('ExpiresAt') is not None:
            self.expires_at = m.get('ExpiresAt')

        if m.get('ExpiresIn') is not None:
            self.expires_in = m.get('ExpiresIn')

        if m.get('TokenType') is not None:
            self.token_type = m.get('TokenType')

        return self

