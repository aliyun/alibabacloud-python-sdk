# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class GetMessageTokenResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetMessageTokenResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetMessageTokenResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetMessageTokenResponseBodyResult(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        access_token_expired_time: int = None,
        refresh_token: str = None,
    ):
        # The token used to establish a persistent connection.
        self.access_token = access_token
        # Indicates how long until the token expires. Unit: milliseconds.
        self.access_token_expired_time = access_token_expired_time
        # The updated token. If a token expires, you can call RefreshToken to obtain a new token.
        self.refresh_token = refresh_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token is not None:
            result['AccessToken'] = self.access_token

        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time

        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')

        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')

        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')

        return self

