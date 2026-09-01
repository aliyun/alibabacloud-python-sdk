# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DeleteRouteEntriesRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_entries: List[main_models.DeleteRouteEntriesRequestRouteEntries] = None,
    ):
        # Specifies whether to perform a dry run. Valid values:
        # 
        # **true**: performs a dry run without deleting routes. The system checks the AccessKey pair, the authorization of the Resource Access Management (RAM) user, and the required parameters. If the check fails, the corresponding error is returned. If the check passes, the error code `DryRunOperation` is returned.
        # 
        # **false** (default): sends a normal request. If the check passes, a 2xx HTTP status code is returned and the routes are deleted.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the route table resides.
        # 
        # You can call [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The information about the route entries to delete.
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
                temp_model = main_models.DeleteRouteEntriesRequestRouteEntries()
                self.route_entries.append(temp_model.from_map(k1))

        return self

class DeleteRouteEntriesRequestRouteEntries(DaraModel):
    def __init__(
        self,
        dst_cidr_block: str = None,
        next_hop: str = None,
        route_entry_id: str = None,
        route_table_id: str = None,
    ):
        # The destination CIDR block of the route entry to delete. IPv4 CIDR blocks, IPv6 CIDR blocks, and prefix list CIDR blocks are supported. You can specify up to 50 destination CIDR blocks.
        # 
        # > If the **RouteEntryId** parameter is not specified, the **DstCidrBlock** and **NextHop** parameters are required.
        self.dst_cidr_block = dst_cidr_block
        # The ID of the next hop instance to delete. You can specify up to 50 instance IDs.
        # 
        # > If the **RouteEntryId** parameter is not specified, the **DstCidrBlock** and **NextHop** parameters are required.
        self.next_hop = next_hop
        # The ID of the route entry to delete. You can specify up to 50 route entry IDs.
        # 
        # > If the **RouteEntryId** parameter is not specified, the **DstCidrBlock** and **NextHop** parameters are required.
        self.route_entry_id = route_entry_id
        # The ID of the route table that contains the route entry to delete. You can specify up to 50 route table IDs.
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
        if self.dst_cidr_block is not None:
            result['DstCidrBlock'] = self.dst_cidr_block

        if self.next_hop is not None:
            result['NextHop'] = self.next_hop

        if self.route_entry_id is not None:
            result['RouteEntryId'] = self.route_entry_id

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstCidrBlock') is not None:
            self.dst_cidr_block = m.get('DstCidrBlock')

        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')

        if m.get('RouteEntryId') is not None:
            self.route_entry_id = m.get('RouteEntryId')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

