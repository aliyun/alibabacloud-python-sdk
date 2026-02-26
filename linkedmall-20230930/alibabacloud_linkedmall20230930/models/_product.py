# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class Product(DaraModel):
    def __init__(
        self,
        brand_name: str = None,
        can_sell: bool = None,
        category_chain: List[main_models.Category] = None,
        category_leaf_id: int = None,
        desc_path: str = None,
        division_code: str = None,
        extend_properties: List[main_models.ProductExtendProperty] = None,
        fuzzy_quantity: str = None,
        images: List[str] = None,
        in_group: bool = None,
        limit_rules: List[main_models.LimitRule] = None,
        lm_item_id: str = None,
        pic_url: str = None,
        product_id: str = None,
        product_specs: List[main_models.ProductSpec] = None,
        product_status: str = None,
        product_type: str = None,
        properties: List[main_models.ProductProperty] = None,
        quantity: int = None,
        request_id: str = None,
        service_promises: List[str] = None,
        shop_id: str = None,
        skus: List[main_models.Sku] = None,
        sold_quantity: str = None,
        tax_code: str = None,
        tax_rate: int = None,
        title: str = None,
    ):
        self.brand_name = brand_name
        self.can_sell = can_sell
        self.category_chain = category_chain
        self.category_leaf_id = category_leaf_id
        self.desc_path = desc_path
        self.division_code = division_code
        self.extend_properties = extend_properties
        self.fuzzy_quantity = fuzzy_quantity
        # images
        self.images = images
        self.in_group = in_group
        self.limit_rules = limit_rules
        self.lm_item_id = lm_item_id
        self.pic_url = pic_url
        self.product_id = product_id
        # productSpecs
        self.product_specs = product_specs
        self.product_status = product_status
        self.product_type = product_type
        self.properties = properties
        self.quantity = quantity
        self.request_id = request_id
        self.service_promises = service_promises
        self.shop_id = shop_id
        # skus
        self.skus = skus
        self.sold_quantity = sold_quantity
        self.tax_code = tax_code
        self.tax_rate = tax_rate
        self.title = title

    def validate(self):
        if self.category_chain:
            for v1 in self.category_chain:
                 if v1:
                    v1.validate()
        if self.extend_properties:
            for v1 in self.extend_properties:
                 if v1:
                    v1.validate()
        if self.limit_rules:
            for v1 in self.limit_rules:
                 if v1:
                    v1.validate()
        if self.product_specs:
            for v1 in self.product_specs:
                 if v1:
                    v1.validate()
        if self.properties:
            for v1 in self.properties:
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
        if self.brand_name is not None:
            result['brandName'] = self.brand_name

        if self.can_sell is not None:
            result['canSell'] = self.can_sell

        result['categoryChain'] = []
        if self.category_chain is not None:
            for k1 in self.category_chain:
                result['categoryChain'].append(k1.to_map() if k1 else None)

        if self.category_leaf_id is not None:
            result['categoryLeafId'] = self.category_leaf_id

        if self.desc_path is not None:
            result['descPath'] = self.desc_path

        if self.division_code is not None:
            result['divisionCode'] = self.division_code

        result['extendProperties'] = []
        if self.extend_properties is not None:
            for k1 in self.extend_properties:
                result['extendProperties'].append(k1.to_map() if k1 else None)

        if self.fuzzy_quantity is not None:
            result['fuzzyQuantity'] = self.fuzzy_quantity

        if self.images is not None:
            result['images'] = self.images

        if self.in_group is not None:
            result['inGroup'] = self.in_group

        result['limitRules'] = []
        if self.limit_rules is not None:
            for k1 in self.limit_rules:
                result['limitRules'].append(k1.to_map() if k1 else None)

        if self.lm_item_id is not None:
            result['lmItemId'] = self.lm_item_id

        if self.pic_url is not None:
            result['picUrl'] = self.pic_url

        if self.product_id is not None:
            result['productId'] = self.product_id

        result['productSpecs'] = []
        if self.product_specs is not None:
            for k1 in self.product_specs:
                result['productSpecs'].append(k1.to_map() if k1 else None)

        if self.product_status is not None:
            result['productStatus'] = self.product_status

        if self.product_type is not None:
            result['productType'] = self.product_type

        result['properties'] = []
        if self.properties is not None:
            for k1 in self.properties:
                result['properties'].append(k1.to_map() if k1 else None)

        if self.quantity is not None:
            result['quantity'] = self.quantity

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.service_promises is not None:
            result['servicePromises'] = self.service_promises

        if self.shop_id is not None:
            result['shopId'] = self.shop_id

        result['skus'] = []
        if self.skus is not None:
            for k1 in self.skus:
                result['skus'].append(k1.to_map() if k1 else None)

        if self.sold_quantity is not None:
            result['soldQuantity'] = self.sold_quantity

        if self.tax_code is not None:
            result['taxCode'] = self.tax_code

        if self.tax_rate is not None:
            result['taxRate'] = self.tax_rate

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('brandName') is not None:
            self.brand_name = m.get('brandName')

        if m.get('canSell') is not None:
            self.can_sell = m.get('canSell')

        self.category_chain = []
        if m.get('categoryChain') is not None:
            for k1 in m.get('categoryChain'):
                temp_model = main_models.Category()
                self.category_chain.append(temp_model.from_map(k1))

        if m.get('categoryLeafId') is not None:
            self.category_leaf_id = m.get('categoryLeafId')

        if m.get('descPath') is not None:
            self.desc_path = m.get('descPath')

        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')

        self.extend_properties = []
        if m.get('extendProperties') is not None:
            for k1 in m.get('extendProperties'):
                temp_model = main_models.ProductExtendProperty()
                self.extend_properties.append(temp_model.from_map(k1))

        if m.get('fuzzyQuantity') is not None:
            self.fuzzy_quantity = m.get('fuzzyQuantity')

        if m.get('images') is not None:
            self.images = m.get('images')

        if m.get('inGroup') is not None:
            self.in_group = m.get('inGroup')

        self.limit_rules = []
        if m.get('limitRules') is not None:
            for k1 in m.get('limitRules'):
                temp_model = main_models.LimitRule()
                self.limit_rules.append(temp_model.from_map(k1))

        if m.get('lmItemId') is not None:
            self.lm_item_id = m.get('lmItemId')

        if m.get('picUrl') is not None:
            self.pic_url = m.get('picUrl')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        self.product_specs = []
        if m.get('productSpecs') is not None:
            for k1 in m.get('productSpecs'):
                temp_model = main_models.ProductSpec()
                self.product_specs.append(temp_model.from_map(k1))

        if m.get('productStatus') is not None:
            self.product_status = m.get('productStatus')

        if m.get('productType') is not None:
            self.product_type = m.get('productType')

        self.properties = []
        if m.get('properties') is not None:
            for k1 in m.get('properties'):
                temp_model = main_models.ProductProperty()
                self.properties.append(temp_model.from_map(k1))

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('servicePromises') is not None:
            self.service_promises = m.get('servicePromises')

        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')

        self.skus = []
        if m.get('skus') is not None:
            for k1 in m.get('skus'):
                temp_model = main_models.Sku()
                self.skus.append(temp_model.from_map(k1))

        if m.get('soldQuantity') is not None:
            self.sold_quantity = m.get('soldQuantity')

        if m.get('taxCode') is not None:
            self.tax_code = m.get('taxCode')

        if m.get('taxRate') is not None:
            self.tax_rate = m.get('taxRate')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

