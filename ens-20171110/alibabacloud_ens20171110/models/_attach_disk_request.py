# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachDiskRequest(DaraModel):
    def __init__(
        self,
        delete_with_instance: str = None,
        disk_id: str = None,
        instance_id: str = None,
    ):
        # Specifies whether the cloud disk to be mounted is released when the instance is released. Valid values:
        # 
        # - true: The cloud disk is released when the instance is released.
        # - false: The cloud disk is retained when the instance is released.
        # - Empty: The default value is false.
        self.delete_with_instance = delete_with_instance
        # The ID of the cloud disk to mount. The cloud disk and the instance must be in the same edge zone.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

