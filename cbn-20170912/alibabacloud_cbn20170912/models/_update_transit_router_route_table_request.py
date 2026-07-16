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
        # Generate a parameter value from your client to make sure that the value is unique among different requests. The ClientToken can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. The dry run checks permissions and the status of the instance. Valid values:
        # 
        # - **false** (default): Sends a normal request. After the request passes the check, the name and description of the route table are modified.
        # 
        # - **true**: Sends a check request. The system checks the required parameters and the request format. If the check fails, the corresponding error is returned. If the check succeeds, the error code `DryRunOperation` is returned.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The features of the route table.
        self.route_table_options = route_table_options
        # The description of the route table.
        # 
        # The description can be empty or 1 to 256 characters in length. It cannot start with http\\:// or https\\://.
        self.transit_router_route_table_description = transit_router_route_table_description
        # The ID of the route table for the Enterprise Edition transit router.
        # 
        # This parameter is required.
        self.transit_router_route_table_id = transit_router_route_table_id
        # The name of the route table.
        # 
        # The name can be empty or 1 to 128 characters in length. It cannot start with http\\:// or https\\://.
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
        # The multi-region ECMP routing feature. Valid values:
        # 
        # - **disable**: Disables multi-region ECMP routing. After you disable this feature, if routes with the same prefix are learned from different regions and have the same attributes, the route that is learned from the region with the alphabetically smallest ID is used as the next hop. This may change traffic latency and inter-region bandwidth consumption. Evaluate the impact before you disable this feature.
        # 
        # - **enable**: Enables multi-region ECMP routing. After you enable this feature, if routes with the same prefix are learned from different regions and have the same attributes, ECMP routes are formed. This may change traffic latency and inter-region bandwidth consumption. Evaluate the impact before you enable this feature.
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

