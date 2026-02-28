# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListVpdRouteEntriesRequest(DaraModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        enable_page: bool = None,
        ignore_detailed_route_entry: bool = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        route_type: str = None,
        status: str = None,
        vpd_id: str = None,
        vpd_route_entry_id: str = None,
    ):
        # Destination CIDR block
        self.destination_cidr_block = destination_cidr_block
        # Specifies whether to enable paged query. Optional values:
        # 
        # *   **true**: Enable pagination query
        # *   **false**: Pagination query is disabled
        self.enable_page = enable_page
        # Filter 32 detailed CIDR blocks. Default value: true
        self.ignore_detailed_route_entry = ignore_detailed_route_entry
        # Next Hop Instance
        self.next_hop_id = next_hop_id
        # Next Hop Instance Type
        self.next_hop_type = next_hop_type
        # The page number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # Route type
        self.route_type = route_type
        # The status of the enterprise-level snapshot policy.
        self.status = status
        # Lingjun CIDR block instance ID
        # 
        # This parameter is required.
        self.vpd_id = vpd_id
        # Lingjun CIDR block route entry instance ID
        self.vpd_route_entry_id = vpd_route_entry_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page

        if self.ignore_detailed_route_entry is not None:
            result['IgnoreDetailedRouteEntry'] = self.ignore_detailed_route_entry

        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.route_type is not None:
            result['RouteType'] = self.route_type

        if self.status is not None:
            result['Status'] = self.status

        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id

        if self.vpd_route_entry_id is not None:
            result['VpdRouteEntryId'] = self.vpd_route_entry_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')

        if m.get('IgnoreDetailedRouteEntry') is not None:
            self.ignore_detailed_route_entry = m.get('IgnoreDetailedRouteEntry')

        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        if m.get('VpdRouteEntryId') is not None:
            self.vpd_route_entry_id = m.get('VpdRouteEntryId')

        return self

