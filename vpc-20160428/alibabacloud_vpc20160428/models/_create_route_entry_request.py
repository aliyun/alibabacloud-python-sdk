# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateRouteEntryRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        destination_cidr_block: str = None,
        dry_run: bool = None,
        next_hop_id: str = None,
        next_hop_list: List[main_models.CreateRouteEntryRequestNextHopList] = None,
        next_hop_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_entry_name: str = None,
        route_table_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # Generate a parameter value from your client. Make sure that the value is unique among different requests. The ClientToken value can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # The description of the custom route entry.
        # 
        # The description must be 1 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The destination CIDR block of the custom route entry. IPv4 CIDR blocks, IPv6 CIDR blocks, destination CIDR blocks of prefix lists, and instance IDs of prefix lists are supported. The following requirements must be met:
        #           
        # - The destination CIDR block cannot point to or be contained by 100.64.0.0/10.  
        #  
        # - The destination CIDR blocks of different route entries in the same route table must be unique.
        # 
        # This parameter is required.
        self.destination_cidr_block = destination_cidr_block
        # Specifies whether to perform a dry run. Valid values:
        # - **true**: performs a dry run. The system checks the required parameters, request format, and business restrictions. If the request fails the dry run, the corresponding error is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # - **false** (default): sends a normal request, passes the dry run, and returns an HTTP 2xx status code. The route is directly created.
        self.dry_run = dry_run
        # The ID of the next hop instance of the custom route entry.
        # > If you set NextHopType to ECR, you can call the [DescribeExpressConnectRouterAssociation](https://help.aliyun.com/document_detail/2712069.html) operation to obtain the AssociationId as the next hop ID.
        # > -.
        self.next_hop_id = next_hop_id
        # The information about the next hops.
        self.next_hop_list = next_hop_list
        # The type of next hop of the custom route entry. Valid values: 
        # 
        # - **Instance** (default): ECS instance.
        # 
        # - **HaVip**: high-availability virtual IP address.  
        # 
        # - **RouterInterface**: vRouter interface.
        # 
        # - **NetworkInterface**: network interface controller (NIC).
        # 
        # - **VpnGateway**: VPN gateway.
        # 
        # - **IPv6Gateway**: IPv6 gateway.
        # 
        # - **NatGateway**: NAT gateway.
        # 
        # - **Attachment**: transit router.
        # 
        # - **VpcPeer**: VPC peering connection.
        # - **Ipv4Gateway**: IPv4 gateway.
        # - **GatewayEndpoint**: gateway endpoint.
        # - **Ecr**: Express Connect Router (ECR).
        # - **GatewayLoadBalancerEndpoint**: Gateway Load Balancer endpoint (GWLBe).
        self.next_hop_type = next_hop_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the route table.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the custom route entry to add.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.route_entry_name = route_entry_name
        # The ID of the route table to which you want to add a custom route entry.
        # 
        # This parameter is required.
        self.route_table_id = route_table_id

    def validate(self):
        if self.next_hop_list:
            for v1 in self.next_hop_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id

        result['NextHopList'] = []
        if self.next_hop_list is not None:
            for k1 in self.next_hop_list:
                result['NextHopList'].append(k1.to_map() if k1 else None)

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

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

        if self.route_entry_name is not None:
            result['RouteEntryName'] = self.route_entry_name

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        self.next_hop_list = []
        if m.get('NextHopList') is not None:
            for k1 in m.get('NextHopList'):
                temp_model = main_models.CreateRouteEntryRequestNextHopList()
                self.next_hop_list.append(temp_model.from_map(k1))

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

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

        if m.get('RouteEntryName') is not None:
            self.route_entry_name = m.get('RouteEntryName')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

class CreateRouteEntryRequestNextHopList(DaraModel):
    def __init__(
        self,
        next_hop_id: str = None,
        next_hop_type: str = None,
        weight: int = None,
    ):
        # The ID of the next hop instance of the ECMP route.
        self.next_hop_id = next_hop_id
        # The type of next hop of the ECMP route. Valid value: **RouterInterface** (router interface).
        self.next_hop_type = next_hop_type
        # The weight of the next hop of the ECMP route.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

