# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TrainOrderPayRequest(DaraModel):
    def __init__(
        self,
        order_id: str = None,
        out_order_id: str = None,
        pay_amount: int = None,
    ):
        # This parameter is required.
        self.order_id = order_id
        # This parameter is required.
        self.out_order_id = out_order_id
        # This parameter is required.
        self.pay_amount = pay_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        if self.pay_amount is not None:
            result['pay_amount'] = self.pay_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        if m.get('pay_amount') is not None:
            self.pay_amount = m.get('pay_amount')

        return self

