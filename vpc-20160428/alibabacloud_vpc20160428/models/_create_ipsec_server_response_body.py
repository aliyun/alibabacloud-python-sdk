# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIpsecServerResponseBody(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        ipsec_server_id: str = None,
        ipsec_server_name: str = None,
        region_id: str = None,
        request_id: str = None,
        vpn_gateway_id: str = None,
    ):
        # The time when the IPsec server was created.
        # 
        # T is used as a delimiter. Z indicates that the time is in UTC.
        self.creation_time = creation_time
        # The IPsec server ID.
        self.ipsec_server_id = ipsec_server_id
        # The IPsec server name.
        self.ipsec_server_name = ipsec_server_name
        # The ID of the region where the VPN gateway is deployed.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The ID of the VPN gateway.
        self.vpn_gateway_id = vpn_gateway_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.ipsec_server_id is not None:
            result['IpsecServerId'] = self.ipsec_server_id

        if self.ipsec_server_name is not None:
            result['IpsecServerName'] = self.ipsec_server_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vpn_gateway_id is not None:
            result['VpnGatewayId'] = self.vpn_gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('IpsecServerId') is not None:
            self.ipsec_server_id = m.get('IpsecServerId')

        if m.get('IpsecServerName') is not None:
            self.ipsec_server_name = m.get('IpsecServerName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VpnGatewayId') is not None:
            self.vpn_gateway_id = m.get('VpnGatewayId')

        return self

