# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEnsRouteEntryListRequest(DaraModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        page_number: int = None,
        page_size: int = None,
        route_entry_id: str = None,
        route_entry_name: str = None,
        route_entry_type: str = None,
        route_table_id: str = None,
    ):
        # The destination Classless Inter-Domain Routing (CIDR) block of the route entry.
        self.destination_cidr_block = destination_cidr_block
        # The ID of the next hop.
        self.next_hop_id = next_hop_id
        # The type of next hop of the custom route entry. Valid values:
        # 
        # *   Instance (default): an ENS instance.
        # *   HaVip: a high-availability virtual IP address (HAVIP).
        # *   NetworkPeer: VPC peering connection.
        self.next_hop_type = next_hop_type
        # The page number of the returned page. Valid values: integers that are greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Valid values: 10 to 100.
        self.page_size = page_size
        # The ID of the route that you want to query.
        self.route_entry_id = route_entry_id
        # The name of the route.
        self.route_entry_name = route_entry_name
        # The route type. Valid values:
        # 
        # *   Custom: custom route
        # *   System: system route
        self.route_entry_type = route_entry_type
        # The ID of the route table that you want to query.
        self.route_table_id = route_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.route_entry_id is not None:
            result['RouteEntryId'] = self.route_entry_id

        if self.route_entry_name is not None:
            result['RouteEntryName'] = self.route_entry_name

        if self.route_entry_type is not None:
            result['RouteEntryType'] = self.route_entry_type

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RouteEntryId') is not None:
            self.route_entry_id = m.get('RouteEntryId')

        if m.get('RouteEntryName') is not None:
            self.route_entry_name = m.get('RouteEntryName')

        if m.get('RouteEntryType') is not None:
            self.route_entry_type = m.get('RouteEntryType')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

