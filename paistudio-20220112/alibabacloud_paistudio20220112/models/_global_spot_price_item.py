# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GlobalSpotPriceItem(DaraModel):
    def __init__(
        self,
        effective_at: str = None,
        instance_type: str = None,
        spot_discount: str = None,
    ):
        # The effective period.
        self.effective_at = effective_at
        # The instance type.
        self.instance_type = instance_type
        # The current market price.
        self.spot_discount = spot_discount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effective_at is not None:
            result['effectiveAt'] = self.effective_at

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        if self.spot_discount is not None:
            result['spotDiscount'] = self.spot_discount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effectiveAt') is not None:
            self.effective_at = m.get('effectiveAt')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        if m.get('spotDiscount') is not None:
            self.spot_discount = m.get('spotDiscount')

        return self

