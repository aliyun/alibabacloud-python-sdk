# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteResourceCategoryRequest(DaraModel):
    def __init__(
        self,
        resource_category_id: str = None,
    ):
        # Resource category ID
        # 
        # This parameter is required.
        self.resource_category_id = resource_category_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_category_id is not None:
            result['ResourceCategoryId'] = self.resource_category_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCategoryId') is not None:
            self.resource_category_id = m.get('ResourceCategoryId')

        return self

