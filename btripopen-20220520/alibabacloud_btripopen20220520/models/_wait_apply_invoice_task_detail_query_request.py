# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WaitApplyInvoiceTaskDetailQueryRequest(DaraModel):
    def __init__(
        self,
        bill_date: str = None,
    ):
        # This parameter is required.
        self.bill_date = bill_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_date is not None:
            result['bill_date'] = self.bill_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bill_date') is not None:
            self.bill_date = m.get('bill_date')

        return self

