# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nlb20220430 import models as main_models
from darabonba.model import DaraModel

class CreateListenerShrinkRequest(DaraModel):
    def __init__(
        self,
        alpn_enabled: bool = None,
        alpn_policy: str = None,
        ca_certificate_ids: List[str] = None,
        ca_enabled: bool = None,
        certificate_ids: List[str] = None,
        client_token: str = None,
        cps: int = None,
        dry_run: bool = None,
        end_port: int = None,
        idle_timeout: int = None,
        listener_description: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        load_balancer_id: str = None,
        mss: int = None,
        proxy_protocol_enabled: bool = None,
        proxy_protocol_v2config_shrink: str = None,
        region_id: str = None,
        sec_sensor_enabled: bool = None,
        security_policy_id: str = None,
        server_group_id: str = None,
        start_port: int = None,
        tag: List[main_models.CreateListenerShrinkRequestTag] = None,
    ):
        # Specifies whether to enable ALPN. Valid values:
        # 
        # - **true**: enables ALPN.
        # 
        # - **false** (default): disables ALPN.
        self.alpn_enabled = alpn_enabled
        # The ALPN policy. Valid values:
        # 
        # - **HTTP1Only**: negotiates only HTTP/1.x. The priority is HTTP/1.1 > HTTP/1.0.
        # - **HTTP2Only**: negotiates only HTTP/2.
        # - **HTTP2Optional**: prefers HTTP/1.x but also accepts HTTP/2. The priority is HTTP/1.1 > HTTP/1.0 > HTTP/2.
        # - **HTTP2Preferred**: prefers HTTP/2 but also accepts HTTP/1.x. The priority is HTTP/2 > HTTP/1.1 > HTTP/1.0.
        # 
        # > You must configure this parameter after **AlpnEnabled** is enabled.
        self.alpn_policy = alpn_policy
        # The CA certificate list. This parameter takes effect only for TCPSSL listeners.
        # 
        # > Currently, you can add only one CA certificate.
        self.ca_certificate_ids = ca_certificate_ids
        # Specifies whether to enable mutual authentication. Valid values:
        # 
        # - **true**: enables mutual authentication.
        # 
        # - **false** (default): disables mutual authentication.
        self.ca_enabled = ca_enabled
        # The server certificate list. This parameter takes effect only for TCPSSL listeners.
        # 
        # > Currently, you can add only one server certificate.
        self.certificate_ids = certificate_ids
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate a parameter value on your client to ensure that the value is unique across different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is unique.
        self.client_token = client_token
        # The limit on the number of new connections processed per second by the listener in each zone (VIP). Valid values: **0** to **1000000**. **0** indicates that no limit is applied.
        self.cps = cps
        # Specifies whether to only precheck the request. Valid values:
        # - **true**: sends a precheck request without creating the listener. The system checks whether required parameters are specified, the request format, and service limits. If the request fails the precheck, the corresponding error is returned. If the request passes the precheck, the DryRunOperation error code is returned.
        # - **false** (default): sends a regular request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The end port for all-port listening. Valid values: **1** to **65535**.
        # The end port must be greater than the start port.
        # 
        # > You must configure this parameter when **ListenerPort** is set to **0**.
        self.end_port = end_port
        # The idle timeout period for connections. Unit: seconds.
        # 
        # - If **ListenerProtocol** is set to **TCP** or **TCPSSL**, the valid values are **10** to **900**. Default value: **900**.
        # 
        # - If **ListenerProtocol** is set to **UDP**, the valid values are **10** to **90**. Default value: **90**.
        self.idle_timeout = idle_timeout
        # The custom listener name.
        # 
        # The name must be 2 to 256 characters in length, and can contain Chinese characters, English letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (_), and hyphens (-).
        self.listener_description = listener_description
        # The listener port. Valid values: **0** to **65535**.
        # 
        # **0**: indicates that the all-port feature is used. If you set this parameter to **0**, you must configure **StartPort** and **EndPort**.
        # 
        # This parameter is required.
        self.listener_port = listener_port
        # The listener protocol. Valid values: **TCP**, **UDP**, and **TCPSSL**.
        # 
        # This parameter is required.
        self.listener_protocol = listener_protocol
        # The Network Load Balancer (NLB) instance ID.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The maximum segment size (MSS) of TCP packets. Unit: bytes. Valid values: **0** to **1500**.
        # **0**: indicates that the MSS value of user TCP packets is not modified.
        # 
        # > This parameter is supported only by TCP and TCPSSL listeners.
        self.mss = mss
        # Specifies whether to use the Proxy Protocol to pass the client source IP address to backend servers. Valid values:
        # 
        # - **true**: enables the feature.
        # 
        # - **false** (default): disables the feature.
        self.proxy_protocol_enabled = proxy_protocol_enabled
        # The configuration for passing the VpcId, PrivateLinkEpId, and PrivateLinkEpsId information to backend servers by using the Proxy Protocol.
        self.proxy_protocol_v2config_shrink = proxy_protocol_v2config_shrink
        # The region ID of the Network Load Balancer (NLB) instance. 
        # 
        # You can invoke the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to query region IDs.
        self.region_id = region_id
        # Specifies whether to enable second-level monitoring. Valid values:
        # 
        # - **true**: enables second-level monitoring.
        # 
        # - **false** (default): disables second-level monitoring.
        self.sec_sensor_enabled = sec_sensor_enabled
        # The ID of the security policy. System security policies and custom security policies are supported.
        # 
        # - System policies: **tls_cipher_policy_1_0** (default), **tls_cipher_policy_1_1**, **tls_cipher_policy_1_2**, **tls_cipher_policy_1_2_strict**, and **tls_cipher_policy_1_2_strict_with_1_3**.
        # - Custom security policies: Enter the ID of a custom security policy.
        #     - To create a custom policy, refer to [CreateSecurityPolicy](https://help.aliyun.com/document_detail/445901.html).
        #     - To query security policies, refer to [ListSecurityPolicy](https://help.aliyun.com/document_detail/445900.html).
        # 
        # > This parameter takes effect only for TCPSSL listeners.
        self.security_policy_id = security_policy_id
        # The ID of the server group.
        # > - If **ListenerProtocol** is set to **TCP**, the listener supports server groups whose backend protocol is **TCP** or **TCP_UDP**, but does not support server groups whose backend protocol is **UDP**.
        # > - If **ListenerProtocol** is set to **UDP**, the listener supports server groups whose backend protocol is **UDP** or **TCP_UDP**, but does not support server groups whose backend protocol is **TCP**.
        # > - If **ListenerProtocol** is set to **TCPSSL**, the listener supports server groups whose backend protocol is **TCP** and for which **client address preservation is disabled**. It does not support server groups whose backend protocol is **TCP** and for which **client address preservation is enabled**, or server groups whose backend protocol is **UDP** or **TCP_UDP**.
        self.server_group_id = server_group_id
        # The start port for all-port listening. Valid values: **1** to **65535**.
        # 
        # > You must configure this parameter when **ListenerPort** is set to **0**.
        self.start_port = start_port
        # The list of tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alpn_enabled is not None:
            result['AlpnEnabled'] = self.alpn_enabled

        if self.alpn_policy is not None:
            result['AlpnPolicy'] = self.alpn_policy

        if self.ca_certificate_ids is not None:
            result['CaCertificateIds'] = self.ca_certificate_ids

        if self.ca_enabled is not None:
            result['CaEnabled'] = self.ca_enabled

        if self.certificate_ids is not None:
            result['CertificateIds'] = self.certificate_ids

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cps is not None:
            result['Cps'] = self.cps

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.end_port is not None:
            result['EndPort'] = self.end_port

        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout

        if self.listener_description is not None:
            result['ListenerDescription'] = self.listener_description

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.mss is not None:
            result['Mss'] = self.mss

        if self.proxy_protocol_enabled is not None:
            result['ProxyProtocolEnabled'] = self.proxy_protocol_enabled

        if self.proxy_protocol_v2config_shrink is not None:
            result['ProxyProtocolV2Config'] = self.proxy_protocol_v2config_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sec_sensor_enabled is not None:
            result['SecSensorEnabled'] = self.sec_sensor_enabled

        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id

        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        if self.start_port is not None:
            result['StartPort'] = self.start_port

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlpnEnabled') is not None:
            self.alpn_enabled = m.get('AlpnEnabled')

        if m.get('AlpnPolicy') is not None:
            self.alpn_policy = m.get('AlpnPolicy')

        if m.get('CaCertificateIds') is not None:
            self.ca_certificate_ids = m.get('CaCertificateIds')

        if m.get('CaEnabled') is not None:
            self.ca_enabled = m.get('CaEnabled')

        if m.get('CertificateIds') is not None:
            self.certificate_ids = m.get('CertificateIds')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Cps') is not None:
            self.cps = m.get('Cps')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EndPort') is not None:
            self.end_port = m.get('EndPort')

        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')

        if m.get('ListenerDescription') is not None:
            self.listener_description = m.get('ListenerDescription')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('Mss') is not None:
            self.mss = m.get('Mss')

        if m.get('ProxyProtocolEnabled') is not None:
            self.proxy_protocol_enabled = m.get('ProxyProtocolEnabled')

        if m.get('ProxyProtocolV2Config') is not None:
            self.proxy_protocol_v2config_shrink = m.get('ProxyProtocolV2Config')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecSensorEnabled') is not None:
            self.sec_sensor_enabled = m.get('SecSensorEnabled')

        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')

        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        if m.get('StartPort') is not None:
            self.start_port = m.get('StartPort')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateListenerShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateListenerShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The key can be up to 64 characters in length, and cannot start with `aliyun` or `acs:`, or contain `http://` or `https://`. Supported characters include letters, digits, underscores (_), periods (.), colons (:), forward slashes (/), equal signs (=), plus signs (+), hyphens (-), and at signs (@).
        # 
        # You can add up to 20 tags in a single call.
        self.key = key
        # The tag value. The value can be up to 128 characters in length, and cannot start with `aliyun` or `acs:`, or contain `http://` or `https://`. Supported characters include letters, digits, underscores (_), periods (.), colons (:), forward slashes (/), equal signs (=), plus signs (+), hyphens (-), and at signs (@).
        # 
        # You can add up to 20 tags in a single call.
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

