# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryUserListRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # The keyword to search for organization members by username or nickname.
        self.keyword = keyword
        # The page number to return.
        # 
        # - Starting value: 1
        # 
        # - Default value: 1
        self.page_num = page_num
        # The number of organization members to return per page.
        # 
        # - Default value: 10
        # 
        # - Maximum value: 1000
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

