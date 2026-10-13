# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetProductCategoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetProductCategoryResponseBodyData = None,
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
            temp_model = main_models.GetProductCategoryResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetProductCategoryResponseBodyData(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        description: str = None,
        icon: main_models.HiMarketIcon = None,
        name: str = None,
    ):
        # The ID of the product category. This ID can be used as the categoryId path parameter for GetProductCategory, UpdateProductCategory, and DeleteProductCategory, or as an element in the categories array for SetProductCategories and CreateProduct.
        self.category_id = category_id
        # The description of the product category.
        self.description = description
        # The icon of the product category. It consists of two fields: icon type (type) and icon value (value).
        self.icon = icon
        # The name of the product category.
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

