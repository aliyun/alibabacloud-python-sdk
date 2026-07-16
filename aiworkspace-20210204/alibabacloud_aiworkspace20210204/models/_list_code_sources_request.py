# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCodeSourcesRequest(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        workspace_id: str = None,
    ):
        # The display name of the code source configuration. Fuzzy match is supported.
        self.display_name = display_name
        # The sort order. Valid values:
        # 
        # - ASC (default): Ascending order.
        # 
        # - DESC: Descending order.
        self.order = order
        # The page number. The value starts from 1. The default value is 1.
        self.page_number = page_number
        # The number of entries to return on each page. The default value is 20.
        self.page_size = page_size
        # The field to use for sorting. Valid values:
        # 
        # - GmtModifyTime: The time when the code source was last modified.
        # 
        # - DisplayName: The display name.
        # 
        # - CodeSourceId: The code source ID.
        # 
        # - GmtCreateTime (default): The time when the code source was created.
        self.sort_by = sort_by
        # The workspace ID. For more information, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

