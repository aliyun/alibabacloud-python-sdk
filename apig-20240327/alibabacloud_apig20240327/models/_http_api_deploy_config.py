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
        custom_domain_ids: List[str] = None,
        custom_domain_infos: List[main_models.HttpApiDeployConfigCustomDomainInfos] = None,
        environment_id: str = None,
        gateway_id: str = None,
        gateway_info: main_models.GatewayInfo = None,
        gateway_type: str = None,
        mock: main_models.HttpApiMockContract = None,
        policy_configs: List[main_models.HttpApiDeployConfigPolicyConfigs] = None,
        route_backend: main_models.Backend = None,
        service_configs: List[main_models.HttpApiDeployConfigServiceConfigs] = None,
        sub_domains: List[main_models.HttpApiDeployConfigSubDomains] = None,
    ):
        self.auto_deploy = auto_deploy
        self.backend_scene = backend_scene
        self.custom_domain_ids = custom_domain_ids
        self.custom_domain_infos = custom_domain_infos
        self.environment_id = environment_id
        self.gateway_id = gateway_id
        self.gateway_info = gateway_info
        self.gateway_type = gateway_type
        self.mock = mock
        self.policy_configs = policy_configs
        self.route_backend = route_backend
        self.service_configs = service_configs
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
                temp_model = main_models.HttpApiDeployConfigPolicyConfigs()
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

class HttpApiDeployConfigServiceConfigs(DaraModel):
    def __init__(
        self,
        intent_code: str = None,
        model_name: str = None,
        model_name_pattern: str = None,
        service_id: str = None,
        weight: int = None,
    ):
        self.intent_code = intent_code
        self.model_name = model_name
        self.model_name_pattern = model_name_pattern
        self.service_id = service_id
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.intent_code is not None:
            result['intentCode'] = self.intent_code

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.model_name_pattern is not None:
            result['modelNamePattern'] = self.model_name_pattern

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('intentCode') is not None:
            self.intent_code = m.get('intentCode')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('modelNamePattern') is not None:
            self.model_name_pattern = m.get('modelNamePattern')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class HttpApiDeployConfigPolicyConfigs(DaraModel):
    def __init__(
        self,
        ai_fallback_config: main_models.HttpApiDeployConfigPolicyConfigsAiFallbackConfig = None,
        enable: bool = None,
        type: str = None,
    ):
        self.ai_fallback_config = ai_fallback_config
        self.enable = enable
        self.type = type

    def validate(self):
        if self.ai_fallback_config:
            self.ai_fallback_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_fallback_config is not None:
            result['aiFallbackConfig'] = self.ai_fallback_config.to_map()

        if self.enable is not None:
            result['enable'] = self.enable

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiFallbackConfig') is not None:
            temp_model = main_models.HttpApiDeployConfigPolicyConfigsAiFallbackConfig()
            self.ai_fallback_config = temp_model.from_map(m.get('aiFallbackConfig'))

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class HttpApiDeployConfigPolicyConfigsAiFallbackConfig(DaraModel):
    def __init__(
        self,
        service_configs: List[main_models.HttpApiDeployConfigPolicyConfigsAiFallbackConfigServiceConfigs] = None,
    ):
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
        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k1 in self.service_configs:
                result['serviceConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k1 in m.get('serviceConfigs'):
                temp_model = main_models.HttpApiDeployConfigPolicyConfigsAiFallbackConfigServiceConfigs()
                self.service_configs.append(temp_model.from_map(k1))

        return self

class HttpApiDeployConfigPolicyConfigsAiFallbackConfigServiceConfigs(DaraModel):
    def __init__(
        self,
        service_id: str = None,
        target_model_name: str = None,
    ):
        self.service_id = service_id
        self.target_model_name = target_model_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.target_model_name is not None:
            result['targetModelName'] = self.target_model_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('targetModelName') is not None:
            self.target_model_name = m.get('targetModelName')

        return self

class HttpApiDeployConfigCustomDomainInfos(DaraModel):
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

