# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataAgentMcpRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        ready_only: bool = None,
        search_key: str = None,
        type: str = None,
        workspace_id: str = None,
    ):
        # A compatible pagination parameter. The actual number of records per page is controlled by PageSize.
        self.max_results = max_results
        # A compatible pagination token. The actual page sequence is controlled by PageNumber.
        self.next_token = next_token
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of records per page. Valid values: 1 to 500. Default value: 20.
        self.page_size = page_size
        # Specifies whether to return only MCP Servers that are enabled and in the ready state. Default value: false.
        self.ready_only = ready_only
        # The keyword for name search. The server performs a fuzzy match against MCP Server names.
        self.search_key = search_key
        # The MCP Server type. Valid values:
        # - system: system MCP.
        # - customer: custom MCP.
        self.type = type
        # The Data Agent workspace ID. The caller must have at least MEMBER permissions on this workspace.
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.ready_only is not None:
            result['ReadyOnly'] = self.ready_only

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.type is not None:
            result['Type'] = self.type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ReadyOnly') is not None:
            self.ready_only = m.get('ReadyOnly')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

