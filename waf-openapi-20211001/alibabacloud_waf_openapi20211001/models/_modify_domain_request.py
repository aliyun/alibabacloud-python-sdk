# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class ModifyDomainRequest(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        domain: str = None,
        domain_id: str = None,
        instance_id: str = None,
        listen: main_models.ModifyDomainRequestListen = None,
        redirect: main_models.ModifyDomainRequestRedirect = None,
        region_id: str = None,
    ):
        # The access type of the WAF instance. Valid values:
        self.access_type = access_type
        # The domain name to operate on.
        self.domain = domain
        # The domain name ID.
        self.domain_id = domain_id
        # The ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The listening configuration.
        # 
        # This parameter is required.
        self.listen = listen
        # The forwarding configuration.
        # 
        # This parameter is required.
        self.redirect = redirect
        # The region where the WAF instance resides. Valid values:
        # 
        # This parameter is required.
        self.region_id = region_id

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
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.listen is not None:
            result['Listen'] = self.listen.to_map()

        if self.redirect is not None:
            result['Redirect'] = self.redirect.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Listen') is not None:
            temp_model = main_models.ModifyDomainRequestListen()
            self.listen = temp_model.from_map(m.get('Listen'))

        if m.get('Redirect') is not None:
            temp_model = main_models.ModifyDomainRequestRedirect()
            self.redirect = temp_model.from_map(m.get('Redirect'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ModifyDomainRequestRedirect(DaraModel):
    def __init__(
        self,
        backend_ports: List[main_models.ModifyDomainRequestRedirectBackendPorts] = None,
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
        request_headers: List[main_models.ModifyDomainRequestRedirectRequestHeaders] = None,
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
        # The IP addresses or domain names of the origin servers that correspond to the domain name. You can specify only IP addresses or domain names, not both. When the back-to-origin address is a domain name, only IPv4 is supported. IPv6 is not supported.
        self.backends = backends
        # The IP addresses or domain names of the secondary origin servers that correspond to the domain name.
        self.backup_backends = backup_backends
        # Specifies whether to enable public cloud disaster recovery. Valid values:
        self.cname_enabled = cname_enabled
        # The connection timeout period. Unit: seconds.
        self.connect_timeout = connect_timeout
        # Specifies whether to enable forced HTTP back-to-origin. This parameter is available only when **HttpsPorts** is not empty, which indicates that the domain name uses HTTPS. Valid values:
        self.focus_http_backend = focus_http_backend
        # Specifies whether to enable HTTP/2 back-to-origin. Valid values:
        self.http_2origin = http_2origin
        # The maximum number of concurrent HTTP/2 back-to-origin connections. Valid values: 1 to 512. Default value: 2.
        self.http_2origin_max_concurrency = http_2origin_max_concurrency
        # Specifies whether to enable persistent connections. Valid values:
        self.keepalive = keepalive
        # The number of requests that reuse a persistent connection. Valid values: 60 to 1000. Default value: 1000.
        self.keepalive_requests = keepalive_requests
        # The idle persistent connection timeout period. Valid values: 1 to 60. Default value: 15. Unit: seconds.
        self.keepalive_timeout = keepalive_timeout
        # The load balancing algorithm used for back-to-origin. Valid values:
        # 
        # This parameter is required.
        self.loadbalance = loadbalance
        # The maximum request body size. Valid values: 2 to 10. Default value: 2. Unit: GB.
        self.max_body_size = max_body_size
        # Indicates whether the client source IP preservation feature is enabled.
        self.proxy_protocol = proxy_protocol
        # The read timeout period. Unit: seconds.
        self.read_timeout = read_timeout
        # The traffic tag fields and values of the domain name, used to tag traffic processed by WAF.
        self.request_headers = request_headers
        # Specifies whether to retry when WAF fails to forward requests to the origin server. Valid values:
        self.retry = retry
        # The hybrid cloud forwarding rules. The value is a string converted from a JSON array. Each element in the JSON array is a struct that contains the following fields:
        self.routing_rules = routing_rules
        # Specifies whether to enable back-to-origin SNI. This parameter is available only when **HttpsPorts** is not empty, which indicates that the domain name uses HTTPS. Valid values:
        self.sni_enabled = sni_enabled
        # The value of the custom SNI extension field. If this parameter is not specified, the value of the **Host** field in the request header is used as the SNI extension field value by default.
        self.sni_host = sni_host
        # Specifies whether to allow WAF to overwrite WL-Proxy-Client-IP. Valid values:
        self.wlproxy_client_ip = wlproxy_client_ip
        # Specifies whether to allow WAF to overwrite Web-Server-Type. Valid values:
        self.web_server_type = web_server_type
        # The write timeout period. Unit: seconds.
        self.write_timeout = write_timeout
        # Specifies whether to allow WAF to overwrite X-Client-IP. Valid values:
        self.xclient_ip = xclient_ip
        # Specifies whether to allow WAF to overwrite X-True-IP. Valid values:
        self.xtrue_ip = xtrue_ip
        # Specifies whether X-Forward-For-Proto passes the WAF protocol. Valid values:
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
                temp_model = main_models.ModifyDomainRequestRedirectBackendPorts()
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
                temp_model = main_models.ModifyDomainRequestRedirectRequestHeaders()
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

class ModifyDomainRequestRedirectRequestHeaders(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The custom request header field.
        self.key = key
        # The value set for the custom request header field.
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

class ModifyDomainRequestRedirectBackendPorts(DaraModel):
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
        # The protocol of the listening port. Valid values:
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

class ModifyDomainRequestListen(DaraModel):
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
        # The ID of the certificate to add.
        self.cert_id = cert_id
        # The type of cipher suite to add. This parameter is available only when **HttpsPorts** is not empty, which indicates that the domain name uses HTTPS. Valid values:
        self.cipher_suite = cipher_suite
        # The specific custom cipher suites to add. This parameter is available only when **CipherSuite** is set to **99**.
        self.custom_ciphers = custom_ciphers
        # Specifies whether to support TLS 1.3. Valid values:
        self.enable_tlsv_3 = enable_tlsv_3
        # Specifies whether to enable an exclusive IP address. This parameter is available only when **IPv6Enabled** is set to false and **ProtectionResource** is set to **share**, which indicates that a shared cluster is used. Valid values:
        self.exclusive_ip = exclusive_ip
        # Specifies whether to enable forced HTTPS redirect. This parameter is available only when **HttpsPorts** is not empty, which indicates that the domain name uses HTTPS, and **HttpPorts** is empty, which indicates that the domain name does not use HTTP. Valid values:
        self.focus_https = focus_https
        # Specifies whether HSTS includes subdomains. Valid values:
        self.hsts_include_sub_domain = hsts_include_sub_domain
        # The HSTS expiration time. Unit: seconds.
        self.hsts_max_age = hsts_max_age
        # Specifies whether to enable HSTS preloading. This feature is disabled by default. Valid values:
        self.hsts_preload = hsts_preload
        # Specifies whether to enable HTTP/2. This parameter is available only when **HttpsPorts** is not empty, which indicates that the domain name uses HTTPS. Valid values:
        self.http_2enabled = http_2enabled
        # The listening ports for HTTP. Use the [**port1,port2,...**] format.
        self.http_ports = http_ports
        # The listening ports for HTTPS. Use the [**port1,port2,...**] format.
        self.https_ports = https_ports
        # Specifies whether to enable IPv6. Valid values:
        self.ipv_6enabled = ipv_6enabled
        # The type of protection resource to use. Valid values:
        self.protection_resource = protection_resource
        # Specifies whether to allow only SM2 client access. This parameter is available only when SM2Enable is set to true.
        self.sm2access_only = sm2access_only
        # The ID of the SM2 certificate to add. This parameter is available only when SM2Enable is set to true.
        self.sm2cert_id = sm2cert_id
        # Specifies whether to enable SM2 certificates.
        self.sm2enabled = sm2enabled
        # The TLS version to add. This parameter is available only when **HttpsPorts** is not empty, which indicates that the domain name uses HTTPS. Valid values:
        self.tlsversion = tlsversion
        # The method that WAF uses to obtain the originating IP address of the client. Valid values:
        self.xff_header_mode = xff_header_mode
        # The list of custom header fields used to obtain the client IP address. Use the [**"header1","header2",...**] format.
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

