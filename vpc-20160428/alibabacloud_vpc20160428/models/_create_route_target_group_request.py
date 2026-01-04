# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateRouteTargetGroupRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        config_mode: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        route_target_group_description: str = None,
        route_target_group_name: str = None,
        route_target_member_list: List[main_models.CreateRouteTargetGroupRequestRouteTargetMemberList] = None,
        tag: List[main_models.CreateRouteTargetGroupRequestTag] = None,
        vpc_id: str = None,
    ):
        # Client token used to ensure the idempotence of the request. Generate a parameter value from your client to ensure that it is unique across different requests. ClientToken supports only ASCII characters. Note: If you do not specify this, the system automatically uses the RequestId of the API request as the ClientToken identifier. Each API request has a different RequestId.
        self.client_token = client_token
        # The configuration mode of the route target group. Supported modes:
        # 
        # - **Active-Standby**: Active-Standby mode.
        # 
        # This parameter is required.
        self.config_mode = config_mode
        # The region ID to which the route target group belongs. You can obtain the region ID by calling the DescribeRegions interface.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        # 
        # For more information about resource groups, see [What is a Resource Group](https://help.aliyun.com/document_detail/2381067.html).
        self.resource_group_id = resource_group_id
        # The description of the route target group.
        # 
        # The description length must be between 1 and 256 characters, and cannot start with http:// or https://.
        self.route_target_group_description = route_target_group_description
        # The name of the route target group.
        # 
        # The name length must be between 1 and 128 characters, and cannot start with http:// or https://.
        self.route_target_group_name = route_target_group_name
        # The member list of the route target group.
        # 
        # In Active-Standby mode, the following restrictions apply to the members of the route target group:
        # 
        # 1. The number of route target group members must be 2.
        # 2. The route target group members must belong to different availability zones.
        # 
        # This parameter is required.
        self.route_target_member_list = route_target_member_list
        # The tags of the resource.
        self.tag = tag
        # The ID of the VPC to which the route target group belongs.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        if self.route_target_member_list:
            for v1 in self.route_target_member_list:
                 if v1:
                    v1.validate()
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

        if self.config_mode is not None:
            result['ConfigMode'] = self.config_mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.route_target_group_description is not None:
            result['RouteTargetGroupDescription'] = self.route_target_group_description

        if self.route_target_group_name is not None:
            result['RouteTargetGroupName'] = self.route_target_group_name

        result['RouteTargetMemberList'] = []
        if self.route_target_member_list is not None:
            for k1 in self.route_target_member_list:
                result['RouteTargetMemberList'].append(k1.to_map() if k1 else None)

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConfigMode') is not None:
            self.config_mode = m.get('ConfigMode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RouteTargetGroupDescription') is not None:
            self.route_target_group_description = m.get('RouteTargetGroupDescription')

        if m.get('RouteTargetGroupName') is not None:
            self.route_target_group_name = m.get('RouteTargetGroupName')

        self.route_target_member_list = []
        if m.get('RouteTargetMemberList') is not None:
            for k1 in m.get('RouteTargetMemberList'):
                temp_model = main_models.CreateRouteTargetGroupRequestRouteTargetMemberList()
                self.route_target_member_list.append(temp_model.from_map(k1))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateRouteTargetGroupRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateRouteTargetGroupRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. Up to 20 tag keys are supported. If you need to pass this value, you cannot input an empty string.
        # 
        # A tag key can have up to 128 characters and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. Up to 20 tag values are supported. If you need to pass this value, you can input an empty string.
        # 
        # A tag value can have up to 128 characters and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
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

class CreateRouteTargetGroupRequestRouteTargetMemberList(DaraModel):
    def __init__(
        self,
        member_id: str = None,
        member_type: str = None,
        weight: int = None,
    ):
        # The instance ID of the route target group member.
        # 
        # This parameter is required.
        self.member_id = member_id
        # The type of the route target group member.
        # 
        # Currently supported types:
        # 
        # - **GatewayLoadBalancerEndpoint**
        # 
        # In Active-Standby mode, all members of the route target group must have the same type.
        # 
        # This parameter is required.
        self.member_type = member_type
        # The weight value of the route target group member. Values:
        # 
        # - **100**: Indicates the member is a primary instance.
        # - **0**: Indicates the member is a standby instance.
        # 
        # The weight value can only be set during creation and cannot be modified.
        # 
        # This parameter is required.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.member_type is not None:
            result['MemberType'] = self.member_type

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

