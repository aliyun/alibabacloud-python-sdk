# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IncrByCacheOperateSyncRequest(DaraModel):
    def __init__(
        self,
        default_value: int = None,
        expire_seconds: int = None,
        key: str = None,
        step: int = None,
    ):
        self.default_value = default_value
        self.expire_seconds = expire_seconds
        self.key = key
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.expire_seconds is not None:
            result['ExpireSeconds'] = self.expire_seconds

        if self.key is not None:
            result['Key'] = self.key

        if self.step is not None:
            result['Step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('ExpireSeconds') is not None:
            self.expire_seconds = m.get('ExpireSeconds')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        return self

