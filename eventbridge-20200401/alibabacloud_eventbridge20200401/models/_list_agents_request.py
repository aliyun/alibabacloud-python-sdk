# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgentsRequest(DaraModel):
    def __init__(
        self,
        after: str = None,
        limit: str = None,
        order: str = None,
    ):
        self.after = after
        self.limit = limit
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after is not None:
            result['After'] = self.after

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.order is not None:
            result['Order'] = self.order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('After') is not None:
            self.after = m.get('After')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        return self

