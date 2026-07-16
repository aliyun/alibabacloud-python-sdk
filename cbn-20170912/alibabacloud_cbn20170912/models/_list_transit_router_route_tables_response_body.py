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
        # The token that is used for the next query. Valid values:
        # 
        # - If **NextToken** is empty, it indicates that no next query is to be sent.
        # 
        # - If a value is returned for **NextToken**, the value is the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The list of route tables.
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
        # The time is displayed in the YYYY-MM-DDThh:mmZ format in UTC.
        self.create_time = create_time
        # The ID of the region where the Enterprise Edition transit router is deployed.
        self.region_id = region_id
        # The features of the route table.
        self.route_table_options = route_table_options
        # The list of tags.
        self.tags = tags
        # The ID of the transit router.
        self.transit_router_id = transit_router_id
        # The description of the route table.
        self.transit_router_route_table_description = transit_router_route_table_description
        # The route table ID.
        self.transit_router_route_table_id = transit_router_route_table_id
        # The name of the route table.
        self.transit_router_route_table_name = transit_router_route_table_name
        # The status of the route table.
        # 
        # - **Creating**: The route table is being created.
        # 
        # - **Deleting**: The route table is being deleted.
        # 
        # - **Active**: The route table is available.
        self.transit_router_route_table_status = transit_router_route_table_status
        # The type of the route table.
        # 
        # - **Custom**: a custom route table.
        # 
        # - **System**: the default route table.
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
        # The multi-region ECMP routing feature. Valid values:
        # 
        # - **disable**: Disables multi-region ECMP routing. After this feature is disabled, for routes that are learned from different regions and have the same prefix and other attributes, the system selects the transit router with the smallest region ID as the next hop. Region IDs are sorted in alphabetical order. This changes the latency and bandwidth consumption between different regions. Make sure that you fully evaluate the impact before you disable the feature.
        # 
        # - **enable**: Enables multi-region ECMP routing. After this feature is enabled, for routes that are learned from different regions and have the same prefix and other attributes, ECMP routing is formed. This changes the latency and bandwidth consumption between different regions. Make sure that you fully evaluate the impact before you enable the feature.
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

