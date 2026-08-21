# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TicketQueryOrderRequest(DaraModel):
    def __init__(
        self,
        account_no: int = None,
        distributor_order_id: str = None,
    ):
        # This parameter is required.
        self.account_no = account_no
        # This parameter is required.
        self.distributor_order_id = distributor_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_no is not None:
            result['AccountNo'] = self.account_no

        if self.distributor_order_id is not None:
            result['DistributorOrderId'] = self.distributor_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')

        if m.get('DistributorOrderId') is not None:
            self.distributor_order_id = m.get('DistributorOrderId')

        return self

