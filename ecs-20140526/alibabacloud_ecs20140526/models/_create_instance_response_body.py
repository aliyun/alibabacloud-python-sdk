# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstanceResponseBody(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        order_id: str = None,
        request_id: str = None,
        trade_price: float = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The order ID. This parameter is returned only if `InstanceChargeType` is set to PrePaid.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id
        # The transaction price.
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

