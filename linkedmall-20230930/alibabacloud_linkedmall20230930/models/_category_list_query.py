# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CategoryListQuery(DaraModel):
    def __init__(
        self,
        category_ids: List[int] = None,
        parent_category_id: int = None,
    ):
        self.category_ids = category_ids
        self.parent_category_id = parent_category_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_ids is not None:
            result['categoryIds'] = self.category_ids

        if self.parent_category_id is not None:
            result['parentCategoryId'] = self.parent_category_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('categoryIds') is not None:
            self.category_ids = m.get('categoryIds')

        if m.get('parentCategoryId') is not None:
            self.parent_category_id = m.get('parentCategoryId')

        return self

