# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAccessPointRequest(DaraModel):
    def __init__(
        self,
        access_group: str = None,
        access_point_id: str = None,
        access_point_name: str = None,
        enabled_ram: bool = None,
        file_system_id: str = None,
    ):
        # The name of the permission group.
        # 
        # This parameter is required for a General-purpose File Storage NAS (NAS) file system.
        # 
        # The default permission group for virtual private clouds (VPCs) is named DEFAULT_VPC_GROUP_NAME.
        self.access_group = access_group
        # The ID of the access point.
        # 
        # This parameter is required.
        self.access_point_id = access_point_id
        # The name of the access point.
        self.access_point_name = access_point_name
        # Specifies whether to enable the Resource Access Management (RAM) policy. Valid values:
        # 
        # *   true: The RAM policy is enabled.
        # *   false (default): The RAM policy is disabled.
        # 
        # >  After the RAM policy is enabled for access points, no RAM user is allowed to use access points to mount and access data by default. To use access points to mount and access data as a RAM user, you must grant the related access permissions to the RAM user. If the RAM policy is disabled, access points can be anonymously mounted.
        self.enabled_ram = enabled_ram
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group is not None:
            result['AccessGroup'] = self.access_group

        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.access_point_name is not None:
            result['AccessPointName'] = self.access_point_name

        if self.enabled_ram is not None:
            result['EnabledRam'] = self.enabled_ram

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroup') is not None:
            self.access_group = m.get('AccessGroup')

        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('AccessPointName') is not None:
            self.access_point_name = m.get('AccessPointName')

        if m.get('EnabledRam') is not None:
            self.enabled_ram = m.get('EnabledRam')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        return self

