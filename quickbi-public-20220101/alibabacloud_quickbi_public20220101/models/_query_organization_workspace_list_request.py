# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryOrganizationWorkspaceListRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
        user_id: str = None,
    ):
        # The keyword for searching workspaces.
        self.keyword = keyword
        # The page number to return.
        # 
        # - Start value: 1
        # 
        # - Default value: 1
        self.page_num = page_num
        # The number of workspaces per page.
        # 
        # - Default value: 10
        # 
        # - Maximum value: 1000
        self.page_size = page_size
        # The user ID in Quick BI.
        self.user_id = user_id

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

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

