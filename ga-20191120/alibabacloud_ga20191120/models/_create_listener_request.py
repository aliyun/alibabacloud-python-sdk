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
        # The ID of the GA instance.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # The SSL certificates.
        self.certificates = certificates
        # Specifies whether to enable client affinity for the listener.
        # 
        # *   If this parameter is left empty, client affinity is disabled. After client affinity is disabled, requests from a specific client IP address may be forwarded to different endpoints.
        # *   To enable client affinity, set this parameter to **SOURCE_IP**. In this case, when a client accesses stateful applications, requests from the same client are forwarded to the same endpoint regardless of the source port or protocol.
        self.client_affinity = client_affinity
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** is different for each API request.
        self.client_token = client_token
        # The endpoint group that is associated with the custom routing listener.
        # 
        # The endpoint groups that are associated with the custom routing listener.
        # 
        # >  You can configure endpoint groups and endpoints for a custom routing listener only if **Type** is set to **CustomRouting**.
        self.custom_routing_endpoint_group_configurations = custom_routing_endpoint_group_configurations
        # The description of the listener.
        # 
        # The description can be up to 200 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The endpoint groups that are associated with the intelligent routing listener.
        # 
        # You can configure up to 10 endpoint groups for an intelligent routing listener.
        # 
        # >  You can configure endpoint groups and endpoints only if you set **Type** to **Standard**.
        self.endpoint_group_configurations = endpoint_group_configurations
        # The maximum version of the HTTP protocol. Valid values:
        # 
        # *   **http3**
        # *   **http2** (default)
        # *   **http1.1**
        # 
        # >  Only HTTPS listeners support this parameter.
        self.http_version = http_version
        # The timeout period of idle connections. Unit: seconds.
        # 
        # *   TCP: 10-900. Default value: 900. Unit: seconds.
        # *   UDP: 10-20. Default value: 20. Unit: seconds.
        # *   HTTP/HTTPS: 1-60. Default value: 15. Unit: seconds.
        self.idle_timeout = idle_timeout
        # The name of the listener.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        self.name = name
        # The listener ports. Valid values: **1** to **65499**. The maximum number of ports that can be configured depends on the routing type and protocol of the listener. For more information, see [Listener overview](https://help.aliyun.com/document_detail/153216.html).
        # 
        # This parameter is required.
        self.port_ranges = port_ranges
        # The network transmission protocol that you want to use for the listener. Valid values:
        # 
        # *   **tcp**: TCP
        # *   **udp**: UDP
        # *   **http**: HTTP
        # *   **https**: HTTPS
        self.protocol = protocol
        # The ID of the region where the GA instance is deployed. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The timeout period for HTTP or HTTPS requests. Unit: seconds.
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
        #     *   Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM-SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA.
        # 
        # *   **tls_cipher_policy_1_1**
        # 
        #     *   Supported TLS versions: TLS 1.1 and TLS 1.2
        #     *   Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM-SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA.
        # 
        # *   **tls_cipher_policy_1_2**
        # 
        #     *   Supported TLS version: TLS 1.2
        #     *   Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM-SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA.
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
        # The routing type of the listener. Valid values:
        # 
        # *   **Standard** (default): intelligent routing
        # *   **CustomRouting**: custom routing
        # 
        # > *   Custom routing listeners are in invitational preview. To use custom routing listeners, contact your account manager.
        # > *   You can create only listeners of the same routing type for a standard GA instance. You cannot change the routing types of listeners. For more information, see [Listener overview](https://help.aliyun.com/document_detail/153216.html).
        self.type = type
        # The `XForward` headers.
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
        # Specifies whether to use the `GA-AP` header to retrieve the information about acceleration regions. Valid values:
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

class CreateListenerRequestPortRanges(DaraModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        # The first port of the listener port range that you want to use to receive and forward requests to endpoints.
        # 
        # Valid values: **1** to **65499**. The value of **FromPort** must be smaller than or equal to the value of **ToPort**.
        # 
        # The maximum number of ports that can be configured varies based on the routing type and protocol of the listener. For more information, see [Listener overview](https://help.aliyun.com/document_detail/153216.html).
        # 
        # > You can configure only one listener port for an HTTP or HTTPS listener. In this case, the first port is the same as the last port.
        # 
        # This parameter is required.
        self.from_port = from_port
        # The last port of the listener port range that you want to use to receive and forward requests to endpoints.
        # 
        # Valid values: **1** to **65499**. The value of **FromPort** must be smaller than or equal to the value of **ToPort**.
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
        # The endpoints that are associated with the intelligent routing listener.
        self.endpoint_configurations = endpoint_configurations
        # The description of the endpoint group that is associated with the intelligent routing listener.
        # 
        # The description can be up to 200 characters in length and cannot contain `http://` or `https://`.
        # 
        # You can enter the descriptions of up to 10 endpoint groups.
        # 
        # >  You can configure endpoint groups and endpoints only if you set **Type** to **Standard**.
        self.endpoint_group_description = endpoint_group_description
        # The name of the endpoint group that is associated with the intelligent routing listener.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        # 
        # You can enter the names of up to 10 endpoint groups.
        # 
        # >  You can configure endpoint groups and endpoints only if you set **Type** to **Standard**.
        self.endpoint_group_name = endpoint_group_name
        # The region ID of the endpoint group that is associated with the intelligent routing listener.
        # 
        # You can enter the IDs of up to 10 regions.
        # 
        # >  You can configure endpoint groups and endpoints only if you set **Type** to **Standard**.
        self.endpoint_group_region = endpoint_group_region
        # The type of the endpoint group associated with the intelligent routing listener. Valid values:
        # 
        # *   **default** (default): a default endpoint group.
        # *   **virtual**: a virtual endpoint group.
        # 
        # You can specify up to 10 endpoint group types.
        # 
        # > *   You can configure endpoint groups and endpoints for an intelligent routing listener only if you set **Type** to **Standard**.
        # >*   Only HTTP and HTTPS intelligent routing listeners support virtual endpoint groups.
        self.endpoint_group_type = endpoint_group_type
        self.endpoint_ip_version = endpoint_ip_version
        # The backend service protocol version of the endpoint that is associated with the intelligent routing listener. Valid values:
        # 
        # *   **HTTP1.1** (default)
        # *   **HTTP2**
        # 
        # >  You can specify this parameter only if EndpointRequestProtocol is set to HTTPS.
        self.endpoint_protocol_version = endpoint_protocol_version
        # The backend service protocol of the endpoint that is associated with the intelligent routing listener. Valid values:
        # 
        # *   **HTTP** (default)
        # *   **HTTPS**
        # 
        # You can specify up to 10 backend service protocols.
        # 
        # > *   You can configure endpoint groups and endpoints for an intelligent routing listener only if you set **Type** to **Standard**.
        # >*   You can specify this parameter only for HTTP and HTTPS intelligent routing listeners.
        # >* For an HTTP listener, the backend service protocol must be **HTTP**.
        self.endpoint_request_protocol = endpoint_request_protocol
        # Specifies whether to enable health checks for the endpoint group. Valid values:
        # 
        # *   **true**: enables the health check feature.
        # *   **false** (default): disables the health check feature.
        # 
        # You can enable the health check feature for up to 10 endpoint groups.
        # 
        # >  You can configure endpoint groups and endpoints only if you set **Type** to **Standard**.
        self.health_check_enabled = health_check_enabled
        self.health_check_host = health_check_host
        # The interval at which health checks are performed. Unit: seconds.
        # 
        # You can specify up to 10 health check intervals.
        # 
        # >  You can configure endpoint groups and endpoints only if you set **Type** to **Standard**.
        self.health_check_interval_seconds = health_check_interval_seconds
        # The health check path.
        # 
        # You can specify up to 10 health check paths.
        # 
        # >  You can configure endpoint groups and endpoints only if you set **Type** to **Standard**.
        self.health_check_path = health_check_path
        # The port that you want to use for health checks. Valid values: **1** to **65535**.
        # 
        # You can specify up to 10 ports for health checks.
        # 
        # >  You can configure endpoint groups and endpoints only if you set **Type** to **Standard**.
        self.health_check_port = health_check_port
        # The protocol over which health check requests are sent. Valid values:
        # 
        # *   **tcp** or **TCP**
        # *   **http** or **HTTP**
        # *   **https** or **HTTPS**
        # 
        # You can specify up to 10 health check protocols.
        # 
        # >  You can configure endpoint groups and endpoints only if you set **Type** to **Standard**.
        self.health_check_protocol = health_check_protocol
        # The port mappings.
        self.port_overrides = port_overrides
        # The number of failed consecutive health checks that must occur before a healthy endpoint group is considered unhealthy or the number of successful consecutive health checks that must occur before an unhealthy endpoint group is considered healthy. Valid values: **2** to **10**. Default value: **3**.
        # 
        # You can specify up to 10 values (the number of consecutive health check successes or consecutive health check failures).
        # 
        # >  You can configure endpoint groups and endpoints only if you set **Type** to **Standard**.
        self.threshold_count = threshold_count
        # The traffic distribution ratio. If an intelligent routing listener is associated with multiple endpoint groups, you can configure this parameter to specify the ratio of traffic distributed to each endpoint group.
        # 
        # Valid values: **1** to **100**. Default value: **100**.
        # 
        # You can specify traffic distribution ratios for up to 10 endpoint groups.
        # 
        # >  You can configure endpoint groups and endpoints only if you set **Type** to **Standard**.
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
        # The endpoint port that is mapped to the listener port.
        # 
        # You can specify endpoint ports in up to five port mappings.
        # 
        # > *   You can configure endpoint groups and endpoints for an intelligent routing listener only if you set **Type** to **Standard**.
        # >*   You cannot configure port mappings for virtual endpoint groups of TCP listeners. If a virtual endpoint group already exists on the listener, you cannot configure port mappings for the default endpoint group. If port mappings are configured for the default endpoint group, you cannot add a virtual endpoint group.
        # >*   If you configure port mappings for a listener, you cannot modify the listener protocol. You can only switch between HTTP and HTTPS.
        # >*   Listener port: When you modify the listener port range, make sure that the port range includes the ports configured in port mappings. For example, if you set the listener port range to 80 to 82 and map the listener ports to endpoint ports 100 to 102, you cannot change the listener port range to 80 to 81.
        self.endpoint_port = endpoint_port
        # The listener port that is mapped to the endpoint port.
        # 
        # You can specify listener ports in up to five port mappings.
        # 
        # > *   You can configure endpoint groups and endpoints for an intelligent routing listener only if you set **Type** to **Standard**.
        # >*   You cannot configure port mappings for virtual endpoint groups of TCP listeners. If a virtual endpoint group already exists on the listener, you cannot configure port mappings for the default endpoint group. If port mappings are configured for the default endpoint group, you cannot add a virtual endpoint group.
        # >*   If you configure port mappings for a listener, you cannot modify the listener protocol. You can only switch between HTTP and HTTPS.
        # >*   Listener port: When you modify the listener port range, make sure that the port range includes the ports configured in port mappings. For example, if you set the listener port range to 80 to 82 and map the listener ports to endpoint ports 100 to 102, you cannot change the listener port range to 80 to 81.
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
        enable_client_ippreservation: bool = None,
        enable_proxy_protocol: bool = None,
        endpoint: str = None,
        sub_address: str = None,
        type: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
        weight: int = None,
    ):
        # Specifies whether to automatically preserve client IP addresses. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        # 
        # > *   By default, client IP address preservation is disabled for an endpoint group that is associated with a UDP or TCP listener. You can configure this parameter based on your business requirements.
        # >*   By default, client IP address preservation is enabled for an endpoint group that is associated with a HTTP or HTTPS listener. Client IP addresses are obtained by using the X-Forwarded-For header. You cannot disable the feature.
        # >*   EnableClientIPPreservation and EnableProxyProtocol cannot be set to true at the same time.
        # >>For more information, see [Preserve client IP addresses](https://help.aliyun.com/document_detail/158080.html).
        self.enable_client_ippreservation = enable_client_ippreservation
        # Specifies whether to use the proxy protocol to preserve client IP addresses. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        # 
        # >*   This parameter is supported only by endpoint groups associated with TCP listeners.
        # >*   EnableClientIPPreservation and EnableProxyProtocol cannot be set to true at the same time.
        # >>For more information, see [Preserve client IP addresses](https://help.aliyun.com/document_detail/158080.html).
        self.enable_proxy_protocol = enable_proxy_protocol
        # The IP address or domain name of the endpoint that is associated with the intelligent routing listener.
        # 
        # You can enter the IP addresses or domain names of up to 100 endpoints in an endpoint group that is associated with the intelligent routing listener.
        # 
        # >  If you set **Type** to **Standard**, you can configure endpoint groups and endpoints, and this parameter is required.
        self.endpoint = endpoint
        # The private IP address of the ENI.
        # 
        # >  This parameter is available only when you set the endpoint type to **ENI**. If you leave this parameter empty, the primary private IP address of the ENI is used.
        self.sub_address = sub_address
        # The type of the endpoint that is associated with the intelligent routing listener. Valid values:
        # 
        # *   **Domain**: a custom domain name.
        # *   **Ip**: a custom IP address.
        # *   **PublicIp**: a public IP address provided by Alibaba Cloud.
        # *   **ECS**: an Elastic Compute Service (ECS) instance.
        # *   **SLB**: a Server Load Balancer (SLB) instance.
        # *   **ALB**: an Application Load Balancer (ALB) instance.
        # *   **OSS**: an Object Storage Service (OSS) bucket.
        # *   **ENI**: an elastic network interface (ENI).
        # *   **NLB**: a Network Load Balancer (NLB) instance.
        # *   **IpTarget**: a custom private IP address.
        # 
        # You can specify up to 100 endpoint types in the endpoint group that is associated with the intelligent routing listener.
        # 
        # > *   If you set **Type** to **Standard**, you can configure the endpoint group and endpoint that are associated with the intelligent routing listener. In addition, this parameter is required.
        # >*   If you set this parameter to **ECS**, **ENI**, **SLB**, **ALB**, **NLB**, or **IpTarget** and the AliyunServiceRoleForGaVpcEndpoint service-linked role does not exist, the system automatically creates the role.
        # >*   If you set this parameter to **ALB** and the AliyunServiceRoleForGaAlb service-linked role does not exist, the system automatically creates the role.
        # >*   If you set this parameter to **OSS** and the AliyunServiceRoleForGaOss service-linked role does not exist, the system automatically creates the role.
        # >*   If you set this parameter to **NLB** and the AliyunServiceRoleForGaNlb service-linked role does not exist, the system automatically creates the role.
        # >>For more information, see [Service-linked roles](https://help.aliyun.com/document_detail/178360.html).
        self.type = type
        # The IDs of vSwitches that are deployed in the VPC.
        self.v_switch_ids = v_switch_ids
        # The virtual private cloud (VPC) ID.
        # 
        # You can specify one VPC ID for an endpoint group of an intelligent routing listener.
        # 
        # >  This parameter is valid and required only if Type is set to **IpTarget**.
        self.vpc_id = vpc_id
        # The weight of the endpoint that is associated with the intelligent routing listener.
        # 
        # Valid values: **0** to **255**.
        # 
        # You can specify the weights of up to 100 endpoints for an endpoint group of an intelligent routing listener.
        # 
        # > *   If you set **Type** to **Standard**, you can configure the endpoint group and endpoint that are associated with the intelligent routing listener. In addition, this parameter is required.
        # >*   If the weight of an endpoint is set to 0, GA stops distributing network traffic to the endpoint. Proceed with caution.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_client_ippreservation is not None:
            result['EnableClientIPPreservation'] = self.enable_client_ippreservation

        if self.enable_proxy_protocol is not None:
            result['EnableProxyProtocol'] = self.enable_proxy_protocol

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

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
        if m.get('EnableClientIPPreservation') is not None:
            self.enable_client_ippreservation = m.get('EnableClientIPPreservation')

        if m.get('EnableProxyProtocol') is not None:
            self.enable_proxy_protocol = m.get('EnableProxyProtocol')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

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
        # The description of the endpoint group that is associated with the custom routing listener.
        # 
        # The description can be up to 200 characters in length and cannot contain `http://` or `https://`.
        # 
        # You can specify up to five endpoint group descriptions.
        # 
        # >  You can configure endpoint groups and endpoints for a custom routing listener only if **Type** is set to **CustomRouting**.
        self.description = description
        # The mapping configurations of the endpoint group that is associated with the custom routing listener.
        # 
        # You need to specify the port ranges and protocols used by the endpoint group. The ports are mapped to listener ports.
        # 
        # You can specify up to 20 mapping configurations for an endpoint group of a custom routing listener.
        # 
        # >  You can configure endpoint groups and endpoints for a custom routing listener only if **Type** is set to **CustomRouting**.
        self.destination_configurations = destination_configurations
        # The endpoints that are associated with the custom routing listener.
        # 
        # You can configure up to 10 endpoints for an endpoint group of a custom routing listener.
        # 
        # >  You can configure endpoint groups and endpoints for a custom routing listener only if **Type** is set to **CustomRouting**.
        self.endpoint_configurations = endpoint_configurations
        # The region ID of the endpoint group that is associated with the custom routing listener.
        # 
        # You can enter the region IDs of up to five endpoint groups.
        # 
        # >  You can configure endpoint groups and endpoints for a custom routing listener only if **Type** is set to **CustomRouting**.
        self.endpoint_group_region = endpoint_group_region
        # The name of the endpoint group that is associated with the custom routing listener.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        # 
        # You can specify up to five endpoint group names.
        # 
        # >  You can configure endpoint groups and endpoints for a custom routing listener only if **Type** is set to **CustomRouting**.
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
        # The name of the vSwitch attached to the endpoint of the custom routing listener.
        # 
        # >  You can configure endpoint groups and endpoints for a custom routing listener only if **Type** is set to **CustomRouting**.
        self.endpoint = endpoint
        # The destinations in the endpoint that is associated with the custom routing listener.
        # 
        # You can specify up to 20 traffic destinations for each endpoint of a custom routing listener.
        # 
        # >  You can configure endpoint groups and endpoints for a custom routing listener only if **Type** is set to **CustomRouting**.
        self.policy_configurations = policy_configurations
        # The traffic policy for the endpoint that is associated with the custom routing listener. Default value: DenyAll. Valid values:
        # 
        # *   **DenyAll** (default): denies all traffic to the specified backend service.
        # *   **AllowAll**: allows all traffic to the specified backend service.
        # *   **AllowCustom**: allows traffic only to specified destinations in the endpoint. If you set this parameter to AllowCustom, you must specify IP addresses and port ranges as the destinations to which you want to distribute traffic. If you specify only IP addresses and do not specify port ranges, GA can forward traffic to the specified IP addresses over all destination ports.
        # 
        # >  You can configure endpoint groups and endpoints for a custom routing listener only if **Type** is set to **CustomRouting**.
        self.traffic_to_endpoint_policy = traffic_to_endpoint_policy
        # The service type of the endpoint that is associated with the custom routing listener. Default value: PrivateSubNet. Set the value to
        # 
        # **PrivateSubNet**, which specifies a private CIDR block.
        # 
        # >  You can configure endpoint groups and endpoints for a custom routing listener only if **Type** is set to **CustomRouting**.
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
        # The IP address of the destination.
        # 
        # This parameter takes effect only if **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify up to 20 destination IP addresses for each endpoint of a custom routing listener.
        # 
        # >  You can configure endpoint groups and endpoints for a custom routing listener only if **Type** is set to **CustomRouting**.
        self.address = address
        # The port ranges of the destination to which traffic is forwarded. The value of this parameter must fall within the port range of the endpoint group.
        # 
        # If you do not specify this parameter, traffic is forwarded over all ports.
        # 
        # This parameter takes effect only if **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify port ranges for up to 20 destinations in each endpoint of a custom routing listener. You can specify up to five port ranges for each destination.
        # 
        # >  You can configure endpoint groups and endpoints for a custom routing listener only if **Type** is set to **CustomRouting**.
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
        # The start port of the port range. The value of this parameter must fall within the port range of the backend service.
        # 
        # This parameter takes effect only if **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify port ranges for up to 20 destinations in each endpoint of a custom routing listener. You can specify up to five start ports for each destination.
        # 
        # >  You can configure endpoint groups and endpoints for a custom routing listener only if **Type** is set to **CustomRouting**.
        self.from_port = from_port
        # The end port of the destination port range. The value of this parameter must fall within the port range of the backend service.
        # 
        # This parameter takes effect only if **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify port ranges for up to 20 destinations in each endpoint of a custom routing listener. You can specify up to five end ports for each destination.
        # 
        # >  You can configure endpoint groups and endpoints for a custom routing listener only if **Type** is set to **CustomRouting**.
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
        # The start port used by the endpoint group that is associated with the custom routing listener.
        # 
        # Valid values: **1** to **65499**. The value of **FromPort** must be equal to or smaller than the value of **ToPort**.
        # 
        # You can specify up to 20 start ports for an endpoint group of a custom routing listener.
        # 
        # >  You can configure endpoint groups and endpoints for a custom routing listener only if **Type** is set to **CustomRouting**.
        self.from_port = from_port
        # The protocol used by the endpoint group that is associated with the custom routing listener.
        # 
        # You can specify up to four protocol types for an endpoint group of a custom routing listener.
        # 
        # >  You can configure endpoint groups and endpoints for a custom routing listener only if **Type** is set to **CustomRouting**.
        self.protocols = protocols
        # The end port used by the endpoint group that is associated with the custom routing listener.
        # 
        # Valid values: **1** to **65499**. The value of **FromPort** must be equal to or smaller than the value of **ToPort**.
        # 
        # You can specify up to 20 end ports for an endpoint group of a custom routing listener.
        # 
        # >  You can configure endpoint groups and endpoints for a custom routing listener only if **Type** is set to **CustomRouting**.
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
        # > This parameter is required only when you create an HTTPS listener.
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

