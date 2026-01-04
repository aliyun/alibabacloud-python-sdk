# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeRouteTableListResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        router_table_list: main_models.DescribeRouteTableListResponseBodyRouterTableList = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The detailed information about the route tables.
        self.router_table_list = router_table_list
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.router_table_list:
            self.router_table_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.router_table_list is not None:
            result['RouterTableList'] = self.router_table_list.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RouterTableList') is not None:
            temp_model = main_models.DescribeRouteTableListResponseBodyRouterTableList()
            self.router_table_list = temp_model.from_map(m.get('RouterTableList'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRouteTableListResponseBodyRouterTableList(DaraModel):
    def __init__(
        self,
        router_table_list_type: List[main_models.DescribeRouteTableListResponseBodyRouterTableListRouterTableListType] = None,
    ):
        self.router_table_list_type = router_table_list_type

    def validate(self):
        if self.router_table_list_type:
            for v1 in self.router_table_list_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RouterTableListType'] = []
        if self.router_table_list_type is not None:
            for k1 in self.router_table_list_type:
                result['RouterTableListType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.router_table_list_type = []
        if m.get('RouterTableListType') is not None:
            for k1 in m.get('RouterTableListType'):
                temp_model = main_models.DescribeRouteTableListResponseBodyRouterTableListRouterTableListType()
                self.router_table_list_type.append(temp_model.from_map(k1))

        return self

class DescribeRouteTableListResponseBodyRouterTableListRouterTableListType(DaraModel):
    def __init__(
        self,
        associate_type: str = None,
        creation_time: str = None,
        description: str = None,
        gateway_ids: main_models.DescribeRouteTableListResponseBodyRouterTableListRouterTableListTypeGatewayIds = None,
        owner_id: int = None,
        resource_group_id: str = None,
        route_propagation_enable: bool = None,
        route_table_id: str = None,
        route_table_name: str = None,
        route_table_type: str = None,
        router_id: str = None,
        router_type: str = None,
        status: str = None,
        tags: main_models.DescribeRouteTableListResponseBodyRouterTableListRouterTableListTypeTags = None,
        v_switch_ids: main_models.DescribeRouteTableListResponseBodyRouterTableListRouterTableListTypeVSwitchIds = None,
        vpc_id: str = None,
    ):
        # The type of the cloud resource with which the route table is associated. Valid values:
        # 
        # *   **VSwitch**: vSwitch
        # *   **Gateway**: IPv4 gateway
        self.associate_type = associate_type
        # The time when the route table was created.
        self.creation_time = creation_time
        # The information about the route table.
        self.description = description
        # The detailed information about the IPv4 gateway.
        self.gateway_ids = gateway_ids
        # The ID of the Alibaba Cloud account to which the route table belongs.
        self.owner_id = owner_id
        # The ID of the resource group to which the route table belongs.
        self.resource_group_id = resource_group_id
        # Whether to receive the propagation routes. Valid Values:
        # 
        # *   **true**: received.
        # 
        # *   **false**: not received.
        self.route_propagation_enable = route_propagation_enable
        # The ID of the route table.
        self.route_table_id = route_table_id
        # The name of the route table.
        self.route_table_name = route_table_name
        # The type of the route table. Valid values:
        # 
        # *   **Custom**
        # *   **System**
        self.route_table_type = route_table_type
        # The ID of the vRouter to which the route table belongs.
        self.router_id = router_id
        # The type of the vRouter to which the route table belongs. Valid values:
        # 
        # - **VRouter**: a vRouter.
        # 
        # - **VBR**: a VBR.
        self.router_type = router_type
        # The status of the route table. Valid values:
        # 
        # *   **Pending**
        # *   **Available**
        # *   **Deleting**
        self.status = status
        # The tags.
        self.tags = tags
        # The vSwitch IDs.
        self.v_switch_ids = v_switch_ids
        # The ID of the VPC to which the route table belongs.
        self.vpc_id = vpc_id

    def validate(self):
        if self.gateway_ids:
            self.gateway_ids.validate()
        if self.tags:
            self.tags.validate()
        if self.v_switch_ids:
            self.v_switch_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associate_type is not None:
            result['AssociateType'] = self.associate_type

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.gateway_ids is not None:
            result['GatewayIds'] = self.gateway_ids.to_map()

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.route_propagation_enable is not None:
            result['RoutePropagationEnable'] = self.route_propagation_enable

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

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociateType') is not None:
            self.associate_type = m.get('AssociateType')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GatewayIds') is not None:
            temp_model = main_models.DescribeRouteTableListResponseBodyRouterTableListRouterTableListTypeGatewayIds()
            self.gateway_ids = temp_model.from_map(m.get('GatewayIds'))

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RoutePropagationEnable') is not None:
            self.route_propagation_enable = m.get('RoutePropagationEnable')

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeRouteTableListResponseBodyRouterTableListRouterTableListTypeTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VSwitchIds') is not None:
            temp_model = main_models.DescribeRouteTableListResponseBodyRouterTableListRouterTableListTypeVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m.get('VSwitchIds'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeRouteTableListResponseBodyRouterTableListRouterTableListTypeVSwitchIds(DaraModel):
    def __init__(
        self,
        v_switch_id: List[str] = None,
    ):
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeRouteTableListResponseBodyRouterTableListRouterTableListTypeTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeRouteTableListResponseBodyRouterTableListRouterTableListTypeTagsTag] = None,
    ):
        self.tag = tag

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
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeRouteTableListResponseBodyRouterTableListRouterTableListTypeTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeRouteTableListResponseBodyRouterTableListRouterTableListTypeTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag that is added to the route table.
        self.key = key
        # The value of the tag that is added to the route table.
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

class DescribeRouteTableListResponseBodyRouterTableListRouterTableListTypeGatewayIds(DaraModel):
    def __init__(
        self,
        gateway_ids: List[str] = None,
    ):
        self.gateway_ids = gateway_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_ids is not None:
            result['GatewayIds'] = self.gateway_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayIds') is not None:
            self.gateway_ids = m.get('GatewayIds')

        return self

