# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FindPkByHidForLoginWithLegacyRequest(DaraModel):
    def __init__(
        self,
        hid: str = None,
        security_token: str = None,
    ):
        self.hid = hid
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hid is not None:
            result['Hid'] = self.hid

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

