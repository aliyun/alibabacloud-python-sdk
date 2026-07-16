# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SpotBidPrice(DaraModel):
    def __init__(
        self,
        bid_price: float = None,
        instance_type: str = None,
    ):
        # The maximum hourly bid price for the instance, with up to three decimal places. This parameter applies only when `SpotStrategy` is set to `SpotWithPriceLimit`.
        self.bid_price = bid_price
        # The ECS instance type.
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bid_price is not None:
            result['BidPrice'] = self.bid_price

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BidPrice') is not None:
            self.bid_price = m.get('BidPrice')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        return self

