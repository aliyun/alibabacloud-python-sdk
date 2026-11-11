# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nlb20220430 import models as main_models
from darabonba.model import DaraModel

class ListListenersResponseBody(DaraModel):
    def __init__(
        self,
        listeners: List[main_models.ListListenersResponseBodyListeners] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of Network Load Balancer (NLB) listeners.
        self.listeners = listeners
        # The number of entries returned per page.
        self.max_results = max_results
        # The pagination token. Valid values:
        # - If **NextToken** is empty, no next query is required.
        # - If **NextToken** returns a value, the value indicates the token for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListListenersResponseBodyListeners(DaraModel):
    def __init__(
        self,
        alpn_enabled: bool = None,
        alpn_policy: str = None,
        ca_certificate_ids: List[str] = None,
        ca_enabled: bool = None,
        certificate_ids: List[str] = None,
        cps: int = None,
        end_port: str = None,
        idle_timeout: int = None,
        listener_description: str = None,
        listener_id: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        listener_status: str = None,
        load_balancer_id: str = None,
        mss: int = None,
        proxy_protocol_enabled: bool = None,
        proxy_protocol_v2config: main_models.ListListenersResponseBodyListenersProxyProtocolV2Config = None,
        region_id: str = None,
        sec_sensor_enabled: bool = None,
        security_policy_id: str = None,
        server_group_id: str = None,
        start_port: str = None,
        tags: List[main_models.ListListenersResponseBodyListenersTags] = None,
    ):
        # Indicates whether Application-Layer Protocol Negotiation (ALPN) is enabled. Valid values:
        # 
        # - **true**: enabled.
        # 
        # - **false**: disabled.
        self.alpn_enabled = alpn_enabled
        # The ALPN policy. Valid values:
        # 
        # - **HTTP1Only**
        # - **HTTP2Only**
        # - **HTTP2Preferred**
        # - **HTTP2Optional**
        self.alpn_policy = alpn_policy
        # The list of CA certificates.
        # > This parameter takes effect only for TCPSSL listeners.
        self.ca_certificate_ids = ca_certificate_ids
        # Indicates whether mutual authentication is enabled. Valid values:
        # 
        # - **true**: enabled.
        # 
        # - **false**: disabled.
        self.ca_enabled = ca_enabled
        # The list of server certificates.
        # 
        # > This parameter takes effect only for TCPSSL listeners.
        self.certificate_ids = certificate_ids
        # The maximum number of new connections per second that the listener can process in each zone (VIP). Valid values: **0** to **1000000**. A value of **0** indicates that no limit is applied.
        self.cps = cps
        # The end port for all-port listening.
        self.end_port = end_port
        # The idle timeout period for connections. Unit: seconds.
        self.idle_timeout = idle_timeout
        # The custom name of the listener.
        # 
        # The name must be 2 to 256 characters in length and can contain Chinese characters, English letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (_), and hyphens (-).
        self.listener_description = listener_description
        # The listener ID.
        self.listener_id = listener_id
        # The listener port.
        self.listener_port = listener_port
        # The listener protocol. Valid values: **TCP**, **UDP**, and **TCPSSL**.
        self.listener_protocol = listener_protocol
        # The status of the listener. Valid values:
        # 
        # - **Provisioning**: The listener is being created.
        # 
        # - **Running**: The listener is running.
        # 
        # - **Configuring**: The listener is being configured.
        # 
        # - **Stopping**: The listener is being stopped.
        # 
        # - **Stopped**: The listener is stopped.
        # 
        # - **Starting**: The listener is being started.
        # 
        # - **Deleting**: The listener is being deleted.
        # 
        # - **Deleted**: The listener is deleted.
        self.listener_status = listener_status
        # The ID of the Network Load Balancer (NLB) instance.
        self.load_balancer_id = load_balancer_id
        # The maximum segment size (MSS) of TCP packets. Unit: bytes. Valid values: **0** to **1500**. A value of **0** indicates that the MSS value of user TCP packets is not modified.
        # 
        # > This parameter is supported only by TCP and TCPSSL listeners.
        self.mss = mss
        # Indicates whether the Proxy Protocol is enabled to pass the client source IP address to backend servers. Valid values:
        # 
        # - **true**: enabled.
        # 
        # - **false**: disabled.
        self.proxy_protocol_enabled = proxy_protocol_enabled
        # The configuration for passing the VpcId, PrivateLinkEpId, and PrivateLinkEpsId information to backend servers by using the Proxy Protocol.
        self.proxy_protocol_v2config = proxy_protocol_v2config
        # The region ID of the Network Load Balancer (NLB) instance.
        self.region_id = region_id
        # Indicates whether second-level monitoring is enabled. Valid values:
        # 
        # - **true**: enabled.
        # 
        # - **false**: disabled.
        self.sec_sensor_enabled = sec_sensor_enabled
        # The ID of the security policy.
        # 
        # > This parameter takes effect only for TCPSSL listeners.
        self.security_policy_id = security_policy_id
        # The ID of the server group.
        self.server_group_id = server_group_id
        # The start port for all-port listening.
        self.start_port = start_port
        # The list of tags.
        self.tags = tags

    def validate(self):
        if self.proxy_protocol_v2config:
            self.proxy_protocol_v2config.validate()
        if self.tags:
            for v1 in self.tags:
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

        if self.cps is not None:
            result['Cps'] = self.cps

        if self.end_port is not None:
            result['EndPort'] = self.end_port

        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout

        if self.listener_description is not None:
            result['ListenerDescription'] = self.listener_description

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol

        if self.listener_status is not None:
            result['ListenerStatus'] = self.listener_status

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

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

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

        if m.get('Cps') is not None:
            self.cps = m.get('Cps')

        if m.get('EndPort') is not None:
            self.end_port = m.get('EndPort')

        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')

        if m.get('ListenerDescription') is not None:
            self.listener_description = m.get('ListenerDescription')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')

        if m.get('ListenerStatus') is not None:
            self.listener_status = m.get('ListenerStatus')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('Mss') is not None:
            self.mss = m.get('Mss')

        if m.get('ProxyProtocolEnabled') is not None:
            self.proxy_protocol_enabled = m.get('ProxyProtocolEnabled')

        if m.get('ProxyProtocolV2Config') is not None:
            temp_model = main_models.ListListenersResponseBodyListenersProxyProtocolV2Config()
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

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListListenersResponseBodyListenersTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListListenersResponseBodyListenersTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class ListListenersResponseBodyListenersProxyProtocolV2Config(DaraModel):
    def __init__(
        self,
        ppv_2cn_id_enabled: bool = None,
        ppv_2private_link_ep_id_enabled: bool = None,
        ppv_2private_link_eps_id_enabled: bool = None,
        ppv_2vpc_id_enabled: bool = None,
    ):
        # Indicates whether the Common Name (CN) field of the client certificate is passed to backend servers by using Proxy Protocol V2. Note: This parameter takes effect only when the listener protocol is TCPSSL, mutual authentication (mTLS) is enabled, and Proxy Protocol V2 is enabled. Valid values:
        # 
        # - **true**: enabled.
        # 
        # - **false**: disabled.
        self.ppv_2cn_id_enabled = ppv_2cn_id_enabled
        # Indicates whether the Proxy Protocol is enabled to pass the PrivateLinkEpId to backend servers. Valid values:
        # 
        # - **true**: enabled.
        # 
        # - **false**: disabled.
        self.ppv_2private_link_ep_id_enabled = ppv_2private_link_ep_id_enabled
        # Indicates whether the Proxy Protocol is enabled to pass the PrivateLinkEpsId to backend servers. Valid values:
        # 
        # - **true**: enabled.
        # 
        # - **false**: disabled.
        self.ppv_2private_link_eps_id_enabled = ppv_2private_link_eps_id_enabled
        # Indicates whether the Proxy Protocol is enabled to pass the VpcId to backend servers. Valid values:
        # 
        # - **true**: enabled.
        # 
        # - **false**: disabled.
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

