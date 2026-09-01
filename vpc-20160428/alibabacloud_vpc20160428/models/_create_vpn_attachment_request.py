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
        # - **true** (default): Automatically configures routes.
        # 
        # - **false**: Does not automatically configure routes.
        self.auto_config_route = auto_config_route
        # This parameter is supported when you create an IPsec-VPN connection in single-tunnel mode.
        # 
        # BGP configuration:
        # 
        # - **BgpConfig.EnableBgp**: specifies whether to enable BGP. Valid values: **true** or **false** (default).
        # 
        # - **BgpConfig.LocalAsn**: the autonomous system number (ASN) on the Alibaba Cloud side. Valid values: **1** to **4294967295**. Default value: **45104**.
        # 
        #     You can enter the ASN in the two-segment format: the first 16 bits.the last 16 bits. Each segment is entered in decimal notation.
        # 
        #     For example, if you enter 123.456, the ASN is 123×65536+456=8061384.
        # 
        # - **BgpConfig.TunnelCidr**: the CIDR block of the IPsec tunnel. The CIDR block must be a /30 subnet within 169.254.0.0/16 and cannot be 169.254.0.0/30, 169.254.1.0/30, 169.254.2.0/30, 169.254.3.0/30, 169.254.4.0/30, 169.254.5.0/30, 169.254.6.0/30, or 169.254.169.252/30.
        # 
        # - **LocalBgpIp**: the BGP IP address on the Alibaba Cloud side. This address must be an IP address within the IPsec tunnel CIDR block.
        # 
        # > - Before you configure BGP, we recommend that you familiarize yourself with how BGP dynamic routing works and its limits. For more information, see [Configure BGP dynamic routing](https://help.aliyun.com/document_detail/445767.html).
        # > - Use a private ASN to establish a BGP connection with Alibaba Cloud. Refer to the relevant documentation for the private ASN range.
        self.bgp_config = bgp_config
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is different.
        self.client_token = client_token
        # The customer gateway ID.
        self.customer_gateway_id = customer_gateway_id
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run without creating the IPsec-VPN connection. The system checks the required parameters, request syntax, and business limits. If the check fails, the corresponding error is returned. If the check passes, the error code `DryRunOperation` is returned.
        # - **false** (default): performs the request. After the check passes, the IPsec-VPN connection is created.
        self.dry_run = dry_run
        # Specifies whether the IPsec-VPN connection configuration takes effect immediately. Valid values:
        # 
        # - **true**: The system immediately initiates IPsec protocol negotiation after the configuration is complete.
        # - **false** (default): The system initiates IPsec protocol negotiation only when inbound traffic is detected.
        self.effect_immediately = effect_immediately
        # This parameter is supported when you create an IPsec-VPN connection in single-tunnel mode.
        # 
        # Specifies whether to enable the Dead Peer Detection (DPD) feature. Valid values:
        # 
        # - **true** (default): Enables the DPD feature. The IPsec initiator sends DPD packets to check whether the peer device is alive. If no correct response is received within the specified period of time, the peer is considered disconnected. The ISAKMP SA and the corresponding IPsec SA are deleted, and the security tunnel is also deleted.
        # 
        # - **false**: Disables the DPD feature. The IPsec initiator does not send DPD probe packets.
        self.enable_dpd = enable_dpd
        # This parameter is supported when you create an IPsec-VPN connection in single-tunnel mode.
        # 
        # Specifies whether to enable NAT traversal. Valid values:
        # 
        # - **true** (default): Enables NAT traversal. After NAT traversal is enabled, the IKE negotiation process skips UDP port number verification and can discover NAT gateway devices in the VPN tunnel.
        # 
        # - **false**: Disables NAT traversal.
        self.enable_nat_traversal = enable_nat_traversal
        # This parameter is supported when you create an IPsec-VPN connection in dual-tunnel mode.
        self.enable_tunnels_bgp = enable_tunnels_bgp
        # This parameter is supported when you create an IPsec-VPN connection in single-tunnel mode.
        self.health_check_config = health_check_config
        # This parameter is supported when you create an IPsec-VPN connection in single-tunnel mode.
        # 
        # Phase 1 negotiation configuration:
        #            
        # - **IkeConfig.Psk**: The pre-shared key, which is used for identity authentication between the VPN gateway and the on-premises data center.
        # 
        #     - The key must be 1 to 100 characters in length and can contain digits, uppercase letters, lowercase letters, and the following characters. It cannot contain spaces. ```~!`@#$%^&*()_-+={}[]|;:\\",.<>/?```
        #     - If you do not specify a pre-shared key, the system randomly generates a string as the pre-shared key. You can call the [DescribeVpnConnection](https://help.aliyun.com/document_detail/2526951.html) operation to query the pre-shared key automatically generated by the system.
        # 
        #     > The pre-shared key on the IPsec-VPN connection side must be the same as the authentication key on the on-premises data center side. Otherwise, a connection cannot be established between the on-premises data center and the VPN gateway.
        # 
        # - **IkeConfig.IkeVersion**: The version of the IKE protocol. Valid values: **ikev1** or **ikev2**. Default value: **ikev1**.   
        # 
        # - **IkeConfig.IkeMode**: The negotiation mode. Valid values: **main** or **aggressive**. Default value: **main**.   
        # 
        # - **IkeConfig.IkeEncAlg**: The encryption algorithm used in Phase 1 negotiation. Valid values: **aes**, **aes192**, **aes256**, **des**, or **3des**. Default value: **aes**.   
        # 
        # - **IkeConfig.IkeAuthAlg**: The authentication algorithm used in Phase 1 negotiation. Valid values: **md5**, **sha1**, **sha256**, **sha384**, or **sha512**. Default value: **md5**.   
        # 
        # - **IkeConfig.IkePfs**: The Diffie-Hellman key exchange algorithm used in Phase 1 negotiation. Valid values: **group1**, **group2**, **group5**, or **group14**. Default value: **group2**.   
        # 
        # - **IkeConfig.IkeLifetime**: The lifetime of the SA generated in Phase 1 negotiation. Unit: seconds. Valid values: **0** to **86400**. Default value: **86400**.   
        # 
        # - **IkeConfig.LocalId**: The identifier on the Alibaba Cloud side of the IPsec-VPN connection. The identifier can be up to 100 characters in length and cannot contain spaces. Default value: empty.
        # 
        # - **IkeConfig.RemoteId**: The identifier on the on-premises data center side of the IPsec-VPN connection. The identifier can be up to 100 characters in length and cannot contain spaces. Default value: the IP address of the customer gateway.
        self.ike_config = ike_config
        # This parameter is supported when you create an IPsec-VPN connection in single-tunnel mode.
        # 
        # The configuration of Phase 2 negotiation:
        # 
        # - **IpsecConfig.IpsecEncAlg**: The encryption algorithm for Phase 2 negotiation. Valid values: **aes**, **aes192**, **aes256**, **des**, or **3des**. Default value: **aes**.
        # 
        # - **IpsecConfig.IpsecAuthAlg**: The authentication algorithm for Phase 2 negotiation. Valid values: **md5**, **sha1**, **sha256**, **sha384**, **sha512**. Default value: **md5**.
        # 
        # - **IpsecConfig.IpsecPfs**: The Diffie-Hellman key exchange algorithm used in Phase 2 negotiation. Valid values: **disabled**, **group1**, **group2**, **group5**, or **group14**. Default value: **group2**.
        # 
        # - **IpsecConfig.IpsecLifetime**: The lifetime of the SA negotiated in Phase 2. Unit: seconds. Valid values: **0** to **86400**. Default value: **86400**.
        self.ipsec_config = ipsec_config
        # The CIDR block on the VPC side that needs to communicate with the on-premises data center. This is used for Phase 2 negotiation.
        # 
        # Separate multiple CIDR blocks with commas (,). Example: 192.168.1.0/24,192.168.2.0/24.
        # 
        # Description of IPsec-VPN connection routing modes:
        # 
        # - If both **LocalSubnet** and **RemoteSubnet** are set to 0.0.0.0/0, the destination routing mode is used.
        # - If both **LocalSubnet** and **RemoteSubnet** are set to specific CIDR blocks, the protected data flow mode is used.
        # 
        # This parameter is required.
        self.local_subnet = local_subnet
        # The name of the IPsec-VPN connection.
        self.name = name
        # The network type of the IPsec-VPN connection. Valid values:
        # - **public** (default): public network. The IPsec-VPN connection establishes an encrypted communication channel over the Internet.
        # - **private**: private network. The IPsec-VPN connection establishes an encrypted communication channel over a private network.
        self.network_type = network_type
        self.owner_account = owner_account
        # The region ID of the IPsec-VPN connection.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The CA certificate of the peer.
        self.remote_ca_cert = remote_ca_cert
        # The CIDR block of the on-premises data center that needs to communicate with the VPC. This is used for Phase 2 negotiation.
        # 
        # Separate multiple CIDR blocks with commas (,). Example: 192.168.3.0/24,192.168.4.0/24.
        # 
        # Description of the routing mode for the IPsec-VPN connection:
        # 
        # - If both **LocalSubnet** and **RemoteSubnet** are set to 0.0.0.0/0, the destination routing mode is used.
        # - If both **LocalSubnet** and **RemoteSubnet** are set to specific CIDR blocks, the protected data flow mode is used.
        # 
        # This parameter is required.
        self.remote_subnet = remote_subnet
        # The ID of the resource group to which the IPsec-VPN connection belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of tags to add to the IPsec-VPN connection.
        self.tags = tags
        # The bandwidth specification of a single VPN tunnel. Valid values:
        self.tunnel_bandwidth = tunnel_bandwidth
        # Configures tunnels.
        # 
        # - When you create a dual-tunnel IPsec-VPN connection, you can configure the parameters in the **TunnelOptionsSpecification** array.
        # - When you create a dual-tunnel IPsec-VPN connection, you must add two tunnels to the IPsec-VPN connection to ensure link redundancy. Only two tunnels can be added to an IPsec-VPN connection.
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
        # The ID of the customer gateway associated with the tunnel.
        self.customer_gateway_id = customer_gateway_id
        # Specifies whether to enable the Dead Peer Detection (DPD) feature for the tunnel. Valid values:
        self.enable_dpd = enable_dpd
        # Specifies whether to enable NAT traversal for the tunnel. Valid values:
        # 
        # - **true** (default): Enables NAT traversal. After NAT traversal is enabled, the IKE negotiation process skips UDP port number verification and can discover NAT gateway devices in the tunnel.
        # 
        # - **false**: Disables NAT traversal.
        self.enable_nat_traversal = enable_nat_traversal
        # The BGP configuration for the tunnel.
        self.tunnel_bgp_config = tunnel_bgp_config
        # The Phase 1 negotiation configuration.
        self.tunnel_ike_config = tunnel_ike_config
        # The creation order of the tunnel.
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
        # The authentication algorithm for Phase 2 negotiation.
        self.ipsec_auth_alg = ipsec_auth_alg
        # The encryption algorithm for Phase 2 negotiation. Valid values: **aes**, **aes192**, **aes256**, **des**, or **3des**. Default value: **aes**.
        self.ipsec_enc_alg = ipsec_enc_alg
        # The lifetime of the SA negotiated in Phase 2. Unit: seconds.
        self.ipsec_lifetime = ipsec_lifetime
        # The Diffie-Hellman key exchange algorithm used in the second phase of negotiation. Default value: **group2**.
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
        # The authentication algorithm for Phase 1 negotiation. Valid values: **md5**, **sha1**, **sha256**, **sha384**, and **sha512**. Default value: **sha1**.
        self.ike_auth_alg = ike_auth_alg
        # The encryption algorithm for Phase 1 negotiation. Valid values: **aes**, **aes192**, **aes256**, **des**, or **3des**. Default value: **aes**.
        self.ike_enc_alg = ike_enc_alg
        # The lifetime of the security association (SA) negotiated during Phase 1. Unit: seconds.
        # 
        # Valid values: **0** to **86400**. Default value: **86400**.
        self.ike_lifetime = ike_lifetime
        # The negotiation mode of the IKE version. Valid values: **main** or **aggressive**. Default value: **main**.
        # 
        # - **main**: Main mode. The negotiation process is highly secure.
        # - **aggressive**: Aggressive mode. Negotiation is fast and has a high success rate.
        self.ike_mode = ike_mode
        # The Diffie-Hellman key exchange algorithm used in the first-phase negotiation. Default value: **group2**.
        # 
        # Valid values: **group1**, **group2**, **group5**, **group14**.
        self.ike_pfs = ike_pfs
        # The version of the IKE protocol. Valid values: **ikev1** or **ikev2**. Default value: **ikev2**.
        # 
        # Compared with IKEv1, IKEv2 simplifies the SA negotiation process and provides better support for multi-CIDR-block scenarios.
        self.ike_version = ike_version
        # The identifier on the Alibaba Cloud side of the tunnel, used for Phase 1 negotiation. The value can be up to 100 characters in length and cannot contain spaces. The default value is the IP address of the tunnel.
        self.local_id = local_id
        # The pre-shared key, which is used for identity authentication between the tunnel and the tunnel peer.
        # 
        # - The key must be 1 to 100 characters in length and can contain digits, uppercase letters, lowercase letters, and the following characters: ```~!\\`@#$%^&*()_-+={}[]|;:\\",.<>/?``` It cannot contain spaces.
        # 
        # - If you do not specify a pre-shared key, the system randomly generates a 16-character string as the pre-shared key. You can call the [DescribeVpnAttachments](https://help.aliyun.com/document_detail/2526939.html) operation to query the pre-shared key automatically generated by the system.
        # 
        # > The pre-shared keys of the tunnel and the tunnel peer must be the same. Otherwise, the tunnel cannot be established.
        self.psk = psk
        # The identifier of the tunnel peer, used for Phase 1 negotiation. The value can be up to 100 characters in length and cannot contain spaces. The default value is the IP address of the customer gateway associated with the tunnel.
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
        # The autonomous system number (ASN) on the Alibaba Cloud side of the tunnel. Valid values: **1** to **4294967295**. Default value: **45104**.
        self.local_asn = local_asn
        # The BGP address on the Alibaba Cloud side of the tunnel. This address is an IP address within the BGP CIDR block.
        self.local_bgp_ip = local_bgp_ip
        # The BGP CIDR block of the tunnel. The CIDR block must fall within 169.254.0.0/16 and have a mask length of 30. The CIDR block cannot be 169.254.0.0/30, 169.254.1.0/30, 169.254.2.0/30, 169.254.3.0/30, 169.254.4.0/30, 169.254.5.0/30, 169.254.6.0/30, or 169.254.169.252/30.
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
        # The tag key. This value cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        # 
        # You can specify up to 20 tag keys at a time.
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

