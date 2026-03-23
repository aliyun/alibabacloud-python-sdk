# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRCDiskAttributeRequest(DaraModel):
    def __init__(
        self,
        bursting_enabled: bool = None,
        delete_with_instance: bool = None,
        description: str = None,
        disk_id: str = None,
        disk_name: str = None,
        region_id: str = None,
    ):
        # Specifies whether to enable the burst (performance burst) feature for disks that support it. Valid values:
        # 
        # true: Enabled.
        # false: No.
        # Note
        # If you specify any value for a disk that does not support the burst feature, an error is returned.
        self.bursting_enabled = bursting_enabled
        # Specifies whether the disk is released when its associated instance is released. Default value: none, which means the current setting remains unchanged.
        # 
        # This parameter cannot be set for disks with the multi-attach feature enabled.
        # 
        # An error occurs if you set DeleteWithInstance to false in either of the following cases:
        # 
        # - The disk category is local disk (ephemeral).
        # - The disk category is basic disk (cloud) and the disk is non-portable (Portable=false).
        # 
        # Warning
        # If you set DeleteWithInstance to false, but the ECS instance to which the disk is attached is security locked (indicated by "LockReason": "security" in OperationLocks), the disk will be released together with the instance regardless of the DeleteWithInstance setting when the instance is released.
        self.delete_with_instance = delete_with_instance
        # The description of the disk. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # The ID of the disk whose property you want to modify.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # Disk name. The name must be 2 to 128 characters in length and can contain characters from the letter categorization in Unicode (including English letters, Chinese characters, and digits). It can also include colons (:), underscores (_), periods (.), or hyphens (-).
        self.disk_name = disk_name
        # The region ID. You can call DescribeRegions to obtain valid region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance

        if self.description is not None:
            result['Description'] = self.description

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

