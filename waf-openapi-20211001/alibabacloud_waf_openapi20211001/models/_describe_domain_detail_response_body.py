# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainDetailResponseBody(DaraModel):
    def __init__(
        self,
        cert_detail: main_models.DescribeDomainDetailResponseBodyCertDetail = None,
        cname: str = None,
        domain: str = None,
        domain_id: str = None,
        listen: main_models.DescribeDomainDetailResponseBodyListen = None,
        redirect: main_models.DescribeDomainDetailResponseBodyRedirect = None,
        request_id: str = None,
        resource_manager_resource_group_id: str = None,
        sm2cert_detail: main_models.DescribeDomainDetailResponseBodySM2CertDetail = None,
        status: int = None,
    ):
        # The details of the SSL certificate.
        self.cert_detail = cert_detail
        # The CNAME assigned by WAF to the domain name.
        self.cname = cname
        # The domain name that is onboarded to WAF.
        self.domain = domain
        # The ID of the domain name that is onboarded to WAF.
        self.domain_id = domain_id
        # The listener configurations.
        self.listen = listen
        # The forwarding configurations.
        self.redirect = redirect
        # The request ID.
        self.request_id = request_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The details of the SM certificate.
        self.sm2cert_detail = sm2cert_detail
        # The status of the domain name. Valid values:
        # 
        # - **1**: The domain name is in normal status.
        # 
        # - **2**: The domain name is being created.
        # 
        # - **3**: The domain name is being modified.
        # 
        # - **4**: The domain name is being released.
        # 
        # - **5**: The domain name stops forwarding traffic.
        self.status = status

    def validate(self):
        if self.cert_detail:
            self.cert_detail.validate()
        if self.listen:
            self.listen.validate()
        if self.redirect:
            self.redirect.validate()
        if self.sm2cert_detail:
            self.sm2cert_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_detail is not None:
            result['CertDetail'] = self.cert_detail.to_map()

        if self.cname is not None:
            result['Cname'] = self.cname

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.listen is not None:
            result['Listen'] = self.listen.to_map()

        if self.redirect is not None:
            result['Redirect'] = self.redirect.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.sm2cert_detail is not None:
            result['SM2CertDetail'] = self.sm2cert_detail.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertDetail') is not None:
            temp_model = main_models.DescribeDomainDetailResponseBodyCertDetail()
            self.cert_detail = temp_model.from_map(m.get('CertDetail'))

        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('Listen') is not None:
            temp_model = main_models.DescribeDomainDetailResponseBodyListen()
            self.listen = temp_model.from_map(m.get('Listen'))

        if m.get('Redirect') is not None:
            temp_model = main_models.DescribeDomainDetailResponseBodyRedirect()
            self.redirect = temp_model.from_map(m.get('Redirect'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('SM2CertDetail') is not None:
            temp_model = main_models.DescribeDomainDetailResponseBodySM2CertDetail()
            self.sm2cert_detail = temp_model.from_map(m.get('SM2CertDetail'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDomainDetailResponseBodySM2CertDetail(DaraModel):
    def __init__(
        self,
        common_name: str = None,
        end_time: int = None,
        id: str = None,
        name: str = None,
        sans: List[str] = None,
        start_time: int = None,
    ):
        # The common name of the SM certificate.
        self.common_name = common_name
        # The end of the validity period of the SM certificate. This value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time
        # The ID of the SM certificate.
        self.id = id
        # The name of the SM certificate.
        self.name = name
        # The domain names that are bound to the SM certificate.
        self.sans = sans
        # The beginning of the validity period of the SM certificate. This value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.sans is not None:
            result['Sans'] = self.sans

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Sans') is not None:
            self.sans = m.get('Sans')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeDomainDetailResponseBodyRedirect(DaraModel):
    def __init__(
        self,
        back_up_backend_list: List[str] = None,
        backend_list: List[str] = None,
        backend_ports: List[main_models.DescribeDomainDetailResponseBodyRedirectBackendPorts] = None,
        backends: List[main_models.DescribeDomainDetailResponseBodyRedirectBackends] = None,
        backup_backends: List[main_models.DescribeDomainDetailResponseBodyRedirectBackupBackends] = None,
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
        request_headers: List[main_models.DescribeDomainDetailResponseBodyRedirectRequestHeaders] = None,
        retry: bool = None,
        sni_enabled: bool = None,
        sni_host: str = None,
        wlproxy_client_ip: bool = None,
        web_server_type: bool = None,
        write_timeout: int = None,
        xclient_ip: bool = None,
        xtrue_ip: bool = None,
        xff_proto: bool = None,
    ):
        # The list of IP addresses or domain names of the backup origin servers for the domain name.
        self.back_up_backend_list = back_up_backend_list
        # The list of IP addresses or domain names of the origin servers for the domain name.
        self.backend_list = backend_list
        # The custom back-to-origin port mappings. By default, the back-to-origin port is the same as the listener port.
        self.backend_ports = backend_ports
        # The addresses of origin servers.
        # 
        # > This parameter will be deprecated. We recommend that you use **BackendList** instead.
        self.backends = backends
        # The addresses of backup origin servers.
        # 
        # > This parameter will be deprecated. We recommend that you use **BackUpBackendList** instead.
        self.backup_backends = backup_backends
        # The timeout period for connections. Unit: seconds. Valid values: 5 to 120.
        self.connect_timeout = connect_timeout
        # Indicates whether back-to-origin requests are forced to use HTTP. Valid values:
        # 
        # - **true**: Requests are forced to use HTTP.
        # 
        # - **false**: Requests are not forced to use HTTP.
        self.focus_http_backend = focus_http_backend
        # Indicates whether HTTP/2 is enabled for back-to-origin requests.
        self.http_2origin = http_2origin
        # The maximum number of concurrent connections for HTTP/2 back-to-origin requests.
        self.http_2origin_max_concurrency = http_2origin_max_concurrency
        # Indicates whether persistent connections are enabled. Valid values:
        # 
        # - **true** (default): Persistent connections are enabled.
        # 
        # - **false**: Persistent connections are disabled.
        self.keepalive = keepalive
        # The maximum number of requests that reuse a persistent connection. Valid values: 60 to 1,000.
        # 
        # > The number of reused persistent connections after the persistent connection feature is enabled.
        self.keepalive_requests = keepalive_requests
        # The timeout period for idle persistent connections. Valid values: 1 to 60. Default value: 15. Unit: seconds.
        # 
        # > The period of time during which a reused persistent connection is allowed to remain idle before the connection is closed.
        self.keepalive_timeout = keepalive_timeout
        # The load balancing algorithm used when WAF forwards requests to the origin server. Valid values:
        # 
        # - **iphash**: the IP hash algorithm.
        # 
        # - **roundRobin**: the round-robin algorithm.
        # 
        # - **leastTime**: the least time algorithm.
        self.loadbalance = loadbalance
        # The maximum size of a request body. Valid values: 2 to 10. Default value: 2. Unit: GB.
        # 
        # > This feature is available only for the Ultimate edition.
        self.max_body_size = max_body_size
        # Indicates whether the Proxy Protocol feature is enabled for back-to-origin requests. Valid values:
        # 
        # - **true**: The Proxy Protocol feature is enabled.
        # 
        # - **false**: The Proxy Protocol feature is disabled.
        self.proxy_protocol = proxy_protocol
        # The timeout period for read operations. Unit: seconds. Valid values: 5 to 1,800.
        self.read_timeout = read_timeout
        # The custom header fields used to mark requests that pass through WAF.
        self.request_headers = request_headers
        # Indicates whether WAF retries forwarding requests to the origin server upon failure. Valid values:
        # 
        # - **true** (default): WAF retries.
        # 
        # - **false**: WAF does not retry.
        self.retry = retry
        # Indicates whether origin Server Name Indication (SNI) is enabled. Valid values:
        # 
        # - **true**: Origin SNI is enabled.
        # 
        # - **false** (default): Origin SNI is not enabled.
        self.sni_enabled = sni_enabled
        # The value of the SNI field.
        self.sni_host = sni_host
        # Indicates whether the WL-Proxy-Client-IP header is included in back-to-origin requests. Valid values:
        # 
        # - **true** (default): The WL-Proxy-Client-IP header is included.
        # 
        # - **false**: The WL-Proxy-Client-IP header is not included.
        self.wlproxy_client_ip = wlproxy_client_ip
        # Indicates whether the Web-Server-Type header is included in back-to-origin requests. Valid values:
        # 
        # - **true** (default): The Web-Server-Type header is included.
        # 
        # - **false**: The Web-Server-Type header is not included.
        self.web_server_type = web_server_type
        # The timeout period for write operations. Unit: seconds. Valid values: 5 to 1,800.
        self.write_timeout = write_timeout
        # Indicates whether the X-Client-IP header is included in back-to-origin requests. Valid values:
        # 
        # - **true** (default): The X-Client-IP header is included.
        # 
        # - **false**: The X-Client-IP header is not included.
        self.xclient_ip = xclient_ip
        # Indicates whether the X-True-IP header is included in back-to-origin requests. Valid values:
        # 
        # - **true** (default): The X-True-IP header is included.
        # 
        # - **false**: The X-True-IP header is not included.
        self.xtrue_ip = xtrue_ip
        # Indicates whether the X-Forward-For-Proto header is included in back-to-origin requests to pass the protocol used by WAF. Valid values:
        # 
        # - **true** (default): The X-Forward-For-Proto header is included.
        # 
        # - **false**: The X-Forward-For-Proto header is not included.
        self.xff_proto = xff_proto

    def validate(self):
        if self.backend_ports:
            for v1 in self.backend_ports:
                 if v1:
                    v1.validate()
        if self.backends:
            for v1 in self.backends:
                 if v1:
                    v1.validate()
        if self.backup_backends:
            for v1 in self.backup_backends:
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
        if self.back_up_backend_list is not None:
            result['BackUpBackendList'] = self.back_up_backend_list

        if self.backend_list is not None:
            result['BackendList'] = self.backend_list

        result['BackendPorts'] = []
        if self.backend_ports is not None:
            for k1 in self.backend_ports:
                result['BackendPorts'].append(k1.to_map() if k1 else None)

        result['Backends'] = []
        if self.backends is not None:
            for k1 in self.backends:
                result['Backends'].append(k1.to_map() if k1 else None)

        result['BackupBackends'] = []
        if self.backup_backends is not None:
            for k1 in self.backup_backends:
                result['BackupBackends'].append(k1.to_map() if k1 else None)

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
        if m.get('BackUpBackendList') is not None:
            self.back_up_backend_list = m.get('BackUpBackendList')

        if m.get('BackendList') is not None:
            self.backend_list = m.get('BackendList')

        self.backend_ports = []
        if m.get('BackendPorts') is not None:
            for k1 in m.get('BackendPorts'):
                temp_model = main_models.DescribeDomainDetailResponseBodyRedirectBackendPorts()
                self.backend_ports.append(temp_model.from_map(k1))

        self.backends = []
        if m.get('Backends') is not None:
            for k1 in m.get('Backends'):
                temp_model = main_models.DescribeDomainDetailResponseBodyRedirectBackends()
                self.backends.append(temp_model.from_map(k1))

        self.backup_backends = []
        if m.get('BackupBackends') is not None:
            for k1 in m.get('BackupBackends'):
                temp_model = main_models.DescribeDomainDetailResponseBodyRedirectBackupBackends()
                self.backup_backends.append(temp_model.from_map(k1))

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
                temp_model = main_models.DescribeDomainDetailResponseBodyRedirectRequestHeaders()
                self.request_headers.append(temp_model.from_map(k1))

        if m.get('Retry') is not None:
            self.retry = m.get('Retry')

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

class DescribeDomainDetailResponseBodyRedirectRequestHeaders(DaraModel):
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

class DescribeDomainDetailResponseBodyRedirectBackupBackends(DaraModel):
    def __init__(
        self,
        backend: str = None,
    ):
        # The backup IP address or domain name of the origin server.
        self.backend = backend

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend is not None:
            result['Backend'] = self.backend

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Backend') is not None:
            self.backend = m.get('Backend')

        return self

class DescribeDomainDetailResponseBodyRedirectBackends(DaraModel):
    def __init__(
        self,
        backend: str = None,
    ):
        # The IP address or domain name of the origin server.
        self.backend = backend

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend is not None:
            result['Backend'] = self.backend

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Backend') is not None:
            self.backend = m.get('Backend')

        return self

class DescribeDomainDetailResponseBodyRedirectBackendPorts(DaraModel):
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
        # The protocol of the back-to-origin port. Valid values:
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

class DescribeDomainDetailResponseBodyListen(DaraModel):
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
        # The ID of the certificate.
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
        # Indicates whether an exclusive IP address is enabled for the domain name. Valid values:
        # 
        # - **true**: An exclusive IP address is enabled for the domain name.
        # 
        # - **false**: An exclusive IP address is not enabled for the domain name.
        self.exclusive_ip = exclusive_ip
        # Indicates whether HTTP to HTTPS redirection is enabled for the domain name. Valid values:
        # 
        # - **true**: HTTP to HTTPS redirection is enabled for the domain name.
        # 
        # - **false**: HTTP to HTTPS redirection is not enabled for the domain name.
        self.focus_https = focus_https
        # Indicates whether HSTS includes subdomains. Valid values:
        # 
        # - **true**: HSTS includes subdomains.
        # 
        # - **false**: HSTS does not include subdomains.
        self.hsts_include_sub_domain = hsts_include_sub_domain
        # The maximum age value of the HSTS policy. Unit: seconds.
        self.hsts_max_age = hsts_max_age
        # Indicates whether HSTS preload is enabled. Default value: false. Valid values:
        # 
        # - **true**: HSTS preload is enabled.
        # 
        # - **false**: HSTS preload is disabled.
        self.hsts_preload = hsts_preload
        # Indicates whether HTTP/2 is enabled. Valid values:
        # 
        # - **true**: HTTP/2 is enabled.
        # 
        # - **false**: HTTP/2 is not enabled.
        self.http_2enabled = http_2enabled
        # The HTTP listener ports.
        self.http_ports = http_ports
        # The HTTPS listener ports.
        self.https_ports = https_ports
        # Indicates whether IPv6 is enabled. Valid values:
        # 
        # - **true**: IPv6 is enabled.
        # 
        # - **false**: IPv6 is not enabled.
        self.ipv_6enabled = ipv_6enabled
        # The type of the protection resource. Valid values:
        # 
        # - **share**: shared cluster.
        # 
        # - **gslb**: intelligent load balancing for shared clusters.
        self.protection_resource = protection_resource
        # Indicates whether only SM certificate-based clients can access the domain name. This parameter is available only if you set SM2Enabled to true. Valid values:
        # 
        # - **true**: Only SM certificate-based clients can access the domain name.
        # 
        # - **false**: Both SM certificate-based and non-SM certificate-based clients can access the domain name.
        self.sm2access_only = sm2access_only
        # The ID of the SM certificate. This parameter is available only if you set SM2Enabled to true.
        self.sm2cert_id = sm2cert_id
        # Indicates whether SM certificate-based verification is enabled. Valid values:
        # 
        # - **true**: SM certificate-based verification is enabled.
        # 
        # - **false**: SM certificate-based verification is not enabled.
        self.sm2enabled = sm2enabled
        # The version of the Transport Layer Security (TLS) protocol. Valid values:
        # 
        # - **tlsv1**
        # 
        # - **tlsv1.1**
        # 
        # - **tlsv1.2**
        self.tlsversion = tlsversion
        # The method that WAF uses to obtain the originating IP address of a client. Valid values:
        # 
        # - **0**: The client traffic is not forwarded by a Layer 7 proxy before the traffic reaches WAF.
        # 
        # - **1**: WAF reads the first value of the X-Forwarded-For (XFF) field in the request header as the client IP address.
        # 
        # - **2**: WAF reads the value of a custom field that you specify in the request header as the client IP address.
        self.xff_header_mode = xff_header_mode
        # The custom header fields used to obtain the actual IP address of a client.
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

class DescribeDomainDetailResponseBodyCertDetail(DaraModel):
    def __init__(
        self,
        common_name: str = None,
        end_time: int = None,
        id: str = None,
        name: str = None,
        sans: List[str] = None,
        start_time: int = None,
    ):
        # The common name of the SSL certificate.
        self.common_name = common_name
        # The end of the validity period of the SSL certificate. This value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time
        # The ID of the SSL certificate.
        self.id = id
        # The name of the SSL certificate.
        self.name = name
        # The domain names that are bound to the certificate.
        self.sans = sans
        # The beginning of the validity period of the SSL certificate. This value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.sans is not None:
            result['Sans'] = self.sans

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Sans') is not None:
            self.sans = m.get('Sans')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

