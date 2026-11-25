# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetachDiskRequest(DaraModel):
    def __init__(
        self,
        delete_with_instance: bool = None,
        disk_id: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The Settings for the automatic release property when uninstalling a system disk or data disk. Specifies whether the system disk or data disk is released when the ECS instance is released.
        # 
        # - true: The disk is released.
        # - false: The disk is not released. The disk is retained and transformed to a pay-as-you-go data disk.
        # 
        # Default value: true.
        # 
        # Take note of the following items:
        # 
        # - This parameter cannot be configured for disks that have the multi-attach attribute enabled.
        # - If you uninstall a data disk, the default value is `false`.
        # - If the disk to be uninstalled is an elastic ephemeral disk, you must set the `DeleteWithInstance` parameter to `true`.
        self.delete_with_instance = delete_with_instance
        # The ID of the disk to be detached.
        # 
        # - The disk must be attached to an instance and be in the In Use (`In_use`) state.
        # 
        # - When you detach a data disk, the instance to which the disk is attached must be in the Running (`Running`) or Stopped (`Stopped`) state.
        # 
        # - When you detach a system disk, the instance to which the disk is attached must be in the Stopped (`Stopped`) state.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # The ECS instance ID to which the disk to be uninstalled is attached.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

