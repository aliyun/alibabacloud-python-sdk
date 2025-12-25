# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HttpApiApiInfo(DaraModel):
    def __init__(
        self,
        agent_protocols: List[str] = None,
        ai_protocols: List[str] = None,
        auth_config: main_models.AuthConfig = None,
        base_path: str = None,
        deploy_cnt_map: Dict[str, main_models.HttpApiApiInfoDeployCntMapValue] = None,
        deploy_configs: List[main_models.HttpApiDeployConfig] = None,
        description: str = None,
        enabel_auth: bool = None,
        environments: List[main_models.HttpApiApiInfoEnvironments] = None,
        gateway_id: str = None,
        http_api_id: str = None,
        ingress_info: main_models.HttpApiApiInfoIngressInfo = None,
        model_category: str = None,
        name: str = None,
        protocols: List[str] = None,
        resource_group_id: str = None,
        type: str = None,
        version_info: main_models.HttpApiVersionInfo = None,
    ):
        self.agent_protocols = agent_protocols
        self.ai_protocols = ai_protocols
        self.auth_config = auth_config
        self.base_path = base_path
        self.deploy_cnt_map = deploy_cnt_map
        self.deploy_configs = deploy_configs
        self.description = description
        self.enabel_auth = enabel_auth
        self.environments = environments
        self.gateway_id = gateway_id
        self.http_api_id = http_api_id
        self.ingress_info = ingress_info
        self.model_category = model_category
        self.name = name
        self.protocols = protocols
        self.resource_group_id = resource_group_id
        self.type = type
        self.version_info = version_info

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.deploy_cnt_map:
            for v1 in self.deploy_cnt_map.values():
                 if v1:
                    v1.validate()
        if self.deploy_configs:
            for v1 in self.deploy_configs:
                 if v1:
                    v1.validate()
        if self.environments:
            for v1 in self.environments:
                 if v1:
                    v1.validate()
        if self.ingress_info:
            self.ingress_info.validate()
        if self.version_info:
            self.version_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_protocols is not None:
            result['agentProtocols'] = self.agent_protocols

        if self.ai_protocols is not None:
            result['aiProtocols'] = self.ai_protocols

        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()

        if self.base_path is not None:
            result['basePath'] = self.base_path

        result['deployCntMap'] = {}
        if self.deploy_cnt_map is not None:
            for k1, v1 in self.deploy_cnt_map.items():
                result['deployCntMap'][k1] = v1.to_map() if v1 else None

        result['deployConfigs'] = []
        if self.deploy_configs is not None:
            for k1 in self.deploy_configs:
                result['deployConfigs'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        if self.enabel_auth is not None:
            result['enabelAuth'] = self.enabel_auth

        result['environments'] = []
        if self.environments is not None:
            for k1 in self.environments:
                result['environments'].append(k1.to_map() if k1 else None)

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.http_api_id is not None:
            result['httpApiId'] = self.http_api_id

        if self.ingress_info is not None:
            result['ingressInfo'] = self.ingress_info.to_map()

        if self.model_category is not None:
            result['modelCategory'] = self.model_category

        if self.name is not None:
            result['name'] = self.name

        if self.protocols is not None:
            result['protocols'] = self.protocols

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.type is not None:
            result['type'] = self.type

        if self.version_info is not None:
            result['versionInfo'] = self.version_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentProtocols') is not None:
            self.agent_protocols = m.get('agentProtocols')

        if m.get('aiProtocols') is not None:
            self.ai_protocols = m.get('aiProtocols')

        if m.get('authConfig') is not None:
            temp_model = main_models.AuthConfig()
            self.auth_config = temp_model.from_map(m.get('authConfig'))

        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')

        self.deploy_cnt_map = {}
        if m.get('deployCntMap') is not None:
            for k1, v1 in m.get('deployCntMap').items():
                temp_model = main_models.HttpApiApiInfoDeployCntMapValue()
                self.deploy_cnt_map[k1] = temp_model.from_map(v1)

        self.deploy_configs = []
        if m.get('deployConfigs') is not None:
            for k1 in m.get('deployConfigs'):
                temp_model = main_models.HttpApiDeployConfig()
                self.deploy_configs.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enabelAuth') is not None:
            self.enabel_auth = m.get('enabelAuth')

        self.environments = []
        if m.get('environments') is not None:
            for k1 in m.get('environments'):
                temp_model = main_models.HttpApiApiInfoEnvironments()
                self.environments.append(temp_model.from_map(k1))

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('httpApiId') is not None:
            self.http_api_id = m.get('httpApiId')

        if m.get('ingressInfo') is not None:
            temp_model = main_models.HttpApiApiInfoIngressInfo()
            self.ingress_info = temp_model.from_map(m.get('ingressInfo'))

        if m.get('modelCategory') is not None:
            self.model_category = m.get('modelCategory')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('protocols') is not None:
            self.protocols = m.get('protocols')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('versionInfo') is not None:
            temp_model = main_models.HttpApiVersionInfo()
            self.version_info = temp_model.from_map(m.get('versionInfo'))

        return self

class HttpApiApiInfoIngressInfo(DaraModel):
    def __init__(
        self,
        environment_info: main_models.HttpApiApiInfoIngressInfoEnvironmentInfo = None,
        ingress_class: str = None,
        k_8s_cluster_info: main_models.HttpApiApiInfoIngressInfoK8sClusterInfo = None,
        override_ingress_ip: bool = None,
        source_id: str = None,
        watch_namespace: str = None,
    ):
        self.environment_info = environment_info
        self.ingress_class = ingress_class
        self.k_8s_cluster_info = k_8s_cluster_info
        self.override_ingress_ip = override_ingress_ip
        self.source_id = source_id
        self.watch_namespace = watch_namespace

    def validate(self):
        if self.environment_info:
            self.environment_info.validate()
        if self.k_8s_cluster_info:
            self.k_8s_cluster_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment_info is not None:
            result['environmentInfo'] = self.environment_info.to_map()

        if self.ingress_class is not None:
            result['ingressClass'] = self.ingress_class

        if self.k_8s_cluster_info is not None:
            result['k8sClusterInfo'] = self.k_8s_cluster_info.to_map()

        if self.override_ingress_ip is not None:
            result['overrideIngressIp'] = self.override_ingress_ip

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.watch_namespace is not None:
            result['watchNamespace'] = self.watch_namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentInfo') is not None:
            temp_model = main_models.HttpApiApiInfoIngressInfoEnvironmentInfo()
            self.environment_info = temp_model.from_map(m.get('environmentInfo'))

        if m.get('ingressClass') is not None:
            self.ingress_class = m.get('ingressClass')

        if m.get('k8sClusterInfo') is not None:
            temp_model = main_models.HttpApiApiInfoIngressInfoK8sClusterInfo()
            self.k_8s_cluster_info = temp_model.from_map(m.get('k8sClusterInfo'))

        if m.get('overrideIngressIp') is not None:
            self.override_ingress_ip = m.get('overrideIngressIp')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('watchNamespace') is not None:
            self.watch_namespace = m.get('watchNamespace')

        return self

class HttpApiApiInfoIngressInfoK8sClusterInfo(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        return self

class HttpApiApiInfoIngressInfoEnvironmentInfo(DaraModel):
    def __init__(
        self,
        environment_id: str = None,
    ):
        self.environment_id = environment_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        return self

class HttpApiApiInfoEnvironments(DaraModel):
    def __init__(
        self,
        alias: str = None,
        backend_scene: str = None,
        backend_type: str = None,
        custom_domains: List[main_models.HttpApiDomainInfo] = None,
        deploy_status: str = None,
        environment_id: str = None,
        gateway_info: main_models.HttpApiApiInfoEnvironmentsGatewayInfo = None,
        name: str = None,
        service_configs: List[main_models.HttpApiApiInfoEnvironmentsServiceConfigs] = None,
        sub_domains: List[main_models.HttpApiApiInfoEnvironmentsSubDomains] = None,
    ):
        self.alias = alias
        self.backend_scene = backend_scene
        self.backend_type = backend_type
        self.custom_domains = custom_domains
        self.deploy_status = deploy_status
        self.environment_id = environment_id
        self.gateway_info = gateway_info
        self.name = name
        self.service_configs = service_configs
        self.sub_domains = sub_domains

    def validate(self):
        if self.custom_domains:
            for v1 in self.custom_domains:
                 if v1:
                    v1.validate()
        if self.gateway_info:
            self.gateway_info.validate()
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
        if self.alias is not None:
            result['alias'] = self.alias

        if self.backend_scene is not None:
            result['backendScene'] = self.backend_scene

        if self.backend_type is not None:
            result['backendType'] = self.backend_type

        result['customDomains'] = []
        if self.custom_domains is not None:
            for k1 in self.custom_domains:
                result['customDomains'].append(k1.to_map() if k1 else None)

        if self.deploy_status is not None:
            result['deployStatus'] = self.deploy_status

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()

        if self.name is not None:
            result['name'] = self.name

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
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('backendScene') is not None:
            self.backend_scene = m.get('backendScene')

        if m.get('backendType') is not None:
            self.backend_type = m.get('backendType')

        self.custom_domains = []
        if m.get('customDomains') is not None:
            for k1 in m.get('customDomains'):
                temp_model = main_models.HttpApiDomainInfo()
                self.custom_domains.append(temp_model.from_map(k1))

        if m.get('deployStatus') is not None:
            self.deploy_status = m.get('deployStatus')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayInfo') is not None:
            temp_model = main_models.HttpApiApiInfoEnvironmentsGatewayInfo()
            self.gateway_info = temp_model.from_map(m.get('gatewayInfo'))

        if m.get('name') is not None:
            self.name = m.get('name')

        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k1 in m.get('serviceConfigs'):
                temp_model = main_models.HttpApiApiInfoEnvironmentsServiceConfigs()
                self.service_configs.append(temp_model.from_map(k1))

        self.sub_domains = []
        if m.get('subDomains') is not None:
            for k1 in m.get('subDomains'):
                temp_model = main_models.HttpApiApiInfoEnvironmentsSubDomains()
                self.sub_domains.append(temp_model.from_map(k1))

        return self

class HttpApiApiInfoEnvironmentsSubDomains(DaraModel):
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

class HttpApiApiInfoEnvironmentsServiceConfigs(DaraModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        match: main_models.HttpApiBackendMatchConditions = None,
        name: str = None,
        port: str = None,
        protocol: str = None,
        service_id: str = None,
        version: str = None,
        weight: int = None,
    ):
        self.gateway_service_id = gateway_service_id
        self.match = match
        self.name = name
        self.port = port
        self.protocol = protocol
        self.service_id = service_id
        self.version = version
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_service_id is not None:
            result['gatewayServiceId'] = self.gateway_service_id

        if self.match is not None:
            result['match'] = self.match.to_map()

        if self.name is not None:
            result['name'] = self.name

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

        if m.get('match') is not None:
            temp_model = main_models.HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m.get('match'))

        if m.get('name') is not None:
            self.name = m.get('name')

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

class HttpApiApiInfoEnvironmentsGatewayInfo(DaraModel):
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

