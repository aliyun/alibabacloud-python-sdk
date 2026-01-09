# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshTokenRequest(DaraModel):
    def __init__(
        self,
        access_token_expiration_time: int = None,
        ticket: str = None,
    ):
        # *   The validity period of the access token. Unit: seconds. Default value: 86400, which specifies one day. Valid values: 0 to 86400.
        # *   The validity period of the access token is the smaller value between accessTokenExpirationTime and expirationTime.
        # *   If you use a Security Token Service (STS) token to call this operation, the validity period of the access token is the smallest value among accessTokenExpirationTime, expirationTime, and the validity period of the STS token.
        self.access_token_expiration_time = access_token_expiration_time
        # The ticket that is used for logon-free access.
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token_expiration_time is not None:
            result['accessTokenExpirationTime'] = self.access_token_expiration_time

        if self.ticket is not None:
            result['ticket'] = self.ticket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessTokenExpirationTime') is not None:
            self.access_token_expiration_time = m.get('accessTokenExpirationTime')

        if m.get('ticket') is not None:
            self.ticket = m.get('ticket')

        return self

