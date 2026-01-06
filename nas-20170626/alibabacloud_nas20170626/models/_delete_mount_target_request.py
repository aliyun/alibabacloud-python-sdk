# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMountTargetRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        mount_target_domain: str = None,
    ):
        # The ID of the file system.
        # 
        # *   Sample ID of a General-purpose NAS file system: 31a8e4\\*\\*\\*\\*.
        # *   The IDs of Extreme NAS file systems must start with `extreme-`, for example, extreme-0015\\*\\*\\*\\*.
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-125487\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The domain name of the mount target.
        # 
        # This parameter is required.
        self.mount_target_domain = mount_target_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')

        return self

