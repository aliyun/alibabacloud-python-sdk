# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTransitRouteTableAggregationShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        transit_route_table_aggregation_cidr: str = None,
        transit_route_table_aggregation_description: str = None,
        transit_route_table_aggregation_name: str = None,
        transit_route_table_aggregation_scope: str = None,
        transit_route_table_aggregation_scope_list_shrink: str = None,
        transit_route_table_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # Generate a value from your client to make sure that the value is unique among different requests. The ClientToken can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may be different for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run for the request. A dry run checks permissions and instance status. Valid values:
        # 
        # - **false** (default): sends a normal request. If the request passes the check, an aggregate route is created.
        # 
        # - **true**: sends a check request to verify the required parameters and the request format. The aggregate route is not created. If the request fails the check, an error is returned. If the request passes the check, the `DryRunOperation` error code is returned.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The destination CIDR block of the aggregate route.
        # 
        # > The following CIDR blocks are not supported:
        # 
        # - CIDR blocks that start with 0 or 100.64
        # 
        # - Multicast addresses (224.0.0.1 to 239.255.255.254)
        # 
        # This parameter is required.
        self.transit_route_table_aggregation_cidr = transit_route_table_aggregation_cidr
        # The description of the aggregate route.
        # 
        # The description can be empty or 1 to 256 characters in length. It cannot start with http\\:// or https\\://.
        self.transit_route_table_aggregation_description = transit_route_table_aggregation_description
        # The name of the aggregate route.
        # 
        # The name can be empty or 1 to 128 characters in length. It cannot start with http\\:// or https\\://.
        self.transit_route_table_aggregation_name = transit_route_table_aggregation_name
        # The propagation scope of the aggregate route.
        # 
        # The only valid value is **VPC**. This value indicates that the aggregate route is propagated to all VPC instances that are associated with the route table of the Enterprise Edition transit router and have route synchronization enabled.
        self.transit_route_table_aggregation_scope = transit_route_table_aggregation_scope
        # The list of propagation scopes for the aggregate route.
        # 
        # > You must specify either this parameter or TransitRouteTableAggregationScope. We recommend that you use this parameter. The elements in this list cannot be the same as the value of TransitRouteTableAggregationScope.
        self.transit_route_table_aggregation_scope_list_shrink = transit_route_table_aggregation_scope_list_shrink
        # The ID of the route table of the Enterprise Edition transit router.
        # 
        # This parameter is required.
        self.transit_route_table_id = transit_route_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.transit_route_table_aggregation_cidr is not None:
            result['TransitRouteTableAggregationCidr'] = self.transit_route_table_aggregation_cidr

        if self.transit_route_table_aggregation_description is not None:
            result['TransitRouteTableAggregationDescription'] = self.transit_route_table_aggregation_description

        if self.transit_route_table_aggregation_name is not None:
            result['TransitRouteTableAggregationName'] = self.transit_route_table_aggregation_name

        if self.transit_route_table_aggregation_scope is not None:
            result['TransitRouteTableAggregationScope'] = self.transit_route_table_aggregation_scope

        if self.transit_route_table_aggregation_scope_list_shrink is not None:
            result['TransitRouteTableAggregationScopeList'] = self.transit_route_table_aggregation_scope_list_shrink

        if self.transit_route_table_id is not None:
            result['TransitRouteTableId'] = self.transit_route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TransitRouteTableAggregationCidr') is not None:
            self.transit_route_table_aggregation_cidr = m.get('TransitRouteTableAggregationCidr')

        if m.get('TransitRouteTableAggregationDescription') is not None:
            self.transit_route_table_aggregation_description = m.get('TransitRouteTableAggregationDescription')

        if m.get('TransitRouteTableAggregationName') is not None:
            self.transit_route_table_aggregation_name = m.get('TransitRouteTableAggregationName')

        if m.get('TransitRouteTableAggregationScope') is not None:
            self.transit_route_table_aggregation_scope = m.get('TransitRouteTableAggregationScope')

        if m.get('TransitRouteTableAggregationScopeList') is not None:
            self.transit_route_table_aggregation_scope_list_shrink = m.get('TransitRouteTableAggregationScopeList')

        if m.get('TransitRouteTableId') is not None:
            self.transit_route_table_id = m.get('TransitRouteTableId')

        return self

