# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfirmDisburseCmd(DaraModel):
    def __init__(
        self,
        order_id: str = None,
        purchase_order_id: str = None,
    ):
        self.order_id = order_id
        self.purchase_order_id = purchase_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['orderId'] = self.order_id

        if self.purchase_order_id is not None:
            result['purchaseOrderId'] = self.purchase_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        if m.get('purchaseOrderId') is not None:
            self.purchase_order_id = m.get('purchaseOrderId')

        return self

