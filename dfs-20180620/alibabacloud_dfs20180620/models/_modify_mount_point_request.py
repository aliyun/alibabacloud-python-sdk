# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyMountPointRequest(DaraModel):
    def __init__(
        self,
        access_group_id: str = None,
        description: str = None,
        file_system_id: str = None,
        input_region_id: str = None,
        mount_point_id: str = None,
        status: str = None,
    ):
        self.access_group_id = access_group_id
        self.description = description
        # This parameter is required.
        self.file_system_id = file_system_id
        # This parameter is required.
        self.input_region_id = input_region_id
        # This parameter is required.
        self.mount_point_id = mount_point_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id

        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id

        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')

        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

