# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterRenewApiKeyRequest(DaraModel):
    def __init__(
        self,
        expire_at: str = None,
    ):
        # The new expiration time in RFC 3339 format. The time must be later than the current time. If this parameter is not specified or is set to null, the API key remains valid indefinitely. This parameter only modifies the validity period and does not change the enabled or disabled status.
        self.expire_at = expire_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_at is not None:
            result['expireAt'] = self.expire_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expireAt') is not None:
            self.expire_at = m.get('expireAt')

        return self

