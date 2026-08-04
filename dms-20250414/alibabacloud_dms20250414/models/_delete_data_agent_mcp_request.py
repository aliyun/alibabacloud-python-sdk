# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteDataAgentMcpRequest(DaraModel):
    def __init__(
        self,
        mcp_server_ids: List[str] = None,
        workspace_id: str = None,
    ):
        # The list of MCP Server IDs to delete.
        self.mcp_server_ids = mcp_server_ids
        # The ID of the Data Agent workspace.
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
        if self.mcp_server_ids is not None:
            result['McpServerIds'] = self.mcp_server_ids

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('McpServerIds') is not None:
            self.mcp_server_ids = m.get('McpServerIds')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

