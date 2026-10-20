# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DiskInit(DaraModel):
    def __init__(
        self,
        disk_name: str = None,
        local_disk: bool = None,
        mkfs_type: str = None,
        mount_for_runtime: bool = None,
        mount_target: str = None,
    ):
        # The unique identifier for a disk in the node pool.
        # - When local_disk is set to false, the value must match one of the disk_name values in scaling_group.data_disks.
        # - When local_disk is set to true, the value must be different from all disk_name values in scaling_group.data_disks.
        # 
        # This parameter is required.
        self.disk_name = disk_name
        # Specifies whether this configuration applies to a local disk. When this parameter is set to true:
        # - If the disk cannot be matched by using the ECS DiskName and symbolic links, the local disk can be matched.
        # - If the disk is detected as uninitialized during boot, it is reinitialized.
        # - Both mount_target and mkfs_type must be set or left empty at the same time.
        # - When used in combination with mount_for_runtime, if the local disk is reinitialized, the node must be removed from and then re-added to the node pool.
        self.local_disk = local_disk
        # The type of the file system for automatic formatting. An empty value indicates that the disk is not formatted.
        self.mkfs_type = mkfs_type
        # Specifies whether container runtime data is stored on the disk.
        self.mount_for_runtime = mount_for_runtime
        # The mount directory. An empty value indicates that the disk is not mounted.
        self.mount_target = mount_target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_name is not None:
            result['disk_name'] = self.disk_name

        if self.local_disk is not None:
            result['local_disk'] = self.local_disk

        if self.mkfs_type is not None:
            result['mkfs_type'] = self.mkfs_type

        if self.mount_for_runtime is not None:
            result['mount_for_runtime'] = self.mount_for_runtime

        if self.mount_target is not None:
            result['mount_target'] = self.mount_target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disk_name') is not None:
            self.disk_name = m.get('disk_name')

        if m.get('local_disk') is not None:
            self.local_disk = m.get('local_disk')

        if m.get('mkfs_type') is not None:
            self.mkfs_type = m.get('mkfs_type')

        if m.get('mount_for_runtime') is not None:
            self.mount_for_runtime = m.get('mount_for_runtime')

        if m.get('mount_target') is not None:
            self.mount_target = m.get('mount_target')

        return self

