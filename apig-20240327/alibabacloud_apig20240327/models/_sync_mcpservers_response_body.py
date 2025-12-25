# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class SyncMCPServersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.SyncMCPServersResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.SyncMCPServersResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class SyncMCPServersResponseBodyData(DaraModel):
    def __init__(
        self,
        failed_mcp_servers: List[main_models.SyncMCPServersResponseBodyDataFailedMcpServers] = None,
        succeed_mcp_servers: List[main_models.SyncMCPServersResponseBodyDataSucceedMcpServers] = None,
    ):
        self.failed_mcp_servers = failed_mcp_servers
        self.succeed_mcp_servers = succeed_mcp_servers

    def validate(self):
        if self.failed_mcp_servers:
            for v1 in self.failed_mcp_servers:
                 if v1:
                    v1.validate()
        if self.succeed_mcp_servers:
            for v1 in self.succeed_mcp_servers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['failedMcpServers'] = []
        if self.failed_mcp_servers is not None:
            for k1 in self.failed_mcp_servers:
                result['failedMcpServers'].append(k1.to_map() if k1 else None)

        result['succeedMcpServers'] = []
        if self.succeed_mcp_servers is not None:
            for k1 in self.succeed_mcp_servers:
                result['succeedMcpServers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_mcp_servers = []
        if m.get('failedMcpServers') is not None:
            for k1 in m.get('failedMcpServers'):
                temp_model = main_models.SyncMCPServersResponseBodyDataFailedMcpServers()
                self.failed_mcp_servers.append(temp_model.from_map(k1))

        self.succeed_mcp_servers = []
        if m.get('succeedMcpServers') is not None:
            for k1 in m.get('succeedMcpServers'):
                temp_model = main_models.SyncMCPServersResponseBodyDataSucceedMcpServers()
                self.succeed_mcp_servers.append(temp_model.from_map(k1))

        return self

class SyncMCPServersResponseBodyDataSucceedMcpServers(DaraModel):
    def __init__(
        self,
        mcp_server_name: str = None,
        protocols: List[str] = None,
    ):
        self.mcp_server_name = mcp_server_name
        self.protocols = protocols

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mcp_server_name is not None:
            result['mcpServerName'] = self.mcp_server_name

        if self.protocols is not None:
            result['protocols'] = self.protocols

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mcpServerName') is not None:
            self.mcp_server_name = m.get('mcpServerName')

        if m.get('protocols') is not None:
            self.protocols = m.get('protocols')

        return self

class SyncMCPServersResponseBodyDataFailedMcpServers(DaraModel):
    def __init__(
        self,
        mcp_server_name: str = None,
        protocols: List[str] = None,
    ):
        self.mcp_server_name = mcp_server_name
        self.protocols = protocols

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mcp_server_name is not None:
            result['mcpServerName'] = self.mcp_server_name

        if self.protocols is not None:
            result['protocols'] = self.protocols

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mcpServerName') is not None:
            self.mcp_server_name = m.get('mcpServerName')

        if m.get('protocols') is not None:
            self.protocols = m.get('protocols')

        return self

