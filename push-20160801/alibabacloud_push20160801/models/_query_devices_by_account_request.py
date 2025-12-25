# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDevicesByAccountRequest(DaraModel):
    def __init__(
        self,
        account: str = None,
        app_key: int = None,
    ):
        # This parameter is required.
        self.account = account
        # This parameter is required.
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        return self

