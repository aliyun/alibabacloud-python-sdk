# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListSupportedProductsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        products: List[main_models.ListSupportedProductsResponseBodyProducts] = None,
        request_id: str = None,
    ):
        # The maximum number of entries to return for a single request. Valid values: 1 to 500.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The cloud services that are supported by Cloud Config.
        self.products = products
        # The request ID.
        self.request_id = request_id

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
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Products'] = []
        if self.products is not None:
            for k1 in self.products:
                result['Products'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.products = []
        if m.get('Products') is not None:
            for k1 in m.get('Products'):
                temp_model = main_models.ListSupportedProductsResponseBodyProducts()
                self.products.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSupportedProductsResponseBodyProducts(DaraModel):
    def __init__(
        self,
        product_name_en: str = None,
        product_name_zh: str = None,
        resource_type_list: List[main_models.ListSupportedProductsResponseBodyProductsResourceTypeList] = None,
    ):
        # The English name of the Alibaba Cloud service.
        self.product_name_en = product_name_en
        # The Chinese name of the Alibaba Cloud service.
        self.product_name_zh = product_name_zh
        # The resource types that are supported by Cloud Config.
        self.resource_type_list = resource_type_list

    def validate(self):
        if self.resource_type_list:
            for v1 in self.resource_type_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_name_en is not None:
            result['ProductNameEn'] = self.product_name_en

        if self.product_name_zh is not None:
            result['ProductNameZh'] = self.product_name_zh

        result['ResourceTypeList'] = []
        if self.resource_type_list is not None:
            for k1 in self.resource_type_list:
                result['ResourceTypeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductNameEn') is not None:
            self.product_name_en = m.get('ProductNameEn')

        if m.get('ProductNameZh') is not None:
            self.product_name_zh = m.get('ProductNameZh')

        self.resource_type_list = []
        if m.get('ResourceTypeList') is not None:
            for k1 in m.get('ResourceTypeList'):
                temp_model = main_models.ListSupportedProductsResponseBodyProductsResourceTypeList()
                self.resource_type_list.append(temp_model.from_map(k1))

        return self

class ListSupportedProductsResponseBodyProductsResourceTypeList(DaraModel):
    def __init__(
        self,
        resource_type: str = None,
        type_name_en: str = None,
        type_name_zh: str = None,
        type_page_link: str = None,
    ):
        # The identifier of the resource type.
        self.resource_type = resource_type
        # The English name of the resource type.
        self.type_name_en = type_name_en
        # The Chinese name of the resource type.
        self.type_name_zh = type_name_zh
        # The URL of the resource type in the console.
        self.type_page_link = type_page_link

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.type_name_en is not None:
            result['TypeNameEn'] = self.type_name_en

        if self.type_name_zh is not None:
            result['TypeNameZh'] = self.type_name_zh

        if self.type_page_link is not None:
            result['TypePageLink'] = self.type_page_link

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TypeNameEn') is not None:
            self.type_name_en = m.get('TypeNameEn')

        if m.get('TypeNameZh') is not None:
            self.type_name_zh = m.get('TypeNameZh')

        if m.get('TypePageLink') is not None:
            self.type_page_link = m.get('TypePageLink')

        return self

