# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ElasticSpotSpec(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        spot_discount_limit: float = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
    ):
        # The spot instance type.
        self.instance_type = instance_type
        # The maximum discount percentage for the spot instance. The system does not select an instance if its discount exceeds this limit. For example, if you set this parameter to `90`, the system considers only instances with a discount of 90% or less.
        self.spot_discount_limit = spot_discount_limit
        # The maximum hourly price you are willing to pay for a spot instance. If omitted, the on-demand price is the default.
        self.spot_price_limit = spot_price_limit
        # The strategy for allocating spot instances. Valid values:
        # 
        # - `LowestPrice`: Launches instances from the spot capacity pool offering the lowest price. This is the default strategy.
        # 
        # - `CapacityOptimized`: Launches instances from the spot capacity pool offering optimal capacity.
        self.spot_strategy = spot_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.spot_discount_limit is not None:
            result['SpotDiscountLimit'] = self.spot_discount_limit

        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('SpotDiscountLimit') is not None:
            self.spot_discount_limit = m.get('SpotDiscountLimit')

        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        return self

