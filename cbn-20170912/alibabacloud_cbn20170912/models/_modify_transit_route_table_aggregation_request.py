# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyTransitRouteTableAggregationRequest(DaraModel):
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
        # Use the client to generate the token, but make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **RequestId** as the **ClientToken**. The **RequestId** may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run to check information such as the permissions and instance status. Valid values:
        # 
        # *   **false** (default): sends the request. If the request passes the check, an Enterprise Edition transit router is created.
        # *   **true**: checks the request but does not create the Enterprise Edition transit router. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The destination CIDR block of the aggregate route.
        # 
        # This parameter is required.
        self.transit_route_table_aggregation_cidr = transit_route_table_aggregation_cidr
        # The description of the aggregate route.
        # 
        # The description can be empty or 0 to 256 characters in length and cannot start with http:// or https://.
        self.transit_route_table_aggregation_description = transit_route_table_aggregation_description
        # The name of the aggregate route.
        # 
        # The name can be empty or 1 to 128 characters in length, and cannot start with http:// or https://.
        self.transit_route_table_aggregation_name = transit_route_table_aggregation_name
        # The scope of networks that you want to advertise the aggregate route.
        # 
        # The valid value is **VPC**, which indicates that the aggregate route is advertised to all VPCs that have associated forwarding correlation with the Enterprise Edition transit router and have route synchronization enabled.
        self.transit_route_table_aggregation_scope = transit_route_table_aggregation_scope
        # The scope of networks to which the aggregate route is advertised.
        # 
        # >  You must select at least one attribute from either the Aggregate Route Propagation Range or the Aggregate Route Propagation Range List. We recommend using the latter. The elements of the two attributes cannot duplicate.
        self.transit_route_table_aggregation_scope_list = transit_route_table_aggregation_scope_list
        # The list of route table IDs of the Enterprise Edition transit router.
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

