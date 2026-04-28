# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetShareLinkTokenResponseBody(DaraModel):
    def __init__(
        self,
        expires_in: int = None,
        share_token: str = None,
    ):
        # The validity period of the token. Unit: seconds. For example, a value of 7200 indicates two hours.
        self.expires_in = expires_in
        # The JSON Web Token (JWT).
        self.share_token = share_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expires_in is not None:
            result['expires_in'] = self.expires_in

        if self.share_token is not None:
            result['share_token'] = self.share_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expires_in') is not None:
            self.expires_in = m.get('expires_in')

        if m.get('share_token') is not None:
            self.share_token = m.get('share_token')

        return self

