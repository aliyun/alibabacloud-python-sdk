# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFavoriteReportsRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        page_size: int = None,
        tree_type: str = None,
        user_id: str = None,
    ):
        # Keyword of the work name.
        self.keyword = keyword
        # Number of rows in the work list to be queried:
        # Default value: 10
        # Maximum value: 9999
        self.page_size = page_size
        # Type of the work to be queried (leave blank to query all types). Value range:
        # - DATAPRODUCT: Data Portal
        # - PAGE: Dashboard
        # - REPORT: Spreadsheet
        self.tree_type = tree_type
        # The UserID of the user in Quick BI to be queried.
        # 
        # This parameter is required.
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

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.tree_type is not None:
            result['TreeType'] = self.tree_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TreeType') is not None:
            self.tree_type = m.get('TreeType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

