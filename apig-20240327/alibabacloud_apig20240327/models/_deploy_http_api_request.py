# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class DeployHttpApiRequest(DaraModel):
    def __init__(
        self,
        http_api_config: main_models.DeployHttpApiRequestHttpApiConfig = None,
        rest_api_config: main_models.DeployHttpApiRequestRestApiConfig = None,
        route_id: str = None,
    ):
        self.http_api_config = http_api_config
        # Rest API deployment configuration. Required when deploying an HTTP API as a Rest API.
        self.rest_api_config = rest_api_config
        # Route ID. This must be provided when publishing the route of an HTTP API.
        self.route_id = route_id

    def validate(self):
        if self.http_api_config:
            self.http_api_config.validate()
        if self.rest_api_config:
            self.rest_api_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_api_config is not None:
            result['httpApiConfig'] = self.http_api_config.to_map()

        if self.rest_api_config is not None:
            result['restApiConfig'] = self.rest_api_config.to_map()

        if self.route_id is not None:
            result['routeId'] = self.route_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('httpApiConfig') is not None:
            temp_model = main_models.DeployHttpApiRequestHttpApiConfig()
            self.http_api_config = temp_model.from_map(m.get('httpApiConfig'))

        if m.get('restApiConfig') is not None:
            temp_model = main_models.DeployHttpApiRequestRestApiConfig()
            self.rest_api_config = temp_model.from_map(m.get('restApiConfig'))

        if m.get('routeId') is not None:
            self.route_id = m.get('routeId')

        return self

class DeployHttpApiRequestRestApiConfig(DaraModel):
    def __init__(
        self,
        description: str = None,
        environment: main_models.DeployHttpApiRequestRestApiConfigEnvironment = None,
        gateway_id: str = None,
        operation_ids: List[str] = None,
        revision_id: str = None,
    ):
        # Publication description.
        self.description = description
        # Publication environment configuration.
        self.environment = environment
        self.gateway_id = gateway_id
        self.operation_ids = operation_ids
        # Historical version number. If this field is specified, the publication information will be based on the historical version information.
        self.revision_id = revision_id

    def validate(self):
        if self.environment:
            self.environment.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.environment is not None:
            result['environment'] = self.environment.to_map()

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.operation_ids is not None:
            result['operationIds'] = self.operation_ids

        if self.revision_id is not None:
            result['revisionId'] = self.revision_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('environment') is not None:
            temp_model = main_models.DeployHttpApiRequestRestApiConfigEnvironment()
            self.environment = temp_model.from_map(m.get('environment'))

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('operationIds') is not None:
            self.operation_ids = m.get('operationIds')

        if m.get('revisionId') is not None:
            self.revision_id = m.get('revisionId')

        return self

class DeployHttpApiRequestRestApiConfigEnvironment(DaraModel):
    def __init__(
        self,
        backend_scene: str = None,
        custom_domain_ids: List[str] = None,
        environment_id: str = None,
        service_configs: List[main_models.DeployHttpApiRequestRestApiConfigEnvironmentServiceConfigs] = None,
    ):
        # API publication scenario.
        self.backend_scene = backend_scene
        # List of user domains.
        self.custom_domain_ids = custom_domain_ids
        # Environment ID.
        self.environment_id = environment_id
        # Existing service configurations. Only one entry is allowed in a single-service scenario, while multiple entries are allowed in scenarios such as by ratio or by content.
        self.service_configs = service_configs

    def validate(self):
        if self.service_configs:
            for v1 in self.service_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_scene is not None:
            result['backendScene'] = self.backend_scene

        if self.custom_domain_ids is not None:
            result['customDomainIds'] = self.custom_domain_ids

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k1 in self.service_configs:
                result['serviceConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backendScene') is not None:
            self.backend_scene = m.get('backendScene')

        if m.get('customDomainIds') is not None:
            self.custom_domain_ids = m.get('customDomainIds')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k1 in m.get('serviceConfigs'):
                temp_model = main_models.DeployHttpApiRequestRestApiConfigEnvironmentServiceConfigs()
                self.service_configs.append(temp_model.from_map(k1))

        return self

class DeployHttpApiRequestRestApiConfigEnvironmentServiceConfigs(DaraModel):
    def __init__(
        self,
        match: main_models.HttpApiBackendMatchConditions = None,
        port: int = None,
        protocol: str = None,
        service_id: str = None,
        version: str = None,
        weight: int = None,
    ):
        # Configuration of matching conditions related to API deployment.
        self.match = match
        # Service port, do not provide for dynamic ports.
        self.port = port
        # Service protocol:
        # - HTTP.
        # - HTTPS.
        self.protocol = protocol
        # Service ID.
        self.service_id = service_id
        # Service version.
        self.version = version
        # Weight, range [1,100], valid only in the by-ratio scenario.
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match is not None:
            result['match'] = self.match.to_map()

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
        if m.get('match') is not None:
            temp_model = main_models.HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m.get('match'))

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

class DeployHttpApiRequestHttpApiConfig(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        route_ids: List[str] = None,
    ):
        self.gateway_id = gateway_id
        self.route_ids = route_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.route_ids is not None:
            result['routeIds'] = self.route_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('routeIds') is not None:
            self.route_ids = m.get('routeIds')

        return self

