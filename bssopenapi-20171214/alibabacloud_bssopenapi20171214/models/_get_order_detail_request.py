# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOrderDetailRequest(DaraModel):
    def __init__(
        self,
        order_id: str = None,
        owner_id: int = None,
    ):
        # The order ID.
        # 
        # This parameter is required.
        self.order_id = order_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

