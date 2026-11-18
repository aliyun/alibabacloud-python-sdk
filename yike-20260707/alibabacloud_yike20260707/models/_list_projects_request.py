# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProjectsRequest(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        workspace_id: str = None,
    ):
        # The page number. Pages start from 1. Specify a valid positive integer for both this parameter and PageSize. Otherwise, the query defaults to page 1 with 10 entries per page.
        self.page_no = page_no
        # The number of entries to return on each page. Specify a valid positive integer for both this parameter and PageNo. Otherwise, the query defaults to page 1 with 10 entries per page.
        self.page_size = page_size
        # Filters projects by workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

