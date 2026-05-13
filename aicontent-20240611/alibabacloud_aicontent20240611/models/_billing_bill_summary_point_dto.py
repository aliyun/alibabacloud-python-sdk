# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BillingBillSummaryPointDTO(DaraModel):
    def __init__(
        self,
        timestamp: int = None,
        total_amount: float = None,
    ):
        self.timestamp = timestamp
        self.total_amount = total_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.total_amount is not None:
            result['totalAmount'] = self.total_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('totalAmount') is not None:
            self.total_amount = m.get('totalAmount')

        return self

