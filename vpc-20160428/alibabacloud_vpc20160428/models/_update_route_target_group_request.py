# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class UpdateRouteTargetGroupRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        route_target_group_description: str = None,
        route_target_group_id: str = None,
        route_target_group_name: str = None,
        route_target_member_list: List[main_models.UpdateRouteTargetGroupRequestRouteTargetMemberList] = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters. If you do not specify this parameter, the system automatically uses the RequestId value as the ClientToken value. The RequestId value may be different for each API request.
        self.client_token = client_token
        # The region ID of the route target group instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The description of the route target group. 
        # 
        # The description must be 1 to 256 characters in length and cannot start with http:// or https://.
        self.route_target_group_description = route_target_group_description
        # The routing target group instance ID.
        # 
        # This parameter is required.
        self.route_target_group_id = route_target_group_id
        # The name of the route target group.
        # 
        # The name must be 1 to 128 characters in length and cannot start with http:// or https://.
        self.route_target_group_name = route_target_group_name
        # The member list of the route target group.
        # 
        # In active/standby mode, the following limits apply to route target group members:
        # 
        # 1. The number of route target group members must be 2.
        # 2. The route target group members must belong to different zones.
        self.route_target_member_list = route_target_member_list

    def validate(self):
        if self.route_target_member_list:
            for v1 in self.route_target_member_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RouteTargetGroupDescription') is not None:
            self.route_target_group_description = m.get('RouteTargetGroupDescription')

        if m.get('RouteTargetGroupId') is not None:
            self.route_target_group_id = m.get('RouteTargetGroupId')

        if m.get('RouteTargetGroupName') is not None:
            self.route_target_group_name = m.get('RouteTargetGroupName')

        self.route_target_member_list = []
        if m.get('RouteTargetMemberList') is not None:
            for k1 in m.get('RouteTargetMemberList'):
                temp_model = main_models.UpdateRouteTargetGroupRequestRouteTargetMemberList()
                self.route_target_member_list.append(temp_model.from_map(k1))

        return self

class UpdateRouteTargetGroupRequestRouteTargetMemberList(DaraModel):
    def __init__(
        self,
        member_id: str = None,
        member_type: str = None,
        weight: int = None,
    ):
        # The instance ID of the route target group member.
        self.member_id = member_id
        # The member type of the route target group.
        # 
        # Currently supported type:
        # 
        # - **GatewayLoadBalancerEndpoint**
        # 
        # In active/standby mode, all members of the route target group must be of the same type.
        self.member_type = member_type
        # The weight of the route target group member. Valid values:
        # 
        # - 100: The member is the active instance.
        # - 0: The member is the standby instance.
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

