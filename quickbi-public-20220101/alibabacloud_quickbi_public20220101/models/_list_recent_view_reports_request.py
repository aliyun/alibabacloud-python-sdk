# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRecentViewReportsRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        offset_day: int = None,
        page_size: int = None,
        query_mode: str = None,
        tree_type: str = None,
        user_id: str = None,
    ):
        # Keyword of the name of the work.
        self.keyword = keyword
        # The number of days to query data in the last few days. Default value: 10.
        self.offset_day = offset_day
        # Query the number of rows in the work list:
        # 
        # *   Default value: 10.
        # *   Maximum value: 9999
        self.page_size = page_size
        # The query mode. Valid values:
        # 
        # *   1: Sort by number of visits
        # *   2: Sort by Last Access Time
        self.query_mode = query_mode
        # Query the type of the work (fill in the blank to query all types). Valid values:
        # 
        # *   DATAPRODUCT: BI portal
        # *   PAGE: Dashboard
        # *   REPORT: workbook
        self.tree_type = tree_type
        # The UserID of the user in the Quick BI.
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

        if self.offset_day is not None:
            result['OffsetDay'] = self.offset_day

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_mode is not None:
            result['QueryMode'] = self.query_mode

        if self.tree_type is not None:
            result['TreeType'] = self.tree_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('OffsetDay') is not None:
            self.offset_day = m.get('OffsetDay')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryMode') is not None:
            self.query_mode = m.get('QueryMode')

        if m.get('TreeType') is not None:
            self.tree_type = m.get('TreeType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

