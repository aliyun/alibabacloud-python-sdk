# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FuPointBillSettlementQueryRequest(DaraModel):
    def __init__(
        self,
        bill_batch: str = None,
        bill_record_time_end: str = None,
        bill_record_time_start: str = None,
        cooperator_id: str = None,
        order_id: int = None,
        page_no: int = None,
        page_size: int = None,
        period_end: str = None,
        period_start: str = None,
        scroll_id: str = None,
        scroll_mod: bool = None,
    ):
        self.bill_batch = bill_batch
        self.bill_record_time_end = bill_record_time_end
        self.bill_record_time_start = bill_record_time_start
        self.cooperator_id = cooperator_id
        self.order_id = order_id
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.period_end = period_end
        self.period_start = period_start
        self.scroll_id = scroll_id
        self.scroll_mod = scroll_mod

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_batch is not None:
            result['bill_batch'] = self.bill_batch

        if self.bill_record_time_end is not None:
            result['bill_record_time_end'] = self.bill_record_time_end

        if self.bill_record_time_start is not None:
            result['bill_record_time_start'] = self.bill_record_time_start

        if self.cooperator_id is not None:
            result['cooperator_id'] = self.cooperator_id

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.page_no is not None:
            result['page_no'] = self.page_no

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.period_end is not None:
            result['period_end'] = self.period_end

        if self.period_start is not None:
            result['period_start'] = self.period_start

        if self.scroll_id is not None:
            result['scroll_id'] = self.scroll_id

        if self.scroll_mod is not None:
            result['scroll_mod'] = self.scroll_mod

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bill_batch') is not None:
            self.bill_batch = m.get('bill_batch')

        if m.get('bill_record_time_end') is not None:
            self.bill_record_time_end = m.get('bill_record_time_end')

        if m.get('bill_record_time_start') is not None:
            self.bill_record_time_start = m.get('bill_record_time_start')

        if m.get('cooperator_id') is not None:
            self.cooperator_id = m.get('cooperator_id')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('page_no') is not None:
            self.page_no = m.get('page_no')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('period_end') is not None:
            self.period_end = m.get('period_end')

        if m.get('period_start') is not None:
            self.period_start = m.get('period_start')

        if m.get('scroll_id') is not None:
            self.scroll_id = m.get('scroll_id')

        if m.get('scroll_mod') is not None:
            self.scroll_mod = m.get('scroll_mod')

        return self

