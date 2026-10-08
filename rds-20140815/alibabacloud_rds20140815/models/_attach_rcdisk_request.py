# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachRCDiskRequest(DaraModel):
    def __init__(
        self,
        delete_with_instance: bool = None,
        disk_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # Specifies whether the cloud disk is released when the instance is released. Valid values:
        # 
        # true: The cloud disk is released when the instance is released.
        # false: The cloud disk is not released when the instance is released. The cloud disk is retained as a pay-as-you-go data cloud disk.
        # Default value: false.
        # 
        # When you configure this parameter, take note of the following items:
        # 
        # If you set DeleteWithInstance to false and the instance is locked for security reasons, meaning that OperationLocks contains "LockReason" : "security", this parameter is ignored and the cloud disk is released along with the instance.
        # 
        # If the cloud disk to be attached is an elastic ephemeral disk, you must set DeleteWithInstance to true.
        # 
        # This parameter is not supported for cloud disks that have the multi-attach feature enabled.
        self.delete_with_instance = delete_with_instance
        # The ID of the cloud disk to be attached. The cloud disk (DiskId) and the instance (InstanceId) must be in the same zone.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # The ID of the destination RDS Custom instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID.
        self.region_id = region_id

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

