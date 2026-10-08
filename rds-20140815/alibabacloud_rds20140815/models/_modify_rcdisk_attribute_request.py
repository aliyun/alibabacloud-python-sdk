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
        # Specifies whether to enable the performance burst feature for cloud disks that support burst. Valid values:
        # 
        # true: Enabled.
        # false: Disabled.
        # Note
        # An error is returned if you pass any value for cloud disks that do not support the burst feature.
        self.bursting_enabled = bursting_enabled
        # Specifies whether to release the cloud disk when the associated instance is released. Default value: null, which indicates that the current value is not changed.
        # 
        # Cloud disks that have the multi-attach feature enabled do not support this parameter.
        # 
        # An error is returned if you set DeleteWithInstance to false in the following cases:
        # 
        # The category of the cloud disk is local disk (ephemeral).
        # The category of the cloud disk is basic cloud disk (cloud) and the cloud disk is not detachable (Portable=false).
        # Warning
        # If you set DeleteWithInstance to false and the ECS instance to which the cloud disk is attached is security-locked with "LockReason" : "security" in OperationLocks, the DeleteWithInstance attribute of the cloud disk is ignored and the cloud disk is released together with the instance.
        self.delete_with_instance = delete_with_instance
        # The description of the cloud disk. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # The ID of the cloud disk whose attributes you want to modify.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # The name of the cloud disk. The name must be 2 to 128 characters in length and can contain Unicode characters under the letter category (including letters from various languages, Chinese characters, and digits). The name can contain colons (:), underscores (_), periods (.), or hyphens (-).
        self.disk_name = disk_name
        # The region ID. You can call DescribeRegions to obtain the region ID.
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

