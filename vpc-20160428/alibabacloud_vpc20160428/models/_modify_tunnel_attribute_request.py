# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ModifyTunnelAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tunnel_id: str = None,
        tunnel_options_specification: main_models.ModifyTunnelAttributeRequestTunnelOptionsSpecification = None,
        vpn_connection_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** as the **ClientToken**. The **RequestId** may be different for each request.
        self.client_token = client_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the IPsec-VPN connection.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tunnel ID.
        # 
        # This parameter is required.
        self.tunnel_id = tunnel_id
        # The tunnel configuration to modify.
        self.tunnel_options_specification = tunnel_options_specification
        # The ID of the IPsec-VPN connection.
        # 
        # This parameter is required.
        self.vpn_connection_id = vpn_connection_id

    def validate(self):
        if self.tunnel_options_specification:
            self.tunnel_options_specification.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id

        if self.tunnel_options_specification is not None:
            result['TunnelOptionsSpecification'] = self.tunnel_options_specification.to_map()

        if self.vpn_connection_id is not None:
            result['VpnConnectionId'] = self.vpn_connection_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')

        if m.get('TunnelOptionsSpecification') is not None:
            temp_model = main_models.ModifyTunnelAttributeRequestTunnelOptionsSpecification()
            self.tunnel_options_specification = temp_model.from_map(m.get('TunnelOptionsSpecification'))

        if m.get('VpnConnectionId') is not None:
            self.vpn_connection_id = m.get('VpnConnectionId')

        return self

class ModifyTunnelAttributeRequestTunnelOptionsSpecification(DaraModel):
    def __init__(
        self,
        customer_gateway_id: str = None,
        enable_dpd: bool = None,
        enable_nat_traversal: bool = None,
        remote_ca_certificate: str = None,
        tunnel_bgp_config: main_models.ModifyTunnelAttributeRequestTunnelOptionsSpecificationTunnelBgpConfig = None,
        tunnel_ike_config: main_models.ModifyTunnelAttributeRequestTunnelOptionsSpecificationTunnelIkeConfig = None,
        tunnel_ipsec_config: main_models.ModifyTunnelAttributeRequestTunnelOptionsSpecificationTunnelIpsecConfig = None,
    ):
        # The instance ID of the customer gateway associated with the tunnel.
        self.customer_gateway_id = customer_gateway_id
        # Specifies whether to enable the Dead Peer Detection (DPD) feature. Valid values:
        # 
        # - **true**: Enabled. The initiator of the IPsec-VPN connection sends DPD packets to check whether the peer is alive. If no correct response is received within the specified period of time, the connection fails. The ISAKMP SA and the corresponding IPsec SA are deleted, and the tunnel is also deleted.
        # 
        # - **false**: Disabled. The initiator of the IPsec-VPN connection does not send DPD packets.
        self.enable_dpd = enable_dpd
        # Specifies whether to enable NAT traversal. Valid values:
        # 
        # - **true**: Enabled. After NAT traversal is enabled, the verification of the UDP port number is removed during IKE negotiations, and the NAT gateway device in the VPN tunnel can be discovered.
        # 
        # - **false**: Disabled.
        self.enable_nat_traversal = enable_nat_traversal
        # The CA certificate of the peer when you use an IPsec-VPN connection with a Chinese SM VPN gateway.
        self.remote_ca_certificate = remote_ca_certificate
        # The BGP configuration of the tunnel to modify.
        # 
        # If BGP was not previously enabled for the tunnel, call the [ModifyVpnConnectionAttribute](https://help.aliyun.com/document_detail/120381.html) operation to enable BGP for the tunnel and add the BGP configuration.
        self.tunnel_bgp_config = tunnel_bgp_config
        # The IKE phase (Phase 1) configuration of the tunnel to modify.
        self.tunnel_ike_config = tunnel_ike_config
        # The IPsec phase (Phase 2) configuration of the tunnel to modify.
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

        if m.get('TunnelBgpConfig') is not None:
            temp_model = main_models.ModifyTunnelAttributeRequestTunnelOptionsSpecificationTunnelBgpConfig()
            self.tunnel_bgp_config = temp_model.from_map(m.get('TunnelBgpConfig'))

        if m.get('TunnelIkeConfig') is not None:
            temp_model = main_models.ModifyTunnelAttributeRequestTunnelOptionsSpecificationTunnelIkeConfig()
            self.tunnel_ike_config = temp_model.from_map(m.get('TunnelIkeConfig'))

        if m.get('TunnelIpsecConfig') is not None:
            temp_model = main_models.ModifyTunnelAttributeRequestTunnelOptionsSpecificationTunnelIpsecConfig()
            self.tunnel_ipsec_config = temp_model.from_map(m.get('TunnelIpsecConfig'))

        return self

class ModifyTunnelAttributeRequestTunnelOptionsSpecificationTunnelIpsecConfig(DaraModel):
    def __init__(
        self,
        ipsec_auth_alg: str = None,
        ipsec_enc_alg: str = None,
        ipsec_lifetime: int = None,
        ipsec_pfs: str = None,
    ):
        # The authentication algorithm used in Phase 2 negotiations.
        # 
        # <props="china">
        # 
        # - If the IPsec-VPN connection is associated with a standard VPN gateway, valid values are **md5**, **sha1**, **sha256**, **sha384**, and **sha512**.
        # - If the IPsec-VPN connection is associated with a Chinese SM VPN gateway, the value is **sm3**.
        # 
        # 
        # 
        # <props="intl">
        # 
        # Valid values: **md5**, **sha1**, **sha256**, **sha384**, and **sha512**.
        # 
        # .
        self.ipsec_auth_alg = ipsec_auth_alg
        # The encryption algorithm used in Phase 2 negotiations.
        # 
        # <props="china">
        # 
        # - If the IPsec-VPN connection is associated with a standard VPN gateway, valid values are **aes**, **aes192**, **aes256**, **des**, and **3des**.  
        # - If the IPsec-VPN connection is associated with a Chinese SM VPN gateway, the value is **sm4**.
        # 
        # 
        # 
        # <props="intl">
        # 
        # Valid values: **aes**, **aes192**, **aes256**, **des**, and **3des**.  
        # 
        # .
        self.ipsec_enc_alg = ipsec_enc_alg
        # The lifetime of the SA negotiated in Phase 2. Unit: seconds. Valid values: **0** to **86400**.
        self.ipsec_lifetime = ipsec_lifetime
        # The Diffie-Hellman key exchange algorithm used in Phase 2 negotiations. Valid values: **disabled**, **group1**, **group2**, **group5**, and **group14**.
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

class ModifyTunnelAttributeRequestTunnelOptionsSpecificationTunnelIkeConfig(DaraModel):
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
        # <props="china">
        # 
        # - If the IPsec-VPN connection is associated with a standard VPN gateway, valid values are **md5**, **sha1**, **sha256**, **sha384**, and **sha512**.
        # - If the IPsec-VPN connection is associated with a Chinese SM VPN gateway, the value is **sm3**.
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # Valid values: **md5**, **sha1**, **sha256**, **sha384**, and **sha512**.
        # 
        # .
        self.ike_auth_alg = ike_auth_alg
        # The encryption algorithm used in Phase 1 negotiations.
        # 
        # <props="china">
        # 
        # - If the IPsec-VPN connection is associated with a standard VPN gateway, valid values are **aes**, **aes192**, **aes256**, **des**, and **3des**.  
        # - If the IPsec-VPN connection is associated with a Chinese SM VPN gateway, the value is **sm4**.
        # 
        # 
        # 
        # <props="intl">
        # 
        # Valid values: **aes**, **aes192**, **aes256**, **des**, and **3des**.  
        # 
        # .
        self.ike_enc_alg = ike_enc_alg
        # The lifetime of the SA negotiated in Phase 1. Unit: seconds. Valid values: **0** to **86400**.
        self.ike_lifetime = ike_lifetime
        # The negotiation mode of the IKE version. Valid values:
        # 
        # - **main**: main mode. This mode offers high security during negotiations.
        # - **aggressive**: aggressive mode. This mode supports fast negotiations and a higher success rate.
        self.ike_mode = ike_mode
        # The Diffie-Hellman key exchange algorithm used in Phase 1 negotiations. Valid values: **group1**, **group2**, **group5**, and **group14**.
        self.ike_pfs = ike_pfs
        # The version of the IKE protocol. Valid values: **ikev1** and **ikev2**.
        self.ike_version = ike_version
        # The identifier of the local end of the tunnel. The identifier can be up to 100 characters in length and cannot contain spaces. It supports FQDN and IP formats. Default value: the IP address of the tunnel.
        self.local_id = local_id
        # The pre-shared key used for identity authentication between the tunnel and the peer.
        #     
        #    - The key must be 1 to 100 characters in length and can contain digits, uppercase letters, lowercase letters, and the following characters. It cannot contain spaces. ```~!`@#$%^&*()_-+={}[]|;:\\",.<>/?```
        #    - If you do not specify a pre-shared key, the system generates a random 16-character string as the pre-shared key. You can call the [DescribeVpnConnection](https://help.aliyun.com/document_detail/120374.html) operation to query the pre-shared key that is automatically generated by the system.
        #    > The pre-shared keys configured on the tunnel and the peer must be the same. Otherwise, the tunnel cannot be established.
        self.psk = psk
        # The identifier of the peer end of the tunnel. The identifier can be up to 100 characters in length and cannot contain spaces. It supports FQDN and IP formats. Default value: the IP address of the customer gateway instance associated with the tunnel.
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

class ModifyTunnelAttributeRequestTunnelOptionsSpecificationTunnelBgpConfig(DaraModel):
    def __init__(
        self,
        local_asn: int = None,
        local_bgp_ip: str = None,
        tunnel_cidr: str = None,
    ):
        # The autonomous system number (ASN) of the local end of the tunnel. Valid values: **1** to **4294967295**.
        self.local_asn = local_asn
        # The BGP IP address of the local end of the tunnel. The IP address must fall within the **TunnelCidr** CIDR block.
        self.local_bgp_ip = local_bgp_ip
        # The CIDR block of the BGP IP address on the local end of the tunnel.
        # 
        # The CIDR block must be a CIDR block with a mask length of 30 within 169.254.0.0/16 and cannot be 169.254.0.0/30, 169.254.1.0/30, 169.254.2.0/30, 169.254.3.0/30, 169.254.4.0/30, 169.254.5.0/30, 169.254.6.0/30, or 169.254.169.252/30.
        # 
        # > The IPsec tunnel CIDR block of each IPsec-VPN connection under a VPN gateway instance must be unique.
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

