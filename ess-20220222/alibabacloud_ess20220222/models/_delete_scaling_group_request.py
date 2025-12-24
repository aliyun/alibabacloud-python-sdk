# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteScalingGroupRequest(DaraModel):
    def __init__(
        self,
        force_delete: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        # Specifies whether to enforce the deletion of the scaling group, including the removal of the current ECS instances or elastic container instances from the scaling group and their subsequent release, even if the scaling group is actively undergoing scaling activities. Valid values:
        # 
        # *   true: enforces the deletion of the scaling group. In this case, the scaling group first enters the Disabled state, ceasing acceptance of new scaling requests. Auto Scaling awaits the conclusion of all ongoing scaling activities in the scaling group before it automatically removes the current ECS instances or elastic container instances from the scaling group and enforces the deletion operation. Note that manually added instances are merely removed from the scaling group, whereas auto-provisioned instances are removed and deleted.
        # 
        # *   false: does not enforce the deletion of the scaling group. The scaling group will be disabled and then deleted once all the following requirements are satisfied:
        # 
        #     *   The scaling group has no ongoing scaling activities.
        #     *   The scaling group contains no ECS instances or elastic container instances (Total Capacity=0).
        # 
        # Default value: false.
        self.force_delete = force_delete
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the scaling group.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force_delete is not None:
            result['ForceDelete'] = self.force_delete

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

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
        if m.get('ForceDelete') is not None:
            self.force_delete = m.get('ForceDelete')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

