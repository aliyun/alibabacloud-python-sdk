# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_openapiexplorer20241130 import models as main_models
from darabonba.model import DaraModel

class ListProductsResponseBody(DaraModel):
    def __init__(
        self,
        products: List[main_models.ListProductsResponseBodyProducts] = None,
        request_id: str = None,
    ):
        self.products = products
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
        result['products'] = []
        if self.products is not None:
            for k1 in self.products:
                result['products'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.products = []
        if m.get('products') is not None:
            for k1 in m.get('products'):
                temp_model = main_models.ListProductsResponseBodyProducts()
                self.products.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListProductsResponseBodyProducts(DaraModel):
    def __init__(
        self,
        category_2name: str = None,
        category_name: str = None,
        code: str = None,
        default_version: str = None,
        description: str = None,
        group: str = None,
        name: str = None,
        short_name: str = None,
        style: str = None,
        versions: List[str] = None,
    ):
        self.category_2name = category_2name
        self.category_name = category_name
        self.code = code
        self.default_version = default_version
        self.description = description
        self.group = group
        self.name = name
        self.short_name = short_name
        self.style = style
        self.versions = versions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_2name is not None:
            result['category2Name'] = self.category_2name

        if self.category_name is not None:
            result['categoryName'] = self.category_name

        if self.code is not None:
            result['code'] = self.code

        if self.default_version is not None:
            result['defaultVersion'] = self.default_version

        if self.description is not None:
            result['description'] = self.description

        if self.group is not None:
            result['group'] = self.group

        if self.name is not None:
            result['name'] = self.name

        if self.short_name is not None:
            result['shortName'] = self.short_name

        if self.style is not None:
            result['style'] = self.style

        if self.versions is not None:
            result['versions'] = self.versions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category2Name') is not None:
            self.category_2name = m.get('category2Name')

        if m.get('categoryName') is not None:
            self.category_name = m.get('categoryName')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('defaultVersion') is not None:
            self.default_version = m.get('defaultVersion')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('group') is not None:
            self.group = m.get('group')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('shortName') is not None:
            self.short_name = m.get('shortName')

        if m.get('style') is not None:
            self.style = m.get('style')

        if m.get('versions') is not None:
            self.versions = m.get('versions')

        return self

