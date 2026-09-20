# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConvertInstanceRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        duration: int = None,
        pay_type: str = None,
        pricing_cycle: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The subscription duration. Valid values:
        # - If PricingCycle is set to year, the value ranges from 1 to 3.
        # - If PricingCycle is set to month, the value ranges from 1 to 9.
        self.duration = duration
        # The billing method of the instance. Valid values:
        # 
        # - **Prepaid**: subscription.
        # - **Postpaid**: pay-as-you-go.
        self.pay_type = pay_type
        # The unit of the subscription period. Valid values:
        # - year: year.
        # - month: month.
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

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        return self

