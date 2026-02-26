# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OrderRenderProductDTO(DaraModel):
    def __init__(
        self,
        product_id: str = None,
        purchaser_id: str = None,
        quantity: int = None,
        sku_id: str = None,
    ):
        # This parameter is required.
        self.product_id = product_id
        # This parameter is required.
        self.purchaser_id = purchaser_id
        # This parameter is required.
        self.quantity = quantity
        # skuID
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
        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.purchaser_id is not None:
            result['purchaserId'] = self.purchaser_id

        if self.quantity is not None:
            result['quantity'] = self.quantity

        if self.sku_id is not None:
            result['skuId'] = self.sku_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('purchaserId') is not None:
            self.purchaser_id = m.get('purchaserId')

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        if m.get('skuId') is not None:
            self.sku_id = m.get('skuId')

        return self

