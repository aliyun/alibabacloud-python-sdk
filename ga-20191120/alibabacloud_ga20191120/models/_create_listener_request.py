# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class CreateListenerRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        certificates: List[main_models.CreateListenerRequestCertificates] = None,
        client_affinity: str = None,
        client_token: str = None,
        custom_routing_endpoint_group_configurations: List[main_models.CreateListenerRequestCustomRoutingEndpointGroupConfigurations] = None,
        description: str = None,
        endpoint_group_configurations: List[main_models.CreateListenerRequestEndpointGroupConfigurations] = None,
        http_version: str = None,
        idle_timeout: int = None,
        name: str = None,
        port_ranges: List[main_models.CreateListenerRequestPortRanges] = None,
        protocol: str = None,
        region_id: str = None,
        request_timeout: int = None,
        security_policy_id: str = None,
        type: str = None,
        xforwarded_for_config: main_models.CreateListenerRequestXForwardedForConfig = None,
    ):
        # The ID of the Global Accelerator instance.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # The SSL certificates for an HTTPS listener.
        self.certificates = certificates
        # The client affinity for the listener.
        # 
        # - By default, client affinity is disabled, and requests from the same client may be routed to different endpoints.
        # 
        # - Set to **SOURCE_IP** to enable client affinity. This setting directs all requests from the same client to the same endpoint, regardless of the source port or protocol.
        self.client_affinity = client_affinity
        # A client token that ensures the idempotence of the request.
        # 
        # Generate a unique token on your client for each request. The token must contain only ASCII characters.
        # 
        # > If you omit this parameter, the system uses the request\\"s **RequestId** as the **ClientToken**.
        self.client_token = client_token
        # The configurations of the endpoint groups for a custom routing listener.
        # 
        # You can specify up to five endpoint groups.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **CustomRouting**.
        self.custom_routing_endpoint_group_configurations = custom_routing_endpoint_group_configurations
        # The description of the listener.
        # 
        # The description can be up to 200 characters long and cannot start with `http://` or `https://`.
        self.description = description
        # The configurations of the endpoint groups for a standard listener.
        # 
        # You can specify up to 10 endpoint groups.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **Standard**.
        self.endpoint_group_configurations = endpoint_group_configurations
        # The maximum HTTP version. Valid values:
        # 
        # - **http3**: HTTP/3
        # 
        # - **http2** (default): HTTP/2
        # 
        # - **http1.1**: HTTP/1.1
        # 
        # > This parameter applies only to HTTPS listeners.
        self.http_version = http_version
        # The connection idle timeout, in seconds.
        # 
        # - TCP: 10–900 seconds. Default: 900 seconds.
        # 
        # - UDP: 10–20 seconds. Default: 20 seconds.
        # 
        # - HTTP/HTTPS: 1–60 seconds. Default: 15 seconds.
        self.idle_timeout = idle_timeout
        # The name of the listener.
        # 
        # The name must be 1 to 128 characters long, start with a letter or a Chinese character, and can contain digits, periods (.), underscores (_), and hyphens (-).
        self.name = name
        # The listener port range. The port numbers must be within the range of **1** to **65499**. The maximum number of allowed ports depends on the listener\\"s routing type and protocol. For more information, see [Listener ports](https://help.aliyun.com/document_detail/153216.html).
        # 
        # This parameter is required.
        self.port_ranges = port_ranges
        # The listener\\"s network protocol. Valid values:
        # 
        # - **tcp**: TCP.
        # 
        # - **udp**: UDP.
        # 
        # - **http**: HTTP.
        # 
        # - **https**: HTTPS.
        self.protocol = protocol
        # The region ID of the Global Accelerator instance. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The request timeout for HTTP/HTTPS connections, in seconds.
        # 
        # Valid values: 1–180 seconds. Default: 60 seconds.
        # 
        # > This parameter applies only to HTTP or HTTPS listeners. If the backend server does not respond within the timeout period, Global Accelerator returns an HTTP 504 error to the client.
        self.request_timeout = request_timeout
        # The ID of the security policy. Valid values:
        # 
        # - **tls_cipher_policy_1_0**
        # 
        #   - Supported TLS versions: TLS 1.0, TLS 1.1, and TLS 1.2.
        # 
        #   - Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM-SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA.
        # 
        # - **tls_cipher_policy_1_1**
        # 
        #   - Supported TLS versions: TLS 1.1 and TLS 1.2.
        # 
        #   - Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM-SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA.
        # 
        # - **tls_cipher_policy_1_2**
        # 
        #   - Supported TLS version: TLS 1.2.
        # 
        #   - Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM-SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA.
        # 
        # - **tls_cipher_policy_1_2_strict**
        # 
        #   - Supported TLS version: TLS 1.2.
        # 
        #   - Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, ECDHE-RSA-AES128-SHA, and ECDHE-RSA-AES256-SHA.
        # 
        # - **tls_cipher_policy_1_2_strict_with_1_3**
        # 
        #   - Supported TLS versions: TLS 1.2 and TLS 1.3.
        # 
        #   - Supported cipher suites: TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384, TLS_CHACHA20_POLY1305_SHA256, TLS_AES_128_CCM_SHA256, TLS_AES_128_CCM_8_SHA256, ECDHE-ECDSA-AES128-GCM-SHA256, ECDHE-ECDSA-AES256-GCM-SHA384, ECDHE-ECDSA-AES128-SHA256, ECDHE-ECDSA-AES256-SHA384, ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, ECDHE-ECDSA-AES128-SHA, ECDHE-ECDSA-AES256-SHA, ECDHE-RSA-AES128-SHA, and ECDHE-RSA-AES256-SHA.
        # 
        # > This parameter applies only to HTTPS listeners.
        self.security_policy_id = security_policy_id
        # The routing type of the listener. Valid values:
        # 
        # - **Standard** (default): standard routing.
        # 
        # - **CustomRouting**: custom routing.
        # 
        # > * Custom routing is in invitation-only preview. To use this feature, contact your Alibaba Cloud account manager.
        # >
        # > * A standard Global Accelerator instance supports only one routing type for all of its listeners. The routing type cannot be changed after the listener is created. For more information, see [Listener overview](https://help.aliyun.com/document_detail/153216.html).
        self.type = type
        # Settings for `X-Forwarded-For` related headers.
        self.xforwarded_for_config = xforwarded_for_config

    def validate(self):
        if self.certificates:
            for v1 in self.certificates:
                 if v1:
                    v1.validate()
        if self.custom_routing_endpoint_group_configurations:
            for v1 in self.custom_routing_endpoint_group_configurations:
                 if v1:
                    v1.validate()
        if self.endpoint_group_configurations:
            for v1 in self.endpoint_group_configurations:
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
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        result['Certificates'] = []
        if self.certificates is not None:
            for k1 in self.certificates:
                result['Certificates'].append(k1.to_map() if k1 else None)

        if self.client_affinity is not None:
            result['ClientAffinity'] = self.client_affinity

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['CustomRoutingEndpointGroupConfigurations'] = []
        if self.custom_routing_endpoint_group_configurations is not None:
            for k1 in self.custom_routing_endpoint_group_configurations:
                result['CustomRoutingEndpointGroupConfigurations'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        result['EndpointGroupConfigurations'] = []
        if self.endpoint_group_configurations is not None:
            for k1 in self.endpoint_group_configurations:
                result['EndpointGroupConfigurations'].append(k1.to_map() if k1 else None)

        if self.http_version is not None:
            result['HttpVersion'] = self.http_version

        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout

        if self.name is not None:
            result['Name'] = self.name

        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k1 in self.port_ranges:
                result['PortRanges'].append(k1.to_map() if k1 else None)

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout

        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id

        if self.type is not None:
            result['Type'] = self.type

        if self.xforwarded_for_config is not None:
            result['XForwardedForConfig'] = self.xforwarded_for_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        self.certificates = []
        if m.get('Certificates') is not None:
            for k1 in m.get('Certificates'):
                temp_model = main_models.CreateListenerRequestCertificates()
                self.certificates.append(temp_model.from_map(k1))

        if m.get('ClientAffinity') is not None:
            self.client_affinity = m.get('ClientAffinity')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.custom_routing_endpoint_group_configurations = []
        if m.get('CustomRoutingEndpointGroupConfigurations') is not None:
            for k1 in m.get('CustomRoutingEndpointGroupConfigurations'):
                temp_model = main_models.CreateListenerRequestCustomRoutingEndpointGroupConfigurations()
                self.custom_routing_endpoint_group_configurations.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.endpoint_group_configurations = []
        if m.get('EndpointGroupConfigurations') is not None:
            for k1 in m.get('EndpointGroupConfigurations'):
                temp_model = main_models.CreateListenerRequestEndpointGroupConfigurations()
                self.endpoint_group_configurations.append(temp_model.from_map(k1))

        if m.get('HttpVersion') is not None:
            self.http_version = m.get('HttpVersion')

        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k1 in m.get('PortRanges'):
                temp_model = main_models.CreateListenerRequestPortRanges()
                self.port_ranges.append(temp_model.from_map(k1))

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')

        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('XForwardedForConfig') is not None:
            temp_model = main_models.CreateListenerRequestXForwardedForConfig()
            self.xforwarded_for_config = temp_model.from_map(m.get('XForwardedForConfig'))

        return self

class CreateListenerRequestXForwardedForConfig(DaraModel):
    def __init__(
        self,
        xforwarded_for_ga_ap_enabled: bool = None,
        xforwarded_for_ga_id_enabled: bool = None,
        xforwarded_for_port_enabled: bool = None,
        xforwarded_for_proto_enabled: bool = None,
        xreal_ip_enabled: bool = None,
    ):
        # Specifies whether to use the `GA-AP` header to pass information about the acceleration region to the backend server. Valid values:
        # 
        # - **true**
        # 
        # - **false** (Default)
        # 
        # > This parameter applies only to HTTP and HTTPS listeners.
        self.xforwarded_for_ga_ap_enabled = xforwarded_for_ga_ap_enabled
        # Specifies whether to use the `GA-ID` header to pass the Global Accelerator instance ID to the backend server. Valid values:
        # 
        # - **true**
        # 
        # - **false** (Default)
        # 
        # > This parameter applies only to HTTP and HTTPS listeners.
        self.xforwarded_for_ga_id_enabled = xforwarded_for_ga_id_enabled
        # Specifies whether to use the `GA-X-Forward-Port` header to pass the listener port of the Global Accelerator instance to the backend server. Valid values:
        # 
        # - **true**
        # 
        # - **false** (Default)
        # 
        # > This parameter applies only to HTTP and HTTPS listeners.
        self.xforwarded_for_port_enabled = xforwarded_for_port_enabled
        # Specifies whether to use the `GA-X-Forward-Proto` header to pass the listener protocol of the Global Accelerator instance to the backend server. Valid values:
        # 
        # - **true**
        # 
        # - **false** (Default)
        # 
        # > This parameter applies only to HTTP and HTTPS listeners.
        self.xforwarded_for_proto_enabled = xforwarded_for_proto_enabled
        # Specifies whether to use the `X-Real-IP` header to pass the client\\"s real IP address to the backend server. Valid values:
        # 
        # - **true**
        # 
        # - **false** (Default)
        # 
        # > This parameter applies only to HTTP and HTTPS listeners.
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

class CreateListenerRequestPortRanges(DaraModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        # The first port in the listener range used to receive and forward requests to endpoints.
        # 
        # The port number must be in the range of **1** to **65499**, and the value of **FromPort** must be less than or equal to the value of **ToPort**.
        # 
        # > For HTTP or HTTPS listeners, you can specify only one listener port. In this case, the value of **FromPort** must be the same as the value of **ToPort**.
        # 
        # This parameter is required.
        self.from_port = from_port
        # The last port in the listener range used to receive and forward requests to endpoints.
        # 
        # The port number must be in the range of **1** to **65499**, and the value of **FromPort** must be less than or equal to the value of **ToPort**.
        # 
        # > For HTTP or HTTPS listeners, you can specify only one listener port. In this case, the value of **FromPort** must be the same as the value of **ToPort**.
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

class CreateListenerRequestEndpointGroupConfigurations(DaraModel):
    def __init__(
        self,
        endpoint_configurations: List[main_models.CreateListenerRequestEndpointGroupConfigurationsEndpointConfigurations] = None,
        endpoint_group_description: str = None,
        endpoint_group_name: str = None,
        endpoint_group_region: str = None,
        endpoint_group_type: str = None,
        endpoint_ip_version: str = None,
        endpoint_protocol_version: str = None,
        endpoint_request_protocol: str = None,
        health_check_enabled: bool = None,
        health_check_host: str = None,
        health_check_interval_seconds: int = None,
        health_check_path: str = None,
        health_check_port: int = None,
        health_check_protocol: str = None,
        port_overrides: List[main_models.CreateListenerRequestEndpointGroupConfigurationsPortOverrides] = None,
        threshold_count: int = None,
        traffic_percentage: int = None,
    ):
        # The endpoint configurations.
        self.endpoint_configurations = endpoint_configurations
        # The description of the endpoint group.
        # 
        # The description can be up to 200 characters long and cannot contain `http://` or `https://`.
        # 
        # You can enter up to 10 endpoint group descriptions.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **Standard**.
        self.endpoint_group_description = endpoint_group_description
        # The name of the endpoint group.
        # 
        # The name must be 1 to 128 characters long, start with a letter or a Chinese character, and can contain digits, periods (.), underscores (_), and hyphens (-).
        # 
        # You can enter up to 10 endpoint group names.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **Standard**.
        self.endpoint_group_name = endpoint_group_name
        # The ID of the region where the endpoint group is created.
        # 
        # You can enter up to 10 endpoint group region IDs.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **Standard**.
        self.endpoint_group_region = endpoint_group_region
        # The type of the endpoint group. Valid values:
        # 
        # - **default** (default): a default endpoint group.
        # 
        # - **virtual**: a virtual endpoint group.
        # 
        # You can enter up to 10 endpoint group types.
        # 
        # > - This parameter applies only when the listener\\"s routing type (**Type**) is **Standard**.
        # >
        # > - You can create virtual endpoint groups only for HTTP or HTTPS listeners.
        self.endpoint_group_type = endpoint_group_type
        # The IP version used by the backend service. Valid values:
        # 
        # - **IPv4** (default): GA uses only IPv4 addresses to communicate with backend services.
        # 
        # - **IPv6**: GA uses only IPv6 addresses to communicate with backend services.
        # 
        # - **ProtocolAffinity**: GA uses the same IP version as the client request to communicate with backend services.
        self.endpoint_ip_version = endpoint_ip_version
        # The protocol version of the backend service. Valid values:
        # 
        # - **HTTP1.1** (default): HTTP/1.1
        # 
        # - **HTTP2**: HTTP/2
        # 
        # > This parameter is available only when EndpointRequestProtocol is set to HTTPS.
        self.endpoint_protocol_version = endpoint_protocol_version
        # The protocol used by the backend service. Valid values:
        # 
        # - **HTTP** (default)
        # 
        # - **HTTPS**
        # 
        # You can enter up to 10 backend service protocols.
        # 
        # > - This parameter applies only when the listener\\"s routing type (**Type**) is **Standard**.
        # >
        # > - You can configure this parameter only for endpoint groups of HTTP or HTTPS listeners.
        # >
        # > - For an HTTP listener, the backend service protocol must be **HTTP**.
        self.endpoint_request_protocol = endpoint_request_protocol
        # Specifies whether to enable health checks for the endpoint group. Valid values:
        # 
        # - **true**: Enables health checks.
        # 
        # - **false** (Default): Disables health checks.
        # 
        # You can enable health checks for up to 10 endpoint groups.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **Standard**.
        self.health_check_enabled = health_check_enabled
        # The domain name that is used for health checks.
        self.health_check_host = health_check_host
        # The health check interval, in seconds.
        # 
        # You can enter up to 10 health check intervals.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **Standard**.
        self.health_check_interval_seconds = health_check_interval_seconds
        # The path to which health check requests are sent.
        # 
        # You can enter up to 10 health check paths.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **Standard**.
        self.health_check_path = health_check_path
        # The port that is used for health checks. Valid values: **1** to **65535**.
        # 
        # You can enter a maximum of 10 ports for health checks.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **Standard**.
        self.health_check_port = health_check_port
        # The protocol over which health check requests are sent. Valid values:
        # 
        # - **tcp** or **TCP**: TCP
        # 
        # - **http** or **HTTP**: HTTP
        # 
        # - **https** or **HTTPS**: HTTPS
        # 
        # You can enter up to 10 health check protocols.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **Standard**.
        self.health_check_protocol = health_check_protocol
        # The port mapping. You can specify up to five port mappings.
        self.port_overrides = port_overrides
        # The number of consecutive successful health checks required to mark an endpoint as healthy, or consecutive failed health checks to mark an endpoint as unhealthy.
        # Valid values: **2** to **10**. Default value: **3**.
        # 
        # You can enter up to 10 values for the number of consecutive health checks required to trigger a health status change.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **Standard**.
        self.threshold_count = threshold_count
        # The traffic distribution ratio. If a standard listener is associated with multiple endpoint groups, this parameter specifies the percentage of traffic that is distributed to each endpoint group.
        # 
        # Valid values: **1** to **100**. Default value: **100**.
        # 
        # You can enter traffic distribution values for up to 10 endpoint groups.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **Standard**.
        self.traffic_percentage = traffic_percentage

    def validate(self):
        if self.endpoint_configurations:
            for v1 in self.endpoint_configurations:
                 if v1:
                    v1.validate()
        if self.port_overrides:
            for v1 in self.port_overrides:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k1 in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k1.to_map() if k1 else None)

        if self.endpoint_group_description is not None:
            result['EndpointGroupDescription'] = self.endpoint_group_description

        if self.endpoint_group_name is not None:
            result['EndpointGroupName'] = self.endpoint_group_name

        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region

        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type

        if self.endpoint_ip_version is not None:
            result['EndpointIpVersion'] = self.endpoint_ip_version

        if self.endpoint_protocol_version is not None:
            result['EndpointProtocolVersion'] = self.endpoint_protocol_version

        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol

        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled

        if self.health_check_host is not None:
            result['HealthCheckHost'] = self.health_check_host

        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds

        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path

        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port

        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol

        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k1 in self.port_overrides:
                result['PortOverrides'].append(k1.to_map() if k1 else None)

        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count

        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k1 in m.get('EndpointConfigurations'):
                temp_model = main_models.CreateListenerRequestEndpointGroupConfigurationsEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k1))

        if m.get('EndpointGroupDescription') is not None:
            self.endpoint_group_description = m.get('EndpointGroupDescription')

        if m.get('EndpointGroupName') is not None:
            self.endpoint_group_name = m.get('EndpointGroupName')

        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')

        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')

        if m.get('EndpointIpVersion') is not None:
            self.endpoint_ip_version = m.get('EndpointIpVersion')

        if m.get('EndpointProtocolVersion') is not None:
            self.endpoint_protocol_version = m.get('EndpointProtocolVersion')

        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')

        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')

        if m.get('HealthCheckHost') is not None:
            self.health_check_host = m.get('HealthCheckHost')

        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')

        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')

        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')

        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')

        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k1 in m.get('PortOverrides'):
                temp_model = main_models.CreateListenerRequestEndpointGroupConfigurationsPortOverrides()
                self.port_overrides.append(temp_model.from_map(k1))

        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')

        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')

        return self

class CreateListenerRequestEndpointGroupConfigurationsPortOverrides(DaraModel):
    def __init__(
        self,
        endpoint_port: int = None,
        listener_port: int = None,
    ):
        # The endpoint port that is specified in the port mapping.
        # 
        # You can enter a maximum of 5 endpoint ports for port mapping.
        # 
        # > - This parameter applies only when the listener\\"s routing type (**Type**) is **Standard**.
        # >
        # > - For TCP listeners, you cannot configure a port mapping for a virtual endpoint group. If a virtual endpoint group already exists for the listener, you cannot configure a port mapping for the default endpoint group. If a port mapping is configured for the default endpoint group, you cannot add a virtual endpoint group to the listener.
        # >
        # > - After you configure a port mapping, you cannot modify the listener protocol, except for switching between HTTP and HTTPS.
        # >
        # > - When you modify the listener port range, make sure that the new port range includes all listener ports that are specified in the port mapping. For example, if the listener port range is 80-82 and the listener ports are mapped to the endpoint ports 100-102, you cannot change the listener port range to 80-81.
        self.endpoint_port = endpoint_port
        # The listener port that is specified in the port mapping.
        # 
        # You can enter up to 5 listener ports for port mappings.
        # 
        # > - This parameter applies only when the listener\\"s routing type (**Type**) is **Standard**.
        # >
        # > - For TCP listeners, you cannot configure a port mapping for a virtual endpoint group. If a virtual endpoint group already exists for the listener, you cannot configure a port mapping for the default endpoint group. If a port mapping is configured for the default endpoint group, you cannot add a virtual endpoint group to the listener.
        # >
        # > - After you configure a port mapping, you cannot modify the listener protocol, except for switching between HTTP and HTTPS.
        # >
        # > - When you modify the listener port range, make sure that the new port range includes all listener ports that are specified in the port mapping. For example, if the listener port range is 80-82 and the listener ports are mapped to the endpoint ports 100-102, you cannot change the listener port range to 80-81.
        self.listener_port = listener_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        return self

class CreateListenerRequestEndpointGroupConfigurationsEndpointConfigurations(DaraModel):
    def __init__(
        self,
        api_keys: List[str] = None,
        enable_client_ippreservation: bool = None,
        enable_proxy_protocol: bool = None,
        endpoint: str = None,
        provider: str = None,
        sub_address: str = None,
        type: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
        weight: int = None,
    ):
        self.api_keys = api_keys
        # Specifies whether to preserve client source IP addresses. Valid values:
        # 
        # - **true**: enables the feature.
        # 
        # - **false** (default): disables the feature.
        # 
        # > * This feature is disabled by default for endpoint groups of TCP or UDP listeners. You can enable it as needed.
        # >
        # > * This feature is enabled by default for endpoint groups of HTTP or HTTPS listeners. Client source IP addresses are retrieved from the `X-Forwarded-For` header. You cannot disable this feature.
        # >
        # > * You cannot set both `EnableClientIPPreservation` and `EnableProxyProtocol` to `true`.
        # >
        # > * For more information, see [Preserve client source IP addresses](https://help.aliyun.com/document_detail/158080.html).
        self.enable_client_ippreservation = enable_client_ippreservation
        # Specifies whether to use the proxy protocol to preserve client source IP addresses. Valid values:
        # 
        # - **true**: enables the feature.
        # 
        # - **false** (default): disables the feature.
        # 
        # > * You can configure this parameter only for endpoint groups of TCP listeners.
        # >
        # > * You cannot set both `EnableClientIPPreservation` and `EnableProxyProtocol` to `true`.
        # >
        # > * For more information, see [Preserve client source IP addresses](https://help.aliyun.com/document_detail/158080.html).
        self.enable_proxy_protocol = enable_proxy_protocol
        # The IP address or domain name of the endpoint.
        # 
        # In an endpoint group of an intelligent routing listener, you can enter up to 100 IP addresses or domain names of endpoints.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **Standard**.
        self.endpoint = endpoint
        self.provider = provider
        # The private IP address of the ENI.
        # 
        # > If the endpoint type is **ENI**, you can specify this parameter. If you do not specify this parameter, the primary private IP address of the ENI is used.
        self.sub_address = sub_address
        # The type of the endpoint. Valid values:
        # 
        # - **Domain**: a custom domain name.
        # 
        # - **Ip**: a custom IP address.
        # 
        # - **PublicIp**: a public IP address of an Alibaba Cloud service.
        # 
        # - **ECS**: an Elastic Compute Service (ECS) instance.
        # 
        # - **SLB**: a Server Load Balancer (SLB) instance.
        # 
        # - **ALB**: an Application Load Balancer (ALB) instance.
        # 
        # - **OSS**: an Object Storage Service (OSS) bucket.
        # 
        # - **ENI**: an elastic network interface (ENI).
        # 
        # - **NLB**: a Network Load Balancer (NLB) instance.
        # 
        # - **IpTarget**: a custom private IP address.
        # 
        # You can specify up to 100 endpoints in an endpoint group.
        # 
        # > - This parameter applies only when the listener\\"s routing type (**Type**) is **Standard**.
        # >
        # > - When you add endpoints, Global Accelerator may create service-linked roles to access your resources. The role created depends on the endpoint type:
        # >
        # > -
        # >
        # > -
        # >
        # > -
        # >
        # > > For more information, see [Service-linked roles](https://help.aliyun.com/document_detail/178360.html).
        self.type = type
        # The list of vSwitches in the VPC. You can specify up to two vSwitch IDs.
        self.v_switch_ids = v_switch_ids
        # The ID of the Virtual Private Cloud (VPC).
        # 
        # In an endpoint group of an intelligent routing listener, you can enter a maximum of 1 VPC ID.
        # 
        # > This parameter is required only for **IpTarget** endpoints.
        self.vpc_id = vpc_id
        # The weight of the endpoint.
        # 
        # Valid values: **0** to **255**.
        # 
        # In an endpoint group for an intelligent routing type listener, you can enter weights for up to 100 endpoints.
        # 
        # > - This parameter applies only when the listener\\"s routing type (**Type**) is **Standard**.
        # >
        # > - If an endpoint\\"s weight is set to 0, Global Accelerator stops sending traffic to it. Use this setting with caution.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_keys is not None:
            result['ApiKeys'] = self.api_keys

        if self.enable_client_ippreservation is not None:
            result['EnableClientIPPreservation'] = self.enable_client_ippreservation

        if self.enable_proxy_protocol is not None:
            result['EnableProxyProtocol'] = self.enable_proxy_protocol

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.sub_address is not None:
            result['SubAddress'] = self.sub_address

        if self.type is not None:
            result['Type'] = self.type

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKeys') is not None:
            self.api_keys = m.get('ApiKeys')

        if m.get('EnableClientIPPreservation') is not None:
            self.enable_client_ippreservation = m.get('EnableClientIPPreservation')

        if m.get('EnableProxyProtocol') is not None:
            self.enable_proxy_protocol = m.get('EnableProxyProtocol')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('SubAddress') is not None:
            self.sub_address = m.get('SubAddress')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class CreateListenerRequestCustomRoutingEndpointGroupConfigurations(DaraModel):
    def __init__(
        self,
        description: str = None,
        destination_configurations: List[main_models.CreateListenerRequestCustomRoutingEndpointGroupConfigurationsDestinationConfigurations] = None,
        endpoint_configurations: List[main_models.CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurations] = None,
        endpoint_group_region: str = None,
        name: str = None,
    ):
        # The description of the endpoint group.
        # 
        # The description can be up to 200 characters long and cannot contain `http://` or `https://`.
        # 
        # You can enter up to 5 endpoint group descriptions.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **CustomRouting**.
        self.description = description
        # The mapping configurations for the endpoint group.
        # 
        # You must specify the port ranges and protocols for the backend service. The settings are mapped to the associated listener port ranges.
        # 
        # You can specify up to 20 mapping configurations for each endpoint group.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **CustomRouting**.
        self.destination_configurations = destination_configurations
        # The endpoint configurations.
        # 
        # You can specify up to 10 endpoints for each endpoint group.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **CustomRouting**.
        self.endpoint_configurations = endpoint_configurations
        # The ID of the region where the endpoint group is created.
        # 
        # You can enter up to 5 endpoint group region IDs.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **CustomRouting**.
        self.endpoint_group_region = endpoint_group_region
        # The name of the endpoint group.
        # 
        # The name must be 1 to 128 characters long, start with a letter or a Chinese character, and can contain digits, periods (.), underscores (_), and hyphens (-).
        # 
        # You can enter up to 5 endpoint group names.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **CustomRouting**.
        self.name = name

    def validate(self):
        if self.destination_configurations:
            for v1 in self.destination_configurations:
                 if v1:
                    v1.validate()
        if self.endpoint_configurations:
            for v1 in self.endpoint_configurations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        result['DestinationConfigurations'] = []
        if self.destination_configurations is not None:
            for k1 in self.destination_configurations:
                result['DestinationConfigurations'].append(k1.to_map() if k1 else None)

        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k1 in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k1.to_map() if k1 else None)

        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.destination_configurations = []
        if m.get('DestinationConfigurations') is not None:
            for k1 in m.get('DestinationConfigurations'):
                temp_model = main_models.CreateListenerRequestCustomRoutingEndpointGroupConfigurationsDestinationConfigurations()
                self.destination_configurations.append(temp_model.from_map(k1))

        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k1 in m.get('EndpointConfigurations'):
                temp_model = main_models.CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k1))

        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurations(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        policy_configurations: List[main_models.CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurations] = None,
        traffic_to_endpoint_policy: str = None,
        type: str = None,
    ):
        # The vSwitch of the custom routing listener.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **CustomRouting**.
        self.endpoint = endpoint
        # The destination configurations for a custom routing listener.
        # 
        # You can specify up to 20 destinations for each endpoint.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **CustomRouting**.
        self.policy_configurations = policy_configurations
        # The traffic policy for the backend service of a custom routing listener. Valid values:
        # 
        # - **DenyAll** (default): Denies all traffic to the specified backend service.
        # 
        # - **AllowAll**: Allows all traffic to the specified backend service.
        # 
        # - **AllowCustom**: Allows traffic to specific destinations.
        #   You must specify the IP addresses and port ranges of the allowed destinations. If no port range is specified, all ports of the destination are allowed.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **CustomRouting**.
        self.traffic_to_endpoint_policy = traffic_to_endpoint_policy
        # The type of the backend service for a custom routing listener. Valid value:
        # 
        # **PrivateSubNet** (default): a private CIDR block.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **CustomRouting**.
        self.type = type

    def validate(self):
        if self.policy_configurations:
            for v1 in self.policy_configurations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        result['PolicyConfigurations'] = []
        if self.policy_configurations is not None:
            for k1 in self.policy_configurations:
                result['PolicyConfigurations'].append(k1.to_map() if k1 else None)

        if self.traffic_to_endpoint_policy is not None:
            result['TrafficToEndpointPolicy'] = self.traffic_to_endpoint_policy

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        self.policy_configurations = []
        if m.get('PolicyConfigurations') is not None:
            for k1 in m.get('PolicyConfigurations'):
                temp_model = main_models.CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurations()
                self.policy_configurations.append(temp_model.from_map(k1))

        if m.get('TrafficToEndpointPolicy') is not None:
            self.traffic_to_endpoint_policy = m.get('TrafficToEndpointPolicy')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurations(DaraModel):
    def __init__(
        self,
        address: str = None,
        port_ranges: List[main_models.CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurationsPortRanges] = None,
    ):
        # The IP address of the destination that is allowed to receive traffic.
        # 
        # This parameter is required only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify up to 20 destination IP addresses for each endpoint.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **CustomRouting**.
        self.address = address
        # The port range of the destination that is allowed to receive traffic. The port range must be within the port range of the backend service.
        # 
        # If you leave this parameter empty, all ports of the destination are allowed.
        # 
        # This parameter is required only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify up to 20 port ranges for each endpoint, and up to 5 port ranges for each destination.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **CustomRouting**.
        self.port_ranges = port_ranges

    def validate(self):
        if self.port_ranges:
            for v1 in self.port_ranges:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k1 in self.port_ranges:
                result['PortRanges'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k1 in m.get('PortRanges'):
                temp_model = main_models.CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k1))

        return self

class CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurationsPortRanges(DaraModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        # The first port of the destination that is allowed to receive traffic. The port must be within the port range of the backend service.
        # 
        # This parameter is required only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify up to 20 port ranges for each endpoint, and up to 5 first ports for each destination.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **CustomRouting**.
        self.from_port = from_port
        # The last port of the destination that is allowed to receive traffic. The port must be within the port range of the backend service.
        # 
        # This parameter is required only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify up to 20 port ranges for each endpoint, and up to 5 last ports for each destination.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **CustomRouting**.
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

class CreateListenerRequestCustomRoutingEndpointGroupConfigurationsDestinationConfigurations(DaraModel):
    def __init__(
        self,
        from_port: int = None,
        protocols: List[str] = None,
        to_port: int = None,
    ):
        # The first port of the backend service.
        # 
        # The valid port range is **1** to **65499**. The value of **FromPort** must be less than or equal to the value of **ToPort**.
        # 
        # In each endpoint group for a custom routing type listener, you can enter up to 20 backend service starting ports.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **CustomRouting**.
        self.from_port = from_port
        # The protocols of the backend service.
        # 
        # You can specify up to four backend service protocols for each mapping configuration.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **CustomRouting**.
        self.protocols = protocols
        # The last port of the backend service.
        # 
        # The valid port range is **1** to **65499**. The value of **FromPort** must be less than or equal to the value of **ToPort**.
        # 
        # In each endpoint group of a listener of the custom routing type, you can enter a maximum of 20 backend service ports.
        # 
        # > This parameter applies only when the listener\\"s routing type (**Type**) is **CustomRouting**.
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

        if self.protocols is not None:
            result['Protocols'] = self.protocols

        if self.to_port is not None:
            result['ToPort'] = self.to_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')

        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')

        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')

        return self

class CreateListenerRequestCertificates(DaraModel):
    def __init__(
        self,
        id: str = None,
    ):
        # The ID of the SSL certificate.
        # 
        # > This parameter is required only for HTTPS listeners.
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

