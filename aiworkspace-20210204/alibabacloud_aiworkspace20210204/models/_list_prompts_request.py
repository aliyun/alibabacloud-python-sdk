# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPromptsRequest(DaraModel):
    def __init__(
        self,
        framework_type: str = None,
        order: str = None,
        page_number: str = None,
        page_size: str = None,
        sort_by: str = None,
        workspace_id: str = None,
    ):
        # The prompt template framework type.
        self.framework_type = framework_type
        # The sorting order for the specified field during paging. Default value: ASC.
        # - ASC: ascending order.
        # - DESC: descending order.
        self.order = order
        # The page number, starting from 1. Default value: 1.
        self.page_number = page_number
        # The page size. Default value: 20.
        self.page_size = page_size
        # The field used for sorting. Valid values:
        # - Name: the run name.
        # - GmtCreateTime (default): the run creation time.
        self.sort_by = sort_by
        # The workspace ID. For information about how to obtain the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.framework_type is not None:
            result['FrameworkType'] = self.framework_type

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
        if m.get('FrameworkType') is not None:
            self.framework_type = m.get('FrameworkType')

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

