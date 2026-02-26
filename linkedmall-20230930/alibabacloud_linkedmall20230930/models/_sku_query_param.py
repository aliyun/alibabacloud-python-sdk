# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SkuQueryParam(DaraModel):
    def __init__(
        self,
        buy_amount: int = None,
        product_id: str = None,
        sku_id: str = None,
    ):
        self.buy_amount = buy_amount
        # This parameter is required.
        self.product_id = product_id
        # skuid
        # 
        # This parameter is required.
        self.sku_id = sku_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buy_amount is not None:
            result['buyAmount'] = self.buy_amount

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.sku_id is not None:
            result['skuId'] = self.sku_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buyAmount') is not None:
            self.buy_amount = m.get('buyAmount')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('skuId') is not None:
            self.sku_id = m.get('skuId')

        return self

