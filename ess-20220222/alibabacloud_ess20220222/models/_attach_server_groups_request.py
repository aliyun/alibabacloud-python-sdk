# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class AttachServerGroupsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        force_attach: bool = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
        server_groups: List[main_models.AttachServerGroupsRequestServerGroups] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # Specifies whether to add the existing Elastic Compute Service (ECS) instances or elastic container instances in the scaling group to the server group. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.force_attach = force_attach
        self.owner_id = owner_id
        # The region ID of the scaling group.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        # The information about the server groups.
        # 
        # This parameter is required.
        self.server_groups = server_groups

    def validate(self):
        if self.server_groups:
            for v1 in self.server_groups:
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

        result['ServerGroups'] = []
        if self.server_groups is not None:
            for k1 in self.server_groups:
                result['ServerGroups'].append(k1.to_map() if k1 else None)

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

        self.server_groups = []
        if m.get('ServerGroups') is not None:
            for k1 in m.get('ServerGroups'):
                temp_model = main_models.AttachServerGroupsRequestServerGroups()
                self.server_groups.append(temp_model.from_map(k1))

        return self

class AttachServerGroupsRequestServerGroups(DaraModel):
    def __init__(
        self,
        port: int = None,
        server_group_id: str = None,
        type: str = None,
        weight: int = None,
    ):
        # The port used by ECS instances or elastic container instances after being added as backend servers to the server group.
        # 
        # Valid values: 1 to 65535.
        self.port = port
        # The ID of the server group.
        # 
        # This parameter is required.
        self.server_group_id = server_group_id
        # The type of the server group. Valid values:
        # 
        # *   ALB
        # *   NLB
        # 
        # This parameter is required.
        self.type = type
        # The weight of an ECS instance or elastic container instance as a backend server of the server group. Valid values: 0 to 100.
        # 
        # If you assign a higher weight to an instance, the instance is allocated a larger proportion of access requests. If you assign zero weight to an instance, the instance is allocated no access requests.
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

        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        if self.type is not None:
            result['Type'] = self.type

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

