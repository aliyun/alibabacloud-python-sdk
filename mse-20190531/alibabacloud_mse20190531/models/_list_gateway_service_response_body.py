# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListGatewayServiceResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListGatewayServiceResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The return value.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # - `true`: The request is successful.
        # - `false`: The request fails.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListGatewayServiceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListGatewayServiceResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        result: List[main_models.ListGatewayServiceResponseBodyDataResult] = None,
        total_size: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The maximum number of records per page. Default value: 10.
        self.page_size = page_size
        # The returned collection.
        self.result = result
        # The total number of entries.
        self.total_size = total_size

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListGatewayServiceResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListGatewayServiceResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        dns_server_list: List[str] = None,
        gateway_id: int = None,
        gateway_traffic_policy: main_models.ListGatewayServiceResponseBodyDataResultGatewayTrafficPolicy = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        group_name: str = None,
        healeh_status: str = None,
        health_check: bool = None,
        health_check_info: main_models.ListGatewayServiceResponseBodyDataResultHealthCheckInfo = None,
        health_status: str = None,
        id: int = None,
        ips: List[str] = None,
        meta_info: str = None,
        name: str = None,
        namespace: str = None,
        ports: List[int] = None,
        service_fqdn: str = None,
        service_name_in_registry: str = None,
        service_port: int = None,
        service_protocol: str = None,
        source_id: int = None,
        source_type: str = None,
        unhealthy_endpoints: List[str] = None,
        versions: List[main_models.ListGatewayServiceResponseBodyDataResultVersions] = None,
    ):
        # The DNS server list (for DNS domain name service only).
        self.dns_server_list = dns_server_list
        # The gateway ID.
        self.gateway_id = gateway_id
        # The traffic management policy.
        self.gateway_traffic_policy = gateway_traffic_policy
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The time when the record was created.
        self.gmt_create = gmt_create
        # The time when the record was modified.
        self.gmt_modified = gmt_modified
        # The group name.
        self.group_name = group_name
        # The health status. Valid values:
        # 
        # - Health
        # 
        # - Unhealthy
        # 
        # - Unknown
        self.healeh_status = healeh_status
        # Indicates whether health checks are performed.
        self.health_check = health_check
        # The health check information.
        self.health_check_info = health_check_info
        # The health status. Valid values:
        # 
        # - Health
        # 
        # - Unhealthy
        # 
        # - Unknown
        self.health_status = health_status
        # The ID.
        self.id = id
        # The IP address list.
        self.ips = ips
        # The metadata or IP address list.
        self.meta_info = meta_info
        # The service name.
        self.name = name
        # The namespace.
        self.namespace = namespace
        # The array of ports.
        self.ports = ports
        # The fully qualified domain name (FQDN) of the service.
        self.service_fqdn = service_fqdn
        # The original service name in the registry.
        self.service_name_in_registry = service_name_in_registry
        # The service port.
        self.service_port = service_port
        # The service protocol.
        self.service_protocol = service_protocol
        # The source ID.
        self.source_id = source_id
        # The source type.
        self.source_type = source_type
        # The array of unhealthy endpoints.
        self.unhealthy_endpoints = unhealthy_endpoints
        # The service versions.
        self.versions = versions

    def validate(self):
        if self.gateway_traffic_policy:
            self.gateway_traffic_policy.validate()
        if self.health_check_info:
            self.health_check_info.validate()
        if self.versions:
            for v1 in self.versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_server_list is not None:
            result['DnsServerList'] = self.dns_server_list

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_traffic_policy is not None:
            result['GatewayTrafficPolicy'] = self.gateway_traffic_policy.to_map()

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.healeh_status is not None:
            result['HealehStatus'] = self.healeh_status

        if self.health_check is not None:
            result['HealthCheck'] = self.health_check

        if self.health_check_info is not None:
            result['HealthCheckInfo'] = self.health_check_info.to_map()

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        if self.id is not None:
            result['Id'] = self.id

        if self.ips is not None:
            result['Ips'] = self.ips

        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.ports is not None:
            result['Ports'] = self.ports

        if self.service_fqdn is not None:
            result['ServiceFQDN'] = self.service_fqdn

        if self.service_name_in_registry is not None:
            result['ServiceNameInRegistry'] = self.service_name_in_registry

        if self.service_port is not None:
            result['ServicePort'] = self.service_port

        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.unhealthy_endpoints is not None:
            result['UnhealthyEndpoints'] = self.unhealthy_endpoints

        result['Versions'] = []
        if self.versions is not None:
            for k1 in self.versions:
                result['Versions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsServerList') is not None:
            self.dns_server_list = m.get('DnsServerList')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayTrafficPolicy') is not None:
            temp_model = main_models.ListGatewayServiceResponseBodyDataResultGatewayTrafficPolicy()
            self.gateway_traffic_policy = temp_model.from_map(m.get('GatewayTrafficPolicy'))

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('HealehStatus') is not None:
            self.healeh_status = m.get('HealehStatus')

        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')

        if m.get('HealthCheckInfo') is not None:
            temp_model = main_models.ListGatewayServiceResponseBodyDataResultHealthCheckInfo()
            self.health_check_info = temp_model.from_map(m.get('HealthCheckInfo'))

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Ips') is not None:
            self.ips = m.get('Ips')

        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Ports') is not None:
            self.ports = m.get('Ports')

        if m.get('ServiceFQDN') is not None:
            self.service_fqdn = m.get('ServiceFQDN')

        if m.get('ServiceNameInRegistry') is not None:
            self.service_name_in_registry = m.get('ServiceNameInRegistry')

        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')

        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('UnhealthyEndpoints') is not None:
            self.unhealthy_endpoints = m.get('UnhealthyEndpoints')

        self.versions = []
        if m.get('Versions') is not None:
            for k1 in m.get('Versions'):
                temp_model = main_models.ListGatewayServiceResponseBodyDataResultVersions()
                self.versions.append(temp_model.from_map(k1))

        return self

class ListGatewayServiceResponseBodyDataResultVersions(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The version name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ListGatewayServiceResponseBodyDataResultHealthCheckInfo(DaraModel):
    def __init__(
        self,
        check: bool = None,
        expected_statuses: List[int] = None,
        healthy_threshold: int = None,
        http_host: str = None,
        http_path: str = None,
        interval: int = None,
        protocol: str = None,
        timeout: int = None,
        unhealthy_threshold: int = None,
    ):
        # Indicates whether the check is performed.
        self.check = check
        # The expected HTTP status codes for health checks.
        self.expected_statuses = expected_statuses
        # The healthy threshold.
        self.healthy_threshold = healthy_threshold
        # The HTTP request address for health checks.
        self.http_host = http_host
        # The HTTP request path for health checks.
        self.http_path = http_path
        # The health check interval.
        self.interval = interval
        # The network protocol.
        self.protocol = protocol
        # The timeout period.
        self.timeout = timeout
        # The unhealthy threshold.
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check is not None:
            result['Check'] = self.check

        if self.expected_statuses is not None:
            result['ExpectedStatuses'] = self.expected_statuses

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.http_host is not None:
            result['HttpHost'] = self.http_host

        if self.http_path is not None:
            result['HttpPath'] = self.http_path

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Check') is not None:
            self.check = m.get('Check')

        if m.get('ExpectedStatuses') is not None:
            self.expected_statuses = m.get('ExpectedStatuses')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('HttpHost') is not None:
            self.http_host = m.get('HttpHost')

        if m.get('HttpPath') is not None:
            self.http_path = m.get('HttpPath')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        return self

class ListGatewayServiceResponseBodyDataResultGatewayTrafficPolicy(DaraModel):
    def __init__(
        self,
        load_balancer_settings: main_models.ListGatewayServiceResponseBodyDataResultGatewayTrafficPolicyLoadBalancerSettings = None,
        tls: main_models.ListGatewayServiceResponseBodyDataResultGatewayTrafficPolicyTls = None,
    ):
        # The load balancing settings.
        self.load_balancer_settings = load_balancer_settings
        # The TLS.
        self.tls = tls

    def validate(self):
        if self.load_balancer_settings:
            self.load_balancer_settings.validate()
        if self.tls:
            self.tls.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.load_balancer_settings is not None:
            result['LoadBalancerSettings'] = self.load_balancer_settings.to_map()

        if self.tls is not None:
            result['Tls'] = self.tls.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerSettings') is not None:
            temp_model = main_models.ListGatewayServiceResponseBodyDataResultGatewayTrafficPolicyLoadBalancerSettings()
            self.load_balancer_settings = temp_model.from_map(m.get('LoadBalancerSettings'))

        if m.get('Tls') is not None:
            temp_model = main_models.ListGatewayServiceResponseBodyDataResultGatewayTrafficPolicyTls()
            self.tls = temp_model.from_map(m.get('Tls'))

        return self

class ListGatewayServiceResponseBodyDataResultGatewayTrafficPolicyTls(DaraModel):
    def __init__(
        self,
        ca_cert_content: str = None,
        ca_cert_id: str = None,
        cert_id: str = None,
        mode: str = None,
        sni: str = None,
        subject_alt_names: List[str] = None,
    ):
        # The public key of the CA certificate.
        self.ca_cert_content = ca_cert_content
        # The CA certificate ID.
        self.ca_cert_id = ca_cert_id
        # The certificate ID.
        self.cert_id = cert_id
        # The TLS mode. Valid values:
        # 
        # - DISABLE
        # 
        # - SIMPLE
        # 
        # - MUTUAL
        # 
        # - ISTIO_MUTUAL
        self.mode = mode
        # The service name identity.
        self.sni = sni
        # The array of subject alternative names.
        self.subject_alt_names = subject_alt_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ca_cert_content is not None:
            result['CaCertContent'] = self.ca_cert_content

        if self.ca_cert_id is not None:
            result['CaCertId'] = self.ca_cert_id

        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.sni is not None:
            result['Sni'] = self.sni

        if self.subject_alt_names is not None:
            result['SubjectAltNames'] = self.subject_alt_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaCertContent') is not None:
            self.ca_cert_content = m.get('CaCertContent')

        if m.get('CaCertId') is not None:
            self.ca_cert_id = m.get('CaCertId')

        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Sni') is not None:
            self.sni = m.get('Sni')

        if m.get('SubjectAltNames') is not None:
            self.subject_alt_names = m.get('SubjectAltNames')

        return self

class ListGatewayServiceResponseBodyDataResultGatewayTrafficPolicyLoadBalancerSettings(DaraModel):
    def __init__(
        self,
        consistent_hash_lbconfig: main_models.ListGatewayServiceResponseBodyDataResultGatewayTrafficPolicyLoadBalancerSettingsConsistentHashLBConfig = None,
        loadbalancer_type: str = None,
        warmup_duration: int = None,
    ):
        # The consistent hashing configuration.
        self.consistent_hash_lbconfig = consistent_hash_lbconfig
        # The load balancing policy. Valid values:
        # 
        # - ROUND_ROBIN
        # 
        # - LEAST_CONN
        # 
        # - RANDOM
        # 
        # - CONSISTENT_HASH
        self.loadbalancer_type = loadbalancer_type
        # The warm-up duration for the minimum number of requests.
        self.warmup_duration = warmup_duration

    def validate(self):
        if self.consistent_hash_lbconfig:
            self.consistent_hash_lbconfig.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consistent_hash_lbconfig is not None:
            result['ConsistentHashLBConfig'] = self.consistent_hash_lbconfig.to_map()

        if self.loadbalancer_type is not None:
            result['LoadbalancerType'] = self.loadbalancer_type

        if self.warmup_duration is not None:
            result['WarmupDuration'] = self.warmup_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsistentHashLBConfig') is not None:
            temp_model = main_models.ListGatewayServiceResponseBodyDataResultGatewayTrafficPolicyLoadBalancerSettingsConsistentHashLBConfig()
            self.consistent_hash_lbconfig = temp_model.from_map(m.get('ConsistentHashLBConfig'))

        if m.get('LoadbalancerType') is not None:
            self.loadbalancer_type = m.get('LoadbalancerType')

        if m.get('WarmupDuration') is not None:
            self.warmup_duration = m.get('WarmupDuration')

        return self

class ListGatewayServiceResponseBodyDataResultGatewayTrafficPolicyLoadBalancerSettingsConsistentHashLBConfig(DaraModel):
    def __init__(
        self,
        consistent_hash_lbtype: str = None,
        http_cookie: main_models.ListGatewayServiceResponseBodyDataResultGatewayTrafficPolicyLoadBalancerSettingsConsistentHashLBConfigHttpCookie = None,
        minimum_ring_size: int = None,
        parameter_name: str = None,
    ):
        # The consistent hashing method. Valid values:
        # 
        # - HEADER
        # 
        # - COOKIE
        # 
        # - SOURCE_IP
        # 
        # - QUERY_PARAMETER
        self.consistent_hash_lbtype = consistent_hash_lbtype
        # The cookie-based parameter.
        self.http_cookie = http_cookie
        # The minimum size of the hash ring.
        self.minimum_ring_size = minimum_ring_size
        # The parameter name.
        self.parameter_name = parameter_name

    def validate(self):
        if self.http_cookie:
            self.http_cookie.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consistent_hash_lbtype is not None:
            result['ConsistentHashLBType'] = self.consistent_hash_lbtype

        if self.http_cookie is not None:
            result['HttpCookie'] = self.http_cookie.to_map()

        if self.minimum_ring_size is not None:
            result['MinimumRingSize'] = self.minimum_ring_size

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsistentHashLBType') is not None:
            self.consistent_hash_lbtype = m.get('ConsistentHashLBType')

        if m.get('HttpCookie') is not None:
            temp_model = main_models.ListGatewayServiceResponseBodyDataResultGatewayTrafficPolicyLoadBalancerSettingsConsistentHashLBConfigHttpCookie()
            self.http_cookie = temp_model.from_map(m.get('HttpCookie'))

        if m.get('MinimumRingSize') is not None:
            self.minimum_ring_size = m.get('MinimumRingSize')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        return self

class ListGatewayServiceResponseBodyDataResultGatewayTrafficPolicyLoadBalancerSettingsConsistentHashLBConfigHttpCookie(DaraModel):
    def __init__(
        self,
        name: str = None,
        path: str = None,
        ttl: str = None,
    ):
        # The cookie name.
        self.name = name
        # The cookie path.
        self.path = path
        # The time-to-live (TTL) of the cookie.
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.path is not None:
            result['Path'] = self.path

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

