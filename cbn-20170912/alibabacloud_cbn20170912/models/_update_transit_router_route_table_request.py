# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class UpdateTransitRouterRouteTableRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_table_options: main_models.UpdateTransitRouterRouteTableRequestRouteTableOptions = None,
        transit_router_route_table_description: str = None,
        transit_router_route_table_id: str = None,
        transit_router_route_table_name: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The ClientToken value can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is different.
        self.client_token = client_token
        # Specifies whether to perform a dry run, including permission and instance status verification. Valid values:
        # 
        # - **false** (default): Sends a normal request. If the request passes the check, the name and description of the route table are modified.
        # - **true**: Sends a check request. Only the validation is performed, and the name and description of the route table are not modified. The check items include whether required parameters are specified and the request format. If the check fails, the corresponding error is returned. If the check passes, the error code `DryRunOperation` is returned.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The route table feature options.
        self.route_table_options = route_table_options
        # The description of the route table.
        # 
        # The description can be empty or 1 to 256 characters in length and cannot start with http:// or https://.
        self.transit_router_route_table_description = transit_router_route_table_description
        # The ID of the Enterprise Edition transit router route table.
        # 
        # This parameter is required.
        self.transit_router_route_table_id = transit_router_route_table_id
        # The name of the route table.
        # 
        # The name can be empty or 1 to 128 characters in length and cannot start with http:// or https://.
        self.transit_router_route_table_name = transit_router_route_table_name

    def validate(self):
        if self.route_table_options:
            self.route_table_options.validate()

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

        if self.route_table_options is not None:
            result['RouteTableOptions'] = self.route_table_options.to_map()

        if self.transit_router_route_table_description is not None:
            result['TransitRouterRouteTableDescription'] = self.transit_router_route_table_description

        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id

        if self.transit_router_route_table_name is not None:
            result['TransitRouterRouteTableName'] = self.transit_router_route_table_name

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

        if m.get('RouteTableOptions') is not None:
            temp_model = main_models.UpdateTransitRouterRouteTableRequestRouteTableOptions()
            self.route_table_options = temp_model.from_map(m.get('RouteTableOptions'))

        if m.get('TransitRouterRouteTableDescription') is not None:
            self.transit_router_route_table_description = m.get('TransitRouterRouteTableDescription')

        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')

        if m.get('TransitRouterRouteTableName') is not None:
            self.transit_router_route_table_name = m.get('TransitRouterRouteTableName')

        return self

class UpdateTransitRouterRouteTableRequestRouteTableOptions(DaraModel):
    def __init__(
        self,
        multi_region_ecmp: str = None,
    ):
        # Multi-region equal-cost multi-path (ECMP) routing. Valid values:
        # - **disable**: Disables multi-region ECMP routing. After multi-region ECMP routing is disabled, routes with the same prefix learned from different regions will prefer the transit router (TR) with the smallest Region ID (sorted alphabetically) as the next hop when other route attributes are the same. In this case, the traffic latency and bandwidth consumed between different regions may change. Make sure that you have fully evaluated the impact before disabling this feature.
        # - **enable**: Enables multi-region ECMP routing. After multi-region ECMP routing is enabled, routes with the same prefix learned from different regions will form equal-cost routes when other route attributes are the same. In this case, the traffic latency and bandwidth consumed between different regions may change. Make sure that you have fully evaluated the impact before enabling this feature.
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

