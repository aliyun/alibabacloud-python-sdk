# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateResourceCategoryRequest(DaraModel):
    def __init__(
        self,
        resource_category_id: str = None,
        resource_category_name: str = None,
        resource_matcher: str = None,
    ):
        # Resource category ID.
        # 
        # This parameter is required.
        self.resource_category_id = resource_category_id
        # Resource category name.
        self.resource_category_name = resource_category_name
        # Resource matcher.
        self.resource_matcher = resource_matcher

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_category_id is not None:
            result['ResourceCategoryId'] = self.resource_category_id

        if self.resource_category_name is not None:
            result['ResourceCategoryName'] = self.resource_category_name

        if self.resource_matcher is not None:
            result['ResourceMatcher'] = self.resource_matcher

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCategoryId') is not None:
            self.resource_category_id = m.get('ResourceCategoryId')

        if m.get('ResourceCategoryName') is not None:
            self.resource_category_name = m.get('ResourceCategoryName')

        if m.get('ResourceMatcher') is not None:
            self.resource_matcher = m.get('ResourceMatcher')

        return self

