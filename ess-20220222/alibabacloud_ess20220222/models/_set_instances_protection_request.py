# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetInstancesProtectionRequest(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        owner_id: int = None,
        protected_from_scale_in: bool = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        # The IDs of the ECS instances.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        self.owner_id = owner_id
        # Specifies whether to protect ECS instances from being stopped or removed from the scaling group during scale-ins. Valid values:
        # 
        # *   true
        # *   false
        # 
        # This parameter is required.
        self.protected_from_scale_in = protected_from_scale_in
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
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.protected_from_scale_in is not None:
            result['ProtectedFromScaleIn'] = self.protected_from_scale_in

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProtectedFromScaleIn') is not None:
            self.protected_from_scale_in = m.get('ProtectedFromScaleIn')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

