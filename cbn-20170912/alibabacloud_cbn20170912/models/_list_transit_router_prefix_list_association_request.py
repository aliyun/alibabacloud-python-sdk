# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTransitRouterPrefixListAssociationRequest(DaraModel):
    def __init__(
        self,
        next_hop: str = None,
        next_hop_instance_id: str = None,
        next_hop_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        owner_uid: int = None,
        page_number: int = None,
        page_size: int = None,
        prefix_list_id: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
        transit_router_id: str = None,
        transit_router_table_id: str = None,
    ):
        # The ID of the next hop.
        # 
        # > Set the value to **BlackHole** if you want to query the prefix list that generates blackhole routes.
        self.next_hop = next_hop
        # The ID of the network instance associated with the next hop connection.
        self.next_hop_instance_id = next_hop_instance_id
        # The type of the next hop. Valid values:
        # 
        # *   **BlackHole**: The prefix list that generates blackhole routes.
        # *   **VPC**: The prefix list whose next hop is a virtual private cloud (VPC) connection.
        # *   **VBR**: The prefix list whose next hop is a virtual border router (VBR) connection.
        # *   **TR**: The prefix list whose next hop is an inter-region connection on the transit router.
        self.next_hop_type = next_hop_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the Alibaba Cloud account to which the prefix list belongs.
        self.owner_uid = owner_uid
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: **100**. Default value: **10**.
        self.page_size = page_size
        # The ID of the prefix list.
        self.prefix_list_id = prefix_list_id
        # The ID of the region where the transit router is deployed.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The status of the prefix list. Valid values:
        # 
        # *   **Active**
        # *   **Updating**
        self.status = status
        # The ID of the transit router.
        # 
        # This parameter is required.
        self.transit_router_id = transit_router_id
        # The ID of the route table of the transit router.
        self.transit_router_table_id = transit_router_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_hop is not None:
            result['NextHop'] = self.next_hop

        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.prefix_list_id is not None:
            result['PrefixListId'] = self.prefix_list_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.status is not None:
            result['Status'] = self.status

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.transit_router_table_id is not None:
            result['TransitRouterTableId'] = self.transit_router_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')

        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrefixListId') is not None:
            self.prefix_list_id = m.get('PrefixListId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('TransitRouterTableId') is not None:
            self.transit_router_table_id = m.get('TransitRouterTableId')

        return self

