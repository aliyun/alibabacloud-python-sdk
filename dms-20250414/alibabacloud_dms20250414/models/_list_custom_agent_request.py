# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCustomAgentRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        query_all_released: bool = None,
        search_key: str = None,
        status: str = None,
        workspace_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.query_all_released = query_all_released
        self.search_key = search_key
        self.status = status
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_all_released is not None:
            result['QueryAllReleased'] = self.query_all_released

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.status is not None:
            result['Status'] = self.status

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryAllReleased') is not None:
            self.query_all_released = m.get('QueryAllReleased')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

