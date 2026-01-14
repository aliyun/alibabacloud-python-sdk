# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListListenersResponseBody(DaraModel):
    def __init__(
        self,
        listeners: List[main_models.ListListenersResponseBodyListeners] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the listeners.
        self.listeners = listeners
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.listeners:
            for v1 in self.listeners:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Listeners'] = []
        if self.listeners is not None:
            for k1 in self.listeners:
                result['Listeners'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listeners = []
        if m.get('Listeners') is not None:
            for k1 in m.get('Listeners'):
                temp_model = main_models.ListListenersResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListListenersResponseBodyListeners(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        backend_ports: List[main_models.ListListenersResponseBodyListenersBackendPorts] = None,
        certificates: List[main_models.ListListenersResponseBodyListenersCertificates] = None,
        client_affinity: str = None,
        create_time: int = None,
        description: str = None,
        http_version: str = None,
        idle_timeout: int = None,
        listener_id: str = None,
        name: str = None,
        port_ranges: List[main_models.ListListenersResponseBodyListenersPortRanges] = None,
        protocol: str = None,
        proxy_protocol: bool = None,
        request_timeout: int = None,
        security_policy_id: str = None,
        service_id: str = None,
        service_managed: bool = None,
        service_managed_infos: List[main_models.ListListenersResponseBodyListenersServiceManagedInfos] = None,
        state: str = None,
        type: str = None,
        xforwarded_for_config: main_models.ListListenersResponseBodyListenersXForwardedForConfig = None,
    ):
        # The ID of the GA instance.
        self.accelerator_id = accelerator_id
        # The range of ports that are used by backend servers.
        self.backend_ports = backend_ports
        # The information about the SSL certificates.
        self.certificates = certificates
        # Indicates whether client affinity is enabled for the listener.
        # 
        # *   If **NONE** is returned, client affinity is disabled. When client affinity is disabled, requests from the same client may be forwarded to different endpoints.
        # *   If **SOURCE_IP** is returned, client affinity is enabled. When a client accesses stateful applications, requests from the same client are forwarded to the same endpoint regardless of the source port or protocol.
        self.client_affinity = client_affinity
        # The timestamp that indicates when the listener was created. Unit: milliseconds.
        self.create_time = create_time
        # The description of the listener.
        self.description = description
        # The maximum version of the HTTP protocol. Valid values:
        # 
        # *   **http3**
        # *   **http2**
        # *   **http1.1**
        # 
        # >  This parameter is returned only for HTTPS listeners.
        self.http_version = http_version
        # The timeout period of idle connections. Unit: seconds.
        self.idle_timeout = idle_timeout
        # The ID of the listener.
        self.listener_id = listener_id
        # The name of the listener.
        self.name = name
        # The information about the listener ports.
        self.port_ranges = port_ranges
        # The network transmission protocol that is used by the listener. Valid values:
        # 
        # *   **tcp**
        # *   **udp**
        # *   **http**
        # *   **https**
        self.protocol = protocol
        # Indicates whether client IP address preservation is enabled. Valid values:
        # 
        # *   **true**: Client IP address preservation is enabled. This feature allows you to view client IP addresses on backend servers.
        # *   **false**: Client IP address preservation is disabled.
        self.proxy_protocol = proxy_protocol
        # The timeout period of HTTP or HTTPS requests. Unit: seconds.
        # 
        # >  This parameter is returned only for HTTP and HTTPS listeners. If no responses are received from the backend server within the timeout period, GA returns an HTTP 504 error code to the client.
        self.request_timeout = request_timeout
        # The ID of the security policy.
        # 
        # *   **tls_cipher_policy_1_0**
        # 
        #     *   Supported Transport Layer Security (TLS) versions: TLS 1.0, TLS 1.1, and TLS 1.2.
        #     *   Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM-SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA.
        # 
        # *   **tls_cipher_policy_1_1**
        # 
        #     *   Supported TLS versions: TLS 1.1 and TLS 1.2.
        #     *   Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM-SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA.
        # 
        # *   **tls_cipher_policy_1_2**
        # 
        #     *   Supported TLS version: TLS 1.2.
        #     *   Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM-SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA.
        # 
        # *   **tls_cipher_policy_1_2_strict**
        # 
        #     *   Supported TLS version: TLS 1.2.
        #     *   Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, ECDHE-RSA-AES128-SHA, and ECDHE-RSA-AES256-SHA.
        # 
        # *   **tls_cipher_policy_1_2_strict_with_1_3**
        # 
        #     *   Supported TLS versions: TLS 1.2 and TLS 1.3.
        #     *   Supported cipher suites: TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384, TLS_CHACHA20_POLY1305_SHA256, TLS_AES_128_CCM_SHA256, TLS_AES_128_CCM_8_SHA256, ECDHE-ECDSA-AES128-GCM-SHA256, ECDHE-ECDSA-AES256-GCM-SHA384, ECDHE-ECDSA-AES128-SHA256, ECDHE-ECDSA-AES256-SHA384, ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, ECDHE-ECDSA-AES128-SHA, ECDHE-ECDSA-AES256-SHA, ECDHE-RSA-AES128-SHA, and ECDHE-RSA-AES256-SHA.
        # 
        # >  This parameter is returned only for HTTPS listeners.
        self.security_policy_id = security_policy_id
        # The ID of the service that manages the instance.
        # 
        # >  This parameter is returned only if the value of **ServiceManaged** is **true**.
        self.service_id = service_id
        # Indicates whether the instance is managed. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.service_managed = service_managed
        # The actions that users can perform on the managed instance.
        # > *   This parameter is returned only if the value of **ServiceManaged** is **true**.
        # > *   Users can perform only specific actions on a managed instance.
        self.service_managed_infos = service_managed_infos
        # The status of the listener. Valid values:
        # 
        # *   **active**
        # *   **init**
        # *   **updating**
        # *   **deleting**
        self.state = state
        # The routing type of the listener. Valid values:
        # 
        # *   **Standard**: intelligent routing.
        # *   **CustomRouting**: custom routing.
        self.type = type
        # The configurations of the `XForward` headers.
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
        if self.service_managed_infos:
            for v1 in self.service_managed_infos:
                 if v1:
                    v1.validate()
        if self.xforwarded_for_config:
            self.xforwarded_for_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

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

        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout

        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        result['ServiceManagedInfos'] = []
        if self.service_managed_infos is not None:
            for k1 in self.service_managed_infos:
                result['ServiceManagedInfos'].append(k1.to_map() if k1 else None)

        if self.state is not None:
            result['State'] = self.state

        if self.type is not None:
            result['Type'] = self.type

        if self.xforwarded_for_config is not None:
            result['XForwardedForConfig'] = self.xforwarded_for_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        self.backend_ports = []
        if m.get('BackendPorts') is not None:
            for k1 in m.get('BackendPorts'):
                temp_model = main_models.ListListenersResponseBodyListenersBackendPorts()
                self.backend_ports.append(temp_model.from_map(k1))

        self.certificates = []
        if m.get('Certificates') is not None:
            for k1 in m.get('Certificates'):
                temp_model = main_models.ListListenersResponseBodyListenersCertificates()
                self.certificates.append(temp_model.from_map(k1))

        if m.get('ClientAffinity') is not None:
            self.client_affinity = m.get('ClientAffinity')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

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
                temp_model = main_models.ListListenersResponseBodyListenersPortRanges()
                self.port_ranges.append(temp_model.from_map(k1))

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('ProxyProtocol') is not None:
            self.proxy_protocol = m.get('ProxyProtocol')

        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')

        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        self.service_managed_infos = []
        if m.get('ServiceManagedInfos') is not None:
            for k1 in m.get('ServiceManagedInfos'):
                temp_model = main_models.ListListenersResponseBodyListenersServiceManagedInfos()
                self.service_managed_infos.append(temp_model.from_map(k1))

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('XForwardedForConfig') is not None:
            temp_model = main_models.ListListenersResponseBodyListenersXForwardedForConfig()
            self.xforwarded_for_config = temp_model.from_map(m.get('XForwardedForConfig'))

        return self

class ListListenersResponseBodyListenersXForwardedForConfig(DaraModel):
    def __init__(
        self,
        xforwarded_for_ga_ap_enabled: bool = None,
        xforwarded_for_ga_id_enabled: bool = None,
        xforwarded_for_port_enabled: bool = None,
        xforwarded_for_proto_enabled: bool = None,
        xreal_ip_enabled: bool = None,
    ):
        # Indicates whether the `GA-AP` header is used to retrieve the information about acceleration regions. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is returned only for HTTP and HTTPS listeners.
        self.xforwarded_for_ga_ap_enabled = xforwarded_for_ga_ap_enabled
        # Indicates whether the `GA-ID` header is used to retrieve the ID of the GA instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is returned only for HTTP and HTTPS listeners.
        self.xforwarded_for_ga_id_enabled = xforwarded_for_ga_id_enabled
        # Indicates whether the `GA-X-Forward-Port` header is used to retrieve the listener ports of the GA instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is returned only for HTTP and HTTPS listeners.
        self.xforwarded_for_port_enabled = xforwarded_for_port_enabled
        # Indicates whether the `GA-X-Forward-Proto` header is used to retrieve the listener protocol of the GA instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is returned only for HTTP and HTTPS listeners.
        self.xforwarded_for_proto_enabled = xforwarded_for_proto_enabled
        # Indicates whether the `X-Real-IP` header is used to retrieve client IP addresses. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is returned only for HTTP and HTTPS listeners.
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

class ListListenersResponseBodyListenersServiceManagedInfos(DaraModel):
    def __init__(
        self,
        action: str = None,
        child_type: str = None,
        is_managed: bool = None,
    ):
        # The name of the action on the managed instance. Valid values:
        # 
        # *   **Create**
        # *   **Update**
        # *   **Delete**
        # *   **Associate**
        # *   **UserUnmanaged**
        # *   **CreateChild**
        self.action = action
        # The type of the child resource. Valid values:
        # 
        # *   **Listener**: listener.
        # *   **IpSet**: acceleration region.
        # *   **EndpointGroup**: endpoint group.
        # *   **ForwardingRule**: forwarding rule.
        # *   **Endpoint**: endpoint.
        # *   **EndpointGroupDestination**: protocol mapping of an endpoint group associated with a custom routing listener.
        # *   **EndpointPolicy**: traffic policy of an endpoint associated with a custom routing listener.
        # 
        # >  This parameter takes effect only if the value of **Action** is **CreateChild**.
        self.child_type = child_type
        # Indicates whether the specified actions are managed.
        # 
        # *   **true**: The specified actions are managed, and users cannot perform the specified actions on the managed instance.
        # *   **false**: The specified actions are not managed, and users can perform the specified actions on the managed instance.
        self.is_managed = is_managed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.child_type is not None:
            result['ChildType'] = self.child_type

        if self.is_managed is not None:
            result['IsManaged'] = self.is_managed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ChildType') is not None:
            self.child_type = m.get('ChildType')

        if m.get('IsManaged') is not None:
            self.is_managed = m.get('IsManaged')

        return self

class ListListenersResponseBodyListenersPortRanges(DaraModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        # The first port in the listener port range that is used to receive and forward requests to endpoints.
        self.from_port = from_port
        # The last port in the listener port range that is used to receive and forward requests to endpoints.
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

class ListListenersResponseBodyListenersCertificates(DaraModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
    ):
        # The ID of the SSL certificate.
        self.id = id
        # The type of the SSL certificate.
        # 
        # Only **Server** may be returned, which indicates a server certificate.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListListenersResponseBodyListenersBackendPorts(DaraModel):
    def __init__(
        self,
        from_port: str = None,
        to_port: str = None,
    ):
        # The first port in the range of ports that are used by backend servers.
        self.from_port = from_port
        # The last port in the range of ports that are used by backend servers.
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

