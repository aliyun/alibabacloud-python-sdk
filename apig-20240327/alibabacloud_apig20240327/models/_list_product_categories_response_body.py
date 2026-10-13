# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListProductCategoriesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListProductCategoriesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListProductCategoriesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListProductCategoriesResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.ListProductCategoriesResponseBodyDataContent] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of product categories. Each element in the list is named category and contains the information about a product category.
        self.content = content
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The total count.
        self.total_count = total_count

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['content'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k1 in m.get('content'):
                temp_model = main_models.ListProductCategoriesResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListProductCategoriesResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        description: str = None,
        icon: main_models.HiMarketIcon = None,
        name: str = None,
    ):
        # The product category ID. You can use this ID as the categoryId path parameter for GetProductCategory, UpdateProductCategory, and DeleteProductCategory. You can also use it as an element in the categories parameter, which is a set of category IDs, for SetProductCategories and CreateProduct.
        self.category_id = category_id
        # The product category description.
        self.description = description
        # The product category icon, which consists of the icon type (type) and icon information (value) fields.
        self.icon = icon
        # The product category name.
        self.name = name

    def validate(self):
        if self.icon:
            self.icon.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['categoryId'] = self.category_id

        if self.description is not None:
            result['description'] = self.description

        if self.icon is not None:
            result['icon'] = self.icon.to_map()

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('categoryId') is not None:
            self.category_id = m.get('categoryId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('icon') is not None:
            temp_model = main_models.HiMarketIcon()
            self.icon = temp_model.from_map(m.get('icon'))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

