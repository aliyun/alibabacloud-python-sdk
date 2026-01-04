# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeEnsRouteTablesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        route_tables: List[main_models.DescribeEnsRouteTablesResponseBodyRouteTables] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The information about the route tables.
        self.route_tables = route_tables
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.route_tables:
            for v1 in self.route_tables:
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RouteTables'] = []
        if self.route_tables is not None:
            for k1 in self.route_tables:
                result['RouteTables'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.route_tables = []
        if m.get('RouteTables') is not None:
            for k1 in m.get('RouteTables'):
                temp_model = main_models.DescribeEnsRouteTablesResponseBodyRouteTables()
                self.route_tables.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeEnsRouteTablesResponseBodyRouteTables(DaraModel):
    def __init__(
        self,
        associate_type: str = None,
        creation_time: str = None,
        description: str = None,
        ens_region_id: str = None,
        is_default_gateway_route_table: bool = None,
        network_id: str = None,
        route_table_id: str = None,
        route_table_name: str = None,
        status: str = None,
        type: str = None,
        v_switch_ids: List[str] = None,
    ):
        # The type of the resource with which the route table is associated. Valid values:
        # 
        # *   **VSwitch**
        # *   **Gateway**
        self.associate_type = associate_type
        # The time when the route table was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description.
        self.description = description
        # The ID of the edge node.
        self.ens_region_id = ens_region_id
        # Specifies whether it is the default gateway route table.
        self.is_default_gateway_route_table = is_default_gateway_route_table
        # The ID of the network.
        self.network_id = network_id
        # The ID of the route table.
        self.route_table_id = route_table_id
        # The name of the route table that you want to query.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        self.route_table_name = route_table_name
        # The status. Valid values:
        # 
        # *   Available: The route table is available.
        self.status = status
        # The type of the route table. Examples:
        # 
        # *   Custom: custom route table.
        # *   System: system route table.
        self.type = type
        # The vSwitches that are associated with the route table.
        self.v_switch_ids = v_switch_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associate_type is not None:
            result['AssociateType'] = self.associate_type

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.is_default_gateway_route_table is not None:
            result['IsDefaultGatewayRouteTable'] = self.is_default_gateway_route_table

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        if self.route_table_name is not None:
            result['RouteTableName'] = self.route_table_name

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociateType') is not None:
            self.associate_type = m.get('AssociateType')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('IsDefaultGatewayRouteTable') is not None:
            self.is_default_gateway_route_table = m.get('IsDefaultGatewayRouteTable')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        if m.get('RouteTableName') is not None:
            self.route_table_name = m.get('RouteTableName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        return self

