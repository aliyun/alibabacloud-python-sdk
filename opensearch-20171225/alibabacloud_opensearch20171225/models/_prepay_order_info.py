# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PrepayOrderInfo(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        duration: int = None,
        pricing_cycle: str = None,
    ):
        self.auto_renew = auto_renew
        self.duration = duration
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew

        if self.duration is not None:
            result['duration'] = self.duration

        if self.pricing_cycle is not None:
            result['pricingCycle'] = self.pricing_cycle

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('pricingCycle') is not None:
            self.pricing_cycle = m.get('pricingCycle')

        return self

