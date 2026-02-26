# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GeneralBillPageQuery(DaraModel):
    def __init__(
        self,
        asc: bool = None,
        bill_id: str = None,
        bill_period: str = None,
        limit: int = None,
        order_by: str = None,
        order_direction: str = None,
        page_number: int = None,
        page_size: int = None,
        shop_id: str = None,
        start: int = None,
    ):
        # asc
        self.asc = asc
        # billId
        self.bill_id = bill_id
        # billPeriod
        self.bill_period = bill_period
        # limit
        self.limit = limit
        # orderBy
        self.order_by = order_by
        # orderDirection
        self.order_direction = order_direction
        # pageNumber
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        # shopId
        self.shop_id = shop_id
        # start
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asc is not None:
            result['asc'] = self.asc

        if self.bill_id is not None:
            result['billId'] = self.bill_id

        if self.bill_period is not None:
            result['billPeriod'] = self.bill_period

        if self.limit is not None:
            result['limit'] = self.limit

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.order_direction is not None:
            result['orderDirection'] = self.order_direction

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.shop_id is not None:
            result['shopId'] = self.shop_id

        if self.start is not None:
            result['start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asc') is not None:
            self.asc = m.get('asc')

        if m.get('billId') is not None:
            self.bill_id = m.get('billId')

        if m.get('billPeriod') is not None:
            self.bill_period = m.get('billPeriod')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('orderDirection') is not None:
            self.order_direction = m.get('orderDirection')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')

        if m.get('start') is not None:
            self.start = m.get('start')

        return self

