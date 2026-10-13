# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListContextDatabaseSyncRunLogsRequest(DaraModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        run_id: str = None,
        workspace_id: str = None,
    ):
        self.page = page
        self.page_size = page_size
        # This parameter is required.
        self.run_id = run_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.run_id is not None:
            result['RunId'] = self.run_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

