# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeHybridCloudResourcesResponseBody(DaraModel):
    def __init__(
        self,
        domains: List[main_models.DescribeHybridCloudResourcesResponseBodyDomains] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The domain names.
        self.domains = domains
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries that are returned.
        self.total_count = total_count

    def validate(self):
        if self.domains:
            for v1 in self.domains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Domains'] = []
        if self.domains is not None:
            for k1 in self.domains:
                result['Domains'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domains = []
        if m.get('Domains') is not None:
            for k1 in m.get('Domains'):
                temp_model = main_models.DescribeHybridCloudResourcesResponseBodyDomains()
                self.domains.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeHybridCloudResourcesResponseBodyDomains(DaraModel):
    def __init__(
        self,
        cname: str = None,
        domain: str = None,
        id: int = None,
        listen: main_models.DescribeHybridCloudResourcesResponseBodyDomainsListen = None,
        redirect: main_models.DescribeHybridCloudResourcesResponseBodyDomainsRedirect = None,
        resource_manager_resource_group_id: str = None,
        status: int = None,
        uid: str = None,
    ):
        # The CNAME assigned by WAF.
        # 
        # >  This parameter is returned only if the value of **CnameEnabled** is true.
        self.cname = cname
        # The domain name.
        self.domain = domain
        # The access ID.
        self.id = id
        # The listeners.
        self.listen = listen
        # The configurations of the forwarding rule.
        self.redirect = redirect
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The status of the domain name. Valid values:
        # 
        # *   **1:** The domain name is in a normal state.
        # *   **2:** The domain name is being created.
        # *   **3:** The domain name is being modified.
        # *   **4:** The domain name is being released.
        # *   **5:** WAF no longer forwards the traffic of the domain name.
        self.status = status
        # The user ID.
        self.uid = uid

    def validate(self):
        if self.listen:
            self.listen.validate()
        if self.redirect:
            self.redirect.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cname is not None:
            result['Cname'] = self.cname

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.id is not None:
            result['Id'] = self.id

        if self.listen is not None:
            result['Listen'] = self.listen.to_map()

        if self.redirect is not None:
            result['Redirect'] = self.redirect.to_map()

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Listen') is not None:
            temp_model = main_models.DescribeHybridCloudResourcesResponseBodyDomainsListen()
            self.listen = temp_model.from_map(m.get('Listen'))

        if m.get('Redirect') is not None:
            temp_model = main_models.DescribeHybridCloudResourcesResponseBodyDomainsRedirect()
            self.redirect = temp_model.from_map(m.get('Redirect'))

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

class DescribeHybridCloudResourcesResponseBodyDomainsRedirect(DaraModel):
    def __init__(
        self,
        backends: List[str] = None,
        cname_enabled: bool = None,
        connect_timeout: int = None,
        focus_http_backend: bool = None,
        keepalive: bool = None,
        keepalive_requests: int = None,
        keepalive_timeout: int = None,
        loadbalance: str = None,
        read_timeout: int = None,
        request_headers: List[main_models.DescribeHybridCloudResourcesResponseBodyDomainsRedirectRequestHeaders] = None,
        retry: bool = None,
        routing_rules: str = None,
        sni_enabled: bool = None,
        sni_host: str = None,
        write_timeout: int = None,
    ):
        # The IP addresses or domain names of the origin server.
        self.backends = backends
        # Indicates whether the public cloud disaster recovery feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.cname_enabled = cname_enabled
        # The timeout period for connections. Unit: seconds. Valid values: 5 to 120.
        self.connect_timeout = connect_timeout
        # Indicates whether the HTTPS to HTTP redirection feature is enabled for back-to-origin requests. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.focus_http_backend = focus_http_backend
        # Indicates whether the persistent connection feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.keepalive = keepalive
        # The number of reused persistent connections. Valid values: 60 to 1000.
        # 
        # >  This parameter indicates the number of reused persistent connections after the persistent connection feature is enabled.
        self.keepalive_requests = keepalive_requests
        # The timeout period for persistent connections that are in the Idle state. Unit: seconds. Valid values: 1 to 60. Default value: 15.
        # 
        # >  This parameter indicates the period of time during which a reused persistent connection can remain in the Idle state before the persistent connection is released.
        self.keepalive_timeout = keepalive_timeout
        # The load balancing algorithm that is used to forward requests to the origin server. Valid values:
        # 
        # *   **iphash**
        # *   **roundRobin**
        # *   **leastTime**
        self.loadbalance = loadbalance
        # The timeout period for read connections. Unit: seconds. Valid values: 5 to 1800.
        self.read_timeout = read_timeout
        # The key-value pair that is used to label requests that pass through WAF.
        self.request_headers = request_headers
        # Indicates whether WAF retries forwarding requests if requests fail to be forwarded to the origin server. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.retry = retry
        # The forwarding rules that are configured for the domain name. This parameter is a string that consists of JSON arrays. Each element in a JSON array is a JSON struct that contains the following fields:
        # 
        # *   **rs**: the back-to-origin IP addresses or CNAMEs. The value is of the ARRAY type.
        # *   **location**: the name of the protection node. The value is of the STRING type.
        # *   **locationId**: the ID of the protection node. The value is of the LONG type.
        self.routing_rules = routing_rules
        # Indicates whether the origin Server Name Indication (SNI) feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.sni_enabled = sni_enabled
        # The value of the custom SNI field. If the parameter is left empty, the value of the **Host** field in the request header is automatically used as the value of the SNI field.
        # 
        # >  This parameter is returned only if the value of **SniEnabled** is **true**.
        self.sni_host = sni_host
        # The timeout period for write connections. Unit: seconds. Valid values: 5 to 1800.
        self.write_timeout = write_timeout

    def validate(self):
        if self.request_headers:
            for v1 in self.request_headers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backends is not None:
            result['Backends'] = self.backends

        if self.cname_enabled is not None:
            result['CnameEnabled'] = self.cname_enabled

        if self.connect_timeout is not None:
            result['ConnectTimeout'] = self.connect_timeout

        if self.focus_http_backend is not None:
            result['FocusHttpBackend'] = self.focus_http_backend

        if self.keepalive is not None:
            result['Keepalive'] = self.keepalive

        if self.keepalive_requests is not None:
            result['KeepaliveRequests'] = self.keepalive_requests

        if self.keepalive_timeout is not None:
            result['KeepaliveTimeout'] = self.keepalive_timeout

        if self.loadbalance is not None:
            result['Loadbalance'] = self.loadbalance

        if self.read_timeout is not None:
            result['ReadTimeout'] = self.read_timeout

        result['RequestHeaders'] = []
        if self.request_headers is not None:
            for k1 in self.request_headers:
                result['RequestHeaders'].append(k1.to_map() if k1 else None)

        if self.retry is not None:
            result['Retry'] = self.retry

        if self.routing_rules is not None:
            result['RoutingRules'] = self.routing_rules

        if self.sni_enabled is not None:
            result['SniEnabled'] = self.sni_enabled

        if self.sni_host is not None:
            result['SniHost'] = self.sni_host

        if self.write_timeout is not None:
            result['WriteTimeout'] = self.write_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Backends') is not None:
            self.backends = m.get('Backends')

        if m.get('CnameEnabled') is not None:
            self.cname_enabled = m.get('CnameEnabled')

        if m.get('ConnectTimeout') is not None:
            self.connect_timeout = m.get('ConnectTimeout')

        if m.get('FocusHttpBackend') is not None:
            self.focus_http_backend = m.get('FocusHttpBackend')

        if m.get('Keepalive') is not None:
            self.keepalive = m.get('Keepalive')

        if m.get('KeepaliveRequests') is not None:
            self.keepalive_requests = m.get('KeepaliveRequests')

        if m.get('KeepaliveTimeout') is not None:
            self.keepalive_timeout = m.get('KeepaliveTimeout')

        if m.get('Loadbalance') is not None:
            self.loadbalance = m.get('Loadbalance')

        if m.get('ReadTimeout') is not None:
            self.read_timeout = m.get('ReadTimeout')

        self.request_headers = []
        if m.get('RequestHeaders') is not None:
            for k1 in m.get('RequestHeaders'):
                temp_model = main_models.DescribeHybridCloudResourcesResponseBodyDomainsRedirectRequestHeaders()
                self.request_headers.append(temp_model.from_map(k1))

        if m.get('Retry') is not None:
            self.retry = m.get('Retry')

        if m.get('RoutingRules') is not None:
            self.routing_rules = m.get('RoutingRules')

        if m.get('SniEnabled') is not None:
            self.sni_enabled = m.get('SniEnabled')

        if m.get('SniHost') is not None:
            self.sni_host = m.get('SniHost')

        if m.get('WriteTimeout') is not None:
            self.write_timeout = m.get('WriteTimeout')

        return self

class DescribeHybridCloudResourcesResponseBodyDomainsRedirectRequestHeaders(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the custom header field.
        self.key = key
        # The value of the custom header field.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeHybridCloudResourcesResponseBodyDomainsListen(DaraModel):
    def __init__(
        self,
        cert_id: str = None,
        cipher_suite: int = None,
        custom_ciphers: List[str] = None,
        enable_tlsv_3: bool = None,
        exclusive_ip: bool = None,
        focus_https: bool = None,
        http_2enabled: bool = None,
        http_ports: List[int] = None,
        https_ports: List[int] = None,
        ipv_6enabled: bool = None,
        protection_resource: str = None,
        tlsversion: str = None,
        xff_header_mode: int = None,
        xff_headers: List[str] = None,
    ):
        # The ID of the certificate.
        self.cert_id = cert_id
        # The types of cipher suites that are added. Valid values:
        # 
        # *   **1:** all cipher suites.
        # *   **2:** strong cipher suites.
        # *   **99:** custom cipher suites.
        self.cipher_suite = cipher_suite
        # The custom cipher suites.
        # 
        # >  This parameter is returned only if the value of **CipherSuite** is **99**.
        self.custom_ciphers = custom_ciphers
        # Indicates whether TLS 1.3 is supported. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable_tlsv_3 = enable_tlsv_3
        # Indicates whether exclusive IP addresses are supported. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.exclusive_ip = exclusive_ip
        # Indicates whether the HTTP to HTTPS redirection feature is enabled for the domain name. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.focus_https = focus_https
        # Indicates whether HTTP/2 is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.http_2enabled = http_2enabled
        # The HTTP listener ports.
        self.http_ports = http_ports
        # The HTTPS listener ports.
        self.https_ports = https_ports
        # Specifies whether to enable IPv6. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.ipv_6enabled = ipv_6enabled
        # The type of the protection resource. Valid values:
        # 
        # *   **share:** shared cluster.
        # *   **gslb:** shared cluster-based intelligent load balancing.
        self.protection_resource = protection_resource
        # The version of the Transport Layer Security (TLS) protocol. Valid values:
        # 
        # *   **tlsv1**
        # *   **tlsv1.1**
        # *   **tlsv1.2**
        self.tlsversion = tlsversion
        # The method that is used to obtain the actual IP address of a client. Valid values:
        # 
        # *   **0**: No Layer 7 proxies are deployed in front of WAF.
        # *   **1**: WAF reads the first value of the X-Forwarded-For (XFF) header field as the actual IP address of the client.
        # *   **2**: WAF reads the value of a custom header field as the actual IP address of the client.
        self.xff_header_mode = xff_header_mode
        # The custom header fields that are used to obtain the actual IP addresses of clients. The value is in the ["header1","header2",...] format.
        # 
        # >  This parameter is returned only if the value of **XffHeaderMode** is 2.
        self.xff_headers = xff_headers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.cipher_suite is not None:
            result['CipherSuite'] = self.cipher_suite

        if self.custom_ciphers is not None:
            result['CustomCiphers'] = self.custom_ciphers

        if self.enable_tlsv_3 is not None:
            result['EnableTLSv3'] = self.enable_tlsv_3

        if self.exclusive_ip is not None:
            result['ExclusiveIp'] = self.exclusive_ip

        if self.focus_https is not None:
            result['FocusHttps'] = self.focus_https

        if self.http_2enabled is not None:
            result['Http2Enabled'] = self.http_2enabled

        if self.http_ports is not None:
            result['HttpPorts'] = self.http_ports

        if self.https_ports is not None:
            result['HttpsPorts'] = self.https_ports

        if self.ipv_6enabled is not None:
            result['IPv6Enabled'] = self.ipv_6enabled

        if self.protection_resource is not None:
            result['ProtectionResource'] = self.protection_resource

        if self.tlsversion is not None:
            result['TLSVersion'] = self.tlsversion

        if self.xff_header_mode is not None:
            result['XffHeaderMode'] = self.xff_header_mode

        if self.xff_headers is not None:
            result['XffHeaders'] = self.xff_headers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CipherSuite') is not None:
            self.cipher_suite = m.get('CipherSuite')

        if m.get('CustomCiphers') is not None:
            self.custom_ciphers = m.get('CustomCiphers')

        if m.get('EnableTLSv3') is not None:
            self.enable_tlsv_3 = m.get('EnableTLSv3')

        if m.get('ExclusiveIp') is not None:
            self.exclusive_ip = m.get('ExclusiveIp')

        if m.get('FocusHttps') is not None:
            self.focus_https = m.get('FocusHttps')

        if m.get('Http2Enabled') is not None:
            self.http_2enabled = m.get('Http2Enabled')

        if m.get('HttpPorts') is not None:
            self.http_ports = m.get('HttpPorts')

        if m.get('HttpsPorts') is not None:
            self.https_ports = m.get('HttpsPorts')

        if m.get('IPv6Enabled') is not None:
            self.ipv_6enabled = m.get('IPv6Enabled')

        if m.get('ProtectionResource') is not None:
            self.protection_resource = m.get('ProtectionResource')

        if m.get('TLSVersion') is not None:
            self.tlsversion = m.get('TLSVersion')

        if m.get('XffHeaderMode') is not None:
            self.xff_header_mode = m.get('XffHeaderMode')

        if m.get('XffHeaders') is not None:
            self.xff_headers = m.get('XffHeaders')

        return self

