# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nlb20220430 import models as main_models
from darabonba.model import DaraModel

class UpdateListenerAttributeRequest(DaraModel):
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
        proxy_protocol_v2config: main_models.UpdateListenerAttributeRequestProxyProtocolV2Config = None,
        region_id: str = None,
        sec_sensor_enabled: bool = None,
        security_policy_id: str = None,
        server_group_id: str = None,
    ):
        # Specifies whether to enable Application-Layer Protocol Negotiation (ALPN). Valid values:
        # 
        # - **true**: enables ALPN.
        # 
        # - **false**: disables ALPN.
        self.alpn_enabled = alpn_enabled
        # The ALPN policy. Valid values:
        # 
        # - **HTTP1Only**: negotiates only HTTP/1.x. The priority is HTTP/1.1 > HTTP/1.0.
        # - **HTTP2Only**: negotiates only HTTP/2.
        # - **HTTP2Optional**: prefers HTTP/1.x but also accepts HTTP/2. The priority is HTTP/1.1 > HTTP/1.0 > HTTP/2.
        # - **HTTP2Preferred**: prefers HTTP/2 but also accepts HTTP/1.x. The priority is HTTP/2 > HTTP/1.1 > HTTP/1.0.
        # 
        # > You must configure this parameter after ALPN is enabled.
        self.alpn_policy = alpn_policy
        # The CA certificates. You can add only one CA certificate.
        # 
        # > This parameter takes effect only for TCPSSL listeners.
        self.ca_certificate_ids = ca_certificate_ids
        # Specifies whether to enable mutual authentication. Valid values:
        # 
        # - **true**: enables mutual authentication.
        # 
        # - **false** (default): disables mutual authentication.
        self.ca_enabled = ca_enabled
        # The server certificates. You can add only one server certificate.
        # 
        # > This parameter takes effect only for TCPSSL listeners.
        self.certificate_ids = certificate_ids
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is unique.
        self.client_token = client_token
        # The maximum number of new connections per second that the listener can process in each zone (VIP). Valid values: **0** to **1000000**. A value of **0** indicates that no limit is applied.
        self.cps = cps
        # Specifies whether to only precheck the request. Valid values:
        # - **true**: prechecks the request without updating the listener. The system checks whether required parameters are specified, the request format is valid, and the service limits are met. If the request fails the precheck, the corresponding error is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # - **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The idle connection timeout period. Unit: seconds.
        # 
        # - If the listener is a **TCP** or **TCPSSL** listener, valid values are **10** to **900**. Default value: **900**.
        # 
        # - If the listener is a **UDP** listener, valid values are **10** to **90**. Default value: **90**.
        self.idle_timeout = idle_timeout
        # The custom name of the listener.
        # 
        # The name must be 2 to 256 characters in length, and can contain Chinese characters, English letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (_), and hyphens (-).
        self.listener_description = listener_description
        # The listener instance ID.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The maximum segment size (MSS) of a TCP packet. Unit: bytes. Valid values: **0** to **1500**. A value of **0** indicates that the MSS value of user TCP packets is not modified. This parameter is supported only by TCP and TCPSSL listeners.
        self.mss = mss
        # Specifies whether to use the Proxy Protocol to pass the client source IP address to backend servers. Valid values:
        # 
        # - **true**: yes.
        # 
        # - **false**: no.
        self.proxy_protocol_enabled = proxy_protocol_enabled
        # The configuration for passing the VpcId, PrivateLinkEpId, and PrivateLinkEpsId information to backend servers by using the Proxy Protocol.
        self.proxy_protocol_v2config = proxy_protocol_v2config
        # The ID of the region where the Network Load Balancer (NLB) instance is deployed. 
        # 
        # You can invoke the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to retrieve the region ID.
        self.region_id = region_id
        # Specifies whether to enable second-level monitoring. Valid values:
        # 
        # - **true**: enables second-level monitoring.
        # 
        # - **false**: disables second-level monitoring.
        self.sec_sensor_enabled = sec_sensor_enabled
        # The ID of the security policy.
        # 
        # > This parameter takes effect only for TCPSSL listeners.
        self.security_policy_id = security_policy_id
        # The ID of the server group.
        # 
        # > - If the listener is a **TCP** listener, you can select a server group whose backend protocol is **TCP** or **TCP_UDP**. You cannot select a server group whose backend protocol is **UDP**.
        # > - If the listener is a **UDP** listener, you can select a server group whose backend protocol is **UDP** or **TCP_UDP**. You cannot select a server group whose backend protocol is **TCP**.
        # > - If the listener is a **TCPSSL** listener, you can select a server group whose backend protocol is **TCP** and for which **client address preservation is disabled**. You cannot select a server group whose backend protocol is **TCP** and for which **client address preservation is enabled**, or a server group whose backend protocol is **UDP** or **TCP_UDP**.
        self.server_group_id = server_group_id

    def validate(self):
        if self.proxy_protocol_v2config:
            self.proxy_protocol_v2config.validate()

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
            temp_model = main_models.UpdateListenerAttributeRequestProxyProtocolV2Config()
            self.proxy_protocol_v2config = temp_model.from_map(m.get('ProxyProtocolV2Config'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecSensorEnabled') is not None:
            self.sec_sensor_enabled = m.get('SecSensorEnabled')

        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')

        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        return self

class UpdateListenerAttributeRequestProxyProtocolV2Config(DaraModel):
    def __init__(
        self,
        ppv_2cn_id_enabled: bool = None,
        ppv_2private_link_ep_id_enabled: bool = None,
        ppv_2private_link_eps_id_enabled: bool = None,
        ppv_2vpc_id_enabled: bool = None,
    ):
        # Specifies whether to use the Proxy Protocol to pass the CN-ID to backend servers. Valid values:
        # 
        # - **true**: yes.
        # 
        # - **false**: no.
        self.ppv_2cn_id_enabled = ppv_2cn_id_enabled
        # Specifies whether to use the Proxy Protocol to pass the PrivateLinkEpId to backend servers. Valid values:
        # 
        # - **true**: yes.
        # 
        # - **false**: no.
        self.ppv_2private_link_ep_id_enabled = ppv_2private_link_ep_id_enabled
        # Specifies whether to use the Proxy Protocol to pass the PrivateLinkEpsId to backend servers. Valid values:
        # 
        # - **true**: yes.
        # 
        # - **false**: no.
        self.ppv_2private_link_eps_id_enabled = ppv_2private_link_eps_id_enabled
        # Specifies whether to use the Proxy Protocol to pass the VpcId to backend servers. Valid values:
        # 
        # - **true**: yes.
        # 
        # - **false**: no.
        self.ppv_2vpc_id_enabled = ppv_2vpc_id_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ppv_2cn_id_enabled is not None:
            result['Ppv2CnIdEnabled'] = self.ppv_2cn_id_enabled

        if self.ppv_2private_link_ep_id_enabled is not None:
            result['Ppv2PrivateLinkEpIdEnabled'] = self.ppv_2private_link_ep_id_enabled

        if self.ppv_2private_link_eps_id_enabled is not None:
            result['Ppv2PrivateLinkEpsIdEnabled'] = self.ppv_2private_link_eps_id_enabled

        if self.ppv_2vpc_id_enabled is not None:
            result['Ppv2VpcIdEnabled'] = self.ppv_2vpc_id_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ppv2CnIdEnabled') is not None:
            self.ppv_2cn_id_enabled = m.get('Ppv2CnIdEnabled')

        if m.get('Ppv2PrivateLinkEpIdEnabled') is not None:
            self.ppv_2private_link_ep_id_enabled = m.get('Ppv2PrivateLinkEpIdEnabled')

        if m.get('Ppv2PrivateLinkEpsIdEnabled') is not None:
            self.ppv_2private_link_eps_id_enabled = m.get('Ppv2PrivateLinkEpsIdEnabled')

        if m.get('Ppv2VpcIdEnabled') is not None:
            self.ppv_2vpc_id_enabled = m.get('Ppv2VpcIdEnabled')

        return self

