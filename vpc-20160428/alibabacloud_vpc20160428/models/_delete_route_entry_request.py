# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DeleteRouteEntryRequest(DaraModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        dry_run: bool = None,
        next_hop_id: str = None,
        next_hop_list: List[main_models.DeleteRouteEntryRequestNextHopList] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_entry_id: str = None,
        route_table_id: str = None,
    ):
        # The destination CIDR block of the route. IPv4 CIDR blocks, IPv6 CIDR blocks, prefix list CIDR blocks, and prefix list instance IDs are supported. This parameter is mutually exclusive with the RouteEntryId parameter.
        # > If the **RouteEntryId** parameter is not specified, the **DestinationCidrBlock** and **RouteTableId** parameters are required. Configure the **NextHopId** or **NextHopList** parameter as needed.
        self.destination_cidr_block = destination_cidr_block
        # Specifies whether to perform a dry run. Valid values:
        # 
        # **true**: performs a dry run without deleting the route. The system checks the AccessKey pair, the authorization of the Resource Access Management (RAM) user, and the required parameters. If the check fails, the corresponding error is returned. If the check succeeds, the error code `DryRunOperation` is returned.
        # 
        # **false** (default): sends a normal request. After the check succeeds, a 2xx HTTP status code is returned and the route is deleted.
        self.dry_run = dry_run
        # The ID of the next hop instance.
        # 
        # - To delete a non-ECMP route, specify **NextHopId**. Do not specify **NextHopList**.
        # - To delete an ECMP route, specify **NextHopList**. Do not specify **NextHopId**.
        self.next_hop_id = next_hop_id
        # The information about the next hop instances of the ECMP route. A maximum of 16 next hop instances are supported.
        self.next_hop_list = next_hop_list
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the route table resides.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the route that you want to delete. This parameter is mutually exclusive with the DestinationCidrBlock parameter.
        # > If the **DestinationCidrBlock** parameter is not specified, the **RouteEntryId** parameter is required.
        self.route_entry_id = route_entry_id
        # The ID of the route table that contains the route.  
        # > If the **RouteEntryId** parameter is not specified, the **DestinationCidrBlock** and **RouteTableId** parameters are required. Configure the **NextHopId** or **NextHopList** parameter as needed.
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

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        self.next_hop_list = []
        if m.get('NextHopList') is not None:
            for k1 in m.get('NextHopList'):
                temp_model = main_models.DeleteRouteEntryRequestNextHopList()
                self.next_hop_list.append(temp_model.from_map(k1))

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

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

class DeleteRouteEntryRequestNextHopList(DaraModel):
    def __init__(
        self,
        next_hop_id: str = None,
        next_hop_type: str = None,
    ):
        # The ID of the next hop instance of the ECMP route. A maximum of 16 next hop instances are supported.
        self.next_hop_id = next_hop_id
        # The type of the next hop of the ECMP route. Set the value to **RouterInterface** (router interface). A maximum of 16 next hop instances are supported.
        self.next_hop_type = next_hop_type

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        return self

