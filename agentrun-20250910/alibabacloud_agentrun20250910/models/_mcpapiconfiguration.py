# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MCPAPIConfiguration(DaraModel):
    def __init__(
        self,
        description: str = None,
        exposed_uri_path: str = None,
        mcp_statistics_enable: bool = None,
        protocol: str = None,
        tool_id: str = None,
    ):
        self.description = description
        self.exposed_uri_path = exposed_uri_path
        self.mcp_statistics_enable = mcp_statistics_enable
        self.protocol = protocol
        self.tool_id = tool_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.exposed_uri_path is not None:
            result['exposedUriPath'] = self.exposed_uri_path

        if self.mcp_statistics_enable is not None:
            result['mcpStatisticsEnable'] = self.mcp_statistics_enable

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.tool_id is not None:
            result['toolId'] = self.tool_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('exposedUriPath') is not None:
            self.exposed_uri_path = m.get('exposedUriPath')

        if m.get('mcpStatisticsEnable') is not None:
            self.mcp_statistics_enable = m.get('mcpStatisticsEnable')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('toolId') is not None:
            self.tool_id = m.get('toolId')

        return self

