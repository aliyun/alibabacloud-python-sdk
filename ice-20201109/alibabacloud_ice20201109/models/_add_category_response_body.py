# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class AddCategoryResponseBody(DaraModel):
    def __init__(
        self,
        category: main_models.AddCategoryResponseBodyCategory = None,
        request_id: str = None,
    ):
        # The information about the category.
        self.category = category
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.category:
            self.category.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            temp_model = main_models.AddCategoryResponseBodyCategory()
            self.category = temp_model.from_map(m.get('Category'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AddCategoryResponseBodyCategory(DaraModel):
    def __init__(
        self,
        cate_id: int = None,
        cate_name: str = None,
        level: int = None,
        parent_id: int = None,
        type: str = None,
    ):
        # The ID of the created category.
        self.cate_id = cate_id
        # The category name.
        self.cate_name = cate_name
        # The level of the category. A value of **0** indicates a level-1 category, a value of **1** indicates a level-2 category, and a value of **2** indicates a level-3 category.
        self.level = level
        # The ID of the parent category. By default, if ParentId is left empty or less than 1, -1 is returned, which indicates that the created category is the root directory.
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

