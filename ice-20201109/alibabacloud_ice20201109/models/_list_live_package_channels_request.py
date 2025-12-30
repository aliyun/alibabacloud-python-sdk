# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLivePackageChannelsRequest(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        keyword: str = None,
        page_no: int = None,
        page_size: int = None,
        sort_by: str = None,
    ):
        # The channel group name.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The channel name or description. Fuzzy match is supported.
        self.keyword = keyword
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The sort order by creation time. Default value: desc.
        # 
        # Valid values:
        # 
        # *   asc
        # *   desc
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

