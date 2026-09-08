# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateTransitRouteTableAggregationRequest(DaraModel):
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
        transit_route_table_aggregation_scope_list: List[str] = None,
        transit_route_table_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may be different for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. The dry run checks items such as permissions and instance status. Valid values:
        # 
        # - **false** (default): sends a normal request and directly creates the aggregate route after the request passes the check.
        # - **true**: sends a check request without creating the aggregate route. The check items include required parameters and request format. If the check fails, the corresponding error is returned. If the check succeeds, the error code `DryRunOperation` is returned.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The destination CIDR block of the aggregate route.
        # 
        # > The following CIDR blocks are not supported:
        # - CIDR blocks that start with "0" or "100.64"
        # - Multicast addresses (224.0.0.1 to 239.255.255.254)
        # 
        # This parameter is required.
        self.transit_route_table_aggregation_cidr = transit_route_table_aggregation_cidr
        # The description of the aggregate route.
        # 
        # The description can be empty or 1 to 256 characters in length and cannot start with http:// or https://.
        self.transit_route_table_aggregation_description = transit_route_table_aggregation_description
        # The name of the aggregate route.
        # 
        # The name can be empty or 1 to 128 characters in length and cannot start with http:// or https://.
        self.transit_route_table_aggregation_name = transit_route_table_aggregation_name
        # The propagation scope of the aggregate route.
        # 
        # Set the value to **VPC**, which indicates that the aggregate route is propagated to all VPC-connected instances that have established an associated forwarding relationship with the current Enterprise Edition transit router route table and have the route synchronization feature enabled.
        self.transit_route_table_aggregation_scope = transit_route_table_aggregation_scope
        # The propagation scope list of the aggregate route.
        # >You must specify at least one of the propagation scope and the propagation scope list. We recommend that you use the propagation scope list. The elements in the propagation scope list cannot duplicate the value of the propagation scope.
        self.transit_route_table_aggregation_scope_list = transit_route_table_aggregation_scope_list
        # The ID of the Enterprise Edition transit router route table.
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

        if self.transit_route_table_aggregation_scope_list is not None:
            result['TransitRouteTableAggregationScopeList'] = self.transit_route_table_aggregation_scope_list

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
            self.transit_route_table_aggregation_scope_list = m.get('TransitRouteTableAggregationScopeList')

        if m.get('TransitRouteTableId') is not None:
            self.transit_route_table_id = m.get('TransitRouteTableId')

        return self

