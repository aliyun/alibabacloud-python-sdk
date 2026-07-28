# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateVpnAttachmentRequest(DaraModel):
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
        network_type: str = None,
        owner_account: str = None,
        region_id: str = None,
        remote_ca_cert: str = None,
        remote_subnet: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags: List[main_models.CreateVpnAttachmentRequestTags] = None,
        tunnel_bandwidth: str = None,
        tunnel_options_specification: List[main_models.CreateVpnAttachmentRequestTunnelOptionsSpecification] = None,
    ):
        # Specifies whether to automatically configure routes. Valid values:
        # 
        # - **true** (default): Automatically configure routes.
        # 
        # - **false**: Do not automatically configure routes.
        self.auto_config_route = auto_config_route
        # This parameter is supported when you create a single-tunnel IPsec-VPN connection.
        # 
        # BGP configuration:
        # 
        # - **BgpConfig.EnableBgp**: Specifies whether to enable the BGP feature. Valid values: **true** or **false** (default).
        # 
        # - **BgpConfig.LocalAsn**: The autonomous system number on the Alibaba Cloud side. Valid values: **1** to **4294967295**. Default value: **45104**.
        # 
        #     You can enter the autonomous system number in the two-segment format: the first 16 bits.the last 16 bits. Enter each segment in decimal format.
        # 
        #     For example, if you enter 123.456, the autonomous system number is 123 × 65536 + 456 = 8061384.
        # 
        # - **BgpConfig.TunnelCidr**: The IPsec tunnel CIDR block. The CIDR block must fall within 169.254.0.0/16 and have a mask length of 30 bits. The CIDR block cannot be 169.254.0.0/30, 169.254.1.0/30, 169.254.2.0/30, 169.254.3.0/30, 169.254.4.0/30, 169.254.5.0/30, 169.254.6.0/30, or 169.254.169.252/30.
        # 
        # - **LocalBgpIp**: The BGP address on the Alibaba Cloud side. This address is an IP address within the IPsec tunnel CIDR block. 
        # 
        # > - Before you add BGP configurations, learn about how the dynamic routing feature works and its limits. For more information, see [Configure BGP dynamic routing](https://help.aliyun.com/document_detail/445767.html).
        # > - Use a private autonomous system number to establish a BGP connection with Alibaba Cloud. Refer to the relevant documentation for the range of private autonomous system numbers.
        self.bgp_config = bgp_config
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # The customer gateway ID.
        # 
        # > This parameter is required only when you create a single-tunnel IPsec-VPN connection.
        self.customer_gateway_id = customer_gateway_id
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run without creating the IPsec-VPN connection. The system checks the required parameters, request format, and service limits. If the check fails, the corresponding error is returned. If the check succeeds, the error code `DryRunOperation` is returned.
        # - **false** (default): performs a dry run and sends the request. If the check succeeds, the IPsec-VPN connection is created.
        self.dry_run = dry_run
        # Specifies whether the configuration takes effect immediately. Valid values:
        # 
        # - **true**: The system initiates IPsec protocol negotiation immediately after the configuration is complete.
        # - **false** (default): The system initiates IPsec protocol negotiation only when traffic enters the IPsec-VPN connection.
        self.effect_immediately = effect_immediately
        # This parameter is supported when you create a single-tunnel IPsec-VPN connection.
        # 
        # Specifies whether to enable the Dead Peer Detection (DPD) feature. Valid values:
        # 
        # - **true** (default): Enables the DPD feature. The IPsec initiator sends DPD packets to check the existence and availability of the peer. If no correct response is received within the specified time, the connection fails. Then, the ISAKMP SA, IPsec SA, and IPsec tunnel are deleted.
        # 
        # - **false**: Disables the DPD feature. The IPsec initiator does not send DPD packets.
        self.enable_dpd = enable_dpd
        # This parameter is supported when you create a single-tunnel IPsec-VPN connection.
        # 
        # Specifies whether to enable NAT traversal. Valid values:
        # 
        # - **true** (default): Enables NAT traversal. After NAT traversal is enabled, the verification of the UDP port number is removed during IKE negotiation, and NAT gateway devices along the VPN tunnel can be discovered.
        # 
        # - **false**: Disables NAT traversal.
        self.enable_nat_traversal = enable_nat_traversal
        # This parameter is supported when you create a dual-tunnel IPsec-VPN connection.
        # 
        # Specifies whether to enable the BGP dynamic routing feature for the tunnels. Valid values: **true** or **false** (default).
        # 
        # > Before you add BGP configurations, learn about how the BGP dynamic routing feature works and its limits. For more information, see [Configure BGP dynamic routing](https://help.aliyun.com/document_detail/445767.html).
        self.enable_tunnels_bgp = enable_tunnels_bgp
        # This parameter is supported when you create a single-tunnel IPsec-VPN connection.
        # 
        # Health check configuration:
        # 
        # - **HealthCheckConfig.enable**: Specifies whether to enable health checks. Valid values: **true** or **false** (default).
        # 
        # - **HealthCheckConfig.dip**: The destination IP address of the health check. Enter an IP address of the on-premises data center that can be accessed from the VPC side through the IPsec-VPN connection.
        # 
        # - **HealthCheckConfig.sip**: The source IP address of the health check. Enter an IP address on the VPC side that can be accessed from the on-premises data center through the IPsec-VPN connection.
        # 
        # - **HealthCheckConfig.interval**: The retry interval of the health check. Unit: seconds. Default value: **3**.
        # 
        # - **HealthCheckConfig.retry**: The number of retry packets sent during the health check. Default value: **3**.
        # 
        # - **HealthCheckConfig.Policy**: Specifies whether to withdraw published routes when the health check fails. Valid values:
        # 
        #      - **revoke_route** (default): Withdraw published routes.
        #      - **reserve_route**: Do not withdraw published routes.
        self.health_check_config = health_check_config
        # This parameter is supported when you create a single-tunnel IPsec-VPN connection.
        # 
        # Phase 1 negotiation configuration:
        #            
        # - **IkeConfig.Psk**: The pre-shared key used for identity authentication between the VPN gateway and the on-premises data center.
        # 
        #     - The key must be 1 to 100 characters in length and can contain digits, uppercase and lowercase letters, and the following characters. It cannot contain spaces. ```~!`@#$%^&*()_-+={}[]|;:\\",.<>/?```
        #     - If you do not specify a pre-shared key, the system randomly generates a string as the pre-shared key. You can call the [DescribeVpnConnection](https://help.aliyun.com/document_detail/2526951.html) operation to query the pre-shared key that is automatically generated by the system.
        # 
        #     > The pre-shared key on the IPsec-VPN connection side must be the same as the authentication key on the on-premises data center side. Otherwise, the connection between the on-premises data center and the VPN gateway cannot be established.
        # 
        # - **IkeConfig.IkeVersion**: The version of the IKE protocol. Valid values: **ikev1** or **ikev2**. Default value: **ikev1**.   
        # 
        # - **IkeConfig.IkeMode**: The negotiation mode. Valid values: **main** or **aggressive**. Default value: **main**.   
        # 
        # - **IkeConfig.IkeEncAlg**: The encryption algorithm used in Phase 1 negotiation. Valid values: **aes**, **aes192**, **aes256**, **des**, or **3des**. Default value: **aes**.   
        # 
        # - **IkeConfig.IkeAuthAlg**: The authentication algorithm used in Phase 1 negotiation. Valid values: **md5**, **sha1**, **sha256**, **sha384**, **sha512**. Default value: **md5**.   
        # 
        # - **IkeConfig.IkePfs**: The Diffie-Hellman key exchange algorithm used in Phase 1 negotiation. Valid values: **group1**, **group2**, **group5**, or **group14**. Default value: **group2**.   
        # 
        # - **IkeConfig.IkeLifetime**: The lifetime of the SA generated in Phase 1 negotiation. Unit: seconds. Valid values: **0** to **86400**. Default value: **86400**.   
        # 
        # - **IkeConfig.LocalId**: The identifier on the Alibaba Cloud side of the IPsec-VPN connection. The identifier is limited to 100 characters in length and cannot contain spaces. The default value is empty.
        # 
        # - **IkeConfig.RemoteId**: The identifier on the on-premises data center side of the IPsec-VPN connection. The identifier is limited to 100 characters in length and cannot contain spaces. The default value is the IP address of the customer gateway.
        self.ike_config = ike_config
        # This parameter is supported when you create a single-tunnel IPsec-VPN connection.
        # 
        # Phase 2 negotiation configuration: 
        # 
        # - **IpsecConfig.IpsecEncAlg**: The encryption algorithm used in Phase 2 negotiation. Valid values: **aes**, **aes192**, **aes256**, **des**, or **3des**. Default value: **aes**.   
        # 
        # - **IpsecConfig.IpsecAuthAlg**: The authentication algorithm used in Phase 2 negotiation. Valid values: **md5**, **sha1**, **sha256**, **sha384**, **sha512**. Default value: **md5**.   
        # 
        # - **IpsecConfig.IpsecPfs**: The Diffie-Hellman key exchange algorithm used in Phase 2 negotiation. Valid values: **disabled**, **group1**, **group2**, **group5**, or **group14**. Default value: **group2**.   
        # 
        # - **IpsecConfig.IpsecLifetime**: The lifetime of the SA generated in Phase 2 negotiation. Unit: seconds. Valid values: **0** to **86400**. Default value: **86400**.
        self.ipsec_config = ipsec_config
        # The CIDR block on the VPC side that needs to communicate with the on-premises data center. This CIDR block is used in Phase 2 negotiation.
        # 
        # Separate multiple CIDR blocks with commas (,). Example: 192.168.1.0/24,192.168.2.0/24.
        # 
        # Notes on the routing mode of the IPsec-VPN connection:
        # 
        # - If both **LocalSubnet** and **RemoteSubnet** are set to 0.0.0.0/0, the destination routing mode is used.
        # - If both **LocalSubnet** and **RemoteSubnet** are set to specific CIDR blocks, the policy-based routing mode is used.
        # 
        # This parameter is required.
        self.local_subnet = local_subnet
        # The name of the IPsec-VPN connection.
        # 
        # The name must be 1 to 100 characters in length and cannot start with `http://` or `https://`.
        self.name = name
        # The network type of the IPsec-VPN connection. Valid values:
        # - **public** (default): public network. The IPsec-VPN connection establishes an encrypted communication channel over the Internet.
        # - **private**: private network. The IPsec-VPN connection establishes an encrypted communication channel over a private network.
        self.network_type = network_type
        self.owner_account = owner_account
        # The region ID of the IPsec-VPN connection.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The CA certificate of the peer.
        # 
        # > This parameter is not in effect.
        self.remote_ca_cert = remote_ca_cert
        # The CIDR block on the on-premises data center side that needs to communicate with the VPC. This CIDR block is used in Phase 2 negotiation.
        # 
        # Separate multiple CIDR blocks with commas (,). Example: 192.168.3.0/24,192.168.4.0/24.
        # 
        # Notes on the routing mode of the IPsec-VPN connection:
        # 
        # - If both **LocalSubnet** and **RemoteSubnet** are set to 0.0.0.0/0, the destination routing mode is used.
        # - If both **LocalSubnet** and **RemoteSubnet** are set to specific CIDR blocks, the policy-based routing mode is used.
        # 
        # This parameter is required.
        self.remote_subnet = remote_subnet
        # The ID of the resource group to which the IPsec-VPN connection belongs.
        # 
        # - You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to query the resource group ID.
        # - If you do not specify a resource group ID, the IPsec-VPN connection belongs to the default resource group after it is created.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of tags to add to the IPsec-VPN connection.
        # 
        # You can add up to 20 tags to an IPsec-VPN connection at a time.
        self.tags = tags
        # The bandwidth specification of a single VPN tunnel. Valid values:
        # - Standard (default): standard. The default bandwidth is 1 Gbps.
        # - Large: large. The default bandwidth is 3 Gbps.
        self.tunnel_bandwidth = tunnel_bandwidth
        # The tunnel configurations.
        # 
        # - The parameters in the **TunnelOptionsSpecification** array are supported when you create a dual-tunnel IPsec-VPN connection.
        # - When you create a dual-tunnel IPsec-VPN connection, you must add two tunnels at the same time to ensure link redundancy for the IPsec-VPN connection. Only two tunnels can be added to an IPsec-VPN connection.
        self.tunnel_options_specification = tunnel_options_specification

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

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remote_ca_cert is not None:
            result['RemoteCaCert'] = self.remote_ca_cert

        if self.remote_subnet is not None:
            result['RemoteSubnet'] = self.remote_subnet

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.tunnel_bandwidth is not None:
            result['TunnelBandwidth'] = self.tunnel_bandwidth

        result['TunnelOptionsSpecification'] = []
        if self.tunnel_options_specification is not None:
            for k1 in self.tunnel_options_specification:
                result['TunnelOptionsSpecification'].append(k1.to_map() if k1 else None)

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

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemoteCaCert') is not None:
            self.remote_ca_cert = m.get('RemoteCaCert')

        if m.get('RemoteSubnet') is not None:
            self.remote_subnet = m.get('RemoteSubnet')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateVpnAttachmentRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TunnelBandwidth') is not None:
            self.tunnel_bandwidth = m.get('TunnelBandwidth')

        self.tunnel_options_specification = []
        if m.get('TunnelOptionsSpecification') is not None:
            for k1 in m.get('TunnelOptionsSpecification'):
                temp_model = main_models.CreateVpnAttachmentRequestTunnelOptionsSpecification()
                self.tunnel_options_specification.append(temp_model.from_map(k1))

        return self

class CreateVpnAttachmentRequestTunnelOptionsSpecification(DaraModel):
    def __init__(
        self,
        customer_gateway_id: str = None,
        enable_dpd: bool = None,
        enable_nat_traversal: bool = None,
        tunnel_bgp_config: main_models.CreateVpnAttachmentRequestTunnelOptionsSpecificationTunnelBgpConfig = None,
        tunnel_ike_config: main_models.CreateVpnAttachmentRequestTunnelOptionsSpecificationTunnelIkeConfig = None,
        tunnel_index: int = None,
        tunnel_ipsec_config: main_models.CreateVpnAttachmentRequestTunnelOptionsSpecificationTunnelIpsecConfig = None,
    ):
        # The customer gateway ID associated with the tunnel.
        # 
        # > This parameter is required when you create a dual-tunnel IPsec-VPN connection.
        self.customer_gateway_id = customer_gateway_id
        # Specifies whether to enable the Dead Peer Detection (DPD) feature for the tunnel. Valid values:
        # 
        # - **true** (default): Enables the DPD feature. The IPsec initiator sends DPD packets to check the existence and availability of the peer. If no correct response is received within the specified time, the connection fails. Then, the ISAKMP SA, IPsec SA, and IPsec tunnel are deleted.
        # 
        # - **false**: Disables the DPD feature. The IPsec initiator does not send DPD packets.
        self.enable_dpd = enable_dpd
        # Specifies whether to enable NAT traversal for the tunnel. Valid values:
        # 
        # - **true** (default): Enables NAT traversal. After NAT traversal is enabled, the verification of the UDP port number is removed during IKE negotiation, and NAT gateway devices along the tunnel can be discovered.
        # 
        # - **false**: Disables NAT traversal.
        self.enable_nat_traversal = enable_nat_traversal
        # The BGP configuration for the tunnel.
        # 
        # > This parameter is required when you enable BGP for the IPsec-VPN connection (set **EnableTunnelsBgp** to **true**).
        self.tunnel_bgp_config = tunnel_bgp_config
        # The Phase 1 negotiation configuration.
        self.tunnel_ike_config = tunnel_ike_config
        # The order in which the tunnel is created.
        # 
        # - **1**: the first tunnel.
        # - **2**: the second tunnel.
        self.tunnel_index = tunnel_index
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

        if self.tunnel_bgp_config is not None:
            result['TunnelBgpConfig'] = self.tunnel_bgp_config.to_map()

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

        if m.get('TunnelBgpConfig') is not None:
            temp_model = main_models.CreateVpnAttachmentRequestTunnelOptionsSpecificationTunnelBgpConfig()
            self.tunnel_bgp_config = temp_model.from_map(m.get('TunnelBgpConfig'))

        if m.get('TunnelIkeConfig') is not None:
            temp_model = main_models.CreateVpnAttachmentRequestTunnelOptionsSpecificationTunnelIkeConfig()
            self.tunnel_ike_config = temp_model.from_map(m.get('TunnelIkeConfig'))

        if m.get('TunnelIndex') is not None:
            self.tunnel_index = m.get('TunnelIndex')

        if m.get('TunnelIpsecConfig') is not None:
            temp_model = main_models.CreateVpnAttachmentRequestTunnelOptionsSpecificationTunnelIpsecConfig()
            self.tunnel_ipsec_config = temp_model.from_map(m.get('TunnelIpsecConfig'))

        return self

class CreateVpnAttachmentRequestTunnelOptionsSpecificationTunnelIpsecConfig(DaraModel):
    def __init__(
        self,
        ipsec_auth_alg: str = None,
        ipsec_enc_alg: str = None,
        ipsec_lifetime: int = None,
        ipsec_pfs: str = None,
    ):
        # The authentication algorithm used in Phase 2 negotiation.
        # 
        # Valid values: **md5**, **sha1**, **sha256**, **sha384**, **sha512**. Default value: **sha1**.
        self.ipsec_auth_alg = ipsec_auth_alg
        # The encryption algorithm used in Phase 2 negotiation. Valid values: **aes**, **aes192**, **aes256**, **des**, or **3des**. Default value: **aes**.
        self.ipsec_enc_alg = ipsec_enc_alg
        # The lifetime of the SA generated in Phase 2 negotiation. Unit: seconds.
        # 
        # Valid values: **0** to **86400**. Default value: **86400**.
        self.ipsec_lifetime = ipsec_lifetime
        # The Diffie-Hellman key exchange algorithm used in Phase 2 negotiation. Default value: **group2**.   
        # 
        # Valid values: **disabled**, **group1**, **group2**, **group5**, **group14**.
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

class CreateVpnAttachmentRequestTunnelOptionsSpecificationTunnelIkeConfig(DaraModel):
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
        # The authentication algorithm used in Phase 1 negotiation. Valid values: **md5**, **sha1**, **sha256**, **sha384**, **sha512**. Default value: **sha1**.
        self.ike_auth_alg = ike_auth_alg
        # The encryption algorithm used in Phase 1 negotiation. Valid values: **aes**, **aes192**, **aes256**, **des**, or **3des**. Default value: **aes**.
        self.ike_enc_alg = ike_enc_alg
        # The lifetime of the SA generated in Phase 1 negotiation. Unit: seconds.
        # 
        # Valid values: **0** to **86400**. Default value: **86400**.
        self.ike_lifetime = ike_lifetime
        # The negotiation mode of the IKE version. Valid values: **main** or **aggressive**. Default value: **main**.   
        # 
        # - **main**: main mode. The negotiation process is more secure.
        # - **aggressive**: aggressive mode. The negotiation is faster and has a higher success rate.
        self.ike_mode = ike_mode
        # The Diffie-Hellman key exchange algorithm used in Phase 1 negotiation. Default value: **group2**.   
        # Valid values: **group1**, **group2**, **group5**, **group14**.
        self.ike_pfs = ike_pfs
        # The version of the IKE protocol. Valid values: **ikev1** or **ikev2**. Default value: **ikev2**.
        # 
        # Compared with IKEv1, IKEv2 simplifies the SA negotiation process and provides better support for multi-CIDR-block scenarios.
        self.ike_version = ike_version
        # The identifier on the local end (Alibaba Cloud side) of the tunnel, which is used in Phase 1 negotiation. The identifier is limited to 100 characters in length and cannot contain spaces. The default value is the IP address of the tunnel.
        # 
        # **LocalId** supports the FQDN format. If you use the FQDN format, we recommend that you set the negotiation mode to **aggressive**.
        self.local_id = local_id
        # The pre-shared key used for identity authentication between the tunnel and the tunnel peer.
        # 
        # - The key must be 1 to 100 characters in length and can contain digits, uppercase and lowercase letters, and the following characters. It cannot contain spaces. ```~!\\`@#$%^&*()_-+={}[]|;:\\",.<>/?```
        # 
        # - If you do not specify a pre-shared key, the system randomly generates a 16-character string as the pre-shared key. You can call the [DescribeVpnAttachments](https://help.aliyun.com/document_detail/2526939.html) operation to query the pre-shared key that is automatically generated by the system.     
        # 
        # > The pre-shared keys of the tunnel and the tunnel peer must be the same. Otherwise, the system cannot establish the tunnel.
        self.psk = psk
        # The identifier of the tunnel peer, which is used in Phase 1 negotiation. The identifier is limited to 100 characters in length and cannot contain spaces. The default value is the IP address of the customer gateway associated with the tunnel.
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

class CreateVpnAttachmentRequestTunnelOptionsSpecificationTunnelBgpConfig(DaraModel):
    def __init__(
        self,
        local_asn: int = None,
        local_bgp_ip: str = None,
        tunnel_cidr: str = None,
    ):
        # The autonomous system number on the local end (Alibaba Cloud side) of the tunnel. Valid values: **1** to **4294967295**. Default value: **45104**.
        # 
        # > We recommend that you use a private autonomous system number to establish a BGP connection with Alibaba Cloud. Refer to the relevant documentation for the range of private autonomous system numbers.
        self.local_asn = local_asn
        # The BGP address on the local end (Alibaba Cloud side) of the tunnel. This address is an IP address within the BGP CIDR block.
        self.local_bgp_ip = local_bgp_ip
        # The BGP CIDR block of the tunnel. The CIDR block must fall within 169.254.0.0/16 and have a mask length of 30 bits. The CIDR block cannot be 169.254.0.0/30, 169.254.1.0/30, 169.254.2.0/30, 169.254.3.0/30, 169.254.4.0/30, 169.254.5.0/30, 169.254.6.0/30, or 169.254.169.252/30.
        # 
        # > The tunnel CIDR blocks of the two tunnels under an IPsec-VPN connection must be different.
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

class CreateVpnAttachmentRequestTags(DaraModel):
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

