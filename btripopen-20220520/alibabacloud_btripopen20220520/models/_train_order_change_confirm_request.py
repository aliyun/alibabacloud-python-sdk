# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TrainOrderChangeConfirmRequest(DaraModel):
    def __init__(
        self,
        change_apply_id: str = None,
        change_settle_amount: int = None,
        order_id: str = None,
        out_change_apply_id: str = None,
        out_order_id: str = None,
    ):
        # This parameter is required.
        self.change_apply_id = change_apply_id
        # This parameter is required.
        self.change_settle_amount = change_settle_amount
        # This parameter is required.
        self.order_id = order_id
        # This parameter is required.
        self.out_change_apply_id = out_change_apply_id
        # This parameter is required.
        self.out_order_id = out_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_apply_id is not None:
            result['change_apply_id'] = self.change_apply_id

        if self.change_settle_amount is not None:
            result['change_settle_amount'] = self.change_settle_amount

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.out_change_apply_id is not None:
            result['out_change_apply_id'] = self.out_change_apply_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change_apply_id') is not None:
            self.change_apply_id = m.get('change_apply_id')

        if m.get('change_settle_amount') is not None:
            self.change_settle_amount = m.get('change_settle_amount')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_change_apply_id') is not None:
            self.out_change_apply_id = m.get('out_change_apply_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        return self

