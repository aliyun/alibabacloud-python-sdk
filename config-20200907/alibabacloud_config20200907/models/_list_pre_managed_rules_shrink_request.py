# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPreManagedRulesShrinkRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        resource_types_shrink: str = None,
    ):
        # The page number.
        # 
        # The value starts from 1. The default value is 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # The default value is 10.
        self.page_size = page_size
        # A list of resource types.
        self.resource_types_shrink = resource_types_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_types_shrink is not None:
            result['ResourceTypes'] = self.resource_types_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceTypes') is not None:
            self.resource_types_shrink = m.get('ResourceTypes')

        return self

