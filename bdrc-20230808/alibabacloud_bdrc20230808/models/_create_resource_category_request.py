# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateResourceCategoryRequest(DaraModel):
    def __init__(
        self,
        resource_category_name: str = None,
        resource_matcher: str = None,
        resource_type: str = None,
    ):
        # The resource category name.
        # 
        # This parameter is required.
        self.resource_category_name = resource_category_name
        # The resource matcher.
        # 
        # This parameter is required.
        self.resource_matcher = resource_matcher
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_category_name is not None:
            result['ResourceCategoryName'] = self.resource_category_name

        if self.resource_matcher is not None:
            result['ResourceMatcher'] = self.resource_matcher

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCategoryName') is not None:
            self.resource_category_name = m.get('ResourceCategoryName')

        if m.get('ResourceMatcher') is not None:
            self.resource_matcher = m.get('ResourceMatcher')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

