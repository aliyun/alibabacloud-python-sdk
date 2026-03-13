# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MonthBillGetRequest(DaraModel):
    def __init__(
        self,
        bill_batch: str = None,
        bill_month: str = None,
    ):
        self.bill_batch = bill_batch
        self.bill_month = bill_month

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_batch is not None:
            result['bill_batch'] = self.bill_batch

        if self.bill_month is not None:
            result['bill_month'] = self.bill_month

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bill_batch') is not None:
            self.bill_batch = m.get('bill_batch')

        if m.get('bill_month') is not None:
            self.bill_month = m.get('bill_month')

        return self

