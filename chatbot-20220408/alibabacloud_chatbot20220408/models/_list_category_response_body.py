# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class ListCategoryResponseBody(DaraModel):
    def __init__(
        self,
        categories: List[main_models.ListCategoryResponseBodyCategories] = None,
        request_id: str = None,
    ):
        self.categories = categories
        self.request_id = request_id

    def validate(self):
        if self.categories:
            for v1 in self.categories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Categories'] = []
        if self.categories is not None:
            for k1 in self.categories:
                result['Categories'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.categories = []
        if m.get('Categories') is not None:
            for k1 in m.get('Categories'):
                temp_model = main_models.ListCategoryResponseBodyCategories()
                self.categories.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCategoryResponseBodyCategories(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        category_id: int = None,
        name: str = None,
        parent_category_id: int = None,
        status: int = None,
    ):
        self.biz_code = biz_code
        self.category_id = category_id
        self.name = name
        self.parent_category_id = parent_category_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

