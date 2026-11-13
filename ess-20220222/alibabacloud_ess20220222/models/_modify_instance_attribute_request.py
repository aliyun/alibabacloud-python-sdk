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
        # Specifies whether the lifecycle (epoch) of an instance manually added to the scaling group is managed by the scaling group. Valid values:
        # 
        # - true: Managed. The lifecycle (epoch) of the instance is managed by Auto Scaling, which is consistent with that of instances automatically created in the scaling group. The instance is automatically released when it is removed from the scaling group, excluding instances removed when you invoke the DetachInstances operation.
        # - false: Unmanaged. The instance is not released when it is removed from the scaling group.
        # 
        # > This parameter applies only to instances manually added to the scaling group, not to instances created within the scaling group.
        self.entrusted = entrusted
        # The ID of the ECS instance in the scaling group.
        self.instance_id = instance_id
        # The list of instance IDs.
        self.instance_ids = instance_ids
        self.owner_id = owner_id
        # The ID of the region to which the scaling group belongs.
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

