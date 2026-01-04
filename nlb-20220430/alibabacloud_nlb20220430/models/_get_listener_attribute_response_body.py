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
        # Indicates whether Application-Layer Protocol Negotiation (ALPN) is enabled. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.alpn_enabled = alpn_enabled
        # The ALPN policy. Valid values:
        # 
        # *   **HTTP1Only**
        # *   **HTTP2Only**
        # *   **HTTP2Preferred**
        # *   **HTTP2Optional**
        self.alpn_policy = alpn_policy
        # The CA certificates. Only one CA certificate is supported.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.ca_certificate_ids = ca_certificate_ids
        # Indicates whether mutual authentication is enabled. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.ca_enabled = ca_enabled
        # The server certificates. Only one server certificate is supported.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.certificate_ids = certificate_ids
        # The maximum number of new connections per second supported by the listener in each zone (virtual IP address). Valid values: **0** to **1000000**. **0** indicates that the number of connections is unlimited.
        self.cps = cps
        # The last port in the listening port range. Valid values: **0** to **65535**. The number of the last port must be smaller than that of the first port.
        self.end_port = end_port
        # The timeout period of an idle connection. Unit: seconds. Valid values: **1** to **900**.
        self.idle_timeout = idle_timeout
        # The name of the listener.
        # 
        # The name must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (_), and hyphens (-).
        self.listener_description = listener_description
        # The ID of the listener.
        self.listener_id = listener_id
        # The listening port. Valid values: **0** to **65535**. A value of **0** specifies all ports. If you set the value to **0**, you must also set the **StartPort** and **EndPort** parameters.
        self.listener_port = listener_port
        # The listening protocol. Valid values: **TCP**, **UDP**, and **TCPSSL**.
        self.listener_protocol = listener_protocol
        # The status of the listener. Valid values:
        # 
        # *   **Provisioning**: The listener is being created.
        # *   **Running**: The listener is running.
        # *   **Configuring**: The listener is being configured.
        # *   **Stopping**: The listener is being stopped.
        # *   **Stopped**: The listener is stopped.
        # *   **Starting**: The listener is being started.
        # *   **Deleting**: The listener is being deleted.
        # *   **Deleted**: The listener is deleted.
        self.listener_status = listener_status
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id
        # The size of the largest TCP segment. Unit: bytes. Valid values: **0** to **1500**. **0** specifies that the maximum segment size remains unchanged.
        # 
        # >  This parameter is supported only by listeners that use SSL over TCP.
        self.mss = mss
        # Indicates whether the Proxy protocol is used to pass client IP addresses to backend servers. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.proxy_protocol_enabled = proxy_protocol_enabled
        # Indicates whether the Proxy protocol passes the VpcId, PrivateLinkEpId, and PrivateLinkEpsId parameters to backend servers.
        self.proxy_protocol_v2config = proxy_protocol_v2config
        # The ID of the region where the NLB instance is deployed.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether fine-grained monitoring is enabled. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.sec_sensor_enabled = sec_sensor_enabled
        # The ID of the security policy. System security policies and custom security policies are supported.
        # 
        # - Valid values: **tls_cipher_policy_1_0**, **tls_cipher_policy_1_1**, **tls_cipher_policy_1_2**, **tls_cipher_policy_1_2_strict**, and **tls_cipher_policy_1_2_strict_with_1_3**.
        # 
        # - Custom security policy: the ID of the custom security policy.
        #     - For more information about how to create a custom security policy, see [CreateSecurityPolicy](https://help.aliyun.com/document_detail/2399231.html) .
        # 
        #     - For more information about how to query security policies, see [ListSecurityPolicy](https://help.aliyun.com/document_detail/2399234.html) .
        # 
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.security_policy_id = security_policy_id
        # The ID of the server group.
        self.server_group_id = server_group_id
        # The first port in the listening port range. Valid values: **0** to **65535**.
        self.start_port = start_port
        # The tags.
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
        ppv_2private_link_ep_id_enabled: bool = None,
        ppv_2private_link_eps_id_enabled: bool = None,
        ppv_2vpc_id_enabled: bool = None,
    ):
        # Indicates whether the Proxy protocol passes the PrivateLinkEpId parameter to backend servers. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.ppv_2private_link_ep_id_enabled = ppv_2private_link_ep_id_enabled
        # Indicates whether the Proxy protocol passes the PrivateLinkEpsId parameter to backend servers. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.ppv_2private_link_eps_id_enabled = ppv_2private_link_eps_id_enabled
        # Indicates whether the Proxy protocol passes the VpcId parameter to backend servers. Valid values:
        # 
        # *   **true**
        # *   **false**
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

