# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOrderRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        commodity: str = None,
        order_souce: str = None,
        order_type: str = None,
        owner_id: str = None,
        payment_type: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.commodity = commodity
        self.order_souce = order_souce
        # This parameter is required.
        self.order_type = order_type
        self.owner_id = owner_id
        # This parameter is required.
        self.payment_type = payment_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.commodity is not None:
            result['Commodity'] = self.commodity

        if self.order_souce is not None:
            result['OrderSouce'] = self.order_souce

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Commodity') is not None:
            self.commodity = m.get('Commodity')

        if m.get('OrderSouce') is not None:
            self.order_souce = m.get('OrderSouce')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        return self

