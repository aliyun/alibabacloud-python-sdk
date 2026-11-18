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
        # Specifies whether to automatically publish route entry. Valid values:
        # 
        # - **true**: Automatically publishes route entry.
        #    
        # - **false**: Does not automatically publish route entry.
        self.auto_config_route = auto_config_route
        # This parameter is supported when you modify an IPsec-VPN connection in single-tunnel pattern.
        # 
        # The BGP configurations:
        # 
        # - **BgpConfig.EnableBgp**: Specifies whether to enable the BGP feature. Valid values: **true** and **false**.
        # 
        # - **BgpConfig.LocalAsn**: The autonomous system number (ASN) on the Alibaba Cloud side. Valid values: **1** to **4294967295**.  
        # 
        #    You can enter the ASN in a two-part format: the first 16 bits and the last 16 bits, separated by a period. Each part must be entered in decimal format.
        # 
        #     For example, if you enter 123.456, the ASN is calculated as follows: 123 × 65536 + 456 = 8061384.
        # 
        # - **BgpConfig.TunnelCidr**: The CIDR block of the IPsec tunnel. The CIDR block must be a subnet with a mask length of 30 within 169.254.0.0/16, and cannot be 169.254.0.0/30, 169.254.1.0/30, 169.254.2.0/30, 169.254.3.0/30, 169.254.4.0/30, 169.254.5.0/30, 169.254.6.0/30, or 169.254.169.252/30.
        # 
        #     > The IPsec tunnel CIDR block of each IPsec-VPN connection under the same VPN gateway instance must be unique.
        # 
        # - **LocalBgpIp**: The BGP IP address on the Alibaba Cloud side. This IP address must be within the IPsec tunnel CIDR block. 
        # 
        # > - This parameter is required when the BGP dynamic routing feature is enabled for the VPN gateway.
        # > - Before adding BGP configurations, understand the working mechanism and limits of BGP dynamic routing. For more information, see [Configure BGP dynamic routing](https://help.aliyun.com/document_detail/2638220.html).
        # > - Use a private ASN to establish a BGP connection with Alibaba Cloud. Refer to relevant documentation for the range of private ASNs.
        self.bgp_config = bgp_config
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is unique.
        self.client_token = client_token
        # Specifies whether the configurations of the IPsec-VPN connection take effect immediately. Valid values:
        #            
        # - **true**: Yes. The system immediately initiates IPsec negotiations after the configurations are completed.
        #    
        # - **false**: No. The system initiates IPsec negotiations only when traffic is detected.
        self.effect_immediately = effect_immediately
        # This parameter is supported when you modify an IPsec-VPN connection in single-tunnel mode.
        # 
        # Specifies whether to enable the dead peer detection (DPD) feature. Valid values:
        # 
        # - **true**: Enables the DPD feature. The IPsec initiator sends DPD packets to check whether the peer device is alive. If no correct response is received within the specified time, the peer is considered disconnected. IPsec deletes the ISAKMP SA and the corresponding IPsec SA, and the secure tunnel is also deleted.
        # 
        # - **false**: Disables the DPD feature. The IPsec initiator does not send DPD probe packets.
        self.enable_dpd = enable_dpd
        # This parameter is supported when you modify an IPsec-VPN connection in single-tunnel mode.
        # 
        # Specifies whether to enable the NAT traversal feature. Valid values:
        # 
        # - **true**: Enables the NAT traversal feature. After this feature is enabled, the IKE negotiation process skips the verification of UDP port numbers and discovers NAT gateway devices in the VPN tunnel.
        # 
        # - **false**: Disables the NAT traversal feature.
        self.enable_nat_traversal = enable_nat_traversal
        # This parameter is supported when you modify an IPsec-VPN connection in dual-tunnel mode.
        # 
        # Specifies whether to enable the BGP feature for the tunnel. Valid values: **true** and **false**.
        self.enable_tunnels_bgp = enable_tunnels_bgp
        # This parameter is supported when you modify an IPsec-VPN connection in single-tunnel mode.
        # 
        # The health check configurations:
        # 
        # - **HealthCheckConfig.enable**: Specifies whether to enable health checks. Valid values: **true** and **false**.
        # 
        # - **HealthCheckConfig.dip**: The destination IP address for health checks.
        # 
        # - **HealthCheckConfig.sip**: The source IP address for health checks.
        # 
        # - **HealthCheckConfig.interval**: The retry interval for health checks. Unit: seconds.
        # 
        # - **HealthCheckConfig.retry**: The maximum number of health check retries.
        self.health_check_config = health_check_config
        # This parameter is supported when you modify an IPsec-VPN connection in single-tunnel mode.
        # 
        # The configurations for Phase 1 negotiations: 
        #            
        # - **IkeConfig.Psk**: The pre-shared key used for authentication between the VPN gateway and the data center.
        # 
        #     - The key must be 1 to 100 characters in length and can contain digits, letters, and the following special characters: ```~!`@#$%^&*()_-+={}[]|;:\\",.<>/?``` It cannot contain spaces.
        #     - If you do not specify a pre-shared key, the system randomly generates a 16-character string as the pre-shared key. You can call the [DescribeVpnConnection](https://help.aliyun.com/document_detail/2526951.html) operation to query the automatically generated pre-shared key.
        #     > The pre-shared key on the IPsec-VPN connection side must be the same as the authentication key on the data center side. Otherwise, the connection between the data center and the VPN gateway cannot be established. 
        # 
        # - **IkeConfig.IkeVersion**: The version of the IKE protocol. Valid values: **ikev1** and **ikev2**. 
        # 
        #     Compared with IKEv1, IKEv2 simplifies the SA negotiation process and provides better support for multi-CIDR block scenarios.
        # 
        #     <props="china"><ph>If the VPN gateway is a ShangMi (SM) gateway, only **ikev1** is supported.</ph>
        # 
        # - **IkeConfig.IkeMode**: The negotiation mode of the IKE version. Valid values: **main** and **aggressive**.   
        #     - **main**: The main mode. The negotiation process is highly secure.
        #     - **aggressive**: The aggressive mode. The negotiation process is fast and has a high success rate.
        # 
        #     <props="china"><ph>If the VPN gateway is an SM gateway, only **main** is supported.</ph>
        # 
        # - **IkeConfig.IkeEncAlg**: The encryption algorithm used in Phase 1 negotiations.
        # 
        #     <props="intl"><ph>Valid values: **aes**, **aes192**, **aes256**, **des**, and **3des**.</ph>
        # 
        #     <props="china"><ph>If the VPN gateway is a standard gateway, valid values are **aes**, **aes192**, **aes256**, **des**, and **3des**.</ph>
        # 
        #     <props="china"><ph>If the VPN gateway is an SM gateway, the only valid value is **sm4**.</ph>
        # 
        # - **IkeConfig.IkeAuthAlg**: The authentication algorithm used in Phase 1 negotiations.
        # 
        #     <props="intl"><ph>Valid values: **md5**, **sha1**, **sha256**, **sha384**, and **sha512**.</ph>
        # 
        #     <props="china"><ph>If the VPN gateway is a standard gateway, valid values are **md5**, **sha1**, **sha256**, **sha384**, and **sha512**.</ph>
        # 
        #     <props="china"><ph>If the VPN gateway is an SM gateway, the only valid value is **sm3**.</ph>
        # 
        # - **IkeConfig.IkePfs**: The Diffie-Hellman key exchange algorithm used in Phase 1 negotiations. Valid values: **group1**, **group2**, **group5**, and **group14**.
        # 
        # - **IkeConfig.IkeLifetime**: The SA lifetime determined by Phase 1 negotiations. Unit: seconds. Valid values: **0** to **86400**.
        # 
        # - **IkeConfig.LocalId**: The identifier of the VPN gateway. The identifier can be up to 100 characters in length and cannot contain spaces. The default value is the IP address of the VPN gateway. 
        # 
        # - **IkeConfig.RemoteId**: The identifier of the customer gateway. The identifier can be up to 100 characters in length and cannot contain spaces. The default value is the IP address of the customer gateway.
        self.ike_config = ike_config
        # This parameter is supported when you modify an IPsec-VPN connection in single-tunnel mode.
        # 
        # The configurations for Phase 2 negotiations: 
        # 
        # - **IpsecConfig.IpsecEncAlg**: The encryption algorithm used in Phase 2 negotiations.
        # 
        #     <props="intl"><ph>Valid values: **aes**, **aes192**, **aes256**, **des**, and **3des**.</ph>
        # 
        #     <props="china"><ph>If the VPN gateway is a standard gateway, valid values are **aes**, **aes192**, **aes256**, **des**, and **3des**.</ph>
        # 
        #     <props="china"><ph>If the VPN gateway is an SM gateway, the only valid value is **sm4**.</ph>
        # 
        # - **IpsecConfig.IpsecAuthAlg**: The authentication algorithm used in Phase 2 negotiations.
        # 
        #     <props="intl"><ph>Valid values: **md5**, **sha1**, **sha256**, **sha384**, and **sha512**.</ph>
        # 
        #     <props="china"><ph>If the VPN gateway is a standard gateway, valid values are **md5**, **sha1**, **sha256**, **sha384**, and **sha512**.</ph>
        # 
        #     <props="china"><ph>If the VPN gateway is an SM gateway, the only valid value is **sm3**.</ph>
        # 
        # - **IpsecConfig.IpsecPfs**: The Diffie-Hellman key exchange algorithm used in Phase 1 negotiations for forwarding packets of all protocols. Valid values: **disabled**, **group1**, **group2**, **group5**, and **group14**.   
        # 
        # - **IpsecConfig.IpsecLifetime**: The SA lifetime determined by Phase 2 negotiations. Unit: seconds. Valid values: **0** to **86400**.
        self.ipsec_config = ipsec_config
        # The CIDR block on the VPC side that needs to communicate with the data center. This parameter is used for Phase 2 negotiations.
        # 
        # Separate multiple CIDR blocks with commas (,). Example: 192.168.1.0/24,192.168.2.0/24.
        # 
        # Routing modes of the IPsec-VPN connection:
        # 
        # - If both **LocalSubnet** and **RemoteSubnet** are set to 0.0.0.0/0, the destination routing mode is used.
        # - If both **LocalSubnet** and **RemoteSubnet** are set to specific CIDR blocks, the interested traffic mode is used.
        self.local_subnet = local_subnet
        # The name of the IPsec-VPN connection.  
        # 
        # The name must be 1 to 100 characters in length, and cannot start with `http://` or `https://`.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the IPsec-VPN connection. 
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # This parameter is supported when you modify an IPsec-VPN connection in single-tunnel mode.
        # 
        # If the current VPN gateway is an SM VPN gateway, you can modify the CA certificate of the peer.
        # 
        # If the current VPN gateway is a standard VPN gateway, this parameter is not supported.
        self.remote_ca_certificate = remote_ca_certificate
        # The CIDR block on the data center side. This parameter is used for Phase 2 negotiations.
        # 
        # Separate multiple CIDR blocks with commas (,). Example: 192.168.3.0/24,192.168.4.0/24.
        # 
        # Routing modes of the IPsec-VPN connection:
        # 
        # - If both **LocalSubnet** and **RemoteSubnet** are set to 0.0.0.0/0, the destination routing mode is used.
        # - If both **LocalSubnet** and **RemoteSubnet** are set to specific CIDR blocks, the interested traffic mode is used.
        self.remote_subnet = remote_subnet
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tunnel configurations.
        # 
        # The parameters in the **TunnelOptionsSpecification** array are supported only when you modify an IPsec-VPN connection in dual-tunnel mode. You can modify the configurations of both the primary and secondary tunnels of the IPsec-VPN connection at the same time.
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
        # The instance ID of the customer gateway instance associated with the tunnel.
        self.customer_gateway_id = customer_gateway_id
        # Specifies whether to enable the dead peer detection (DPD) feature for the tunnel. Valid values:
        # 
        # - **true**: Enables the DPD feature. The IPsec initiator sends DPD packets to check whether the peer device is alive. If no correct response is received within the specified time, the peer is considered disconnected. IPsec deletes the ISAKMP SA and the corresponding IPsec SA, and the secure tunnel is also deleted.
        # 
        # - **false**: Disables the DPD feature. The IPsec initiator does not send DPD probe packets.
        self.enable_dpd = enable_dpd
        # Specifies whether to enable the NAT traversal feature for the tunnel. Valid values:
        # 
        # - **true**: Enables the NAT traversal feature. After this feature is enabled, the IKE negotiation process skips the verification of UDP port numbers and discovers NAT gateway devices in the VPN tunnel.
        # 
        # - **false**: Disables the NAT traversal feature.
        self.enable_nat_traversal = enable_nat_traversal
        # If the current VPN gateway is an SM VPN gateway, you can modify the CA certificate of the peer for the tunnel.
        # 
        # If the current VPN gateway is a standard VPN gateway, this parameter is not supported.
        self.remote_ca_certificate = remote_ca_certificate
        # The role of the tunnel.
        # 
        # - **master**: The current tunnel is the primary tunnel.
        # - **slave**: The current tunnel is the secondary tunnel.
        self.role = role
        # The BGP configurations of the tunnel.
        self.tunnel_bgp_config = tunnel_bgp_config
        # The ID of the tunnel.
        self.tunnel_id = tunnel_id
        # The configurations for Phase 1 negotiations.
        self.tunnel_ike_config = tunnel_ike_config
        # The configurations for Phase 2 negotiations.
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
        # The authentication algorithm used in Phase 2 negotiations.
        # 
        # <props="intl"><ph>Valid values: **md5**, **sha1**, **sha256**, **sha384**, and **sha512**.</ph>
        # 
        # <props="china"><ph>If the VPN gateway is a standard gateway, valid values are **md5**, **sha1**, **sha256**, **sha384**, and **sha512**.</ph>
        # 
        # <props="china"><ph>If the VPN gateway is an SM gateway, the only valid value is **sm3**.</ph>
        self.ipsec_auth_alg = ipsec_auth_alg
        # The encryption algorithm used in Phase 2 negotiations.
        # 
        # <props="intl"><ph>Valid values: **aes**, **aes192**, **aes256**, **des**, and **3des**.</ph>
        # 
        # <props="china"><ph>If the VPN gateway is a standard gateway, valid values are **aes**, **aes192**, **aes256**, **des**, and **3des**.</ph>
        # 
        # <props="china"><ph>If the VPN gateway is an SM gateway, the only valid value is **sm4**.</ph>
        self.ipsec_enc_alg = ipsec_enc_alg
        # The SA lifetime determined by Phase 2 negotiations. Unit: seconds. Valid values: **0** to **86400**.
        self.ipsec_lifetime = ipsec_lifetime
        # The Diffie-Hellman key exchange algorithm used in Phase 2 negotiations.
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
        # The authentication algorithm used in Phase 1 negotiations.
        # 
        # <props="intl"><ph>Valid values: **md5**, **sha1**, **sha256**, **sha384**, and **sha512**.</ph>
        # 
        # <props="china"><ph>If the VPN gateway is a standard gateway, valid values are **md5**, **sha1**, **sha256**, **sha384**, and **sha512**.</ph>
        # 
        # <props="china"><ph>If the VPN gateway is an SM gateway, the only valid value is **sm3**.</ph>
        self.ike_auth_alg = ike_auth_alg
        # The encryption algorithm used in Phase 1 negotiations.
        # 
        # <props="intl"><ph>Valid values: **aes**, **aes192**, **aes256**, **des**, and **3des**.</ph>
        # 
        # <props="china"><ph>If the VPN gateway is a standard gateway, valid values are **aes**, **aes192**, **aes256**, **des**, and **3des**.</ph>
        # 
        # <props="china"><ph>If the VPN gateway is an SM gateway, the only valid value is **sm4**.</ph>
        self.ike_enc_alg = ike_enc_alg
        # The SA lifetime determined by Phase 1 negotiations. Unit: seconds. Valid values: **0** to **86400**.
        self.ike_lifetime = ike_lifetime
        # The negotiation mode of the IKE version. Valid values:
        # 
        # - **main**: The main mode. The negotiation process is highly secure.
        # - **aggressive**: The aggressive mode. The negotiation process is fast and has a high success rate.
        # 
        # <props="china"><ph>If the VPN gateway is an SM gateway, only **main** is supported.</ph>
        self.ike_mode = ike_mode
        # The Diffie-Hellman key exchange algorithm used in Phase 1 negotiations. Valid values: **group1**, **group2**, **group5**, and **group14**.
        self.ike_pfs = ike_pfs
        # The version of the IKE protocol. Valid values: **ikev1** and **ikev2**.
        # 
        # Compared with IKEv1, IKEv2 simplifies the SA negotiation process and provides better support for multi-CIDR block scenarios.
        # 
        # <props="china"><ph>If the VPN gateway is an SM gateway, only **ikev1** is supported.</ph>
        self.ike_version = ike_version
        # The identifier on the Alibaba Cloud side of the tunnel, which is used for Phase 1 negotiations. The identifier can be up to 100 characters in length and cannot contain spaces. The default value is the IP address of the tunnel.
        # 
        # **LocalId** supports the FQDN format. If you use the FQDN format, set the negotiation mode to **aggressive**.
        self.local_id = local_id
        # The pre-shared key used for authentication between the tunnel and the peer.
        # 
        # - The key must be 1 to 100 characters in length and can contain digits, letters, and the following special characters: ```~!`@#$%^&*()_-+={}[]|;:\\",.<>/?``` It cannot contain spaces.
        # 
        # - If you do not specify a pre-shared key, the system randomly generates a 16-character string as the pre-shared key. You can call the [DescribeVpnConnection](https://help.aliyun.com/document_detail/2526951.html) operation to query the automatically generated pre-shared key.     
        # 
        # > The pre-shared key of the tunnel must be the same as that of the peer. Otherwise, the system cannot establish the tunnel.
        self.psk = psk
        # The identifier of the peer, which is used for Phase 1 negotiations. The identifier can be up to 100 characters in length and cannot contain spaces. The default value is the IP address of the customer gateway associated with the tunnel.
        # 
        # **RemoteId** supports the FQDN format. If you use the FQDN format, set the negotiation mode to **aggressive**.
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
        # The autonomous system number (ASN) on the Alibaba Cloud side of the tunnel. Valid values: **1** to **4294967295**. Default value: **45104**.
        # 
        # > - This parameter can be configured or modified only after you enable the BGP feature for the IPsec-VPN connection (that is, set **EnableTunnelsBgp** to **true**).
        # > - Before adding BGP configurations, understand the working mechanism and limits of BGP dynamic routing. For more information, see [Configure BGP dynamic routing](https://help.aliyun.com/document_detail/2638220.html).
        # > - Use a private ASN to establish a BGP connection with Alibaba Cloud. Refer to relevant documentation for the range of private ASNs.
        self.local_asn = local_asn
        # The BGP IP address on the Alibaba Cloud side of the tunnel. This IP address must be within the BGP CIDR block.
        self.local_bgp_ip = local_bgp_ip
        # The BGP CIDR block of the tunnel.
        # 
        # The CIDR block must be a subnet with a mask length of 30 within 169.254.0.0/16, and cannot be 169.254.0.0/30, 169.254.1.0/30, 169.254.2.0/30, 169.254.3.0/30, 169.254.4.0/30, 169.254.5.0/30, 169.254.6.0/30, or 169.254.169.252/30.
        # 
        # > The BGP CIDR block of each tunnel under the same VPN gateway instance must be unique.
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

