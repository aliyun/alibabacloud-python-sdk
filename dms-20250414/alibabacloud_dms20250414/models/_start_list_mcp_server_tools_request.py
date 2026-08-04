# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartListMcpServerToolsRequest(DaraModel):
    def __init__(
        self,
        dmsunit: str = None,
        language: str = None,
        mcp_server_uuid: str = None,
    ):
        # The identifier of the Data Management unit that runs the Data Agent resources.
        self.dmsunit = dmsunit
        # The language used for the detection session.
        self.language = language
        # The ID of the MCP Server for which to detect connectivity and query the tool list. Only the service creator can trigger the detection.
        self.mcp_server_uuid = mcp_server_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dmsunit is not None:
            result['DMSUnit'] = self.dmsunit

        if self.language is not None:
            result['Language'] = self.language

        if self.mcp_server_uuid is not None:
            result['McpServerUuid'] = self.mcp_server_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('McpServerUuid') is not None:
            self.mcp_server_uuid = m.get('McpServerUuid')

        return self

