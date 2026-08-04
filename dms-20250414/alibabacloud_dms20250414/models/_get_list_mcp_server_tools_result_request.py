# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetListMcpServerToolsResultRequest(DaraModel):
    def __init__(
        self,
        dmsunit: str = None,
        mcp_server_uuid: str = None,
        session_id: str = None,
    ):
        # The DMS unit identifier. This value is typically the same as the DMSUnit used in the request that started the tool detection.
        self.dmsunit = dmsunit
        # The MCP Server ID used when the detection was started. This value must match the detection record associated with the SessionId.
        self.mcp_server_uuid = mcp_server_uuid
        # The temporary session ID returned by StartListMcpServerTools. This ID is used to locate the connectivity detection task.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dmsunit is not None:
            result['DMSUnit'] = self.dmsunit

        if self.mcp_server_uuid is not None:
            result['McpServerUuid'] = self.mcp_server_uuid

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')

        if m.get('McpServerUuid') is not None:
            self.mcp_server_uuid = m.get('McpServerUuid')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

