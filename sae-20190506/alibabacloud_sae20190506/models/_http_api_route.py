# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class HttpApiRoute(DaraModel):
    def __init__(
        self,
        address_type: str = None,
        deploy_status: str = None,
        destination_type: str = None,
        domains: List[main_models.HttpApiRouteDomains] = None,
        environment_id: str = None,
        gateway_id: str = None,
        http_api_id: str = None,
        http_api_name: str = None,
        http_api_type: str = None,
        ingress_id: int = None,
        nacos_instance_id: str = None,
        nacos_namespace_id: str = None,
        name: str = None,
        namespace_id: str = None,
        policies: main_models.HttpApiRoutePolicies = None,
        predicates: main_models.HttpApiRoutePredicates = None,
        route_id: str = None,
        services: List[main_models.HttpApiRouteServices] = None,
        source_type: str = None,
    ):
        self.address_type = address_type
        self.deploy_status = deploy_status
        self.destination_type = destination_type
        self.domains = domains
        self.environment_id = environment_id
        self.gateway_id = gateway_id
        self.http_api_id = http_api_id
        self.http_api_name = http_api_name
        self.http_api_type = http_api_type
        self.ingress_id = ingress_id
        self.nacos_instance_id = nacos_instance_id
        self.nacos_namespace_id = nacos_namespace_id
        self.name = name
        self.namespace_id = namespace_id
        self.policies = policies
        self.predicates = predicates
        self.route_id = route_id
        self.services = services
        self.source_type = source_type

    def validate(self):
        if self.domains:
            for v1 in self.domains:
                 if v1:
                    v1.validate()
        if self.policies:
            self.policies.validate()
        if self.predicates:
            self.predicates.validate()
        if self.services:
            for v1 in self.services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.deploy_status is not None:
            result['DeployStatus'] = self.deploy_status

        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type

        result['Domains'] = []
        if self.domains is not None:
            for k1 in self.domains:
                result['Domains'].append(k1.to_map() if k1 else None)

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.http_api_id is not None:
            result['HttpApiId'] = self.http_api_id

        if self.http_api_name is not None:
            result['HttpApiName'] = self.http_api_name

        if self.http_api_type is not None:
            result['HttpApiType'] = self.http_api_type

        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id

        if self.nacos_instance_id is not None:
            result['NacosInstanceId'] = self.nacos_instance_id

        if self.nacos_namespace_id is not None:
            result['NacosNamespaceId'] = self.nacos_namespace_id

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.policies is not None:
            result['Policies'] = self.policies.to_map()

        if self.predicates is not None:
            result['Predicates'] = self.predicates.to_map()

        if self.route_id is not None:
            result['RouteId'] = self.route_id

        result['Services'] = []
        if self.services is not None:
            for k1 in self.services:
                result['Services'].append(k1.to_map() if k1 else None)

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('DeployStatus') is not None:
            self.deploy_status = m.get('DeployStatus')

        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

        self.domains = []
        if m.get('Domains') is not None:
            for k1 in m.get('Domains'):
                temp_model = main_models.HttpApiRouteDomains()
                self.domains.append(temp_model.from_map(k1))

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('HttpApiId') is not None:
            self.http_api_id = m.get('HttpApiId')

        if m.get('HttpApiName') is not None:
            self.http_api_name = m.get('HttpApiName')

        if m.get('HttpApiType') is not None:
            self.http_api_type = m.get('HttpApiType')

        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')

        if m.get('NacosInstanceId') is not None:
            self.nacos_instance_id = m.get('NacosInstanceId')

        if m.get('NacosNamespaceId') is not None:
            self.nacos_namespace_id = m.get('NacosNamespaceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('Policies') is not None:
            temp_model = main_models.HttpApiRoutePolicies()
            self.policies = temp_model.from_map(m.get('Policies'))

        if m.get('Predicates') is not None:
            temp_model = main_models.HttpApiRoutePredicates()
            self.predicates = temp_model.from_map(m.get('Predicates'))

        if m.get('RouteId') is not None:
            self.route_id = m.get('RouteId')

        self.services = []
        if m.get('Services') is not None:
            for k1 in m.get('Services'):
                temp_model = main_models.HttpApiRouteServices()
                self.services.append(temp_model.from_map(k1))

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

class HttpApiRouteServices(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        service_id: str = None,
        service_name: str = None,
        service_port: int = None,
        service_protocol: str = None,
        service_weight: int = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.service_id = service_id
        self.service_name = service_name
        self.service_port = service_port
        self.service_protocol = service_protocol
        self.service_weight = service_weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_port is not None:
            result['ServicePort'] = self.service_port

        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol

        if self.service_weight is not None:
            result['ServiceWeight'] = self.service_weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')

        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')

        if m.get('ServiceWeight') is not None:
            self.service_weight = m.get('ServiceWeight')

        return self

class HttpApiRoutePredicates(DaraModel):
    def __init__(
        self,
        header_predicates: List[main_models.HttpApiRoutePredicatesHeaderPredicates] = None,
        method_predicates: List[str] = None,
        path_predicates: main_models.HttpApiRoutePredicatesPathPredicates = None,
        query_predicates: List[main_models.HttpApiRoutePredicatesQueryPredicates] = None,
    ):
        self.header_predicates = header_predicates
        self.method_predicates = method_predicates
        self.path_predicates = path_predicates
        self.query_predicates = query_predicates

    def validate(self):
        if self.header_predicates:
            for v1 in self.header_predicates:
                 if v1:
                    v1.validate()
        if self.path_predicates:
            self.path_predicates.validate()
        if self.query_predicates:
            for v1 in self.query_predicates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HeaderPredicates'] = []
        if self.header_predicates is not None:
            for k1 in self.header_predicates:
                result['HeaderPredicates'].append(k1.to_map() if k1 else None)

        if self.method_predicates is not None:
            result['MethodPredicates'] = self.method_predicates

        if self.path_predicates is not None:
            result['PathPredicates'] = self.path_predicates.to_map()

        result['QueryPredicates'] = []
        if self.query_predicates is not None:
            for k1 in self.query_predicates:
                result['QueryPredicates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.header_predicates = []
        if m.get('HeaderPredicates') is not None:
            for k1 in m.get('HeaderPredicates'):
                temp_model = main_models.HttpApiRoutePredicatesHeaderPredicates()
                self.header_predicates.append(temp_model.from_map(k1))

        if m.get('MethodPredicates') is not None:
            self.method_predicates = m.get('MethodPredicates')

        if m.get('PathPredicates') is not None:
            temp_model = main_models.HttpApiRoutePredicatesPathPredicates()
            self.path_predicates = temp_model.from_map(m.get('PathPredicates'))

        self.query_predicates = []
        if m.get('QueryPredicates') is not None:
            for k1 in m.get('QueryPredicates'):
                temp_model = main_models.HttpApiRoutePredicatesQueryPredicates()
                self.query_predicates.append(temp_model.from_map(k1))

        return self

class HttpApiRoutePredicatesQueryPredicates(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class HttpApiRoutePredicatesPathPredicates(DaraModel):
    def __init__(
        self,
        ignore_case: bool = None,
        path: str = None,
        type: str = None,
    ):
        self.ignore_case = ignore_case
        self.path = path
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ignore_case is not None:
            result['IgnoreCase'] = self.ignore_case

        if self.path is not None:
            result['Path'] = self.path

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoreCase') is not None:
            self.ignore_case = m.get('IgnoreCase')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class HttpApiRoutePredicatesHeaderPredicates(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class HttpApiRoutePolicies(DaraModel):
    def __init__(
        self,
        fallback: main_models.HttpApiRoutePoliciesFallback = None,
        retry: main_models.HttpApiRoutePoliciesRetry = None,
        timeout: main_models.HttpApiRoutePoliciesTimeout = None,
    ):
        self.fallback = fallback
        self.retry = retry
        self.timeout = timeout

    def validate(self):
        if self.fallback:
            self.fallback.validate()
        if self.retry:
            self.retry.validate()
        if self.timeout:
            self.timeout.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fallback is not None:
            result['Fallback'] = self.fallback.to_map()

        if self.retry is not None:
            result['Retry'] = self.retry.to_map()

        if self.timeout is not None:
            result['Timeout'] = self.timeout.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fallback') is not None:
            temp_model = main_models.HttpApiRoutePoliciesFallback()
            self.fallback = temp_model.from_map(m.get('Fallback'))

        if m.get('Retry') is not None:
            temp_model = main_models.HttpApiRoutePoliciesRetry()
            self.retry = temp_model.from_map(m.get('Retry'))

        if m.get('Timeout') is not None:
            temp_model = main_models.HttpApiRoutePoliciesTimeout()
            self.timeout = temp_model.from_map(m.get('Timeout'))

        return self

class HttpApiRoutePoliciesTimeout(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        time_unit: str = None,
        unit_num: int = None,
    ):
        self.enable = enable
        self.time_unit = time_unit
        self.unit_num = unit_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit

        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')

        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')

        return self

class HttpApiRoutePoliciesRetry(DaraModel):
    def __init__(
        self,
        attempts: int = None,
        enable: bool = None,
        http_codes: List[str] = None,
        retry_on: List[str] = None,
    ):
        self.attempts = attempts
        self.enable = enable
        self.http_codes = http_codes
        self.retry_on = retry_on

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attempts is not None:
            result['Attempts'] = self.attempts

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.http_codes is not None:
            result['HttpCodes'] = self.http_codes

        if self.retry_on is not None:
            result['RetryOn'] = self.retry_on

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attempts') is not None:
            self.attempts = m.get('Attempts')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('HttpCodes') is not None:
            self.http_codes = m.get('HttpCodes')

        if m.get('RetryOn') is not None:
            self.retry_on = m.get('RetryOn')

        return self

class HttpApiRoutePoliciesFallback(DaraModel):
    def __init__(
        self,
        destinations: List[main_models.HttpApiRoutePoliciesFallbackDestinations] = None,
        enable: bool = None,
    ):
        self.destinations = destinations
        self.enable = enable

    def validate(self):
        if self.destinations:
            for v1 in self.destinations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Destinations'] = []
        if self.destinations is not None:
            for k1 in self.destinations:
                result['Destinations'].append(k1.to_map() if k1 else None)

        if self.enable is not None:
            result['Enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.destinations = []
        if m.get('Destinations') is not None:
            for k1 in m.get('Destinations'):
                temp_model = main_models.HttpApiRoutePoliciesFallbackDestinations()
                self.destinations.append(temp_model.from_map(k1))

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        return self

class HttpApiRoutePoliciesFallbackDestinations(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        service_id: str = None,
        service_name: str = None,
        service_port: int = None,
        service_protocol: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.service_id = service_id
        self.service_name = service_name
        self.service_port = service_port
        self.service_protocol = service_protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_port is not None:
            result['ServicePort'] = self.service_port

        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')

        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')

        return self

class HttpApiRouteDomains(DaraModel):
    def __init__(
        self,
        domain_id: str = None,
        domain_name: str = None,
    ):
        self.domain_id = domain_id
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        return self

