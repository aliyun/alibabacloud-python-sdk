# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HttpApiDeployConfig(DaraModel):
    def __init__(
        self,
        auto_deploy: bool = None,
        backend_scene: str = None,
        builtin_route_names: List[str] = None,
        custom_domain_ids: List[str] = None,
        custom_domain_infos: List[main_models.HttpApiDeployConfigCustomDomainInfos] = None,
        environment_id: str = None,
        gateway_id: str = None,
        gateway_info: main_models.GatewayInfo = None,
        gateway_type: str = None,
        mock: main_models.HttpApiMockContract = None,
        policy_configs: List[main_models.HttpApiPolicyConfigs] = None,
        route_backend: main_models.Backend = None,
        service_configs: List[main_models.HttpApiDeployConfigServiceConfigs] = None,
        sub_domains: List[main_models.HttpApiDeployConfigSubDomains] = None,
    ):
        # Specifies whether to enable automatic deployment.
        self.auto_deploy = auto_deploy
        # The publishing scenario.
        self.backend_scene = backend_scene
        self.builtin_route_names = builtin_route_names
        # The IDs of the custom domain names.
        self.custom_domain_ids = custom_domain_ids
        # The information about the custom domain names.
        self.custom_domain_infos = custom_domain_infos
        # The environment ID.
        self.environment_id = environment_id
        # The instance ID.
        self.gateway_id = gateway_id
        # The instance information.
        self.gateway_info = gateway_info
        # 网关类型
        self.gateway_type = gateway_type
        # The Mock settings.
        self.mock = mock
        # The policy configurations.
        self.policy_configs = policy_configs
        # routeBackend
        self.route_backend = route_backend
        # The service configurations.
        self.service_configs = service_configs
        # The information about the sub-domain names.
        self.sub_domains = sub_domains

    def validate(self):
        if self.custom_domain_infos:
            for v1 in self.custom_domain_infos:
                 if v1:
                    v1.validate()
        if self.gateway_info:
            self.gateway_info.validate()
        if self.mock:
            self.mock.validate()
        if self.policy_configs:
            for v1 in self.policy_configs:
                 if v1:
                    v1.validate()
        if self.route_backend:
            self.route_backend.validate()
        if self.service_configs:
            for v1 in self.service_configs:
                 if v1:
                    v1.validate()
        if self.sub_domains:
            for v1 in self.sub_domains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_deploy is not None:
            result['autoDeploy'] = self.auto_deploy

        if self.backend_scene is not None:
            result['backendScene'] = self.backend_scene

        if self.builtin_route_names is not None:
            result['builtinRouteNames'] = self.builtin_route_names

        if self.custom_domain_ids is not None:
            result['customDomainIds'] = self.custom_domain_ids

        result['customDomainInfos'] = []
        if self.custom_domain_infos is not None:
            for k1 in self.custom_domain_infos:
                result['customDomainInfos'].append(k1.to_map() if k1 else None)

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()

        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

        if self.mock is not None:
            result['mock'] = self.mock.to_map()

        result['policyConfigs'] = []
        if self.policy_configs is not None:
            for k1 in self.policy_configs:
                result['policyConfigs'].append(k1.to_map() if k1 else None)

        if self.route_backend is not None:
            result['routeBackend'] = self.route_backend.to_map()

        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k1 in self.service_configs:
                result['serviceConfigs'].append(k1.to_map() if k1 else None)

        result['subDomains'] = []
        if self.sub_domains is not None:
            for k1 in self.sub_domains:
                result['subDomains'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoDeploy') is not None:
            self.auto_deploy = m.get('autoDeploy')

        if m.get('backendScene') is not None:
            self.backend_scene = m.get('backendScene')

        if m.get('builtinRouteNames') is not None:
            self.builtin_route_names = m.get('builtinRouteNames')

        if m.get('customDomainIds') is not None:
            self.custom_domain_ids = m.get('customDomainIds')

        self.custom_domain_infos = []
        if m.get('customDomainInfos') is not None:
            for k1 in m.get('customDomainInfos'):
                temp_model = main_models.HttpApiDeployConfigCustomDomainInfos()
                self.custom_domain_infos.append(temp_model.from_map(k1))

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('gatewayInfo') is not None:
            temp_model = main_models.GatewayInfo()
            self.gateway_info = temp_model.from_map(m.get('gatewayInfo'))

        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

        if m.get('mock') is not None:
            temp_model = main_models.HttpApiMockContract()
            self.mock = temp_model.from_map(m.get('mock'))

        self.policy_configs = []
        if m.get('policyConfigs') is not None:
            for k1 in m.get('policyConfigs'):
                temp_model = main_models.HttpApiPolicyConfigs()
                self.policy_configs.append(temp_model.from_map(k1))

        if m.get('routeBackend') is not None:
            temp_model = main_models.Backend()
            self.route_backend = temp_model.from_map(m.get('routeBackend'))

        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k1 in m.get('serviceConfigs'):
                temp_model = main_models.HttpApiDeployConfigServiceConfigs()
                self.service_configs.append(temp_model.from_map(k1))

        self.sub_domains = []
        if m.get('subDomains') is not None:
            for k1 in m.get('subDomains'):
                temp_model = main_models.HttpApiDeployConfigSubDomains()
                self.sub_domains.append(temp_model.from_map(k1))

        return self

class HttpApiDeployConfigSubDomains(DaraModel):
    def __init__(
        self,
        domain_id: str = None,
        name: str = None,
        network_type: str = None,
        protocol: str = None,
    ):
        # The domain name ID.
        self.domain_id = domain_id
        # The domain name.
        self.name = name
        # The network type.
        self.network_type = network_type
        # The protocol.
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

class HttpApiDeployConfigServiceConfigs(DaraModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        intent_code: str = None,
        match: main_models.HttpApiBackendMatchConditions = None,
        model_name: str = None,
        model_name_pattern: str = None,
        multi_service_route_strategy: str = None,
        name: str = None,
        observability_route_config: main_models.HttpApiDeployConfigServiceConfigsObservabilityRouteConfig = None,
        port: int = None,
        protocol: str = None,
        service_id: str = None,
        version: str = None,
        weight: int = None,
    ):
        # Legacy gateway service ID for backward compatibility
        self.gateway_service_id = gateway_service_id
        # Intent classification code
        self.intent_code = intent_code
        # Match conditions
        self.match = match
        # The model name.
        self.model_name = model_name
        # The model name matching rule.
        self.model_name_pattern = model_name_pattern
        # Multi-service routing strategy type
        self.multi_service_route_strategy = multi_service_route_strategy
        # Service display name
        self.name = name
        # Observability metrics-based routing config
        self.observability_route_config = observability_route_config
        # Service port number
        self.port = port
        # Service protocol
        self.protocol = protocol
        # The service ID.
        self.service_id = service_id
        # Service version tag for tag-based routing scenarios
        self.version = version
        # The service weight.
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()
        if self.observability_route_config:
            self.observability_route_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_service_id is not None:
            result['gatewayServiceId'] = self.gateway_service_id

        if self.intent_code is not None:
            result['intentCode'] = self.intent_code

        if self.match is not None:
            result['match'] = self.match.to_map()

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.model_name_pattern is not None:
            result['modelNamePattern'] = self.model_name_pattern

        if self.multi_service_route_strategy is not None:
            result['multiServiceRouteStrategy'] = self.multi_service_route_strategy

        if self.name is not None:
            result['name'] = self.name

        if self.observability_route_config is not None:
            result['observabilityRouteConfig'] = self.observability_route_config.to_map()

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
        if m.get('gatewayServiceId') is not None:
            self.gateway_service_id = m.get('gatewayServiceId')

        if m.get('intentCode') is not None:
            self.intent_code = m.get('intentCode')

        if m.get('match') is not None:
            temp_model = main_models.HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m.get('match'))

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('modelNamePattern') is not None:
            self.model_name_pattern = m.get('modelNamePattern')

        if m.get('multiServiceRouteStrategy') is not None:
            self.multi_service_route_strategy = m.get('multiServiceRouteStrategy')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('observabilityRouteConfig') is not None:
            temp_model = main_models.HttpApiDeployConfigServiceConfigsObservabilityRouteConfig()
            self.observability_route_config = temp_model.from_map(m.get('observabilityRouteConfig'))

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

class HttpApiDeployConfigServiceConfigsObservabilityRouteConfig(DaraModel):
    def __init__(
        self,
        mode: str = None,
        queue_size: int = None,
        rate_limit: float = None,
    ):
        # Routing mode
        self.mode = mode
        # Queue size
        self.queue_size = queue_size
        # Max traffic ratio per single service
        self.rate_limit = rate_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['mode'] = self.mode

        if self.queue_size is not None:
            result['queueSize'] = self.queue_size

        if self.rate_limit is not None:
            result['rateLimit'] = self.rate_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('queueSize') is not None:
            self.queue_size = m.get('queueSize')

        if m.get('rateLimit') is not None:
            self.rate_limit = m.get('rateLimit')

        return self

class HttpApiDeployConfigCustomDomainInfos(DaraModel):
    def __init__(
        self,
        domain_id: str = None,
        name: str = None,
        protocol: str = None,
    ):
        # The domain name ID.
        self.domain_id = domain_id
        # The domain name.
        self.name = name
        # The protocol.
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

