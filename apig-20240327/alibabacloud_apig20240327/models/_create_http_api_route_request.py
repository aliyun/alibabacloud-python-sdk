# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class CreateHttpApiRouteRequest(DaraModel):
    def __init__(
        self,
        backend_config: main_models.CreateHttpApiRouteRequestBackendConfig = None,
        deploy_configs: List[main_models.HttpApiDeployConfig] = None,
        description: str = None,
        domain_ids: List[str] = None,
        environment_id: str = None,
        match: main_models.HttpRouteMatch = None,
        mcp_route_config: main_models.CreateHttpApiRouteRequestMcpRouteConfig = None,
        name: str = None,
        policy_configs: List[main_models.HttpApiPolicyConfigs] = None,
    ):
        # The backend service configuration of the route.
        self.backend_config = backend_config
        # The API deployment configuration.
        self.deploy_configs = deploy_configs
        # The route description.
        self.description = description
        # The domain name IDs.
        self.domain_ids = domain_ids
        # The environment ID.
        self.environment_id = environment_id
        # The route match rule.
        self.match = match
        # The MCP route configuration.
        self.mcp_route_config = mcp_route_config
        # The route name.
        self.name = name
        # The policy type.
        self.policy_configs = policy_configs

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
        if self.policy_configs:
            for v1 in self.policy_configs:
                 if v1:
                    v1.validate()

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

        result['policyConfigs'] = []
        if self.policy_configs is not None:
            for k1 in self.policy_configs:
                result['policyConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backendConfig') is not None:
            temp_model = main_models.CreateHttpApiRouteRequestBackendConfig()
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
            temp_model = main_models.CreateHttpApiRouteRequestMcpRouteConfig()
            self.mcp_route_config = temp_model.from_map(m.get('mcpRouteConfig'))

        if m.get('name') is not None:
            self.name = m.get('name')

        self.policy_configs = []
        if m.get('policyConfigs') is not None:
            for k1 in m.get('policyConfigs'):
                temp_model = main_models.HttpApiPolicyConfigs()
                self.policy_configs.append(temp_model.from_map(k1))

        return self

class CreateHttpApiRouteRequestMcpRouteConfig(DaraModel):
    def __init__(
        self,
        exposed_uri_path: str = None,
        mcp_statistics_enable: bool = None,
        protocol: str = None,
    ):
        # The exposed URI path.
        self.exposed_uri_path = exposed_uri_path
        # Specifies whether to enable MCP observability. Default value: false.
        self.mcp_statistics_enable = mcp_statistics_enable
        # The service protocol. Valid values:
        # - TCP.
        # - HTTP.
        # - DUBBO.
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

class CreateHttpApiRouteRequestBackendConfig(DaraModel):
    def __init__(
        self,
        scene: str = None,
        services: List[main_models.CreateHttpApiRouteRequestBackendConfigServices] = None,
    ):
        # The backend service scenario. Valid values:
        # - SingleService: single service.
        # - MultiServiceByRatio: multiple services with ratio-based canary release.
        # - Mock: mock service.
        # - Redirect: redirect service.
        self.scene = scene
        # The list of backend services.
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
                temp_model = main_models.CreateHttpApiRouteRequestBackendConfigServices()
                self.services.append(temp_model.from_map(k1))

        return self

class CreateHttpApiRouteRequestBackendConfigServices(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        http_dubbo_transcoder: main_models.HttpDubboTranscoder = None,
        model_name: str = None,
        namespace: str = None,
        port: int = None,
        protocol: str = None,
        service_id: str = None,
        source_type: str = None,
        version: str = None,
        weight: int = None,
    ):
        # The service group. Used in the HTTP-to-Dubbo conversion scenario.
        self.group_name = group_name
        # The HTTP-to-Dubbo protocol conversion configuration. Only supported for SingleService MSE_NACOS DUBBO backends of HTTP APIs.
        self.http_dubbo_transcoder = http_dubbo_transcoder
        # The target model name. This field is shared by multiple model backend scenarios. The specific routing or model rewrite semantics are determined by backendConfig.scene. This field is required for the SemanticRouter scenario. If not specified in the AiAutoRouter scenario, the default model of the AI service is used.
        self.model_name = model_name
        # The service namespace. Used in the HTTP-to-Dubbo conversion scenario.
        self.namespace = namespace
        # The service port. Do not specify this parameter for dynamic ports.
        self.port = port
        # The service protocol. Valid values:
        # - HTTP.
        # - HTTPS.
        self.protocol = protocol
        # The service ID.
        self.service_id = service_id
        # The service source type. Used in the HTTP-to-Dubbo conversion scenario.
        self.source_type = source_type
        # The service version. This parameter is valid only in the tag-based scenario.
        self.version = version
        # The traffic ratio percentage value.
        self.weight = weight

    def validate(self):
        if self.http_dubbo_transcoder:
            self.http_dubbo_transcoder.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.http_dubbo_transcoder is not None:
            result['httpDubboTranscoder'] = self.http_dubbo_transcoder.to_map()

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.port is not None:
            result['port'] = self.port

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.version is not None:
            result['version'] = self.version

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('httpDubboTranscoder') is not None:
            temp_model = main_models.HttpDubboTranscoder()
            self.http_dubbo_transcoder = temp_model.from_map(m.get('httpDubboTranscoder'))

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

