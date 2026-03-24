# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class CreateDomainRequest(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        domain: str = None,
        instance_id: str = None,
        listen: main_models.CreateDomainRequestListen = None,
        redirect: main_models.CreateDomainRequestRedirect = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        tag: List[main_models.CreateDomainRequestTag] = None,
    ):
        # The access type of the WAF instance. Valid values:
        # 
        # - **share** (default): onboarding by using a CNAME record.
        # 
        # - **hybrid_cloud_cname**: onboarding by using a hybrid cloud CNAME record.
        self.access_type = access_type
        # The domain name that you want to add.
        # 
        # This parameter is required.
        self.domain = domain
        # The ID of the WAF instance.
        # 
        # > Call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The listening configurations.
        # 
        # This parameter is required.
        self.listen = listen
        # The forwarding configurations.
        # 
        # This parameter is required.
        self.redirect = redirect
        # The region where the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: The Chinese mainland.
        # 
        # - **ap-southeast-1**: Outside the Chinese mainland.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The tags. You can specify up to 20 tags.
        self.tag = tag

    def validate(self):
        if self.listen:
            self.listen.validate()
        if self.redirect:
            self.redirect.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.listen is not None:
            result['Listen'] = self.listen.to_map()

        if self.redirect is not None:
            result['Redirect'] = self.redirect.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Listen') is not None:
            temp_model = main_models.CreateDomainRequestListen()
            self.listen = temp_model.from_map(m.get('Listen'))

        if m.get('Redirect') is not None:
            temp_model = main_models.CreateDomainRequestRedirect()
            self.redirect = temp_model.from_map(m.get('Redirect'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateDomainRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateDomainRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class CreateDomainRequestRedirect(DaraModel):
    def __init__(
        self,
        backend_ports: List[main_models.CreateDomainRequestRedirectBackendPorts] = None,
        backends: List[str] = None,
        backup_backends: List[str] = None,
        cname_enabled: bool = None,
        connect_timeout: int = None,
        focus_http_backend: bool = None,
        http_2origin: bool = None,
        http_2origin_max_concurrency: int = None,
        keepalive: bool = None,
        keepalive_requests: int = None,
        keepalive_timeout: int = None,
        loadbalance: str = None,
        max_body_size: int = None,
        proxy_protocol: bool = None,
        read_timeout: int = None,
        request_headers: List[main_models.CreateDomainRequestRedirectRequestHeaders] = None,
        retry: bool = None,
        routing_rules: str = None,
        sni_enabled: bool = None,
        sni_host: str = None,
        wlproxy_client_ip: bool = None,
        web_server_type: bool = None,
        write_timeout: int = None,
        xclient_ip: bool = None,
        xtrue_ip: bool = None,
        xff_proto: bool = None,
    ):
        # The custom port configuration.
        self.backend_ports = backend_ports
        # The IP address or domain name of the origin server.
        self.backends = backends
        # The secondary IP address or domain name of the origin server.
        self.backup_backends = backup_backends
        # Indicates whether the public cloud disaster recovery feature is enabled for the domain name. Valid values:
        # 
        # - **true**: The public cloud disaster recovery feature is enabled.
        # 
        # - **false** (default): The public cloud disaster recovery feature is disabled.
        self.cname_enabled = cname_enabled
        # The timeout period for connections. Unit: seconds. Valid values: 1 to 3600. Default value: 5.
        self.connect_timeout = connect_timeout
        # Indicates whether force redirect from HTTPS to HTTP is enabled for back-to-origin requests. This parameter is available only if you specify **HttpsPorts** (indicating that the domain name uses HTTPS). Valid values:
        # 
        # - **true**: Force redirect from HTTPS to HTTP is enabled for back-to-origin requests.
        # 
        # - **false**: Force redirect from HTTPS to HTTP is disabled for back-to-origin requests.
        self.focus_http_backend = focus_http_backend
        # Indicates whether HTTP/2 is enabled for back-to-origin traffic. Valid values:
        # 
        # - **true**: HTTP/2 is enabled for back-to-origin traffic.
        # 
        # - **false**: HTTP/2 is disabled for back-to-origin traffic.
        self.http_2origin = http_2origin
        # The maximum number of concurrent HTTP/2 back-to-origin requests. Valid values: 1 to 512. Default value: 128.
        self.http_2origin_max_concurrency = http_2origin_max_concurrency
        # Indicates whether the persistent connection feature is enabled. Valid values:
        # 
        # - **true** (default): The persistent connection feature is enabled.
        # 
        # - **false**: The persistent connection feature is disabled.
        self.keepalive = keepalive
        # The number of reused persistent connections. Valid values: 60 to 1000. Default value: 1000.
        # 
        # > The number of reused persistent connections after the persistent connection feature is enabled.
        self.keepalive_requests = keepalive_requests
        # The timeout period of idle persistent connections. Valid values: 1 to 60. Default value: 15. Unit: seconds.
        # 
        # > This parameter specifies the time for which a reused persistent connection can remain in the Idle state before the persistent connection is closed.
        self.keepalive_timeout = keepalive_timeout
        # The load balancing algorithm that you want to use when WAF forwards requests to the origin server. Valid values:
        # 
        # - **iphash**: IP hash algorithm.
        # 
        # - **roundRobin**: Round-robin algorithm.
        # 
        # - **leastTime**: Least Time algorithm. This value is available only if you set **ProtectionResource** to **gslb** (indicating that intelligent load balancing for a shared cluster is used).
        # 
        # This parameter is required.
        self.loadbalance = loadbalance
        # The maximum size of a request body. Valid values: 2 to 10. Default value: 2. Unit: GB.
        # 
        # > This parameter is supported only by the Ultimate edition.
        self.max_body_size = max_body_size
        # Indicates whether the Proxy Protocol feature is enabled to preserve the client\\"s source IP address. Valid values:
        # 
        # - **true**: The Proxy Protocol feature is enabled. After this feature is enabled, backend services can view the original IP address of the client.
        # 
        # - **false**: The Proxy Protocol feature is disabled.
        self.proxy_protocol = proxy_protocol
        # The timeout period for read operations. Unit: seconds. Valid values: 1 to 3600. Default value: 120.
        self.read_timeout = read_timeout
        # The key-value pairs that you want to use to label the requests that pass through the WAF instance.
        # 
        # When a request passes through WAF, WAF automatically adds the custom header fields to the request to mark the request. This way, the backend service can identify requests that are processed by WAF.
        self.request_headers = request_headers
        # Indicates whether WAF retries when WAF fails to forward requests to the origin server. Valid values:
        # 
        # - **true** (default): WAF retries.
        # 
        # - **false**: WAF does not retry.
        self.retry = retry
        # The forwarding rules for hybrid cloud mode. The value contains the following fields:
        # 
        # - **rs**: The IP addresses or canonical names of the origin servers.
        # 
        # - **backupRs**: The backup IP addresses or canonical names of the origin servers. Required. An empty array [] means no backup is configured.
        # 
        # - **location**: The name of the protection node.
        # 
        # - **locationId**: The ID of the protection node.
        self.routing_rules = routing_rules
        # Indicates whether the Server Name Indication (SNI) feature is enabled for back-to-origin requests. This parameter is available only if you specify **HttpsPorts** (indicating that the domain name uses HTTPS). Valid values:
        # 
        # - **true**: The SNI feature is enabled for back-to-origin requests.
        # 
        # - **false** (default): The SNI feature is disabled for back-to-origin requests.
        self.sni_enabled = sni_enabled
        # The custom value of the SNI field. If you do not specify this parameter, the value of the **Host** header in the request is used as the value of the SNI field. This parameter is optional. If you want WAF to use an SNI field value that is different from the Host field value in back-to-origin requests, you can specify a custom value for the SNI field.
        # 
        # > This parameter is required only if you set **SniEnabled** to **true** (indicating that the SNI feature is enabled for back-to-origin requests).
        self.sni_host = sni_host
        # Indicates whether WAF is allowed to overwrite the WL-Proxy-Client-IP header. Valid values:
        # 
        # - **true** (default): WAF overwrites the header.
        # 
        # - **false**: WAF does not overwrite the header.
        self.wlproxy_client_ip = wlproxy_client_ip
        # Indicates whether WAF is allowed to overwrite the Web-Server-Type header. Valid values:
        # 
        # - **true** (default): WAF overwrites the header.
        # 
        # - **false**: WAF does not overwrite the header.
        self.web_server_type = web_server_type
        # The timeout period for write operations. Unit: seconds. Valid values: 1 to 3600. Default value: 120.
        self.write_timeout = write_timeout
        # Indicates whether WAF is allowed to overwrite the X-Client-IP header. Valid values:
        # 
        # - **true** (default): WAF overwrites the header.
        # 
        # - **false**: WAF does not overwrite the header.
        self.xclient_ip = xclient_ip
        # Indicates whether WAF is allowed to overwrite the X-True-IP header. Valid values:
        # 
        # - **true** (default): WAF overwrites the header.
        # 
        # - **false**: WAF does not overwrite the header.
        self.xtrue_ip = xtrue_ip
        # Indicates whether the X-Forward-For-Proto header is used to identify the protocol used by WAF to forward requests to the origin server. Valid values:
        # 
        # - **true** (default): The X-Forward-For-Proto header is used to identify the protocol.
        # 
        # - **false**: The X-Forward-For-Proto header is not used.
        self.xff_proto = xff_proto

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

        if self.backup_backends is not None:
            result['BackupBackends'] = self.backup_backends

        if self.cname_enabled is not None:
            result['CnameEnabled'] = self.cname_enabled

        if self.connect_timeout is not None:
            result['ConnectTimeout'] = self.connect_timeout

        if self.focus_http_backend is not None:
            result['FocusHttpBackend'] = self.focus_http_backend

        if self.http_2origin is not None:
            result['Http2Origin'] = self.http_2origin

        if self.http_2origin_max_concurrency is not None:
            result['Http2OriginMaxConcurrency'] = self.http_2origin_max_concurrency

        if self.keepalive is not None:
            result['Keepalive'] = self.keepalive

        if self.keepalive_requests is not None:
            result['KeepaliveRequests'] = self.keepalive_requests

        if self.keepalive_timeout is not None:
            result['KeepaliveTimeout'] = self.keepalive_timeout

        if self.loadbalance is not None:
            result['Loadbalance'] = self.loadbalance

        if self.max_body_size is not None:
            result['MaxBodySize'] = self.max_body_size

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

        if self.wlproxy_client_ip is not None:
            result['WLProxyClientIp'] = self.wlproxy_client_ip

        if self.web_server_type is not None:
            result['WebServerType'] = self.web_server_type

        if self.write_timeout is not None:
            result['WriteTimeout'] = self.write_timeout

        if self.xclient_ip is not None:
            result['XClientIp'] = self.xclient_ip

        if self.xtrue_ip is not None:
            result['XTrueIp'] = self.xtrue_ip

        if self.xff_proto is not None:
            result['XffProto'] = self.xff_proto

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_ports = []
        if m.get('BackendPorts') is not None:
            for k1 in m.get('BackendPorts'):
                temp_model = main_models.CreateDomainRequestRedirectBackendPorts()
                self.backend_ports.append(temp_model.from_map(k1))

        if m.get('Backends') is not None:
            self.backends = m.get('Backends')

        if m.get('BackupBackends') is not None:
            self.backup_backends = m.get('BackupBackends')

        if m.get('CnameEnabled') is not None:
            self.cname_enabled = m.get('CnameEnabled')

        if m.get('ConnectTimeout') is not None:
            self.connect_timeout = m.get('ConnectTimeout')

        if m.get('FocusHttpBackend') is not None:
            self.focus_http_backend = m.get('FocusHttpBackend')

        if m.get('Http2Origin') is not None:
            self.http_2origin = m.get('Http2Origin')

        if m.get('Http2OriginMaxConcurrency') is not None:
            self.http_2origin_max_concurrency = m.get('Http2OriginMaxConcurrency')

        if m.get('Keepalive') is not None:
            self.keepalive = m.get('Keepalive')

        if m.get('KeepaliveRequests') is not None:
            self.keepalive_requests = m.get('KeepaliveRequests')

        if m.get('KeepaliveTimeout') is not None:
            self.keepalive_timeout = m.get('KeepaliveTimeout')

        if m.get('Loadbalance') is not None:
            self.loadbalance = m.get('Loadbalance')

        if m.get('MaxBodySize') is not None:
            self.max_body_size = m.get('MaxBodySize')

        if m.get('ProxyProtocol') is not None:
            self.proxy_protocol = m.get('ProxyProtocol')

        if m.get('ReadTimeout') is not None:
            self.read_timeout = m.get('ReadTimeout')

        self.request_headers = []
        if m.get('RequestHeaders') is not None:
            for k1 in m.get('RequestHeaders'):
                temp_model = main_models.CreateDomainRequestRedirectRequestHeaders()
                self.request_headers.append(temp_model.from_map(k1))

        if m.get('Retry') is not None:
            self.retry = m.get('Retry')

        if m.get('RoutingRules') is not None:
            self.routing_rules = m.get('RoutingRules')

        if m.get('SniEnabled') is not None:
            self.sni_enabled = m.get('SniEnabled')

        if m.get('SniHost') is not None:
            self.sni_host = m.get('SniHost')

        if m.get('WLProxyClientIp') is not None:
            self.wlproxy_client_ip = m.get('WLProxyClientIp')

        if m.get('WebServerType') is not None:
            self.web_server_type = m.get('WebServerType')

        if m.get('WriteTimeout') is not None:
            self.write_timeout = m.get('WriteTimeout')

        if m.get('XClientIp') is not None:
            self.xclient_ip = m.get('XClientIp')

        if m.get('XTrueIp') is not None:
            self.xtrue_ip = m.get('XTrueIp')

        if m.get('XffProto') is not None:
            self.xff_proto = m.get('XffProto')

        return self

class CreateDomainRequestRedirectRequestHeaders(DaraModel):
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

class CreateDomainRequestRedirectBackendPorts(DaraModel):
    def __init__(
        self,
        backend_port: int = None,
        listen_port: int = None,
        protocol: str = None,
    ):
        # The back-to-origin port.
        self.backend_port = backend_port
        # The listener port.
        self.listen_port = listen_port
        # The protocol of the listener port. Valid values:
        # 
        # - **http**: HTTP.
        # 
        # - **https**: HTTPS.
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

class CreateDomainRequestListen(DaraModel):
    def __init__(
        self,
        cert_id: str = None,
        cipher_suite: int = None,
        custom_ciphers: List[str] = None,
        enable_tlsv_3: bool = None,
        exclusive_ip: bool = None,
        focus_https: bool = None,
        hsts_include_sub_domain: bool = None,
        hsts_max_age: int = None,
        hsts_preload: bool = None,
        http_2enabled: bool = None,
        http_ports: List[int] = None,
        https_ports: List[int] = None,
        ipv_6enabled: bool = None,
        protection_resource: str = None,
        sm2access_only: bool = None,
        sm2cert_id: str = None,
        sm2enabled: bool = None,
        tlsversion: str = None,
        xff_header_mode: int = None,
        xff_headers: List[str] = None,
    ):
        # The ID of the certificate. This parameter is available only if you specify **HttpsPorts** (indicating that the domain name uses HTTPS).
        self.cert_id = cert_id
        # The type of the cipher suite. This parameter is available only if you specify **HttpsPorts** (indicating that the domain name uses HTTPS). Valid values:
        # 
        # - **1**: All cipher suites.
        # 
        # - **2**: Strong cipher suites. This value is available only if you set **TLSVersion** to **tlsv1.2**.
        # 
        # - **99**: Custom cipher suites.
        self.cipher_suite = cipher_suite
        # The custom cipher suites.
        self.custom_ciphers = custom_ciphers
        # Indicates whether TLS 1.3 is supported. This parameter is available only if you specify **HttpsPorts** (indicating that the domain name uses HTTPS). Valid values:
        # 
        # - **true**: TLS 1.3 is supported.
        # 
        # - **false**: TLS 1.3 is not supported.
        self.enable_tlsv_3 = enable_tlsv_3
        # Indicates whether the exclusive IP address feature is enabled. This parameter is available only if you set **IPv6Enabled** to **false** (indicating that IPv6 is disabled) and **ProtectionResource** to **share** (indicating that a shared cluster is used). Valid values:
        # 
        # - **true**: The exclusive IP address feature is enabled.
        # 
        # - **false** (default): The exclusive IP address feature is disabled.
        self.exclusive_ip = exclusive_ip
        # Indicates whether force redirect from HTTP to HTTPS is enabled for received requests. This parameter is available only if you specify HttpsPorts and leave HttpPorts empty. Valid values:
        # 
        # - **true**: Force redirect from HTTP to HTTPS is enabled.
        # 
        # - **false**: Force redirect from HTTP to HTTPS is disabled.
        self.focus_https = focus_https
        # Indicates whether HSTS includes subdomains. Valid values:
        # 
        # - **true**: HSTS includes subdomains.
        # 
        # - **false**: HSTS does not include subdomains.
        self.hsts_include_sub_domain = hsts_include_sub_domain
        # The time-to-live (TTL) for HSTS. Unit: seconds.
        self.hsts_max_age = hsts_max_age
        # Indicates whether HSTS preloading is enabled. Valid values:
        # 
        # - **true**: HSTS preloading is enabled.
        # 
        # - **false**: HSTS preloading is disabled.
        self.hsts_preload = hsts_preload
        # Indicates whether HTTP/2 is enabled. This parameter is available only if you specify **HttpsPorts** (indicating that the domain name uses HTTPS). Valid values:
        # 
        # - **true**: HTTP/2 is enabled.
        # 
        # - **false** (default): HTTP/2 is disabled.
        self.http_2enabled = http_2enabled
        # The listening ports for HTTP.
        self.http_ports = http_ports
        # The listening ports for HTTPS.
        self.https_ports = https_ports
        # Indicates whether IPv6 is enabled. Valid values:
        # 
        # - **true**: IPv6 is enabled.
        # 
        # - **false** (default): IPv6 is disabled.
        self.ipv_6enabled = ipv_6enabled
        # The type of protection resource. Valid values:
        # 
        # - **share** (default): Shared cluster.
        # 
        # - **gslb**: Intelligent load balancing for a shared cluster.
        self.protection_resource = protection_resource
        # Indicates whether access is restricted to SM certificate-based clients only. This parameter is available only if you set SM2Enabled to true. Valid values:
        # 
        # - **true**: Only SM certificate-based clients can access the domain.
        # 
        # - **false**: Both SM certificate-based and non-SM certificate-based clients can access the domain.
        self.sm2access_only = sm2access_only
        # The ID of the SM certificate. This parameter is available only if you set SM2Enabled to true.
        self.sm2cert_id = sm2cert_id
        # Indicates whether SM certificate-based encryption is enabled.
        self.sm2enabled = sm2enabled
        # The minimum Transport Layer Security (TLS) version. This parameter is available only if you specify **HttpsPorts** (indicating that the domain name uses HTTPS). Valid values:
        # 
        # - **tlsv1**
        # 
        # - **tlsv1.1**
        # 
        # - **tlsv1.2**
        self.tlsversion = tlsversion
        # The method that WAF uses to obtain the originating IP address of a client. Valid values:
        # 
        # - **0** (default): The client traffic does not pass through other Layer 7 proxies before it reaches WAF.
        # 
        # - **1**: WAF uses the first value in the X-Forwarded-For (XFF) header as the client IP address.
        # 
        # - **2**: WAF uses the value of a custom header field that you specify as the client IP address.
        self.xff_header_mode = xff_header_mode
        # The custom header fields that are used to obtain the originating IP address of a client.
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

        if self.hsts_include_sub_domain is not None:
            result['HstsIncludeSubDomain'] = self.hsts_include_sub_domain

        if self.hsts_max_age is not None:
            result['HstsMaxAge'] = self.hsts_max_age

        if self.hsts_preload is not None:
            result['HstsPreload'] = self.hsts_preload

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

        if self.sm2access_only is not None:
            result['SM2AccessOnly'] = self.sm2access_only

        if self.sm2cert_id is not None:
            result['SM2CertId'] = self.sm2cert_id

        if self.sm2enabled is not None:
            result['SM2Enabled'] = self.sm2enabled

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

        if m.get('HstsIncludeSubDomain') is not None:
            self.hsts_include_sub_domain = m.get('HstsIncludeSubDomain')

        if m.get('HstsMaxAge') is not None:
            self.hsts_max_age = m.get('HstsMaxAge')

        if m.get('HstsPreload') is not None:
            self.hsts_preload = m.get('HstsPreload')

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

        if m.get('SM2AccessOnly') is not None:
            self.sm2access_only = m.get('SM2AccessOnly')

        if m.get('SM2CertId') is not None:
            self.sm2cert_id = m.get('SM2CertId')

        if m.get('SM2Enabled') is not None:
            self.sm2enabled = m.get('SM2Enabled')

        if m.get('TLSVersion') is not None:
            self.tlsversion = m.get('TLSVersion')

        if m.get('XffHeaderMode') is not None:
            self.xff_header_mode = m.get('XffHeaderMode')

        if m.get('XffHeaders') is not None:
            self.xff_headers = m.get('XffHeaders')

        return self

