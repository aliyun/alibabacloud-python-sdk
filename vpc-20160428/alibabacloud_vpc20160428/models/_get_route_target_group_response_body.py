# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class GetRouteTargetGroupResponseBody(DaraModel):
    def __init__(
        self,
        config_mode: str = None,
        create_time: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        route_target_group_description: str = None,
        route_target_group_id: str = None,
        route_target_group_name: str = None,
        route_target_member_list: List[main_models.GetRouteTargetGroupResponseBodyRouteTargetMemberList] = None,
        status: str = None,
        tags: List[main_models.GetRouteTargetGroupResponseBodyTags] = None,
        vpc_id: str = None,
    ):
        # The configuration mode of the route target group. Valid values:
        # 
        # - **Active-Standby**: active/standby mode.
        self.config_mode = config_mode
        # The time when the route target group was created.
        self.create_time = create_time
        # The region ID of the VPC to which the route target group belongs. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group to which the route target group belongs.
        self.resource_group_id = resource_group_id
        # The description of the route target group.
        self.route_target_group_description = route_target_group_description
        # The instance ID of the routing target group.
        self.route_target_group_id = route_target_group_id
        # The name of the route target group.
        self.route_target_group_name = route_target_group_name
        # The member list of the route target group.
        self.route_target_member_list = route_target_member_list
        # The status of the routing target group. Valid values:
        # 
        # - **Recovering**: The active/standby switchback is in progress.
        # - **Switched**: The active/standby switchover is complete.
        # - **Available**: The routing target group is available.
        # - **Abnormal**: The standby instance has instance failures.
        # - **Pending**: The routing target group is being created.
        # - **Switching**: The active/standby switchover is in progress.
        # - **Deleting**: The routing target group is being deleted.
        # - **Unavailable**: Both the primary and secondary instances have instance failures.
        self.status = status
        # The tags of the route target group.
        self.tags = tags
        # The ID of the VPC to which the route target group belongs.
        self.vpc_id = vpc_id

    def validate(self):
        if self.route_target_member_list:
            for v1 in self.route_target_member_list:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_mode is not None:
            result['ConfigMode'] = self.config_mode

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.route_target_group_description is not None:
            result['RouteTargetGroupDescription'] = self.route_target_group_description

        if self.route_target_group_id is not None:
            result['RouteTargetGroupId'] = self.route_target_group_id

        if self.route_target_group_name is not None:
            result['RouteTargetGroupName'] = self.route_target_group_name

        result['RouteTargetMemberList'] = []
        if self.route_target_member_list is not None:
            for k1 in self.route_target_member_list:
                result['RouteTargetMemberList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMode') is not None:
            self.config_mode = m.get('ConfigMode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RouteTargetGroupDescription') is not None:
            self.route_target_group_description = m.get('RouteTargetGroupDescription')

        if m.get('RouteTargetGroupId') is not None:
            self.route_target_group_id = m.get('RouteTargetGroupId')

        if m.get('RouteTargetGroupName') is not None:
            self.route_target_group_name = m.get('RouteTargetGroupName')

        self.route_target_member_list = []
        if m.get('RouteTargetMemberList') is not None:
            for k1 in m.get('RouteTargetMemberList'):
                temp_model = main_models.GetRouteTargetGroupResponseBodyRouteTargetMemberList()
                self.route_target_member_list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetRouteTargetGroupResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetRouteTargetGroupResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class GetRouteTargetGroupResponseBodyRouteTargetMemberList(DaraModel):
    def __init__(
        self,
        enable_status: str = None,
        health_check_status: str = None,
        member_id: str = None,
        member_type: str = None,
        weight: int = None,
    ):
        # The enable status of the route target group member. Valid values:
        # 
        # - **Enable**: Enabled.
        # - **Disable**: Disabled.
        # 
        # Only route target group members in the disabled state can be replaced with other instances. Route target group members in the enabled state cannot be modified.
        self.enable_status = enable_status
        # The health check status of the route target group member. Valid values:
        # 
        # - **Normal**: Normal.
        # - **Abnormal**: Abnormal.
        self.health_check_status = health_check_status
        # The instance ID of the routing target group member.
        self.member_id = member_id
        # The member type of the route target group.
        # 
        # Currently supported types:
        # 
        # - **GatewayLoadBalancerEndpoint**
        self.member_type = member_type
        # The weight of the route target group member. Valid values:
        # 
        # - **100**: The member is the active instance.
        # - **0**: The member is the standby instance.
        # 
        # The weight can only be set during creation and cannot be modified.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.health_check_status is not None:
            result['HealthCheckStatus'] = self.health_check_status

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.member_type is not None:
            result['MemberType'] = self.member_type

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('HealthCheckStatus') is not None:
            self.health_check_status = m.get('HealthCheckStatus')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

