# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePriceRequest(DaraModel):
    def __init__(
        self,
        commodity: str = None,
        order_type: str = None,
    ):
        # This parameter is required.
        self.commodity = commodity
        # This parameter is required.
        self.order_type = order_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity is not None:
            result['Commodity'] = self.commodity

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commodity') is not None:
            self.commodity = m.get('Commodity')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        return self

