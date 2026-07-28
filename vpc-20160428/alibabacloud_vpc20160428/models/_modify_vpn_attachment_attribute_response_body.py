# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ModifyVpnAttachmentAttributeResponseBody(DaraModel):
    def __init__(
        self,
        attach_instance_id: str = None,
        attach_type: str = None,
        create_time: int = None,
        customer_gateway_id: str = None,
        description: str = None,
        effect_immediately: bool = None,
        enable_dpd: bool = None,
        enable_nat_traversal: bool = None,
        enable_tunnels_bgp: bool = None,
        ike_config: main_models.ModifyVpnAttachmentAttributeResponseBodyIkeConfig = None,
        ipsec_config: main_models.ModifyVpnAttachmentAttributeResponseBodyIpsecConfig = None,
        local_subnet: str = None,
        name: str = None,
        network_type: str = None,
        remote_subnet: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        spec: str = None,
        status: str = None,
        tunnel_options_specification: List[main_models.ModifyVpnAttachmentAttributeResponseBodyTunnelOptionsSpecification] = None,
        vco_health_check: main_models.ModifyVpnAttachmentAttributeResponseBodyVcoHealthCheck = None,
        vpn_bgp_config: main_models.ModifyVpnAttachmentAttributeResponseBodyVpnBgpConfig = None,
        vpn_connection_id: str = None,
        vpn_gateway_id: str = None,
    ):
        # The ID of the Cloud Enterprise Network (CEN) instance to which the transit router (vRouter) associated with the IPsec-VPN connection belongs.
        self.attach_instance_id = attach_instance_id
        # The type of resource that the IPsec-VPN connection is associated with.
        # 
        # - **CEN**: The IPsec-VPN connection is associated with a transit router instance.
        # - **VPNGW**: The IPsec-VPN connection is associated with a VPN gateway instance.
        # - **NO_ASSOCIATED**: The IPsec-VPN connection is not associated with any resource.
        self.attach_type = attach_type
        # The timestamp when the IPsec-VPN connection was created. Unit: milliseconds.
        # 
        # The timestamp follows the UNIX time format, which represents the total number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The ID of the customer gateway associated with the IPsec-VPN connection.
        # 
        # This parameter is returned only for single-tunnel IPsec-VPN connections.
        self.customer_gateway_id = customer_gateway_id
        # The description of the IPsec-VPN connection.
        self.description = description
        # Indicates whether the IPsec-VPN connection configuration takes effect immediately. 
        # 
        # - **true**: The configuration takes effect immediately.
        # - **false**: The configuration does not take effect immediately.
        self.effect_immediately = effect_immediately
        # Indicates whether DPD is enabled for the IPsec-VPN connection.
        # 
        # - **true**: enabled.
        # - **false**: disabled.
        # 
        # This parameter is returned only for single-tunnel IPsec-VPN connections.
        self.enable_dpd = enable_dpd
        # Indicates whether NAT traversal is enabled for the IPsec-VPN connection.
        # 
        # - **true**: enabled.
        # - **false**: disabled.
        # 
        # This parameter is returned only for single-tunnel IPsec-VPN connections.
        self.enable_nat_traversal = enable_nat_traversal
        # The enabling status of tunnel BGP.
        # 
        # - **true**: Enabled.
        # - **false**: Not enabled.
        # 
        # This parameter is returned only for IPsec-VPN connections in dual-tunnel pattern.
        self.enable_tunnels_bgp = enable_tunnels_bgp
        # The Phase 1 negotiation configuration.
        # 
        # The parameters in the **IkeConfig** array are returned only for single-tunnel IPsec-VPN connections.
        self.ike_config = ike_config
        # The Phase 2 negotiation configuration.
        # 
        # The parameters in the **IpsecConfig** array are returned only for single-tunnel IPsec-VPN connections.
        self.ipsec_config = ipsec_config
        # The CIDR block on the Alibaba Cloud side that communicates with the on-premises data center, such as the VPC CIDR block.
        self.local_subnet = local_subnet
        # The name of the IPsec-VPN connection.
        self.name = name
        # The network type of the IPsec-VPN connection.
        # - **public**: public network.
        # - **private**: private network.
        self.network_type = network_type
        # The CIDR block on the on-premises data center side that communicates with Alibaba Cloud.
        self.remote_subnet = remote_subnet
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group to which the IPsec-VPN connection belongs.
        # 
        # You can call [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) to query resource group information.
        self.resource_group_id = resource_group_id
        # The bandwidth specification of the IPsec-VPN connection.
        # 
        # **M** in the return value indicates the unit **Mbps**.
        self.spec = spec
        # The status of the IPsec-VPN connection.
        # 
        # - **ike_sa_not_established**: Phase 1 negotiation failed.
        # 
        # - **ike_sa_established**: Phase 1 negotiation succeeded.
        # 
        # - **ipsec_sa_not_established**: Phase 2 negotiation failed.
        # 
        # - **ipsec_sa_established**: Phase 2 negotiation succeeded.
        self.status = status
        # The tunnel configuration of the IPsec-VPN connection.
        # 
        # The parameters in the **TunnelOptionsSpecification** array are returned only for dual-tunnel IPsec-VPN connections.
        self.tunnel_options_specification = tunnel_options_specification
        # The health check configuration of the IPsec-VPN connection.
        # 
        # The parameters in the **VcoHealthCheck** array are returned only for single-tunnel IPsec-VPN connections.
        self.vco_health_check = vco_health_check
        # The BGP configuration of the IPsec-VPN connection.
        # 
        # The parameters in the **VpnBgpConfig** array are returned only for single-tunnel IPsec-VPN connections.
        self.vpn_bgp_config = vpn_bgp_config
        # The ID of the IPsec-VPN connection.
        self.vpn_connection_id = vpn_connection_id
        # The ID of the VPN gateway instance associated with the IPsec-VPN connection.
        # 
        # **vpn-not-exist**: The IPsec-VPN connection is not associated with a VPN gateway instance.
        self.vpn_gateway_id = vpn_gateway_id

    def validate(self):
        if self.ike_config:
            self.ike_config.validate()
        if self.ipsec_config:
            self.ipsec_config.validate()
        if self.tunnel_options_specification:
            for v1 in self.tunnel_options_specification:
                 if v1:
                    v1.validate()
        if self.vco_health_check:
            self.vco_health_check.validate()
        if self.vpn_bgp_config:
            self.vpn_bgp_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_instance_id is not None:
            result['AttachInstanceId'] = self.attach_instance_id

        if self.attach_type is not None:
            result['AttachType'] = self.attach_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.customer_gateway_id is not None:
            result['CustomerGatewayId'] = self.customer_gateway_id

        if self.description is not None:
            result['Description'] = self.description

        if self.effect_immediately is not None:
            result['EffectImmediately'] = self.effect_immediately

        if self.enable_dpd is not None:
            result['EnableDpd'] = self.enable_dpd

        if self.enable_nat_traversal is not None:
            result['EnableNatTraversal'] = self.enable_nat_traversal

        if self.enable_tunnels_bgp is not None:
            result['EnableTunnelsBgp'] = self.enable_tunnels_bgp

        if self.ike_config is not None:
            result['IkeConfig'] = self.ike_config.to_map()

        if self.ipsec_config is not None:
            result['IpsecConfig'] = self.ipsec_config.to_map()

        if self.local_subnet is not None:
            result['LocalSubnet'] = self.local_subnet

        if self.name is not None:
            result['Name'] = self.name

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.remote_subnet is not None:
            result['RemoteSubnet'] = self.remote_subnet

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.status is not None:
            result['Status'] = self.status

        result['TunnelOptionsSpecification'] = []
        if self.tunnel_options_specification is not None:
            for k1 in self.tunnel_options_specification:
                result['TunnelOptionsSpecification'].append(k1.to_map() if k1 else None)

        if self.vco_health_check is not None:
            result['VcoHealthCheck'] = self.vco_health_check.to_map()

        if self.vpn_bgp_config is not None:
            result['VpnBgpConfig'] = self.vpn_bgp_config.to_map()

        if self.vpn_connection_id is not None:
            result['VpnConnectionId'] = self.vpn_connection_id

        if self.vpn_gateway_id is not None:
            result['VpnGatewayId'] = self.vpn_gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachInstanceId') is not None:
            self.attach_instance_id = m.get('AttachInstanceId')

        if m.get('AttachType') is not None:
            self.attach_type = m.get('AttachType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CustomerGatewayId') is not None:
            self.customer_gateway_id = m.get('CustomerGatewayId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EffectImmediately') is not None:
            self.effect_immediately = m.get('EffectImmediately')

        if m.get('EnableDpd') is not None:
            self.enable_dpd = m.get('EnableDpd')

        if m.get('EnableNatTraversal') is not None:
            self.enable_nat_traversal = m.get('EnableNatTraversal')

        if m.get('EnableTunnelsBgp') is not None:
            self.enable_tunnels_bgp = m.get('EnableTunnelsBgp')

        if m.get('IkeConfig') is not None:
            temp_model = main_models.ModifyVpnAttachmentAttributeResponseBodyIkeConfig()
            self.ike_config = temp_model.from_map(m.get('IkeConfig'))

        if m.get('IpsecConfig') is not None:
            temp_model = main_models.ModifyVpnAttachmentAttributeResponseBodyIpsecConfig()
            self.ipsec_config = temp_model.from_map(m.get('IpsecConfig'))

        if m.get('LocalSubnet') is not None:
            self.local_subnet = m.get('LocalSubnet')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('RemoteSubnet') is not None:
            self.remote_subnet = m.get('RemoteSubnet')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tunnel_options_specification = []
        if m.get('TunnelOptionsSpecification') is not None:
            for k1 in m.get('TunnelOptionsSpecification'):
                temp_model = main_models.ModifyVpnAttachmentAttributeResponseBodyTunnelOptionsSpecification()
                self.tunnel_options_specification.append(temp_model.from_map(k1))

        if m.get('VcoHealthCheck') is not None:
            temp_model = main_models.ModifyVpnAttachmentAttributeResponseBodyVcoHealthCheck()
            self.vco_health_check = temp_model.from_map(m.get('VcoHealthCheck'))

        if m.get('VpnBgpConfig') is not None:
            temp_model = main_models.ModifyVpnAttachmentAttributeResponseBodyVpnBgpConfig()
            self.vpn_bgp_config = temp_model.from_map(m.get('VpnBgpConfig'))

        if m.get('VpnConnectionId') is not None:
            self.vpn_connection_id = m.get('VpnConnectionId')

        if m.get('VpnGatewayId') is not None:
            self.vpn_gateway_id = m.get('VpnGatewayId')

        return self

class ModifyVpnAttachmentAttributeResponseBodyVpnBgpConfig(DaraModel):
    def __init__(
        self,
        enable_bgp: str = None,
        local_asn: int = None,
        local_bgp_ip: str = None,
        peer_asn: int = None,
        peer_bgp_ip: str = None,
        status: str = None,
        tunnel_cidr: str = None,
    ):
        # Indicates whether BGP is enabled for the IPsec-VPN connection.
        # 
        # - **true**: enabled.
        # - **false**: disabled.
        self.enable_bgp = enable_bgp
        # The autonomous system number on the Alibaba Cloud side.
        self.local_asn = local_asn
        # The BGP IP address on the Alibaba Cloud side.
        self.local_bgp_ip = local_bgp_ip
        # The autonomous system number on the on-premises data center side.
        self.peer_asn = peer_asn
        # The BGP IP address on the on-premises data center side.
        self.peer_bgp_ip = peer_bgp_ip
        # The BGP negotiation status.
        # 
        # - **success**: normal.
        # - **false**: abnormal.
        self.status = status
        # The IPsec tunnel CIDR block.
        self.tunnel_cidr = tunnel_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_bgp is not None:
            result['EnableBgp'] = self.enable_bgp

        if self.local_asn is not None:
            result['LocalAsn'] = self.local_asn

        if self.local_bgp_ip is not None:
            result['LocalBgpIp'] = self.local_bgp_ip

        if self.peer_asn is not None:
            result['PeerAsn'] = self.peer_asn

        if self.peer_bgp_ip is not None:
            result['PeerBgpIp'] = self.peer_bgp_ip

        if self.status is not None:
            result['Status'] = self.status

        if self.tunnel_cidr is not None:
            result['TunnelCidr'] = self.tunnel_cidr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableBgp') is not None:
            self.enable_bgp = m.get('EnableBgp')

        if m.get('LocalAsn') is not None:
            self.local_asn = m.get('LocalAsn')

        if m.get('LocalBgpIp') is not None:
            self.local_bgp_ip = m.get('LocalBgpIp')

        if m.get('PeerAsn') is not None:
            self.peer_asn = m.get('PeerAsn')

        if m.get('PeerBgpIp') is not None:
            self.peer_bgp_ip = m.get('PeerBgpIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TunnelCidr') is not None:
            self.tunnel_cidr = m.get('TunnelCidr')

        return self

class ModifyVpnAttachmentAttributeResponseBodyVcoHealthCheck(DaraModel):
    def __init__(
        self,
        dip: str = None,
        enable: str = None,
        interval: int = None,
        policy: str = None,
        retry: int = None,
        sip: str = None,
    ):
        # The destination IP address of the health check.
        self.dip = dip
        # Indicates whether health checks are enabled for the IPsec-VPN connection.
        # 
        # - **true**: enabled.
        # - **false**: disabled.
        self.enable = enable
        # The retry interval of the health check. Unit: seconds.
        self.interval = interval
        # Indicates whether published routes are withdrawn when the health check fails.
        # 
        # - **revoke_route**: Published routes are withdrawn.
        # - **reserve_route**: Published routes are not withdrawn.
        self.policy = policy
        # The number of health check retries.
        self.retry = retry
        # The source IP address of the health check.
        self.sip = sip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dip is not None:
            result['Dip'] = self.dip

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.retry is not None:
            result['Retry'] = self.retry

        if self.sip is not None:
            result['Sip'] = self.sip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dip') is not None:
            self.dip = m.get('Dip')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Retry') is not None:
            self.retry = m.get('Retry')

        if m.get('Sip') is not None:
            self.sip = m.get('Sip')

        return self

class ModifyVpnAttachmentAttributeResponseBodyTunnelOptionsSpecification(DaraModel):
    def __init__(
        self,
        customer_gateway_id: str = None,
        enable_dpd: bool = None,
        enable_nat_traversal: bool = None,
        internet_ip: str = None,
        role: str = None,
        state: str = None,
        tunnel_bgp_config: main_models.ModifyVpnAttachmentAttributeResponseBodyTunnelOptionsSpecificationTunnelBgpConfig = None,
        tunnel_id: str = None,
        tunnel_ike_config: main_models.ModifyVpnAttachmentAttributeResponseBodyTunnelOptionsSpecificationTunnelIkeConfig = None,
        tunnel_index: int = None,
        tunnel_ipsec_config: main_models.ModifyVpnAttachmentAttributeResponseBodyTunnelOptionsSpecificationTunnelIpsecConfig = None,
    ):
        # The customer gateway ID associated with the tunnel.
        self.customer_gateway_id = customer_gateway_id
        # Indicates whether DPD is enabled for the tunnel.
        # 
        # - **true**: enabled.
        # - **false**: disabled.
        self.enable_dpd = enable_dpd
        # Indicates whether NAT traversal is enabled for the tunnel.
        # 
        # - **true**: enabled.
        # - **false**: disabled.
        self.enable_nat_traversal = enable_nat_traversal
        # The gateway IP address on the Alibaba Cloud side of the tunnel.
        self.internet_ip = internet_ip
        # The role of the tunnel.
        # 
        # - **master**: The tunnel is the active tunnel.
        # - **slave**: The tunnel is the standby tunnel.
        self.role = role
        # The status of the tunnel.
        # 
        # - **active**: normal.
        # - **updating**: being updated.
        # - **deleting**: being deleted.
        self.state = state
        # The BGP configuration of the tunnel.
        self.tunnel_bgp_config = tunnel_bgp_config
        # The tunnel ID.
        self.tunnel_id = tunnel_id
        # The configuration of Phase 1 negotiation.
        self.tunnel_ike_config = tunnel_ike_config
        # The creation order of the tunnel.
        # 
        # - **1**: the first tunnel.
        # - **2**: the second tunnel.
        self.tunnel_index = tunnel_index
        # The configuration of Phase 2 negotiation.
        self.tunnel_ipsec_config = tunnel_ipsec_config

    def validate(self):
        if self.tunnel_bgp_config:
            self.tunnel_bgp_config.validate()
        if self.tunnel_ike_config:
            self.tunnel_ike_config.validate()
        if self.tunnel_ipsec_config:
            self.tunnel_ipsec_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_gateway_id is not None:
            result['CustomerGatewayId'] = self.customer_gateway_id

        if self.enable_dpd is not None:
            result['EnableDpd'] = self.enable_dpd

        if self.enable_nat_traversal is not None:
            result['EnableNatTraversal'] = self.enable_nat_traversal

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.role is not None:
            result['Role'] = self.role

        if self.state is not None:
            result['State'] = self.state

        if self.tunnel_bgp_config is not None:
            result['TunnelBgpConfig'] = self.tunnel_bgp_config.to_map()

        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id

        if self.tunnel_ike_config is not None:
            result['TunnelIkeConfig'] = self.tunnel_ike_config.to_map()

        if self.tunnel_index is not None:
            result['TunnelIndex'] = self.tunnel_index

        if self.tunnel_ipsec_config is not None:
            result['TunnelIpsecConfig'] = self.tunnel_ipsec_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerGatewayId') is not None:
            self.customer_gateway_id = m.get('CustomerGatewayId')

        if m.get('EnableDpd') is not None:
            self.enable_dpd = m.get('EnableDpd')

        if m.get('EnableNatTraversal') is not None:
            self.enable_nat_traversal = m.get('EnableNatTraversal')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TunnelBgpConfig') is not None:
            temp_model = main_models.ModifyVpnAttachmentAttributeResponseBodyTunnelOptionsSpecificationTunnelBgpConfig()
            self.tunnel_bgp_config = temp_model.from_map(m.get('TunnelBgpConfig'))

        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')

        if m.get('TunnelIkeConfig') is not None:
            temp_model = main_models.ModifyVpnAttachmentAttributeResponseBodyTunnelOptionsSpecificationTunnelIkeConfig()
            self.tunnel_ike_config = temp_model.from_map(m.get('TunnelIkeConfig'))

        if m.get('TunnelIndex') is not None:
            self.tunnel_index = m.get('TunnelIndex')

        if m.get('TunnelIpsecConfig') is not None:
            temp_model = main_models.ModifyVpnAttachmentAttributeResponseBodyTunnelOptionsSpecificationTunnelIpsecConfig()
            self.tunnel_ipsec_config = temp_model.from_map(m.get('TunnelIpsecConfig'))

        return self

class ModifyVpnAttachmentAttributeResponseBodyTunnelOptionsSpecificationTunnelIpsecConfig(DaraModel):
    def __init__(
        self,
        ipsec_auth_alg: str = None,
        ipsec_enc_alg: str = None,
        ipsec_lifetime: int = None,
        ipsec_pfs: str = None,
    ):
        # The authentication algorithm in the IPsec phase.
        self.ipsec_auth_alg = ipsec_auth_alg
        # The encryption algorithm in the IPsec phase.
        self.ipsec_enc_alg = ipsec_enc_alg
        # The lifetime in the IPsec phase. Unit: seconds.
        self.ipsec_lifetime = ipsec_lifetime
        # The DH group in the IPsec phase.
        self.ipsec_pfs = ipsec_pfs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipsec_auth_alg is not None:
            result['IpsecAuthAlg'] = self.ipsec_auth_alg

        if self.ipsec_enc_alg is not None:
            result['IpsecEncAlg'] = self.ipsec_enc_alg

        if self.ipsec_lifetime is not None:
            result['IpsecLifetime'] = self.ipsec_lifetime

        if self.ipsec_pfs is not None:
            result['IpsecPfs'] = self.ipsec_pfs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpsecAuthAlg') is not None:
            self.ipsec_auth_alg = m.get('IpsecAuthAlg')

        if m.get('IpsecEncAlg') is not None:
            self.ipsec_enc_alg = m.get('IpsecEncAlg')

        if m.get('IpsecLifetime') is not None:
            self.ipsec_lifetime = m.get('IpsecLifetime')

        if m.get('IpsecPfs') is not None:
            self.ipsec_pfs = m.get('IpsecPfs')

        return self

class ModifyVpnAttachmentAttributeResponseBodyTunnelOptionsSpecificationTunnelIkeConfig(DaraModel):
    def __init__(
        self,
        ike_auth_alg: str = None,
        ike_enc_alg: str = None,
        ike_lifetime: int = None,
        ike_mode: str = None,
        ike_pfs: str = None,
        ike_version: str = None,
        local_id: str = None,
        psk: str = None,
        remote_id: str = None,
    ):
        # The authentication algorithm in the IKE phase.
        self.ike_auth_alg = ike_auth_alg
        # The encryption algorithm in the IKE phase.
        self.ike_enc_alg = ike_enc_alg
        # The lifetime in the IKE phase. Unit: seconds.
        self.ike_lifetime = ike_lifetime
        # The negotiation mode of the IKE version. Valid values:
        # 
        # - **main**: Main mode. This mode offers high negotiation security.
        # - **aggressive**: Aggressive mode. This mode supports fast negotiation and a higher success rate.
        self.ike_mode = ike_mode
        # The DH group in the IKE phase.
        self.ike_pfs = ike_pfs
        # The IKE protocol version.
        self.ike_version = ike_version
        # The identifier on the Alibaba Cloud side of the tunnel.
        self.local_id = local_id
        # The pre-shared key.
        self.psk = psk
        # The identifier of the tunnel peer.
        self.remote_id = remote_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ike_auth_alg is not None:
            result['IkeAuthAlg'] = self.ike_auth_alg

        if self.ike_enc_alg is not None:
            result['IkeEncAlg'] = self.ike_enc_alg

        if self.ike_lifetime is not None:
            result['IkeLifetime'] = self.ike_lifetime

        if self.ike_mode is not None:
            result['IkeMode'] = self.ike_mode

        if self.ike_pfs is not None:
            result['IkePfs'] = self.ike_pfs

        if self.ike_version is not None:
            result['IkeVersion'] = self.ike_version

        if self.local_id is not None:
            result['LocalId'] = self.local_id

        if self.psk is not None:
            result['Psk'] = self.psk

        if self.remote_id is not None:
            result['RemoteId'] = self.remote_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IkeAuthAlg') is not None:
            self.ike_auth_alg = m.get('IkeAuthAlg')

        if m.get('IkeEncAlg') is not None:
            self.ike_enc_alg = m.get('IkeEncAlg')

        if m.get('IkeLifetime') is not None:
            self.ike_lifetime = m.get('IkeLifetime')

        if m.get('IkeMode') is not None:
            self.ike_mode = m.get('IkeMode')

        if m.get('IkePfs') is not None:
            self.ike_pfs = m.get('IkePfs')

        if m.get('IkeVersion') is not None:
            self.ike_version = m.get('IkeVersion')

        if m.get('LocalId') is not None:
            self.local_id = m.get('LocalId')

        if m.get('Psk') is not None:
            self.psk = m.get('Psk')

        if m.get('RemoteId') is not None:
            self.remote_id = m.get('RemoteId')

        return self

class ModifyVpnAttachmentAttributeResponseBodyTunnelOptionsSpecificationTunnelBgpConfig(DaraModel):
    def __init__(
        self,
        local_asn: int = None,
        local_bgp_ip: str = None,
        peer_asn: int = None,
        peer_bgp_ip: str = None,
        tunnel_cidr: str = None,
    ):
        # The autonomous system number on the local end (Alibaba Cloud side) of the tunnel.
        # [_single.resp.200.props.TunnelOptionsSpecification.items.TunnelBgpConfig.LocalBgpI
        self.local_asn = local_asn
        # The BGP address on the Alibaba Cloud side of the tunnel.
        self.local_bgp_ip = local_bgp_ip
        # The autonomous system number of the tunnel peer.
        self.peer_asn = peer_asn
        # The BGP address of the tunnel peer.
        self.peer_bgp_ip = peer_bgp_ip
        # The BGP CIDR block of the tunnel.
        self.tunnel_cidr = tunnel_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.local_asn is not None:
            result['LocalAsn'] = self.local_asn

        if self.local_bgp_ip is not None:
            result['LocalBgpIp'] = self.local_bgp_ip

        if self.peer_asn is not None:
            result['PeerAsn'] = self.peer_asn

        if self.peer_bgp_ip is not None:
            result['PeerBgpIp'] = self.peer_bgp_ip

        if self.tunnel_cidr is not None:
            result['TunnelCidr'] = self.tunnel_cidr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalAsn') is not None:
            self.local_asn = m.get('LocalAsn')

        if m.get('LocalBgpIp') is not None:
            self.local_bgp_ip = m.get('LocalBgpIp')

        if m.get('PeerAsn') is not None:
            self.peer_asn = m.get('PeerAsn')

        if m.get('PeerBgpIp') is not None:
            self.peer_bgp_ip = m.get('PeerBgpIp')

        if m.get('TunnelCidr') is not None:
            self.tunnel_cidr = m.get('TunnelCidr')

        return self

class ModifyVpnAttachmentAttributeResponseBodyIpsecConfig(DaraModel):
    def __init__(
        self,
        ipsec_auth_alg: str = None,
        ipsec_enc_alg: str = None,
        ipsec_lifetime: int = None,
        ipsec_pfs: str = None,
    ):
        # The authentication algorithm for Phase 2 negotiation.
        self.ipsec_auth_alg = ipsec_auth_alg
        # The encryption algorithm for Phase 2 negotiation.
        self.ipsec_enc_alg = ipsec_enc_alg
        # The lifetime of the SA negotiated in Phase 2. Unit: seconds.
        self.ipsec_lifetime = ipsec_lifetime
        # The Diffie-Hellman key exchange algorithm used in Phase 2 negotiation.
        self.ipsec_pfs = ipsec_pfs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipsec_auth_alg is not None:
            result['IpsecAuthAlg'] = self.ipsec_auth_alg

        if self.ipsec_enc_alg is not None:
            result['IpsecEncAlg'] = self.ipsec_enc_alg

        if self.ipsec_lifetime is not None:
            result['IpsecLifetime'] = self.ipsec_lifetime

        if self.ipsec_pfs is not None:
            result['IpsecPfs'] = self.ipsec_pfs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpsecAuthAlg') is not None:
            self.ipsec_auth_alg = m.get('IpsecAuthAlg')

        if m.get('IpsecEncAlg') is not None:
            self.ipsec_enc_alg = m.get('IpsecEncAlg')

        if m.get('IpsecLifetime') is not None:
            self.ipsec_lifetime = m.get('IpsecLifetime')

        if m.get('IpsecPfs') is not None:
            self.ipsec_pfs = m.get('IpsecPfs')

        return self

class ModifyVpnAttachmentAttributeResponseBodyIkeConfig(DaraModel):
    def __init__(
        self,
        ike_auth_alg: str = None,
        ike_enc_alg: str = None,
        ike_lifetime: int = None,
        ike_mode: str = None,
        ike_pfs: str = None,
        ike_version: str = None,
        local_id: str = None,
        psk: str = None,
        remote_id: str = None,
    ):
        # The authentication algorithm for Phase 1 negotiation.
        self.ike_auth_alg = ike_auth_alg
        # The encryption algorithm for Phase 1 negotiation.
        self.ike_enc_alg = ike_enc_alg
        # The lifetime of the SA negotiated in Phase 1. Unit: seconds.
        self.ike_lifetime = ike_lifetime
        # The IKE negotiation mode.
        # 
        # - **main**: main mode. The negotiation process is highly secure.
        # - **aggressive**: aggressive mode. The negotiation is fast and has a high success rate.
        self.ike_mode = ike_mode
        # The Diffie-Hellman key exchange algorithm used in Phase 1 negotiation.
        self.ike_pfs = ike_pfs
        # The IKE protocol version.
        # 
        # - **ikev1**
        # - **ikev2**
        # 
        # Compared with IKEv1, IKEv2 simplifies the SA negotiation process and provides better support for multi-CIDR-block scenarios.
        self.ike_version = ike_version
        # The identifier on the Alibaba Cloud side of the IPsec-VPN connection.
        self.local_id = local_id
        # The pre-shared key used for identity authentication between the Alibaba Cloud IPsec-VPN connection and the on-premises data center.
        # 
        # > The pre-shared key on the IPsec-VPN connection side must be the same as the authentication key on the on-premises data center side. Otherwise, a connection cannot be established between the on-premises data center and the VPN gateway.
        self.psk = psk
        # The identifier on the on-premises data center side of the IPsec-VPN connection.
        self.remote_id = remote_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ike_auth_alg is not None:
            result['IkeAuthAlg'] = self.ike_auth_alg

        if self.ike_enc_alg is not None:
            result['IkeEncAlg'] = self.ike_enc_alg

        if self.ike_lifetime is not None:
            result['IkeLifetime'] = self.ike_lifetime

        if self.ike_mode is not None:
            result['IkeMode'] = self.ike_mode

        if self.ike_pfs is not None:
            result['IkePfs'] = self.ike_pfs

        if self.ike_version is not None:
            result['IkeVersion'] = self.ike_version

        if self.local_id is not None:
            result['LocalId'] = self.local_id

        if self.psk is not None:
            result['Psk'] = self.psk

        if self.remote_id is not None:
            result['RemoteId'] = self.remote_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IkeAuthAlg') is not None:
            self.ike_auth_alg = m.get('IkeAuthAlg')

        if m.get('IkeEncAlg') is not None:
            self.ike_enc_alg = m.get('IkeEncAlg')

        if m.get('IkeLifetime') is not None:
            self.ike_lifetime = m.get('IkeLifetime')

        if m.get('IkeMode') is not None:
            self.ike_mode = m.get('IkeMode')

        if m.get('IkePfs') is not None:
            self.ike_pfs = m.get('IkePfs')

        if m.get('IkeVersion') is not None:
            self.ike_version = m.get('IkeVersion')

        if m.get('LocalId') is not None:
            self.local_id = m.get('LocalId')

        if m.get('Psk') is not None:
            self.psk = m.get('Psk')

        if m.get('RemoteId') is not None:
            self.remote_id = m.get('RemoteId')

        return self

