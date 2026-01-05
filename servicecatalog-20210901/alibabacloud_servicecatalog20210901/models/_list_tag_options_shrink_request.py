# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTagOptionsShrinkRequest(DaraModel):
    def __init__(
        self,
        filters_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_order: str = None,
    ):
        # The filter condition.
        self.filters_shrink = filters_shrink
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Minimum value: 1. Default value: 10.
        self.page_size = page_size
        # The information based on which you want to sort the query results.
        # 
        # Set the value to CreateTime, which specifies the creation time of tag options.
        self.sort_by = sort_by
        # The order in which you want to sort the query results. Valid values:
        # 
        # *   Asc: the ascending order
        # *   Desc (default): the descending order
        self.sort_order = sort_order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filters_shrink is not None:
            result['Filters'] = self.filters_shrink

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filters') is not None:
            self.filters_shrink = m.get('Filters')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        return self

