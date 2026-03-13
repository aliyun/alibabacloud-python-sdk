# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FlightItineraryScanQueryRequest(DaraModel):
    def __init__(
        self,
        bill_date: str = None,
        bill_id: int = None,
        invoice_sub_task_id: int = None,
        itinerary_num: str = None,
        order_id: int = None,
        page_no: int = None,
        page_size: int = None,
        ticket_no: str = None,
    ):
        self.bill_date = bill_date
        self.bill_id = bill_id
        self.invoice_sub_task_id = invoice_sub_task_id
        self.itinerary_num = itinerary_num
        self.order_id = order_id
        self.page_no = page_no
        self.page_size = page_size
        self.ticket_no = ticket_no

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

        if self.itinerary_num is not None:
            result['itinerary_num'] = self.itinerary_num

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.page_no is not None:
            result['page_no'] = self.page_no

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bill_date') is not None:
            self.bill_date = m.get('bill_date')

        if m.get('bill_id') is not None:
            self.bill_id = m.get('bill_id')

        if m.get('invoice_sub_task_id') is not None:
            self.invoice_sub_task_id = m.get('invoice_sub_task_id')

        if m.get('itinerary_num') is not None:
            self.itinerary_num = m.get('itinerary_num')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('page_no') is not None:
            self.page_no = m.get('page_no')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        return self

