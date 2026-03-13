# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsInvoiceScanQueryRequest(DaraModel):
    def __init__(
        self,
        bill_date: str = None,
        bill_id: int = None,
        invoice_sub_task_id: int = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.bill_date = bill_date
        self.bill_id = bill_id
        self.invoice_sub_task_id = invoice_sub_task_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_date is not None:
            result['bill_date'] = self.bill_date

        if self.bill_id is not None:
            result['bill_id'] = self.bill_id

        if self.invoice_sub_task_id is not None:
            result['invoice_sub_task_id'] = self.invoice_sub_task_id

        if self.page_no is not None:
            result['page_no'] = self.page_no

        if self.page_size is not None:
            result['page_size'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bill_date') is not None:
            self.bill_date = m.get('bill_date')

        if m.get('bill_id') is not None:
            self.bill_id = m.get('bill_id')

        if m.get('invoice_sub_task_id') is not None:
            self.invoice_sub_task_id = m.get('invoice_sub_task_id')

        if m.get('page_no') is not None:
            self.page_no = m.get('page_no')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        return self

