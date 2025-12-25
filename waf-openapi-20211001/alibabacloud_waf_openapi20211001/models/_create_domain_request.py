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
        # The mode in which you want to add the domain name to WAF. Valid values:
        # 
        # *   **share:** adds the domain name to WAF in CNAME record mode. This is the default value.
        # *   **hybrid_cloud_cname:** adds the domain name to WAF in hybrid cloud reverse proxy mode.
        self.access_type = access_type
        # The domain name that you want to add to WAF.
        # 
        # This parameter is required.
        self.domain = domain
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to obtain the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The listener configurations.
        # 
        # This parameter is required.
        self.listen = listen
        # The forwarding configurations.
        # 
        # This parameter is required.
        self.redirect = redirect
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou**: the Chinese mainland
        # *   **ap-southeast-1**: outside the Chinese mainland
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
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
        # The key of the tag.
        self.key = key
        # The value of the tag.
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
        self.backend_ports = backend_ports
        # The IP addresses or domain names of the origin server.
        self.backends = backends
        # The secondary IP addresses or domain names of the origin server.
        self.backup_backends = backup_backends
        # Specifies whether to enable the public cloud disaster recovery feature. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.cname_enabled = cname_enabled
        # The timeout period of connections. Unit: seconds. Valid values: 1 to 3600.
        self.connect_timeout = connect_timeout
        # Specifies whether to enable force redirect from HTTPS to HTTP for back-to-origin requests. This parameter is available only if you specify **HttpsPorts**. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.focus_http_backend = focus_http_backend
        self.http_2origin = http_2origin
        self.http_2origin_max_concurrency = http_2origin_max_concurrency
        # Specifies whether to enable the persistent connection feature. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        self.keepalive = keepalive
        # The number of reused persistent connections. Valid values: 60 to 1000.
        # 
        # >  This parameter specifies the number of persistent connections that can be reused after you enable the persistent connection feature.
        self.keepalive_requests = keepalive_requests
        # The timeout period of idle persistent connections. Valid values: 1 to 60. Default value: 15. Unit: seconds.
        # 
        # >  This parameter specifies the period of time after which an idle persistent connection is closed.
        self.keepalive_timeout = keepalive_timeout
        # The load balancing algorithm that you want to use to forward requests to the origin server. Valid values:
        # 
        # *   **iphash**
        # *   **roundRobin**
        # *   **leastTime**: This value is available only if you set **ProtectionResource** to **gslb**.
        # 
        # This parameter is required.
        self.loadbalance = loadbalance
        self.max_body_size = max_body_size
        # The timeout period of read connections. Unit: seconds. Valid values: 1 to 3600.
        self.read_timeout = read_timeout
        # The custom header fields, which are key-value pairs. The fields are used to mark requests that pass through WAF.
        # 
        # When a request passes through WAF, WAF automatically adds the custom header fields to the request to mark the request. This way, the backend service can identify requests that are processed by WAF.
        self.request_headers = request_headers
        # Specifies whether WAF retries if WAF fails to forward requests to the origin server. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        self.retry = retry
        # The forwarding rules for the hybrid cloud mode. The value is a string that consists of JSON arrays. Each element in a JSON array is a JSON struct that contains the following fields:
        # 
        # *   **rs**: the back-to-origin IP addresses or CNAMEs. Data type: array.
        # *   **location**: the name of the protection node. Data type: string.
        # *   **locationId**: the ID of the protection node. Data type: long.
        self.routing_rules = routing_rules
        # Specifies whether to enable the Server Name Indication (SNI) feature for back-to-origin requests. This parameter is available only if you specify **HttpsPorts**. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.sni_enabled = sni_enabled
        # The custom value of the SNI field. If you do not specify this parameter, the value of the **Host** header field is automatically used. In most cases, you do not need to specify a custom value for the SNI field. However, if you want WAF to use an SNI field whose value is different from the value of the Host header field in back-to-origin requests, you can specify a custom value for the SNI field.
        # 
        # >  This parameter is required only if you set **SniEnabled** to **true**.
        self.sni_host = sni_host
        self.wlproxy_client_ip = wlproxy_client_ip
        self.web_server_type = web_server_type
        # The timeout period of write connections. Unit: seconds. Valid values: 1 to 3600.
        self.write_timeout = write_timeout
        self.xclient_ip = xclient_ip
        self.xtrue_ip = xtrue_ip
        # Specifies whether to use the X-Forward-For-Proto header field to pass the protocol used by WAF to forward requests to the origin server. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
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
        self.backend_port = backend_port
        self.listen_port = listen_port
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
        # The ID of the certificate that you want to add. This parameter is available only if you specify **HttpsPorts**.
        self.cert_id = cert_id
        # The type of the cipher suites that you want to add. This parameter is available only if you specify **HttpsPorts**. Valid values:
        # 
        # *   **1**: all cipher suites.
        # *   **2**: strong cipher suites. This value is available only if you set **TLSVersion** to **tlsv1.2**.
        # *   **99**: custom cipher suites.
        self.cipher_suite = cipher_suite
        # The custom cipher suites that you want to add.
        self.custom_ciphers = custom_ciphers
        # Specifies whether to support TLS 1.3. This parameter is available only if you specify **HttpsPorts**. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable_tlsv_3 = enable_tlsv_3
        # Specifies whether to enable the exclusive IP address feature. This parameter is available only if you set **IPv6Enabled** to **false** and **ProtectionResource** to **share**. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.exclusive_ip = exclusive_ip
        # Specifies whether to enable force redirect from HTTP to HTTPS for received requests. This parameter is available only if you specify HttpsPorts and leave HttpPorts empty. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.focus_https = focus_https
        # Specifies whether to enable HTTP/2. This parameter is available only if you specify **HttpsPorts**. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.http_2enabled = http_2enabled
        # The HTTP listener ports.
        self.http_ports = http_ports
        # The HTTPS listener ports.
        self.https_ports = https_ports
        # Specifies whether to enable IPv6 protection. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.ipv_6enabled = ipv_6enabled
        # The type of the protection resource. Valid values:
        # 
        # *   **share** (default): a shared cluster.
        # *   **gslb**: shared cluster-based intelligent load balancing.
        self.protection_resource = protection_resource
        # Specifies whether to allow access only from SM certificate-based clients. This parameter is available only if you set SM2Enabled to true.
        # 
        # *   true
        # *   false
        self.sm2access_only = sm2access_only
        # The ID of the SM certificate that you want to add. This parameter is available only if you set SM2Enabled to true.
        self.sm2cert_id = sm2cert_id
        # Specifies whether to add an SM certificate.
        self.sm2enabled = sm2enabled
        # The Transport Layer Security (TLS) version that you want to add. This parameter is available only if you specify **HttpsPorts**. Valid values:
        # 
        # *   **tlsv1**
        # *   **tlsv1.1**
        # *   **tlsv1.2**
        self.tlsversion = tlsversion
        # The method that is used to obtain the originating IP address of a client. Valid values:
        # 
        # *   **0** (default): Client traffic is not filtered by a Layer 7 proxy before the traffic reaches WAF.
        # *   **1**: WAF reads the first value of the X-Forwarded-For (XFF) header field as the originating IP address of the client.
        # *   **2**: WAF reads the value of a custom header field as the originating IP address of the client.
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

