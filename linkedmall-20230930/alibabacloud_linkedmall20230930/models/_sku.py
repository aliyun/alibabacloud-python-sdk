# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class Sku(DaraModel):
    def __init__(
        self,
        barcode: str = None,
        can_sell: bool = None,
        discount_retail_price: int = None,
        division_code: str = None,
        fuzzy_quantity: str = None,
        mark_price: int = None,
        pic_url: str = None,
        platform_price: int = None,
        price: int = None,
        product_id: str = None,
        quantity: int = None,
        rank_value: int = None,
        shop_id: str = None,
        sku_alias: str = None,
        sku_id: str = None,
        sku_specs: List[main_models.SkuSpec] = None,
        sku_specs_code: str = None,
        sku_status: str = None,
        suggested_retail_price: int = None,
        title: str = None,
    ):
        self.barcode = barcode
        self.can_sell = can_sell
        self.discount_retail_price = discount_retail_price
        self.division_code = division_code
        self.fuzzy_quantity = fuzzy_quantity
        self.mark_price = mark_price
        self.pic_url = pic_url
        self.platform_price = platform_price
        self.price = price
        self.product_id = product_id
        self.quantity = quantity
        self.rank_value = rank_value
        self.shop_id = shop_id
        self.sku_alias = sku_alias
        # skuId
        self.sku_id = sku_id
        # sku
        self.sku_specs = sku_specs
        self.sku_specs_code = sku_specs_code
        self.sku_status = sku_status
        self.suggested_retail_price = suggested_retail_price
        self.title = title

    def validate(self):
        if self.sku_specs:
            for v1 in self.sku_specs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.barcode is not None:
            result['barcode'] = self.barcode

        if self.can_sell is not None:
            result['canSell'] = self.can_sell

        if self.discount_retail_price is not None:
            result['discountRetailPrice'] = self.discount_retail_price

        if self.division_code is not None:
            result['divisionCode'] = self.division_code

        if self.fuzzy_quantity is not None:
            result['fuzzyQuantity'] = self.fuzzy_quantity

        if self.mark_price is not None:
            result['markPrice'] = self.mark_price

        if self.pic_url is not None:
            result['picUrl'] = self.pic_url

        if self.platform_price is not None:
            result['platformPrice'] = self.platform_price

        if self.price is not None:
            result['price'] = self.price

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.quantity is not None:
            result['quantity'] = self.quantity

        if self.rank_value is not None:
            result['rankValue'] = self.rank_value

        if self.shop_id is not None:
            result['shopId'] = self.shop_id

        if self.sku_alias is not None:
            result['skuAlias'] = self.sku_alias

        if self.sku_id is not None:
            result['skuId'] = self.sku_id

        result['skuSpecs'] = []
        if self.sku_specs is not None:
            for k1 in self.sku_specs:
                result['skuSpecs'].append(k1.to_map() if k1 else None)

        if self.sku_specs_code is not None:
            result['skuSpecsCode'] = self.sku_specs_code

        if self.sku_status is not None:
            result['skuStatus'] = self.sku_status

        if self.suggested_retail_price is not None:
            result['suggestedRetailPrice'] = self.suggested_retail_price

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('barcode') is not None:
            self.barcode = m.get('barcode')

        if m.get('canSell') is not None:
            self.can_sell = m.get('canSell')

        if m.get('discountRetailPrice') is not None:
            self.discount_retail_price = m.get('discountRetailPrice')

        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')

        if m.get('fuzzyQuantity') is not None:
            self.fuzzy_quantity = m.get('fuzzyQuantity')

        if m.get('markPrice') is not None:
            self.mark_price = m.get('markPrice')

        if m.get('picUrl') is not None:
            self.pic_url = m.get('picUrl')

        if m.get('platformPrice') is not None:
            self.platform_price = m.get('platformPrice')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        if m.get('rankValue') is not None:
            self.rank_value = m.get('rankValue')

        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')

        if m.get('skuAlias') is not None:
            self.sku_alias = m.get('skuAlias')

        if m.get('skuId') is not None:
            self.sku_id = m.get('skuId')

        self.sku_specs = []
        if m.get('skuSpecs') is not None:
            for k1 in m.get('skuSpecs'):
                temp_model = main_models.SkuSpec()
                self.sku_specs.append(temp_model.from_map(k1))

        if m.get('skuSpecsCode') is not None:
            self.sku_specs_code = m.get('skuSpecsCode')

        if m.get('skuStatus') is not None:
            self.sku_status = m.get('skuStatus')

        if m.get('suggestedRetailPrice') is not None:
            self.suggested_retail_price = m.get('suggestedRetailPrice')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

