# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PaymentInfo(DaraModel):
    def __init__(
        self,
        auto_renew_duration: int = None,
        duration: int = None,
        is_auto_renew: bool = None,
        pricing_cycle: str = None,
    ):
        # The auto-renewal cycle. Unit: month. This parameter is required when **isAutoRenew** is set to **true**. The valid values are the same as those on the buy page.
        self.auto_renew_duration = auto_renew_duration
        # The subscription duration. This parameter is required. You can specify the duration in months or years.
        self.duration = duration
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # - true: enabled.
        # - false (default): disabled.
        self.is_auto_renew = is_auto_renew
        # The unit of the subscription duration. This parameter is required. Valid values:
        # 
        # - Year: year
        # - Month: month.
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew_duration is not None:
            result['autoRenewDuration'] = self.auto_renew_duration

        if self.duration is not None:
            result['duration'] = self.duration

        if self.is_auto_renew is not None:
            result['isAutoRenew'] = self.is_auto_renew

        if self.pricing_cycle is not None:
            result['pricingCycle'] = self.pricing_cycle

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRenewDuration') is not None:
            self.auto_renew_duration = m.get('autoRenewDuration')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('isAutoRenew') is not None:
            self.is_auto_renew = m.get('isAutoRenew')

        if m.get('pricingCycle') is not None:
            self.pricing_cycle = m.get('pricingCycle')

        return self

