# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCenRouteMapsRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        cen_region_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_map_id: str = None,
        transit_router_route_table_id: str = None,
        transmit_direction: str = None,
    ):
        # The ID of the Cloud Enterprise Network (CEN) instance.
        # 
        # This parameter is required.
        self.cen_id = cen_id
        # The region ID of the routing policy.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query the most recent region list.
        self.cen_region_id = cen_region_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: **10**.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The routing policy ID.
        self.route_map_id = route_map_id
        # The route table ID of the transit router with which the routing policy is associated.
        self.transit_router_route_table_id = transit_router_route_table_id
        # The direction in which the routing policy is applied. Valid values:
        # 
        # *   **RegionIn**: Routes are advertised to the gateways in the regions that are connected by the CEN instance.
        # 
        # For example, routes are advertised from network instances deployed in the current region or other regions to the gateway deployed in the current region.
        # 
        # *   **RegionOut**: Routes are advertised from the gateways in the regions that are connected by the CEN instance.
        # 
        # For example, routes are advertised from the gateway deployed in the current region to network instances deployed in the current region, or to gateways deployed in other regions.
        self.transmit_direction = transmit_direction

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cen_region_id is not None:
            result['CenRegionId'] = self.cen_region_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id

        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id

        if self.transmit_direction is not None:
            result['TransmitDirection'] = self.transmit_direction

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CenRegionId') is not None:
            self.cen_region_id = m.get('CenRegionId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')

        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')

        if m.get('TransmitDirection') is not None:
            self.transmit_direction = m.get('TransmitDirection')

        return self

