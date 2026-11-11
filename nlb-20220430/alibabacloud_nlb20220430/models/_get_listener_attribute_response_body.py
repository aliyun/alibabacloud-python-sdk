# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nlb20220430 import models as main_models
from darabonba.model import DaraModel

class GetListenerAttributeResponseBody(DaraModel):
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
        proxy_protocol_v2config: main_models.GetListenerAttributeResponseBodyProxyProtocolV2Config = None,
        region_id: str = None,
        request_id: str = None,
        sec_sensor_enabled: bool = None,
        security_policy_id: str = None,
        server_group_id: str = None,
        start_port: str = None,
        tags: List[main_models.GetListenerAttributeResponseBodyTags] = None,
    ):
        # Specifies whether Application-Layer Protocol Negotiation (ALPN) is enabled. Valid values:
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
        # The CA certificate list. Currently, you can add only one CA certificate.
        # > This parameter takes effect only for TCPSSL listeners.
        self.ca_certificate_ids = ca_certificate_ids
        # Specifies whether mutual authentication is enabled. Valid values:
        # 
        # - **true**: enabled.
        # 
        # - **false**: disabled.
        self.ca_enabled = ca_enabled
        # The server certificate list. Currently, you can add only one server certificate.
        # 
        # > This parameter takes effect only for TCPSSL listeners.
        self.certificate_ids = certificate_ids
        # The maximum number of new connections per second that the listener can process in each zone (VIP). Valid values: **0** to **1000000**. **0** indicates that no limit is applied.
        self.cps = cps
        # The end port of the all-port listener. Valid values: **0** to **65535**. The end port must be less than the start port.
        self.end_port = end_port
        # The idle timeout period for connections. Unit: seconds.
        self.idle_timeout = idle_timeout
        # The custom listener name.
        # 
        # The name must be 2 to 256 characters in length, and can contain Chinese characters and English letters. It can also contain digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (_), and hyphens (-).
        self.listener_description = listener_description
        # The listener ID.
        self.listener_id = listener_id
        # The listener port. Valid values: **0** to **65535**. **0** indicates that all-port listening is used. If you set this parameter to **0**, you must configure **StartPort** and **EndPort**.
        self.listener_port = listener_port
        # The listener protocol. Valid values: **TCP**, **UDP**, and **TCPSSL**.
        self.listener_protocol = listener_protocol
        # The current status of the listener. Valid values:
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
        # The Network Load Balancer (NLB) instance ID.
        self.load_balancer_id = load_balancer_id
        # The maximum segment size (MSS) of a TCP packet. Unit: bytes. Valid values: **0** to **1500**. **0** indicates that the MSS value of user TCP packets is not modified.
        # 
        # > This field is supported only by TCP and TCPSSL listeners.
        self.mss = mss
        # Specifies whether to use the Proxy Protocol to pass the client source IP address to backend servers. Valid values:
        # 
        # - **true**: enabled.
        # 
        # - **false**: disabled.
        self.proxy_protocol_enabled = proxy_protocol_enabled
        # The configuration for passing the VpcId, PrivateLinkEpId, and PrivateLinkEpsId information to backend servers by using the Proxy Protocol.
        self.proxy_protocol_v2config = proxy_protocol_v2config
        # The region ID of the Network Load Balancer (NLB) instance.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # Specifies whether to enable the second-level monitoring feature. Valid values:
        # 
        # - **true**: enabled.
        # 
        # - **false**: disabled.
        self.sec_sensor_enabled = sec_sensor_enabled
        # The security policy ID. System security policies and custom security policies are supported.
        # 
        # - System policies: **tls_cipher_policy_1_0** (default), **tls_cipher_policy_1_1**, **tls_cipher_policy_1_2**, **tls_cipher_policy_1_2_strict**, and **tls_cipher_policy_1_2_strict_with_1_3**.
        # - Custom security policies: Enter the ID of the custom security policy.
        #     - To create a custom policy, see [CreateSecurityPolicy](https://help.aliyun.com/document_detail/445901.html).
        #     - To query security policies, see [ListSecurityPolicy](https://help.aliyun.com/document_detail/445900.html).
        # 
        # > This parameter takes effect only for TCPSSL listeners.
        self.security_policy_id = security_policy_id
        # The server group ID.
        self.server_group_id = server_group_id
        # The start port of the all-port listener. Valid values: **0** to **65535**.
        self.start_port = start_port
        # The tag list.
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
            temp_model = main_models.GetListenerAttributeResponseBodyProxyProtocolV2Config()
            self.proxy_protocol_v2config = temp_model.from_map(m.get('ProxyProtocolV2Config'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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
                temp_model = main_models.GetListenerAttributeResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class GetListenerAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class GetListenerAttributeResponseBodyProxyProtocolV2Config(DaraModel):
    def __init__(
        self,
        ppv_2cn_id_enabled: bool = None,
        ppv_2private_link_ep_id_enabled: bool = None,
        ppv_2private_link_eps_id_enabled: bool = None,
        ppv_2vpc_id_enabled: bool = None,
    ):
        # Specifies whether to use the Proxy Protocol to pass the CN-ID to backend servers. Valid values:
        # 
        # - **true**: enabled.
        # 
        # - **false**: disabled.
        self.ppv_2cn_id_enabled = ppv_2cn_id_enabled
        # Specifies whether to use the Proxy Protocol to pass the PrivateLinkEpId to backend servers. Valid values:
        # 
        # - **true**: enabled.
        # 
        # - **false**: disabled.
        self.ppv_2private_link_ep_id_enabled = ppv_2private_link_ep_id_enabled
        # Specifies whether to use the Proxy Protocol to pass the PrivateLinkEpsId to backend servers. Valid values:
        # 
        # - **true**: enabled.
        # 
        # - **false**: disabled.
        self.ppv_2private_link_eps_id_enabled = ppv_2private_link_eps_id_enabled
        # Specifies whether to use the Proxy Protocol to pass the VpcId to backend servers. Valid values:
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

