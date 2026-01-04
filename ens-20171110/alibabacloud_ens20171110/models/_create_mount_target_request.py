# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMountTargetRequest(DaraModel):
    def __init__(
        self,
        ens_region_id: str = None,
        file_system_id: str = None,
        mount_target_name: str = None,
        net_work_id: str = None,
    ):
        # The ID of the region.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The name of the mount target.
        # 
        # This parameter is required.
        self.mount_target_name = mount_target_name
        # The ID of the network.
        # 
        # This parameter is required.
        self.net_work_id = net_work_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.mount_target_name is not None:
            result['MountTargetName'] = self.mount_target_name

        if self.net_work_id is not None:
            result['NetWorkId'] = self.net_work_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('MountTargetName') is not None:
            self.mount_target_name = m.get('MountTargetName')

        if m.get('NetWorkId') is not None:
            self.net_work_id = m.get('NetWorkId')

        return self

