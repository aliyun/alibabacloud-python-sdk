# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeResourceGroupRequest(DaraModel):
    def __init__(
        self,
        new_resource_group_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: str = None,
        resource_owner_account: str = None,
        resource_type: str = None,
    ):
        # The ID of the resource group to which you want to move the scaling group.
        # 
        # This parameter is required.
        self.new_resource_group_id = new_resource_group_id
        self.owner_id = owner_id
        # The region ID of the scaling group.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the scaling group that you want to move from the current resource group to another resource group.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        # The resource type. Set the value to scalinggroup.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

