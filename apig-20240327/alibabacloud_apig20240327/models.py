# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class Attachment(TeaModel):
    def __init__(
        self,
        attach_resource_ids: List[str] = None,
        attach_resource_type: str = None,
        environment_id: str = None,
        gateway_id: str = None,
        policy_attachment_id: str = None,
    ):
        self.attach_resource_ids = attach_resource_ids
        self.attach_resource_type = attach_resource_type
        self.environment_id = environment_id
        self.gateway_id = gateway_id
        self.policy_attachment_id = policy_attachment_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_resource_ids is not None:
            result['attachResourceIds'] = self.attach_resource_ids
        if self.attach_resource_type is not None:
            result['attachResourceType'] = self.attach_resource_type
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.policy_attachment_id is not None:
            result['policyAttachmentId'] = self.policy_attachment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceIds') is not None:
            self.attach_resource_ids = m.get('attachResourceIds')
        if m.get('attachResourceType') is not None:
            self.attach_resource_type = m.get('attachResourceType')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('policyAttachmentId') is not None:
            self.policy_attachment_id = m.get('policyAttachmentId')
        return self


class CheckServiceLinkedRoleResult(TeaModel):
    def __init__(
        self,
        existed: bool = None,
    ):
        self.existed = existed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.existed is not None:
            result['existed'] = self.existed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('existed') is not None:
            self.existed = m.get('existed')
        return self


class DashboardFilter(TeaModel):
    def __init__(
        self,
        route_name: str = None,
    ):
        self.route_name = route_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.route_name is not None:
            result['routeName'] = self.route_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('routeName') is not None:
            self.route_name = m.get('routeName')
        return self


class DomainInfo(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
        create_from: str = None,
        create_timestamp: int = None,
        domain_id: str = None,
        force_https: bool = None,
        name: str = None,
        protocol: str = None,
        status: str = None,
        update_timestamp: int = None,
    ):
        self.cert_identifier = cert_identifier
        self.create_from = create_from
        self.create_timestamp = create_timestamp
        self.domain_id = domain_id
        self.force_https = force_https
        self.name = name
        self.protocol = protocol
        self.status = status
        self.update_timestamp = update_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['certIdentifier'] = self.cert_identifier
        if self.create_from is not None:
            result['createFrom'] = self.create_from
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.force_https is not None:
            result['forceHttps'] = self.force_https
        if self.name is not None:
            result['name'] = self.name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.status is not None:
            result['status'] = self.status
        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certIdentifier') is not None:
            self.cert_identifier = m.get('certIdentifier')
        if m.get('createFrom') is not None:
            self.create_from = m.get('createFrom')
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('forceHttps') is not None:
            self.force_https = m.get('forceHttps')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')
        return self


class GatewayInfo(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class SubDomainInfo(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class EnvironmentInfo(TeaModel):
    def __init__(
        self,
        alias: str = None,
        create_timestamp: int = None,
        default: bool = None,
        description: str = None,
        environment_id: str = None,
        gateway_info: GatewayInfo = None,
        name: str = None,
        sub_domain_infos: List[SubDomainInfo] = None,
        update_timestamp: int = None,
    ):
        self.alias = alias
        self.create_timestamp = create_timestamp
        self.default = default
        self.description = description
        self.environment_id = environment_id
        self.gateway_info = gateway_info
        self.name = name
        self.sub_domain_infos = sub_domain_infos
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.gateway_info:
            self.gateway_info.validate()
        if self.sub_domain_infos:
            for k in self.sub_domain_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        if self.default is not None:
            result['default'] = self.default
        if self.description is not None:
            result['description'] = self.description
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()
        if self.name is not None:
            result['name'] = self.name
        result['subDomainInfos'] = []
        if self.sub_domain_infos is not None:
            for k in self.sub_domain_infos:
                result['subDomainInfos'].append(k.to_map() if k else None)
        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        if m.get('default') is not None:
            self.default = m.get('default')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('gatewayInfo') is not None:
            temp_model = GatewayInfo()
            self.gateway_info = temp_model.from_map(m['gatewayInfo'])
        if m.get('name') is not None:
            self.name = m.get('name')
        self.sub_domain_infos = []
        if m.get('subDomainInfos') is not None:
            for k in m.get('subDomainInfos'):
                temp_model = SubDomainInfo()
                self.sub_domain_infos.append(temp_model.from_map(k))
        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')
        return self


class GatewayLogConfigSlsConfig(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        return self


class GatewayLogConfig(TeaModel):
    def __init__(
        self,
        sls_config: GatewayLogConfigSlsConfig = None,
    ):
        self.sls_config = sls_config

    def validate(self):
        if self.sls_config:
            self.sls_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sls_config is not None:
            result['slsConfig'] = self.sls_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('slsConfig') is not None:
            temp_model = GatewayLogConfigSlsConfig()
            self.sls_config = temp_model.from_map(m['slsConfig'])
        return self


class GatewayRouteBackendServices(TeaModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        name: str = None,
        port: int = None,
        protocol: str = None,
        version: str = None,
        weight: float = None,
    ):
        self.gateway_service_id = gateway_service_id
        self.name = name
        self.port = port
        self.protocol = protocol
        self.version = version
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_service_id is not None:
            result['gatewayServiceId'] = self.gateway_service_id
        if self.name is not None:
            result['name'] = self.name
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
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class GatewayRouteBackend(TeaModel):
    def __init__(
        self,
        services: List[GatewayRouteBackendServices] = None,
        type: str = None,
    ):
        self.services = services
        self.type = type

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['services'] = []
        if self.services is not None:
            for k in self.services:
                result['services'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.services = []
        if m.get('services') is not None:
            for k in m.get('services'):
                temp_model = GatewayRouteBackendServices()
                self.services.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GatewayRouteBackendConfigServices(TeaModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        port: int = None,
        protocol: str = None,
        source_type: str = None,
        weight: float = None,
    ):
        self.gateway_service_id = gateway_service_id
        self.port = port
        self.protocol = protocol
        self.source_type = source_type
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_service_id is not None:
            result['gatewayServiceId'] = self.gateway_service_id
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayServiceId') is not None:
            self.gateway_service_id = m.get('gatewayServiceId')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class GatewayRouteBackendConfig(TeaModel):
    def __init__(
        self,
        services: List[GatewayRouteBackendConfigServices] = None,
        type: str = None,
    ):
        self.services = services
        self.type = type

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['services'] = []
        if self.services is not None:
            for k in self.services:
                result['services'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.services = []
        if m.get('services') is not None:
            for k in m.get('services'):
                temp_model = GatewayRouteBackendConfigServices()
                self.services.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GatewayRouteDomainConfig(TeaModel):
    def __init__(
        self,
        domain_ids: List[str] = None,
    ):
        self.domain_ids = domain_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_ids is not None:
            result['domainIds'] = self.domain_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainIds') is not None:
            self.domain_ids = m.get('domainIds')
        return self


class GatewayRouteDomainInfoDomains(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GatewayRouteDomainInfo(TeaModel):
    def __init__(
        self,
        domains: List[GatewayRouteDomainInfoDomains] = None,
    ):
        self.domains = domains

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['domains'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domains = []
        if m.get('domains') is not None:
            for k in m.get('domains'):
                temp_model = GatewayRouteDomainInfoDomains()
                self.domains.append(temp_model.from_map(k))
        return self


class GatewayServicePorts(TeaModel):
    def __init__(
        self,
        name: str = None,
        port: int = None,
        protocol: str = None,
    ):
        self.name = name
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class ServiceHealthCheck(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        healthy_threshold: int = None,
        http_host: str = None,
        http_path: str = None,
        interval: int = None,
        protocol: str = None,
        timeout: int = None,
        unhealthy_threshold: int = None,
    ):
        self.enable = enable
        self.healthy_threshold = healthy_threshold
        self.http_host = http_host
        self.http_path = http_path
        self.interval = interval
        self.protocol = protocol
        self.timeout = timeout
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.healthy_threshold is not None:
            result['healthyThreshold'] = self.healthy_threshold
        if self.http_host is not None:
            result['httpHost'] = self.http_host
        if self.http_path is not None:
            result['httpPath'] = self.http_path
        if self.interval is not None:
            result['interval'] = self.interval
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.unhealthy_threshold is not None:
            result['unhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('healthyThreshold') is not None:
            self.healthy_threshold = m.get('healthyThreshold')
        if m.get('httpHost') is not None:
            self.http_host = m.get('httpHost')
        if m.get('httpPath') is not None:
            self.http_path = m.get('httpPath')
        if m.get('interval') is not None:
            self.interval = m.get('interval')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('unhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('unhealthyThreshold')
        return self


class GatewayService(TeaModel):
    def __init__(
        self,
        addresses: List[str] = None,
        create_timestamp: int = None,
        gateway_service_id: str = None,
        health_check: ServiceHealthCheck = None,
        health_status: str = None,
        name: str = None,
        namespace: str = None,
        ports: List[GatewayServicePorts] = None,
        qualifier: str = None,
        source_type: str = None,
        unhealthy_endpoints: List[str] = None,
        update_timestamp: int = None,
    ):
        self.addresses = addresses
        self.create_timestamp = create_timestamp
        self.gateway_service_id = gateway_service_id
        self.health_check = health_check
        self.health_status = health_status
        self.name = name
        self.namespace = namespace
        self.ports = ports
        self.qualifier = qualifier
        self.source_type = source_type
        self.unhealthy_endpoints = unhealthy_endpoints
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.health_check:
            self.health_check.validate()
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['addresses'] = self.addresses
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        if self.gateway_service_id is not None:
            result['gatewayServiceId'] = self.gateway_service_id
        if self.health_check is not None:
            result['healthCheck'] = self.health_check.to_map()
        if self.health_status is not None:
            result['healthStatus'] = self.health_status
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        result['ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.unhealthy_endpoints is not None:
            result['unhealthyEndpoints'] = self.unhealthy_endpoints
        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addresses') is not None:
            self.addresses = m.get('addresses')
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        if m.get('gatewayServiceId') is not None:
            self.gateway_service_id = m.get('gatewayServiceId')
        if m.get('healthCheck') is not None:
            temp_model = ServiceHealthCheck()
            self.health_check = temp_model.from_map(m['healthCheck'])
        if m.get('healthStatus') is not None:
            self.health_status = m.get('healthStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        self.ports = []
        if m.get('ports') is not None:
            for k in m.get('ports'):
                temp_model = GatewayServicePorts()
                self.ports.append(temp_model.from_map(k))
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('unhealthyEndpoints') is not None:
            self.unhealthy_endpoints = m.get('unhealthyEndpoints')
        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')
        return self


class GatewayServiceSourceK8sServiceSourceInfoIngressConfig(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        ingress_class: str = None,
        override_ingress_ip: bool = None,
        watch_namespace: str = None,
    ):
        self.enable = enable
        self.ingress_class = ingress_class
        self.override_ingress_ip = override_ingress_ip
        self.watch_namespace = watch_namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.ingress_class is not None:
            result['ingressClass'] = self.ingress_class
        if self.override_ingress_ip is not None:
            result['overrideIngressIp'] = self.override_ingress_ip
        if self.watch_namespace is not None:
            result['watchNamespace'] = self.watch_namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('ingressClass') is not None:
            self.ingress_class = m.get('ingressClass')
        if m.get('overrideIngressIp') is not None:
            self.override_ingress_ip = m.get('overrideIngressIp')
        if m.get('watchNamespace') is not None:
            self.watch_namespace = m.get('watchNamespace')
        return self


class GatewayServiceSourceK8sServiceSourceInfo(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        ingress_config: GatewayServiceSourceK8sServiceSourceInfoIngressConfig = None,
    ):
        self.cluster_id = cluster_id
        self.ingress_config = ingress_config

    def validate(self):
        if self.ingress_config:
            self.ingress_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.ingress_config is not None:
            result['ingressConfig'] = self.ingress_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('ingressConfig') is not None:
            temp_model = GatewayServiceSourceK8sServiceSourceInfoIngressConfig()
            self.ingress_config = temp_model.from_map(m['ingressConfig'])
        return self


class GatewayServiceSourceNacosServiceSourceInfo(TeaModel):
    def __init__(
        self,
        address: str = None,
        cluster_id: str = None,
        instance_id: str = None,
    ):
        self.address = address
        self.cluster_id = cluster_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class GatewayServiceSource(TeaModel):
    def __init__(
        self,
        bound: bool = None,
        create_timestamp: int = None,
        k_8s_service_source_info: GatewayServiceSourceK8sServiceSourceInfo = None,
        nacos_service_source_info: GatewayServiceSourceNacosServiceSourceInfo = None,
        name: str = None,
        service_source_id: str = None,
        type: str = None,
        update_timestamp: int = None,
    ):
        self.bound = bound
        self.create_timestamp = create_timestamp
        self.k_8s_service_source_info = k_8s_service_source_info
        self.nacos_service_source_info = nacos_service_source_info
        self.name = name
        self.service_source_id = service_source_id
        self.type = type
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.k_8s_service_source_info:
            self.k_8s_service_source_info.validate()
        if self.nacos_service_source_info:
            self.nacos_service_source_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bound is not None:
            result['bound'] = self.bound
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        if self.k_8s_service_source_info is not None:
            result['k8sServiceSourceInfo'] = self.k_8s_service_source_info.to_map()
        if self.nacos_service_source_info is not None:
            result['nacosServiceSourceInfo'] = self.nacos_service_source_info.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.service_source_id is not None:
            result['serviceSourceId'] = self.service_source_id
        if self.type is not None:
            result['type'] = self.type
        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bound') is not None:
            self.bound = m.get('bound')
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        if m.get('k8sServiceSourceInfo') is not None:
            temp_model = GatewayServiceSourceK8sServiceSourceInfo()
            self.k_8s_service_source_info = temp_model.from_map(m['k8sServiceSourceInfo'])
        if m.get('nacosServiceSourceInfo') is not None:
            temp_model = GatewayServiceSourceNacosServiceSourceInfo()
            self.nacos_service_source_info = temp_model.from_map(m['nacosServiceSourceInfo'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('serviceSourceId') is not None:
            self.service_source_id = m.get('serviceSourceId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')
        return self


class HttpApiBackendMatchCondition(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        type: str = None,
        value: str = None,
    ):
        self.key = key
        self.operator = operator
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class HttpApiBackendMatchConditions(TeaModel):
    def __init__(
        self,
        conditions: List[HttpApiBackendMatchCondition] = None,
        default: bool = None,
    ):
        self.conditions = conditions
        self.default = default

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['conditions'].append(k.to_map() if k else None)
        if self.default is not None:
            result['default'] = self.default
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('conditions') is not None:
            for k in m.get('conditions'):
                temp_model = HttpApiBackendMatchCondition()
                self.conditions.append(temp_model.from_map(k))
        if m.get('default') is not None:
            self.default = m.get('default')
        return self


class HttpApiApiInfoEnvironmentsCloudProductConfigContainerServiceConfigs(TeaModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        match: HttpApiBackendMatchConditions = None,
        name: str = None,
        namespace: str = None,
        port: int = None,
        protocol: str = None,
        weight: int = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
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


class HttpApiApiInfoEnvironmentsCloudProductConfigFunctionConfigs(TeaModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        match: HttpApiBackendMatchConditions = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class HttpApiApiInfoEnvironmentsCloudProductConfigMseNacosConfigs(TeaModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        group_name: str = None,
        match: HttpApiBackendMatchConditions = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class HttpApiApiInfoEnvironmentsCloudProductConfig(TeaModel):
    def __init__(
        self,
        cloud_product_type: str = None,
        container_service_configs: List[HttpApiApiInfoEnvironmentsCloudProductConfigContainerServiceConfigs] = None,
        function_configs: List[HttpApiApiInfoEnvironmentsCloudProductConfigFunctionConfigs] = None,
        mse_nacos_configs: List[HttpApiApiInfoEnvironmentsCloudProductConfigMseNacosConfigs] = None,
    ):
        self.cloud_product_type = cloud_product_type
        self.container_service_configs = container_service_configs
        self.function_configs = function_configs
        self.mse_nacos_configs = mse_nacos_configs

    def validate(self):
        if self.container_service_configs:
            for k in self.container_service_configs:
                if k:
                    k.validate()
        if self.function_configs:
            for k in self.function_configs:
                if k:
                    k.validate()
        if self.mse_nacos_configs:
            for k in self.mse_nacos_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_product_type is not None:
            result['cloudProductType'] = self.cloud_product_type
        result['containerServiceConfigs'] = []
        if self.container_service_configs is not None:
            for k in self.container_service_configs:
                result['containerServiceConfigs'].append(k.to_map() if k else None)
        result['functionConfigs'] = []
        if self.function_configs is not None:
            for k in self.function_configs:
                result['functionConfigs'].append(k.to_map() if k else None)
        result['mseNacosConfigs'] = []
        if self.mse_nacos_configs is not None:
            for k in self.mse_nacos_configs:
                result['mseNacosConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cloudProductType') is not None:
            self.cloud_product_type = m.get('cloudProductType')
        self.container_service_configs = []
        if m.get('containerServiceConfigs') is not None:
            for k in m.get('containerServiceConfigs'):
                temp_model = HttpApiApiInfoEnvironmentsCloudProductConfigContainerServiceConfigs()
                self.container_service_configs.append(temp_model.from_map(k))
        self.function_configs = []
        if m.get('functionConfigs') is not None:
            for k in m.get('functionConfigs'):
                temp_model = HttpApiApiInfoEnvironmentsCloudProductConfigFunctionConfigs()
                self.function_configs.append(temp_model.from_map(k))
        self.mse_nacos_configs = []
        if m.get('mseNacosConfigs') is not None:
            for k in m.get('mseNacosConfigs'):
                temp_model = HttpApiApiInfoEnvironmentsCloudProductConfigMseNacosConfigs()
                self.mse_nacos_configs.append(temp_model.from_map(k))
        return self


class HttpApiApiInfoEnvironmentsDnsConfigs(TeaModel):
    def __init__(
        self,
        dns_list: List[str] = None,
        match: HttpApiBackendMatchConditions = None,
        weight: int = None,
    ):
        self.dns_list = dns_list
        self.match = match
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class HttpApiApiInfoEnvironmentsServiceConfigs(TeaModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        match: HttpApiBackendMatchConditions = None,
        name: str = None,
        port: str = None,
        protocol: str = None,
        version: str = None,
        weight: int = None,
    ):
        self.gateway_service_id = gateway_service_id
        self.match = match
        self.name = name
        self.port = port
        self.protocol = protocol
        self.version = version
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class HttpApiApiInfoEnvironmentsVipConfigs(TeaModel):
    def __init__(
        self,
        endpoints: List[str] = None,
        match: HttpApiBackendMatchConditions = None,
        weight: int = None,
    ):
        self.endpoints = endpoints
        self.match = match
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class HttpApiApiInfoEnvironments(TeaModel):
    def __init__(
        self,
        backend_scene: str = None,
        backend_type: str = None,
        cloud_product_config: HttpApiApiInfoEnvironmentsCloudProductConfig = None,
        dns_configs: List[HttpApiApiInfoEnvironmentsDnsConfigs] = None,
        environment_id: str = None,
        service_configs: List[HttpApiApiInfoEnvironmentsServiceConfigs] = None,
        vip_configs: List[HttpApiApiInfoEnvironmentsVipConfigs] = None,
    ):
        self.backend_scene = backend_scene
        self.backend_type = backend_type
        self.cloud_product_config = cloud_product_config
        self.dns_configs = dns_configs
        self.environment_id = environment_id
        self.service_configs = service_configs
        self.vip_configs = vip_configs

    def validate(self):
        if self.cloud_product_config:
            self.cloud_product_config.validate()
        if self.dns_configs:
            for k in self.dns_configs:
                if k:
                    k.validate()
        if self.service_configs:
            for k in self.service_configs:
                if k:
                    k.validate()
        if self.vip_configs:
            for k in self.vip_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_scene is not None:
            result['backendScene'] = self.backend_scene
        if self.backend_type is not None:
            result['backendType'] = self.backend_type
        if self.cloud_product_config is not None:
            result['cloudProductConfig'] = self.cloud_product_config.to_map()
        result['dnsConfigs'] = []
        if self.dns_configs is not None:
            for k in self.dns_configs:
                result['dnsConfigs'].append(k.to_map() if k else None)
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k in self.service_configs:
                result['serviceConfigs'].append(k.to_map() if k else None)
        result['vipConfigs'] = []
        if self.vip_configs is not None:
            for k in self.vip_configs:
                result['vipConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backendScene') is not None:
            self.backend_scene = m.get('backendScene')
        if m.get('backendType') is not None:
            self.backend_type = m.get('backendType')
        if m.get('cloudProductConfig') is not None:
            temp_model = HttpApiApiInfoEnvironmentsCloudProductConfig()
            self.cloud_product_config = temp_model.from_map(m['cloudProductConfig'])
        self.dns_configs = []
        if m.get('dnsConfigs') is not None:
            for k in m.get('dnsConfigs'):
                temp_model = HttpApiApiInfoEnvironmentsDnsConfigs()
                self.dns_configs.append(temp_model.from_map(k))
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k in m.get('serviceConfigs'):
                temp_model = HttpApiApiInfoEnvironmentsServiceConfigs()
                self.service_configs.append(temp_model.from_map(k))
        self.vip_configs = []
        if m.get('vipConfigs') is not None:
            for k in m.get('vipConfigs'):
                temp_model = HttpApiApiInfoEnvironmentsVipConfigs()
                self.vip_configs.append(temp_model.from_map(k))
        return self


class HttpApiVersionInfo(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        header_name: str = None,
        query_name: str = None,
        scheme: str = None,
        version: str = None,
    ):
        self.enable = enable
        self.header_name = header_name
        self.query_name = query_name
        self.scheme = scheme
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.header_name is not None:
            result['headerName'] = self.header_name
        if self.query_name is not None:
            result['queryName'] = self.query_name
        if self.scheme is not None:
            result['scheme'] = self.scheme
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('headerName') is not None:
            self.header_name = m.get('headerName')
        if m.get('queryName') is not None:
            self.query_name = m.get('queryName')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class HttpApiApiInfo(TeaModel):
    def __init__(
        self,
        base_path: str = None,
        description: str = None,
        environments: List[HttpApiApiInfoEnvironments] = None,
        http_api_id: str = None,
        name: str = None,
        protocols: List[str] = None,
        version_info: HttpApiVersionInfo = None,
    ):
        self.base_path = base_path
        self.description = description
        self.environments = environments
        self.http_api_id = http_api_id
        self.name = name
        self.protocols = protocols
        self.version_info = version_info

    def validate(self):
        if self.environments:
            for k in self.environments:
                if k:
                    k.validate()
        if self.version_info:
            self.version_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_path is not None:
            result['basePath'] = self.base_path
        if self.description is not None:
            result['description'] = self.description
        result['environments'] = []
        if self.environments is not None:
            for k in self.environments:
                result['environments'].append(k.to_map() if k else None)
        if self.http_api_id is not None:
            result['httpApiId'] = self.http_api_id
        if self.name is not None:
            result['name'] = self.name
        if self.protocols is not None:
            result['protocols'] = self.protocols
        if self.version_info is not None:
            result['versionInfo'] = self.version_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.environments = []
        if m.get('environments') is not None:
            for k in m.get('environments'):
                temp_model = HttpApiApiInfoEnvironments()
                self.environments.append(temp_model.from_map(k))
        if m.get('httpApiId') is not None:
            self.http_api_id = m.get('httpApiId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocols') is not None:
            self.protocols = m.get('protocols')
        if m.get('versionInfo') is not None:
            temp_model = HttpApiVersionInfo()
            self.version_info = temp_model.from_map(m['versionInfo'])
        return self


class HttpApiDomainInfo(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class HttpApiInfoByName(TeaModel):
    def __init__(
        self,
        name: str = None,
        version_enabled: bool = None,
        versioned_http_apis: List[HttpApiApiInfo] = None,
    ):
        self.name = name
        self.version_enabled = version_enabled
        self.versioned_http_apis = versioned_http_apis

    def validate(self):
        if self.versioned_http_apis:
            for k in self.versioned_http_apis:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.version_enabled is not None:
            result['versionEnabled'] = self.version_enabled
        result['versionedHttpApis'] = []
        if self.versioned_http_apis is not None:
            for k in self.versioned_http_apis:
                result['versionedHttpApis'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('versionEnabled') is not None:
            self.version_enabled = m.get('versionEnabled')
        self.versioned_http_apis = []
        if m.get('versionedHttpApis') is not None:
            for k in m.get('versionedHttpApis'):
                temp_model = HttpApiApiInfo()
                self.versioned_http_apis.append(temp_model.from_map(k))
        return self


class HttpApiMockContract(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        response_code: int = None,
        response_content: str = None,
    ):
        self.enable = enable
        self.response_code = response_code
        self.response_content = response_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.response_code is not None:
            result['responseCode'] = self.response_code
        if self.response_content is not None:
            result['responseContent'] = self.response_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('responseCode') is not None:
            self.response_code = m.get('responseCode')
        if m.get('responseContent') is not None:
            self.response_content = m.get('responseContent')
        return self


class HttpApiParameter(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        example_value: str = None,
        name: str = None,
        required: bool = None,
        type: str = None,
    ):
        self.default_value = default_value
        self.description = description
        self.example_value = example_value
        # This parameter is required.
        self.name = name
        self.required = required
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.description is not None:
            result['description'] = self.description
        if self.example_value is not None:
            result['exampleValue'] = self.example_value
        if self.name is not None:
            result['name'] = self.name
        if self.required is not None:
            result['required'] = self.required
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('exampleValue') is not None:
            self.example_value = m.get('exampleValue')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class HttpApiRequestContractBody(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        description: str = None,
        example: str = None,
        json_schema: str = None,
    ):
        self.content_type = content_type
        self.description = description
        self.example = example
        self.json_schema = json_schema

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.description is not None:
            result['description'] = self.description
        if self.example is not None:
            result['example'] = self.example
        if self.json_schema is not None:
            result['jsonSchema'] = self.json_schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('example') is not None:
            self.example = m.get('example')
        if m.get('jsonSchema') is not None:
            self.json_schema = m.get('jsonSchema')
        return self


class HttpApiRequestContract(TeaModel):
    def __init__(
        self,
        body: HttpApiRequestContractBody = None,
        header_parameters: List[HttpApiParameter] = None,
        path_parameters: List[HttpApiParameter] = None,
        query_parameters: List[HttpApiParameter] = None,
    ):
        self.body = body
        self.header_parameters = header_parameters
        self.path_parameters = path_parameters
        self.query_parameters = query_parameters

    def validate(self):
        if self.body:
            self.body.validate()
        if self.header_parameters:
            for k in self.header_parameters:
                if k:
                    k.validate()
        if self.path_parameters:
            for k in self.path_parameters:
                if k:
                    k.validate()
        if self.query_parameters:
            for k in self.query_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        result['headerParameters'] = []
        if self.header_parameters is not None:
            for k in self.header_parameters:
                result['headerParameters'].append(k.to_map() if k else None)
        result['pathParameters'] = []
        if self.path_parameters is not None:
            for k in self.path_parameters:
                result['pathParameters'].append(k.to_map() if k else None)
        result['queryParameters'] = []
        if self.query_parameters is not None:
            for k in self.query_parameters:
                result['queryParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = HttpApiRequestContractBody()
            self.body = temp_model.from_map(m['body'])
        self.header_parameters = []
        if m.get('headerParameters') is not None:
            for k in m.get('headerParameters'):
                temp_model = HttpApiParameter()
                self.header_parameters.append(temp_model.from_map(k))
        self.path_parameters = []
        if m.get('pathParameters') is not None:
            for k in m.get('pathParameters'):
                temp_model = HttpApiParameter()
                self.path_parameters.append(temp_model.from_map(k))
        self.query_parameters = []
        if m.get('queryParameters') is not None:
            for k in m.get('queryParameters'):
                temp_model = HttpApiParameter()
                self.query_parameters.append(temp_model.from_map(k))
        return self


class HttpApiResponseContractItems(TeaModel):
    def __init__(
        self,
        code: int = None,
        description: str = None,
        example: str = None,
        json_schema: str = None,
    ):
        self.code = code
        self.description = description
        self.example = example
        self.json_schema = json_schema

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.description is not None:
            result['description'] = self.description
        if self.example is not None:
            result['example'] = self.example
        if self.json_schema is not None:
            result['jsonSchema'] = self.json_schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('example') is not None:
            self.example = m.get('example')
        if m.get('jsonSchema') is not None:
            self.json_schema = m.get('jsonSchema')
        return self


class HttpApiResponseContract(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        items: List[HttpApiResponseContractItems] = None,
    ):
        # This parameter is required.
        self.content_type = content_type
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['contentType'] = self.content_type
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = HttpApiResponseContractItems()
                self.items.append(temp_model.from_map(k))
        return self


class HttpApiOperation(TeaModel):
    def __init__(
        self,
        description: str = None,
        method: str = None,
        mock: HttpApiMockContract = None,
        name: str = None,
        path: str = None,
        request: HttpApiRequestContract = None,
        response: HttpApiResponseContract = None,
    ):
        self.description = description
        # This parameter is required.
        self.method = method
        self.mock = mock
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.path = path
        self.request = request
        self.response = response

    def validate(self):
        if self.mock:
            self.mock.validate()
        if self.request:
            self.request.validate()
        if self.response:
            self.response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.method is not None:
            result['method'] = self.method
        if self.mock is not None:
            result['mock'] = self.mock.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.path is not None:
            result['path'] = self.path
        if self.request is not None:
            result['request'] = self.request.to_map()
        if self.response is not None:
            result['response'] = self.response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('mock') is not None:
            temp_model = HttpApiMockContract()
            self.mock = temp_model.from_map(m['mock'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('request') is not None:
            temp_model = HttpApiRequestContract()
            self.request = temp_model.from_map(m['request'])
        if m.get('response') is not None:
            temp_model = HttpApiResponseContract()
            self.response = temp_model.from_map(m['response'])
        return self


class HttpApiOperationInfo(TeaModel):
    def __init__(
        self,
        create_timestamp: int = None,
        description: str = None,
        method: str = None,
        mock: HttpApiMockContract = None,
        name: str = None,
        operation_id: str = None,
        path: str = None,
        request: HttpApiRequestContract = None,
        response: HttpApiResponseContract = None,
    ):
        self.create_timestamp = create_timestamp
        self.description = description
        self.method = method
        self.mock = mock
        self.name = name
        self.operation_id = operation_id
        self.path = path
        self.request = request
        self.response = response

    def validate(self):
        if self.mock:
            self.mock.validate()
        if self.request:
            self.request.validate()
        if self.response:
            self.response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        if self.description is not None:
            result['description'] = self.description
        if self.method is not None:
            result['method'] = self.method
        if self.mock is not None:
            result['mock'] = self.mock.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.operation_id is not None:
            result['operationId'] = self.operation_id
        if self.path is not None:
            result['path'] = self.path
        if self.request is not None:
            result['request'] = self.request.to_map()
        if self.response is not None:
            result['response'] = self.response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('mock') is not None:
            temp_model = HttpApiMockContract()
            self.mock = temp_model.from_map(m['mock'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('operationId') is not None:
            self.operation_id = m.get('operationId')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('request') is not None:
            temp_model = HttpApiRequestContract()
            self.request = temp_model.from_map(m['request'])
        if m.get('response') is not None:
            temp_model = HttpApiResponseContract()
            self.response = temp_model.from_map(m['response'])
        return self


class HttpApiPublishRevisionInfoCloudProductConfigContainerServiceConfigs(TeaModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        match: HttpApiBackendMatchConditions = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
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


class HttpApiPublishRevisionInfoCloudProductConfigFunctionConfigs(TeaModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        match: HttpApiBackendMatchConditions = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class HttpApiPublishRevisionInfoCloudProductConfigMseNacosConfigs(TeaModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        group_name: str = None,
        match: HttpApiBackendMatchConditions = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class HttpApiPublishRevisionInfoCloudProductConfig(TeaModel):
    def __init__(
        self,
        cloud_product_type: str = None,
        container_service_configs: List[HttpApiPublishRevisionInfoCloudProductConfigContainerServiceConfigs] = None,
        function_configs: List[HttpApiPublishRevisionInfoCloudProductConfigFunctionConfigs] = None,
        mse_nacos_configs: List[HttpApiPublishRevisionInfoCloudProductConfigMseNacosConfigs] = None,
    ):
        self.cloud_product_type = cloud_product_type
        self.container_service_configs = container_service_configs
        self.function_configs = function_configs
        self.mse_nacos_configs = mse_nacos_configs

    def validate(self):
        if self.container_service_configs:
            for k in self.container_service_configs:
                if k:
                    k.validate()
        if self.function_configs:
            for k in self.function_configs:
                if k:
                    k.validate()
        if self.mse_nacos_configs:
            for k in self.mse_nacos_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_product_type is not None:
            result['cloudProductType'] = self.cloud_product_type
        result['containerServiceConfigs'] = []
        if self.container_service_configs is not None:
            for k in self.container_service_configs:
                result['containerServiceConfigs'].append(k.to_map() if k else None)
        result['functionConfigs'] = []
        if self.function_configs is not None:
            for k in self.function_configs:
                result['functionConfigs'].append(k.to_map() if k else None)
        result['mseNacosConfigs'] = []
        if self.mse_nacos_configs is not None:
            for k in self.mse_nacos_configs:
                result['mseNacosConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cloudProductType') is not None:
            self.cloud_product_type = m.get('cloudProductType')
        self.container_service_configs = []
        if m.get('containerServiceConfigs') is not None:
            for k in m.get('containerServiceConfigs'):
                temp_model = HttpApiPublishRevisionInfoCloudProductConfigContainerServiceConfigs()
                self.container_service_configs.append(temp_model.from_map(k))
        self.function_configs = []
        if m.get('functionConfigs') is not None:
            for k in m.get('functionConfigs'):
                temp_model = HttpApiPublishRevisionInfoCloudProductConfigFunctionConfigs()
                self.function_configs.append(temp_model.from_map(k))
        self.mse_nacos_configs = []
        if m.get('mseNacosConfigs') is not None:
            for k in m.get('mseNacosConfigs'):
                temp_model = HttpApiPublishRevisionInfoCloudProductConfigMseNacosConfigs()
                self.mse_nacos_configs.append(temp_model.from_map(k))
        return self


class HttpApiPublishRevisionInfoDnsConfigs(TeaModel):
    def __init__(
        self,
        dns_list: List[str] = None,
        match: HttpApiBackendMatchConditions = None,
        weight: int = None,
    ):
        self.dns_list = dns_list
        self.match = match
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class HttpApiPublishRevisionInfoEnvironmentInfoGatewayInfo(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class HttpApiPublishRevisionInfoEnvironmentInfo(TeaModel):
    def __init__(
        self,
        alias: str = None,
        environment_id: str = None,
        gateway_info: HttpApiPublishRevisionInfoEnvironmentInfoGatewayInfo = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpApiPublishRevisionInfoEnvironmentInfoGatewayInfo()
            self.gateway_info = temp_model.from_map(m['gatewayInfo'])
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class HttpApiPublishRevisionInfoServiceConfigs(TeaModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        match: HttpApiBackendMatchConditions = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class HttpApiPublishRevisionInfoVipConfigs(TeaModel):
    def __init__(
        self,
        endpoints: List[str] = None,
        match: HttpApiBackendMatchConditions = None,
        weight: int = None,
    ):
        self.endpoints = endpoints
        self.match = match
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class HttpApiPublishRevisionInfo(TeaModel):
    def __init__(
        self,
        backend_scene: str = None,
        backend_type: str = None,
        cloud_product_config: HttpApiPublishRevisionInfoCloudProductConfig = None,
        create_timestamp: int = None,
        custom_domains: List[HttpApiDomainInfo] = None,
        dns_configs: List[HttpApiPublishRevisionInfoDnsConfigs] = None,
        environment_info: HttpApiPublishRevisionInfoEnvironmentInfo = None,
        is_current_version: bool = None,
        operations: List[HttpApiOperationInfo] = None,
        revision_id: str = None,
        service_configs: List[HttpApiPublishRevisionInfoServiceConfigs] = None,
        sub_domains: List[HttpApiDomainInfo] = None,
        vip_configs: List[HttpApiPublishRevisionInfoVipConfigs] = None,
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
            for k in self.custom_domains:
                if k:
                    k.validate()
        if self.dns_configs:
            for k in self.dns_configs:
                if k:
                    k.validate()
        if self.environment_info:
            self.environment_info.validate()
        if self.operations:
            for k in self.operations:
                if k:
                    k.validate()
        if self.service_configs:
            for k in self.service_configs:
                if k:
                    k.validate()
        if self.sub_domains:
            for k in self.sub_domains:
                if k:
                    k.validate()
        if self.vip_configs:
            for k in self.vip_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.custom_domains:
                result['customDomains'].append(k.to_map() if k else None)
        result['dnsConfigs'] = []
        if self.dns_configs is not None:
            for k in self.dns_configs:
                result['dnsConfigs'].append(k.to_map() if k else None)
        if self.environment_info is not None:
            result['environmentInfo'] = self.environment_info.to_map()
        if self.is_current_version is not None:
            result['isCurrentVersion'] = self.is_current_version
        result['operations'] = []
        if self.operations is not None:
            for k in self.operations:
                result['operations'].append(k.to_map() if k else None)
        if self.revision_id is not None:
            result['revisionId'] = self.revision_id
        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k in self.service_configs:
                result['serviceConfigs'].append(k.to_map() if k else None)
        result['subDomains'] = []
        if self.sub_domains is not None:
            for k in self.sub_domains:
                result['subDomains'].append(k.to_map() if k else None)
        result['vipConfigs'] = []
        if self.vip_configs is not None:
            for k in self.vip_configs:
                result['vipConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backendScene') is not None:
            self.backend_scene = m.get('backendScene')
        if m.get('backendType') is not None:
            self.backend_type = m.get('backendType')
        if m.get('cloudProductConfig') is not None:
            temp_model = HttpApiPublishRevisionInfoCloudProductConfig()
            self.cloud_product_config = temp_model.from_map(m['cloudProductConfig'])
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        self.custom_domains = []
        if m.get('customDomains') is not None:
            for k in m.get('customDomains'):
                temp_model = HttpApiDomainInfo()
                self.custom_domains.append(temp_model.from_map(k))
        self.dns_configs = []
        if m.get('dnsConfigs') is not None:
            for k in m.get('dnsConfigs'):
                temp_model = HttpApiPublishRevisionInfoDnsConfigs()
                self.dns_configs.append(temp_model.from_map(k))
        if m.get('environmentInfo') is not None:
            temp_model = HttpApiPublishRevisionInfoEnvironmentInfo()
            self.environment_info = temp_model.from_map(m['environmentInfo'])
        if m.get('isCurrentVersion') is not None:
            self.is_current_version = m.get('isCurrentVersion')
        self.operations = []
        if m.get('operations') is not None:
            for k in m.get('operations'):
                temp_model = HttpApiOperationInfo()
                self.operations.append(temp_model.from_map(k))
        if m.get('revisionId') is not None:
            self.revision_id = m.get('revisionId')
        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k in m.get('serviceConfigs'):
                temp_model = HttpApiPublishRevisionInfoServiceConfigs()
                self.service_configs.append(temp_model.from_map(k))
        self.sub_domains = []
        if m.get('subDomains') is not None:
            for k in m.get('subDomains'):
                temp_model = HttpApiDomainInfo()
                self.sub_domains.append(temp_model.from_map(k))
        self.vip_configs = []
        if m.get('vipConfigs') is not None:
            for k in m.get('vipConfigs'):
                temp_model = HttpApiPublishRevisionInfoVipConfigs()
                self.vip_configs.append(temp_model.from_map(k))
        return self


class HttpApiVersionConfig(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        header_name: str = None,
        query_name: str = None,
        scheme: str = None,
        version: str = None,
    ):
        self.enable = enable
        self.header_name = header_name
        self.query_name = query_name
        self.scheme = scheme
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.header_name is not None:
            result['headerName'] = self.header_name
        if self.query_name is not None:
            result['queryName'] = self.query_name
        if self.scheme is not None:
            result['scheme'] = self.scheme
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('headerName') is not None:
            self.header_name = m.get('headerName')
        if m.get('queryName') is not None:
            self.query_name = m.get('queryName')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class HttpDubboTranscoderMothedMapListParamMapsList(TeaModel):
    def __init__(
        self,
        extract_key: str = None,
        extract_key_spec: str = None,
        mapping_type: str = None,
    ):
        self.extract_key = extract_key
        self.extract_key_spec = extract_key_spec
        self.mapping_type = mapping_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extract_key is not None:
            result['extractKey'] = self.extract_key
        if self.extract_key_spec is not None:
            result['extractKeySpec'] = self.extract_key_spec
        if self.mapping_type is not None:
            result['mappingType'] = self.mapping_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extractKey') is not None:
            self.extract_key = m.get('extractKey')
        if m.get('extractKeySpec') is not None:
            self.extract_key_spec = m.get('extractKeySpec')
        if m.get('mappingType') is not None:
            self.mapping_type = m.get('mappingType')
        return self


class HttpDubboTranscoderMothedMapList(TeaModel):
    def __init__(
        self,
        dubbo_mothed_name: str = None,
        http_mothed: str = None,
        mothedpath: str = None,
        param_maps_list: List[HttpDubboTranscoderMothedMapListParamMapsList] = None,
        pass_through_all_headers: str = None,
        pass_through_list: List[str] = None,
    ):
        self.dubbo_mothed_name = dubbo_mothed_name
        self.http_mothed = http_mothed
        self.mothedpath = mothedpath
        self.param_maps_list = param_maps_list
        self.pass_through_all_headers = pass_through_all_headers
        self.pass_through_list = pass_through_list

    def validate(self):
        if self.param_maps_list:
            for k in self.param_maps_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dubbo_mothed_name is not None:
            result['dubboMothedName'] = self.dubbo_mothed_name
        if self.http_mothed is not None:
            result['httpMothed'] = self.http_mothed
        if self.mothedpath is not None:
            result['mothedpath'] = self.mothedpath
        result['paramMapsList'] = []
        if self.param_maps_list is not None:
            for k in self.param_maps_list:
                result['paramMapsList'].append(k.to_map() if k else None)
        if self.pass_through_all_headers is not None:
            result['passThroughAllHeaders'] = self.pass_through_all_headers
        if self.pass_through_list is not None:
            result['passThroughList'] = self.pass_through_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dubboMothedName') is not None:
            self.dubbo_mothed_name = m.get('dubboMothedName')
        if m.get('httpMothed') is not None:
            self.http_mothed = m.get('httpMothed')
        if m.get('mothedpath') is not None:
            self.mothedpath = m.get('mothedpath')
        self.param_maps_list = []
        if m.get('paramMapsList') is not None:
            for k in m.get('paramMapsList'):
                temp_model = HttpDubboTranscoderMothedMapListParamMapsList()
                self.param_maps_list.append(temp_model.from_map(k))
        if m.get('passThroughAllHeaders') is not None:
            self.pass_through_all_headers = m.get('passThroughAllHeaders')
        if m.get('passThroughList') is not None:
            self.pass_through_list = m.get('passThroughList')
        return self


class HttpDubboTranscoder(TeaModel):
    def __init__(
        self,
        dubbo_service_group: str = None,
        dubbo_service_name: str = None,
        dubbo_service_version: str = None,
        mothed_map_list: List[HttpDubboTranscoderMothedMapList] = None,
    ):
        self.dubbo_service_group = dubbo_service_group
        self.dubbo_service_name = dubbo_service_name
        self.dubbo_service_version = dubbo_service_version
        self.mothed_map_list = mothed_map_list

    def validate(self):
        if self.mothed_map_list:
            for k in self.mothed_map_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dubbo_service_group is not None:
            result['dubboServiceGroup'] = self.dubbo_service_group
        if self.dubbo_service_name is not None:
            result['dubboServiceName'] = self.dubbo_service_name
        if self.dubbo_service_version is not None:
            result['dubboServiceVersion'] = self.dubbo_service_version
        result['mothedMapList'] = []
        if self.mothed_map_list is not None:
            for k in self.mothed_map_list:
                result['mothedMapList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dubboServiceGroup') is not None:
            self.dubbo_service_group = m.get('dubboServiceGroup')
        if m.get('dubboServiceName') is not None:
            self.dubbo_service_name = m.get('dubboServiceName')
        if m.get('dubboServiceVersion') is not None:
            self.dubbo_service_version = m.get('dubboServiceVersion')
        self.mothed_map_list = []
        if m.get('mothedMapList') is not None:
            for k in m.get('mothedMapList'):
                temp_model = HttpDubboTranscoderMothedMapList()
                self.mothed_map_list.append(temp_model.from_map(k))
        return self


class HttpRouteMatchHeaders(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        self.name = name
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class HttpRouteMatchPath(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class HttpRouteMatchQueryParams(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        self.name = name
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class HttpRouteMatch(TeaModel):
    def __init__(
        self,
        headers: List[HttpRouteMatchHeaders] = None,
        ignore_uri_case: bool = None,
        methods: List[str] = None,
        path: HttpRouteMatchPath = None,
        query_params: List[HttpRouteMatchQueryParams] = None,
    ):
        self.headers = headers
        self.ignore_uri_case = ignore_uri_case
        self.methods = methods
        self.path = path
        self.query_params = query_params

    def validate(self):
        if self.headers:
            for k in self.headers:
                if k:
                    k.validate()
        if self.path:
            self.path.validate()
        if self.query_params:
            for k in self.query_params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['headers'] = []
        if self.headers is not None:
            for k in self.headers:
                result['headers'].append(k.to_map() if k else None)
        if self.ignore_uri_case is not None:
            result['ignoreUriCase'] = self.ignore_uri_case
        if self.methods is not None:
            result['methods'] = self.methods
        if self.path is not None:
            result['path'] = self.path.to_map()
        result['queryParams'] = []
        if self.query_params is not None:
            for k in self.query_params:
                result['queryParams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.headers = []
        if m.get('headers') is not None:
            for k in m.get('headers'):
                temp_model = HttpRouteMatchHeaders()
                self.headers.append(temp_model.from_map(k))
        if m.get('ignoreUriCase') is not None:
            self.ignore_uri_case = m.get('ignoreUriCase')
        if m.get('methods') is not None:
            self.methods = m.get('methods')
        if m.get('path') is not None:
            temp_model = HttpRouteMatchPath()
            self.path = temp_model.from_map(m['path'])
        self.query_params = []
        if m.get('queryParams') is not None:
            for k in m.get('queryParams'):
                temp_model = HttpRouteMatchQueryParams()
                self.query_params.append(temp_model.from_map(k))
        return self


class PolicyClassInfo(TeaModel):
    def __init__(
        self,
        alias: str = None,
        attachable_resource_types: List[str] = None,
        class_id: str = None,
        config_example: str = None,
        deprecated: bool = None,
        description: str = None,
        direction: str = None,
        enable_log: bool = None,
        execute_priority: str = None,
        execute_stage: str = None,
        name: str = None,
        type: str = None,
        version: str = None,
    ):
        self.alias = alias
        self.attachable_resource_types = attachable_resource_types
        self.class_id = class_id
        self.config_example = config_example
        self.deprecated = deprecated
        self.description = description
        self.direction = direction
        self.enable_log = enable_log
        self.execute_priority = execute_priority
        self.execute_stage = execute_stage
        self.name = name
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.attachable_resource_types is not None:
            result['attachableResourceTypes'] = self.attachable_resource_types
        if self.class_id is not None:
            result['classId'] = self.class_id
        if self.config_example is not None:
            result['configExample'] = self.config_example
        if self.deprecated is not None:
            result['deprecated'] = self.deprecated
        if self.description is not None:
            result['description'] = self.description
        if self.direction is not None:
            result['direction'] = self.direction
        if self.enable_log is not None:
            result['enableLog'] = self.enable_log
        if self.execute_priority is not None:
            result['executePriority'] = self.execute_priority
        if self.execute_stage is not None:
            result['executeStage'] = self.execute_stage
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('attachableResourceTypes') is not None:
            self.attachable_resource_types = m.get('attachableResourceTypes')
        if m.get('classId') is not None:
            self.class_id = m.get('classId')
        if m.get('configExample') is not None:
            self.config_example = m.get('configExample')
        if m.get('deprecated') is not None:
            self.deprecated = m.get('deprecated')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('enableLog') is not None:
            self.enable_log = m.get('enableLog')
        if m.get('executePriority') is not None:
            self.execute_priority = m.get('executePriority')
        if m.get('executeStage') is not None:
            self.execute_stage = m.get('executeStage')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class PolicyDetailInfo(TeaModel):
    def __init__(
        self,
        class_id: str = None,
        class_name: str = None,
        config: str = None,
        description: str = None,
        name: str = None,
        policy_id: str = None,
    ):
        self.class_id = class_id
        self.class_name = class_name
        self.config = config
        self.description = description
        self.name = name
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['classId'] = self.class_id
        if self.class_name is not None:
            result['className'] = self.class_name
        if self.config is not None:
            result['config'] = self.config
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classId') is not None:
            self.class_id = m.get('classId')
        if m.get('className') is not None:
            self.class_name = m.get('className')
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        return self


class PolicyInfo(TeaModel):
    def __init__(
        self,
        attachments: List[Attachment] = None,
        class_alias: str = None,
        class_name: str = None,
        config: str = None,
        direction: str = None,
        execute_priority: str = None,
        execute_stage: str = None,
        name: str = None,
        policy_id: str = None,
        type: str = None,
    ):
        self.attachments = attachments
        self.class_alias = class_alias
        self.class_name = class_name
        self.config = config
        self.direction = direction
        self.execute_priority = execute_priority
        self.execute_stage = execute_stage
        self.name = name
        self.policy_id = policy_id
        self.type = type

    def validate(self):
        if self.attachments:
            for k in self.attachments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attachments'] = []
        if self.attachments is not None:
            for k in self.attachments:
                result['attachments'].append(k.to_map() if k else None)
        if self.class_alias is not None:
            result['classAlias'] = self.class_alias
        if self.class_name is not None:
            result['className'] = self.class_name
        if self.config is not None:
            result['config'] = self.config
        if self.direction is not None:
            result['direction'] = self.direction
        if self.execute_priority is not None:
            result['executePriority'] = self.execute_priority
        if self.execute_stage is not None:
            result['executeStage'] = self.execute_stage
        if self.name is not None:
            result['name'] = self.name
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('attachments') is not None:
            for k in m.get('attachments'):
                temp_model = Attachment()
                self.attachments.append(temp_model.from_map(k))
        if m.get('classAlias') is not None:
            self.class_alias = m.get('classAlias')
        if m.get('className') is not None:
            self.class_name = m.get('className')
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('executePriority') is not None:
            self.execute_priority = m.get('executePriority')
        if m.get('executeStage') is not None:
            self.execute_stage = m.get('executeStage')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ResourceStatistic(TeaModel):
    def __init__(
        self,
        resource_count: int = None,
        resource_type: str = None,
    ):
        self.resource_count = resource_count
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_count is not None:
            result['resourceCount'] = self.resource_count
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceCount') is not None:
            self.resource_count = m.get('resourceCount')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ServiceLinkedRole(TeaModel):
    def __init__(
        self,
        arn: str = None,
        assume_role_policy_document: str = None,
        create_date: str = None,
        description: str = None,
        is_service_linked_role: bool = None,
        role_id: str = None,
        role_name: str = None,
        role_principal_name: str = None,
    ):
        self.arn = arn
        self.assume_role_policy_document = assume_role_policy_document
        self.create_date = create_date
        self.description = description
        self.is_service_linked_role = is_service_linked_role
        self.role_id = role_id
        self.role_name = role_name
        self.role_principal_name = role_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['arn'] = self.arn
        if self.assume_role_policy_document is not None:
            result['assumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.create_date is not None:
            result['createDate'] = self.create_date
        if self.description is not None:
            result['description'] = self.description
        if self.is_service_linked_role is not None:
            result['isServiceLinkedRole'] = self.is_service_linked_role
        if self.role_id is not None:
            result['roleId'] = self.role_id
        if self.role_name is not None:
            result['roleName'] = self.role_name
        if self.role_principal_name is not None:
            result['rolePrincipalName'] = self.role_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arn') is not None:
            self.arn = m.get('arn')
        if m.get('assumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('assumeRolePolicyDocument')
        if m.get('createDate') is not None:
            self.create_date = m.get('createDate')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('isServiceLinkedRole') is not None:
            self.is_service_linked_role = m.get('isServiceLinkedRole')
        if m.get('roleId') is not None:
            self.role_id = m.get('roleId')
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        if m.get('rolePrincipalName') is not None:
            self.role_principal_name = m.get('rolePrincipalName')
        return self


class SslCertMetaInfo(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        cert_id: int = None,
        cert_identifier: str = None,
        cert_name: str = None,
        common_name: str = None,
        domain: str = None,
        domain_match_cert: bool = None,
        fingerprint: str = None,
        instance_id: str = None,
        is_chain_completed: bool = None,
        issuer: str = None,
        key_size: str = None,
        md_5: str = None,
        not_after_timestamp: int = None,
        not_before_timestamp: int = None,
        sans: str = None,
        serial_no: str = None,
        sha_2: str = None,
        sign_algorithm: str = None,
    ):
        self.algorithm = algorithm
        self.cert_id = cert_id
        self.cert_identifier = cert_identifier
        self.cert_name = cert_name
        self.common_name = common_name
        self.domain = domain
        self.domain_match_cert = domain_match_cert
        self.fingerprint = fingerprint
        self.instance_id = instance_id
        self.is_chain_completed = is_chain_completed
        self.issuer = issuer
        self.key_size = key_size
        self.md_5 = md_5
        self.not_after_timestamp = not_after_timestamp
        self.not_before_timestamp = not_before_timestamp
        self.sans = sans
        self.serial_no = serial_no
        self.sha_2 = sha_2
        self.sign_algorithm = sign_algorithm

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.cert_id is not None:
            result['certId'] = self.cert_id
        if self.cert_identifier is not None:
            result['certIdentifier'] = self.cert_identifier
        if self.cert_name is not None:
            result['certName'] = self.cert_name
        if self.common_name is not None:
            result['commonName'] = self.common_name
        if self.domain is not None:
            result['domain'] = self.domain
        if self.domain_match_cert is not None:
            result['domainMatchCert'] = self.domain_match_cert
        if self.fingerprint is not None:
            result['fingerprint'] = self.fingerprint
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.is_chain_completed is not None:
            result['isChainCompleted'] = self.is_chain_completed
        if self.issuer is not None:
            result['issuer'] = self.issuer
        if self.key_size is not None:
            result['keySize'] = self.key_size
        if self.md_5 is not None:
            result['md5'] = self.md_5
        if self.not_after_timestamp is not None:
            result['notAfterTimestamp'] = self.not_after_timestamp
        if self.not_before_timestamp is not None:
            result['notBeforeTimestamp'] = self.not_before_timestamp
        if self.sans is not None:
            result['sans'] = self.sans
        if self.serial_no is not None:
            result['serialNo'] = self.serial_no
        if self.sha_2 is not None:
            result['sha2'] = self.sha_2
        if self.sign_algorithm is not None:
            result['signAlgorithm'] = self.sign_algorithm
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('certId') is not None:
            self.cert_id = m.get('certId')
        if m.get('certIdentifier') is not None:
            self.cert_identifier = m.get('certIdentifier')
        if m.get('certName') is not None:
            self.cert_name = m.get('certName')
        if m.get('commonName') is not None:
            self.common_name = m.get('commonName')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('domainMatchCert') is not None:
            self.domain_match_cert = m.get('domainMatchCert')
        if m.get('fingerprint') is not None:
            self.fingerprint = m.get('fingerprint')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isChainCompleted') is not None:
            self.is_chain_completed = m.get('isChainCompleted')
        if m.get('issuer') is not None:
            self.issuer = m.get('issuer')
        if m.get('keySize') is not None:
            self.key_size = m.get('keySize')
        if m.get('md5') is not None:
            self.md_5 = m.get('md5')
        if m.get('notAfterTimestamp') is not None:
            self.not_after_timestamp = m.get('notAfterTimestamp')
        if m.get('notBeforeTimestamp') is not None:
            self.not_before_timestamp = m.get('notBeforeTimestamp')
        if m.get('sans') is not None:
            self.sans = m.get('sans')
        if m.get('serialNo') is not None:
            self.serial_no = m.get('serialNo')
        if m.get('sha2') is not None:
            self.sha_2 = m.get('sha2')
        if m.get('signAlgorithm') is not None:
            self.sign_algorithm = m.get('signAlgorithm')
        return self


class AddGatewaySecurityGroupRuleRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        port_ranges: List[str] = None,
        security_group_id: str = None,
    ):
        self.description = description
        self.port_ranges = port_ranges
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.port_ranges is not None:
            result['portRanges'] = self.port_ranges
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('portRanges') is not None:
            self.port_ranges = m.get('portRanges')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        return self


class AddGatewaySecurityGroupRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AddGatewaySecurityGroupRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddGatewaySecurityGroupRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddGatewaySecurityGroupRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDomainRequest(TeaModel):
    def __init__(
        self,
        ca_cert_indentifier: str = None,
        cert_indentifier: str = None,
        force_https: bool = None,
        http_2option: str = None,
        name: str = None,
        protocol: str = None,
        tls_max: str = None,
        tls_min: str = None,
    ):
        self.ca_cert_indentifier = ca_cert_indentifier
        self.cert_indentifier = cert_indentifier
        self.force_https = force_https
        self.http_2option = http_2option
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.protocol = protocol
        self.tls_max = tls_max
        self.tls_min = tls_min

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_cert_indentifier is not None:
            result['caCertIndentifier'] = self.ca_cert_indentifier
        if self.cert_indentifier is not None:
            result['certIndentifier'] = self.cert_indentifier
        if self.force_https is not None:
            result['forceHttps'] = self.force_https
        if self.http_2option is not None:
            result['http2Option'] = self.http_2option
        if self.name is not None:
            result['name'] = self.name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.tls_max is not None:
            result['tlsMax'] = self.tls_max
        if self.tls_min is not None:
            result['tlsMin'] = self.tls_min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caCertIndentifier') is not None:
            self.ca_cert_indentifier = m.get('caCertIndentifier')
        if m.get('certIndentifier') is not None:
            self.cert_indentifier = m.get('certIndentifier')
        if m.get('forceHttps') is not None:
            self.force_https = m.get('forceHttps')
        if m.get('http2Option') is not None:
            self.http_2option = m.get('http2Option')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('tlsMax') is not None:
            self.tls_max = m.get('tlsMax')
        if m.get('tlsMin') is not None:
            self.tls_min = m.get('tlsMin')
        return self


class CreateDomainResponseBodyData(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
    ):
        self.domain_id = domain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        return self


class CreateDomainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateDomainResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateDomainResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnvironmentRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
        description: str = None,
        gateway_id: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.alias = alias
        self.description = description
        # This parameter is required.
        self.gateway_id = gateway_id
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.description is not None:
            result['description'] = self.description
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateEnvironmentResponseBodyData(TeaModel):
    def __init__(
        self,
        environment_id: str = None,
    ):
        self.environment_id = environment_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        return self


class CreateEnvironmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateEnvironmentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateEnvironmentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGatewayRouteRequest(TeaModel):
    def __init__(
        self,
        backend_config: GatewayRouteBackendConfig = None,
        description: str = None,
        domain_config: GatewayRouteDomainConfig = None,
        match: HttpRouteMatch = None,
        name: str = None,
    ):
        self.backend_config = backend_config
        self.description = description
        self.domain_config = domain_config
        self.match = match
        self.name = name

    def validate(self):
        if self.backend_config:
            self.backend_config.validate()
        if self.domain_config:
            self.domain_config.validate()
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_config is not None:
            result['backendConfig'] = self.backend_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.domain_config is not None:
            result['domainConfig'] = self.domain_config.to_map()
        if self.match is not None:
            result['match'] = self.match.to_map()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backendConfig') is not None:
            temp_model = GatewayRouteBackendConfig()
            self.backend_config = temp_model.from_map(m['backendConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domainConfig') is not None:
            temp_model = GatewayRouteDomainConfig()
            self.domain_config = temp_model.from_map(m['domainConfig'])
        if m.get('match') is not None:
            temp_model = HttpRouteMatch()
            self.match = temp_model.from_map(m['match'])
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateGatewayRouteResponseBodyData(TeaModel):
    def __init__(
        self,
        gateway_route_id: str = None,
    ):
        self.gateway_route_id = gateway_route_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_route_id is not None:
            result['gatewayRouteId'] = self.gateway_route_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayRouteId') is not None:
            self.gateway_route_id = m.get('gatewayRouteId')
        return self


class CreateGatewayRouteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateGatewayRouteResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateGatewayRouteResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateGatewayRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGatewayRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateGatewayRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGatewayServiceRequestGatewayServiceConfigs(TeaModel):
    def __init__(
        self,
        addresses: List[str] = None,
        group_name: str = None,
        name: str = None,
        namespace: str = None,
        port: int = None,
        qualifier: str = None,
    ):
        self.addresses = addresses
        self.group_name = group_name
        self.name = name
        self.namespace = namespace
        self.port = port
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['addresses'] = self.addresses
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.port is not None:
            result['port'] = self.port
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addresses') is not None:
            self.addresses = m.get('addresses')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class CreateGatewayServiceRequest(TeaModel):
    def __init__(
        self,
        gateway_service_configs: List[CreateGatewayServiceRequestGatewayServiceConfigs] = None,
        source_type: str = None,
    ):
        self.gateway_service_configs = gateway_service_configs
        self.source_type = source_type

    def validate(self):
        if self.gateway_service_configs:
            for k in self.gateway_service_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['gatewayServiceConfigs'] = []
        if self.gateway_service_configs is not None:
            for k in self.gateway_service_configs:
                result['gatewayServiceConfigs'].append(k.to_map() if k else None)
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gateway_service_configs = []
        if m.get('gatewayServiceConfigs') is not None:
            for k in m.get('gatewayServiceConfigs'):
                temp_model = CreateGatewayServiceRequestGatewayServiceConfigs()
                self.gateway_service_configs.append(temp_model.from_map(k))
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        return self


class CreateGatewayServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        gateway_service_ids: List[str] = None,
    ):
        self.gateway_service_ids = gateway_service_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_service_ids is not None:
            result['gatewayServiceIds'] = self.gateway_service_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayServiceIds') is not None:
            self.gateway_service_ids = m.get('gatewayServiceIds')
        return self


class CreateGatewayServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateGatewayServiceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateGatewayServiceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateGatewayServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGatewayServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateGatewayServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGatewayServiceVersionRequestLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateGatewayServiceVersionRequest(TeaModel):
    def __init__(
        self,
        labels: List[CreateGatewayServiceVersionRequestLabels] = None,
        name: str = None,
    ):
        self.labels = labels
        self.name = name

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('labels') is not None:
            for k in m.get('labels'):
                temp_model = CreateGatewayServiceVersionRequestLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateGatewayServiceVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateGatewayServiceVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGatewayServiceVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateGatewayServiceVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHttpApiRequest(TeaModel):
    def __init__(
        self,
        base_path: str = None,
        description: str = None,
        name: str = None,
        protocols: List[str] = None,
        version_config: HttpApiVersionConfig = None,
    ):
        # This parameter is required.
        self.base_path = base_path
        self.description = description
        # This parameter is required.
        self.name = name
        self.protocols = protocols
        self.version_config = version_config

    def validate(self):
        if self.version_config:
            self.version_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_path is not None:
            result['basePath'] = self.base_path
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.protocols is not None:
            result['protocols'] = self.protocols
        if self.version_config is not None:
            result['versionConfig'] = self.version_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocols') is not None:
            self.protocols = m.get('protocols')
        if m.get('versionConfig') is not None:
            temp_model = HttpApiVersionConfig()
            self.version_config = temp_model.from_map(m['versionConfig'])
        return self


class CreateHttpApiResponseBodyData(TeaModel):
    def __init__(
        self,
        http_api_id: str = None,
        name: str = None,
    ):
        self.http_api_id = http_api_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_api_id is not None:
            result['httpApiId'] = self.http_api_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('httpApiId') is not None:
            self.http_api_id = m.get('httpApiId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateHttpApiResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateHttpApiResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateHttpApiResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateHttpApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateHttpApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateHttpApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHttpApiOperationRequest(TeaModel):
    def __init__(
        self,
        operations: List[HttpApiOperation] = None,
    ):
        self.operations = operations

    def validate(self):
        if self.operations:
            for k in self.operations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['operations'] = []
        if self.operations is not None:
            for k in self.operations:
                result['operations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operations = []
        if m.get('operations') is not None:
            for k in m.get('operations'):
                temp_model = HttpApiOperation()
                self.operations.append(temp_model.from_map(k))
        return self


class CreateHttpApiOperationResponseBodyDataOperations(TeaModel):
    def __init__(
        self,
        operation_id: str = None,
    ):
        self.operation_id = operation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['operationId'] = self.operation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operationId') is not None:
            self.operation_id = m.get('operationId')
        return self


class CreateHttpApiOperationResponseBodyData(TeaModel):
    def __init__(
        self,
        operations: List[CreateHttpApiOperationResponseBodyDataOperations] = None,
    ):
        self.operations = operations

    def validate(self):
        if self.operations:
            for k in self.operations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['operations'] = []
        if self.operations is not None:
            for k in self.operations:
                result['operations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operations = []
        if m.get('operations') is not None:
            for k in m.get('operations'):
                temp_model = CreateHttpApiOperationResponseBodyDataOperations()
                self.operations.append(temp_model.from_map(k))
        return self


class CreateHttpApiOperationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateHttpApiOperationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateHttpApiOperationResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateHttpApiOperationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateHttpApiOperationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateHttpApiOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceSourceRequestK8sServiceSourceConfigAuthorizeSecurityGroupRules(TeaModel):
    def __init__(
        self,
        description: str = None,
        port_ranges: List[str] = None,
        security_group_id: str = None,
    ):
        self.description = description
        self.port_ranges = port_ranges
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.port_ranges is not None:
            result['portRanges'] = self.port_ranges
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('portRanges') is not None:
            self.port_ranges = m.get('portRanges')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        return self


class CreateServiceSourceRequestK8sServiceSourceConfigIngressConfig(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        ingress_class: str = None,
        override_ingress_ip: bool = None,
        watch_namespace: str = None,
    ):
        self.enable = enable
        self.ingress_class = ingress_class
        self.override_ingress_ip = override_ingress_ip
        self.watch_namespace = watch_namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.ingress_class is not None:
            result['ingressClass'] = self.ingress_class
        if self.override_ingress_ip is not None:
            result['overrideIngressIp'] = self.override_ingress_ip
        if self.watch_namespace is not None:
            result['watchNamespace'] = self.watch_namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('ingressClass') is not None:
            self.ingress_class = m.get('ingressClass')
        if m.get('overrideIngressIp') is not None:
            self.override_ingress_ip = m.get('overrideIngressIp')
        if m.get('watchNamespace') is not None:
            self.watch_namespace = m.get('watchNamespace')
        return self


class CreateServiceSourceRequestK8sServiceSourceConfig(TeaModel):
    def __init__(
        self,
        authorize_security_group_rules: List[CreateServiceSourceRequestK8sServiceSourceConfigAuthorizeSecurityGroupRules] = None,
        cluster_id: str = None,
        ingress_config: CreateServiceSourceRequestK8sServiceSourceConfigIngressConfig = None,
    ):
        self.authorize_security_group_rules = authorize_security_group_rules
        self.cluster_id = cluster_id
        self.ingress_config = ingress_config

    def validate(self):
        if self.authorize_security_group_rules:
            for k in self.authorize_security_group_rules:
                if k:
                    k.validate()
        if self.ingress_config:
            self.ingress_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['authorizeSecurityGroupRules'] = []
        if self.authorize_security_group_rules is not None:
            for k in self.authorize_security_group_rules:
                result['authorizeSecurityGroupRules'].append(k.to_map() if k else None)
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.ingress_config is not None:
            result['ingressConfig'] = self.ingress_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorize_security_group_rules = []
        if m.get('authorizeSecurityGroupRules') is not None:
            for k in m.get('authorizeSecurityGroupRules'):
                temp_model = CreateServiceSourceRequestK8sServiceSourceConfigAuthorizeSecurityGroupRules()
                self.authorize_security_group_rules.append(temp_model.from_map(k))
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('ingressConfig') is not None:
            temp_model = CreateServiceSourceRequestK8sServiceSourceConfigIngressConfig()
            self.ingress_config = temp_model.from_map(m['ingressConfig'])
        return self


class CreateServiceSourceRequestNacosServiceSourceConfig(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class CreateServiceSourceRequest(TeaModel):
    def __init__(
        self,
        k_8s_service_source_config: CreateServiceSourceRequestK8sServiceSourceConfig = None,
        nacos_service_source_config: CreateServiceSourceRequestNacosServiceSourceConfig = None,
        type: str = None,
    ):
        self.k_8s_service_source_config = k_8s_service_source_config
        self.nacos_service_source_config = nacos_service_source_config
        self.type = type

    def validate(self):
        if self.k_8s_service_source_config:
            self.k_8s_service_source_config.validate()
        if self.nacos_service_source_config:
            self.nacos_service_source_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.k_8s_service_source_config is not None:
            result['k8sServiceSourceConfig'] = self.k_8s_service_source_config.to_map()
        if self.nacos_service_source_config is not None:
            result['nacosServiceSourceConfig'] = self.nacos_service_source_config.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('k8sServiceSourceConfig') is not None:
            temp_model = CreateServiceSourceRequestK8sServiceSourceConfig()
            self.k_8s_service_source_config = temp_model.from_map(m['k8sServiceSourceConfig'])
        if m.get('nacosServiceSourceConfig') is not None:
            temp_model = CreateServiceSourceRequestNacosServiceSourceConfig()
            self.nacos_service_source_config = temp_model.from_map(m['nacosServiceSourceConfig'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateServiceSourceResponseBodyData(TeaModel):
    def __init__(
        self,
        service_source_id: str = None,
    ):
        self.service_source_id = service_source_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_source_id is not None:
            result['serviceSourceId'] = self.service_source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceSourceId') is not None:
            self.service_source_id = m.get('serviceSourceId')
        return self


class CreateServiceSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateServiceSourceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateServiceSourceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateServiceSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateServiceSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnvironmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGatewayResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayRouteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteGatewayRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGatewayRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteGatewayRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteGatewayServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGatewayServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteGatewayServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayServiceVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteGatewayServiceVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGatewayServiceVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteGatewayServiceVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHttpApiResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteHttpApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteHttpApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteHttpApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHttpApiOperationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteHttpApiOperationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteHttpApiOperationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteHttpApiOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteServiceSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteServiceSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteServiceSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainResponseBodyData(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        ca_cert_indentifier: str = None,
        cert_indentifier: str = None,
        cert_name: str = None,
        create_from: str = None,
        create_timestamp: int = None,
        default: bool = None,
        domain_id: str = None,
        force_https: bool = None,
        http_2option: str = None,
        issuer: str = None,
        name: str = None,
        not_after_timstamp: int = None,
        not_before_timestamp: int = None,
        protocol: str = None,
        sans: str = None,
        tls_max: str = None,
        tls_min: str = None,
        updatetimestamp: int = None,
    ):
        self.algorithm = algorithm
        self.ca_cert_indentifier = ca_cert_indentifier
        self.cert_indentifier = cert_indentifier
        self.cert_name = cert_name
        self.create_from = create_from
        self.create_timestamp = create_timestamp
        self.default = default
        self.domain_id = domain_id
        self.force_https = force_https
        self.http_2option = http_2option
        self.issuer = issuer
        self.name = name
        self.not_after_timstamp = not_after_timstamp
        self.not_before_timestamp = not_before_timestamp
        self.protocol = protocol
        self.sans = sans
        self.tls_max = tls_max
        self.tls_min = tls_min
        self.updatetimestamp = updatetimestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.ca_cert_indentifier is not None:
            result['caCertIndentifier'] = self.ca_cert_indentifier
        if self.cert_indentifier is not None:
            result['certIndentifier'] = self.cert_indentifier
        if self.cert_name is not None:
            result['certName'] = self.cert_name
        if self.create_from is not None:
            result['createFrom'] = self.create_from
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        if self.default is not None:
            result['default'] = self.default
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.force_https is not None:
            result['forceHttps'] = self.force_https
        if self.http_2option is not None:
            result['http2Option'] = self.http_2option
        if self.issuer is not None:
            result['issuer'] = self.issuer
        if self.name is not None:
            result['name'] = self.name
        if self.not_after_timstamp is not None:
            result['notAfterTimstamp'] = self.not_after_timstamp
        if self.not_before_timestamp is not None:
            result['notBeforeTimestamp'] = self.not_before_timestamp
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.sans is not None:
            result['sans'] = self.sans
        if self.tls_max is not None:
            result['tlsMax'] = self.tls_max
        if self.tls_min is not None:
            result['tlsMin'] = self.tls_min
        if self.updatetimestamp is not None:
            result['updatetimestamp'] = self.updatetimestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('caCertIndentifier') is not None:
            self.ca_cert_indentifier = m.get('caCertIndentifier')
        if m.get('certIndentifier') is not None:
            self.cert_indentifier = m.get('certIndentifier')
        if m.get('certName') is not None:
            self.cert_name = m.get('certName')
        if m.get('createFrom') is not None:
            self.create_from = m.get('createFrom')
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        if m.get('default') is not None:
            self.default = m.get('default')
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('forceHttps') is not None:
            self.force_https = m.get('forceHttps')
        if m.get('http2Option') is not None:
            self.http_2option = m.get('http2Option')
        if m.get('issuer') is not None:
            self.issuer = m.get('issuer')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('notAfterTimstamp') is not None:
            self.not_after_timstamp = m.get('notAfterTimstamp')
        if m.get('notBeforeTimestamp') is not None:
            self.not_before_timestamp = m.get('notBeforeTimestamp')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('sans') is not None:
            self.sans = m.get('sans')
        if m.get('tlsMax') is not None:
            self.tls_max = m.get('tlsMax')
        if m.get('tlsMin') is not None:
            self.tls_min = m.get('tlsMin')
        if m.get('updatetimestamp') is not None:
            self.updatetimestamp = m.get('updatetimestamp')
        return self


class GetDomainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDomainResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetDomainResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnvironmentResponseBodyData(TeaModel):
    def __init__(
        self,
        alias: str = None,
        create_timestamp: int = None,
        default: bool = None,
        description: str = None,
        environment_id: str = None,
        gateway_info: GatewayInfo = None,
        name: str = None,
        sub_domain_infos: List[SubDomainInfo] = None,
        update_timestamp: int = None,
    ):
        self.alias = alias
        self.create_timestamp = create_timestamp
        self.default = default
        self.description = description
        self.environment_id = environment_id
        self.gateway_info = gateway_info
        self.name = name
        self.sub_domain_infos = sub_domain_infos
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.gateway_info:
            self.gateway_info.validate()
        if self.sub_domain_infos:
            for k in self.sub_domain_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        if self.default is not None:
            result['default'] = self.default
        if self.description is not None:
            result['description'] = self.description
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()
        if self.name is not None:
            result['name'] = self.name
        result['subDomainInfos'] = []
        if self.sub_domain_infos is not None:
            for k in self.sub_domain_infos:
                result['subDomainInfos'].append(k.to_map() if k else None)
        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        if m.get('default') is not None:
            self.default = m.get('default')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('gatewayInfo') is not None:
            temp_model = GatewayInfo()
            self.gateway_info = temp_model.from_map(m['gatewayInfo'])
        if m.get('name') is not None:
            self.name = m.get('name')
        self.sub_domain_infos = []
        if m.get('subDomainInfos') is not None:
            for k in m.get('subDomainInfos'):
                temp_model = SubDomainInfo()
                self.sub_domain_infos.append(temp_model.from_map(k))
        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')
        return self


class GetEnvironmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetEnvironmentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetEnvironmentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGatewayResponseBodyDataEnvironments(TeaModel):
    def __init__(
        self,
        alias: str = None,
        environment_id: str = None,
        name: str = None,
    ):
        self.alias = alias
        self.environment_id = environment_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetGatewayResponseBodyDataLoadBalancersPorts(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class GetGatewayResponseBodyDataLoadBalancers(TeaModel):
    def __init__(
        self,
        address: str = None,
        address_ip_version: str = None,
        address_type: str = None,
        gateway_default: bool = None,
        load_balancer_id: str = None,
        mode: str = None,
        ports: List[GetGatewayResponseBodyDataLoadBalancersPorts] = None,
        status: str = None,
        type: str = None,
    ):
        self.address = address
        self.address_ip_version = address_ip_version
        self.address_type = address_type
        self.gateway_default = gateway_default
        self.load_balancer_id = load_balancer_id
        self.mode = mode
        self.ports = ports
        self.status = status
        self.type = type

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.address_ip_version is not None:
            result['addressIpVersion'] = self.address_ip_version
        if self.address_type is not None:
            result['addressType'] = self.address_type
        if self.gateway_default is not None:
            result['gatewayDefault'] = self.gateway_default
        if self.load_balancer_id is not None:
            result['loadBalancerId'] = self.load_balancer_id
        if self.mode is not None:
            result['mode'] = self.mode
        result['ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('addressIpVersion') is not None:
            self.address_ip_version = m.get('addressIpVersion')
        if m.get('addressType') is not None:
            self.address_type = m.get('addressType')
        if m.get('gatewayDefault') is not None:
            self.gateway_default = m.get('gatewayDefault')
        if m.get('loadBalancerId') is not None:
            self.load_balancer_id = m.get('loadBalancerId')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        self.ports = []
        if m.get('ports') is not None:
            for k in m.get('ports'):
                temp_model = GetGatewayResponseBodyDataLoadBalancersPorts()
                self.ports.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetGatewayResponseBodyDataSecurityGroup(TeaModel):
    def __init__(
        self,
        name: str = None,
        security_group_id: str = None,
    ):
        self.name = name
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        return self


class GetGatewayResponseBodyDataVSwitch(TeaModel):
    def __init__(
        self,
        name: str = None,
        v_switch_id: str = None,
    ):
        self.name = name
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        return self


class GetGatewayResponseBodyDataVpc(TeaModel):
    def __init__(
        self,
        name: str = None,
        vpc_id: str = None,
    ):
        self.name = name
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class GetGatewayResponseBodyDataZonesVSwitch(TeaModel):
    def __init__(
        self,
        name: str = None,
        v_switch_id: str = None,
    ):
        self.name = name
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        return self


class GetGatewayResponseBodyDataZones(TeaModel):
    def __init__(
        self,
        name: str = None,
        v_switch: GetGatewayResponseBodyDataZonesVSwitch = None,
        zone_id: str = None,
    ):
        self.name = name
        self.v_switch = v_switch
        self.zone_id = zone_id

    def validate(self):
        if self.v_switch:
            self.v_switch.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.v_switch is not None:
            result['vSwitch'] = self.v_switch.to_map()
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('vSwitch') is not None:
            temp_model = GetGatewayResponseBodyDataZonesVSwitch()
            self.v_switch = temp_model.from_map(m['vSwitch'])
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class GetGatewayResponseBodyData(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        create_from: str = None,
        create_timestamp: int = None,
        environments: List[GetGatewayResponseBodyDataEnvironments] = None,
        expire_timestamp: int = None,
        gateway_id: str = None,
        load_balancers: List[GetGatewayResponseBodyDataLoadBalancers] = None,
        name: str = None,
        replicas: str = None,
        security_group: GetGatewayResponseBodyDataSecurityGroup = None,
        spec: str = None,
        status: str = None,
        target_version: str = None,
        update_timestamp: int = None,
        v_switch: GetGatewayResponseBodyDataVSwitch = None,
        version: str = None,
        vpc: GetGatewayResponseBodyDataVpc = None,
        zones: List[GetGatewayResponseBodyDataZones] = None,
    ):
        self.charge_type = charge_type
        self.create_from = create_from
        self.create_timestamp = create_timestamp
        self.environments = environments
        self.expire_timestamp = expire_timestamp
        self.gateway_id = gateway_id
        self.load_balancers = load_balancers
        self.name = name
        self.replicas = replicas
        self.security_group = security_group
        self.spec = spec
        self.status = status
        self.target_version = target_version
        self.update_timestamp = update_timestamp
        self.v_switch = v_switch
        self.version = version
        self.vpc = vpc
        self.zones = zones

    def validate(self):
        if self.environments:
            for k in self.environments:
                if k:
                    k.validate()
        if self.load_balancers:
            for k in self.load_balancers:
                if k:
                    k.validate()
        if self.security_group:
            self.security_group.validate()
        if self.v_switch:
            self.v_switch.validate()
        if self.vpc:
            self.vpc.validate()
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.create_from is not None:
            result['createFrom'] = self.create_from
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        result['environments'] = []
        if self.environments is not None:
            for k in self.environments:
                result['environments'].append(k.to_map() if k else None)
        if self.expire_timestamp is not None:
            result['expireTimestamp'] = self.expire_timestamp
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        result['loadBalancers'] = []
        if self.load_balancers is not None:
            for k in self.load_balancers:
                result['loadBalancers'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.replicas is not None:
            result['replicas'] = self.replicas
        if self.security_group is not None:
            result['securityGroup'] = self.security_group.to_map()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.status is not None:
            result['status'] = self.status
        if self.target_version is not None:
            result['targetVersion'] = self.target_version
        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp
        if self.v_switch is not None:
            result['vSwitch'] = self.v_switch.to_map()
        if self.version is not None:
            result['version'] = self.version
        if self.vpc is not None:
            result['vpc'] = self.vpc.to_map()
        result['zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('createFrom') is not None:
            self.create_from = m.get('createFrom')
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        self.environments = []
        if m.get('environments') is not None:
            for k in m.get('environments'):
                temp_model = GetGatewayResponseBodyDataEnvironments()
                self.environments.append(temp_model.from_map(k))
        if m.get('expireTimestamp') is not None:
            self.expire_timestamp = m.get('expireTimestamp')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        self.load_balancers = []
        if m.get('loadBalancers') is not None:
            for k in m.get('loadBalancers'):
                temp_model = GetGatewayResponseBodyDataLoadBalancers()
                self.load_balancers.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')
        if m.get('securityGroup') is not None:
            temp_model = GetGatewayResponseBodyDataSecurityGroup()
            self.security_group = temp_model.from_map(m['securityGroup'])
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('targetVersion') is not None:
            self.target_version = m.get('targetVersion')
        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')
        if m.get('vSwitch') is not None:
            temp_model = GetGatewayResponseBodyDataVSwitch()
            self.v_switch = temp_model.from_map(m['vSwitch'])
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('vpc') is not None:
            temp_model = GetGatewayResponseBodyDataVpc()
            self.vpc = temp_model.from_map(m['vpc'])
        self.zones = []
        if m.get('zones') is not None:
            for k in m.get('zones'):
                temp_model = GetGatewayResponseBodyDataZones()
                self.zones.append(temp_model.from_map(k))
        return self


class GetGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetGatewayResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetGatewayResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGatewayResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGatewayRouteResponseBodyData(TeaModel):
    def __init__(
        self,
        backend: GatewayRouteBackend = None,
        create_timestamp: int = None,
        description: str = None,
        domain_info: GatewayRouteDomainInfo = None,
        gateway_route_id: str = None,
        match: HttpRouteMatch = None,
        name: str = None,
        status: str = None,
        update_timestamp: int = None,
    ):
        self.backend = backend
        self.create_timestamp = create_timestamp
        self.description = description
        self.domain_info = domain_info
        self.gateway_route_id = gateway_route_id
        self.match = match
        self.name = name
        self.status = status
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.backend:
            self.backend.validate()
        if self.domain_info:
            self.domain_info.validate()
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend is not None:
            result['backend'] = self.backend.to_map()
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        if self.description is not None:
            result['description'] = self.description
        if self.domain_info is not None:
            result['domainInfo'] = self.domain_info.to_map()
        if self.gateway_route_id is not None:
            result['gatewayRouteId'] = self.gateway_route_id
        if self.match is not None:
            result['match'] = self.match.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backend') is not None:
            temp_model = GatewayRouteBackend()
            self.backend = temp_model.from_map(m['backend'])
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domainInfo') is not None:
            temp_model = GatewayRouteDomainInfo()
            self.domain_info = temp_model.from_map(m['domainInfo'])
        if m.get('gatewayRouteId') is not None:
            self.gateway_route_id = m.get('gatewayRouteId')
        if m.get('match') is not None:
            temp_model = HttpRouteMatch()
            self.match = temp_model.from_map(m['match'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')
        return self


class GetGatewayRouteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetGatewayRouteResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetGatewayRouteResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetGatewayRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGatewayRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetGatewayRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGatewayServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GatewayService = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GatewayService()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetGatewayServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGatewayServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetGatewayServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHttpApiResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: HttpApiApiInfo = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpApiApiInfo()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetHttpApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHttpApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetHttpApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHttpApiOperationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: HttpApiOperationInfo = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpApiOperationInfo()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetHttpApiOperationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHttpApiOperationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetHttpApiOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDomainsRequest(TeaModel):
    def __init__(
        self,
        name_like: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.name_like = name_like
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name_like is not None:
            result['nameLike'] = self.name_like
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nameLike') is not None:
            self.name_like = m.get('nameLike')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListDomainsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[DomainInfo] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
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
            for k in m.get('items'):
                temp_model = DomainInfo()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListDomainsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListDomainsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListDomainsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDomainsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentsRequest(TeaModel):
    def __init__(
        self,
        alias_like: str = None,
        gateway_id: str = None,
        gateway_name_like: str = None,
        name_like: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.alias_like = alias_like
        self.gateway_id = gateway_id
        self.gateway_name_like = gateway_name_like
        self.name_like = name_like
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_like is not None:
            result['aliasLike'] = self.alias_like
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.gateway_name_like is not None:
            result['gatewayNameLike'] = self.gateway_name_like
        if self.name_like is not None:
            result['nameLike'] = self.name_like
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasLike') is not None:
            self.alias_like = m.get('aliasLike')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('gatewayNameLike') is not None:
            self.gateway_name_like = m.get('gatewayNameLike')
        if m.get('nameLike') is not None:
            self.name_like = m.get('nameLike')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListEnvironmentsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[EnvironmentInfo] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
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
            for k in m.get('items'):
                temp_model = EnvironmentInfo()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListEnvironmentsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListEnvironmentsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListEnvironmentsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListEnvironmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEnvironmentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEnvironmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGatewayRoutesRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        path: str = None,
        status: str = None,
    ):
        self.keyword = keyword
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.path = path
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.name is not None:
            result['name'] = self.name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.path is not None:
            result['path'] = self.path
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListGatewayRoutesResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        backend: GatewayRouteBackend = None,
        create_timestamp: int = None,
        description: str = None,
        domain_info: GatewayRouteDomainInfo = None,
        gateway_route_id: str = None,
        match: HttpRouteMatch = None,
        name: str = None,
        status: str = None,
        update_timestamp: int = None,
    ):
        self.backend = backend
        self.create_timestamp = create_timestamp
        self.description = description
        self.domain_info = domain_info
        self.gateway_route_id = gateway_route_id
        self.match = match
        self.name = name
        self.status = status
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.backend:
            self.backend.validate()
        if self.domain_info:
            self.domain_info.validate()
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend is not None:
            result['backend'] = self.backend.to_map()
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        if self.description is not None:
            result['description'] = self.description
        if self.domain_info is not None:
            result['domainInfo'] = self.domain_info.to_map()
        if self.gateway_route_id is not None:
            result['gatewayRouteId'] = self.gateway_route_id
        if self.match is not None:
            result['match'] = self.match.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backend') is not None:
            temp_model = GatewayRouteBackend()
            self.backend = temp_model.from_map(m['backend'])
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domainInfo') is not None:
            temp_model = GatewayRouteDomainInfo()
            self.domain_info = temp_model.from_map(m['domainInfo'])
        if m.get('gatewayRouteId') is not None:
            self.gateway_route_id = m.get('gatewayRouteId')
        if m.get('match') is not None:
            temp_model = HttpRouteMatch()
            self.match = temp_model.from_map(m['match'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')
        return self


class ListGatewayRoutesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListGatewayRoutesResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
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
            for k in m.get('items'):
                temp_model = ListGatewayRoutesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListGatewayRoutesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListGatewayRoutesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListGatewayRoutesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListGatewayRoutesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGatewayRoutesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListGatewayRoutesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGatewayServicesRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        source_type: str = None,
    ):
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        return self


class ListGatewayServicesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[GatewayService] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
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
            for k in m.get('items'):
                temp_model = GatewayService()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListGatewayServicesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListGatewayServicesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListGatewayServicesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListGatewayServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGatewayServicesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListGatewayServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGatewaysRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        keyword: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.gateway_id = gateway_id
        self.keyword = keyword
        self.name = name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.name is not None:
            result['name'] = self.name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListGatewaysResponseBodyDataItemsLoadBalancersPorts(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class ListGatewaysResponseBodyDataItemsLoadBalancers(TeaModel):
    def __init__(
        self,
        address: str = None,
        address_ip_version: str = None,
        address_type: str = None,
        gateway_default: bool = None,
        load_balancer_id: str = None,
        mode: str = None,
        ports: List[ListGatewaysResponseBodyDataItemsLoadBalancersPorts] = None,
        status: str = None,
        type: str = None,
    ):
        self.address = address
        self.address_ip_version = address_ip_version
        self.address_type = address_type
        self.gateway_default = gateway_default
        self.load_balancer_id = load_balancer_id
        self.mode = mode
        self.ports = ports
        self.status = status
        self.type = type

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.address_ip_version is not None:
            result['addressIpVersion'] = self.address_ip_version
        if self.address_type is not None:
            result['addressType'] = self.address_type
        if self.gateway_default is not None:
            result['gatewayDefault'] = self.gateway_default
        if self.load_balancer_id is not None:
            result['loadBalancerId'] = self.load_balancer_id
        if self.mode is not None:
            result['mode'] = self.mode
        result['ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('addressIpVersion') is not None:
            self.address_ip_version = m.get('addressIpVersion')
        if m.get('addressType') is not None:
            self.address_type = m.get('addressType')
        if m.get('gatewayDefault') is not None:
            self.gateway_default = m.get('gatewayDefault')
        if m.get('loadBalancerId') is not None:
            self.load_balancer_id = m.get('loadBalancerId')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        self.ports = []
        if m.get('ports') is not None:
            for k in m.get('ports'):
                temp_model = ListGatewaysResponseBodyDataItemsLoadBalancersPorts()
                self.ports.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListGatewaysResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        create_from: str = None,
        create_timestamp: int = None,
        expire_timestamp: int = None,
        gateway_id: str = None,
        load_balancers: List[ListGatewaysResponseBodyDataItemsLoadBalancers] = None,
        name: str = None,
        replicas: str = None,
        spec: str = None,
        status: str = None,
        target_version: str = None,
        update_timestamp: int = None,
        version: str = None,
    ):
        self.charge_type = charge_type
        self.create_from = create_from
        self.create_timestamp = create_timestamp
        self.expire_timestamp = expire_timestamp
        self.gateway_id = gateway_id
        self.load_balancers = load_balancers
        self.name = name
        self.replicas = replicas
        self.spec = spec
        self.status = status
        self.target_version = target_version
        self.update_timestamp = update_timestamp
        self.version = version

    def validate(self):
        if self.load_balancers:
            for k in self.load_balancers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.create_from is not None:
            result['createFrom'] = self.create_from
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        if self.expire_timestamp is not None:
            result['expireTimestamp'] = self.expire_timestamp
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        result['loadBalancers'] = []
        if self.load_balancers is not None:
            for k in self.load_balancers:
                result['loadBalancers'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.replicas is not None:
            result['replicas'] = self.replicas
        if self.spec is not None:
            result['spec'] = self.spec
        if self.status is not None:
            result['status'] = self.status
        if self.target_version is not None:
            result['targetVersion'] = self.target_version
        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('createFrom') is not None:
            self.create_from = m.get('createFrom')
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        if m.get('expireTimestamp') is not None:
            self.expire_timestamp = m.get('expireTimestamp')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        self.load_balancers = []
        if m.get('loadBalancers') is not None:
            for k in m.get('loadBalancers'):
                temp_model = ListGatewaysResponseBodyDataItemsLoadBalancers()
                self.load_balancers.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('targetVersion') is not None:
            self.target_version = m.get('targetVersion')
        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListGatewaysResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListGatewaysResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
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
            for k in m.get('items'):
                temp_model = ListGatewaysResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListGatewaysResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListGatewaysResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListGatewaysResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListGatewaysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGatewaysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListGatewaysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHttpApiOperationsRequest(TeaModel):
    def __init__(
        self,
        method: str = None,
        name_like: str = None,
        page_number: int = None,
        page_size: int = None,
        path_like: str = None,
    ):
        self.method = method
        self.name_like = name_like
        self.page_number = page_number
        self.page_size = page_size
        self.path_like = path_like

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method is not None:
            result['method'] = self.method
        if self.name_like is not None:
            result['nameLike'] = self.name_like
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.path_like is not None:
            result['pathLike'] = self.path_like
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('nameLike') is not None:
            self.name_like = m.get('nameLike')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('pathLike') is not None:
            self.path_like = m.get('pathLike')
        return self


class ListHttpApiOperationsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[HttpApiOperationInfo] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
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
            for k in m.get('items'):
                temp_model = HttpApiOperationInfo()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListHttpApiOperationsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListHttpApiOperationsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListHttpApiOperationsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListHttpApiOperationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHttpApiOperationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListHttpApiOperationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHttpApisRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        published_only: bool = None,
    ):
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.published_only = published_only

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.published_only is not None:
            result['publishedOnly'] = self.published_only
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('publishedOnly') is not None:
            self.published_only = m.get('publishedOnly')
        return self


class ListHttpApisResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[HttpApiInfoByName] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
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
            for k in m.get('items'):
                temp_model = HttpApiInfoByName()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListHttpApisResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListHttpApisResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListHttpApisResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListHttpApisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHttpApisResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListHttpApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OfflineGatewayRouteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class OfflineGatewayRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OfflineGatewayRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OfflineGatewayRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OfflineHttpApiRequest(TeaModel):
    def __init__(
        self,
        environment_id: str = None,
    ):
        # This parameter is required.
        self.environment_id = environment_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        return self


class OfflineHttpApiResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class OfflineHttpApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OfflineHttpApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OfflineHttpApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishGatewayRouteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class PublishGatewayRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishGatewayRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PublishGatewayRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishHttpApiRequestEnvironmentCloudProductConfigContainerServiceConfigs(TeaModel):
    def __init__(
        self,
        match: HttpApiBackendMatchConditions = None,
        name: str = None,
        namespace: str = None,
        port: int = None,
        protocol: str = None,
        weight: int = None,
    ):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('match') is not None:
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
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


class PublishHttpApiRequestEnvironmentCloudProductConfigFunctionConfigs(TeaModel):
    def __init__(
        self,
        match: HttpApiBackendMatchConditions = None,
        name: str = None,
        quanlifer: str = None,
        weight: int = None,
    ):
        self.match = match
        self.name = name
        self.quanlifer = quanlifer
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match is not None:
            result['match'] = self.match.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.quanlifer is not None:
            result['quanlifer'] = self.quanlifer
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('match') is not None:
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('quanlifer') is not None:
            self.quanlifer = m.get('quanlifer')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class PublishHttpApiRequestEnvironmentCloudProductConfigMseNacosConfigs(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        match: HttpApiBackendMatchConditions = None,
        name: str = None,
        namespace: str = None,
        weight: str = None,
    ):
        self.group_name = group_name
        self.match = match
        self.name = name
        self.namespace = namespace
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('match') is not None:
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class PublishHttpApiRequestEnvironmentCloudProductConfig(TeaModel):
    def __init__(
        self,
        cloud_product_type: str = None,
        container_service_configs: List[PublishHttpApiRequestEnvironmentCloudProductConfigContainerServiceConfigs] = None,
        function_configs: List[PublishHttpApiRequestEnvironmentCloudProductConfigFunctionConfigs] = None,
        mse_nacos_configs: List[PublishHttpApiRequestEnvironmentCloudProductConfigMseNacosConfigs] = None,
    ):
        self.cloud_product_type = cloud_product_type
        self.container_service_configs = container_service_configs
        self.function_configs = function_configs
        self.mse_nacos_configs = mse_nacos_configs

    def validate(self):
        if self.container_service_configs:
            for k in self.container_service_configs:
                if k:
                    k.validate()
        if self.function_configs:
            for k in self.function_configs:
                if k:
                    k.validate()
        if self.mse_nacos_configs:
            for k in self.mse_nacos_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_product_type is not None:
            result['cloudProductType'] = self.cloud_product_type
        result['containerServiceConfigs'] = []
        if self.container_service_configs is not None:
            for k in self.container_service_configs:
                result['containerServiceConfigs'].append(k.to_map() if k else None)
        result['functionConfigs'] = []
        if self.function_configs is not None:
            for k in self.function_configs:
                result['functionConfigs'].append(k.to_map() if k else None)
        result['mseNacosConfigs'] = []
        if self.mse_nacos_configs is not None:
            for k in self.mse_nacos_configs:
                result['mseNacosConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cloudProductType') is not None:
            self.cloud_product_type = m.get('cloudProductType')
        self.container_service_configs = []
        if m.get('containerServiceConfigs') is not None:
            for k in m.get('containerServiceConfigs'):
                temp_model = PublishHttpApiRequestEnvironmentCloudProductConfigContainerServiceConfigs()
                self.container_service_configs.append(temp_model.from_map(k))
        self.function_configs = []
        if m.get('functionConfigs') is not None:
            for k in m.get('functionConfigs'):
                temp_model = PublishHttpApiRequestEnvironmentCloudProductConfigFunctionConfigs()
                self.function_configs.append(temp_model.from_map(k))
        self.mse_nacos_configs = []
        if m.get('mseNacosConfigs') is not None:
            for k in m.get('mseNacosConfigs'):
                temp_model = PublishHttpApiRequestEnvironmentCloudProductConfigMseNacosConfigs()
                self.mse_nacos_configs.append(temp_model.from_map(k))
        return self


class PublishHttpApiRequestEnvironmentDnsConfigs(TeaModel):
    def __init__(
        self,
        dns_list: List[str] = None,
        match: HttpApiBackendMatchConditions = None,
        weight: int = None,
    ):
        self.dns_list = dns_list
        self.match = match
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class PublishHttpApiRequestEnvironmentServiceConfigs(TeaModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        match: HttpApiBackendMatchConditions = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class PublishHttpApiRequestEnvironmentVipConfigs(TeaModel):
    def __init__(
        self,
        endpoints: List[str] = None,
        match: HttpApiBackendMatchConditions = None,
        weight: int = None,
    ):
        self.endpoints = endpoints
        self.match = match
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class PublishHttpApiRequestEnvironment(TeaModel):
    def __init__(
        self,
        backend_scene: str = None,
        backend_type: str = None,
        cloud_product_config: PublishHttpApiRequestEnvironmentCloudProductConfig = None,
        custom_domain_ids: List[str] = None,
        dns_configs: List[PublishHttpApiRequestEnvironmentDnsConfigs] = None,
        environment_id: str = None,
        service_configs: List[PublishHttpApiRequestEnvironmentServiceConfigs] = None,
        vip_configs: List[PublishHttpApiRequestEnvironmentVipConfigs] = None,
    ):
        self.backend_scene = backend_scene
        self.backend_type = backend_type
        self.cloud_product_config = cloud_product_config
        self.custom_domain_ids = custom_domain_ids
        self.dns_configs = dns_configs
        self.environment_id = environment_id
        self.service_configs = service_configs
        self.vip_configs = vip_configs

    def validate(self):
        if self.cloud_product_config:
            self.cloud_product_config.validate()
        if self.dns_configs:
            for k in self.dns_configs:
                if k:
                    k.validate()
        if self.service_configs:
            for k in self.service_configs:
                if k:
                    k.validate()
        if self.vip_configs:
            for k in self.vip_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_scene is not None:
            result['backendScene'] = self.backend_scene
        if self.backend_type is not None:
            result['backendType'] = self.backend_type
        if self.cloud_product_config is not None:
            result['cloudProductConfig'] = self.cloud_product_config.to_map()
        if self.custom_domain_ids is not None:
            result['customDomainIds'] = self.custom_domain_ids
        result['dnsConfigs'] = []
        if self.dns_configs is not None:
            for k in self.dns_configs:
                result['dnsConfigs'].append(k.to_map() if k else None)
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k in self.service_configs:
                result['serviceConfigs'].append(k.to_map() if k else None)
        result['vipConfigs'] = []
        if self.vip_configs is not None:
            for k in self.vip_configs:
                result['vipConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backendScene') is not None:
            self.backend_scene = m.get('backendScene')
        if m.get('backendType') is not None:
            self.backend_type = m.get('backendType')
        if m.get('cloudProductConfig') is not None:
            temp_model = PublishHttpApiRequestEnvironmentCloudProductConfig()
            self.cloud_product_config = temp_model.from_map(m['cloudProductConfig'])
        if m.get('customDomainIds') is not None:
            self.custom_domain_ids = m.get('customDomainIds')
        self.dns_configs = []
        if m.get('dnsConfigs') is not None:
            for k in m.get('dnsConfigs'):
                temp_model = PublishHttpApiRequestEnvironmentDnsConfigs()
                self.dns_configs.append(temp_model.from_map(k))
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k in m.get('serviceConfigs'):
                temp_model = PublishHttpApiRequestEnvironmentServiceConfigs()
                self.service_configs.append(temp_model.from_map(k))
        self.vip_configs = []
        if m.get('vipConfigs') is not None:
            for k in m.get('vipConfigs'):
                temp_model = PublishHttpApiRequestEnvironmentVipConfigs()
                self.vip_configs.append(temp_model.from_map(k))
        return self


class PublishHttpApiRequest(TeaModel):
    def __init__(
        self,
        allow_overwrite: bool = None,
        description: str = None,
        environment: PublishHttpApiRequestEnvironment = None,
        revision_id: str = None,
    ):
        self.allow_overwrite = allow_overwrite
        self.description = description
        self.environment = environment
        self.revision_id = revision_id

    def validate(self):
        if self.environment:
            self.environment.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_overwrite is not None:
            result['allowOverwrite'] = self.allow_overwrite
        if self.description is not None:
            result['description'] = self.description
        if self.environment is not None:
            result['environment'] = self.environment.to_map()
        if self.revision_id is not None:
            result['revisionId'] = self.revision_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowOverwrite') is not None:
            self.allow_overwrite = m.get('allowOverwrite')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('environment') is not None:
            temp_model = PublishHttpApiRequestEnvironment()
            self.environment = temp_model.from_map(m['environment'])
        if m.get('revisionId') is not None:
            self.revision_id = m.get('revisionId')
        return self


class PublishHttpApiResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class PublishHttpApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishHttpApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PublishHttpApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDomainRequest(TeaModel):
    def __init__(
        self,
        ca_cert_indentifier: str = None,
        cert_indentifier: str = None,
        force_https: bool = None,
        http_2option: str = None,
        protocol: str = None,
        tls_max: str = None,
        tls_min: str = None,
    ):
        self.ca_cert_indentifier = ca_cert_indentifier
        self.cert_indentifier = cert_indentifier
        self.force_https = force_https
        self.http_2option = http_2option
        # This parameter is required.
        self.protocol = protocol
        self.tls_max = tls_max
        self.tls_min = tls_min

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_cert_indentifier is not None:
            result['caCertIndentifier'] = self.ca_cert_indentifier
        if self.cert_indentifier is not None:
            result['certIndentifier'] = self.cert_indentifier
        if self.force_https is not None:
            result['forceHttps'] = self.force_https
        if self.http_2option is not None:
            result['http2Option'] = self.http_2option
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.tls_max is not None:
            result['tlsMax'] = self.tls_max
        if self.tls_min is not None:
            result['tlsMin'] = self.tls_min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caCertIndentifier') is not None:
            self.ca_cert_indentifier = m.get('caCertIndentifier')
        if m.get('certIndentifier') is not None:
            self.cert_indentifier = m.get('certIndentifier')
        if m.get('forceHttps') is not None:
            self.force_https = m.get('forceHttps')
        if m.get('http2Option') is not None:
            self.http_2option = m.get('http2Option')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('tlsMax') is not None:
            self.tls_max = m.get('tlsMax')
        if m.get('tlsMin') is not None:
            self.tls_min = m.get('tlsMin')
        return self


class UpdateDomainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnvironmentRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
        description: str = None,
    ):
        # This parameter is required.
        self.alias = alias
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateEnvironmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayRouteRequest(TeaModel):
    def __init__(
        self,
        backend_config: GatewayRouteBackendConfig = None,
        description: str = None,
        domain_config: GatewayRouteDomainConfig = None,
        match: HttpRouteMatch = None,
    ):
        self.backend_config = backend_config
        self.description = description
        self.domain_config = domain_config
        self.match = match

    def validate(self):
        if self.backend_config:
            self.backend_config.validate()
        if self.domain_config:
            self.domain_config.validate()
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_config is not None:
            result['backendConfig'] = self.backend_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.domain_config is not None:
            result['domainConfig'] = self.domain_config.to_map()
        if self.match is not None:
            result['match'] = self.match.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backendConfig') is not None:
            temp_model = GatewayRouteBackendConfig()
            self.backend_config = temp_model.from_map(m['backendConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domainConfig') is not None:
            temp_model = GatewayRouteDomainConfig()
            self.domain_config = temp_model.from_map(m['domainConfig'])
        if m.get('match') is not None:
            temp_model = HttpRouteMatch()
            self.match = temp_model.from_map(m['match'])
        return self


class UpdateGatewayRouteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateGatewayRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateGatewayRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateGatewayRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayServiceRequest(TeaModel):
    def __init__(
        self,
        addresses: List[str] = None,
        port: int = None,
    ):
        self.addresses = addresses
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['addresses'] = self.addresses
        if self.port is not None:
            result['port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addresses') is not None:
            self.addresses = m.get('addresses')
        if m.get('port') is not None:
            self.port = m.get('port')
        return self


class UpdateGatewayServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateGatewayServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateGatewayServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateGatewayServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayServiceVersionRequestLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class UpdateGatewayServiceVersionRequest(TeaModel):
    def __init__(
        self,
        labels: List[UpdateGatewayServiceVersionRequestLabels] = None,
    ):
        self.labels = labels

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('labels') is not None:
            for k in m.get('labels'):
                temp_model = UpdateGatewayServiceVersionRequestLabels()
                self.labels.append(temp_model.from_map(k))
        return self


class UpdateGatewayServiceVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateGatewayServiceVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateGatewayServiceVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateGatewayServiceVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHttpApiRequest(TeaModel):
    def __init__(
        self,
        base_path: str = None,
        description: str = None,
        protocols: List[str] = None,
        version_config: HttpApiVersionConfig = None,
    ):
        # This parameter is required.
        self.base_path = base_path
        self.description = description
        self.protocols = protocols
        self.version_config = version_config

    def validate(self):
        if self.version_config:
            self.version_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_path is not None:
            result['basePath'] = self.base_path
        if self.description is not None:
            result['description'] = self.description
        if self.protocols is not None:
            result['protocols'] = self.protocols
        if self.version_config is not None:
            result['versionConfig'] = self.version_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('protocols') is not None:
            self.protocols = m.get('protocols')
        if m.get('versionConfig') is not None:
            temp_model = HttpApiVersionConfig()
            self.version_config = temp_model.from_map(m['versionConfig'])
        return self


class UpdateHttpApiResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateHttpApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateHttpApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateHttpApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHttpApiOperationRequest(TeaModel):
    def __init__(
        self,
        operation: HttpApiOperation = None,
    ):
        self.operation = operation

    def validate(self):
        if self.operation:
            self.operation.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['operation'] = self.operation.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operation') is not None:
            temp_model = HttpApiOperation()
            self.operation = temp_model.from_map(m['operation'])
        return self


class UpdateHttpApiOperationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateHttpApiOperationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateHttpApiOperationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateHttpApiOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceSourceRequestK8sServiceSourceConfigIngressConfig(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        ingress_class: str = None,
        override_ingress_ip: bool = None,
        watch_namespace: str = None,
    ):
        self.enable = enable
        self.ingress_class = ingress_class
        self.override_ingress_ip = override_ingress_ip
        self.watch_namespace = watch_namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.ingress_class is not None:
            result['ingressClass'] = self.ingress_class
        if self.override_ingress_ip is not None:
            result['overrideIngressIp'] = self.override_ingress_ip
        if self.watch_namespace is not None:
            result['watchNamespace'] = self.watch_namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('ingressClass') is not None:
            self.ingress_class = m.get('ingressClass')
        if m.get('overrideIngressIp') is not None:
            self.override_ingress_ip = m.get('overrideIngressIp')
        if m.get('watchNamespace') is not None:
            self.watch_namespace = m.get('watchNamespace')
        return self


class UpdateServiceSourceRequestK8sServiceSourceConfig(TeaModel):
    def __init__(
        self,
        ingress_config: UpdateServiceSourceRequestK8sServiceSourceConfigIngressConfig = None,
    ):
        self.ingress_config = ingress_config

    def validate(self):
        if self.ingress_config:
            self.ingress_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_config is not None:
            result['ingressConfig'] = self.ingress_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ingressConfig') is not None:
            temp_model = UpdateServiceSourceRequestK8sServiceSourceConfigIngressConfig()
            self.ingress_config = temp_model.from_map(m['ingressConfig'])
        return self


class UpdateServiceSourceRequest(TeaModel):
    def __init__(
        self,
        k_8s_service_source_config: UpdateServiceSourceRequestK8sServiceSourceConfig = None,
    ):
        self.k_8s_service_source_config = k_8s_service_source_config

    def validate(self):
        if self.k_8s_service_source_config:
            self.k_8s_service_source_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.k_8s_service_source_config is not None:
            result['k8sServiceSourceConfig'] = self.k_8s_service_source_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('k8sServiceSourceConfig') is not None:
            temp_model = UpdateServiceSourceRequestK8sServiceSourceConfig()
            self.k_8s_service_source_config = temp_model.from_map(m['k8sServiceSourceConfig'])
        return self


class UpdateServiceSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateServiceSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateServiceSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


