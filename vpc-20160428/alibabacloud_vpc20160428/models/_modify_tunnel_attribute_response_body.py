# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ModifyTunnelAttributeResponseBody(DaraModel):
    def __init__(
        self,
        customer_gateway_id: str = None,
        enable_dpd: bool = None,
        enable_nat_traversal: bool = None,
        internet_ip: str = None,
        remote_ca_certificate: str = None,
        request_id: str = None,
        role: str = None,
        state: str = None,
        tunnel_bgp_config: main_models.ModifyTunnelAttributeResponseBodyTunnelBgpConfig = None,
        tunnel_id: str = None,
        tunnel_ike_config: main_models.ModifyTunnelAttributeResponseBodyTunnelIkeConfig = None,
        tunnel_ipsec_config: main_models.ModifyTunnelAttributeResponseBodyTunnelIpsecConfig = None,
        zone_no: str = None,
    ):
        # The ID of the customer gateway associated with the customer gateway.
        self.customer_gateway_id = customer_gateway_id
        # Indicates whether DPD is enabled. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.enable_dpd = enable_dpd
        # Indicates whether NAT traversal is enabled. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.enable_nat_traversal = enable_nat_traversal
        # The tunnel IP address.
        self.internet_ip = internet_ip
        # The peer CA certificate when a VPN gateway that uses an SM certificate is used to create the IPsec connection.
        self.remote_ca_certificate = remote_ca_certificate
        # The request ID.
        self.request_id = request_id
        # The tunnel role. Valid values:
        # 
        # *   **master**
        # *   **slave**
        self.role = role
        # The tunnel status. Valid values:
        # 
        # *   **active**
        # *   **updating**
        # *   **deleting**
        self.state = state
        # The BGP configuration.
        self.tunnel_bgp_config = tunnel_bgp_config
        # The tunnel ID.
        self.tunnel_id = tunnel_id
        # The Phase 1 configuration.
        self.tunnel_ike_config = tunnel_ike_config
        # The configurations of IPsec Phase 2.
        self.tunnel_ipsec_config = tunnel_ipsec_config
        # The tunnel zone.
        self.zone_no = zone_no

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

        if self.remote_ca_certificate is not None:
            result['RemoteCaCertificate'] = self.remote_ca_certificate

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if self.tunnel_ipsec_config is not None:
            result['TunnelIpsecConfig'] = self.tunnel_ipsec_config.to_map()

        if self.zone_no is not None:
            result['ZoneNo'] = self.zone_no

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

        if m.get('RemoteCaCertificate') is not None:
            self.remote_ca_certificate = m.get('RemoteCaCertificate')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TunnelBgpConfig') is not None:
            temp_model = main_models.ModifyTunnelAttributeResponseBodyTunnelBgpConfig()
            self.tunnel_bgp_config = temp_model.from_map(m.get('TunnelBgpConfig'))

        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')

        if m.get('TunnelIkeConfig') is not None:
            temp_model = main_models.ModifyTunnelAttributeResponseBodyTunnelIkeConfig()
            self.tunnel_ike_config = temp_model.from_map(m.get('TunnelIkeConfig'))

        if m.get('TunnelIpsecConfig') is not None:
            temp_model = main_models.ModifyTunnelAttributeResponseBodyTunnelIpsecConfig()
            self.tunnel_ipsec_config = temp_model.from_map(m.get('TunnelIpsecConfig'))

        if m.get('ZoneNo') is not None:
            self.zone_no = m.get('ZoneNo')

        return self

class ModifyTunnelAttributeResponseBodyTunnelIpsecConfig(DaraModel):
    def __init__(
        self,
        ipsec_auth_alg: str = None,
        ipsec_enc_alg: str = None,
        ipsec_lifetime: int = None,
        ipsec_pfs: str = None,
    ):
        # The IPsec authentication algorithm.
        self.ipsec_auth_alg = ipsec_auth_alg
        # The IPsec encryption algorithm.
        self.ipsec_enc_alg = ipsec_enc_alg
        # The IPsec lifetime. Unit: seconds.
        self.ipsec_lifetime = ipsec_lifetime
        # The DH group.
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

class ModifyTunnelAttributeResponseBodyTunnelIkeConfig(DaraModel):
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
        # The IKE authentication algorithm.
        self.ike_auth_alg = ike_auth_alg
        # The IKE encryption algorithm.
        self.ike_enc_alg = ike_enc_alg
        # The IKE lifetime. Unit: seconds.
        self.ike_lifetime = ike_lifetime
        # The IKE negotiation mode.
        # 
        # *   **main:** This mode offers higher security during negotiations.
        # *   **aggressive**: This mode is faster and has a higher success rate.
        self.ike_mode = ike_mode
        # The DH group.
        self.ike_pfs = ike_pfs
        # The IKE version.
        # 
        # *   **ikev1**
        # *   **ikev2**
        # 
        # Compared with IKEv1, IKEv2 simplifies the SA negotiation process and provides better support for scenarios with multiple CIDR blocks.
        self.ike_version = ike_version
        # The tunnel identifier. The identifier supports FQDNs and IP addresses. The default value is the tunnel IP address.
        self.local_id = local_id
        # The pre-shared key.
        self.psk = psk
        # The peer identifier. The identifier supports FQDNs and IP addresses. The default identifier is the IP address of the customer gateway associated with the tunnel.
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

class ModifyTunnelAttributeResponseBodyTunnelBgpConfig(DaraModel):
    def __init__(
        self,
        enable_bgp: bool = None,
        local_asn: int = None,
        local_bgp_ip: str = None,
        peer_asn: int = None,
        peer_bgp_ip: str = None,
        tunnel_cidr: str = None,
    ):
        # Indicates whether the BGP feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable_bgp = enable_bgp
        # The local ASN.
        self.local_asn = local_asn
        # The BGP IP address of the tunnel.
        self.local_bgp_ip = local_bgp_ip
        # The peer ASN.
        self.peer_asn = peer_asn
        # The BGP IP address of the peer.
        self.peer_bgp_ip = peer_bgp_ip
        # The CIDR block to which the tunnel BGP IP address belongs.
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

        if m.get('TunnelCidr') is not None:
            self.tunnel_cidr = m.get('TunnelCidr')

        return self

