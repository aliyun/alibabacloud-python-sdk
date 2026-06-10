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
        self.instance_type = instance_type
        self.spot_discount_limit = spot_discount_limit
        self.spot_price_limit = spot_price_limit
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

