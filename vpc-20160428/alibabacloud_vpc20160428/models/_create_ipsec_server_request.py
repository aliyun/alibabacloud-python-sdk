# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIpsecServerRequest(DaraModel):
    def __init__(
        self,
        client_ip_pool: str = None,
        client_token: str = None,
        dry_run: str = None,
        effect_immediately: bool = None,
        ike_config: str = None,
        ip_sec_server_name: str = None,
        ipsec_config: str = None,
        local_subnet: str = None,
        psk: str = None,
        psk_enabled: bool = None,
        region_id: str = None,
        vpn_gateway_id: str = None,
    ):
        # The client CIDR block from which an IP address is allocated to the virtual network interface controller (NIC) of the client.
        # 
        # >  The client CIDR block must not overlap with the CIDR blocks of the VPC.
        # 
        # This parameter is required.
        self.client_ip_pool = client_ip_pool
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to only precheck this request. Valid values:
        # 
        # *   **true**: prechecks the request without creating the IPsec server. The system checks the required parameters, request format, and service limits. If the request fails to pass the precheck, an error code is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. This is the default value. If the request passes the precheck, the system creates the IPsec server.
        self.dry_run = dry_run
        # Specify whether to start connection negotiations immediately. Valid values:
        # 
        # *   **true**: immediately initiates negotiations after the configuration is complete.
        # *   **false** (default): initiates negotiations when inbound traffic is detected. This is the default value.
        self.effect_immediately = effect_immediately
        # The configuration of Phase 1 negotiation. Valid values:
        # 
        # *   **IkeVersion**: the IKE version. Valid values: **ikev1** and **ikev2**. Default value: **ikev2**.
        # *   **IkeMode**: the IKE negotiation mode. Default value: **main**.
        # *   **IkeEncAlg**: the encryption algorithm that is used in Phase 1 negotiation. Default value: **aes**.
        # *   **IkeAuthAlg**: the authentication algorithm that is used in Phase 1 negotiation. Default value: **sha1**.
        # *   **IkePfs**: the Diffie-Hellman key exchange algorithm that is used in Phase 1 negotiation. Default value: **group2**.
        # *   **IkeLifetime**: the security association (SA) lifetime determined by Phase 1 negotiation. Unit: seconds. Valid values: **0** to **86400**. Default value: **86400**.
        # *   **LocalId**: the identifier of the IPsec server. The value can be a fully qualified domain name (FQDN) or an IP address. The default value is the public IP address of the VPN gateway.
        # *   **RemoteId**: the peer identifier. The value can be an FQDN or an IP address. The default value is empty.
        self.ike_config = ike_config
        # The name of the IPsec server.
        # 
        # The name must be 1 to 100 characters in length.
        self.ip_sec_server_name = ip_sec_server_name
        # The configuration of Phase 2 negotiation. Valid values:
        # 
        # *   **IpsecEncAlg**: the encryption algorithm that is used in Phase 2 negotiation. Default value: **aes**.
        # *   **IpsecAuthAlg**: the authentication algorithm that is used in Phase 2 negotiation. Default value: **sha1**.
        # *   **IpsecPfs**: forwards packets of all protocols. The Diffie-Hellman key exchange algorithm that is used in Phase 2 negotiation. Default value: **group2**.
        # *   **IpsecLifetime**: the SA lifetime determined by Phase 2 negotiation. Unit: seconds. Valid values: **0** to **86400**. Default value: **86400**.
        self.ipsec_config = ipsec_config
        # The local CIDR blocks, which are the CIDR blocks of the virtual private cloud (VPC) for the client to access.
        # 
        # Multiple CIDR blocks are separated with commas (,). Example: 192.168.1.0/24,192.168.2.0/24.
        # 
        # This parameter is required.
        self.local_subnet = local_subnet
        # The pre-shared key.
        # 
        # The pre-shared key that is used for authentication between the IPsec-VPN server and the client. It must be 1 to 100 characters in length.
        # 
        # If you do not specify a pre-shared key, the system randomly generates a 16-bit string as the pre-shared key. You can call [ListIpsecServers](https://help.aliyun.com/document_detail/2794120.html) to query keys generated by the system.
        # 
        # > The pre-shared key of the IPsec server key must be the same as that of the client. Otherwise, the connection between the IPsec server and the client cannot be established.
        self.psk = psk
        # Indicates whether pre-shared key authentication is enabled. If you set the value to **true**, pre-shared key authentication is enabled.
        # 
        # >  This parameter is required.
        self.psk_enabled = psk_enabled
        # The ID of the region where the VPN gateway is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the VPN gateway.
        # 
        # This parameter is required.
        self.vpn_gateway_id = vpn_gateway_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip_pool is not None:
            result['ClientIpPool'] = self.client_ip_pool

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.effect_immediately is not None:
            result['EffectImmediately'] = self.effect_immediately

        if self.ike_config is not None:
            result['IkeConfig'] = self.ike_config

        if self.ip_sec_server_name is not None:
            result['IpSecServerName'] = self.ip_sec_server_name

        if self.ipsec_config is not None:
            result['IpsecConfig'] = self.ipsec_config

        if self.local_subnet is not None:
            result['LocalSubnet'] = self.local_subnet

        if self.psk is not None:
            result['Psk'] = self.psk

        if self.psk_enabled is not None:
            result['PskEnabled'] = self.psk_enabled

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vpn_gateway_id is not None:
            result['VpnGatewayId'] = self.vpn_gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIpPool') is not None:
            self.client_ip_pool = m.get('ClientIpPool')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EffectImmediately') is not None:
            self.effect_immediately = m.get('EffectImmediately')

        if m.get('IkeConfig') is not None:
            self.ike_config = m.get('IkeConfig')

        if m.get('IpSecServerName') is not None:
            self.ip_sec_server_name = m.get('IpSecServerName')

        if m.get('IpsecConfig') is not None:
            self.ipsec_config = m.get('IpsecConfig')

        if m.get('LocalSubnet') is not None:
            self.local_subnet = m.get('LocalSubnet')

        if m.get('Psk') is not None:
            self.psk = m.get('Psk')

        if m.get('PskEnabled') is not None:
            self.psk_enabled = m.get('PskEnabled')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VpnGatewayId') is not None:
            self.vpn_gateway_id = m.get('VpnGatewayId')

        return self

