# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListJobsShrinkRequest(DaraModel):
    def __init__(
        self,
        filter_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by_shrink: str = None,
    ):
        # Queries job filter conditions.
        self.filter_shrink = filter_shrink
        # The page number.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries on the current page. Default value: 50. Maximum value: 100.
        self.page_size = page_size
        # The sorting method.
        self.sort_by_shrink = sort_by_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by_shrink is not None:
            result['SortBy'] = self.sort_by_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by_shrink = m.get('SortBy')

        return self

