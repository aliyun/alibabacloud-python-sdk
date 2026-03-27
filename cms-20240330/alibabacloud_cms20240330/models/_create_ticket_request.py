# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTicketRequest(DaraModel):
    def __init__(
        self,
        access_token_expiration_time: int = None,
        expiration_time: int = None,
    ):
        # - Access token expiration time (in seconds), which is the expiration time for the user to access the page interface. The default value is 86400 seconds (one day), and the range of values is from 0 to 86400 seconds (one day).
        # - The access token expiration time is the minimum value between `accessTokenExpirationTime` and `expirationTime`.
        # - If called through STS, the access token expiration time (i.e., the time during which the user can access the page interface) is the minimum value among `accessTokenExpirationTime`, `expirationTime`, and the STS expiration time.
        self.access_token_expiration_time = access_token_expiration_time
        # - Expiration time (in seconds), which is the expiration time for the embedded page URL. The default value is 86400 seconds (one day), and the range of values is from 0 to 2592000 seconds (30 days).
        self.expiration_time = expiration_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token_expiration_time is not None:
            result['accessTokenExpirationTime'] = self.access_token_expiration_time

        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessTokenExpirationTime') is not None:
            self.access_token_expiration_time = m.get('accessTokenExpirationTime')

        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')

        return self

