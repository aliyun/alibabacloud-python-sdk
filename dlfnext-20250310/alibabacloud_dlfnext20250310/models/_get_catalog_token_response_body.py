# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class GetCatalogTokenResponseBody(DaraModel):
    def __init__(
        self,
        expires_at_millis: int = None,
        token: Dict[str, str] = None,
    ):
        self.expires_at_millis = expires_at_millis
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expires_at_millis is not None:
            result['expiresAtMillis'] = self.expires_at_millis

        if self.token is not None:
            result['token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expiresAtMillis') is not None:
            self.expires_at_millis = m.get('expiresAtMillis')

        if m.get('token') is not None:
            self.token = m.get('token')

        return self

