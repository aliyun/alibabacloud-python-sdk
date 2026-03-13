# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TrainApplyRefundShrinkRequest(DaraModel):
    def __init__(
        self,
        order_id: str = None,
        out_order_id: str = None,
        out_refund_id: str = None,
        refund_train_infos_shrink: str = None,
    ):
        # This parameter is required.
        self.order_id = order_id
        # This parameter is required.
        self.out_order_id = out_order_id
        # This parameter is required.
        self.out_refund_id = out_refund_id
        # This parameter is required.
        self.refund_train_infos_shrink = refund_train_infos_shrink

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

        if self.out_refund_id is not None:
            result['out_refund_id'] = self.out_refund_id

        if self.refund_train_infos_shrink is not None:
            result['refund_train_infos'] = self.refund_train_infos_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        if m.get('out_refund_id') is not None:
            self.out_refund_id = m.get('out_refund_id')

        if m.get('refund_train_infos') is not None:
            self.refund_train_infos_shrink = m.get('refund_train_infos')

        return self

