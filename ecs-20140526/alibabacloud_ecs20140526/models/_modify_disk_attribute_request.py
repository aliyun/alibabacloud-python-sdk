# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyDiskAttributeRequest(DaraModel):
    def __init__(
        self,
        bursting_enabled: bool = None,
        delete_auto_snapshot: bool = None,
        delete_with_instance: bool = None,
        description: str = None,
        disk_id: str = None,
        disk_ids: List[str] = None,
        disk_name: str = None,
        enable_auto_snapshot: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to enable performance burst for the disk if the disk supports performance burst. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  An error is reported if you specify this parameter for a disk that does not support performance burst.
        self.bursting_enabled = bursting_enabled
        # Specifies whether to delete the automatic snapshots of the disk when the disk is released. Valid values:
        # 
        # *   true
        # *   false
        # 
        # This parameter is empty by default, which indicates that the current value remains unchanged.
        self.delete_auto_snapshot = delete_auto_snapshot
        # Specifies whether to release the disk together with the associated instance. This parameter is empty by default, which indicates that the current value remains unchanged.
        # 
        # An error is returned if you set `DeleteWithInstance` to `false` in one of the following cases:
        # 
        # *   The disk is a local disk.
        # *   The disk is a basic disk and is not removable. If the Portable attribute of a disk is set to false, the disk is not removable.
        # 
        # **
        # 
        # **Warning** If you set DeleteWithInstance to false and the instance to which the disk is attached is locked for security reasons, the DeleteWithInstance attribute of the disk is ignored and the disk is released together with the instance. If "LockReason" : "security" is displayed in the response when you query information about an instance, the instance is locked for security reasons.
        self.delete_with_instance = delete_with_instance
        # The description of the disk. The description must be 2 to 256 characters in length. It cannot start with `http://` or `https://`.
        self.description = description
        # The ID of the disk whose attributes you want to modify.
        # 
        # >  You can specify `DiskId` or `DiskIds.N`, but not both.
        self.disk_id = disk_id
        # The IDs of the disks whose attributes you want to modify. Valid values of N: 0 to 100.
        # 
        # >  You can specify `DiskId` or `DiskIds.N`, but not both.
        self.disk_ids = disk_ids
        # The name of the disk. The name must be 2 to 128 characters in length and can contain Unicode characters under the Decimal Number category and the categories whose names contain Letter. The name can also contain colons (:), underscores (_), periods (.), and hyphens (-).
        self.disk_name = disk_name
        # Specifies whether to enable the automatic snapshot policy feature. Valid values:
        # 
        # *   true: enables the automatic snapshot policy feature for the cloud disk.
        # *   false: disables the automatic snapshot policy feature for the cloud disk.
        # 
        # This parameter is empty by default, which indicates that the current value remains unchanged.
        # 
        # >  This parameter is deprecated. By default, the automatic snapshot policy feature is enabled for cloud disks. You only need to apply an automatic snapshot policy to a cloud disk before you can use the automatic snapshot policy.
        self.enable_auto_snapshot = enable_auto_snapshot
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the command. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent list of regions.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.delete_auto_snapshot is not None:
            result['DeleteAutoSnapshot'] = self.delete_auto_snapshot

        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance

        if self.description is not None:
            result['Description'] = self.description

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.disk_ids is not None:
            result['DiskIds'] = self.disk_ids

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.enable_auto_snapshot is not None:
            result['EnableAutoSnapshot'] = self.enable_auto_snapshot

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('DeleteAutoSnapshot') is not None:
            self.delete_auto_snapshot = m.get('DeleteAutoSnapshot')

        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('DiskIds') is not None:
            self.disk_ids = m.get('DiskIds')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('EnableAutoSnapshot') is not None:
            self.enable_auto_snapshot = m.get('EnableAutoSnapshot')

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

        return self

