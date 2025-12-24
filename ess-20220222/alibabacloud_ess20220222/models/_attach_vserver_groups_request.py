# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class AttachVServerGroupsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        force_attach: bool = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
        vserver_groups: List[main_models.AttachVServerGroupsRequestVServerGroups] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # Specifies whether to add the existing Elastic Compute Service (ECS) instances or elastic container instances in the scaling group to the new vServer group. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.force_attach = force_attach
        self.owner_id = owner_id
        # The region ID of the scaling group. Examples: cn-hangzhou and cn-shanghai. For information about regions and zones, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        # The information about the vServer groups.
        # 
        # This parameter is required.
        self.vserver_groups = vserver_groups

    def validate(self):
        if self.vserver_groups:
            for v1 in self.vserver_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.force_attach is not None:
            result['ForceAttach'] = self.force_attach

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        result['VServerGroups'] = []
        if self.vserver_groups is not None:
            for k1 in self.vserver_groups:
                result['VServerGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ForceAttach') is not None:
            self.force_attach = m.get('ForceAttach')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        self.vserver_groups = []
        if m.get('VServerGroups') is not None:
            for k1 in m.get('VServerGroups'):
                temp_model = main_models.AttachVServerGroupsRequestVServerGroups()
                self.vserver_groups.append(temp_model.from_map(k1))

        return self

class AttachVServerGroupsRequestVServerGroups(DaraModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        vserver_group_attributes: List[main_models.AttachVServerGroupsRequestVServerGroupsVServerGroupAttributes] = None,
    ):
        # The ID of the CLB instance to which the new vServer group belongs.
        self.load_balancer_id = load_balancer_id
        # The attributes of the vServer group.
        self.vserver_group_attributes = vserver_group_attributes

    def validate(self):
        if self.vserver_group_attributes:
            for v1 in self.vserver_group_attributes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        result['VServerGroupAttributes'] = []
        if self.vserver_group_attributes is not None:
            for k1 in self.vserver_group_attributes:
                result['VServerGroupAttributes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        self.vserver_group_attributes = []
        if m.get('VServerGroupAttributes') is not None:
            for k1 in m.get('VServerGroupAttributes'):
                temp_model = main_models.AttachVServerGroupsRequestVServerGroupsVServerGroupAttributes()
                self.vserver_group_attributes.append(temp_model.from_map(k1))

        return self

class AttachVServerGroupsRequestVServerGroupsVServerGroupAttributes(DaraModel):
    def __init__(
        self,
        port: int = None,
        vserver_group_id: str = None,
        weight: int = None,
    ):
        # The port number over which Auto Scaling adds ECS instances or elastic container instances to the new vServer group. Valid values: 1 to 65535.
        self.port = port
        # The ID of the vServer group.
        self.vserver_group_id = vserver_group_id
        # The weight of an ECS instance or elastic container instance as a backend server. Valid values: 0 to 100.
        # 
        # Default value: 50.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['Port'] = self.port

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

