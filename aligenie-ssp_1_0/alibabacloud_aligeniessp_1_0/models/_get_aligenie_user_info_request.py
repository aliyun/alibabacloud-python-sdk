# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAligenieUserInfoRequest(DaraModel):
    def __init__(
        self,
        login_state_access_token: str = None,
    ):
        # Logon state access credential
        # 
        # This parameter is required.
        self.login_state_access_token = login_state_access_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.login_state_access_token is not None:
            result['LoginStateAccessToken'] = self.login_state_access_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginStateAccessToken') is not None:
            self.login_state_access_token = m.get('LoginStateAccessToken')

        return self

