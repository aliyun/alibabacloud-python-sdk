# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAutoProvisioningGroupRequest(DaraModel):
    def __init__(
        self,
        auto_provisioning_group_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        terminate_instances: bool = None,
    ):
        # The ID of the auto provisioning group.
        # 
        # This parameter is required.
        self.auto_provisioning_group_id = auto_provisioning_group_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the auto provisioning group.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to release instances in the auto provisioning group. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  By default, this parameter inherits the value of `TerminateInstances` that you specified when you call the `CreateAutoProvisioningGroup` operation to create an auto provisioning group. You can also change the value of `TerminateInstances` when you call the DeleteAutoProvisioningGroup operation to delete the auto provisioning group.
        self.terminate_instances = terminate_instances

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_provisioning_group_id is not None:
            result['AutoProvisioningGroupId'] = self.auto_provisioning_group_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.terminate_instances is not None:
            result['TerminateInstances'] = self.terminate_instances

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoProvisioningGroupId') is not None:
            self.auto_provisioning_group_id = m.get('AutoProvisioningGroupId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TerminateInstances') is not None:
            self.terminate_instances = m.get('TerminateInstances')

        return self

