# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListMcpServersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListMcpServersResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The response payload.
        self.data = data
        # The status message.
        self.message = message
        # The request ID.
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
            temp_model = main_models.ListMcpServersResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListMcpServersResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListMcpServersResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # The list of MCP servers.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_size = total_size

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_size is not None:
            result['totalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListMcpServersResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')

        return self

class ListMcpServersResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        assembled_sources: List[main_models.ListMcpServersResponseBodyDataItemsAssembledSources] = None,
        backend: main_models.Backend = None,
        create_from_type: str = None,
        deploy_status: str = None,
        description: str = None,
        domain_ids: List[str] = None,
        domain_infos: List[main_models.HttpApiDomainInfo] = None,
        environment_id: str = None,
        exposed_uri_path: str = None,
        gateway_id: str = None,
        match: main_models.HttpRouteMatch = None,
        mcp_server_config: str = None,
        mcp_server_id: str = None,
        mcp_server_path: str = None,
        mcp_statistics_enable: bool = None,
        nacos_mcp_sync_info: main_models.ListMcpServersResponseBodyDataItemsNacosMcpSyncInfo = None,
        name: str = None,
        protocol: str = None,
        route_id: str = None,
        type: str = None,
    ):
        # The API ID.
        self.api_id = api_id
        # The list of assembly sources. This parameter is required when the type parameter is set to AssemblyMCP.
        self.assembled_sources = assembled_sources
        # The backend service of the route.
        self.backend = backend
        # The type of source for MCP server creation. Valid values: 
        # 
        # ApiGatewayHttpToMCP 
        # ApiGatewayMcpHosting 
        # ApiGatewayAssembly 
        # NacosHttpToMCP 
        # NacosMcpHosting
        self.create_from_type = create_from_type
        # The publishing status of the API in the current environment.
        self.deploy_status = deploy_status
        # The description.
        self.description = description
        # The domain name IDs.
        self.domain_ids = domain_ids
        # The list of domain information.
        self.domain_infos = domain_infos
        # The environment ID.
        self.environment_id = environment_id
        # The exposed URI path. This parameter is required when the protocol parameter is set to SSE or StreamableHTTP, and the type parameter is set to RealMCP.
        self.exposed_uri_path = exposed_uri_path
        # The gateway instance ID.
        self.gateway_id = gateway_id
        # The route match rule.
        self.match = match
        # The HTTP-to-MCP configurations.
        self.mcp_server_config = mcp_server_config
        # The MCP server ID.
        self.mcp_server_id = mcp_server_id
        # The MCP server access path provided by the gateway.
        self.mcp_server_path = mcp_server_path
        # Indicates whether MCP observability is enabled. Default value: false.
        self.mcp_statistics_enable = mcp_statistics_enable
        # The MCP information synchronized and managed by Nacos.
        self.nacos_mcp_sync_info = nacos_mcp_sync_info
        # The name of the MCP server.
        self.name = name
        # The service protocol.
        self.protocol = protocol
        # The ID of the MCP server associated route.
        self.route_id = route_id
        # The type of the MCP server. Valid values: RealMCP and AssemblyMCP.
        self.type = type

    def validate(self):
        if self.assembled_sources:
            for v1 in self.assembled_sources:
                 if v1:
                    v1.validate()
        if self.backend:
            self.backend.validate()
        if self.domain_infos:
            for v1 in self.domain_infos:
                 if v1:
                    v1.validate()
        if self.match:
            self.match.validate()
        if self.nacos_mcp_sync_info:
            self.nacos_mcp_sync_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['apiId'] = self.api_id

        result['assembledSources'] = []
        if self.assembled_sources is not None:
            for k1 in self.assembled_sources:
                result['assembledSources'].append(k1.to_map() if k1 else None)

        if self.backend is not None:
            result['backend'] = self.backend.to_map()

        if self.create_from_type is not None:
            result['createFromType'] = self.create_from_type

        if self.deploy_status is not None:
            result['deployStatus'] = self.deploy_status

        if self.description is not None:
            result['description'] = self.description

        if self.domain_ids is not None:
            result['domainIds'] = self.domain_ids

        result['domainInfos'] = []
        if self.domain_infos is not None:
            for k1 in self.domain_infos:
                result['domainInfos'].append(k1.to_map() if k1 else None)

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.exposed_uri_path is not None:
            result['exposedUriPath'] = self.exposed_uri_path

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.match is not None:
            result['match'] = self.match.to_map()

        if self.mcp_server_config is not None:
            result['mcpServerConfig'] = self.mcp_server_config

        if self.mcp_server_id is not None:
            result['mcpServerId'] = self.mcp_server_id

        if self.mcp_server_path is not None:
            result['mcpServerPath'] = self.mcp_server_path

        if self.mcp_statistics_enable is not None:
            result['mcpStatisticsEnable'] = self.mcp_statistics_enable

        if self.nacos_mcp_sync_info is not None:
            result['nacosMcpSyncInfo'] = self.nacos_mcp_sync_info.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.route_id is not None:
            result['routeId'] = self.route_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')

        self.assembled_sources = []
        if m.get('assembledSources') is not None:
            for k1 in m.get('assembledSources'):
                temp_model = main_models.ListMcpServersResponseBodyDataItemsAssembledSources()
                self.assembled_sources.append(temp_model.from_map(k1))

        if m.get('backend') is not None:
            temp_model = main_models.Backend()
            self.backend = temp_model.from_map(m.get('backend'))

        if m.get('createFromType') is not None:
            self.create_from_type = m.get('createFromType')

        if m.get('deployStatus') is not None:
            self.deploy_status = m.get('deployStatus')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domainIds') is not None:
            self.domain_ids = m.get('domainIds')

        self.domain_infos = []
        if m.get('domainInfos') is not None:
            for k1 in m.get('domainInfos'):
                temp_model = main_models.HttpApiDomainInfo()
                self.domain_infos.append(temp_model.from_map(k1))

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('exposedUriPath') is not None:
            self.exposed_uri_path = m.get('exposedUriPath')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('match') is not None:
            temp_model = main_models.HttpRouteMatch()
            self.match = temp_model.from_map(m.get('match'))

        if m.get('mcpServerConfig') is not None:
            self.mcp_server_config = m.get('mcpServerConfig')

        if m.get('mcpServerId') is not None:
            self.mcp_server_id = m.get('mcpServerId')

        if m.get('mcpServerPath') is not None:
            self.mcp_server_path = m.get('mcpServerPath')

        if m.get('mcpStatisticsEnable') is not None:
            self.mcp_statistics_enable = m.get('mcpStatisticsEnable')

        if m.get('nacosMcpSyncInfo') is not None:
            temp_model = main_models.ListMcpServersResponseBodyDataItemsNacosMcpSyncInfo()
            self.nacos_mcp_sync_info = temp_model.from_map(m.get('nacosMcpSyncInfo'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('routeId') is not None:
            self.route_id = m.get('routeId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListMcpServersResponseBodyDataItemsNacosMcpSyncInfo(DaraModel):
    def __init__(
        self,
        import_instance_id: str = None,
        import_mcp_server_id: str = None,
        import_namespace: str = None,
    ):
        # The Nacos instance.
        self.import_instance_id = import_instance_id
        # The synchronized MCP server ID.
        self.import_mcp_server_id = import_mcp_server_id
        # The Nacos namespace.
        self.import_namespace = import_namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.import_instance_id is not None:
            result['importInstanceId'] = self.import_instance_id

        if self.import_mcp_server_id is not None:
            result['importMcpServerId'] = self.import_mcp_server_id

        if self.import_namespace is not None:
            result['importNamespace'] = self.import_namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('importInstanceId') is not None:
            self.import_instance_id = m.get('importInstanceId')

        if m.get('importMcpServerId') is not None:
            self.import_mcp_server_id = m.get('importMcpServerId')

        if m.get('importNamespace') is not None:
            self.import_namespace = m.get('importNamespace')

        return self

class ListMcpServersResponseBodyDataItemsAssembledSources(DaraModel):
    def __init__(
        self,
        mcp_server_id: str = None,
        mcp_server_name: str = None,
        tools: List[str] = None,
    ):
        # The MCP server ID.
        self.mcp_server_id = mcp_server_id
        # The name of the MCP server.
        self.mcp_server_name = mcp_server_name
        # The list of MCP tools.
        self.tools = tools

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mcp_server_id is not None:
            result['mcpServerId'] = self.mcp_server_id

        if self.mcp_server_name is not None:
            result['mcpServerName'] = self.mcp_server_name

        if self.tools is not None:
            result['tools'] = self.tools

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mcpServerId') is not None:
            self.mcp_server_id = m.get('mcpServerId')

        if m.get('mcpServerName') is not None:
            self.mcp_server_name = m.get('mcpServerName')

        if m.get('tools') is not None:
            self.tools = m.get('tools')

        return self

