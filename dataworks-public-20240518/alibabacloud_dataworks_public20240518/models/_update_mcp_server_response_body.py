# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateMcpServerResponseBody(DaraModel):
    def __init__(
        self,
        mcp_server: main_models.UpdateMcpServerResponseBodyMcpServer = None,
        request_id: str = None,
    ):
        # - The details of the updated MCP Server.
        self.mcp_server = mcp_server
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.mcp_server:
            self.mcp_server.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mcp_server is not None:
            result['McpServer'] = self.mcp_server.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('McpServer') is not None:
            temp_model = main_models.UpdateMcpServerResponseBodyMcpServer()
            self.mcp_server = temp_model.from_map(m.get('McpServer'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateMcpServerResponseBodyMcpServer(DaraModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        name: str = None,
    ):
        # The creation time. This value is a millisecond timestamp.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_create_time = gmt_create_time
        # **The last modification time. This value is a millisecond timestamp.**
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_modified_time = gmt_modified_time
        # **The name of the MCP Server.**
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

