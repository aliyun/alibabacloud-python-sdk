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
        # - The expiration time of the access token in seconds. This specifies the period during which the token is valid for accessing page API operations. The default value is 86400 seconds (one day). The value must be an integer from 0 to 86400.
        # 
        # - The actual expiration time of the access token is the minimum value of accessTokenExpirationTime and expirationTime.
        # 
        # - If you call this operation using Security Token Service (STS), the actual expiration time of the access token is the minimum value of accessTokenExpirationTime, expirationTime, and the STS token expiration time.
        self.access_token_expiration_time = access_token_expiration_time
        # The logon-free ticket.
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

