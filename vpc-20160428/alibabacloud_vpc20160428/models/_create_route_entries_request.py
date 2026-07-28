# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateRouteEntriesRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_entries: List[main_models.CreateRouteEntriesRequestRouteEntries] = None,
    ):
        # Specifies whether to perform a dry run. Valid values:
        # 
        # **true**: performs a dry run without creating routes. The system checks the AccessKey pair, the authorization of the Resource Access Management (RAM) user, and the required parameters. If the check fails, the corresponding error is returned. If the check passes, the `DryRunOperation` error code is returned.
        # 
        # **false** (default): sends a Normal request. If the check passes, a 2xx HTTP status code is returned and the routes are created.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the route table.
        # 
        # You can call [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of route entry information.
        # 
        # This parameter is required.
        self.route_entries = route_entries

    def validate(self):
        if self.route_entries:
            for v1 in self.route_entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

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

        result['RouteEntries'] = []
        if self.route_entries is not None:
            for k1 in self.route_entries:
                result['RouteEntries'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

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

        self.route_entries = []
        if m.get('RouteEntries') is not None:
            for k1 in m.get('RouteEntries'):
                temp_model = main_models.CreateRouteEntriesRequestRouteEntries()
                self.route_entries.append(temp_model.from_map(k1))

        return self

class CreateRouteEntriesRequestRouteEntries(DaraModel):
    def __init__(
        self,
        description: str = None,
        dst_cidr_block: str = None,
        ip_version: int = None,
        name: str = None,
        next_hop: str = None,
        next_hop_type: str = None,
        route_table_id: str = None,
    ):
        # The description of the custom route entry. You can specify a maximum of 50 descriptions.
        # 
        # The description must be 1 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The destination CIDR block of the custom route entry. Both IPv4 and IPv6 destination CIDR blocks are supported. You can specify a maximum of 50 destination CIDR blocks. The following requirements must be met:
        #           
        # - The destination CIDR block cannot point to or be contained by 100.64.0.0/10.  
        #  
        # - The destination CIDR blocks of different route entries in the same route table must be unique.
        # 
        # This parameter is required.
        self.dst_cidr_block = dst_cidr_block
        # The version of the IP protocol. You can specify a maximum of 50 IP protocol versions. Valid values:
        # 
        # - **4**: IPv4.
        # - **6**: IPv6.
        self.ip_version = ip_version
        # The name of the custom route entry to add. You can specify a maximum of 50 names.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.name = name
        # The ID of the next hop instance for the custom route entry. You can specify a maximum of 50 instance IDs.
        # > If NextHopType is set to ECR, you can call [DescribeExpressConnectRouterAssociation](https://help.aliyun.com/document_detail/2712069.html) to obtain the AssociationId as the next hop ID.
        # 
        # This parameter is required.
        self.next_hop = next_hop
        # The type of the next hop for the custom route entry. You can specify a maximum of 50 next hop types. Valid values: 
        # 
        # - **Instance** (default): ECS instance. Forwards traffic to an ECS instance.
        # 
        # - **HaVip**: high-availability virtual IP address.  
        # 
        # - **RouterInterface**: vRouter interface.
        # 
        # - **NetworkInterface**: elastic network interfaces (ENIs).
        # 
        # - **VpnGateway**: VPN gateway.
        # 
        # - **IPv6Gateway**: IPv6 gateway.
        # 
        # - **NatGateway**: NAT gateway.
        # 
        # - **Attachment**: transit router. Forwards traffic to a transit router.
        # 
        # - **VpcPeer**: VPC peering connection.
        # - **Ipv4Gateway**: IPv4 gateway.
        # - **GatewayEndpoint**: gateway endpoint.
        # - **CenBasic**: CEN that does not support transit routers.
        # - **Ecr**: Express Connect Router (ECR).
        # - **GatewayLoadBalancerEndpoint**: Gateway Load Balancer endpoint (GWLBe).
        # - **RouteTargetGroup**: routing target group.
        # 
        # This parameter is required.
        self.next_hop_type = next_hop_type
        # The ID of the route table to which you want to add the custom route entry. You can specify a maximum of 50 route table IDs.
        # 
        # This parameter is required.
        self.route_table_id = route_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.dst_cidr_block is not None:
            result['DstCidrBlock'] = self.dst_cidr_block

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.name is not None:
            result['Name'] = self.name

        if self.next_hop is not None:
            result['NextHop'] = self.next_hop

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DstCidrBlock') is not None:
            self.dst_cidr_block = m.get('DstCidrBlock')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

