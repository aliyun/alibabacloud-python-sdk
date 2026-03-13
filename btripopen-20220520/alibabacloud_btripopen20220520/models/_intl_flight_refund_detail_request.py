# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IntlFlightRefundDetailRequest(DaraModel):
    def __init__(
        self,
        order_id: str = None,
        out_order_id: str = None,
        out_refund_apply_id: str = None,
        refund_apply_id: str = None,
    ):
        # This parameter is required.
        self.order_id = order_id
        self.out_order_id = out_order_id
        self.out_refund_apply_id = out_refund_apply_id
        # This parameter is required.
        self.refund_apply_id = refund_apply_id

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

        if self.out_refund_apply_id is not None:
            result['out_refund_apply_id'] = self.out_refund_apply_id

        if self.refund_apply_id is not None:
            result['refund_apply_id'] = self.refund_apply_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        if m.get('out_refund_apply_id') is not None:
            self.out_refund_apply_id = m.get('out_refund_apply_id')

        if m.get('refund_apply_id') is not None:
            self.refund_apply_id = m.get('refund_apply_id')

        return self

