# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetCategoriesResponseBody(DaraModel):
    def __init__(
        self,
        category: main_models.GetCategoriesResponseBodyCategory = None,
        request_id: str = None,
        sub_categories: main_models.GetCategoriesResponseBodySubCategories = None,
        sub_total: int = None,
    ):
        # The information about the category.
        self.category = category
        # The request ID.
        self.request_id = request_id
        # The subcategories in the category.
        self.sub_categories = sub_categories
        # The total number of subcategories.
        self.sub_total = sub_total

    def validate(self):
        if self.category:
            self.category.validate()
        if self.sub_categories:
            self.sub_categories.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sub_categories is not None:
            result['SubCategories'] = self.sub_categories.to_map()

        if self.sub_total is not None:
            result['SubTotal'] = self.sub_total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            temp_model = main_models.GetCategoriesResponseBodyCategory()
            self.category = temp_model.from_map(m.get('Category'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SubCategories') is not None:
            temp_model = main_models.GetCategoriesResponseBodySubCategories()
            self.sub_categories = temp_model.from_map(m.get('SubCategories'))

        if m.get('SubTotal') is not None:
            self.sub_total = m.get('SubTotal')

        return self

class GetCategoriesResponseBodySubCategories(DaraModel):
    def __init__(
        self,
        category: List[main_models.GetCategoriesResponseBodySubCategoriesCategory] = None,
    ):
        self.category = category

    def validate(self):
        if self.category:
            for v1 in self.category:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Category'] = []
        if self.category is not None:
            for k1 in self.category:
                result['Category'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.category = []
        if m.get('Category') is not None:
            for k1 in m.get('Category'):
                temp_model = main_models.GetCategoriesResponseBodySubCategoriesCategory()
                self.category.append(temp_model.from_map(k1))

        return self

class GetCategoriesResponseBodySubCategoriesCategory(DaraModel):
    def __init__(
        self,
        cate_id: int = None,
        cate_name: str = None,
        level: int = None,
        parent_id: int = None,
        sub_total: int = None,
        type: str = None,
    ):
        # The category ID.
        self.cate_id = cate_id
        # The category name.
        # 
        # *   The value can be up to 64 bytes in length.
        # *   The value is encoded in UTF-8.
        self.cate_name = cate_name
        # The level of the category. A value of **0** indicates a level-1 category, a value of **1** indicates a level-2 category, and a value of **2** indicates a level-3 category.
        self.level = level
        # The ID of the parent category.
        self.parent_id = parent_id
        # The total number of subcategories.
        self.sub_total = sub_total
        # The type of the category. Valid values:
        # 
        # *   **default**: audio, video, and image files. This is the default value.
        # *   **material**: short video materials.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.cate_name is not None:
            result['CateName'] = self.cate_name

        if self.level is not None:
            result['Level'] = self.level

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.sub_total is not None:
            result['SubTotal'] = self.sub_total

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('SubTotal') is not None:
            self.sub_total = m.get('SubTotal')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetCategoriesResponseBodyCategory(DaraModel):
    def __init__(
        self,
        cate_id: int = None,
        cate_name: str = None,
        level: int = None,
        parent_id: int = None,
        type: str = None,
    ):
        # The category ID.
        self.cate_id = cate_id
        # The category name.
        self.cate_name = cate_name
        # The level of the category. A value of **0** indicates a level-1 category, a value of **1** indicates a level-2 category, and a value of **2** indicates a level-3 category.
        self.level = level
        # The ID of the parent category.
        self.parent_id = parent_id
        # The type of the category. Valid values:
        # 
        # *   **default**: audio, video, and image files. This is the default value.
        # *   **material**: short video materials.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.cate_name is not None:
            result['CateName'] = self.cate_name

        if self.level is not None:
            result['Level'] = self.level

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

