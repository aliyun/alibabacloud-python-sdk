# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListTransitRouterRouteTablesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_table_options: main_models.ListTransitRouterRouteTablesRequestRouteTableOptions = None,
        tag: List[main_models.ListTransitRouterRouteTablesRequestTag] = None,
        transit_router_id: str = None,
        transit_router_route_table_ids: List[str] = None,
        transit_router_route_table_names: List[str] = None,
        transit_router_route_table_status: str = None,
        transit_router_route_table_type: str = None,
    ):
        # The number of entries per page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The token that determines the start point of the query. Valid values:
        # 
        # *   If this is your first query or no subsequent query is to be sent, ignore this parameter.
        # *   If a subsequent query is to be sent, set the value to the value of **NextToken** that is returned from the last call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The features of the route table.
        self.route_table_options = route_table_options
        # The information about the tags.
        # 
        # You can specify at most 20 tags in each call.
        self.tag = tag
        # The ID of the Enterprise Edition transit router.
        self.transit_router_id = transit_router_id
        # The ID of the route table.
        # 
        # You can query multiple route tables in each call. Maximum value of **N**: **20**.
        self.transit_router_route_table_ids = transit_router_route_table_ids
        # The name of the route table.
        # 
        # You can query multiple route tables in each call. Maximum value of **N**: **20**.
        # 
        # > If you set both **TransitRouterRouteTableNames.N** and **TransitRouterRouteTableIds.N**, make sure that the specified name and ID belong to the same route table.
        self.transit_router_route_table_names = transit_router_route_table_names
        # The status of the route table. Valid values:
        # 
        # *   **Creating**: The route table is being created.
        # *   **Deleting**: The route table is being deleted.
        # *   **Active**: The route table is available.
        self.transit_router_route_table_status = transit_router_route_table_status
        # The type of the route table. Valid values:
        # 
        # *   **Custom**: a custom route table
        # *   **System**: the default route table
        self.transit_router_route_table_type = transit_router_route_table_type

    def validate(self):
        if self.route_table_options:
            self.route_table_options.validate()
        if self.tag:
            for v1 in self.tag:
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

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.route_table_options is not None:
            result['RouteTableOptions'] = self.route_table_options.to_map()

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.transit_router_route_table_ids is not None:
            result['TransitRouterRouteTableIds'] = self.transit_router_route_table_ids

        if self.transit_router_route_table_names is not None:
            result['TransitRouterRouteTableNames'] = self.transit_router_route_table_names

        if self.transit_router_route_table_status is not None:
            result['TransitRouterRouteTableStatus'] = self.transit_router_route_table_status

        if self.transit_router_route_table_type is not None:
            result['TransitRouterRouteTableType'] = self.transit_router_route_table_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RouteTableOptions') is not None:
            temp_model = main_models.ListTransitRouterRouteTablesRequestRouteTableOptions()
            self.route_table_options = temp_model.from_map(m.get('RouteTableOptions'))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListTransitRouterRouteTablesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('TransitRouterRouteTableIds') is not None:
            self.transit_router_route_table_ids = m.get('TransitRouterRouteTableIds')

        if m.get('TransitRouterRouteTableNames') is not None:
            self.transit_router_route_table_names = m.get('TransitRouterRouteTableNames')

        if m.get('TransitRouterRouteTableStatus') is not None:
            self.transit_router_route_table_status = m.get('TransitRouterRouteTableStatus')

        if m.get('TransitRouterRouteTableType') is not None:
            self.transit_router_route_table_type = m.get('TransitRouterRouteTableType')

        return self

class ListTransitRouterRouteTablesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # The tag key cannot be an empty string. The tag key can be up to 64 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # You can specify at most 20 tag keys.
        self.key = key
        # The tag value.
        # 
        # The tag value can be 0 to 128 characters in length, and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # Each tag key must have a unique tag value. You can specify at most 20 tag values in each call.
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

class ListTransitRouterRouteTablesRequestRouteTableOptions(DaraModel):
    def __init__(
        self,
        multi_region_ecmp: str = None,
    ):
        # Specifies whether to enable equal-cost multi-path (ECMP) routing. Valid values:
        # 
        # *   **disable**: disables ECMP routing If you disable ECMP routing, routes that are learned from different regions but have the same prefix and attributes select the transit router with the smallest region ID as the next hop. Region IDs are sorted in alphabetic order. The network latency and bandwidth consumption also vary based on the region. Proceed with caution.
        # *   **enable**: enables ECMP routing. If you enable ECMP routing, routes that are learned from different regions but have the same prefix and attributes form an ECMP route. The network latency and bandwidth consumption also vary based on the region. Proceed with caution.
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

