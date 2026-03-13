# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TrainFeeCalculateChangeShrinkRequest(DaraModel):
    def __init__(
        self,
        change_train_details_shrink: str = None,
        distribute_order_id: str = None,
        order_id: str = None,
    ):
        # This parameter is required.
        self.change_train_details_shrink = change_train_details_shrink
        # This parameter is required.
        self.distribute_order_id = distribute_order_id
        # This parameter is required.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_train_details_shrink is not None:
            result['change_train_details'] = self.change_train_details_shrink

        if self.distribute_order_id is not None:
            result['distribute_order_id'] = self.distribute_order_id

        if self.order_id is not None:
            result['order_id'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change_train_details') is not None:
            self.change_train_details_shrink = m.get('change_train_details')

        if m.get('distribute_order_id') is not None:
            self.distribute_order_id = m.get('distribute_order_id')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        return self

