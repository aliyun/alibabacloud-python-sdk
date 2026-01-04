# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DownloadVpnConnectionConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        vpn_connection_config: main_models.DownloadVpnConnectionConfigResponseBodyVpnConnectionConfig = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The configurations of the peer gateway device.
        self.vpn_connection_config = vpn_connection_config

    def validate(self):
        if self.vpn_connection_config:
            self.vpn_connection_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vpn_connection_config is not None:
            result['VpnConnectionConfig'] = self.vpn_connection_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VpnConnectionConfig') is not None:
            temp_model = main_models.DownloadVpnConnectionConfigResponseBodyVpnConnectionConfig()
            self.vpn_connection_config = temp_model.from_map(m.get('VpnConnectionConfig'))

        return self

class DownloadVpnConnectionConfigResponseBodyVpnConnectionConfig(DaraModel):
    def __init__(
        self,
        bgp_configs: main_models.DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigBgpConfigs = None,
        ike_config: main_models.DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigIkeConfig = None,
        ipsec_config: main_models.DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigIpsecConfig = None,
        local: str = None,
        local_subnet: str = None,
        remote: str = None,
        remote_subnet: str = None,
        tunnels_config: main_models.DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigTunnelsConfig = None,
    ):
        self.bgp_configs = bgp_configs
        # The configurations of Phase 1 negotiations.
        self.ike_config = ike_config
        # The configurations of Phase 2 negotiations.
        self.ipsec_config = ipsec_config
        # The identifier of the customer gateway.
        self.local = local
        # The CIDR block on the data center side.
        self.local_subnet = local_subnet
        # The identifier of the VPN gateway.
        self.remote = remote
        # The CIDR block on the virtual private cloud (VPC) side.
        self.remote_subnet = remote_subnet
        # The tunnel configurations of the peer gateway device.
        # 
        # The parameters in **TunnelsConfig** are returned only when the IPsec-VPN connection supports the dual-tunnel mode.
        self.tunnels_config = tunnels_config

    def validate(self):
        if self.bgp_configs:
            self.bgp_configs.validate()
        if self.ike_config:
            self.ike_config.validate()
        if self.ipsec_config:
            self.ipsec_config.validate()
        if self.tunnels_config:
            self.tunnels_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bgp_configs is not None:
            result['BgpConfigs'] = self.bgp_configs.to_map()

        if self.ike_config is not None:
            result['IkeConfig'] = self.ike_config.to_map()

        if self.ipsec_config is not None:
            result['IpsecConfig'] = self.ipsec_config.to_map()

        if self.local is not None:
            result['Local'] = self.local

        if self.local_subnet is not None:
            result['LocalSubnet'] = self.local_subnet

        if self.remote is not None:
            result['Remote'] = self.remote

        if self.remote_subnet is not None:
            result['RemoteSubnet'] = self.remote_subnet

        if self.tunnels_config is not None:
            result['TunnelsConfig'] = self.tunnels_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgpConfigs') is not None:
            temp_model = main_models.DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigBgpConfigs()
            self.bgp_configs = temp_model.from_map(m.get('BgpConfigs'))

        if m.get('IkeConfig') is not None:
            temp_model = main_models.DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigIkeConfig()
            self.ike_config = temp_model.from_map(m.get('IkeConfig'))

        if m.get('IpsecConfig') is not None:
            temp_model = main_models.DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigIpsecConfig()
            self.ipsec_config = temp_model.from_map(m.get('IpsecConfig'))

        if m.get('Local') is not None:
            self.local = m.get('Local')

        if m.get('LocalSubnet') is not None:
            self.local_subnet = m.get('LocalSubnet')

        if m.get('Remote') is not None:
            self.remote = m.get('Remote')

        if m.get('RemoteSubnet') is not None:
            self.remote_subnet = m.get('RemoteSubnet')

        if m.get('TunnelsConfig') is not None:
            temp_model = main_models.DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigTunnelsConfig()
            self.tunnels_config = temp_model.from_map(m.get('TunnelsConfig'))

        return self

class DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigTunnelsConfig(DaraModel):
    def __init__(
        self,
        tunnel_config: List[main_models.DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigTunnelsConfigTunnelConfig] = None,
    ):
        self.tunnel_config = tunnel_config

    def validate(self):
        if self.tunnel_config:
            for v1 in self.tunnel_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TunnelConfig'] = []
        if self.tunnel_config is not None:
            for k1 in self.tunnel_config:
                result['TunnelConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tunnel_config = []
        if m.get('TunnelConfig') is not None:
            for k1 in m.get('TunnelConfig'):
                temp_model = main_models.DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigTunnelsConfigTunnelConfig()
                self.tunnel_config.append(temp_model.from_map(k1))

        return self

class DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigTunnelsConfigTunnelConfig(DaraModel):
    def __init__(
        self,
        ike_config: main_models.DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigTunnelsConfigTunnelConfigIkeConfig = None,
        ipsec_config: main_models.DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigTunnelsConfigTunnelConfigIpsecConfig = None,
        local: str = None,
        remote: str = None,
        tunnel_id: str = None,
    ):
        # The configurations of Phase 1 negotiations.
        self.ike_config = ike_config
        # The configurations of Phase 2 negotiations.
        self.ipsec_config = ipsec_config
        # The identifier of the tunnel on the data center side.
        self.local = local
        # The identifier of the tunnel on the Alibaba Cloud side.
        self.remote = remote
        # The tunnel ID.
        self.tunnel_id = tunnel_id

    def validate(self):
        if self.ike_config:
            self.ike_config.validate()
        if self.ipsec_config:
            self.ipsec_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ike_config is not None:
            result['IkeConfig'] = self.ike_config.to_map()

        if self.ipsec_config is not None:
            result['IpsecConfig'] = self.ipsec_config.to_map()

        if self.local is not None:
            result['Local'] = self.local

        if self.remote is not None:
            result['Remote'] = self.remote

        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IkeConfig') is not None:
            temp_model = main_models.DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigTunnelsConfigTunnelConfigIkeConfig()
            self.ike_config = temp_model.from_map(m.get('IkeConfig'))

        if m.get('IpsecConfig') is not None:
            temp_model = main_models.DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigTunnelsConfigTunnelConfigIpsecConfig()
            self.ipsec_config = temp_model.from_map(m.get('IpsecConfig'))

        if m.get('Local') is not None:
            self.local = m.get('Local')

        if m.get('Remote') is not None:
            self.remote = m.get('Remote')

        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')

        return self

class DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigTunnelsConfigTunnelConfigIpsecConfig(DaraModel):
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

class DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigTunnelsConfigTunnelConfigIkeConfig(DaraModel):
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
        # The IKE negotiation mode. Valid values:
        # 
        # *   **main**: This mode offers higher security during negotiations.
        # *   **aggressive**: This mode is faster and has a higher success rate.
        self.ike_mode = ike_mode
        # The DH group in the IKE phase.
        self.ike_pfs = ike_pfs
        # The IKE version.
        self.ike_version = ike_version
        # The identifier of the tunnel on the data center side.
        self.local_id = local_id
        # The pre-shared key.
        self.psk = psk
        # The identifier of the tunnel on the Alibaba Cloud side.
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

class DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigIpsecConfig(DaraModel):
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

class DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigIkeConfig(DaraModel):
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
        # The IKE negotiation mode. Valid values:
        # 
        # *   **main**: This mode offers higher security during negotiations.
        # *   **aggressive**: This mode is faster and has a higher success rate.
        self.ike_mode = ike_mode
        # The DH group in the IKE phase.
        self.ike_pfs = ike_pfs
        # The IKE version.
        self.ike_version = ike_version
        # The identifier of the customer gateway. FQDN and IP formats are supported. The default value is the IP address of the customer gateway.
        self.local_id = local_id
        # The pre-shared key.
        self.psk = psk
        # The identifier of the VPN gateway. FQDN and IP formats are supported. The default value is the IP address of the VPN gateway.
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

class DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigBgpConfigs(DaraModel):
    def __init__(
        self,
        bgp_config: List[main_models.DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigBgpConfigsBgpConfig] = None,
    ):
        self.bgp_config = bgp_config

    def validate(self):
        if self.bgp_config:
            for v1 in self.bgp_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BgpConfig'] = []
        if self.bgp_config is not None:
            for k1 in self.bgp_config:
                result['BgpConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bgp_config = []
        if m.get('BgpConfig') is not None:
            for k1 in m.get('BgpConfig'):
                temp_model = main_models.DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigBgpConfigsBgpConfig()
                self.bgp_config.append(temp_model.from_map(k1))

        return self

class DownloadVpnConnectionConfigResponseBodyVpnConnectionConfigBgpConfigsBgpConfig(DaraModel):
    def __init__(
        self,
        local_asn: str = None,
        local_bgp_ip: str = None,
        peer_asn: str = None,
        peer_bgp_ip: str = None,
        tunnel_cidr: str = None,
        tunnel_id: str = None,
    ):
        self.local_asn = local_asn
        self.local_bgp_ip = local_bgp_ip
        self.peer_asn = peer_asn
        self.peer_bgp_ip = peer_bgp_ip
        self.tunnel_cidr = tunnel_cidr
        self.tunnel_id = tunnel_id

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

        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id

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

        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')

        return self

