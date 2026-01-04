# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeRouteTableListRequest(DaraModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_table_id: str = None,
        route_table_name: str = None,
        route_table_type: str = None,
        router_id: str = None,
        router_type: str = None,
        tag: List[main_models.DescribeRouteTableListRequestTag] = None,
        vpc_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the returned page. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The region ID of the VPC to which the route table belongs.
        # 
        # You can call [DescribeRegions](https://www.alibabacloud.com/help/vpc/developer-reference/api-vpc-2016-04-28-describeregions) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the route table belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the route table.
        self.route_table_id = route_table_id
        # The name of the route table.
        self.route_table_name = route_table_name
        # The type of the route table.
        # 
        # *   **System**
        # *   **Custom**
        self.route_table_type = route_table_type
        # The ID of vRouter to which the route table belongs.
        self.router_id = router_id
        # The type of the router to which the route table belongs. Valid value:
        # 
        # *   **VRouter** (default): a vRouter
        # *   **VBR**: a VBR
        self.router_type = router_type
        # The tags of the resource.
        self.tag = tag
        # The ID of the VPC to which the route table belongs. 
        # 
        # When this parameter is set, the value of **RouterType** is automatically assigned to **VRouter**.
        self.vpc_id = vpc_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        if self.route_table_name is not None:
            result['RouteTableName'] = self.route_table_name

        if self.route_table_type is not None:
            result['RouteTableType'] = self.route_table_type

        if self.router_id is not None:
            result['RouterId'] = self.router_id

        if self.router_type is not None:
            result['RouterType'] = self.router_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        if m.get('RouteTableName') is not None:
            self.route_table_name = m.get('RouteTableName')

        if m.get('RouteTableType') is not None:
            self.route_table_type = m.get('RouteTableType')

        if m.get('RouterId') is not None:
            self.router_id = m.get('RouterId')

        if m.get('RouterType') is not None:
            self.router_type = m.get('RouterType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeRouteTableListRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeRouteTableListRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The value of tag N to add to the resource. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        self.key = key
        # The value of tag N to add to the resource. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
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

