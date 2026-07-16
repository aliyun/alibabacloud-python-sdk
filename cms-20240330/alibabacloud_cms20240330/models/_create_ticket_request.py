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
        # - The expiration time of the access token, in seconds. This is the period during which a user can access the page APIs. The value can range from 0 to 86,400 seconds (one day). The default value is 86,400 seconds (one day).
        # 
        # - The effective expiration time of the access token is the minimum value of accessTokenExpirationTime and expirationTime.
        # 
        # - If you call the operation using a Security Token Service (STS) token, the effective expiration time of the access token is the minimum value of accessTokenExpirationTime, expirationTime, and the expiration time of the STS token.
        self.access_token_expiration_time = access_token_expiration_time
        # - The expiration time of the URL for the embedded page, in seconds. The value can range from 0 to 2,592,000 seconds (30 days). The default value is 86,400 seconds (one day).
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

