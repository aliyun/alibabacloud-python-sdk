# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRouteTableAttributesRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_propagation_enable: bool = None,
        route_table_id: str = None,
        route_table_name: str = None,
    ):
        # The description of the route table.
        # 
        # The description must be 1 to 256 characters in length, and cannot start with `http://` or `https://`.
        self.description = description
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the virtual private cloud (VPC) to which the custom route table belongs.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Indicates whether to enable route propagation to receive dynamic routes. Valid values:
        # 
        # - **true** (default): enables route propagation.
        # 
        # - **false**: disables route propagation.
        self.route_propagation_enable = route_propagation_enable
        # The ID of the route table.
        # 
        # This parameter is required.
        self.route_table_id = route_table_id
        # The name of the route table.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.route_table_name = route_table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.route_propagation_enable is not None:
            result['RoutePropagationEnable'] = self.route_propagation_enable

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        if self.route_table_name is not None:
            result['RouteTableName'] = self.route_table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RoutePropagationEnable') is not None:
            self.route_propagation_enable = m.get('RoutePropagationEnable')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        if m.get('RouteTableName') is not None:
            self.route_table_name = m.get('RouteTableName')

        return self

