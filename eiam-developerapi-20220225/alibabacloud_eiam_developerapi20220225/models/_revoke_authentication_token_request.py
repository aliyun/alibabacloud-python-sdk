# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RevokeAuthenticationTokenRequest(DaraModel):
    def __init__(
        self,
        token: str = None,
        token_type_hint: str = None,
    ):
        # This parameter is required.
        self.token = token
        self.token_type_hint = token_type_hint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.token is not None:
            result['token'] = self.token

        if self.token_type_hint is not None:
            result['token_type_hint'] = self.token_type_hint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('token') is not None:
            self.token = m.get('token')

        if m.get('token_type_hint') is not None:
            self.token_type_hint = m.get('token_type_hint')

        return self

