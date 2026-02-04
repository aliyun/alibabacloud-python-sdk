# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListTransitRouterPrefixListAssociationResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        prefix_lists: List[main_models.ListTransitRouterPrefixListAssociationResponseBodyPrefixLists] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # A list of prefix lists.
        self.prefix_lists = prefix_lists
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.prefix_lists:
            for v1 in self.prefix_lists:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['PrefixLists'] = []
        if self.prefix_lists is not None:
            for k1 in self.prefix_lists:
                result['PrefixLists'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.prefix_lists = []
        if m.get('PrefixLists') is not None:
            for k1 in m.get('PrefixLists'):
                temp_model = main_models.ListTransitRouterPrefixListAssociationResponseBodyPrefixLists()
                self.prefix_lists.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTransitRouterPrefixListAssociationResponseBodyPrefixLists(DaraModel):
    def __init__(
        self,
        next_hop: str = None,
        next_hop_instance_id: str = None,
        next_hop_type: str = None,
        owner_uid: int = None,
        prefix_list_id: str = None,
        status: str = None,
        transit_router_id: str = None,
        transit_router_table_id: str = None,
    ):
        # The ID of the next hop.
        # 
        # > A value of **BlackHole** indicates that all the CIDR blocks in the prefix list are blackhole routes. Packets destined for the CIDR blocks are dropped.
        self.next_hop = next_hop
        # The ID of the network instance associated with the next hop connection.
        self.next_hop_instance_id = next_hop_instance_id
        # The type of the next hop. Valid values:
        # 
        # *   **BlackHole**: All the CIDR blocks in the prefix list are blackhole routes. Packets destined for the CIDR blocks are dropped.
        # *   **VPC**: The next hop of the CIDR blocks in the prefix list is a VPC connection.
        # *   **VBR**: The next hop of the CIDR blocks in the prefix list is a VBR connection.
        # *   **TR**: The next hop of the CIDR blocks in the prefix list is an inter-region connection.
        self.next_hop_type = next_hop_type
        # The ID of the Alibaba Cloud account to which the prefix list belongs.
        self.owner_uid = owner_uid
        # The ID of the prefix list.
        self.prefix_list_id = prefix_list_id
        # The status of the prefix list. Valid values:
        # 
        # *   **Active**: The prefix list is effective.
        # *   **Updating**: The prefix list is being updated.
        self.status = status
        # The ID of the transit router.
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

        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid

        if self.prefix_list_id is not None:
            result['PrefixListId'] = self.prefix_list_id

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

        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')

        if m.get('PrefixListId') is not None:
            self.prefix_list_id = m.get('PrefixListId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('TransitRouterTableId') is not None:
            self.transit_router_table_id = m.get('TransitRouterTableId')

        return self

