# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class MCPAPI(DaraModel):
    def __init__(
        self,
        backend_config: main_models.MCPBackendConfig = None,
        description: str = None,
        exposed_uri_path: str = None,
        match: main_models.MCPMatch = None,
        mcp_statistics_enable: bool = None,
        protocol: str = None,
        tool_id: str = None,
        tools_config: str = None,
    ):
        self.backend_config = backend_config
        self.description = description
        self.exposed_uri_path = exposed_uri_path
        self.match = match
        self.mcp_statistics_enable = mcp_statistics_enable
        self.protocol = protocol
        self.tool_id = tool_id
        self.tools_config = tools_config

    def validate(self):
        if self.backend_config:
            self.backend_config.validate()
        if self.match:
            self.match.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_config is not None:
            result['backendConfig'] = self.backend_config.to_map()

        if self.description is not None:
            result['description'] = self.description

        if self.exposed_uri_path is not None:
            result['exposedUriPath'] = self.exposed_uri_path

        if self.match is not None:
            result['match'] = self.match.to_map()

        if self.mcp_statistics_enable is not None:
            result['mcpStatisticsEnable'] = self.mcp_statistics_enable

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.tool_id is not None:
            result['toolId'] = self.tool_id

        if self.tools_config is not None:
            result['toolsConfig'] = self.tools_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backendConfig') is not None:
            temp_model = main_models.MCPBackendConfig()
            self.backend_config = temp_model.from_map(m.get('backendConfig'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('exposedUriPath') is not None:
            self.exposed_uri_path = m.get('exposedUriPath')

        if m.get('match') is not None:
            temp_model = main_models.MCPMatch()
            self.match = temp_model.from_map(m.get('match'))

        if m.get('mcpStatisticsEnable') is not None:
            self.mcp_statistics_enable = m.get('mcpStatisticsEnable')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('toolId') is not None:
            self.tool_id = m.get('toolId')

        if m.get('toolsConfig') is not None:
            self.tools_config = m.get('toolsConfig')

        return self

