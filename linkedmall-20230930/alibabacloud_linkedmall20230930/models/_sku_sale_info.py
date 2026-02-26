# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SkuSaleInfo(DaraModel):
    def __init__(
        self,
        can_not_sell_reason: str = None,
        can_sell: bool = None,
        division_code: str = None,
        fuzzy_quantity: str = None,
        mark_price: int = None,
        price: int = None,
        product_id: str = None,
        quantity: int = None,
        shop_id: str = None,
        sku_id: str = None,
        sku_status: str = None,
        title: str = None,
    ):
        self.can_not_sell_reason = can_not_sell_reason
        self.can_sell = can_sell
        self.division_code = division_code
        self.fuzzy_quantity = fuzzy_quantity
        self.mark_price = mark_price
        self.price = price
        self.product_id = product_id
        self.quantity = quantity
        self.shop_id = shop_id
        # skuId
        self.sku_id = sku_id
        self.sku_status = sku_status
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_not_sell_reason is not None:
            result['canNotSellReason'] = self.can_not_sell_reason

        if self.can_sell is not None:
            result['canSell'] = self.can_sell

        if self.division_code is not None:
            result['divisionCode'] = self.division_code

        if self.fuzzy_quantity is not None:
            result['fuzzyQuantity'] = self.fuzzy_quantity

        if self.mark_price is not None:
            result['markPrice'] = self.mark_price

        if self.price is not None:
            result['price'] = self.price

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.quantity is not None:
            result['quantity'] = self.quantity

        if self.shop_id is not None:
            result['shopId'] = self.shop_id

        if self.sku_id is not None:
            result['skuId'] = self.sku_id

        if self.sku_status is not None:
            result['skuStatus'] = self.sku_status

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('canNotSellReason') is not None:
            self.can_not_sell_reason = m.get('canNotSellReason')

        if m.get('canSell') is not None:
            self.can_sell = m.get('canSell')

        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')

        if m.get('fuzzyQuantity') is not None:
            self.fuzzy_quantity = m.get('fuzzyQuantity')

        if m.get('markPrice') is not None:
            self.mark_price = m.get('markPrice')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')

        if m.get('skuId') is not None:
            self.sku_id = m.get('skuId')

        if m.get('skuStatus') is not None:
            self.sku_status = m.get('skuStatus')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

