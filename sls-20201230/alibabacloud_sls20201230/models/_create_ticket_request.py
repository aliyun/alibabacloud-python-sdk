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
        # *   The validity period of the access token. Unit: seconds. Default value: 86400, which specifies one day. Valid values: 0 to 86400.
        # *   The validity period of the access token is the smaller value between accessTokenExpirationTime and expirationTime.
        # *   If you use a Security Token Service (STS) token to call this operation, the validity period of the access token is the smallest value among accessTokenExpirationTime, expirationTime, and the validity period of the STS token.
        self.access_token_expiration_time = access_token_expiration_time
        # *   You must use the Simple Log Service endpoint for the China (Shanghai) or Singapore region to call the CreateTicket operation. After you obtain the ticket, you can use the ticket regardless of the region.
        # *   The validity period for the URL of the console page that you want to embed. Unit: seconds. Default value: 86400 (one day). Valid values: 0 to 2592000 (30 days).
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

