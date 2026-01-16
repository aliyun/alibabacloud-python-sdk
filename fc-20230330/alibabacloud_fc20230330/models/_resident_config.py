# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResidentConfig(DaraModel):
    def __init__(
        self,
        count: int = None,
        pool_id: str = None,
    ):
        self.count = count
        self.pool_id = pool_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        if self.pool_id is not None:
            result['poolId'] = self.pool_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('poolId') is not None:
            self.pool_id = m.get('poolId')

        return self

