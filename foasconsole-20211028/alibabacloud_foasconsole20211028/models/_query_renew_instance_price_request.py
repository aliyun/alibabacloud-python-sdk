# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRenewInstancePriceRequest(DaraModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        pricing_cycle: str = None,
        promotion_code: str = None,
        region: str = None,
        use_promotion_code: bool = None,
    ):
        # This parameter is required.
        self.duration = duration
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.pricing_cycle = pricing_cycle
        self.promotion_code = promotion_code
        # This parameter is required.
        self.region = region
        self.use_promotion_code = use_promotion_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.region is not None:
            result['Region'] = self.region

        if self.use_promotion_code is not None:
            result['UsePromotionCode'] = self.use_promotion_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('UsePromotionCode') is not None:
            self.use_promotion_code = m.get('UsePromotionCode')

        return self

