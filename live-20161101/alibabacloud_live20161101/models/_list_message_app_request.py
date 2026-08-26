# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMessageAppRequest(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        sort_type: int = None,
    ):
        # Page number. Default value: 1. Valid values: 1 to 100000.
        # 
        # > This page number is the current display page.
        # 
        # This parameter is required.
        self.page_num = page_num
        # Number of applications displayed per page. Default value: 20. Valid values: 1 to 50.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Sorting method. Valid values:
        # 
        # - 0: Ascending order by time.
        # - 1: Descending order by time.
        self.sort_type = sort_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        return self

