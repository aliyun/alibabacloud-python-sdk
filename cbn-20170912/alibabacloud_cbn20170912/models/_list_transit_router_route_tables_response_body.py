# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListTransitRouterRouteTablesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        transit_router_route_tables: List[main_models.ListTransitRouterRouteTablesResponseBodyTransitRouterRouteTables] = None,
    ):
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that determines the start point of the next query. Valid values:
        # 
        # *   If **NextToken** was returned in the previous query, specify the value to obtain the next set of results.
        # *   If a value of **NextToken** is not returned, it indicates that no additional results exist.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # A list of route tables.
        self.transit_router_route_tables = transit_router_route_tables

    def validate(self):
        if self.transit_router_route_tables:
            for v1 in self.transit_router_route_tables:
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['TransitRouterRouteTables'] = []
        if self.transit_router_route_tables is not None:
            for k1 in self.transit_router_route_tables:
                result['TransitRouterRouteTables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.transit_router_route_tables = []
        if m.get('TransitRouterRouteTables') is not None:
            for k1 in m.get('TransitRouterRouteTables'):
                temp_model = main_models.ListTransitRouterRouteTablesResponseBodyTransitRouterRouteTables()
                self.transit_router_route_tables.append(temp_model.from_map(k1))

        return self

class ListTransitRouterRouteTablesResponseBodyTransitRouterRouteTables(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        region_id: str = None,
        route_table_options: main_models.ListTransitRouterRouteTablesResponseBodyTransitRouterRouteTablesRouteTableOptions = None,
        tags: List[main_models.ListTransitRouterRouteTablesResponseBodyTransitRouterRouteTablesTags] = None,
        transit_router_id: str = None,
        transit_router_route_table_description: str = None,
        transit_router_route_table_id: str = None,
        transit_router_route_table_name: str = None,
        transit_router_route_table_status: str = None,
        transit_router_route_table_type: str = None,
    ):
        # The time when the route table was created.
        # 
        # The time follows the ISO8601 standard in the YYYY-MM-DDThh:mmZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The region ID of the Enterprise Edition transit router.
        self.region_id = region_id
        # The features of the route table.
        self.route_table_options = route_table_options
        # The tags.
        self.tags = tags
        # The transit router ID.
        self.transit_router_id = transit_router_id
        # The description of the route table.
        self.transit_router_route_table_description = transit_router_route_table_description
        # The ID of the route table.
        self.transit_router_route_table_id = transit_router_route_table_id
        # The name of the route table.
        self.transit_router_route_table_name = transit_router_route_table_name
        # The status of the route table. Valid values:
        # 
        # *   **Creating**
        # *   **Deleting**
        # *   **Active**
        self.transit_router_route_table_status = transit_router_route_table_status
        # The type of the route table. Valid values:
        # 
        # *   **Custom**
        # *   **System**
        self.transit_router_route_table_type = transit_router_route_table_type

    def validate(self):
        if self.route_table_options:
            self.route_table_options.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.route_table_options is not None:
            result['RouteTableOptions'] = self.route_table_options.to_map()

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.transit_router_route_table_description is not None:
            result['TransitRouterRouteTableDescription'] = self.transit_router_route_table_description

        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id

        if self.transit_router_route_table_name is not None:
            result['TransitRouterRouteTableName'] = self.transit_router_route_table_name

        if self.transit_router_route_table_status is not None:
            result['TransitRouterRouteTableStatus'] = self.transit_router_route_table_status

        if self.transit_router_route_table_type is not None:
            result['TransitRouterRouteTableType'] = self.transit_router_route_table_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RouteTableOptions') is not None:
            temp_model = main_models.ListTransitRouterRouteTablesResponseBodyTransitRouterRouteTablesRouteTableOptions()
            self.route_table_options = temp_model.from_map(m.get('RouteTableOptions'))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListTransitRouterRouteTablesResponseBodyTransitRouterRouteTablesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('TransitRouterRouteTableDescription') is not None:
            self.transit_router_route_table_description = m.get('TransitRouterRouteTableDescription')

        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')

        if m.get('TransitRouterRouteTableName') is not None:
            self.transit_router_route_table_name = m.get('TransitRouterRouteTableName')

        if m.get('TransitRouterRouteTableStatus') is not None:
            self.transit_router_route_table_status = m.get('TransitRouterRouteTableStatus')

        if m.get('TransitRouterRouteTableType') is not None:
            self.transit_router_route_table_type = m.get('TransitRouterRouteTableType')

        return self

class ListTransitRouterRouteTablesResponseBodyTransitRouterRouteTablesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class ListTransitRouterRouteTablesResponseBodyTransitRouterRouteTablesRouteTableOptions(DaraModel):
    def __init__(
        self,
        multi_region_ecmp: str = None,
    ):
        # Indicates whether ECMP routing is enabled. Valid values:
        # 
        # *   **disable** If ECMP routing is disabled, routes that are learned from different regions but have the same prefix and attributes select the transit router with the smallest region ID as the next hop. Region IDs are sorted in alphabetic order. The network latency and bandwidth consumption also vary based on the region. Proceed with caution.
        # *   **enable** If ECMP routing is enabled, routes that are learned from different regions but have the same prefix and attributes form an ECMP route. The network latency and bandwidth consumption also vary based on the region. Proceed with caution.
        self.multi_region_ecmp = multi_region_ecmp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.multi_region_ecmp is not None:
            result['MultiRegionECMP'] = self.multi_region_ecmp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MultiRegionECMP') is not None:
            self.multi_region_ecmp = m.get('MultiRegionECMP')

        return self

