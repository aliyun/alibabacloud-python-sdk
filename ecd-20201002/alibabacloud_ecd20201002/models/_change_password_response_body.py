# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangePasswordResponseBody(DaraModel):
    def __init__(
        self,
        login_token: str = None,
        request_id: str = None,
    ):
        # The logon token.
        self.login_token = login_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

