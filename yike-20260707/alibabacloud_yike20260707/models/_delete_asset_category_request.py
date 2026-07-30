# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAssetCategoryRequest(DaraModel):
    def __init__(
        self,
        category_id: int = None,
    ):
        # The category ID. You can obtain the value by using one of the following methods:
        # 
        # - When you create a category by calling the CreateAssetCategory operation, the category ID is the value of CategoryId in the response.
        # - When you query categories by calling the ListAssetCategories operation, the category ID is the value of CategoryId in the corresponding entry in the response.
        # 
        # This parameter is required.
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        return self

