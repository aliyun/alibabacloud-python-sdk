# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class UpdateHttpApiRouteRequest(DaraModel):
    def __init__(
        self,
        backend_config: main_models.UpdateHttpApiRouteRequestBackendConfig = None,
        deploy_configs: List[main_models.HttpApiDeployConfig] = None,
        description: str = None,
        domain_ids: List[str] = None,
        environment_id: str = None,
        match: main_models.HttpRouteMatch = None,
        mcp_route_config: main_models.UpdateHttpApiRouteRequestMcpRouteConfig = None,
        name: str = None,
    ):
        # The backend service configurations of the route.
        self.backend_config = backend_config
        self.deploy_configs = deploy_configs
        # The route description.
        self.description = description
        # The domain IDs.
        self.domain_ids = domain_ids
        # The environment ID.
        self.environment_id = environment_id
        # The rules for matching the route.
        self.match = match
        self.mcp_route_config = mcp_route_config
        self.name = name

    def validate(self):
        if self.backend_config:
            self.backend_config.validate()
        if self.deploy_configs:
            for v1 in self.deploy_configs:
                 if v1:
                    v1.validate()
        if self.match:
            self.match.validate()
        if self.mcp_route_config:
            self.mcp_route_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_config is not None:
            result['backendConfig'] = self.backend_config.to_map()

        result['deployConfigs'] = []
        if self.deploy_configs is not None:
            for k1 in self.deploy_configs:
                result['deployConfigs'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        if self.domain_ids is not None:
            result['domainIds'] = self.domain_ids

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.match is not None:
            result['match'] = self.match.to_map()

        if self.mcp_route_config is not None:
            result['mcpRouteConfig'] = self.mcp_route_config.to_map()

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backendConfig') is not None:
            temp_model = main_models.UpdateHttpApiRouteRequestBackendConfig()
            self.backend_config = temp_model.from_map(m.get('backendConfig'))

        self.deploy_configs = []
        if m.get('deployConfigs') is not None:
            for k1 in m.get('deployConfigs'):
                temp_model = main_models.HttpApiDeployConfig()
                self.deploy_configs.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domainIds') is not None:
            self.domain_ids = m.get('domainIds')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('match') is not None:
            temp_model = main_models.HttpRouteMatch()
            self.match = temp_model.from_map(m.get('match'))

        if m.get('mcpRouteConfig') is not None:
            temp_model = main_models.UpdateHttpApiRouteRequestMcpRouteConfig()
            self.mcp_route_config = temp_model.from_map(m.get('mcpRouteConfig'))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class UpdateHttpApiRouteRequestMcpRouteConfig(DaraModel):
    def __init__(
        self,
        exposed_uri_path: str = None,
        mcp_statistics_enable: bool = None,
        protocol: str = None,
    ):
        self.exposed_uri_path = exposed_uri_path
        self.mcp_statistics_enable = mcp_statistics_enable
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

        if self.mcp_statistics_enable is not None:
            result['mcpStatisticsEnable'] = self.mcp_statistics_enable

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exposedUriPath') is not None:
            self.exposed_uri_path = m.get('exposedUriPath')

        if m.get('mcpStatisticsEnable') is not None:
            self.mcp_statistics_enable = m.get('mcpStatisticsEnable')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

class UpdateHttpApiRouteRequestBackendConfig(DaraModel):
    def __init__(
        self,
        scene: str = None,
        services: List[main_models.UpdateHttpApiRouteRequestBackendConfigServices] = None,
    ):
        # The backend service scenario.
        # 
        # Valid values:
        # 
        # *   SingleService
        # *   MultiServiceByRatio
        # *   Redirect
        # *   Mock
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
                temp_model = main_models.UpdateHttpApiRouteRequestBackendConfigServices()
                self.services.append(temp_model.from_map(k1))

        return self

class UpdateHttpApiRouteRequestBackendConfigServices(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
        service_id: str = None,
        version: str = None,
        weight: int = None,
    ):
        # The service port. If you want to use a dynamic port, do not pass this parameter.
        self.port = port
        # The protocol. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        self.protocol = protocol
        # The service ID.
        self.service_id = service_id
        # The service version.
        self.version = version
        # The percentage value of traffic.
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

