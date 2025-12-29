# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DLOrder(DaraModel):
    def __init__(
        self,
        col: str = None,
        order: int = None,
    ):
        self.col = col
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.col is not None:
            result['Col'] = self.col

        if self.order is not None:
            result['Order'] = self.order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Col') is not None:
            self.col = m.get('Col')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        return self

