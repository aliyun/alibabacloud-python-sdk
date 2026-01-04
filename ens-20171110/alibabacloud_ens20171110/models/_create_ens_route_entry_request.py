# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEnsRouteEntryRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        destination_cidr_block: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        route_entry_name: str = None,
        route_table_id: str = None,
        source_cidr_block: str = None,
    ):
        # The description of the custom route entry.
        self.description = description
        # The destination CIDR block of the custom route entry. Make sure that the following requirements are met:
        # 
        # *   The destination CIDR block cannot point or belong to 100.64.0.0/10.
        # *   The destination CIDR blocks of the custom route entries in the same route table cannot overlap.
        # *   0.0.0.0/0 indicates the default CIDR block.
        # 
        # This parameter is required.
        self.destination_cidr_block = destination_cidr_block
        # The ID of the next hop of the custom route entry.
        # 
        # This parameter is required.
        self.next_hop_id = next_hop_id
        # The next hop type of the custom route. Valid values:
        # 
        # *   Instance: an ENS instance.
        # *   HaVip: a high-availability virtual IP address (HAVIP).
        # *   NetworkPeer: VPC peering connection.
        self.next_hop_type = next_hop_type
        # The name of the custom route entry that you want to add. The name must be 1 to 128 characters in length. It cannot start with http:// or https://.
        self.route_entry_name = route_entry_name
        # The ID of the route table to which you want to add a custom route entry.
        # 
        # This parameter is required.
        self.route_table_id = route_table_id
        # The source CIDR block is available when you configure a route entry in the gateway route table, but is not unavailable when you configure a route entry in the vSwitch route table.
        self.source_cidr_block = source_cidr_block

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        if self.route_entry_name is not None:
            result['RouteEntryName'] = self.route_entry_name

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        if self.source_cidr_block is not None:
            result['SourceCidrBlock'] = self.source_cidr_block

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        if m.get('RouteEntryName') is not None:
            self.route_entry_name = m.get('RouteEntryName')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        if m.get('SourceCidrBlock') is not None:
            self.source_cidr_block = m.get('SourceCidrBlock')

        return self

