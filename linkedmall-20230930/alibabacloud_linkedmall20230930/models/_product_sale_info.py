# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class ProductSaleInfo(DaraModel):
    def __init__(
        self,
        can_sell: bool = None,
        division_code: str = None,
        fuzzy_quantity: str = None,
        limit_rules: List[main_models.LimitRule] = None,
        lm_item_id: str = None,
        product_id: str = None,
        product_status: str = None,
        quantity: int = None,
        request_id: str = None,
        shop_id: str = None,
        skus: List[main_models.SkuSaleInfo] = None,
        title: str = None,
    ):
        self.can_sell = can_sell
        self.division_code = division_code
        self.fuzzy_quantity = fuzzy_quantity
        self.limit_rules = limit_rules
        self.lm_item_id = lm_item_id
        self.product_id = product_id
        self.product_status = product_status
        self.quantity = quantity
        self.request_id = request_id
        self.shop_id = shop_id
        self.skus = skus
        self.title = title

    def validate(self):
        if self.limit_rules:
            for v1 in self.limit_rules:
                 if v1:
                    v1.validate()
        if self.skus:
            for v1 in self.skus:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_sell is not None:
            result['canSell'] = self.can_sell

        if self.division_code is not None:
            result['divisionCode'] = self.division_code

        if self.fuzzy_quantity is not None:
            result['fuzzyQuantity'] = self.fuzzy_quantity

        result['limitRules'] = []
        if self.limit_rules is not None:
            for k1 in self.limit_rules:
                result['limitRules'].append(k1.to_map() if k1 else None)

        if self.lm_item_id is not None:
            result['lmItemId'] = self.lm_item_id

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.product_status is not None:
            result['productStatus'] = self.product_status

        if self.quantity is not None:
            result['quantity'] = self.quantity

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.shop_id is not None:
            result['shopId'] = self.shop_id

        result['skus'] = []
        if self.skus is not None:
            for k1 in self.skus:
                result['skus'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('canSell') is not None:
            self.can_sell = m.get('canSell')

        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')

        if m.get('fuzzyQuantity') is not None:
            self.fuzzy_quantity = m.get('fuzzyQuantity')

        self.limit_rules = []
        if m.get('limitRules') is not None:
            for k1 in m.get('limitRules'):
                temp_model = main_models.LimitRule()
                self.limit_rules.append(temp_model.from_map(k1))

        if m.get('lmItemId') is not None:
            self.lm_item_id = m.get('lmItemId')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('productStatus') is not None:
            self.product_status = m.get('productStatus')

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')

        self.skus = []
        if m.get('skus') is not None:
            for k1 in m.get('skus'):
                temp_model = main_models.SkuSaleInfo()
                self.skus.append(temp_model.from_map(k1))

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

