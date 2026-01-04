# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ModifyVpnConnectionAttributeRequest(DaraModel):
    def __init__(
        self,
        auto_config_route: bool = None,
        bgp_config: str = None,
        client_token: str = None,
        effect_immediately: bool = None,
        enable_dpd: bool = None,
        enable_nat_traversal: bool = None,
        enable_tunnels_bgp: bool = None,
        health_check_config: str = None,
        ike_config: str = None,
        ipsec_config: str = None,
        local_subnet: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        remote_ca_certificate: str = None,
        remote_subnet: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tunnel_options_specification: List[main_models.ModifyVpnConnectionAttributeRequestTunnelOptionsSpecification] = None,
        vpn_connection_id: str = None,
    ):
        # Specifies whether to automatically advertise routes. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.auto_config_route = auto_config_route
        # This parameter is supported if you modify the configurations of an IPsec-VPN connection in single-tunnel mode.
        # 
        # BGP configuration:
        # 
        # *   **BgpConfig.EnableBgp**: specifies whether to enable BGP. Valid values: **true** and **false**.
        # 
        # *   **BgpConfig.LocalAsn:** the autonomous system number (ASN) on the Alibaba Cloud side. Valid values: **1** to **4294967295**.
        # 
        #     You can enter a value in two segments separated by a period (.). Each segment is 16 bits in length. Enter the number in each segment in decimal format.
        # 
        #     For example, if you enter 123.456, the ASN is 8061384. The ASN is calculated by using the following formula: 123 × 65536 + 456 = 8061384.
        # 
        # *   **BgpConfig.TunnelCidr**: The CIDR block of the IPsec tunnel. The CIDR block must fall within 169.254.0.0/16 and the mask of the CIDR block must be 30 bits in length. The CIDR block cannot be 169.254.0.0/30, 169.254.1.0/30, 169.254.2.0/30, 169.254.3.0/30, 169.254.4.0/30, 169.254.5.0/30, 169.254.6.0/30, or 169.254.169.252/30.
        # 
        #     > The CIDR block of the IPsec tunnel for each IPsec-VPN connection on a VPN gateway must be unique.
        # 
        # *   **LocalBgpIp**: the BGP address on the Alibaba Cloud side. It must be an IP address that falls within the CIDR block of the IPsec tunnel.
        # 
        # > - This parameter is required when the VPN gateway has dynamic BGP enabled.
        # > - Before you add BGP configurations, we recommend that you learn about how BGP dynamic routing works and the limits. For more information, see [Configure BGP dynamic routing](https://help.aliyun.com/document_detail/2638220.html).
        # > - We recommend that you use a private ASN to establish BGP connections to Alibaba Cloud. For information about the range of private ASNs, see the relevant documentation.
        self.bgp_config = bgp_config
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the value of **RequestId** as the value of **ClientToken**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to immediately start IPsec negotiations after the configuration takes effect. Valid values:
        # 
        # *   **true**: immediately starts IPsec negotiations after the configuration takes effect.
        # *   **false**: IPsec negotiations start when inbound traffic is detected.
        self.effect_immediately = effect_immediately
        # You can specify this parameter if you modify the configuration of a single-tunnel IPsec-VPN connection.
        # 
        # Specifies whether to enable the dead peer detection (DPD) feature. Valid values:
        # 
        # *   **true:**: enables the DPD feature. The initiator of the IPsec-VPN connection sends DPD packets to check the existence and availability of the peer. If no feedback is received from the peer within a specific period of time, the connection fails. Then, the ISAKMP SA, IPsec SA, and IPsec tunnel are deleted.
        # *   **false**: disables the DPD feature. The initiator of the IPsec-VPN connection does not send DPD packets.
        self.enable_dpd = enable_dpd
        # You can specify this parameter if you modify the configuration of a single-tunnel IPsec-VPN connection.
        # 
        # Specifies whether to enable NAT traversal. Valid values:
        # 
        # *   **true** After NAT traversal is enabled, the initiator does not check the UDP ports during IKE negotiations and can automatically discover NAT gateway devices along the IPsec tunnel.
        # *   **false**
        self.enable_nat_traversal = enable_nat_traversal
        # You can specify this parameter if you modify the configuration of a dual-tunnel IPsec-VPN connection.
        # 
        # Specifies whether to enable BGP for the tunnel. Valid values: **true** and **false**.
        self.enable_tunnels_bgp = enable_tunnels_bgp
        # You can specify this parameter if you modify the configuration of a single-tunnel IPsec-VPN connection.
        # 
        # The health check configuration:
        # 
        # *   **HealthCheckConfig.enable**: specifies whether to enable health checks. Valid values: **true** and **false**.
        # *   **HealthCheckConfig.dip**: the destination IP address that is used for health checks.
        # *   **HealthCheckConfig.sip**: the source IP address that is used for health checks.
        # *   **HealthCheckConfig.interval**: the interval between two consecutive health checks. Unit: seconds.
        # *   **HealthCheckConfig.retry**: the maximum number of health check retries.
        self.health_check_config = health_check_config
        # This parameter is supported if you modify the configurations of an IPsec-VPN connection in single-tunnel mode.
        # 
        # The configurations of Phase 1 negotiations:
        # 
        # *   **IkeConfig.Psk**: The pre-shared key that is used for identity authentication between the VPN gateway and the on-premises data center.
        # 
        #     *   The key cannot contain space characters. The key must be 1 to 100 characters in length, and can contain digits, letters, and the following special characters: ``~!`@#$%^&*()_-+={}[]|;:\\",.<>/?``
        #     *   If you do not specify a pre-shared key, the system randomly generates a 16-bit string as the pre-shared key. You can call the [DescribeVpnConnection](https://help.aliyun.com/document_detail/2526951.html) operation to query the pre-shared key that is automatically generated by the system.
        # 
        #     > The pre-shared key of the IPsec-VPN connection must be the same as the authentication key of the on-premises data center. Otherwise, connections between the on-premises data center and the VPN gateway cannot be established.
        # 
        # *   **IkeConfig.IkeVersion**: the version of the Internet Key Exchange (IKE) protocol. Valid values: **ikev1** and **ikev2**.
        # 
        #     Compared with IKEv1, IKEv2 simplifies the security association (SA) negotiation process and provides better support for scenarios with multiple CIDR blocks.
        # 
        # *   **IkeConfig.IkeMode**: the negotiation mode of IKE. Valid values: **main** and **aggressive**.
        # 
        #     *   **main:** This mode offers higher security during negotiations.
        #     *   **aggressive:** This mode supports faster negotiations and a higher success rate.
        # 
        # *   **IkeConfig.IkeEncAlg**: the encryption algorithm that is used in Phase 1 negotiations.
        # 
        #     Valid values: **aes**, **aes192**, **aes256**, **des**, and **3des**.
        # 
        # *   **IkeConfig.IkeAuthAlg**: the authentication algorithm that is used in Phase 1 negotiations.
        # 
        #     Valid values: **md5**, **sha1**, **sha256**, **sha384**, and **sha512**.
        # 
        # *   **IkeConfig.IkePfs**: the Diffie-Hellman key exchange algorithm that is used in Phase 1 negotiations. Valid values: **group1**, **group2**, **group5**, and **group14**.
        # 
        # *   **IkeConfig.IkeLifetime**: the SA lifetime as a result of Phase 1 negotiations. Unit: seconds Valid values: **0 to 86400**.
        # 
        # *   **IkeConfig.LocalId**: the identifier of the VPN gateway. The identifier cannot exceed 100 characters in length and cannot contain space characters. The default value is the IP address of the VPN gateway.
        # 
        # *   **IkeConfig.RemoteId**: the identifier of the customer gateway. The identifier cannot exceed 100 characters in length and cannot contain space characters. The default value is the IP address of the customer gateway.
        self.ike_config = ike_config
        # You can specify this parameter if you modify the configuration of a single-tunnel IPsec-VPN connection.
        # 
        # The configuration of Phase 2 negotiations:
        # 
        # *   **IpsecConfig.IpsecEncAlg**: the encryption algorithm that is used in Phase 2 negotiations.
        # 
        #     Valid values: **aes**, **aes192**, **aes256**, **des**, and **3des**.
        # 
        # *   **IpsecConfig. IpsecAuthAlg**: the authentication algorithm that is used in Phase 2 negotiations.
        # 
        #     Valid values: **md5**, **sha1**, **sha256**, **sha384**, and **sha512**.
        # 
        # *   **IpsecConfig. IpsecPfs**: the DH key exchange algorithm that is used in Phase 1 negotiations. If you specify this parameter, packets of all protocols are forwarded. Valid values: **disabled**, **group1**, **group2**, **group5**, and **group14**.
        # 
        # *   **IpsecConfig. IpsecLifetime:** the SA lifetime that is determined by Phase 2 negotiations. Unit: seconds. Valid values: **0 to 86400**.
        self.ipsec_config = ipsec_config
        # The CIDR block used to connect the virtual private cloud (VPC) to the data center. The CIDR block is used in Phase 2 negotiations.
        # 
        # Separate multiple CIDR blocks with commas (,). Example: 192.168.1.0/24,192.168.2.0/24.
        # 
        # The following routing modes are supported:
        # 
        # *   If you set **LocalSubnet** and **RemoteSubnet** to 0.0.0.0/0, the routing mode of the IPsec-VPN connection is set to Destination Routing Mode.
        # *   If you set **LocalSubnet** and **RemoteSubnet** to specific CIDR blocks, the routing mode of the IPsec-VPN connection is set to Protected Data Flows.
        self.local_subnet = local_subnet
        # The name of the IPsec-VPN connection.
        # 
        # The name must be 1 to 100 characters in length and cannot start with `http://` or `https://`.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region in which the IPsec-VPN connection is created.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # You can specify this parameter if you modify the configuration of a single-tunnel IPsec-VPN connection.
        # 
        # If the VPN gateway uses a ShangMi (SM) certificate, you can modify the CA certificate used by the IPsec peer.
        # 
        # If the VPN gateway does not use an SM certificate, you cannot specify this parameter.
        self.remote_ca_certificate = remote_ca_certificate
        # The CIDR block on the data center side. This CIDR block is used in Phase 2 negotiations.
        # 
        # Separate multiple CIDR blocks with commas (,). Example: 192.168.3.0/24,192.168.4.0/24.
        # 
        # The following routing modes are supported:
        # 
        # *   If you set **LocalSubnet** and **RemoteSubnet** to 0.0.0.0/0, the routing mode of the IPsec-VPN connection is set to Destination Routing Mode.
        # *   If you set **LocalSubnet** and **RemoteSubnet** to specific CIDR blocks, the routing mode of the IPsec-VPN connection is set to Protected Data Flows.
        self.remote_subnet = remote_subnet
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tunnel configurations.
        # 
        # You can specify parameters in the **TunnelOptionsSpecification** array when you modify the configurations of an IPsec-VPN connection in dual-tunnel mode. You can modify the configurations of both the active and standby tunnels of the IPsec-VPN connection.
        self.tunnel_options_specification = tunnel_options_specification
        # The ID of the IPsec-VPN connection.
        # 
        # This parameter is required.
        self.vpn_connection_id = vpn_connection_id

    def validate(self):
        if self.tunnel_options_specification:
            for v1 in self.tunnel_options_specification:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_config_route is not None:
            result['AutoConfigRoute'] = self.auto_config_route

        if self.bgp_config is not None:
            result['BgpConfig'] = self.bgp_config

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.effect_immediately is not None:
            result['EffectImmediately'] = self.effect_immediately

        if self.enable_dpd is not None:
            result['EnableDpd'] = self.enable_dpd

        if self.enable_nat_traversal is not None:
            result['EnableNatTraversal'] = self.enable_nat_traversal

        if self.enable_tunnels_bgp is not None:
            result['EnableTunnelsBgp'] = self.enable_tunnels_bgp

        if self.health_check_config is not None:
            result['HealthCheckConfig'] = self.health_check_config

        if self.ike_config is not None:
            result['IkeConfig'] = self.ike_config

        if self.ipsec_config is not None:
            result['IpsecConfig'] = self.ipsec_config

        if self.local_subnet is not None:
            result['LocalSubnet'] = self.local_subnet

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remote_ca_certificate is not None:
            result['RemoteCaCertificate'] = self.remote_ca_certificate

        if self.remote_subnet is not None:
            result['RemoteSubnet'] = self.remote_subnet

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['TunnelOptionsSpecification'] = []
        if self.tunnel_options_specification is not None:
            for k1 in self.tunnel_options_specification:
                result['TunnelOptionsSpecification'].append(k1.to_map() if k1 else None)

        if self.vpn_connection_id is not None:
            result['VpnConnectionId'] = self.vpn_connection_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoConfigRoute') is not None:
            self.auto_config_route = m.get('AutoConfigRoute')

        if m.get('BgpConfig') is not None:
            self.bgp_config = m.get('BgpConfig')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EffectImmediately') is not None:
            self.effect_immediately = m.get('EffectImmediately')

        if m.get('EnableDpd') is not None:
            self.enable_dpd = m.get('EnableDpd')

        if m.get('EnableNatTraversal') is not None:
            self.enable_nat_traversal = m.get('EnableNatTraversal')

        if m.get('EnableTunnelsBgp') is not None:
            self.enable_tunnels_bgp = m.get('EnableTunnelsBgp')

        if m.get('HealthCheckConfig') is not None:
            self.health_check_config = m.get('HealthCheckConfig')

        if m.get('IkeConfig') is not None:
            self.ike_config = m.get('IkeConfig')

        if m.get('IpsecConfig') is not None:
            self.ipsec_config = m.get('IpsecConfig')

        if m.get('LocalSubnet') is not None:
            self.local_subnet = m.get('LocalSubnet')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemoteCaCertificate') is not None:
            self.remote_ca_certificate = m.get('RemoteCaCertificate')

        if m.get('RemoteSubnet') is not None:
            self.remote_subnet = m.get('RemoteSubnet')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tunnel_options_specification = []
        if m.get('TunnelOptionsSpecification') is not None:
            for k1 in m.get('TunnelOptionsSpecification'):
                temp_model = main_models.ModifyVpnConnectionAttributeRequestTunnelOptionsSpecification()
                self.tunnel_options_specification.append(temp_model.from_map(k1))

        if m.get('VpnConnectionId') is not None:
            self.vpn_connection_id = m.get('VpnConnectionId')

        return self

class ModifyVpnConnectionAttributeRequestTunnelOptionsSpecification(DaraModel):
    def __init__(
        self,
        customer_gateway_id: str = None,
        enable_dpd: bool = None,
        enable_nat_traversal: bool = None,
        remote_ca_certificate: str = None,
        role: str = None,
        tunnel_bgp_config: main_models.ModifyVpnConnectionAttributeRequestTunnelOptionsSpecificationTunnelBgpConfig = None,
        tunnel_id: str = None,
        tunnel_ike_config: main_models.ModifyVpnConnectionAttributeRequestTunnelOptionsSpecificationTunnelIkeConfig = None,
        tunnel_ipsec_config: main_models.ModifyVpnConnectionAttributeRequestTunnelOptionsSpecificationTunnelIpsecConfig = None,
    ):
        # The ID of the customer gateway associated with the tunnel.
        self.customer_gateway_id = customer_gateway_id
        # Specifies whether to enable the Dead Peer Detection (DPD) feature for the tunnel. Valid values:
        # 
        # *   **true**: enables DPD. The initiator of the IPsec-VPN connection sends DPD packets to check the existence and availability of the peer. If no feedback is received from the peer within the specified period of time, the connection fails. In this case, ISAKMP SA and IPsec SA are deleted. The security tunnel is also deleted.
        # *   **false**: disables DPD. The initiator of the IPsec-VPN connection does not send DPD packets.
        self.enable_dpd = enable_dpd
        # Specifies whether to enable NAT traversal for the tunnel. Valid values:
        # 
        # *   **true**: enables NAT traversal. After NAT traversal is enabled, the initiator does not check the UDP ports during IKE negotiations and can automatically discover NAT gateway devices along the IPsec-VPN tunnel.
        # *   **false**: disables NAT traversal.
        self.enable_nat_traversal = enable_nat_traversal
        # If the VPN gateway uses an SM certificate, you can modify the CA certificate used by the IPsec peer.
        # 
        # If the VPN gateway does not use an SM certificate, this parameter is not supported.
        self.remote_ca_certificate = remote_ca_certificate
        # The tunnel role. Valid values:
        # 
        # *   **master**: The tunnel is an active tunnel.
        # *   **slave**: The tunnel is a standby tunnel.
        self.role = role
        # The Border Gateway Protocol (BGP) configurations of the tunnel.
        self.tunnel_bgp_config = tunnel_bgp_config
        # The tunnel ID.
        self.tunnel_id = tunnel_id
        # The configurations of Phase 1 negotiations.
        self.tunnel_ike_config = tunnel_ike_config
        # The configurations of Phase 2 negotiations.
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

        if self.remote_ca_certificate is not None:
            result['RemoteCaCertificate'] = self.remote_ca_certificate

        if self.role is not None:
            result['Role'] = self.role

        if self.tunnel_bgp_config is not None:
            result['TunnelBgpConfig'] = self.tunnel_bgp_config.to_map()

        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id

        if self.tunnel_ike_config is not None:
            result['TunnelIkeConfig'] = self.tunnel_ike_config.to_map()

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

        if m.get('RemoteCaCertificate') is not None:
            self.remote_ca_certificate = m.get('RemoteCaCertificate')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('TunnelBgpConfig') is not None:
            temp_model = main_models.ModifyVpnConnectionAttributeRequestTunnelOptionsSpecificationTunnelBgpConfig()
            self.tunnel_bgp_config = temp_model.from_map(m.get('TunnelBgpConfig'))

        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')

        if m.get('TunnelIkeConfig') is not None:
            temp_model = main_models.ModifyVpnConnectionAttributeRequestTunnelOptionsSpecificationTunnelIkeConfig()
            self.tunnel_ike_config = temp_model.from_map(m.get('TunnelIkeConfig'))

        if m.get('TunnelIpsecConfig') is not None:
            temp_model = main_models.ModifyVpnConnectionAttributeRequestTunnelOptionsSpecificationTunnelIpsecConfig()
            self.tunnel_ipsec_config = temp_model.from_map(m.get('TunnelIpsecConfig'))

        return self

class ModifyVpnConnectionAttributeRequestTunnelOptionsSpecificationTunnelIpsecConfig(DaraModel):
    def __init__(
        self,
        ipsec_auth_alg: str = None,
        ipsec_enc_alg: str = None,
        ipsec_lifetime: int = None,
        ipsec_pfs: str = None,
    ):
        # The authentication algorithm that is used in Phase 2 negotiations.
        # 
        # Valid values: **md5**, **sha1**, **sha256**, **sha384**, and **sha512**.
        self.ipsec_auth_alg = ipsec_auth_alg
        # The encryption algorithm that is used in Phase 2 negotiations.
        # 
        # Valid values: **aes**, **aes192**, **aes256**, **des**, and **3des**.
        self.ipsec_enc_alg = ipsec_enc_alg
        # The SA lifetime as a result of Phase 2 negotiations. Unit: seconds Valid values: **0** to **86400**.
        self.ipsec_lifetime = ipsec_lifetime
        # The Diffie-Hellman key exchange algorithm that is used in Phase 2 negotiations.
        # 
        # Valid values: **disabled**, **group1**, **group2**, **group5**, and **group14**.
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

class ModifyVpnConnectionAttributeRequestTunnelOptionsSpecificationTunnelIkeConfig(DaraModel):
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
        # The authentication algorithm that is used in Phase 1 negotiations.
        # 
        # Valid values: **md5**, **sha1**, **sha256**, **sha384**, and **sha512**.
        self.ike_auth_alg = ike_auth_alg
        # The encryption algorithm that is used in Phase 1 negotiations.
        # 
        # Valid values: **aes**, **aes192**, **aes256**, **des**, and **3des**.
        self.ike_enc_alg = ike_enc_alg
        # The SA lifetime as a result of Phase 1 negotiations. Unit: seconds Valid values: **0** to **86400**.
        self.ike_lifetime = ike_lifetime
        # The negotiation mode of IKE. Valid values:
        # 
        # *   **main:** This mode offers higher security during negotiations.
        # *   **aggressive:** This mode supports faster negotiations and a higher success rate.
        self.ike_mode = ike_mode
        # The Diffie-Hellman key exchange algorithm that is used in Phase 1 negotiations. Valid values: **group1**, **group2**, **group5**, and **group14**.
        self.ike_pfs = ike_pfs
        # The version of the IKE protocol. Valid values: **ikev1** and **ikev2**.
        # 
        # Compared with IKEv1, IKEv2 simplifies the SA negotiation process and provides better support for scenarios with multiple CIDR blocks.
        self.ike_version = ike_version
        # The identifier on the Alibaba Cloud side, which is used in Phase 1 negotiations. The identifier cannot exceed 100 characters in length and cannot contain space characters. The default value is the IP address of the tunnel.
        # 
        # **LocalId** supports fully qualified domain names (FQDNs). If you use an FQDN, we recommend that you set the negotiation mode to **aggressive**.
        self.local_id = local_id
        # The pre-shared key, which is used for identity authentication between the tunnel and the tunnel peer.
        # 
        # *   The key cannot contain space characters. The key must be 1 to 100 characters in length, and can contain digits, letters, and the following special characters: ``~!\\`@#$%^&*()_-+={}[]|;:\\",.<>/?``
        # *   If you do not specify a pre-shared key, the system randomly generates a 16-bit string as the pre-shared key. You can call the [DescribeVpnConnection](https://help.aliyun.com/document_detail/2526951.html) operation to query the pre-shared key that is automatically generated by the system.
        # 
        # >  The tunnel and the tunnel peer must use the same pre-shared key. Otherwise, the tunnel cannot be built.
        self.psk = psk
        # The identifier of the tunnel peer, which is used in Phase 1 negotiations. The identifier cannot exceed 100 characters in length and cannot contain space characters. The default value is the IP address of the customer gateway that is associated with the tunnel.
        # 
        # **RemoteId** supports FQDNs. If you use an FQDN, we recommend that you set the negotiation mode to **aggressive**.
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

class ModifyVpnConnectionAttributeRequestTunnelOptionsSpecificationTunnelBgpConfig(DaraModel):
    def __init__(
        self,
        local_asn: int = None,
        local_bgp_ip: str = None,
        tunnel_cidr: str = None,
    ):
        # The ASN of the tunnel on the Alibaba Cloud side. Valid values: **1** to **4294967295**. Default value: **45104**.
        # 
        # >  You can specify this parameter only if **EnableTunnelsBgp** is set to **true**.
        # 
        # *   Before you add BGP configurations, we recommend that you learn about how BGP dynamic routing works and the limits. For more information, see [Configure BGP dynamic routing](https://help.aliyun.com/document_detail/2638220.html).
        # 
        # *   We recommend that you use a private ASN to establish BGP connections to Alibaba Cloud. For information about the range of private ASNs, see the relevant documentation.
        self.local_asn = local_asn
        # The BGP IP address of the tunnel on the Alibaba Cloud side. The address is an IP address that falls within the BGP CIDR block.
        self.local_bgp_ip = local_bgp_ip
        # The BGP CIDR block of the tunnel.
        # 
        # The CIDR block must fall within 169.254.0.0/16 and the mask of the CIDR block must be 30 bits in length. The CIDR block cannot be 169.254.0.0/30, 169.254.1.0/30, 169.254.2.0/30, 169.254.3.0/30, 169.254.4.0/30, 169.254.5.0/30, 169.254.6.0/30, or 169.254.169.252/30.
        # 
        # >  The BGP CIDR block of each tunnel must be unique on a VPN gateway.
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

        if self.tunnel_cidr is not None:
            result['TunnelCidr'] = self.tunnel_cidr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalAsn') is not None:
            self.local_asn = m.get('LocalAsn')

        if m.get('LocalBgpIp') is not None:
            self.local_bgp_ip = m.get('LocalBgpIp')

        if m.get('TunnelCidr') is not None:
            self.tunnel_cidr = m.get('TunnelCidr')

        return self

