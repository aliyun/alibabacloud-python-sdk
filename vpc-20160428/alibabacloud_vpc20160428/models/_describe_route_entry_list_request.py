# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeRouteEntryListRequest(DaraModel):
    def __init__(
        self,
        dest_cidr_block_list: List[str] = None,
        destination_cidr_block: str = None,
        ip_version: str = None,
        max_result: int = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_entry_id: str = None,
        route_entry_name: str = None,
        route_entry_type: str = None,
        route_table_id: str = None,
        service_type: str = None,
    ):
        # The list of destination CIDR blocks of route entries.
        self.dest_cidr_block_list = dest_cidr_block_list
        # The destination CIDR block of the route entry. Both IPv4 and IPv6 CIDR blocks are supported.
        self.destination_cidr_block = destination_cidr_block
        # The version of the IP protocol. Valid values:
        # 
        # - **ipv4**: IPv4 protocol.
        # 
        # - **ipv6**: IPv6 protocol.
        self.ip_version = ip_version
        # The number of entries to return per page during a paged query. Valid values: **1** to **100**. Default value: **10**.
        self.max_result = max_result
        # The ID of the next hop instance.
        self.next_hop_id = next_hop_id
        # The type of the next hop. Valid values:
        # 
        # - **Instance** (default): ECS instance.
        # 
        # - **HaVip**: high-availability virtual IP address (HAVIP).
        # 
        # - **VpnGateway**: VPN gateway.
        # 
        # - **NatGateway**: NAT gateway.
        # 
        # - **NetworkInterface**: secondary elastic network interface.
        # 
        # - **RouterInterface**: router interface.
        # 
        # - **IPv6Gateway**: IPv6 gateway.
        # 
        # - **Attachment**: transit router.
        # - **Ipv4Gateway**: IPv4 gateway.
        # - **GatewayEndpoint**: gateway endpoint.
        # - **Ecr**: Express Connect Router.
        self.next_hop_type = next_hop_type
        # Specifies whether a next query token (Token) exists. Valid values:
        # - You do not need to specify this parameter for the first query or if no next query exists.
        # - If a next query exists, set the value to the NextToken value returned from the previous API call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the route table to which the route entry belongs.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the route entry to query.
        self.route_entry_id = route_entry_id
        # The name of the route entry.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.route_entry_name = route_entry_name
        # The type of the route. Valid values:
        # 
        # - **Custom**: custom route.
        # - **System**: system route.
        # - **BGP**: BGP route.
        # - **CEN**: Cloud Enterprise Network (CEN) route.
        # - **ECR**: Express Connect Router route.
        self.route_entry_type = route_entry_type
        # The ID of the route table to query.
        # 
        # This parameter is required.
        self.route_table_id = route_table_id
        # The type of route service. If this field is empty, it indicates that the route is not managed.
        # 
        # Valid value: **TR**, which indicates that the managed type is transit router.
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dest_cidr_block_list is not None:
            result['DestCidrBlockList'] = self.dest_cidr_block_list

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.max_result is not None:
            result['MaxResult'] = self.max_result

        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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

        if self.route_entry_id is not None:
            result['RouteEntryId'] = self.route_entry_id

        if self.route_entry_name is not None:
            result['RouteEntryName'] = self.route_entry_name

        if self.route_entry_type is not None:
            result['RouteEntryType'] = self.route_entry_type

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestCidrBlockList') is not None:
            self.dest_cidr_block_list = m.get('DestCidrBlockList')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')

        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

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

        if m.get('RouteEntryId') is not None:
            self.route_entry_id = m.get('RouteEntryId')

        if m.get('RouteEntryName') is not None:
            self.route_entry_name = m.get('RouteEntryName')

        if m.get('RouteEntryType') is not None:
            self.route_entry_type = m.get('RouteEntryType')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        return self

