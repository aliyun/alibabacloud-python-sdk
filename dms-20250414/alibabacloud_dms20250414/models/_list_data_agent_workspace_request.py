# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataAgentWorkspaceRequest(DaraModel):
    def __init__(
        self,
        dmsunit: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        order_by: str = None,
        page_number: str = None,
        page_size: str = None,
        workspace_name: str = None,
        workspace_type: str = None,
    ):
        self.dmsunit = dmsunit
        self.max_results = max_results
        self.next_token = next_token
        self.order = order
        self.order_by = order_by
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.workspace_name = workspace_name
        # This parameter is required.
        self.workspace_type = workspace_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dmsunit is not None:
            result['DMSUnit'] = self.dmsunit

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order is not None:
            result['Order'] = self.order

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        if self.workspace_type is not None:
            result['WorkspaceType'] = self.workspace_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        if m.get('WorkspaceType') is not None:
            self.workspace_type = m.get('WorkspaceType')

        return self

