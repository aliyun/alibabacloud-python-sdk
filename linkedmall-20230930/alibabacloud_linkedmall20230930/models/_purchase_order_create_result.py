# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PurchaseOrderCreateResult(DaraModel):
    def __init__(
        self,
        purchase_order_id: str = None,
        request_id: str = None,
    ):
        self.purchase_order_id = purchase_order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.purchase_order_id is not None:
            result['purchaseOrderId'] = self.purchase_order_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('purchaseOrderId') is not None:
            self.purchase_order_id = m.get('purchaseOrderId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

