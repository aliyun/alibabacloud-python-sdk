# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class CreateMcpServerRequest(DaraModel):
    def __init__(
        self,
        assembled_sources: List[main_models.CreateMcpServerRequestAssembledSources] = None,
        backend_config: main_models.CreateMcpServerRequestBackendConfig = None,
        create_from_type: str = None,
        description: str = None,
        domain_ids: List[str] = None,
        exposed_uri_path: str = None,
        gateway_id: str = None,
        gray_mcp_server_configs: List[main_models.CreateMcpServerRequestGrayMcpServerConfigs] = None,
        match: main_models.HttpRouteMatch = None,
        mcp_server_config: main_models.CreateMcpServerRequestMcpServerConfig = None,
        mcp_statistics_enable: bool = None,
        name: str = None,
        protocol: str = None,
        type: str = None,
    ):
        # The list of assembly sources. This parameter is required when the type parameter is set to AssemblyMCP.
        self.assembled_sources = assembled_sources
        # The backend service configurations for the route.
        self.backend_config = backend_config
        # Creates the MCP server from the specified type.
        self.create_from_type = create_from_type
        # The MCP server description.
        self.description = description
        # The domain IDs.
        self.domain_ids = domain_ids
        # The exposed URI path. This parameter is required when the protocol parameter is set to SSE or StreamableHTTP, and the type parameter is set to RealMCP.
        self.exposed_uri_path = exposed_uri_path
        # The ID of the gateway.
        # 
        # This parameter is required.
        self.gateway_id = gateway_id
        self.gray_mcp_server_configs = gray_mcp_server_configs
        # The route match rule.
        self.match = match
        self.mcp_server_config = mcp_server_config
        # Specifies whether MCP observability is enabled. Default: false.
        self.mcp_statistics_enable = mcp_statistics_enable
        # The name of the MCP server. The name must match the regular expression ^[a-z0-9](%5B-a-z0-9%5D\\*%5Ba-z0-9%5D)?(.[a-z0-9](%5B-a-z0-9%5D\\*%5Ba-z0-9%5D)?)\\*$ and can be up to 64 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The protocol type. Valid values: HTTP, HTTPS, SSE, and StreamableHTTP
        self.protocol = protocol
        # The type. Valid value:
        # 
        # RealMCP: regular MCP service
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.assembled_sources:
            for v1 in self.assembled_sources:
                 if v1:
                    v1.validate()
        if self.backend_config:
            self.backend_config.validate()
        if self.gray_mcp_server_configs:
            for v1 in self.gray_mcp_server_configs:
                 if v1:
                    v1.validate()
        if self.match:
            self.match.validate()
        if self.mcp_server_config:
            self.mcp_server_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['assembledSources'] = []
        if self.assembled_sources is not None:
            for k1 in self.assembled_sources:
                result['assembledSources'].append(k1.to_map() if k1 else None)

        if self.backend_config is not None:
            result['backendConfig'] = self.backend_config.to_map()

        if self.create_from_type is not None:
            result['createFromType'] = self.create_from_type

        if self.description is not None:
            result['description'] = self.description

        if self.domain_ids is not None:
            result['domainIds'] = self.domain_ids

        if self.exposed_uri_path is not None:
            result['exposedUriPath'] = self.exposed_uri_path

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        result['grayMcpServerConfigs'] = []
        if self.gray_mcp_server_configs is not None:
            for k1 in self.gray_mcp_server_configs:
                result['grayMcpServerConfigs'].append(k1.to_map() if k1 else None)

        if self.match is not None:
            result['match'] = self.match.to_map()

        if self.mcp_server_config is not None:
            result['mcpServerConfig'] = self.mcp_server_config.to_map()

        if self.mcp_statistics_enable is not None:
            result['mcpStatisticsEnable'] = self.mcp_statistics_enable

        if self.name is not None:
            result['name'] = self.name

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assembled_sources = []
        if m.get('assembledSources') is not None:
            for k1 in m.get('assembledSources'):
                temp_model = main_models.CreateMcpServerRequestAssembledSources()
                self.assembled_sources.append(temp_model.from_map(k1))

        if m.get('backendConfig') is not None:
            temp_model = main_models.CreateMcpServerRequestBackendConfig()
            self.backend_config = temp_model.from_map(m.get('backendConfig'))

        if m.get('createFromType') is not None:
            self.create_from_type = m.get('createFromType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domainIds') is not None:
            self.domain_ids = m.get('domainIds')

        if m.get('exposedUriPath') is not None:
            self.exposed_uri_path = m.get('exposedUriPath')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        self.gray_mcp_server_configs = []
        if m.get('grayMcpServerConfigs') is not None:
            for k1 in m.get('grayMcpServerConfigs'):
                temp_model = main_models.CreateMcpServerRequestGrayMcpServerConfigs()
                self.gray_mcp_server_configs.append(temp_model.from_map(k1))

        if m.get('match') is not None:
            temp_model = main_models.HttpRouteMatch()
            self.match = temp_model.from_map(m.get('match'))

        if m.get('mcpServerConfig') is not None:
            temp_model = main_models.CreateMcpServerRequestMcpServerConfig()
            self.mcp_server_config = temp_model.from_map(m.get('mcpServerConfig'))

        if m.get('mcpStatisticsEnable') is not None:
            self.mcp_statistics_enable = m.get('mcpStatisticsEnable')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateMcpServerRequestMcpServerConfig(DaraModel):
    def __init__(
        self,
        mcp_server_spec: str = None,
        swagger_config: str = None,
    ):
        self.mcp_server_spec = mcp_server_spec
        self.swagger_config = swagger_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mcp_server_spec is not None:
            result['mcpServerSpec'] = self.mcp_server_spec

        if self.swagger_config is not None:
            result['swaggerConfig'] = self.swagger_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mcpServerSpec') is not None:
            self.mcp_server_spec = m.get('mcpServerSpec')

        if m.get('swaggerConfig') is not None:
            self.swagger_config = m.get('swaggerConfig')

        return self

class CreateMcpServerRequestGrayMcpServerConfigs(DaraModel):
    def __init__(
        self,
        backend_config: main_models.CreateMcpServerRequestGrayMcpServerConfigsBackendConfig = None,
        match: main_models.HttpRouteMatch = None,
        route_id: str = None,
    ):
        self.backend_config = backend_config
        self.match = match
        self.route_id = route_id

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

        if self.match is not None:
            result['match'] = self.match.to_map()

        if self.route_id is not None:
            result['routeId'] = self.route_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backendConfig') is not None:
            temp_model = main_models.CreateMcpServerRequestGrayMcpServerConfigsBackendConfig()
            self.backend_config = temp_model.from_map(m.get('backendConfig'))

        if m.get('match') is not None:
            temp_model = main_models.HttpRouteMatch()
            self.match = temp_model.from_map(m.get('match'))

        if m.get('routeId') is not None:
            self.route_id = m.get('routeId')

        return self

class CreateMcpServerRequestGrayMcpServerConfigsBackendConfig(DaraModel):
    def __init__(
        self,
        scene: str = None,
        services: List[main_models.CreateMcpServerRequestGrayMcpServerConfigsBackendConfigServices] = None,
    ):
        self.scene = scene
        self.services = services

    def validate(self):
        if self.services:
            for v1 in self.services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scene is not None:
            result['scene'] = self.scene

        result['services'] = []
        if self.services is not None:
            for k1 in self.services:
                result['services'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scene') is not None:
            self.scene = m.get('scene')

        self.services = []
        if m.get('services') is not None:
            for k1 in m.get('services'):
                temp_model = main_models.CreateMcpServerRequestGrayMcpServerConfigsBackendConfigServices()
                self.services.append(temp_model.from_map(k1))

        return self

class CreateMcpServerRequestGrayMcpServerConfigsBackendConfigServices(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
        service_id: str = None,
        version: str = None,
        weight: int = None,
    ):
        self.port = port
        self.protocol = protocol
        self.service_id = service_id
        self.version = version
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['port'] = self.port

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.version is not None:
            result['version'] = self.version

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class CreateMcpServerRequestBackendConfig(DaraModel):
    def __init__(
        self,
        scene: str = None,
        services: List[main_models.CreateMcpServerRequestBackendConfigServices] = None,
    ):
        # The scenario of the backend service.
        self.scene = scene
        # The backend services.
        self.services = services

    def validate(self):
        if self.services:
            for v1 in self.services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scene is not None:
            result['scene'] = self.scene

        result['services'] = []
        if self.services is not None:
            for k1 in self.services:
                result['services'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scene') is not None:
            self.scene = m.get('scene')

        self.services = []
        if m.get('services') is not None:
            for k1 in m.get('services'):
                temp_model = main_models.CreateMcpServerRequestBackendConfigServices()
                self.services.append(temp_model.from_map(k1))

        return self

class CreateMcpServerRequestBackendConfigServices(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
        service_id: str = None,
        version: str = None,
        weight: int = None,
    ):
        # The backend node port of the service.
        self.port = port
        # The service protocol. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        self.protocol = protocol
        # The service ID.
        self.service_id = service_id
        # The service version.
        self.version = version
        # The weight.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['port'] = self.port

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.version is not None:
            result['version'] = self.version

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class CreateMcpServerRequestAssembledSources(DaraModel):
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
        # The list of the MCP tools.
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

