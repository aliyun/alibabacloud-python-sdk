# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class ListProductsResponseBody(DaraModel):
    def __init__(
        self,
        products: List[main_models.ListProductsResponseBodyProducts] = None,
        request_id: str = None,
        services: List[main_models.ListProductsResponseBodyServices] = None,
    ):
        self.products = products
        self.request_id = request_id
        self.services = services

    def validate(self):
        if self.products:
            for v1 in self.products:
                 if v1:
                    v1.validate()
        if self.services:
            for v1 in self.services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Products'] = []
        if self.products is not None:
            for k1 in self.products:
                result['Products'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Services'] = []
        if self.services is not None:
            for k1 in self.services:
                result['Services'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.products = []
        if m.get('Products') is not None:
            for k1 in m.get('Products'):
                temp_model = main_models.ListProductsResponseBodyProducts()
                self.products.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.services = []
        if m.get('Services') is not None:
            for k1 in m.get('Services'):
                temp_model = main_models.ListProductsResponseBodyServices()
                self.services.append(temp_model.from_map(k1))

        return self

class ListProductsResponseBodyServices(DaraModel):
    def __init__(
        self,
        is_open: bool = None,
        open_url: str = None,
        service_code: str = None,
    ):
        self.is_open = is_open
        self.open_url = open_url
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_open is not None:
            result['IsOpen'] = self.is_open

        if self.open_url is not None:
            result['OpenUrl'] = self.open_url

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsOpen') is not None:
            self.is_open = m.get('IsOpen')

        if m.get('OpenUrl') is not None:
            self.open_url = m.get('OpenUrl')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        return self

class ListProductsResponseBodyProducts(DaraModel):
    def __init__(
        self,
        has_permission_to_purchase: bool = None,
        is_purchased: bool = None,
        product_code: str = None,
        product_id: str = None,
        purchase_url: str = None,
    ):
        self.has_permission_to_purchase = has_permission_to_purchase
        self.is_purchased = is_purchased
        self.product_code = product_code
        self.product_id = product_id
        self.purchase_url = purchase_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_permission_to_purchase is not None:
            result['HasPermissionToPurchase'] = self.has_permission_to_purchase

        if self.is_purchased is not None:
            result['IsPurchased'] = self.is_purchased

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.purchase_url is not None:
            result['PurchaseUrl'] = self.purchase_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasPermissionToPurchase') is not None:
            self.has_permission_to_purchase = m.get('HasPermissionToPurchase')

        if m.get('IsPurchased') is not None:
            self.is_purchased = m.get('IsPurchased')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('PurchaseUrl') is not None:
            self.purchase_url = m.get('PurchaseUrl')

        return self

