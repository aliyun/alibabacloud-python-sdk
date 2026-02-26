# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class SearchProductsResponseBody(DaraModel):
    def __init__(
        self,
        products: List[main_models.SearchProductsResponseBodyProducts] = None,
        total: int = None,
    ):
        self.products = products
        self.total = total

    def validate(self):
        if self.products:
            for v1 in self.products:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['products'] = []
        if self.products is not None:
            for k1 in self.products:
                result['products'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.products = []
        if m.get('products') is not None:
            for k1 in m.get('products'):
                temp_model = main_models.SearchProductsResponseBodyProducts()
                self.products.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class SearchProductsResponseBodyProducts(DaraModel):
    def __init__(
        self,
        band_name: str = None,
        can_not_sell_reason: str = None,
        can_sell: bool = None,
        category_chain: List[main_models.SearchProductsResponseBodyProductsCategoryChain] = None,
        credit: List[str] = None,
        diff_price: str = None,
        distribution_price: str = None,
        distribution_price_ratio: str = None,
        external_platform_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        in_group: bool = None,
        in_group_time: str = None,
        inventory_risk_level: str = None,
        invoice_type: str = None,
        lm_item_id: str = None,
        pic_url: str = None,
        platform_price: str = None,
        platform_reserve_price: str = None,
        product_id: str = None,
        product_name: str = None,
        shop_name: str = None,
        sold_quantity: str = None,
        tax_code: str = None,
        tax_rate: int = None,
        trade_mode: str = None,
    ):
        self.band_name = band_name
        self.can_not_sell_reason = can_not_sell_reason
        self.can_sell = can_sell
        self.category_chain = category_chain
        self.credit = credit
        self.diff_price = diff_price
        self.distribution_price = distribution_price
        self.distribution_price_ratio = distribution_price_ratio
        self.external_platform_type = external_platform_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.in_group = in_group
        self.in_group_time = in_group_time
        self.inventory_risk_level = inventory_risk_level
        self.invoice_type = invoice_type
        self.lm_item_id = lm_item_id
        self.pic_url = pic_url
        self.platform_price = platform_price
        self.platform_reserve_price = platform_reserve_price
        self.product_id = product_id
        self.product_name = product_name
        self.shop_name = shop_name
        self.sold_quantity = sold_quantity
        self.tax_code = tax_code
        self.tax_rate = tax_rate
        self.trade_mode = trade_mode

    def validate(self):
        if self.category_chain:
            for v1 in self.category_chain:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.band_name is not None:
            result['bandName'] = self.band_name

        if self.can_not_sell_reason is not None:
            result['canNotSellReason'] = self.can_not_sell_reason

        if self.can_sell is not None:
            result['canSell'] = self.can_sell

        result['categoryChain'] = []
        if self.category_chain is not None:
            for k1 in self.category_chain:
                result['categoryChain'].append(k1.to_map() if k1 else None)

        if self.credit is not None:
            result['credit'] = self.credit

        if self.diff_price is not None:
            result['diffPrice'] = self.diff_price

        if self.distribution_price is not None:
            result['distributionPrice'] = self.distribution_price

        if self.distribution_price_ratio is not None:
            result['distributionPriceRatio'] = self.distribution_price_ratio

        if self.external_platform_type is not None:
            result['externalPlatformType'] = self.external_platform_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.in_group is not None:
            result['inGroup'] = self.in_group

        if self.in_group_time is not None:
            result['inGroupTime'] = self.in_group_time

        if self.inventory_risk_level is not None:
            result['inventoryRiskLevel'] = self.inventory_risk_level

        if self.invoice_type is not None:
            result['invoiceType'] = self.invoice_type

        if self.lm_item_id is not None:
            result['lmItemId'] = self.lm_item_id

        if self.pic_url is not None:
            result['picUrl'] = self.pic_url

        if self.platform_price is not None:
            result['platformPrice'] = self.platform_price

        if self.platform_reserve_price is not None:
            result['platformReservePrice'] = self.platform_reserve_price

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.product_name is not None:
            result['productName'] = self.product_name

        if self.shop_name is not None:
            result['shopName'] = self.shop_name

        if self.sold_quantity is not None:
            result['soldQuantity'] = self.sold_quantity

        if self.tax_code is not None:
            result['taxCode'] = self.tax_code

        if self.tax_rate is not None:
            result['taxRate'] = self.tax_rate

        if self.trade_mode is not None:
            result['tradeMode'] = self.trade_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bandName') is not None:
            self.band_name = m.get('bandName')

        if m.get('canNotSellReason') is not None:
            self.can_not_sell_reason = m.get('canNotSellReason')

        if m.get('canSell') is not None:
            self.can_sell = m.get('canSell')

        self.category_chain = []
        if m.get('categoryChain') is not None:
            for k1 in m.get('categoryChain'):
                temp_model = main_models.SearchProductsResponseBodyProductsCategoryChain()
                self.category_chain.append(temp_model.from_map(k1))

        if m.get('credit') is not None:
            self.credit = m.get('credit')

        if m.get('diffPrice') is not None:
            self.diff_price = m.get('diffPrice')

        if m.get('distributionPrice') is not None:
            self.distribution_price = m.get('distributionPrice')

        if m.get('distributionPriceRatio') is not None:
            self.distribution_price_ratio = m.get('distributionPriceRatio')

        if m.get('externalPlatformType') is not None:
            self.external_platform_type = m.get('externalPlatformType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('inGroup') is not None:
            self.in_group = m.get('inGroup')

        if m.get('inGroupTime') is not None:
            self.in_group_time = m.get('inGroupTime')

        if m.get('inventoryRiskLevel') is not None:
            self.inventory_risk_level = m.get('inventoryRiskLevel')

        if m.get('invoiceType') is not None:
            self.invoice_type = m.get('invoiceType')

        if m.get('lmItemId') is not None:
            self.lm_item_id = m.get('lmItemId')

        if m.get('picUrl') is not None:
            self.pic_url = m.get('picUrl')

        if m.get('platformPrice') is not None:
            self.platform_price = m.get('platformPrice')

        if m.get('platformReservePrice') is not None:
            self.platform_reserve_price = m.get('platformReservePrice')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('productName') is not None:
            self.product_name = m.get('productName')

        if m.get('shopName') is not None:
            self.shop_name = m.get('shopName')

        if m.get('soldQuantity') is not None:
            self.sold_quantity = m.get('soldQuantity')

        if m.get('taxCode') is not None:
            self.tax_code = m.get('taxCode')

        if m.get('taxRate') is not None:
            self.tax_rate = m.get('taxRate')

        if m.get('tradeMode') is not None:
            self.trade_mode = m.get('tradeMode')

        return self

class SearchProductsResponseBodyProductsCategoryChain(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        is_leaf: bool = None,
        level: int = None,
        name: str = None,
        parent_id: int = None,
    ):
        self.category_id = category_id
        self.is_leaf = is_leaf
        self.level = level
        self.name = name
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['categoryId'] = self.category_id

        if self.is_leaf is not None:
            result['isLeaf'] = self.is_leaf

        if self.level is not None:
            result['level'] = self.level

        if self.name is not None:
            result['name'] = self.name

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('categoryId') is not None:
            self.category_id = m.get('categoryId')

        if m.get('isLeaf') is not None:
            self.is_leaf = m.get('isLeaf')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        return self

