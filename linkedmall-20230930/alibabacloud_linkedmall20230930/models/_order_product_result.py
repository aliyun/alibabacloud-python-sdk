# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class OrderProductResult(DaraModel):
    def __init__(
        self,
        can_sell: bool = None,
        features: Dict[str, Any] = None,
        message: str = None,
        price: int = None,
        product_id: str = None,
        product_pic_url: str = None,
        product_title: str = None,
        purchaser_id: str = None,
        quantity: int = None,
        sku_id: str = None,
        sku_title: str = None,
    ):
        self.can_sell = can_sell
        self.features = features
        self.message = message
        self.price = price
        self.product_id = product_id
        self.product_pic_url = product_pic_url
        self.product_title = product_title
        self.purchaser_id = purchaser_id
        self.quantity = quantity
        # SKUID
        self.sku_id = sku_id
        self.sku_title = sku_title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_sell is not None:
            result['canSell'] = self.can_sell

        if self.features is not None:
            result['features'] = self.features

        if self.message is not None:
            result['message'] = self.message

        if self.price is not None:
            result['price'] = self.price

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.product_pic_url is not None:
            result['productPicUrl'] = self.product_pic_url

        if self.product_title is not None:
            result['productTitle'] = self.product_title

        if self.purchaser_id is not None:
            result['purchaserId'] = self.purchaser_id

        if self.quantity is not None:
            result['quantity'] = self.quantity

        if self.sku_id is not None:
            result['skuId'] = self.sku_id

        if self.sku_title is not None:
            result['skuTitle'] = self.sku_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('canSell') is not None:
            self.can_sell = m.get('canSell')

        if m.get('features') is not None:
            self.features = m.get('features')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('productPicUrl') is not None:
            self.product_pic_url = m.get('productPicUrl')

        if m.get('productTitle') is not None:
            self.product_title = m.get('productTitle')

        if m.get('purchaserId') is not None:
            self.purchaser_id = m.get('purchaserId')

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        if m.get('skuId') is not None:
            self.sku_id = m.get('skuId')

        if m.get('skuTitle') is not None:
            self.sku_title = m.get('skuTitle')

        return self

