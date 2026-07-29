# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class ListAssetCategoriesResponseBody(DaraModel):
    def __init__(
        self,
        categories: List[main_models.ListAssetCategoriesResponseBodyCategories] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.categories = categories
        self.request_id = request_id
        self.total = total

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

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.categories = []
        if m.get('Categories') is not None:
            for k1 in m.get('Categories'):
                temp_model = main_models.ListAssetCategoriesResponseBodyCategories()
                self.categories.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListAssetCategoriesResponseBodyCategories(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        category_name: str = None,
        level: str = None,
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

