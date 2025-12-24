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
        # Specifies whether to release the system disk or data disk when the instance from which you want to detach the disk is released. Valid values:
        # 
        # *   true: releases the disk when the instance is released.
        # *   false: does not release the disk when the instance is released. The disk is retained as a pay-as-you-go data disk.
        # 
        # Default value: true.
        # 
        # Take note of the following items:
        # 
        # *   You cannot specify this parameter for disks for which the multi-attach feature is enabled.
        # *   If a data disk is to be detached, the default value is `false`.
        # *   If you want to detach an `elastic ephemeral disk`, you must set `DeleteWithInstance` to `true`.
        self.delete_with_instance = delete_with_instance
        # The ID of the disk that you want to detach.
        # 
        # *   The disk that you want to detach must be attached to an ECS instance and in the In Use (`In_use`) state.
        # *   The instance from which you want to detach a data disk must be in the `Running` or `Stopped` state.
        # *   The instance from which you want to detach the system disk must be in the `Stopped` state.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # The ID of the ECS instance from which you want to detach the disk.
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

