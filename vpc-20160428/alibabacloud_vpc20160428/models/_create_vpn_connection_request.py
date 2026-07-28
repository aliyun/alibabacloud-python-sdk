# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateVpnConnectionRequest(DaraModel):
    def __init__(
        self,
        auto_config_route: bool = None,
        bgp_config: str = None,
        client_token: str = None,
        customer_gateway_id: str = None,
        dry_run: bool = None,
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
        tags: List[main_models.CreateVpnConnectionRequestTags] = None,
        tunnel_options_specification: List[main_models.CreateVpnConnectionRequestTunnelOptionsSpecification] = None,
        vpn_gateway_id: str = None,
    ):
        # Specifies whether to automatically configure routes. Valid values:
        # 
        # - **true** (default): Routes are automatically configured.
        # 
        # - **false**: Routes are not automatically configured.
        self.auto_config_route = auto_config_route
        # This parameter is supported when you create an IPsec-VPN connection in single-tunnel mode.
        # 
        # The BGP configuration:
        # 
        # - **BgpConfig.EnableBgp**: Specifies whether to enable the BGP feature. Valid values: **true** and **false** (default).
        # - **BgpConfig.LocalAsn**: The autonomous system number on the Alibaba Cloud side. Valid values: **1** to **4294967295**. Default value: **45104**.
        #     
        #     You can enter the autonomous system number in the two-segment format: the first 16 bits.the last 16 bits. Enter each segment in decimal format.
        #     
        #     For example, if you enter 123.456, the autonomous system number is 123 × 65536 + 456 = 8061384.
        # - **BgpConfig.TunnelCidr**: The CIDR block of the IPsec tunnel. The CIDR block must be a CIDR block with a mask length of 30 within 169.254.0.0/16 and cannot be 169.254.0.0/30, 169.254.1.0/30, 169.254.2.0/30, 169.254.3.0/30, 169.254.4.0/30, 169.254.5.0/30, 169.254.6.0/30, or 169.254.169.252/30.
        #     > The IPsec tunnel CIDR block of each IPsec-VPN connection under a VPN gateway instance must be unique.
        # - **LocalBgpIp**: The BGP address on the Alibaba Cloud side. This address is an IP address within the IPsec tunnel CIDR block. 
        # 
        # > - Before you configure BGP, learn about how the BGP dynamic routing feature works and its limits. For more information, see [Configure BGP dynamic routing](https://help.aliyun.com/document_detail/2638220.html).
        # > - Use a private autonomous system number to establish a BGP connection with Alibaba Cloud. Refer to the relevant documentation for the range of private autonomous system numbers.
        self.bgp_config = bgp_config
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # This parameter is supported and required when you create an IPsec-VPN connection in single-tunnel mode.
        # 
        # The ID of the customer gateway.
        self.customer_gateway_id = customer_gateway_id
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # - **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # - **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, the IPsec-VPN connection is created.
        self.dry_run = dry_run
        # Specifies whether the IPsec-VPN connection configuration takes effect immediately. Valid values:
        #            
        # - **true**: The system immediately initiates IPsec protocol negotiation after the configuration is complete.
        #    
        # - **false** (default): The system initiates IPsec protocol negotiation only when inbound traffic is detected.
        self.effect_immediately = effect_immediately
        # This parameter is supported when you create an IPsec-VPN connection in single-tunnel mode.
        # 
        # Specifies whether to enable the Dead Peer Detection (DPD) feature. Valid values:
        # 
        # - **true** (default): DPD is enabled. The IPsec initiator sends DPD packets to check whether the peer device is alive. If no correct response is received within the specified period, the peer is considered disconnected. The ISAKMP SA and the corresponding IPsec SA are deleted, and the security tunnel is also deleted.
        # 
        # - **false**: DPD is disabled. The IPsec initiator does not send DPD probe packets.
        self.enable_dpd = enable_dpd
        # This parameter is supported when you create an IPsec-VPN connection in single-tunnel mode.
        # 
        # Specifies whether to enable the NAT traversal feature. Valid values:
        # 
        # - **true** (default): NAT traversal is enabled. After NAT traversal is enabled, the IKE negotiation process removes the verification of the UDP port number and can discover NAT gateway devices in the VPN tunnel.
        # 
        # - **false**: NAT traversal is disabled.
        self.enable_nat_traversal = enable_nat_traversal
        # This parameter is supported when you create an IPsec-VPN connection in dual-tunnel mode.
        # 
        # Specifies whether to enable BGP for the tunnels. Valid values: **true** and **false** (default).
        self.enable_tunnels_bgp = enable_tunnels_bgp
        # This parameter is supported when you create an IPsec-VPN connection in single-tunnel mode.
        # 
        # The health check configuration:
        # 
        # - **HealthCheckConfig.enable**: Specifies whether to enable health checks. Valid values: **true** and **false** (default).
        # 
        # - **HealthCheckConfig.dip**: The destination IP address of the health check.
        # 
        # - **HealthCheckConfig.sip**: The source IP address of the health check.
        # 
        # - **HealthCheckConfig.interval**: The retry interval of the health check. Unit: seconds. Default value: **3**.
        # 
        # - **HealthCheckConfig.retry**: The number of retries for the health check. Default value: **3**.
        self.health_check_config = health_check_config
        # This parameter is supported when you create an IPsec-VPN connection in single-tunnel mode.
        # 
        # The Phase 1 negotiation configuration:
        #            
        # - **IkeConfig.Psk**: The pre-shared key used for identity authentication between the VPN gateway and the on-premises data center.
        # 
        #     - The key must be 1 to 100 characters in length and can contain digits, uppercase and lowercase letters, and the following characters. It cannot contain spaces. ```~!\\`@#$%^&*()_-+={}[]|;:\\",.<>/?```
        #     - If you do not specify a pre-shared key, the system generates a random string as the pre-shared key. You can call the [DescribeVpnConnection](https://help.aliyun.com/document_detail/2526951.html) operation to query the pre-shared key that is automatically generated by the system.     
        # 
        #         > The pre-shared key on the IPsec-VPN connection side must be the same as the authentication key on the on-premises data center side. Otherwise, the connection between the on-premises data center and the VPN gateway cannot be established.
        # 
        # - **IkeConfig.IkeVersion**: The version of the IKE protocol. Valid values: **ikev1** and **ikev2**. Default value: **ikev1**.  
        # 
        #     Compared with IKEv1, IKEv2 simplifies the SA negotiation process and provides better support for multi-CIDR-block scenarios.
        # 
        #    <props="china"><ph>If the VPN gateway instance type is China Certified Cryptography, only **ikev1** is supported for the IKE version.</ph>
        # 
        # - **IkeConfig.IkeMode**: The negotiation mode of the IKE version. Valid values: **main** and **aggressive**. Default value: **main**.   
        # 
        #     - **main**: Main mode. The negotiation process is highly secure.
        #     - **aggressive**: Aggressive mode. The negotiation is fast and has a high success rate.
        # 
        #    <props="china"><ph>If the VPN gateway instance type is China Certified Cryptography, only **main** is supported for the negotiation mode.</ph>
        # 
        # - **IkeConfig.IkeEncAlg**: The encryption algorithm used in Phase 1 negotiation.
        # 
        #    <props="intl"><ph>Valid values: **aes**, **aes192**, **aes256**, **des**, and **3des**. Default value: **aes**. </ph>
        # 
        #    <props="china">If the VPN gateway instance type is Standard, valid values are **aes**, **aes192**, **aes256**, **des**, and **3des**. Default value: **aes**.
        # 
        #    <props="china"><ph>If the VPN gateway instance type is China Certified Cryptography, the value is **sm4** (default).</ph>
        # 
        # - **IkeConfig.IkeAuthAlg**: The authentication algorithm used in Phase 1 negotiation.
        # 
        #    <props="intl"><ph>Valid values: **md5**, **sha1**, **sha256**, **sha384**, and **sha512**. Default value: **md5**.</ph>
        # 
        #    <props="china"><ph>If the VPN gateway instance type is Standard, valid values: **md5**, **sha1**, **sha256**, **sha384**, and **sha512**. Default value: **md5**.</ph>
        # 
        #    <props="china"><ph>If the VPN gateway instance type is China Certified Cryptography, the value is **sm3** (default).</ph>
        # 
        # - **IkeConfig.IkePfs**: The Diffie-Hellman key exchange algorithm used in Phase 1 negotiation. Valid values: **group1**, **group2**, **group5**, and **group14**. Default value: **group2**.   
        # 
        # - **IkeConfig.IkeLifetime**: The lifetime of the SA negotiated in Phase 1. Unit: seconds. Valid values: **0** to **86400**. Default value: **86400**.   
        # 
        # - **IkeConfig.LocalId**: The identifier of the VPN gateway. The identifier can be up to 100 characters in length and cannot contain spaces. The default value is the IP address of the VPN gateway. 
        # 
        # - **IkeConfig.RemoteId**: The identifier of the customer gateway. The identifier can be up to 100 characters in length and cannot contain spaces. The default value is the IP address of the customer gateway.
        self.ike_config = ike_config
        # This parameter is supported when you create an IPsec-VPN connection in single-tunnel mode.
        # 
        # The Phase 2 negotiation configuration: 
        # 
        # - **IpsecConfig.IpsecEncAlg**: The encryption algorithm used in Phase 2 negotiation.
        # 
        #    <props="intl"><ph>Valid values: **aes**, **aes192**, **aes256**, **des**, and **3des**. Default value: **aes**. </ph>
        # 
        #    <props="china"><ph>If the VPN gateway instance type is Standard, valid values are **aes**, **aes192**, **aes256**, **des**, and **3des**. Default value: **aes**.</ph>
        # 
        #    <props="china"><ph>If the VPN gateway instance type is China Certified Cryptography, the value is **sm4** (default).</ph>
        # 
        # - **IpsecConfig. IpsecAuthAlg**: The authentication algorithm used in Phase 2 negotiation.
        # 
        #    <props="intl"><ph>Valid values: **md5**, **sha1**, **sha256**, **sha384**, and **sha512**. Default value: **md5**.</ph>
        # 
        #    <props="china"><ph>If the VPN gateway instance type is Standard, valid values: **md5**, **sha1**, **sha256**, **sha384**, and **sha512**. Default value: **md5**.</ph>
        # 
        #    <props="china"><ph>If the VPN gateway instance type is China Certified Cryptography, the value is **sm3** (default).</ph>
        # 
        # - **IpsecConfig. IpsecPfs**: The Diffie-Hellman key exchange algorithm used in Phase 2 negotiation. Valid values: **disabled**, **group1**, **group2**, **group5**, and **group14**. Default value: **group2**.   
        # 
        # - **IpsecConfig. IpsecLifetime**: The lifetime of the SA negotiated in Phase 2. Unit: seconds. Valid values: **0** to **86400**. Default value: **86400**.
        self.ipsec_config = ipsec_config
        # The CIDR block on the VPC side that needs to communicate with the on-premises data center. This CIDR block is used in Phase 2 negotiation.
        # 
        # Separate multiple CIDR blocks with commas (,). Example: 192.168.1.0/24,192.168.2.0/24.
        # 
        # The following routing modes are supported for IPsec-VPN connections:
        # 
        # - If both **LocalSubnet** and **RemoteSubnet** are set to 0.0.0.0/0, the destination routing mode is used.
        # - If both **LocalSubnet** and **RemoteSubnet** are set to specific CIDR blocks, the protected data flow mode is used.
        # 
        # This parameter is required.
        self.local_subnet = local_subnet
        # The name of the IPsec-VPN connection.
        # 
        # The name must be 1 to 100 characters in length and cannot start with `http://` or `https://`.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the IPsec-VPN connection. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # This parameter is supported when you create an IPsec-VPN connection in single-tunnel mode.
        # 
        # If the current VPN gateway instance is a China Certified Cryptography VPN gateway, you must configure the peer CA certificate.
        # 
        # - For a China Certified Cryptography VPN gateway, this parameter is required when you create an IPsec-VPN connection.
        # 
        # - For a Standard VPN gateway, this parameter must be left empty.
        self.remote_ca_certificate = remote_ca_certificate
        # The CIDR block on the on-premises data center side that needs to communicate with the VPC. This CIDR block is used in Phase 2 negotiation.
        # 
        # Separate multiple CIDR blocks with commas (,). Example: 192.168.3.0/24,192.168.4.0/24.
        # 
        # The following routing modes are supported for IPsec-VPN connections:
        # 
        # - If both **LocalSubnet** and **RemoteSubnet** are set to 0.0.0.0/0, the destination routing mode is used.
        # - If both **LocalSubnet** and **RemoteSubnet** are set to specific CIDR blocks, the protected data flow mode is used.
        # 
        # This parameter is required.
        self.remote_subnet = remote_subnet
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of tags to add to the IPsec-VPN connection.
        # 
        # You can add up to 20 tags to an IPsec-VPN connection at a time.
        self.tags = tags
        # The tunnel configurations.
        # 
        # - The parameters under the **TunnelOptionsSpecification** array are supported when you create an IPsec-VPN connection in dual-tunnel mode.
        # - When you create an IPsec-VPN connection in dual-tunnel mode, you must configure both the active tunnel and the standby tunnel for the IPsec-VPN connection. Only two tunnels (active and standby) can be added to an IPsec-VPN connection.
        self.tunnel_options_specification = tunnel_options_specification
        # The instance ID of the VPN gateway.
        # 
        # This parameter is required.
        self.vpn_gateway_id = vpn_gateway_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
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

        if self.customer_gateway_id is not None:
            result['CustomerGatewayId'] = self.customer_gateway_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

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

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        result['TunnelOptionsSpecification'] = []
        if self.tunnel_options_specification is not None:
            for k1 in self.tunnel_options_specification:
                result['TunnelOptionsSpecification'].append(k1.to_map() if k1 else None)

        if self.vpn_gateway_id is not None:
            result['VpnGatewayId'] = self.vpn_gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoConfigRoute') is not None:
            self.auto_config_route = m.get('AutoConfigRoute')

        if m.get('BgpConfig') is not None:
            self.bgp_config = m.get('BgpConfig')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CustomerGatewayId') is not None:
            self.customer_gateway_id = m.get('CustomerGatewayId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

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

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateVpnConnectionRequestTags()
                self.tags.append(temp_model.from_map(k1))

        self.tunnel_options_specification = []
        if m.get('TunnelOptionsSpecification') is not None:
            for k1 in m.get('TunnelOptionsSpecification'):
                temp_model = main_models.CreateVpnConnectionRequestTunnelOptionsSpecification()
                self.tunnel_options_specification.append(temp_model.from_map(k1))

        if m.get('VpnGatewayId') is not None:
            self.vpn_gateway_id = m.get('VpnGatewayId')

        return self

class CreateVpnConnectionRequestTunnelOptionsSpecification(DaraModel):
    def __init__(
        self,
        customer_gateway_id: str = None,
        enable_dpd: bool = None,
        enable_nat_traversal: bool = None,
        remote_ca_certificate: str = None,
        role: str = None,
        tunnel_bgp_config: main_models.CreateVpnConnectionRequestTunnelOptionsSpecificationTunnelBgpConfig = None,
        tunnel_ike_config: main_models.CreateVpnConnectionRequestTunnelOptionsSpecificationTunnelIkeConfig = None,
        tunnel_ipsec_config: main_models.CreateVpnConnectionRequestTunnelOptionsSpecificationTunnelIpsecConfig = None,
    ):
        # The ID of the customer gateway associated with the tunnel.
        # 
        # > - This parameter is required when you create an IPsec-VPN connection in dual-tunnel mode.
        # > - The parameters under the **TunnelOptionsSpecification** array are supported when you create an IPsec-VPN connection in dual-tunnel mode.
        # > - When you create an IPsec-VPN connection in dual-tunnel mode, you must configure both the active tunnel and the standby tunnel for the IPsec-VPN connection. Only two tunnels (active and standby) can be added to an IPsec-VPN connection.
        self.customer_gateway_id = customer_gateway_id
        # Specifies whether to enable the Dead Peer Detection (DPD) feature for the tunnel. Valid values:
        # 
        # - **true** (default): DPD is enabled. The IPsec initiator sends DPD packets to check whether the peer device is alive. If no correct response is received within the specified period, the peer is considered disconnected. The ISAKMP SA and the corresponding IPsec SA are deleted, and the security tunnel is also deleted.
        # 
        # - **false**: DPD is disabled. The IPsec initiator does not send DPD probe packets.
        self.enable_dpd = enable_dpd
        # Specifies whether to enable the NAT traversal feature for the tunnel. Valid values:
        # 
        # - **true** (default): NAT traversal is enabled. After NAT traversal is enabled, the IKE negotiation process removes the verification of the UDP port number and can discover NAT gateway devices in the tunnel.
        # 
        # - **false**: NAT traversal is disabled.
        self.enable_nat_traversal = enable_nat_traversal
        # If the current VPN gateway instance is a China Certified Cryptography VPN gateway, you must configure the peer CA certificate for the tunnel.
        # 
        # - For a China Certified Cryptography VPN gateway, this parameter is required.
        # 
        # - For a Standard VPN gateway, this parameter must be left empty.
        self.remote_ca_certificate = remote_ca_certificate
        # The role of the tunnel. Valid values:
        # 
        # - **master**: The tunnel is the active tunnel.
        # - **slave**: The tunnel is the standby tunnel.
        self.role = role
        # The BGP configuration for the tunnel.
        self.tunnel_bgp_config = tunnel_bgp_config
        # The Phase 1 negotiation configuration.
        self.tunnel_ike_config = tunnel_ike_config
        # The Phase 2 negotiation configuration.
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
            temp_model = main_models.CreateVpnConnectionRequestTunnelOptionsSpecificationTunnelBgpConfig()
            self.tunnel_bgp_config = temp_model.from_map(m.get('TunnelBgpConfig'))

        if m.get('TunnelIkeConfig') is not None:
            temp_model = main_models.CreateVpnConnectionRequestTunnelOptionsSpecificationTunnelIkeConfig()
            self.tunnel_ike_config = temp_model.from_map(m.get('TunnelIkeConfig'))

        if m.get('TunnelIpsecConfig') is not None:
            temp_model = main_models.CreateVpnConnectionRequestTunnelOptionsSpecificationTunnelIpsecConfig()
            self.tunnel_ipsec_config = temp_model.from_map(m.get('TunnelIpsecConfig'))

        return self

class CreateVpnConnectionRequestTunnelOptionsSpecificationTunnelIpsecConfig(DaraModel):
    def __init__(
        self,
        ipsec_auth_alg: str = None,
        ipsec_enc_alg: str = None,
        ipsec_lifetime: int = None,
        ipsec_pfs: str = None,
    ):
        # The authentication algorithm used in Phase 2 negotiation.
        # 
        # <props="intl"><ph>Valid values: **md5**, **sha1**, **sha256**, **sha384**, and **sha512**. Default value: **md5**.</ph>
        # 
        # <props="china"><ph>If the VPN gateway instance type is Standard, valid values: **md5**, **sha1**, **sha256**, **sha384**, and **sha512**. Default value: **md5**.</ph>
        # 
        # <props="china"><ph>If the VPN gateway instance type is China Certified Cryptography, the value is **sm3** (default).</ph>
        self.ipsec_auth_alg = ipsec_auth_alg
        # The encryption algorithm used in Phase 2 negotiation.
        # 
        # <props="intl"><ph>Valid values: **aes**, **aes192**, **aes256**, **des**, and **3des**. Default value: **aes**. </ph>
        # 
        # <props="china"><ph>If the VPN gateway instance type is Standard, valid values are **aes**, **aes192**, **aes256**, **des**, and **3des**. Default value: **aes**.</ph>
        # 
        # <props="china"><ph>If the VPN gateway instance type is China Certified Cryptography, the value is **sm4** (default).</ph>
        self.ipsec_enc_alg = ipsec_enc_alg
        # The lifetime of the SA negotiated in Phase 2. Unit: seconds.
        # 
        # Valid values: **0** to **86400**. Default value: **86400**.
        self.ipsec_lifetime = ipsec_lifetime
        # The Diffie-Hellman key exchange algorithm used in Phase 2 negotiation. Default value: **group2**.   
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

class CreateVpnConnectionRequestTunnelOptionsSpecificationTunnelIkeConfig(DaraModel):
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
        # The authentication algorithm used in Phase 1 negotiation.
        # 
        # <props="intl"><ph>Valid values: **md5**, **sha1**, **sha256**, **sha384**, and **sha512**. Default value: **md5**.</ph>
        # 
        # <props="china"><ph>If the VPN gateway instance type is Standard, valid values: **md5**, **sha1**, **sha256**, **sha384**, and **sha512**. Default value: **md5**.</ph>
        # 
        # <props="china"><ph>If the VPN gateway instance type is China Certified Cryptography, the value is **sm3** (default).</ph>
        self.ike_auth_alg = ike_auth_alg
        # The encryption algorithm used in Phase 1 negotiation.
        # 
        # <props="intl"><ph>Valid values: **aes**, **aes192**, **aes256**, **des**, and **3des**. Default value: **aes**. </ph>
        # 
        # <props="china"><ph>If the VPN gateway instance type is Standard, valid values are **aes**, **aes192**, **aes256**, **des**, and **3des**. Default value: **aes**.</ph>
        # 
        # <props="china"><ph>If the VPN gateway instance type is China Certified Cryptography, the value is **sm4** (default).</ph>
        self.ike_enc_alg = ike_enc_alg
        # The lifetime of the SA negotiated in Phase 1. Unit: seconds.
        # 
        # Valid values: **0** to **86400**. Default value: **86400**.
        self.ike_lifetime = ike_lifetime
        # The negotiation mode of the IKE version. Valid values: **main** and **aggressive**. Default value: **main**.   
        # 
        # - **main**: Main mode. The negotiation process is highly secure.
        # - **aggressive**: Aggressive mode. The negotiation is fast and has a high success rate.
        # 
        # <props="china"><ph>If the VPN gateway instance type is China Certified Cryptography, only **main** is supported for the negotiation mode.</ph>
        self.ike_mode = ike_mode
        # The Diffie-Hellman key exchange algorithm used in Phase 1 negotiation. Default value: **group2**.   
        # Valid values: **group1**, **group2**, **group5**, and **group14**.
        self.ike_pfs = ike_pfs
        # The version of the IKE protocol. Valid values: **ikev1** and **ikev2**. Default value: **ikev1**.
        # 
        # Compared with IKEv1, IKEv2 simplifies the SA negotiation process and provides better support for multi-CIDR-block scenarios.
        #    
        # <props="china"><ph>If the VPN gateway instance type is China Certified Cryptography, only **ikev1** is supported for the IKE version.</ph>
        self.ike_version = ike_version
        # The identifier of the local end (Alibaba Cloud side) of the tunnel, which is used in Phase 1 negotiation. The identifier can be up to 100 characters in length and cannot contain spaces. The default value is the IP address of the tunnel.
        # 
        # **LocalId** supports the FQDN format. If you use the FQDN format, we recommend that you set the negotiation mode to **aggressive**.
        self.local_id = local_id
        # The pre-shared key used for identity authentication between the tunnel and the tunnel peer.
        # 
        # - The key must be 1 to 100 characters in length and can contain digits, uppercase and lowercase letters, and the following characters. It cannot contain spaces. ```~!\\`@#$%^&*()_-+={}[]|;:\\",.<>/?```
        # 
        # - If you do not specify a pre-shared key, the system generates a random 16-character string as the pre-shared key. You can call the [DescribeVpnConnection](https://help.aliyun.com/document_detail/2526951.html) operation to query the pre-shared key that is automatically generated by the system.     
        # 
        # > The pre-shared keys of the tunnel and the tunnel peer must be the same. Otherwise, the tunnel cannot be established.
        self.psk = psk
        # The identifier of the tunnel peer, which is used in Phase 1 negotiation. The identifier can be up to 100 characters in length and cannot contain spaces. The default value is the IP address of the customer gateway associated with the tunnel.
        # 
        # **RemoteId** supports the FQDN format. If you use the FQDN format, we recommend that you set the negotiation mode to **aggressive**.
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

class CreateVpnConnectionRequestTunnelOptionsSpecificationTunnelBgpConfig(DaraModel):
    def __init__(
        self,
        local_asn: int = None,
        local_bgp_ip: str = None,
        tunnel_cidr: str = None,
    ):
        # The autonomous system number on the local end (Alibaba Cloud side) of the tunnel. Valid values: **1** to **4294967295**. Default value: **45104**.
        # 
        # > - This parameter is required after you enable the BGP feature for the IPsec-VPN connection (by setting **EnableTunnelsBgp** to **true**).
        # > - Before you configure BGP, learn about how the BGP dynamic route feature works and its limits. For more information, see [Configure BGP dynamic routing](https://help.aliyun.com/document_detail/2638220.html).
        # > - Use a private autonomous system number to establish a BGP connection with Alibaba Cloud. Refer to the relevant documentation for the range of private autonomous system numbers.
        self.local_asn = local_asn
        # The BGP address on the local end (Alibaba Cloud side) of the tunnel. This address is an IP address within the BGP CIDR block.
        self.local_bgp_ip = local_bgp_ip
        # The BGP CIDR block of the tunnel. The CIDR block must be a CIDR block with a mask length of 30 within 169.254.0.0/16 and cannot be 169.254.0.0/30, 169.254.1.0/30, 169.254.2.0/30, 169.254.3.0/30, 169.254.4.0/30, 169.254.5.0/30, 169.254.6.0/30, or 169.254.169.252/30.
        # 
        # > The BGP CIDR block of each tunnel under a VPN gateway instance must be unique.
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

class CreateVpnConnectionRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. Once specified, the tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # You can specify up to 20 tag keys at a time.
        self.key = key
        # The tag value.
        # 
        # The tag value can be up to 128 characters in length and can be an empty string. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        # 
        # Each tag key corresponds to one tag value. You can specify up to 20 tag values at a time.
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

