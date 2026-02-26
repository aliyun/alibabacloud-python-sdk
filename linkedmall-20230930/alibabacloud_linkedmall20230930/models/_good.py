# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Good(DaraModel):
    def __init__(
        self,
        good_name: str = None,
        product_id: str = None,
        quantity: int = None,
        sku_id: str = None,
        sku_title: str = None,
    ):
        self.good_name = good_name
        self.product_id = product_id
        self.quantity = quantity
        self.sku_id = sku_id
        self.sku_title = sku_title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.good_name is not None:
            result['goodName'] = self.good_name

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.quantity is not None:
            result['quantity'] = self.quantity

        if self.sku_id is not None:
            result['skuId'] = self.sku_id

        if self.sku_title is not None:
            result['skuTitle'] = self.sku_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('goodName') is not None:
            self.good_name = m.get('goodName')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        if m.get('skuId') is not None:
            self.sku_id = m.get('skuId')

        if m.get('skuTitle') is not None:
            self.sku_title = m.get('skuTitle')

        return self

