# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDataAgentMcpRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        enable: bool = None,
        endpoint: str = None,
        headers: str = None,
        mcp_server_id: str = None,
        name: str = None,
        need_uid_in_header: bool = None,
        transport_type: str = None,
        workspace_id: str = None,
    ):
        # The brief description of the artifact. This parameter can be empty.
        self.description = description
        # Specifies whether the MCP server is enabled.
        self.enable = enable
        # The endpoint of the MCP instance.
        self.endpoint = endpoint
        # The request header settings.
        self.headers = headers
        # The ID of the MCP server.
        # 
        # This parameter is required.
        self.mcp_server_id = mcp_server_id
        # The MCP name.
        self.name = name
        # Specifies whether to include the Alibaba Cloud UID in the request header.
        self.need_uid_in_header = need_uid_in_header
        # The transport channel type. Valid values: streamablehttp, sse.
        self.transport_type = transport_type
        # The workspace ID.
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
        if self.description is not None:
            result['Description'] = self.description

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.headers is not None:
            result['Headers'] = self.headers

        if self.mcp_server_id is not None:
            result['McpServerId'] = self.mcp_server_id

        if self.name is not None:
            result['Name'] = self.name

        if self.need_uid_in_header is not None:
            result['NeedUidInHeader'] = self.need_uid_in_header

        if self.transport_type is not None:
            result['TransportType'] = self.transport_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Headers') is not None:
            self.headers = m.get('Headers')

        if m.get('McpServerId') is not None:
            self.mcp_server_id = m.get('McpServerId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NeedUidInHeader') is not None:
            self.need_uid_in_header = m.get('NeedUidInHeader')

        if m.get('TransportType') is not None:
            self.transport_type = m.get('TransportType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

