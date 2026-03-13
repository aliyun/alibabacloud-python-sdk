# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OrderRefundDetailQueryRequest(DaraModel):
    def __init__(
        self,
        cooperator_order_id: str = None,
        order_id: str = None,
    ):
        # This parameter is required.
        self.cooperator_order_id = cooperator_order_id
        # This parameter is required.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cooperator_order_id is not None:
            result['cooperator_order_id'] = self.cooperator_order_id

        if self.order_id is not None:
            result['order_id'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cooperator_order_id') is not None:
            self.cooperator_order_id = m.get('cooperator_order_id')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        return self

