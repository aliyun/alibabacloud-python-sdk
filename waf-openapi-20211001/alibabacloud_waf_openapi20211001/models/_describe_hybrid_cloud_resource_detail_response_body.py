# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeHybridCloudResourceDetailResponseBody(DaraModel):
    def __init__(
        self,
        domain: main_models.DescribeHybridCloudResourceDetailResponseBodyDomain = None,
        request_id: str = None,
    ):
        # The domain name information.
        self.domain = domain
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.domain:
            self.domain.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            temp_model = main_models.DescribeHybridCloudResourceDetailResponseBodyDomain()
            self.domain = temp_model.from_map(m.get('Domain'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeHybridCloudResourceDetailResponseBodyDomain(DaraModel):
    def __init__(
        self,
        cname: str = None,
        domain: str = None,
        id: int = None,
        listen: main_models.DescribeHybridCloudResourceDetailResponseBodyDomainListen = None,
        redirect: main_models.DescribeHybridCloudResourceDetailResponseBodyDomainRedirect = None,
        resource_manager_resource_group_id: str = None,
        status: int = None,
        uid: str = None,
    ):
        # CNAME
        self.cname = cname
        # The domain name.
        self.domain = domain
        # id
        self.id = id
        # The listening information.
        self.listen = listen
        # The rules for returning response header values.
        self.redirect = redirect
        # The resource group ID.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The resource status.
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
            temp_model = main_models.DescribeHybridCloudResourceDetailResponseBodyDomainListen()
            self.listen = temp_model.from_map(m.get('Listen'))

        if m.get('Redirect') is not None:
            temp_model = main_models.DescribeHybridCloudResourceDetailResponseBodyDomainRedirect()
            self.redirect = temp_model.from_map(m.get('Redirect'))

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

class DescribeHybridCloudResourceDetailResponseBodyDomainRedirect(DaraModel):
    def __init__(
        self,
        backend_ports: List[main_models.DescribeHybridCloudResourceDetailResponseBodyDomainRedirectBackendPorts] = None,
        backends: List[str] = None,
        cname_enabled: bool = None,
        connect_timeout: int = None,
        focus_http_backend: bool = None,
        keepalive: bool = None,
        keepalive_requests: int = None,
        keepalive_timeout: int = None,
        loadbalance: str = None,
        proxy_protocol: bool = None,
        read_timeout: int = None,
        request_headers: List[main_models.DescribeHybridCloudResourceDetailResponseBodyDomainRedirectRequestHeaders] = None,
        retry: bool = None,
        routing_rules: str = None,
        sni_enabled: bool = None,
        sni_host: str = None,
        write_timeout: int = None,
    ):
        # The custom port configuration. By default, this is the same as the listening port.
        self.backend_ports = backend_ports
        # The IP address of the origin server or the domain name used for back-to-origin.
        self.backends = backends
        # Specifies whether to enable public cloud disaster recovery. Valid values:
        # 
        # - **true**: Public cloud disaster recovery is enabled.
        # 
        # - **false**: Public cloud disaster recovery is disabled.
        self.cname_enabled = cname_enabled
        # The connection timeout period. Unit: milliseconds.
        self.connect_timeout = connect_timeout
        # Indicates whether forced HTTP back-to-origin is enabled. Valid values:
        # 
        # - **true**: Forced HTTP back-to-origin is enabled.
        # 
        # - **false**: Forced HTTP back-to-origin is disabled.
        self.focus_http_backend = focus_http_backend
        # Indicates whether persistent connections are enabled. Valid values:
        # 
        # - **true** (default): Persistent connections are enabled.
        # 
        # - **false**: Persistent connections are disabled.
        self.keepalive = keepalive
        # The number of requests that reuse persistent connections. Valid values: 60 to 1000.
        # 
        # > This specifies how many persistent connections are reused after persistent connections are enabled.
        self.keepalive_requests = keepalive_requests
        # The idle timeout period of persistent connections.
        self.keepalive_timeout = keepalive_timeout
        # The load balancing algorithm used for back-to-origin. Valid values:
        # 
        # - **iphash**: IP hash algorithm.
        # 
        # - **roundRobin**: round-robin algorithm.
        # 
        # - **leastTime**: least-time back-to-origin algorithm.
        self.loadbalance = loadbalance
        # Indicates whether the client source IP preservation feature is enabled.
        # 
        # - true: The client source IP preservation feature is enabled. After this feature is enabled, the backend service can view the originating IP address of the client.
        # - false: The client source IP preservation feature is disabled.
        self.proxy_protocol = proxy_protocol
        # The read timeout period of the request.
        self.read_timeout = read_timeout
        # The HTTP request headers.
        self.request_headers = request_headers
        # Indicates whether WAF retries when back-to-origin fails. Valid values:
        # 
        # - **true**: WAF retries.
        # 
        # - **false**: WAF does not retry.
        self.retry = retry
        # The hybrid cloud forwarding rules, expressed as a string converted from a JSON array. Each element in the JSON array is a structure that contains the following field:
        # - **rs**: Array type.
        self.routing_rules = routing_rules
        # Indicates whether back-to-origin Server Name Indication (SNI) is enabled. Valid values:
        # 
        # - **true**: Back-to-origin SNI is enabled.
        # 
        # - **false**: Back-to-origin SNI is disabled.
        self.sni_enabled = sni_enabled
        # The custom value of the SNI extension field. If the value is empty, the SNI value is not customized, and the value of the **Host** field in the request header is used as the value of the SNI extension field by default.
        # 
        # > This parameter is returned only when **SniStatus** is set to **1**, which indicates that back-to-origin SNI is enabled.
        self.sni_host = sni_host
        # The write timeout period. Unit: milliseconds.
        self.write_timeout = write_timeout

    def validate(self):
        if self.backend_ports:
            for v1 in self.backend_ports:
                 if v1:
                    v1.validate()
        if self.request_headers:
            for v1 in self.request_headers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackendPorts'] = []
        if self.backend_ports is not None:
            for k1 in self.backend_ports:
                result['BackendPorts'].append(k1.to_map() if k1 else None)

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

        if self.proxy_protocol is not None:
            result['ProxyProtocol'] = self.proxy_protocol

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
        self.backend_ports = []
        if m.get('BackendPorts') is not None:
            for k1 in m.get('BackendPorts'):
                temp_model = main_models.DescribeHybridCloudResourceDetailResponseBodyDomainRedirectBackendPorts()
                self.backend_ports.append(temp_model.from_map(k1))

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

        if m.get('ProxyProtocol') is not None:
            self.proxy_protocol = m.get('ProxyProtocol')

        if m.get('ReadTimeout') is not None:
            self.read_timeout = m.get('ReadTimeout')

        self.request_headers = []
        if m.get('RequestHeaders') is not None:
            for k1 in m.get('RequestHeaders'):
                temp_model = main_models.DescribeHybridCloudResourceDetailResponseBodyDomainRedirectRequestHeaders()
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

class DescribeHybridCloudResourceDetailResponseBodyDomainRedirectRequestHeaders(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value.
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

class DescribeHybridCloudResourceDetailResponseBodyDomainRedirectBackendPorts(DaraModel):
    def __init__(
        self,
        backend_port: int = None,
        listen_port: int = None,
        protocol: str = None,
    ):
        # The back-to-origin port.
        self.backend_port = backend_port
        # The listening port.
        self.listen_port = listen_port
        # The protocol type of the listening port. Valid values:
        # 
        # - http: HTTP protocol.
        # - https: HTTPS protocol.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_port is not None:
            result['BackendPort'] = self.backend_port

        if self.listen_port is not None:
            result['ListenPort'] = self.listen_port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendPort') is not None:
            self.backend_port = m.get('BackendPort')

        if m.get('ListenPort') is not None:
            self.listen_port = m.get('ListenPort')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

class DescribeHybridCloudResourceDetailResponseBodyDomainListen(DaraModel):
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
        # The certificate ID.
        self.cert_id = cert_id
        # The type of cipher suite. Valid values:
        # 
        # - **1**: all cipher suites.
        # 
        # - **2**: strong cipher suites.
        # 
        # - **99**: custom cipher suites.
        self.cipher_suite = cipher_suite
        # The custom cipher suites.
        self.custom_ciphers = custom_ciphers
        # Indicates whether TLS 1.3 is supported. Valid values:
        # 
        # - **true**: TLS 1.3 is supported.
        # 
        # - **false**: TLS 1.3 is not supported.
        self.enable_tlsv_3 = enable_tlsv_3
        # Indicates whether an exclusive IP address is supported. Valid values:
        # - **true**: Supported.
        # 
        # - **false**: Not supported.
        self.exclusive_ip = exclusive_ip
        # Indicates whether HTTPS forced redirect is enabled. Valid values:
        # 
        # - **true**: HTTPS forced redirect is enabled.
        # 
        # - **false**: HTTPS forced redirect is disabled.
        self.focus_https = focus_https
        # Indicates whether HTTP/2 is enabled. Valid values:
        # 
        # - **true**: HTTP/2 is enabled.
        # 
        # - **false**: HTTP/2 is disabled.
        self.http_2enabled = http_2enabled
        # The list of available ports for the HTTP protocol. The value is a string. When multiple ports are available, they are returned in the format of **port1,port2,port3**.
        self.http_ports = http_ports
        # The ports for the HTTPS protocol.
        self.https_ports = https_ports
        # Indicates whether IPv6 is enabled. Valid values:
        # 
        # - **true**: IPv6 is enabled.
        # 
        # - **false**: IPv6 is disabled.
        self.ipv_6enabled = ipv_6enabled
        # The type of protection resource to use. Valid values:
        # 
        # - **share**: shared cluster.
        # 
        # - **gslb**: shared cluster with intelligent load balancing.
        self.protection_resource = protection_resource
        # The TLS version. Valid values:
        # 
        # - **tlsv1**
        # 
        # - **tlsv1.1**
        # 
        # - **tlsv1.2**
        self.tlsversion = tlsversion
        # The method that WAF uses to obtain the actual client IP address. Valid values:
        # 
        # - **0**: No Layer 7 proxy is deployed in front of WAF.
        # 
        # - **1**: WAF reads the first value of the X-Forwarded-For (XFF) header field as the client IP address.
        # 
        # - **2**: WAF reads the value of a custom header field that you specify as the client IP address.
        self.xff_header_mode = xff_header_mode
        # The custom header fields used to obtain the client IP address, in the format of [**"header1","header2",……**].
        # 
        # > This parameter is required only when **XffHeaderMode** is set to 2, which indicates that WAF reads the value of a custom header field that you specify in the request header as the client IP address.
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

