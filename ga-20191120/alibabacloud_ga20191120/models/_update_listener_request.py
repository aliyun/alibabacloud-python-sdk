# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class UpdateListenerRequest(DaraModel):
    def __init__(
        self,
        backend_ports: List[main_models.UpdateListenerRequestBackendPorts] = None,
        certificates: List[main_models.UpdateListenerRequestCertificates] = None,
        client_affinity: str = None,
        client_token: str = None,
        description: str = None,
        http_version: str = None,
        idle_timeout: int = None,
        listener_id: str = None,
        name: str = None,
        port_ranges: List[main_models.UpdateListenerRequestPortRanges] = None,
        protocol: str = None,
        proxy_protocol: str = None,
        region_id: str = None,
        request_timeout: int = None,
        security_policy_id: str = None,
        xforwarded_for_config: main_models.UpdateListenerRequestXForwardedForConfig = None,
    ):
        # The range of ports that are used by backend servers to receive requests.
        self.backend_ports = backend_ports
        # The SSL certificate.
        self.certificates = certificates
        # Indicates whether client affinity is enabled for the listener. Valid values:
        # 
        # *   **NONE**: Client affinity is disabled. Requests from the same client may be forwarded to different endpoints.
        # *   **SOURCE_IP**: Client affinity is enabled. When a client accesses stateful applications, requests from the same client are forwarded to the same endpoint regardless of the source port or protocol.
        self.client_affinity = client_affinity
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The description of the listener.
        # 
        # The description can be up to 200 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The maximum version of the HTTP protocol. Valid values:
        # 
        # *   **http3**
        # *   **http2**
        # *   **http1.1**
        # 
        # >  Only HTTPS listeners support this parameter.
        self.http_version = http_version
        # The timeout period for idle connections. Unit: seconds.
        # 
        # *   TCP: 10-900. Default value: 900. Unit: seconds.
        # *   UDP: 10-20. Default value: 20. Unit: seconds.
        # *   HTTP/HTTPS: 1-60. Default value: 15. Unit: seconds.
        self.idle_timeout = idle_timeout
        # The ID of the listener.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The name of the listener.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        self.name = name
        # The listener ports that are used to receive requests and forward the requests to endpoints.
        # 
        # Valid values: **1** to **65499**.
        # 
        # The maximum number of ports that can be configured varies based on the routing type and protocol of the listener. For more information, see [Listener overview](https://help.aliyun.com/document_detail/153216.html).
        self.port_ranges = port_ranges
        # The network transmission protocol that is used by the listener. Valid values:
        # 
        # *   **tcp**: TCP
        # *   **udp**: UDP
        # *   **http**: HTTP
        # *   **https**: HTTPS
        self.protocol = protocol
        # Specifies whether to preserve source IP addresses of clients.
        # 
        # *   **true** This feature allows you to view client IP addresses on backend servers.
        # *   **false** (default)
        # 
        # >  This parameter will be discontinued in the API operations that are used to configure listeners. We recommend that you set this parameter when you call API operations to configure endpoint groups. For more information about the **ProxyProtocol** parameter, see [CreateEndpointGroup](https://help.aliyun.com/document_detail/153259.html) and [UpdateEndpointGroup](https://help.aliyun.com/document_detail/153262.html).
        self.proxy_protocol = proxy_protocol
        # The ID of the region where the Global Accelerator (GA) instance is deployed. Set the value to **cn-hangzhou**.
        self.region_id = region_id
        # The timeout period for HTTP or HTTPS requests.
        # 
        # Valid values: 1 to 180. Default value: 60. Unit: seconds.
        # 
        # >  This parameter takes effect only for HTTP or HTTPS listeners. If the backend server does not respond within the timeout period, GA returns an HTTP 504 error code to the client.
        self.request_timeout = request_timeout
        # The ID of the security policy. Valid values:
        # 
        # *   **tls_cipher_policy_1_0**
        # 
        #     *   Supported Transport Layer Security (TLS) versions: TLS 1.0, TLS 1.1, and TLS 1.2
        #     *   Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM-SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA
        # 
        # *   **tls_cipher_policy_1_1**
        # 
        #     *   Supported TLS versions: TLS 1.1 and TLS 1.2
        #     *   Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM-SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA
        # 
        # *   **tls_cipher_policy_1_2**
        # 
        #     *   Supported TLS version: TLS 1.2
        #     *   Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM-SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA
        # 
        # *   **tls_cipher_policy_1_2_strict**
        # 
        #     *   Supported TLS version: TLS 1.2
        #     *   Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, ECDHE-RSA-AES128-SHA, and ECDHE-RSA-AES256-SHA
        # 
        # *   **tls_cipher_policy_1_2_strict_with_1_3**
        # 
        #     *   Supported TLS versions: TLS 1.2 and TLS 1.3
        #     *   Supported cipher suites: TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384, TLS_CHACHA20_POLY1305_SHA256, TLS_AES_128_CCM_SHA256, TLS_AES_128_CCM_8_SHA256, ECDHE-ECDSA-AES128-GCM-SHA256, ECDHE-ECDSA-AES256-GCM-SHA384, ECDHE-ECDSA-AES128-SHA256, ECDHE-ECDSA-AES256-SHA384, ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, ECDHE-ECDSA-AES128-SHA, ECDHE-ECDSA-AES256-SHA, ECDHE-RSA-AES128-SHA, and ECDHE-RSA-AES256-SHA
        # 
        # > This parameter is available only when you create an HTTPS listener.
        self.security_policy_id = security_policy_id
        # The `XForward` headers.
        self.xforwarded_for_config = xforwarded_for_config

    def validate(self):
        if self.backend_ports:
            for v1 in self.backend_ports:
                 if v1:
                    v1.validate()
        if self.certificates:
            for v1 in self.certificates:
                 if v1:
                    v1.validate()
        if self.port_ranges:
            for v1 in self.port_ranges:
                 if v1:
                    v1.validate()
        if self.xforwarded_for_config:
            self.xforwarded_for_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackendPorts'] = []
        if self.backend_ports is not None:
            for k1 in self.backend_ports:
                result['BackendPorts'].append(k1.to_map() if k1 else None)

        result['Certificates'] = []
        if self.certificates is not None:
            for k1 in self.certificates:
                result['Certificates'].append(k1.to_map() if k1 else None)

        if self.client_affinity is not None:
            result['ClientAffinity'] = self.client_affinity

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.http_version is not None:
            result['HttpVersion'] = self.http_version

        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.name is not None:
            result['Name'] = self.name

        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k1 in self.port_ranges:
                result['PortRanges'].append(k1.to_map() if k1 else None)

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.proxy_protocol is not None:
            result['ProxyProtocol'] = self.proxy_protocol

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout

        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id

        if self.xforwarded_for_config is not None:
            result['XForwardedForConfig'] = self.xforwarded_for_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_ports = []
        if m.get('BackendPorts') is not None:
            for k1 in m.get('BackendPorts'):
                temp_model = main_models.UpdateListenerRequestBackendPorts()
                self.backend_ports.append(temp_model.from_map(k1))

        self.certificates = []
        if m.get('Certificates') is not None:
            for k1 in m.get('Certificates'):
                temp_model = main_models.UpdateListenerRequestCertificates()
                self.certificates.append(temp_model.from_map(k1))

        if m.get('ClientAffinity') is not None:
            self.client_affinity = m.get('ClientAffinity')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HttpVersion') is not None:
            self.http_version = m.get('HttpVersion')

        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k1 in m.get('PortRanges'):
                temp_model = main_models.UpdateListenerRequestPortRanges()
                self.port_ranges.append(temp_model.from_map(k1))

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('ProxyProtocol') is not None:
            self.proxy_protocol = m.get('ProxyProtocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')

        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')

        if m.get('XForwardedForConfig') is not None:
            temp_model = main_models.UpdateListenerRequestXForwardedForConfig()
            self.xforwarded_for_config = temp_model.from_map(m.get('XForwardedForConfig'))

        return self

class UpdateListenerRequestXForwardedForConfig(DaraModel):
    def __init__(
        self,
        xforwarded_for_ga_ap_enabled: bool = None,
        xforwarded_for_ga_id_enabled: bool = None,
        xforwarded_for_port_enabled: bool = None,
        xforwarded_for_proto_enabled: bool = None,
        xreal_ip_enabled: bool = None,
    ):
        # Specifies whether to use the `GA-AP` header to retrieve information about acceleration regions. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        # 
        # > This parameter is available only when you create an HTTPS or HTTP listener.
        self.xforwarded_for_ga_ap_enabled = xforwarded_for_ga_ap_enabled
        # Specifies whether to use the `GA-ID` header to retrieve the ID of the GA instance. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        # 
        # > This parameter is available only when you create an HTTPS or HTTP listener.
        self.xforwarded_for_ga_id_enabled = xforwarded_for_ga_id_enabled
        # Specifies whether to use the `GA-X-Forward-Port` header to retrieve the listener ports of the GA instance. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        # 
        # > This parameter is available only when you create an HTTPS or HTTP listener.
        self.xforwarded_for_port_enabled = xforwarded_for_port_enabled
        # Specifies whether to use the `GA-X-Forward-Proto` header to retrieve the listener protocol of the GA instance. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        # 
        # > This parameter is available only when you create an HTTPS or HTTP listener.
        self.xforwarded_for_proto_enabled = xforwarded_for_proto_enabled
        # Specifies whether to use the `X-Real-IP` header to retrieve client IP addresses. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        # 
        # > This parameter is available only when you create an HTTPS or HTTP listener.
        self.xreal_ip_enabled = xreal_ip_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.xforwarded_for_ga_ap_enabled is not None:
            result['XForwardedForGaApEnabled'] = self.xforwarded_for_ga_ap_enabled

        if self.xforwarded_for_ga_id_enabled is not None:
            result['XForwardedForGaIdEnabled'] = self.xforwarded_for_ga_id_enabled

        if self.xforwarded_for_port_enabled is not None:
            result['XForwardedForPortEnabled'] = self.xforwarded_for_port_enabled

        if self.xforwarded_for_proto_enabled is not None:
            result['XForwardedForProtoEnabled'] = self.xforwarded_for_proto_enabled

        if self.xreal_ip_enabled is not None:
            result['XRealIpEnabled'] = self.xreal_ip_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('XForwardedForGaApEnabled') is not None:
            self.xforwarded_for_ga_ap_enabled = m.get('XForwardedForGaApEnabled')

        if m.get('XForwardedForGaIdEnabled') is not None:
            self.xforwarded_for_ga_id_enabled = m.get('XForwardedForGaIdEnabled')

        if m.get('XForwardedForPortEnabled') is not None:
            self.xforwarded_for_port_enabled = m.get('XForwardedForPortEnabled')

        if m.get('XForwardedForProtoEnabled') is not None:
            self.xforwarded_for_proto_enabled = m.get('XForwardedForProtoEnabled')

        if m.get('XRealIpEnabled') is not None:
            self.xreal_ip_enabled = m.get('XRealIpEnabled')

        return self

class UpdateListenerRequestPortRanges(DaraModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        # The first port of the listener port range that is used to receive and forward requests to endpoints.
        # 
        # Valid values: **1** to **65499**. The **FromPort** value must be smaller than or equal to the **ToPort** value.
        # 
        # The maximum number of ports that can be configured varies based on the routing type and protocol of the listener. For more information, see [Listener overview](https://help.aliyun.com/document_detail/153216.html).
        # 
        # > You can configure only one listener port for an HTTP or HTTPS listener. In this case, the first port is the same as the last port.
        # 
        # This parameter is required.
        self.from_port = from_port
        # The last port of the listener port range that is used to receive and forward requests to endpoints.
        # 
        # Valid values: **1** to **65499**. The **FromPort** value must be smaller than or equal to the **ToPort** value.
        # 
        # The maximum number of ports that can be configured varies based on the routing type and protocol of the listener. For more information, see [Listener overview](https://help.aliyun.com/document_detail/153216.html).
        # 
        # > You can configure only one listener port for an HTTP or HTTPS listener. In this case, the first port is the same as the last port.
        # 
        # This parameter is required.
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_port is not None:
            result['FromPort'] = self.from_port

        if self.to_port is not None:
            result['ToPort'] = self.to_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')

        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')

        return self

class UpdateListenerRequestCertificates(DaraModel):
    def __init__(
        self,
        id: str = None,
    ):
        # The ID of the SSL certificate.
        # 
        # > This parameter is required only when you configure an HTTPS listener.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class UpdateListenerRequestBackendPorts(DaraModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        # The first port in the range of ports that are used by backend servers to receive requests.
        # 
        # > This parameter is required only when you configure an HTTPS or HTTP listener and the listener port is different from the service port of the backend servers. In this case, the first port that is used by the backend servers to receive requests must be the same as the last port.
        self.from_port = from_port
        # The last port in the range of ports that are used by backend servers to receive requests.
        # 
        # > This parameter is required only when you configure an HTTPS or HTTP listener and the listener port is different from the service port of the backend servers. In this case, the first port that is used by the backend servers to receive requests must be the same as the last port.
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_port is not None:
            result['FromPort'] = self.from_port

        if self.to_port is not None:
            result['ToPort'] = self.to_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')

        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')

        return self

