# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateTokenResponseBody(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        expires_at: int = None,
        expires_in: int = None,
        id_token: str = None,
        refresh_token: str = None,
        token_type: str = None,
    ):
        # The access token.
        self.access_token = access_token
        # The time when the token expires. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.expires_at = expires_at
        # The remaining validity period of the token. Unit: seconds.
        self.expires_in = expires_in
        # The ID token.
        self.id_token = id_token
        # The refresh token.
        self.refresh_token = refresh_token
        # The type of the token. Valid values: Basic Bearer
        self.token_type = token_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token is not None:
            result['access_token'] = self.access_token

        if self.expires_at is not None:
            result['expires_at'] = self.expires_at

        if self.expires_in is not None:
            result['expires_in'] = self.expires_in

        if self.id_token is not None:
            result['id_token'] = self.id_token

        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token

        if self.token_type is not None:
            result['token_type'] = self.token_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access_token') is not None:
            self.access_token = m.get('access_token')

        if m.get('expires_at') is not None:
            self.expires_at = m.get('expires_at')

        if m.get('expires_in') is not None:
            self.expires_in = m.get('expires_in')

        if m.get('id_token') is not None:
            self.id_token = m.get('id_token')

        if m.get('refresh_token') is not None:
            self.refresh_token = m.get('refresh_token')

        if m.get('token_type') is not None:
            self.token_type = m.get('token_type')

        return self

