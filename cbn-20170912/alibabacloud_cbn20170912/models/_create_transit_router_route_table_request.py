# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class CreateTransitRouterRouteTableRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_table_options: main_models.CreateTransitRouterRouteTableRequestRouteTableOptions = None,
        tag: List[main_models.CreateTransitRouterRouteTableRequestTag] = None,
        transit_router_id: str = None,
        transit_router_route_table_description: str = None,
        transit_router_route_table_name: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run, including permission and instance status verification. Valid values:
        # 
        # - **false** (default): sends a normal request and creates the custom route table after the request passes the verification.
        # - **true**: sends a check request without creating the custom route table. The system checks the required parameters, request format, and other conditions. If the check fails, the corresponding error is returned. If the check passes, the corresponding request ID is returned.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The route table options.
        self.route_table_options = route_table_options
        # The tag information.
        # 
        # You can specify up to 20 tags at a time.
        self.tag = tag
        # The ID of the Enterprise Edition transit router instance.
        # 
        # This parameter is required.
        self.transit_router_id = transit_router_id
        # The description of the custom route table.
        # 
        # The description can be empty or 1 to 256 characters in length and cannot start with http:// or https://.
        self.transit_router_route_table_description = transit_router_route_table_description
        # The name of the custom route table.
        # 
        # The name can be empty or 1 to 128 characters in length and cannot start with http:// or https://.
        self.transit_router_route_table_name = transit_router_route_table_name

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

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.transit_router_route_table_description is not None:
            result['TransitRouterRouteTableDescription'] = self.transit_router_route_table_description

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
            temp_model = main_models.CreateTransitRouterRouteTableRequestRouteTableOptions()
            self.route_table_options = temp_model.from_map(m.get('RouteTableOptions'))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateTransitRouterRouteTableRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('TransitRouterRouteTableDescription') is not None:
            self.transit_router_route_table_description = m.get('TransitRouterRouteTableDescription')

        if m.get('TransitRouterRouteTableName') is not None:
            self.transit_router_route_table_name = m.get('TransitRouterRouteTableName')

        return self

class CreateTransitRouterRouteTableRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource.
        # 
        # Once specified, the tag key cannot be an empty string. The tag key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # You can specify up to 20 tag keys at a time.
        self.key = key
        # The tag value of the resource.
        # 
        # Once specified, the tag value cannot be empty. The tag value can be up to 128 characters in length and cannot start with aliyun or acs:. It cannot contain http:// or https://.
        # 
        # Each tag key corresponds to one tag value. You can specify up to 20 tag values at a time.
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

class CreateTransitRouterRouteTableRequestRouteTableOptions(DaraModel):
    def __init__(
        self,
        multi_region_ecmp: str = None,
    ):
        # The multi-region equal-cost multi-path (ECMP) routing setting. Valid values:
        # - **disable** (default): disables multi-region ECMP routing. After multi-region ECMP routing is disabled, routes with the same prefix learned from different regions prefer the transit router whose Region ID is the smallest (sorted alphabetically) as the next hop when other route attributes are the same. This may change traffic latency and bandwidth consumption between regions. Make sure that you fully evaluate the impact before disabling this feature.
        # - **enable**: enables multi-region ECMP routing. After multi-region ECMP routing is enabled, routes with the same prefix learned from different regions form ECMP routes when other route attributes are the same. This may change traffic latency and bandwidth consumption between regions. Make sure that you fully evaluate the impact before enabling this feature.
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

