# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeEnsRouteTablesRequest(DaraModel):
    def __init__(
        self,
        associate_type: str = None,
        ens_region_id: str = None,
        ens_region_ids: List[str] = None,
        network_id: str = None,
        page_number: int = None,
        page_size: int = None,
        route_table_id: str = None,
        route_table_name: str = None,
        type: str = None,
    ):
        # The type of the resource with which the route table is associated. Valid values:
        # 
        # *   **VSwitch**
        # *   **Gateway**
        self.associate_type = associate_type
        # The ID of the ENS node.
        self.ens_region_id = ens_region_id
        # The IDs of edge nodes. You can specify 1 to 100 IDs.
        self.ens_region_ids = ens_region_ids
        # The ID of the network.
        self.network_id = network_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the route table.
        self.route_table_id = route_table_id
        # The name of the route table.
        self.route_table_name = route_table_name
        # The SNAT type.
        # 
        # *   FullCone: full cone NAT.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associate_type is not None:
            result['AssociateType'] = self.associate_type

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.ens_region_ids is not None:
            result['EnsRegionIds'] = self.ens_region_ids

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        if self.route_table_name is not None:
            result['RouteTableName'] = self.route_table_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociateType') is not None:
            self.associate_type = m.get('AssociateType')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('EnsRegionIds') is not None:
            self.ens_region_ids = m.get('EnsRegionIds')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        if m.get('RouteTableName') is not None:
            self.route_table_name = m.get('RouteTableName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

