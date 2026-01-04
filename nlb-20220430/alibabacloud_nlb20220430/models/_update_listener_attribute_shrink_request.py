# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateListenerAttributeShrinkRequest(DaraModel):
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
        idle_timeout: int = None,
        listener_description: str = None,
        listener_id: str = None,
        mss: int = None,
        proxy_protocol_enabled: bool = None,
        proxy_protocol_v2config_shrink: str = None,
        region_id: str = None,
        sec_sensor_enabled: bool = None,
        security_policy_id: str = None,
        server_group_id: str = None,
    ):
        # Specifies whether to enable Application-Layer Protocol Negotiation (ALPN). Valid values:
        # 
        # *   **true**
        # *   **false**
        self.alpn_enabled = alpn_enabled
        # The name of the ALPN policy. The following are the possible values:
        # 
        # *   **HTTP1Only**: Negotiate only HTTP/1.\\*. The ALPN preference list is HTTP/1.1, HTTP/1.0.
        # *   **HTTP2Only**: Negotiate only HTTP/2. The ALPN preference list is HTTP/2.
        # *   **HTTP2Optional**: Prefer HTTP/1.\\* over HTTP/2. The ALPN preference list is HTTP/1.1, HTTP/1.0, HTTP/2.
        # *   **HTTP2Preferred**: Prefer HTTP/2 over HTTP/1.\\*. The ALPN preference list is HTTP/2, HTTP/1.1, HTTP/1.0.
        # 
        # >  This parameter is required if AlpnEnabled is set to true.
        self.alpn_policy = alpn_policy
        # The CA certificate. You can specify only one CA certificate.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.ca_certificate_ids = ca_certificate_ids
        # Specifies whether to enable mutual authentication. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.ca_enabled = ca_enabled
        # The server certificate. Only one server certificate is supported.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.certificate_ids = certificate_ids
        # The client token used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token. Ensure that the token is unique among different requests. Only ASCII characters are allowed.
        # 
        # >  If you do not set this parameter, the value of **RequestId** is used.**** The value of **RequestId** is different for each request.
        self.client_token = client_token
        # The maximum number of new connections per second supported by the listener in each zone (virtual IP address). Valid values: **0** to **1000000**. **0** indicates that the number of connections is unlimited.
        self.cps = cps
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: validates the request without performing the operation. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the validation, the corresponding error message is returned. If the request passes the validation, the `DryRunOperation` error code is returned.
        # *   **false** (default): validates the request and performs the operation. If the request passes the validation, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The timeout period for idle connections. Unit: seconds
        # 
        # *   If the listener uses **TCP** or **TCPSSL**, you can set this parameter to a value ranging from **10** to **900**. Default value: **900**
        # *   If the listener uses **UDP**, you can set this parameter to a value ranging from **10** to **20**. Default value: **20**
        self.idle_timeout = idle_timeout
        # The name of the listener.
        # 
        # The name must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (_), and hyphens (-).
        self.listener_description = listener_description
        # The listener ID.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The size of the largest TCP packet segment. Unit: bytes. Valid values: **0** to **1500**. **0** indicates that the maximum segment size (MSS) remains unchanged. This parameter is supported only by TCP listeners and listeners that use SSL over TCP.
        self.mss = mss
        # Specifies whether to use the Proxy protocol to pass the client IP address to the backend server. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.proxy_protocol_enabled = proxy_protocol_enabled
        # Specifies that the Proxy protocol passes the VpcId, PrivateLinkEpId, and PrivateLinkEpsId parameters to backend servers.
        self.proxy_protocol_v2config_shrink = proxy_protocol_v2config_shrink
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to query the most recent region list.
        self.region_id = region_id
        # Specifies whether to enable fine-grained monitoring. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.sec_sensor_enabled = sec_sensor_enabled
        # The ID of the security policy.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.security_policy_id = security_policy_id
        # The server group ID.
        # 
        # > 
        # 
        # *   If the listener uses **TCP**, you can specify server groups whose protocol is **TCP** or **TCP_UDP**. **UDP** server groups are not supported.
        # 
        # *   If the listener uses **UDP**, you can specify server groups whose protocol is **UDP** or **TCP_UDP**. **TCP** server groups are not supported.
        # 
        # *   If the listener uses **TCPSSL**, you can specify server groups whose protocol is **TCP** and whose **client IP preservation is disabled**. **TCP** server groups for which **client IP preservation is enabled** and server groups whose protocol is **UDP** or **TCP_UDP** are not supported.
        self.server_group_id = server_group_id

    def validate(self):
        pass

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

        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout

        if self.listener_description is not None:
            result['ListenerDescription'] = self.listener_description

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

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

        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')

        if m.get('ListenerDescription') is not None:
            self.listener_description = m.get('ListenerDescription')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

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

        return self

