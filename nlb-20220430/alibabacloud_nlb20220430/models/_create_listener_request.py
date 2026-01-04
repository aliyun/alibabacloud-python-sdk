# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nlb20220430 import models as main_models
from darabonba.model import DaraModel

class CreateListenerRequest(DaraModel):
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
        proxy_protocol_v2config: main_models.CreateListenerRequestProxyProtocolV2Config = None,
        region_id: str = None,
        sec_sensor_enabled: bool = None,
        security_policy_id: str = None,
        server_group_id: str = None,
        start_port: int = None,
        tag: List[main_models.CreateListenerRequestTag] = None,
    ):
        # Specifies whether to enable Application-Layer Protocol Negotiation (ALPN). Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.alpn_enabled = alpn_enabled
        # The ALPN policy. Valid values:
        # 
        # *   **HTTP1Only**: uses only HTTP 1.x. The priority of HTTP 1.1 is higher than that of HTTP 1.0.
        # *   **HTTP2Only**: uses only HTTP 2.0.
        # *   **HTTP2Optional**: preferentially uses HTTP 1.x over HTTP 2.0. The priority of HTTP 1.1 is higher than that of HTTP 1.0, and the priority of HTTP 1.0 is higher than that of HTTP 2.0.
        # *   **HTTP2Preferred**: preferentially uses HTTP 2.0 over HTTP 1.x. The priority of HTTP 2.0 is higher than that of HTTP 1.1, and the priority of HTTP 1.1 is higher than that of HTTP 1.0.
        # 
        # >  This parameter is required if **AlpnEnabled** is set to true.
        self.alpn_policy = alpn_policy
        # The certificate authority (CA) certificate. This parameter is supported only by TCLSSL listeners.
        # 
        # >  You can specify only one CA certificate.
        self.ca_certificate_ids = ca_certificate_ids
        # Specifies whether to enable mutual authentication. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.ca_enabled = ca_enabled
        # The server certificate. This parameter is supported only by TCLSSL listeners.
        # 
        # >  You can specify only one server certificate.
        self.certificate_ids = certificate_ids
        # The client token used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token. Ensure that the token is unique among different requests. Only ASCII characters are allowed.
        # 
        # >  If you do not set this parameter, the value of **RequestId** is used.**** The value of **RequestId** is different for each request.
        self.client_token = client_token
        # The maximum number of new connections per second supported by the listener in each zone (virtual IP address). Valid values: **0** to **1000000**. **0** indicates that the number of connections is unlimited.
        self.cps = cps
        # Specifies whether to perform a dry run, without sending the actual request. Valid values:
        # 
        # *   **true**: validates the request without performing the operation. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the validation, the corresponding error message is returned. If the request passes the validation, the `DryRunOperation` error code is returned.
        # *   **false** (default): validates the request and performs the operation. If the request passes the validation, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The last port in the listener port range. Valid values: **0** to **65535**. The port number of the last port must be greater than the port number of the first port.
        # 
        # >  This parameter is required when **ListenerPort** is set to **0**.
        self.end_port = end_port
        # The timeout period for idle connections. Unit: seconds.
        # 
        # *   If you set **ListenerProtocol** to **TCP** or **TCPSSL**, this parameter can be set to a value ranging from **10** to **900**. Default value: **900**.
        # *   If **ListenerProtocol** is set to **UDP**, this parameter can be set to a value ranging from **10** to **20**. Default value: **20**.
        self.idle_timeout = idle_timeout
        # The name of the listener.
        # 
        # The name must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (_), and hyphens (-).
        self.listener_description = listener_description
        # The listener port. Valid values: **0** to **65535**.
        # 
        # If you set this parameter to **0**, the listener listens by port range. If you set this parameter to **0**, you must also set the **StartPort** and **EndPort** parameters.
        # 
        # This parameter is required.
        self.listener_port = listener_port
        # The listener protocol. Valid values: **TCP**, **UDP**, and **TCPSSL**.
        # 
        # This parameter is required.
        self.listener_protocol = listener_protocol
        # The ID of the NLB instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The size of the largest TCP packet segment. Unit: bytes. Valid values: **0** to **1500**. **0** indicates that the maximum segment size (MSS) value of TCP packets remains unchanged.
        # 
        # >  This parameter takes effect only for TCP and TCPSSL listeners.
        self.mss = mss
        # Specifies whether to use the Proxy protocol to pass client IP addresses to backend servers. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.proxy_protocol_enabled = proxy_protocol_enabled
        # Specifies whether to use the Proxy protocol to pass the VpcId, PrivateLinkEpId, and PrivateLinkEpsId parameters to backend servers.
        self.proxy_protocol_v2config = proxy_protocol_v2config
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to query the most recent region list.
        self.region_id = region_id
        # Specifies whether to enable fine-grained monitoring. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.sec_sensor_enabled = sec_sensor_enabled
        # The ID of the security policy. System security policies and custom security policies are supported.
        # 
        # *   Valid values for system security policies: **tls_cipher_policy_1_0** (default), **tls_cipher_policy_1_1**, **tls_cipher_policy_1_2**, **tls_cipher_policy_1_2_strict**, and **tls_cipher_policy_1_2_strict_with_1_3**.
        # 
        # *   For a custom security policy, enter the policy ID.
        # 
        #     *   For information about creating a custom security policy, see [CreateSecurityPolicy](https://help.aliyun.com/document_detail/445901.html).
        #     *   For information about querying security policies, see [ListSecurityPolicy](https://help.aliyun.com/document_detail/445900.html).
        # 
        # >  This parameter takes effect only for TCPSSL listeners.
        self.security_policy_id = security_policy_id
        # The server group ID.
        # 
        # >  *   If you set **ListenerProtocol** to **TCP**, you can associate the listener with server groups whose backend protocol is **TCP** or **TCP_UDP**. You cannot associate the listener with server groups whose backend protocol is **UDP**.
        # >  *   If you set **ListenerProtocol** to **UDP**, you can associate the listener with server groups whose backend protocol is **UDP** or **TCP_UDP**. You cannot associate the listener with server groups whose backend protocol is **TCP**.
        # >  *   If you set **ListenerProtocol** to **TCPSSL**, you can associate the listener with server groups whose backend protocol is **TCP** and have **client IP preservation disabled**. You cannot associate the listener with server groups whose backend protocol is **TCP** and have **client IP preservation enabled** or server groups whose backend protocol is **UDP** or **TCP_UDP**.
        self.server_group_id = server_group_id
        # The first port in the listener port range. Valid values: **0** to **65535**.
        # 
        # >  This parameter is required when **ListenerPort** is set to **0**.
        self.start_port = start_port
        # The tags.
        self.tag = tag

    def validate(self):
        if self.proxy_protocol_v2config:
            self.proxy_protocol_v2config.validate()
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

        if self.proxy_protocol_v2config is not None:
            result['ProxyProtocolV2Config'] = self.proxy_protocol_v2config.to_map()

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
            temp_model = main_models.CreateListenerRequestProxyProtocolV2Config()
            self.proxy_protocol_v2config = temp_model.from_map(m.get('ProxyProtocolV2Config'))

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
                temp_model = main_models.CreateListenerRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateListenerRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. The tag key can be up to 64 characters in length, cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`. The tag value can contain letters, digits, and the following special characters: _ . : / = + - @
        # 
        # You can specify up to 20 tags in each call.
        self.key = key
        # The value of the tag. The tag value can be up to 128 characters in length, cannot start with `acs:` or `aliyun`, and cannot contain `http://` or `https://`. The tag value can contain letters, digits, and the following special characters: _ . : / = + - @
        # 
        # You can specify up to 20 tags in each call.
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

class CreateListenerRequestProxyProtocolV2Config(DaraModel):
    def __init__(
        self,
        ppv_2private_link_ep_id_enabled: bool = None,
        ppv_2private_link_eps_id_enabled: bool = None,
        ppv_2vpc_id_enabled: bool = None,
    ):
        # Specifies whether to use the Proxy protocol to pass the Ppv2PrivateLinkEpId parameter to backend servers. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.ppv_2private_link_ep_id_enabled = ppv_2private_link_ep_id_enabled
        # Specifies whether to use the Proxy protocol to pass the PrivateLinkEpsId parameter to backend servers. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.ppv_2private_link_eps_id_enabled = ppv_2private_link_eps_id_enabled
        # Specifies whether to use the Proxy protocol to pass the VpcId parameter to backend servers. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.ppv_2vpc_id_enabled = ppv_2vpc_id_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ppv_2private_link_ep_id_enabled is not None:
            result['Ppv2PrivateLinkEpIdEnabled'] = self.ppv_2private_link_ep_id_enabled

        if self.ppv_2private_link_eps_id_enabled is not None:
            result['Ppv2PrivateLinkEpsIdEnabled'] = self.ppv_2private_link_eps_id_enabled

        if self.ppv_2vpc_id_enabled is not None:
            result['Ppv2VpcIdEnabled'] = self.ppv_2vpc_id_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ppv2PrivateLinkEpIdEnabled') is not None:
            self.ppv_2private_link_ep_id_enabled = m.get('Ppv2PrivateLinkEpIdEnabled')

        if m.get('Ppv2PrivateLinkEpsIdEnabled') is not None:
            self.ppv_2private_link_eps_id_enabled = m.get('Ppv2PrivateLinkEpsIdEnabled')

        if m.get('Ppv2VpcIdEnabled') is not None:
            self.ppv_2vpc_id_enabled = m.get('Ppv2VpcIdEnabled')

        return self

