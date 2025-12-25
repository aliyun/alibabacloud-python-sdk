# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDevicesByAliasRequest(DaraModel):
    def __init__(
        self,
        alias: str = None,
        app_key: int = None,
    ):
        # This parameter is required.
        self.alias = alias
        # This parameter is required.
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        return self

