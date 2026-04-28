# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryOrderPriceResponseBody(DaraModel):
    def __init__(
        self,
        discount_price: float = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        self.discount_price = discount_price
        self.original_price = original_price
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discount_price is not None:
            result['discount_price'] = self.discount_price

        if self.original_price is not None:
            result['original_price'] = self.original_price

        if self.trade_price is not None:
            result['trade_price'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('discount_price') is not None:
            self.discount_price = m.get('discount_price')

        if m.get('original_price') is not None:
            self.original_price = m.get('original_price')

        if m.get('trade_price') is not None:
            self.trade_price = m.get('trade_price')

        return self

