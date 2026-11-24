# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateThirdAppAccessTokenResponseBody(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        expires_at: int = None,
        request_id: str = None,
    ):
        # The time-limited static access token created for the specified user and single cloud desktop. This is a sensitive credential. Do not log or expose the full value.
        self.access_token = access_token
        # The absolute expiration time of the token, in UNIX milliseconds. This parameter is not empty when the call is successful. GetLatestThirdAppAccessToken returns the original expiration time without extending it.
        self.expires_at = expires_at
        # The unique identifier of the request, which can be used to locate and troubleshoot issues.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')

        if m.get('ExpiresAt') is not None:
            self.expires_at = m.get('ExpiresAt')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

