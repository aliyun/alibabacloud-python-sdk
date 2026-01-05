# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class SyncMCPServersRequest(DaraModel):
    def __init__(
        self,
        domain_ids: List[str] = None,
        gateway_id: str = None,
        nacos_mcp_servers: List[main_models.SyncMCPServersRequestNacosMcpServers] = None,
        namespace: str = None,
        source_id: str = None,
    ):
        # The domain ID.
        self.domain_ids = domain_ids
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The synchronized Nacos MCP server list. If the synchronized MCP server is included, add the mcpServerId parameter.
        self.nacos_mcp_servers = nacos_mcp_servers
        # The Nacos namespace.
        self.namespace = namespace
        # The source ID.
        self.source_id = source_id

    def validate(self):
        if self.nacos_mcp_servers:
            for v1 in self.nacos_mcp_servers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_ids is not None:
            result['domainIds'] = self.domain_ids

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        result['nacosMcpServers'] = []
        if self.nacos_mcp_servers is not None:
            for k1 in self.nacos_mcp_servers:
                result['nacosMcpServers'].append(k1.to_map() if k1 else None)

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainIds') is not None:
            self.domain_ids = m.get('domainIds')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        self.nacos_mcp_servers = []
        if m.get('nacosMcpServers') is not None:
            for k1 in m.get('nacosMcpServers'):
                temp_model = main_models.SyncMCPServersRequestNacosMcpServers()
                self.nacos_mcp_servers.append(temp_model.from_map(k1))

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        return self

class SyncMCPServersRequestNacosMcpServers(DaraModel):
    def __init__(
        self,
        exposed_uri_path: str = None,
        instance_id: str = None,
        mcp_server_id: str = None,
        mcp_server_name: str = None,
        protocols: List[str] = None,
    ):
        # The exposed URI path. This parameter is required when the protocol parameter is set to SSE or StreamableHTTP and the type parameter is set to RealMCP.
        self.exposed_uri_path = exposed_uri_path
        # The Nacos instance ID.
        self.instance_id = instance_id
        # The MCP server ID.
        self.mcp_server_id = mcp_server_id
        # The name of the MCP server.
        self.mcp_server_name = mcp_server_name
        # The protocol.
        self.protocols = protocols

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exposed_uri_path is not None:
            result['exposedUriPath'] = self.exposed_uri_path

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.mcp_server_id is not None:
            result['mcpServerId'] = self.mcp_server_id

        if self.mcp_server_name is not None:
            result['mcpServerName'] = self.mcp_server_name

        if self.protocols is not None:
            result['protocols'] = self.protocols

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exposedUriPath') is not None:
            self.exposed_uri_path = m.get('exposedUriPath')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('mcpServerId') is not None:
            self.mcp_server_id = m.get('mcpServerId')

        if m.get('mcpServerName') is not None:
            self.mcp_server_name = m.get('mcpServerName')

        if m.get('protocols') is not None:
            self.protocols = m.get('protocols')

        return self

