# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class CreateAssetCategoryResponseBody(DaraModel):
    def __init__(
        self,
        category: main_models.CreateAssetCategoryResponseBodyCategory = None,
        request_id: str = None,
    ):
        # The media asset category information.
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
            temp_model = main_models.CreateAssetCategoryResponseBodyCategory()
            self.category = temp_model.from_map(m.get('Category'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateAssetCategoryResponseBodyCategory(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        category_name: str = None,
        level: int = None,
        parent_id: int = None,
    ):
        # The ID of the created category.
        self.category_id = category_id
        # The media asset category information.
        self.category_name = category_name
        # The category level. The first-level category has a level of 0, the second-level category has a level of 1, and the third-level category has a level of 2.
        self.level = level
        # The parent category ID. If the ParentId parameter is set to empty or a value less than 1, the default return value is -1, which indicates that the created category is a root directory.
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

