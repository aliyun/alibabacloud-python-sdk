# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterCreateMemberApiKeyRequest(DaraModel):
    def __init__(
        self,
        expire_at: str = None,
        name: str = None,
    ):
        # The expiration time in the format of yyyy-MM-dd HH:mm:ss. This parameter is optional. If not specified, the key is permanently valid.
        self.expire_at = expire_at
        # The name of the API key. This parameter is optional.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_at is not None:
            result['expireAt'] = self.expire_at

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expireAt') is not None:
            self.expire_at = m.get('expireAt')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

