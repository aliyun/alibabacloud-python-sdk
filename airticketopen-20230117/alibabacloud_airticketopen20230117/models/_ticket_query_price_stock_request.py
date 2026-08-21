# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TicketQueryPriceStockRequest(DaraModel):
    def __init__(
        self,
        account_no: int = None,
        end_date: str = None,
        product_id: str = None,
        start_date: str = None,
    ):
        # This parameter is required.
        self.account_no = account_no
        self.end_date = end_date
        # This parameter is required.
        self.product_id = product_id
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_no is not None:
            result['AccountNo'] = self.account_no

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

