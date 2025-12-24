# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DetachAlbServerGroupsRequest(DaraModel):
    def __init__(
        self,
        alb_server_groups: List[main_models.DetachAlbServerGroupsRequestAlbServerGroups] = None,
        client_token: str = None,
        force_detach: bool = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        # Details of the ALB server groups.
        # 
        # This parameter is required.
        self.alb_server_groups = alb_server_groups
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that the value is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure the idempotence of a request](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # Specifies whether to remove the existing Elastic Compute Service (ECS) instances from the Application Load Balancer (ALB) server group marked for detachment. Valid values:
        # 
        # *   true: removes the existing ECS instances from the ALB server group and returns the value of `ScalingActivityId`. You can query the value of ScalingActivityId to check whether the existing ECS instances are removed from the ALB server group.
        # *   false: does not remove the existing ECS instances from the ALB server group.
        # 
        # Default value: false.
        self.force_detach = force_detach
        self.owner_id = owner_id
        # The region ID of the scaling group. Examples: cn-hangzhou and cn-shanghai.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id

    def validate(self):
        if self.alb_server_groups:
            for v1 in self.alb_server_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlbServerGroups'] = []
        if self.alb_server_groups is not None:
            for k1 in self.alb_server_groups:
                result['AlbServerGroups'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.force_detach is not None:
            result['ForceDetach'] = self.force_detach

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alb_server_groups = []
        if m.get('AlbServerGroups') is not None:
            for k1 in m.get('AlbServerGroups'):
                temp_model = main_models.DetachAlbServerGroupsRequestAlbServerGroups()
                self.alb_server_groups.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ForceDetach') is not None:
            self.force_detach = m.get('ForceDetach')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

class DetachAlbServerGroupsRequestAlbServerGroups(DaraModel):
    def __init__(
        self,
        alb_server_group_id: str = None,
        port: int = None,
    ):
        # The ID of the ALB server group.
        # 
        # This parameter is required.
        self.alb_server_group_id = alb_server_group_id
        # The port number used by the ECS instances in the ALB server group.
        # 
        # This parameter is required.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alb_server_group_id is not None:
            result['AlbServerGroupId'] = self.alb_server_group_id

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbServerGroupId') is not None:
            self.alb_server_group_id = m.get('AlbServerGroupId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

