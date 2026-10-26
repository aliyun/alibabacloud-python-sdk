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
        # Specifies whether to enable the performance burst feature for disks that support this feature. Valid values:
        # 
        # true: enables the feature.
        # false: disables the feature.
        # Note
        # An error is returned if you specify any value for a disk that does not support the performance burst feature.
        self.bursting_enabled = bursting_enabled
        # Specifies whether to release the disk when the instance is released. Default value: null. A value of null indicates that the current value remains unchanged.
        # 
        # You cannot configure this parameter for cloud disks that have the multi-attach feature enabled.
        # 
        # An error is returned if you set the DeleteWithInstance parameter to false in the following scenarios:
        # 
        # The disk category is local disk (ephemeral).
        # The disk category is basic cloud disk (cloud) and the disk is not detachable (Portable=false).
        # Warning
        # If you set this parameter to false and the ECS instance to which the disk is attached is locked for security reasons (the OperationLocks parameter indicates "LockReason" : "security"), the disk is released along with the instance regardless of the DeleteWithInstance setting when the instance is released.
        self.delete_with_instance = delete_with_instance
        # The description of the disk. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # The ID of the disk whose attributes you want to modify.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # The cloud disk name. The name must be 2 to 128 characters in length and can contain characters in the Letter category of Unicode, such as English letters, Chinese characters, and digits. It can also contain colons (:), underscores (_), periods (.), and hyphens (-).
        self.disk_name = disk_name
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
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

