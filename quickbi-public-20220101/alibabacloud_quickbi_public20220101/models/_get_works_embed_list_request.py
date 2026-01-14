# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWorksEmbedListRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        page_no: int = None,
        page_size: int = None,
        works_type: str = None,
        ws_id: str = None,
    ):
        # Report name (fuzzy match)
        self.keyword = keyword
        # Page number (defaults to 1 if empty)
        self.page_no = page_no
        # Number of items per page (defaults to 10 if empty)
        self.page_size = page_size
        # Report type
        # 
        # - page, Dashboard
        # - screen, Data Screen
        # - report, Spreadsheet
        # - ANALYSIS, Ad-hoc Analysis
        # - dashboardOfflineQuery, Self-service Data Retrieval
        # - dataForm, Data Entry Form
        self.works_type = works_type
        # Workspace ID
        self.ws_id = ws_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.works_type is not None:
            result['WorksType'] = self.works_type

        if self.ws_id is not None:
            result['WsId'] = self.ws_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('WorksType') is not None:
            self.works_type = m.get('WorksType')

        if m.get('WsId') is not None:
            self.ws_id = m.get('WsId')

        return self

