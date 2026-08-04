# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDataAgentMcpRequest(DaraModel):
    def __init__(
        self,
        mcp_server_id: str = None,
        workspace_id: str = None,
    ):
        # The unique identifier of the MCP Server to query.
        # 
        # This parameter is required.
        self.mcp_server_id = mcp_server_id
        # The Data Agent workspace ID.
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
        if self.mcp_server_id is not None:
            result['McpServerId'] = self.mcp_server_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('McpServerId') is not None:
            self.mcp_server_id = m.get('McpServerId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

