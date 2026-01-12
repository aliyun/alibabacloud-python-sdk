# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListJobSanityCheckResultsRequest(DaraModel):
    def __init__(
        self,
        order: str = None,
    ):
        # The sorting order:
        # 
        # *   desc: descending order
        # *   asc: ascending order
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order is not None:
            result['Order'] = self.order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')

        return self

