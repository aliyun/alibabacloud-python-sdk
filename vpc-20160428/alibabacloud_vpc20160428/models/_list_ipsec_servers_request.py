# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListIpsecServersRequest(DaraModel):
    def __init__(
        self,
        ipsec_server_id: List[str] = None,
        ipsec_server_name: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        vpn_gateway_id: str = None,
    ):
        # The ID of the IPsec server.
        self.ipsec_server_id = ipsec_server_id
        # The name of the IPsec server.
        # 
        # The name must be 1 to 100 characters in length.
        self.ipsec_server_name = ipsec_server_name
        # The number of entries to return on each page. Valid values: **1** to **20**. Default value: **10**.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If this is your first request and no next requests are to be performed, you do not need to specify this parameter.
        # *   You must specify the token that is obtained from the previous query as the value of **NextToken**.
        self.next_token = next_token
        # The ID of the region where the IPsec server is created.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the IPsec server belongs.
        # 
        # The IPsec server and its associated VPN gateway belong to the same resource group. You can call [DescribeVpnGateway](https://help.aliyun.com/document_detail/2794055.html) to query the ID of the resource group to which the VPN gateway belongs.
        self.resource_group_id = resource_group_id
        # The ID of the VPN gateway.
        self.vpn_gateway_id = vpn_gateway_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipsec_server_id is not None:
            result['IpsecServerId'] = self.ipsec_server_id

        if self.ipsec_server_name is not None:
            result['IpsecServerName'] = self.ipsec_server_name

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.vpn_gateway_id is not None:
            result['VpnGatewayId'] = self.vpn_gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpsecServerId') is not None:
            self.ipsec_server_id = m.get('IpsecServerId')

        if m.get('IpsecServerName') is not None:
            self.ipsec_server_name = m.get('IpsecServerName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('VpnGatewayId') is not None:
            self.vpn_gateway_id = m.get('VpnGatewayId')

        return self

