# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HttpRoute(DaraModel):
    def __init__(
        self,
        backend: main_models.Backend = None,
        builtin: str = None,
        create_timestamp: int = None,
        deploy_status: str = None,
        description: str = None,
        domain_infos: List[main_models.HttpRouteDomainInfos] = None,
        environment_info: main_models.HttpRouteEnvironmentInfo = None,
        gateway_status: Dict[str, str] = None,
        match: main_models.HttpRouteMatch = None,
        mcp_server_info: main_models.HttpRouteMcpServerInfo = None,
        name: str = None,
        route_id: str = None,
        update_timestamp: int = None,
    ):
        self.backend = backend
        self.builtin = builtin
        self.create_timestamp = create_timestamp
        self.deploy_status = deploy_status
        self.description = description
        self.domain_infos = domain_infos
        self.environment_info = environment_info
        self.gateway_status = gateway_status
        self.match = match
        self.mcp_server_info = mcp_server_info
        self.name = name
        self.route_id = route_id
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.backend:
            self.backend.validate()
        if self.domain_infos:
            for v1 in self.domain_infos:
                 if v1:
                    v1.validate()
        if self.environment_info:
            self.environment_info.validate()
        if self.match:
            self.match.validate()
        if self.mcp_server_info:
            self.mcp_server_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend is not None:
            result['backend'] = self.backend.to_map()

        if self.builtin is not None:
            result['builtin'] = self.builtin

        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp

        if self.deploy_status is not None:
            result['deployStatus'] = self.deploy_status

        if self.description is not None:
            result['description'] = self.description

        result['domainInfos'] = []
        if self.domain_infos is not None:
            for k1 in self.domain_infos:
                result['domainInfos'].append(k1.to_map() if k1 else None)

        if self.environment_info is not None:
            result['environmentInfo'] = self.environment_info.to_map()

        if self.gateway_status is not None:
            result['gatewayStatus'] = self.gateway_status

        if self.match is not None:
            result['match'] = self.match.to_map()

        if self.mcp_server_info is not None:
            result['mcpServerInfo'] = self.mcp_server_info.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.route_id is not None:
            result['routeId'] = self.route_id

        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backend') is not None:
            temp_model = main_models.Backend()
            self.backend = temp_model.from_map(m.get('backend'))

        if m.get('builtin') is not None:
            self.builtin = m.get('builtin')

        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')

        if m.get('deployStatus') is not None:
            self.deploy_status = m.get('deployStatus')

        if m.get('description') is not None:
            self.description = m.get('description')

        self.domain_infos = []
        if m.get('domainInfos') is not None:
            for k1 in m.get('domainInfos'):
                temp_model = main_models.HttpRouteDomainInfos()
                self.domain_infos.append(temp_model.from_map(k1))

        if m.get('environmentInfo') is not None:
            temp_model = main_models.HttpRouteEnvironmentInfo()
            self.environment_info = temp_model.from_map(m.get('environmentInfo'))

        if m.get('gatewayStatus') is not None:
            self.gateway_status = m.get('gatewayStatus')

        if m.get('match') is not None:
            temp_model = main_models.HttpRouteMatch()
            self.match = temp_model.from_map(m.get('match'))

        if m.get('mcpServerInfo') is not None:
            temp_model = main_models.HttpRouteMcpServerInfo()
            self.mcp_server_info = temp_model.from_map(m.get('mcpServerInfo'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('routeId') is not None:
            self.route_id = m.get('routeId')

        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')

        return self

class HttpRouteMcpServerInfo(DaraModel):
    def __init__(
        self,
        create_from_type: str = None,
        import_instance_id: str = None,
        import_mcp_server_id: str = None,
        import_namespace: str = None,
        mcp_route_config: main_models.HttpRouteMcpServerInfoMcpRouteConfig = None,
        mcp_server_config: str = None,
    ):
        self.create_from_type = create_from_type
        self.import_instance_id = import_instance_id
        self.import_mcp_server_id = import_mcp_server_id
        self.import_namespace = import_namespace
        self.mcp_route_config = mcp_route_config
        self.mcp_server_config = mcp_server_config

    def validate(self):
        if self.mcp_route_config:
            self.mcp_route_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_from_type is not None:
            result['createFromType'] = self.create_from_type

        if self.import_instance_id is not None:
            result['importInstanceId'] = self.import_instance_id

        if self.import_mcp_server_id is not None:
            result['importMcpServerId'] = self.import_mcp_server_id

        if self.import_namespace is not None:
            result['importNamespace'] = self.import_namespace

        if self.mcp_route_config is not None:
            result['mcpRouteConfig'] = self.mcp_route_config.to_map()

        if self.mcp_server_config is not None:
            result['mcpServerConfig'] = self.mcp_server_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createFromType') is not None:
            self.create_from_type = m.get('createFromType')

        if m.get('importInstanceId') is not None:
            self.import_instance_id = m.get('importInstanceId')

        if m.get('importMcpServerId') is not None:
            self.import_mcp_server_id = m.get('importMcpServerId')

        if m.get('importNamespace') is not None:
            self.import_namespace = m.get('importNamespace')

        if m.get('mcpRouteConfig') is not None:
            temp_model = main_models.HttpRouteMcpServerInfoMcpRouteConfig()
            self.mcp_route_config = temp_model.from_map(m.get('mcpRouteConfig'))

        if m.get('mcpServerConfig') is not None:
            self.mcp_server_config = m.get('mcpServerConfig')

        return self

class HttpRouteMcpServerInfoMcpRouteConfig(DaraModel):
    def __init__(
        self,
        exposed_uri_path: str = None,
        protocol: str = None,
    ):
        self.exposed_uri_path = exposed_uri_path
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exposed_uri_path is not None:
            result['exposedUriPath'] = self.exposed_uri_path

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exposedUriPath') is not None:
            self.exposed_uri_path = m.get('exposedUriPath')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

class HttpRouteEnvironmentInfo(DaraModel):
    def __init__(
        self,
        alias: str = None,
        environment_id: str = None,
        gateway_info: main_models.HttpRouteEnvironmentInfoGatewayInfo = None,
        name: str = None,
        sub_domains: List[main_models.HttpRouteEnvironmentInfoSubDomains] = None,
    ):
        self.alias = alias
        self.environment_id = environment_id
        self.gateway_info = gateway_info
        self.name = name
        self.sub_domains = sub_domains

    def validate(self):
        if self.gateway_info:
            self.gateway_info.validate()
        if self.sub_domains:
            for v1 in self.sub_domains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()

        if self.name is not None:
            result['name'] = self.name

        result['subDomains'] = []
        if self.sub_domains is not None:
            for k1 in self.sub_domains:
                result['subDomains'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayInfo') is not None:
            temp_model = main_models.HttpRouteEnvironmentInfoGatewayInfo()
            self.gateway_info = temp_model.from_map(m.get('gatewayInfo'))

        if m.get('name') is not None:
            self.name = m.get('name')

        self.sub_domains = []
        if m.get('subDomains') is not None:
            for k1 in m.get('subDomains'):
                temp_model = main_models.HttpRouteEnvironmentInfoSubDomains()
                self.sub_domains.append(temp_model.from_map(k1))

        return self

class HttpRouteEnvironmentInfoSubDomains(DaraModel):
    def __init__(
        self,
        domain_id: str = None,
        name: str = None,
        network_type: str = None,
        protocol: str = None,
    ):
        self.domain_id = domain_id
        self.name = name
        self.network_type = network_type
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_id is not None:
            result['domainId'] = self.domain_id

        if self.name is not None:
            result['name'] = self.name

        if self.network_type is not None:
            result['networkType'] = self.network_type

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

class HttpRouteEnvironmentInfoGatewayInfo(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        name: str = None,
    ):
        self.gateway_id = gateway_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class HttpRouteDomainInfos(DaraModel):
    def __init__(
        self,
        domain_id: str = None,
        name: str = None,
        protocol: str = None,
    ):
        self.domain_id = domain_id
        self.name = name
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_id is not None:
            result['domainId'] = self.domain_id

        if self.name is not None:
            result['name'] = self.name

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

