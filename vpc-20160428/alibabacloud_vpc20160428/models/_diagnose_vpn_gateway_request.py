# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DiagnoseVpnGatewayRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        ipsec_extend_info: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        vpn_gateway_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Check the connectivity of the destination address. Valid values:
        # 
        # *   **PrivateSourceIp**: the source IP address. The source IP address must be on the VPC side.
        # *   **PrivateDestinationIp**: the destination IP address. The destination IP address must be on the data center side.
        self.ipsec_extend_info = ipsec_extend_info
        # The region ID of the VPN gateway.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource to be diagnosed.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource.
        # 
        # Set the value to **Ipsec**, which specifies an IPsec-VPN connection.
        # 
        # This parameter is required.
        self.resource_type = resource_type
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.ipsec_extend_info is not None:
            result['IPsecExtendInfo'] = self.ipsec_extend_info

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.vpn_gateway_id is not None:
            result['VpnGatewayId'] = self.vpn_gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('IPsecExtendInfo') is not None:
            self.ipsec_extend_info = m.get('IPsecExtendInfo')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('VpnGatewayId') is not None:
            self.vpn_gateway_id = m.get('VpnGatewayId')

        return self

