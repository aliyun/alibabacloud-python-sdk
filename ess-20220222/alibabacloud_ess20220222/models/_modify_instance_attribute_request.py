# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyInstanceAttributeRequest(DaraModel):
    def __init__(
        self,
        entrusted: bool = None,
        instance_id: str = None,
        instance_ids: List[str] = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        # Specifies whether to allow the scaling group to manage the lifecycles of the manually added ECS instances. Valid values:
        # 
        # *   true: allows the scaling group to manage the lifecycles of the manually added ECS instances. The scaling group manages the lifecycles of manually added instances and automatically created instances in the same manner. In this case, Auto Scaling releases the instances when they are removed from the scaling group. This rule does not apply to instances that are removed by calling the DetachInstances operation.
        # *   false: does not allow the scaling group to manage the lifecycles of the manually added ECS instances. In this case, Auto Scaling does not release the instances when they are removed from the scaling group.
        # 
        # >  You can specify this parameter only for ECS instances that are manually added to the scaling group.
        self.entrusted = entrusted
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # The instance IDs.
        self.instance_ids = instance_ids
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

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entrusted is not None:
            result['Entrusted'] = self.entrusted

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

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
        if m.get('Entrusted') is not None:
            self.entrusted = m.get('Entrusted')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

