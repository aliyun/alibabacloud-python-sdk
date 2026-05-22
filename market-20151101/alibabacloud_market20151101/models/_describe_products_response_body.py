# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_market20151101 import models as main_models
from darabonba.model import DaraModel

class DescribeProductsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        product_items: main_models.DescribeProductsResponseBodyProductItems = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.product_items = product_items
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.product_items:
            self.product_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_items is not None:
            result['ProductItems'] = self.product_items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductItems') is not None:
            temp_model = main_models.DescribeProductsResponseBodyProductItems()
            self.product_items = temp_model.from_map(m.get('ProductItems'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeProductsResponseBodyProductItems(DaraModel):
    def __init__(
        self,
        product_item: List[main_models.DescribeProductsResponseBodyProductItemsProductItem] = None,
    ):
        self.product_item = product_item

    def validate(self):
        if self.product_item:
            for v1 in self.product_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ProductItem'] = []
        if self.product_item is not None:
            for k1 in self.product_item:
                result['ProductItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product_item = []
        if m.get('ProductItem') is not None:
            for k1 in m.get('ProductItem'):
                temp_model = main_models.DescribeProductsResponseBodyProductItemsProductItem()
                self.product_item.append(temp_model.from_map(k1))

        return self

class DescribeProductsResponseBodyProductItemsProductItem(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        code: str = None,
        delivery_date: str = None,
        delivery_way: str = None,
        image_url: str = None,
        name: str = None,
        operation_system: str = None,
        price_info: str = None,
        score: str = None,
        short_description: str = None,
        suggested_price: str = None,
        supplier_id: int = None,
        supplier_name: str = None,
        tags: str = None,
        target_url: str = None,
        warranty_date: str = None,
    ):
        self.category_id = category_id
        self.code = code
        self.delivery_date = delivery_date
        self.delivery_way = delivery_way
        self.image_url = image_url
        self.name = name
        self.operation_system = operation_system
        self.price_info = price_info
        self.score = score
        self.short_description = short_description
        self.suggested_price = suggested_price
        self.supplier_id = supplier_id
        self.supplier_name = supplier_name
        self.tags = tags
        self.target_url = target_url
        self.warranty_date = warranty_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.code is not None:
            result['Code'] = self.code

        if self.delivery_date is not None:
            result['DeliveryDate'] = self.delivery_date

        if self.delivery_way is not None:
            result['DeliveryWay'] = self.delivery_way

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.name is not None:
            result['Name'] = self.name

        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system

        if self.price_info is not None:
            result['PriceInfo'] = self.price_info

        if self.score is not None:
            result['Score'] = self.score

        if self.short_description is not None:
            result['ShortDescription'] = self.short_description

        if self.suggested_price is not None:
            result['SuggestedPrice'] = self.suggested_price

        if self.supplier_id is not None:
            result['SupplierId'] = self.supplier_id

        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.target_url is not None:
            result['TargetUrl'] = self.target_url

        if self.warranty_date is not None:
            result['WarrantyDate'] = self.warranty_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DeliveryDate') is not None:
            self.delivery_date = m.get('DeliveryDate')

        if m.get('DeliveryWay') is not None:
            self.delivery_way = m.get('DeliveryWay')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')

        if m.get('PriceInfo') is not None:
            self.price_info = m.get('PriceInfo')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')

        if m.get('SuggestedPrice') is not None:
            self.suggested_price = m.get('SuggestedPrice')

        if m.get('SupplierId') is not None:
            self.supplier_id = m.get('SupplierId')

        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')

        if m.get('WarrantyDate') is not None:
            self.warranty_date = m.get('WarrantyDate')

        return self

