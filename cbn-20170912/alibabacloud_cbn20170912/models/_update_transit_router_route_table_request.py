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
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Default values:
        # 
        # *   **false** (default): performs a dry run and sends the request.
        # *   **true**: performs a dry run. The system checks the required parameters and the request syntax. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The features of the route table.
        self.route_table_options = route_table_options
        # The description of the route table.
        # 
        # The description must be 1 to 256 characters in length, and cannot start with http:// or https://. You can also leave this parameter empty.
        self.transit_router_route_table_description = transit_router_route_table_description
        # The ID of the route table of the Enterprise Edition transit router.
        # 
        # This parameter is required.
        self.transit_router_route_table_id = transit_router_route_table_id
        # The name of the route table.
        # 
        # The name must be 1 to 128 characters in length, and cannot start with http:// or https://. You can also leave this parameter empty.
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
        # Indicates whether multi-region ECMP routing is enabled. Valid values:
        # 
        # - **disable**: If multi-region ECMP routing is disabled, routes that are learned from different regions but have the same prefix and attributes select the transit router with the smallest region ID as the next hop. Region IDs are sorted in alphabetic order. The network latency and bandwidth consumption also vary based on the region. Proceed with caution.
        # - **enable**: If multi-region ECMP routing is enabled, routes that are learned from different regions but have the same prefix and attributes form an ECMP route. The network latency and bandwidth consumption also vary based on the region. Proceed with caution.
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

