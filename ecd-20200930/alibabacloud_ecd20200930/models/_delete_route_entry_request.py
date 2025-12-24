# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRouteEntryRequest(DaraModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        next_hop_id: str = None,
        region_id: str = None,
        route_entry_id: str = None,
        route_table_id: str = None,
    ):
        self.destination_cidr_block = destination_cidr_block
        self.next_hop_id = next_hop_id
        # This parameter is required.
        self.region_id = region_id
        self.route_entry_id = route_entry_id
        # This parameter is required.
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.route_entry_id is not None:
            result['RouteEntryId'] = self.route_entry_id

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RouteEntryId') is not None:
            self.route_entry_id = m.get('RouteEntryId')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

