# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApiKeyInput(DaraModel):
    def __init__(
        self,
        api_key_name: str = None,
        expire_time: str = None,
    ):
        self.api_key_name = api_key_name
        self.expire_time = expire_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_name is not None:
            result['apiKeyName'] = self.api_key_name

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKeyName') is not None:
            self.api_key_name = m.get('apiKeyName')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        return self

