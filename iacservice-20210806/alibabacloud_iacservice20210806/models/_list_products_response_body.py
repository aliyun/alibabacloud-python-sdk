# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListProductsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        products: List[main_models.ListProductsResponseBodyProducts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.products = products
        self.request_id = request_id
        self.total_count = total_count

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
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['products'] = []
        if self.products is not None:
            for k1 in self.products:
                result['products'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.products = []
        if m.get('products') is not None:
            for k1 in m.get('products'):
                temp_model = main_models.ListProductsResponseBodyProducts()
                self.products.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListProductsResponseBodyProducts(DaraModel):
    def __init__(
        self,
        first_category_name: str = None,
        first_category_name_en: str = None,
        product: str = None,
        product_name: str = None,
        product_name_en: str = None,
        second_category_name: str = None,
        second_category_name_en: str = None,
        status: str = None,
        subcategory: str = None,
        support_terraformer: bool = None,
        terraform_provider_version: str = None,
    ):
        self.first_category_name = first_category_name
        self.first_category_name_en = first_category_name_en
        self.product = product
        self.product_name = product_name
        self.product_name_en = product_name_en
        self.second_category_name = second_category_name
        self.second_category_name_en = second_category_name_en
        self.status = status
        self.subcategory = subcategory
        self.support_terraformer = support_terraformer
        self.terraform_provider_version = terraform_provider_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.first_category_name is not None:
            result['firstCategoryName'] = self.first_category_name

        if self.first_category_name_en is not None:
            result['firstCategoryNameEn'] = self.first_category_name_en

        if self.product is not None:
            result['product'] = self.product

        if self.product_name is not None:
            result['productName'] = self.product_name

        if self.product_name_en is not None:
            result['productNameEn'] = self.product_name_en

        if self.second_category_name is not None:
            result['secondCategoryName'] = self.second_category_name

        if self.second_category_name_en is not None:
            result['secondCategoryNameEn'] = self.second_category_name_en

        if self.status is not None:
            result['status'] = self.status

        if self.subcategory is not None:
            result['subcategory'] = self.subcategory

        if self.support_terraformer is not None:
            result['supportTerraformer'] = self.support_terraformer

        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('firstCategoryName') is not None:
            self.first_category_name = m.get('firstCategoryName')

        if m.get('firstCategoryNameEn') is not None:
            self.first_category_name_en = m.get('firstCategoryNameEn')

        if m.get('product') is not None:
            self.product = m.get('product')

        if m.get('productName') is not None:
            self.product_name = m.get('productName')

        if m.get('productNameEn') is not None:
            self.product_name_en = m.get('productNameEn')

        if m.get('secondCategoryName') is not None:
            self.second_category_name = m.get('secondCategoryName')

        if m.get('secondCategoryNameEn') is not None:
            self.second_category_name_en = m.get('secondCategoryNameEn')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('subcategory') is not None:
            self.subcategory = m.get('subcategory')

        if m.get('supportTerraformer') is not None:
            self.support_terraformer = m.get('supportTerraformer')

        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')

        return self

