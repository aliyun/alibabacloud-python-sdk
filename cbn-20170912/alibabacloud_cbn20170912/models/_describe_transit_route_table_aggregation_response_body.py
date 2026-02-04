# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeTransitRouteTableAggregationResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        data: List[main_models.DescribeTransitRouteTableAggregationResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
        total: int = None,
    ):
        # The number of entries returned per page.
        self.count = count
        # A list of aggregate routes.
        self.data = data
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value is returned for **NextToken**, the value is the token that determines the start point of the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeTransitRouteTableAggregationResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeTransitRouteTableAggregationResponseBodyData(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        route_type: str = None,
        scope: str = None,
        scope_list: List[str] = None,
        status: str = None,
        tr_route_table_id: str = None,
        transit_route_table_aggregation_cidr: str = None,
    ):
        # The description of the aggregate route.
        self.description = description
        # The name of the aggregate route.
        self.name = name
        # The type of the aggregate route.
        # 
        # The valid value is **Static**, which indicates a static route. By default, aggregate routes advertised to a VPC are considered custom routes.
        self.route_type = route_type
        # The scope of networks that you want to advertise the aggregate route.
        # 
        # The valid value is **VPC**, which indicates that the aggregate route is advertised to all virtual private clouds (VPCs) that are in associated forwarding correlation with the Enterprise Edition transit router and have route synchronization enabled.
        self.scope = scope
        # The list of propagation ranges of the aggregation route.
        # 
        # >  You must specify at least one of the following attributes: Aggregation Scope and Aggregate Scope List. We recommend that you specify the latter. The elements in the two attributes cannot be duplicate.
        self.scope_list = scope_list
        # The status of the advertisement of the aggregate route. Valid values:
        # 
        # *   **AllConfigured**: The aggregate route is advertised to all VPCs.
        # *   **Configuring**: The aggregate route is being advertised.
        # *   **ConfigFailed**: The aggregate route failed to be advertised.
        # *   **PartialConfigured**: Failed to advertise the aggregate route to some VPCs.
        # *   **Deleting**: The aggregate route is being deleted.
        self.status = status
        # The ID of the route table of the Enterprise Edition transit router.
        self.tr_route_table_id = tr_route_table_id
        # The destination CIDR block of the aggregate route.
        self.transit_route_table_aggregation_cidr = transit_route_table_aggregation_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.route_type is not None:
            result['RouteType'] = self.route_type

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.scope_list is not None:
            result['ScopeList'] = self.scope_list

        if self.status is not None:
            result['Status'] = self.status

        if self.tr_route_table_id is not None:
            result['TrRouteTableId'] = self.tr_route_table_id

        if self.transit_route_table_aggregation_cidr is not None:
            result['TransitRouteTableAggregationCidr'] = self.transit_route_table_aggregation_cidr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('ScopeList') is not None:
            self.scope_list = m.get('ScopeList')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TrRouteTableId') is not None:
            self.tr_route_table_id = m.get('TrRouteTableId')

        if m.get('TransitRouteTableAggregationCidr') is not None:
            self.transit_route_table_aggregation_cidr = m.get('TransitRouteTableAggregationCidr')

        return self

