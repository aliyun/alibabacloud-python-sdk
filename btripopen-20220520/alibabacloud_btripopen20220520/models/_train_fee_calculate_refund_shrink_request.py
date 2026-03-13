# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TrainFeeCalculateRefundShrinkRequest(DaraModel):
    def __init__(
        self,
        distribute_order_id: str = None,
        order_id: str = None,
        refund_train_infos_shrink: str = None,
    ):
        # This parameter is required.
        self.distribute_order_id = distribute_order_id
        # This parameter is required.
        self.order_id = order_id
        # This parameter is required.
        self.refund_train_infos_shrink = refund_train_infos_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.distribute_order_id is not None:
            result['distribute_order_id'] = self.distribute_order_id

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.refund_train_infos_shrink is not None:
            result['refund_train_infos'] = self.refund_train_infos_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('distribute_order_id') is not None:
            self.distribute_order_id = m.get('distribute_order_id')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('refund_train_infos') is not None:
            self.refund_train_infos_shrink = m.get('refund_train_infos')

        return self

