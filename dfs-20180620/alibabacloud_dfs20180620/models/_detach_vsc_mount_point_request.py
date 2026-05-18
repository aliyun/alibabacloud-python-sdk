# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DetachVscMountPointRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        file_system_id: str = None,
        input_region_id: str = None,
        instance_ids: List[str] = None,
        mount_point_id: str = None,
        use_assume_role_chk_server_perm: bool = None,
        vsc_ids: List[str] = None,
    ):
        self.description = description
        # This parameter is required.
        self.file_system_id = file_system_id
        # This parameter is required.
        self.input_region_id = input_region_id
        self.instance_ids = instance_ids
        # This parameter is required.
        self.mount_point_id = mount_point_id
        self.use_assume_role_chk_server_perm = use_assume_role_chk_server_perm
        self.vsc_ids = vsc_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id

        if self.use_assume_role_chk_server_perm is not None:
            result['UseAssumeRoleChkServerPerm'] = self.use_assume_role_chk_server_perm

        if self.vsc_ids is not None:
            result['VscIds'] = self.vsc_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')

        if m.get('UseAssumeRoleChkServerPerm') is not None:
            self.use_assume_role_chk_server_perm = m.get('UseAssumeRoleChkServerPerm')

        if m.get('VscIds') is not None:
            self.vsc_ids = m.get('VscIds')

        return self

