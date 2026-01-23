# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDailyBillRequest(DaraModel):
    def __init__(
        self,
        bill_owner: str = None,
        bill_type: str = None,
        date: str = None,
    ):
        # Bill Owner type. Value Range:</br>
        # 1: Master account</br>
        # 2: Sub account</br>
        # 
        # This parameter is required.
        self.bill_owner = bill_owner
        # BillType. Value Range:</br>
        # 
        # - DailyOrder(Deprecated)
        # - DailyBill (Deprecated)
        # - DailyInstanceBill (Deprecated)
        # - DailyInstanceBillV2
        # 
        # This parameter is required.
        self.bill_type = bill_type
        # Billing date. Format YYYY-MM-DD
        # 
        # This parameter is required.
        self.date = date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_owner is not None:
            result['BillOwner'] = self.bill_owner

        if self.bill_type is not None:
            result['BillType'] = self.bill_type

        if self.date is not None:
            result['Date'] = self.date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillOwner') is not None:
            self.bill_owner = m.get('BillOwner')

        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')

        if m.get('Date') is not None:
            self.date = m.get('Date')

        return self

