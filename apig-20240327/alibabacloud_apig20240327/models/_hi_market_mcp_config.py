# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HiMarketMcpConfig(DaraModel):
    def __init__(
        self,
        mcp_server_config: main_models.HiMarketMcpConfigMcpServerConfig = None,
        mcp_server_name: str = None,
        meta: main_models.HiMarketMcpConfigMeta = None,
        tools: str = None,
    ):
        self.mcp_server_config = mcp_server_config
        self.mcp_server_name = mcp_server_name
        self.meta = meta
        self.tools = tools

    def validate(self):
        if self.mcp_server_config:
            self.mcp_server_config.validate()
        if self.meta:
            self.meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mcp_server_config is not None:
            result['mcpServerConfig'] = self.mcp_server_config.to_map()

        if self.mcp_server_name is not None:
            result['mcpServerName'] = self.mcp_server_name

        if self.meta is not None:
            result['meta'] = self.meta.to_map()

        if self.tools is not None:
            result['tools'] = self.tools

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mcpServerConfig') is not None:
            temp_model = main_models.HiMarketMcpConfigMcpServerConfig()
            self.mcp_server_config = temp_model.from_map(m.get('mcpServerConfig'))

        if m.get('mcpServerName') is not None:
            self.mcp_server_name = m.get('mcpServerName')

        if m.get('meta') is not None:
            temp_model = main_models.HiMarketMcpConfigMeta()
            self.meta = temp_model.from_map(m.get('meta'))

        if m.get('tools') is not None:
            self.tools = m.get('tools')

        return self

class HiMarketMcpConfigMeta(DaraModel):
    def __init__(
        self,
        protocol: str = None,
    ):
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

class HiMarketMcpConfigMcpServerConfig(DaraModel):
    def __init__(
        self,
        domains: List[main_models.HiMarketDomain] = None,
        path: str = None,
    ):
        self.domains = domains
        self.path = path

    def validate(self):
        if self.domains:
            for v1 in self.domains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['domains'] = []
        if self.domains is not None:
            for k1 in self.domains:
                result['domains'].append(k1.to_map() if k1 else None)

        if self.path is not None:
            result['path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domains = []
        if m.get('domains') is not None:
            for k1 in m.get('domains'):
                temp_model = main_models.HiMarketDomain()
                self.domains.append(temp_model.from_map(k1))

        if m.get('path') is not None:
            self.path = m.get('path')

        return self

