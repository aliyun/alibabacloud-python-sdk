# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyInvoiceTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        bill_date: str = None,
        invoice_task_list_shrink: str = None,
    ):
        # This parameter is required.
        self.bill_date = bill_date
        # This parameter is required.
        self.invoice_task_list_shrink = invoice_task_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_date is not None:
            result['bill_date'] = self.bill_date

        if self.invoice_task_list_shrink is not None:
            result['invoice_task_list'] = self.invoice_task_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bill_date') is not None:
            self.bill_date = m.get('bill_date')

        if m.get('invoice_task_list') is not None:
            self.invoice_task_list_shrink = m.get('invoice_task_list')

        return self

