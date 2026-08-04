# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BalancePoolSummaryDTO(DaraModel):
    def __init__(
        self,
        allocated: float = None,
        available: float = None,
        total: float = None,
    ):
        self.allocated = allocated
        self.available = available
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocated is not None:
            result['allocated'] = self.allocated

        if self.available is not None:
            result['available'] = self.available

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allocated') is not None:
            self.allocated = m.get('allocated')

        if m.get('available') is not None:
            self.available = m.get('available')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

