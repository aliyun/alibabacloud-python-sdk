# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HttpApiPublishRevisionInfo(DaraModel):
    def __init__(
        self,
        backend_scene: str = None,
        backend_type: str = None,
        cloud_product_config: main_models.HttpApiPublishRevisionInfoCloudProductConfig = None,
        create_timestamp: int = None,
        custom_domains: List[main_models.HttpApiDomainInfo] = None,
        dns_configs: List[main_models.HttpApiPublishRevisionInfoDnsConfigs] = None,
        environment_info: main_models.HttpApiPublishRevisionInfoEnvironmentInfo = None,
        is_current_version: bool = None,
        operations: List[main_models.HttpApiOperationInfo] = None,
        revision_id: str = None,
        service_configs: List[main_models.HttpApiPublishRevisionInfoServiceConfigs] = None,
        sub_domains: List[main_models.HttpApiDomainInfo] = None,
        vip_configs: List[main_models.HttpApiPublishRevisionInfoVipConfigs] = None,
    ):
        self.backend_scene = backend_scene
        self.backend_type = backend_type
        self.cloud_product_config = cloud_product_config
        self.create_timestamp = create_timestamp
        self.custom_domains = custom_domains
        self.dns_configs = dns_configs
        self.environment_info = environment_info
        self.is_current_version = is_current_version
        self.operations = operations
        self.revision_id = revision_id
        self.service_configs = service_configs
        self.sub_domains = sub_domains
        self.vip_configs = vip_configs

    def validate(self):
        if self.cloud_product_config:
            self.cloud_product_config.validate()
        if self.custom_domains:
            for v1 in self.custom_domains:
                 if v1:
                    v1.validate()
        if self.dns_configs:
            for v1 in self.dns_configs:
                 if v1:
                    v1.validate()
        if self.environment_info:
            self.environment_info.validate()
        if self.operations:
            for v1 in self.operations:
                 if v1:
                    v1.validate()
        if self.service_configs:
            for v1 in self.service_configs:
                 if v1:
                    v1.validate()
        if self.sub_domains:
            for v1 in self.sub_domains:
                 if v1:
                    v1.validate()
        if self.vip_configs:
            for v1 in self.vip_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_scene is not None:
            result['backendScene'] = self.backend_scene

        if self.backend_type is not None:
            result['backendType'] = self.backend_type

        if self.cloud_product_config is not None:
            result['cloudProductConfig'] = self.cloud_product_config.to_map()

        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp

        result['customDomains'] = []
        if self.custom_domains is not None:
            for k1 in self.custom_domains:
                result['customDomains'].append(k1.to_map() if k1 else None)

        result['dnsConfigs'] = []
        if self.dns_configs is not None:
            for k1 in self.dns_configs:
                result['dnsConfigs'].append(k1.to_map() if k1 else None)

        if self.environment_info is not None:
            result['environmentInfo'] = self.environment_info.to_map()

        if self.is_current_version is not None:
            result['isCurrentVersion'] = self.is_current_version

        result['operations'] = []
        if self.operations is not None:
            for k1 in self.operations:
                result['operations'].append(k1.to_map() if k1 else None)

        if self.revision_id is not None:
            result['revisionId'] = self.revision_id

        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k1 in self.service_configs:
                result['serviceConfigs'].append(k1.to_map() if k1 else None)

        result['subDomains'] = []
        if self.sub_domains is not None:
            for k1 in self.sub_domains:
                result['subDomains'].append(k1.to_map() if k1 else None)

        result['vipConfigs'] = []
        if self.vip_configs is not None:
            for k1 in self.vip_configs:
                result['vipConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backendScene') is not None:
            self.backend_scene = m.get('backendScene')

        if m.get('backendType') is not None:
            self.backend_type = m.get('backendType')

        if m.get('cloudProductConfig') is not None:
            temp_model = main_models.HttpApiPublishRevisionInfoCloudProductConfig()
            self.cloud_product_config = temp_model.from_map(m.get('cloudProductConfig'))

        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')

        self.custom_domains = []
        if m.get('customDomains') is not None:
            for k1 in m.get('customDomains'):
                temp_model = main_models.HttpApiDomainInfo()
                self.custom_domains.append(temp_model.from_map(k1))

        self.dns_configs = []
        if m.get('dnsConfigs') is not None:
            for k1 in m.get('dnsConfigs'):
                temp_model = main_models.HttpApiPublishRevisionInfoDnsConfigs()
                self.dns_configs.append(temp_model.from_map(k1))

        if m.get('environmentInfo') is not None:
            temp_model = main_models.HttpApiPublishRevisionInfoEnvironmentInfo()
            self.environment_info = temp_model.from_map(m.get('environmentInfo'))

        if m.get('isCurrentVersion') is not None:
            self.is_current_version = m.get('isCurrentVersion')

        self.operations = []
        if m.get('operations') is not None:
            for k1 in m.get('operations'):
                temp_model = main_models.HttpApiOperationInfo()
                self.operations.append(temp_model.from_map(k1))

        if m.get('revisionId') is not None:
            self.revision_id = m.get('revisionId')

        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k1 in m.get('serviceConfigs'):
                temp_model = main_models.HttpApiPublishRevisionInfoServiceConfigs()
                self.service_configs.append(temp_model.from_map(k1))

        self.sub_domains = []
        if m.get('subDomains') is not None:
            for k1 in m.get('subDomains'):
                temp_model = main_models.HttpApiDomainInfo()
                self.sub_domains.append(temp_model.from_map(k1))

        self.vip_configs = []
        if m.get('vipConfigs') is not None:
            for k1 in m.get('vipConfigs'):
                temp_model = main_models.HttpApiPublishRevisionInfoVipConfigs()
                self.vip_configs.append(temp_model.from_map(k1))

        return self

class HttpApiPublishRevisionInfoVipConfigs(DaraModel):
    def __init__(
        self,
        endpoints: List[str] = None,
        match: main_models.HttpApiBackendMatchConditions = None,
        weight: int = None,
    ):
        self.endpoints = endpoints
        self.match = match
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoints is not None:
            result['endpoints'] = self.endpoints

        if self.match is not None:
            result['match'] = self.match.to_map()

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoints') is not None:
            self.endpoints = m.get('endpoints')

        if m.get('match') is not None:
            temp_model = main_models.HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m.get('match'))

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class HttpApiPublishRevisionInfoServiceConfigs(DaraModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        match: main_models.HttpApiBackendMatchConditions = None,
        port: int = None,
        protocol: str = None,
        version: str = None,
        weight: int = None,
    ):
        self.gateway_service_id = gateway_service_id
        self.match = match
        self.port = port
        self.protocol = protocol
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

        if self.port is not None:
            result['port'] = self.port

        if self.protocol is not None:
            result['protocol'] = self.protocol

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

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class HttpApiPublishRevisionInfoEnvironmentInfo(DaraModel):
    def __init__(
        self,
        alias: str = None,
        environment_id: str = None,
        gateway_info: main_models.HttpApiPublishRevisionInfoEnvironmentInfoGatewayInfo = None,
        name: str = None,
    ):
        self.alias = alias
        self.environment_id = environment_id
        self.gateway_info = gateway_info
        self.name = name

    def validate(self):
        if self.gateway_info:
            self.gateway_info.validate()

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayInfo') is not None:
            temp_model = main_models.HttpApiPublishRevisionInfoEnvironmentInfoGatewayInfo()
            self.gateway_info = temp_model.from_map(m.get('gatewayInfo'))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class HttpApiPublishRevisionInfoEnvironmentInfoGatewayInfo(DaraModel):
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

class HttpApiPublishRevisionInfoDnsConfigs(DaraModel):
    def __init__(
        self,
        dns_list: List[str] = None,
        match: main_models.HttpApiBackendMatchConditions = None,
        weight: int = None,
    ):
        self.dns_list = dns_list
        self.match = match
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_list is not None:
            result['dnsList'] = self.dns_list

        if self.match is not None:
            result['match'] = self.match.to_map()

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dnsList') is not None:
            self.dns_list = m.get('dnsList')

        if m.get('match') is not None:
            temp_model = main_models.HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m.get('match'))

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class HttpApiPublishRevisionInfoCloudProductConfig(DaraModel):
    def __init__(
        self,
        cloud_product_type: str = None,
        container_service_configs: List[main_models.HttpApiPublishRevisionInfoCloudProductConfigContainerServiceConfigs] = None,
        function_configs: List[main_models.HttpApiPublishRevisionInfoCloudProductConfigFunctionConfigs] = None,
        mse_nacos_configs: List[main_models.HttpApiPublishRevisionInfoCloudProductConfigMseNacosConfigs] = None,
    ):
        self.cloud_product_type = cloud_product_type
        self.container_service_configs = container_service_configs
        self.function_configs = function_configs
        self.mse_nacos_configs = mse_nacos_configs

    def validate(self):
        if self.container_service_configs:
            for v1 in self.container_service_configs:
                 if v1:
                    v1.validate()
        if self.function_configs:
            for v1 in self.function_configs:
                 if v1:
                    v1.validate()
        if self.mse_nacos_configs:
            for v1 in self.mse_nacos_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_product_type is not None:
            result['cloudProductType'] = self.cloud_product_type

        result['containerServiceConfigs'] = []
        if self.container_service_configs is not None:
            for k1 in self.container_service_configs:
                result['containerServiceConfigs'].append(k1.to_map() if k1 else None)

        result['functionConfigs'] = []
        if self.function_configs is not None:
            for k1 in self.function_configs:
                result['functionConfigs'].append(k1.to_map() if k1 else None)

        result['mseNacosConfigs'] = []
        if self.mse_nacos_configs is not None:
            for k1 in self.mse_nacos_configs:
                result['mseNacosConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cloudProductType') is not None:
            self.cloud_product_type = m.get('cloudProductType')

        self.container_service_configs = []
        if m.get('containerServiceConfigs') is not None:
            for k1 in m.get('containerServiceConfigs'):
                temp_model = main_models.HttpApiPublishRevisionInfoCloudProductConfigContainerServiceConfigs()
                self.container_service_configs.append(temp_model.from_map(k1))

        self.function_configs = []
        if m.get('functionConfigs') is not None:
            for k1 in m.get('functionConfigs'):
                temp_model = main_models.HttpApiPublishRevisionInfoCloudProductConfigFunctionConfigs()
                self.function_configs.append(temp_model.from_map(k1))

        self.mse_nacos_configs = []
        if m.get('mseNacosConfigs') is not None:
            for k1 in m.get('mseNacosConfigs'):
                temp_model = main_models.HttpApiPublishRevisionInfoCloudProductConfigMseNacosConfigs()
                self.mse_nacos_configs.append(temp_model.from_map(k1))

        return self

class HttpApiPublishRevisionInfoCloudProductConfigMseNacosConfigs(DaraModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        group_name: str = None,
        match: main_models.HttpApiBackendMatchConditions = None,
        name: str = None,
        namespace: str = None,
        weight: int = None,
    ):
        self.gateway_service_id = gateway_service_id
        self.group_name = group_name
        self.match = match
        self.name = name
        self.namespace = namespace
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

        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.match is not None:
            result['match'] = self.match.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayServiceId') is not None:
            self.gateway_service_id = m.get('gatewayServiceId')

        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('match') is not None:
            temp_model = main_models.HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m.get('match'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class HttpApiPublishRevisionInfoCloudProductConfigFunctionConfigs(DaraModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        match: main_models.HttpApiBackendMatchConditions = None,
        name: str = None,
        qualifier: str = None,
        weight: int = None,
    ):
        self.gateway_service_id = gateway_service_id
        self.match = match
        self.name = name
        self.qualifier = qualifier
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

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

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

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class HttpApiPublishRevisionInfoCloudProductConfigContainerServiceConfigs(DaraModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        match: main_models.HttpApiBackendMatchConditions = None,
        name: str = None,
        namespace: str = None,
        port: int = None,
        protocol: str = None,
        weight: str = None,
    ):
        self.gateway_service_id = gateway_service_id
        self.match = match
        self.name = name
        self.namespace = namespace
        self.port = port
        self.protocol = protocol
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

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.port is not None:
            result['port'] = self.port

        if self.protocol is not None:
            result['protocol'] = self.protocol

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

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

