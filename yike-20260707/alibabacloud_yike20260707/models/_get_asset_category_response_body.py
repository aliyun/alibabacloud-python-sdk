# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class GetAssetCategoryResponseBody(DaraModel):
    def __init__(
        self,
        category: main_models.GetAssetCategoryResponseBodyCategory = None,
        request_id: str = None,
        sub_categories: List[main_models.GetAssetCategoryResponseBodySubCategories] = None,
        sub_total: int = None,
    ):
        self.category = category
        self.request_id = request_id
        self.sub_categories = sub_categories
        self.sub_total = sub_total

    def validate(self):
        if self.category:
            self.category.validate()
        if self.sub_categories:
            for v1 in self.sub_categories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SubCategories'] = []
        if self.sub_categories is not None:
            for k1 in self.sub_categories:
                result['SubCategories'].append(k1.to_map() if k1 else None)

        if self.sub_total is not None:
            result['SubTotal'] = self.sub_total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            temp_model = main_models.GetAssetCategoryResponseBodyCategory()
            self.category = temp_model.from_map(m.get('Category'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sub_categories = []
        if m.get('SubCategories') is not None:
            for k1 in m.get('SubCategories'):
                temp_model = main_models.GetAssetCategoryResponseBodySubCategories()
                self.sub_categories.append(temp_model.from_map(k1))

        if m.get('SubTotal') is not None:
            self.sub_total = m.get('SubTotal')

        return self

class GetAssetCategoryResponseBodySubCategories(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        category_name: str = None,
        level: int = None,
        parent_id: int = None,
        sub_total: int = None,
    ):
        self.category_id = category_id
        self.category_name = category_name
        self.level = level
        self.parent_id = parent_id
        self.sub_total = sub_total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.level is not None:
            result['Level'] = self.level

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.sub_total is not None:
            result['SubTotal'] = self.sub_total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('SubTotal') is not None:
            self.sub_total = m.get('SubTotal')

        return self

class GetAssetCategoryResponseBodyCategory(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        category_name: str = None,
        level: int = None,
        parent_id: int = None,
    ):
        self.category_id = category_id
        self.category_name = category_name
        self.level = level
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.level is not None:
            result['Level'] = self.level

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        return self

