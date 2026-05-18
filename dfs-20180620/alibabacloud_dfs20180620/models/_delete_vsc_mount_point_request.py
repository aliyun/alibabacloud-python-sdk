# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteVscMountPointRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        input_region_id: str = None,
        mount_point_id: str = None,
    ):
        # This parameter is required.
        self.file_system_id = file_system_id
        # This parameter is required.
        self.input_region_id = input_region_id
        # This parameter is required.
        self.mount_point_id = mount_point_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id

        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')

        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')

        return self

