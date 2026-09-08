# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListTransitRouterRouteEntriesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        prefix_list_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_filter: List[main_models.ListTransitRouterRouteEntriesRequestRouteFilter] = None,
        transit_router_route_entry_destination_cidr_block: str = None,
        transit_router_route_entry_ids: List[str] = None,
        transit_router_route_entry_names: List[str] = None,
        transit_router_route_entry_next_hop_id: str = None,
        transit_router_route_entry_next_hop_resource_id: str = None,
        transit_router_route_entry_next_hop_resource_type: str = None,
        transit_router_route_entry_next_hop_type: str = None,
        transit_router_route_entry_origin_resource_id: str = None,
        transit_router_route_entry_origin_resource_type: str = None,
        transit_router_route_entry_status: str = None,
        transit_router_route_entry_type: str = None,
        transit_router_route_table_id: str = None,
    ):
        # The number of entries per page when entries are returned in pages. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The token that determines the start point of the query. Valid values:
        # 
        # - You do not need to specify this parameter for the first query or if no subsequent query is to be sent.
        # - If a subsequent query is to be sent, set the value to the **NextToken** value returned by the previous API call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the prefix list.
        self.prefix_list_id = prefix_list_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The filter conditions for route entry CIDR blocks.
        self.route_filter = route_filter
        # The destination CIDR block of the route entry (**This parameter will be deprecated. Use the RouteFilter parameter instead**).
        self.transit_router_route_entry_destination_cidr_block = transit_router_route_entry_destination_cidr_block
        # The IDs of the route entries.
        self.transit_router_route_entry_ids = transit_router_route_entry_ids
        # The names of the route entries.
        self.transit_router_route_entry_names = transit_router_route_entry_names
        # The ID of the network instance connection associated with the next hop of the route entry.
        self.transit_router_route_entry_next_hop_id = transit_router_route_entry_next_hop_id
        # The instance ID of the next hop of the route entry.
        self.transit_router_route_entry_next_hop_resource_id = transit_router_route_entry_next_hop_resource_id
        # The type of the next hop instance of the route entry. Valid values:
        # 
        # - **VPC**: Virtual Private Cloud (VPC) instance.
        # - **VBR**: Virtual Border Router (VBR) instance.
        # - **TR**: transit router instance.
        # - **VPN**: IPsec connection instance.
        self.transit_router_route_entry_next_hop_resource_type = transit_router_route_entry_next_hop_resource_type
        # The next hop type. Valid values:
        # 
        # - **BlackHole**: the route entry is a blackhole route.
        # - **Attachment**: the next hop of the route entry is a network instance connection.
        self.transit_router_route_entry_next_hop_type = transit_router_route_entry_next_hop_type
        # The instance ID of the origin of the route entry.
        self.transit_router_route_entry_origin_resource_id = transit_router_route_entry_origin_resource_id
        # The type of the origin instance of the route entry. Valid values:
        # 
        # - **VPC**: Virtual Private Cloud (VPC) instance.
        # - **VBR**: Virtual Border Router (VBR) instance.
        # - **TR**: transit router instance.
        # - **VPN**: IPsec connection instance.
        self.transit_router_route_entry_origin_resource_type = transit_router_route_entry_origin_resource_type
        # The status of the route entry. Valid values:
        # 
        # - **All**: queries route entries in all states.
        # - **Active (default)**: queries only route entries in the active state.
        # - **Rejected**: queries only route entries that are rejected due to route conflicts.
        # - **Prohibited**: queries only route entries that are prohibited because they match a routing policy.
        # - **Standby**: queries only route entries that serve as standby routes.
        # - **Candidate**: queries only route entries that serve as candidate routes.
        # 
        # If you do not specify this parameter, only route entries in the active state are queried.
        self.transit_router_route_entry_status = transit_router_route_entry_status
        # The type of the route entry. Valid values:
        # 
        # - **Propagated**: generated by automatic learning on the current route table.
        # - **Static**: generated by static configuration on the current route table.
        self.transit_router_route_entry_type = transit_router_route_entry_type
        # The ID of the Enterprise Edition transit router route table.
        # 
        # This parameter is required.
        self.transit_router_route_table_id = transit_router_route_table_id

    def validate(self):
        if self.route_filter:
            for v1 in self.route_filter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.prefix_list_id is not None:
            result['PrefixListId'] = self.prefix_list_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['RouteFilter'] = []
        if self.route_filter is not None:
            for k1 in self.route_filter:
                result['RouteFilter'].append(k1.to_map() if k1 else None)

        if self.transit_router_route_entry_destination_cidr_block is not None:
            result['TransitRouterRouteEntryDestinationCidrBlock'] = self.transit_router_route_entry_destination_cidr_block

        if self.transit_router_route_entry_ids is not None:
            result['TransitRouterRouteEntryIds'] = self.transit_router_route_entry_ids

        if self.transit_router_route_entry_names is not None:
            result['TransitRouterRouteEntryNames'] = self.transit_router_route_entry_names

        if self.transit_router_route_entry_next_hop_id is not None:
            result['TransitRouterRouteEntryNextHopId'] = self.transit_router_route_entry_next_hop_id

        if self.transit_router_route_entry_next_hop_resource_id is not None:
            result['TransitRouterRouteEntryNextHopResourceId'] = self.transit_router_route_entry_next_hop_resource_id

        if self.transit_router_route_entry_next_hop_resource_type is not None:
            result['TransitRouterRouteEntryNextHopResourceType'] = self.transit_router_route_entry_next_hop_resource_type

        if self.transit_router_route_entry_next_hop_type is not None:
            result['TransitRouterRouteEntryNextHopType'] = self.transit_router_route_entry_next_hop_type

        if self.transit_router_route_entry_origin_resource_id is not None:
            result['TransitRouterRouteEntryOriginResourceId'] = self.transit_router_route_entry_origin_resource_id

        if self.transit_router_route_entry_origin_resource_type is not None:
            result['TransitRouterRouteEntryOriginResourceType'] = self.transit_router_route_entry_origin_resource_type

        if self.transit_router_route_entry_status is not None:
            result['TransitRouterRouteEntryStatus'] = self.transit_router_route_entry_status

        if self.transit_router_route_entry_type is not None:
            result['TransitRouterRouteEntryType'] = self.transit_router_route_entry_type

        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrefixListId') is not None:
            self.prefix_list_id = m.get('PrefixListId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.route_filter = []
        if m.get('RouteFilter') is not None:
            for k1 in m.get('RouteFilter'):
                temp_model = main_models.ListTransitRouterRouteEntriesRequestRouteFilter()
                self.route_filter.append(temp_model.from_map(k1))

        if m.get('TransitRouterRouteEntryDestinationCidrBlock') is not None:
            self.transit_router_route_entry_destination_cidr_block = m.get('TransitRouterRouteEntryDestinationCidrBlock')

        if m.get('TransitRouterRouteEntryIds') is not None:
            self.transit_router_route_entry_ids = m.get('TransitRouterRouteEntryIds')

        if m.get('TransitRouterRouteEntryNames') is not None:
            self.transit_router_route_entry_names = m.get('TransitRouterRouteEntryNames')

        if m.get('TransitRouterRouteEntryNextHopId') is not None:
            self.transit_router_route_entry_next_hop_id = m.get('TransitRouterRouteEntryNextHopId')

        if m.get('TransitRouterRouteEntryNextHopResourceId') is not None:
            self.transit_router_route_entry_next_hop_resource_id = m.get('TransitRouterRouteEntryNextHopResourceId')

        if m.get('TransitRouterRouteEntryNextHopResourceType') is not None:
            self.transit_router_route_entry_next_hop_resource_type = m.get('TransitRouterRouteEntryNextHopResourceType')

        if m.get('TransitRouterRouteEntryNextHopType') is not None:
            self.transit_router_route_entry_next_hop_type = m.get('TransitRouterRouteEntryNextHopType')

        if m.get('TransitRouterRouteEntryOriginResourceId') is not None:
            self.transit_router_route_entry_origin_resource_id = m.get('TransitRouterRouteEntryOriginResourceId')

        if m.get('TransitRouterRouteEntryOriginResourceType') is not None:
            self.transit_router_route_entry_origin_resource_type = m.get('TransitRouterRouteEntryOriginResourceType')

        if m.get('TransitRouterRouteEntryStatus') is not None:
            self.transit_router_route_entry_status = m.get('TransitRouterRouteEntryStatus')

        if m.get('TransitRouterRouteEntryType') is not None:
            self.transit_router_route_entry_type = m.get('TransitRouterRouteEntryType')

        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')

        return self

class ListTransitRouterRouteEntriesRequestRouteFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: List[str] = None,
    ):
        # The filter condition. Valid values:
        # 
        # - **PrefixExactMatchCidrs**: exact match.
        # - **LongestPrefixMatchCidrs**: longest prefix match. IP addresses and CIDR blocks are supported.
        # - **SubnetOfMatchCidrs**: subnet match. Matches subnets of the specified CIDR block, including the specified CIDR block itself.
        # - **SupernetOfMatchCidrs**: supernet match. Matches supernets of the specified CIDR block, including the specified CIDR block itself.
        # 
        # Multiple filter conditions have an **AND** relationship by default, which means that a route entry must meet all filter conditions to be considered a match. You cannot specify the same filter condition more than once.
        self.key = key
        # The list of filter condition values.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

