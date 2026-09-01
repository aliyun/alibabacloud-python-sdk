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
        # The client CIDR block, which is the address range used to assign IP addresses to virtual network interface controllers (NICs) of clients.
        # 
        # > The client CIDR block cannot conflict with the VPC-side CIDR block.
        # 
        # This parameter is required.
        self.client_ip_pool = client_ip_pool
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run without creating the IPsec server. The system checks the required parameters, request format, and service limits. If the check fails, the corresponding error message is returned. If the check succeeds, `DryRunOperation` is returned.
        # 
        # - **false** (default): sends the request. After the request passes the check, the IPsec server is created.
        self.dry_run = dry_run
        # Specifies whether the configuration takes effect immediately. Valid values:
        # 
        # - **true**: Negotiation starts immediately after the configuration is complete.
        # 
        # - **false** (default): Negotiation starts when inbound traffic is detected.
        self.effect_immediately = effect_immediately
        # The parameter settings of Phase 1 negotiations. Valid values:
        # 
        # - **IkeVersion**: The version of the IKE protocol. Valid values: **ikev1** and **ikev2**. Default value: **ikev2**.
        # 
        # - **IkeMode**: The negotiation pattern of the IKE version. Default value: **main**.
        # 
        # - **IkeEncAlg**: The encryption algorithm used in Phase 1 negotiations. Default value: **aes**.
        # 
        # - **IkeAuthAlg**: The authentication algorithm used in Phase 1 negotiations. Default value: **sha1**.
        # 
        # - **IkePfs**: The Diffie-Hellman key exchange algorithm used in Phase 1 negotiations. Default value: **group2**.
        # 
        # - **IkeLifetime**: The epoch of the security association (SA) negotiated in Phase 1. Unit: seconds. Valid values: **0** to **86400**. Default value: **86400**.
        # 
        # - **LocalId**: The identity of the IPsec server. The FQDN and IP address formats are supported. Default value: the public IP address of the VPN gateway.
        # 
        # - **RemoteId**: The identity of the peer. The FQDN and IP address formats are supported. Default value: empty.
        self.ike_config = ike_config
        # The name of the IPsec server.
        # 
        # The name must be 1 to 100 characters in length.
        self.ip_sec_server_name = ip_sec_server_name
        # The parameter settings of Phase 2 negotiations. Valid values:
        # 
        # - **IpsecEncAlg**: The encryption algorithm used in Phase 2 negotiations. Default value: **aes**.
        # 
        # - **IpsecAuthAlg**: The authentication algorithm used in Phase 2 negotiations. Default value: **sha1**.
        # 
        # - **IpsecPfs**: Forward all protocol packets. The Diffie-Hellman key exchange algorithm used in Phase 2 negotiations. Default value: **group2**.
        # 
        # - **IpsecLifetime**: The epoch of the SA negotiated in Phase 2. Unit: seconds. Valid values: **0** to **86400**. Default value: **86400**.
        self.ipsec_config = ipsec_config
        # The local CIDR block, which is the VPC-side CIDR block that needs to communicate with the client CIDR block.
        # 
        # Separate multiple CIDR blocks with commas (,). Example: 192.168.1.0/24,192.168.2.0/24.
        # 
        # This parameter is required.
        self.local_subnet = local_subnet
        # The pre-shared key.
        # 
        # The pre-shared key is used for identity authentication between the IPsec server and the client. The key must be 1 to 100 characters in length.
        # 
        # If you do not specify a pre-shared key, the system randomly generates a 16-character string as the pre-shared key. You can call the [ListIpsecServers](https://help.aliyun.com/document_detail/2794120.html) operation to query the pre-shared key generated by the system.
        # 
        # > The pre-shared key of the IPsec server must be the same as the authentication key of the client. Otherwise, a connection cannot be established between the IPsec server and the client.
        self.psk = psk
        # Specifies whether to enable pre-shared key authentication. Valid values: **true**, which indicates that pre-shared key authentication is enabled.
        # 
        # > This parameter is required.
        self.psk_enabled = psk_enabled
        # The region ID of the VPN gateway.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The instance ID of the VPN gateway.
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

