# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenewInstanceRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        duration: int = None,
        pricing_cycle: str = None,
    ):
        # The instance ID of the target instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The renewal epoch for the target instance.
        # 
        # - If PricingCycle is set to **year**, valid values are 1 to 3.
        # - If PricingCycle is set to **month**, valid values are 1 to 9.
        # 
        # This parameter is required.
        self.duration = duration
        # The unit of the renewal epoch for the target instance.
        # 
        # - **year**: year.
        # - **month**: month.
        # 
        # This parameter is required.
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        return self

