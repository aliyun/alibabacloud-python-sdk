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
        # - The access token expiration time, in seconds. This specifies the expiration time for the user to access page operations. Default value: 86400 (one day). Valid values: 0 to 86400 (one day).
        # 
        # - The actual access token expiration time is the minimum value of accessTokenExpirationTime and expirationTime.
        # 
        # - If you call this operation by using Security Token Service (STS), the actual access token expiration time is the minimum value of accessTokenExpirationTime, expirationTime, and the STS token expiration time.
        self.access_token_expiration_time = access_token_expiration_time
        # - The expiration time, in seconds. This specifies the expiration time of the embedded page URL. Default value: 86400 (one day). Valid values: 0 to 2592000 (30 days).
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

